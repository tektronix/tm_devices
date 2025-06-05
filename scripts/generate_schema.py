"""Generate the schema file for the tm_devices configuration file.

This script does the following:
    - Downloads the strict json schema that https://www.schemastore.org/json/ provides
    - Installs ajv-cli using npm
    - Generates the schema for the tm_devices configuration file
    - Post-processes the schema to remove unnecessary fields
    - Converts the schema to draft-07
    - Writes the schema to a file
    - Runs a few pre-commit hooks to format the schema file
    - Validates the tm_devices configuration file schema against the strict json schema using ajv
    - Tests the generated schema against samples from the tests/samples/ directory
    _ Validate links within schema
"""

import json
import logging
import os
import platform
import re
import shutil
import subprocess

from pathlib import Path
from typing import Any, Dict, List, Set, Union

import jsonschema
import requests

from dc_schema import (  # pyright: ignore[reportMissingTypeStubs]
    get_schema,  # pyright: ignore[reportUnknownVariableType]
)

from tm_devices.helpers.constants_and_dataclasses import TMDevicesConfigFileSchema

logging.basicConfig(
    level=getattr(logging, os.getenv("LOGGING_LEVEL", "DEBUG")),
    format="[%(asctime)s] [%(levelname)8s] %(message)s",
)
logger = logging.getLogger(__name__)

JSON_METASCHEMA_URL = "https://schemastore.org/metaschema-draft-07-unofficial-strict.json"
JSON_METASCHEMA_FILE = Path(__file__).parents[1] / Path("temp_metaschema.json")
SCHEMA_OUTPUT_FILE = Path(__file__).parents[1] / Path(
    "src/tm_devices/tm_devices_config_schema.json"
)
LOGGING_SPACE_OFFSET = " " * 37
URL_PATTERN = re.compile(r"https?://[^\s)]+")


def download_json_metaschema() -> None:
    """Download the json metaschema and slightly modify it."""
    # Download the file
    response = requests.get(JSON_METASCHEMA_URL, timeout=10)
    response.raise_for_status()  # Check for HTTP errors
    schema_str = response.text
    # Slightly modify the schema to remove an unneeded attribute that causes warnings to be thrown
    schema_str = schema_str.replace("\r\n", "\n").replace('"format": "regex",', "")
    # Remove the type and title requirements, since those don't add much value
    schema_str = schema_str.replace(
        '"required": ["title", "description", "type"]', '"required": ["description"]'
    )
    # Write the file locally, removing an unneeded attribute that causes warnings to be thrown
    JSON_METASCHEMA_FILE.write_text(
        schema_str,
    )


def run_command(
    command: List[str],
    *,
    ignore_errors: bool = False,
    suppress_output: bool = False,
    replace_commas_in_failure_stderr_with_newlines: bool = False,
) -> None:
    """Run a command and log the output.

    Args:
        command: The command to run.
        ignore_errors: Whether to ignore errors and continue running the script.
        suppress_output: Whether to suppress the output of the command.
        replace_commas_in_failure_stderr_with_newlines: Whether to replace commas with newlines in
            the output of the failure stderr.
    """
    logger.debug("Running command: %s", " ".join(command))
    try:
        cmd_result = subprocess.run(  # noqa: S603
            command,
            check=True,
            capture_output=True,
            text=True,  # Ensures output is treated as text strings
        )
        if not suppress_output:
            if cmd_result.stdout.strip():
                logger.debug(
                    "command stdout:\n%s",
                    "\n".join(
                        f"{LOGGING_SPACE_OFFSET}{x}" for x in cmd_result.stdout.strip().splitlines()
                    ),
                )
            if cmd_result.stderr.strip():
                logger.debug(
                    "command stderr:\n%s",
                    "\n".join(
                        f"{LOGGING_SPACE_OFFSET}{x}" for x in cmd_result.stderr.strip().splitlines()
                    ),
                )
    except subprocess.CalledProcessError as e:
        if not (suppress_output and ignore_errors):
            logger.log(
                logging.INFO if ignore_errors else logging.ERROR,
                "Command failed with exit code %d",
                e.returncode,
            )
            if e.stdout.strip():
                logger.log(
                    logging.INFO if ignore_errors else logging.ERROR,
                    "command stdout:\n%s",
                    "\n".join(f"{LOGGING_SPACE_OFFSET}{x}" for x in e.stdout.strip().splitlines()),
                )
            if e.stderr.strip():
                if replace_commas_in_failure_stderr_with_newlines:
                    logger.log(
                        logging.INFO if ignore_errors else logging.ERROR,
                        "command stderr:\n%s",
                        "\n".join(
                            f"{LOGGING_SPACE_OFFSET}{x}"
                            for x in e.stderr.strip().replace(", ", "\n").splitlines()
                        ),
                    )
                else:
                    logger.log(
                        logging.INFO if ignore_errors else logging.ERROR,
                        "command stderr:\n%s",
                        "\n".join(
                            f"{LOGGING_SPACE_OFFSET}{x}" for x in e.stderr.strip().splitlines()
                        ),
                    )
        if not ignore_errors:
            exit_msg = "`" + " ".join(command) + f"` failed with exit code {e.returncode}"
            raise SystemExit(exit_msg)  # noqa: B904


def convert_to_draft_7(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Convert the schema to draft-07.

    Args:
        schema: The schema to convert.

    Returns:
        The converted schema.
    """
    schema["definitions"] = schema["$defs"]
    del schema["$defs"]
    schema["$schema"] = "http://json-schema.org/draft-07/schema#"
    schema["$id"] = (
        "https://raw.githubusercontent.com/tektronix/tm_devices/"
        "main/src/tm_devices/tm_devices_config_schema.json"
    )
    schema_str = json.dumps(schema)
    schema_str = schema_str.replace("/$defs/", "/definitions/")

    return json.loads(schema_str)


def recursively_post_process_schema(  # noqa: C901,PLR0912
    schema: Union[str, Dict[str, Any], List[Dict[str, Any]]],
) -> None:
    """Recursively post-process the schema to remove unnecessary fields.

    Args:
        schema: The schema to post-process.
    """
    if isinstance(schema, dict):
        # Add "additionalProperties": false if not already present
        if schema.get("properties") and schema.get("additionalProperties") is None:
            schema.setdefault("additionalProperties", False)
        # Remove titles from enums
        if schema.get("enum") and schema.get("title"):
            schema.pop("title")
        # Remove empty titles
        if schema.get("title") == "":
            schema.pop("title")

        for key, value in list(schema.items()):
            if key == "allOf" and isinstance(value, list) and len(value) == 1:  # pyright: ignore[reportUnknownArgumentType]
                # Replace the allOf with the single entry
                schema.pop(key)
                schema.update(value[0])  # pyright: ignore[reportUnknownArgumentType]
                # Check for items that need to be marked as an "object"
                if (
                    len(schema) == 1
                    or set(schema.keys()) == {"$ref", "title", "description"}
                    or set(schema.keys()) == {"$ref", "title", "description", "default"}
                ) and (ref_value := schema.get("$ref")) is not None:
                    if ref_value.endswith(("/DeviceTypes", "/ConnectionTypes")):
                        schema["type"] = "string"
                    else:
                        schema["type"] = "object"
            elif key == "enum" and isinstance(value, list):
                # Filter out items that start with "_UNIT_TEST"
                schema[key] = [item for item in value if not str(item).startswith("_UNIT_TEST")]  # pyright: ignore[reportUnknownArgumentType,reportUnknownVariableType]
            else:
                # Recursively apply to nested structures
                recursively_post_process_schema(value)  # pyright: ignore[reportUnknownArgumentType]
    elif isinstance(schema, list):
        for item in schema:
            recursively_post_process_schema(item)


def extract_urls(json_obj: Union[str, List[Any], Dict[str, Any]]) -> Set[str]:
    """Recursively extract URLs from a JSON object.

    Args:
        json_obj: The JSON object to extract URLs from.

    Returns:
        A set of URLs extracted from the JSON object.
    """
    urls: Set[str] = set()
    if isinstance(json_obj, dict):
        for value in json_obj.values():
            if isinstance(value, str):
                urls.update(set(URL_PATTERN.findall(value)))
            else:
                urls.update(extract_urls(value))
    elif isinstance(json_obj, list):
        for item in json_obj:
            urls.update(extract_urls(item))
    return urls


def validate_links_in_json(file_path: Path) -> None:
    """Validate all URLs in a JSON file.

    Args:
        file_path: The JSON file to validate links in.
    """
    json_data = json.loads(file_path.read_text(encoding="utf-8"))
    urls = extract_urls(json_data)
    invalid_links: List[str] = []
    requests_log = logging.getLogger("requests")
    original_requests_log_level = requests_log.level
    urllib3_log = logging.getLogger("urllib3")
    original_urllib3_log_level = urllib3_log.level
    try:
        requests_log.setLevel(logging.WARNING)
        urllib3_log.setLevel(logging.WARNING)
        for url in urls:
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                logger.debug("URL is valid: %s", url)
            except requests.RequestException:  # noqa: PERF203
                logger.debug("URL is invalid or inaccessible: %s", url)
                invalid_links.append(url)
    finally:
        requests_log.setLevel(original_requests_log_level)
        urllib3_log.setLevel(original_urllib3_log_level)

    if invalid_links:
        logger.warning(
            "There are %d invalid/inaccessible links in the created schema file: %s",
            len(invalid_links),
            invalid_links,
        )


def main() -> None:
    """Run the script."""
    # Download and install dependencies
    logger.info("Beginning download of the json metaschema")
    download_json_metaschema()
    logger.info("Finished downloading the json metaschema")
    if not shutil.which("ajv"):
        logger.info("Beginning installation of ajv-cli via npm")
        ajv_install_command = [
            f"npm{'.cmd' if platform.system().upper() == 'WINDOWS' else ''}",
            "install",
            "-g",
            "ajv-cli",
            "--omit=optional",
            "--no-fund",
        ]
        run_command(ajv_install_command)
        logger.info("Finished installing ajv-cli")

    # Create the schema
    logger.info("Generating the schema for the tm_devices configuration file")
    schema_dict = get_schema(TMDevicesConfigFileSchema)  # pyright: ignore[reportUnknownVariableType]

    # Process the schema
    logger.info("Post-processing the schema")
    recursively_post_process_schema(schema_dict)  # pyright: ignore[reportUnknownArgumentType]
    logger.info("Converting the schema to draft-07")
    schema_dict = convert_to_draft_7(schema_dict)  # pyright: ignore[reportUnknownArgumentType]

    # Validate the schema
    logger.info("Validating the schema in-memory")
    jsonschema.Draft202012Validator.check_schema(schema_dict)
    jsonschema.Draft7Validator.check_schema(schema_dict)
    validated_schema_str = json.dumps(schema_dict, indent=4, sort_keys=True)

    # Write the schema to a file
    logger.info("Writing the schema to %s", SCHEMA_OUTPUT_FILE)
    SCHEMA_OUTPUT_FILE.write_text(validated_schema_str + "\n")

    # Validate the generated schema file
    logger.info("Validating the created schema file with ajv")
    ajv_validate_command = [
        f"ajv{'.cmd' if platform.system().upper() == 'WINDOWS' else ''}",
        "-d",
        SCHEMA_OUTPUT_FILE.as_posix(),
        "-s",
        JSON_METASCHEMA_FILE.as_posix(),
        "--strict=false",
        "--spec=draft7",
        "--all-errors",
        "--errors=text",
    ]
    run_command(ajv_validate_command, replace_commas_in_failure_stderr_with_newlines=True)

    # Validate the links in the generated schema file
    logger.info("Validating the links in the created schema file")
    validate_links_in_json(SCHEMA_OUTPUT_FILE)
    logger.info("Finished validating the links in the created schema file")

    # Test the generated schema file
    logger.info(
        "Testing the generated schema file against samples from the tests/samples/ directory"
    )
    sample_file_dir = Path(__file__).parents[1] / "tests/samples"
    for ajv_test_file, expected_status in (
        (sample_file_dir / "sample_devices.yaml", "valid"),
        (sample_file_dir / "simulated_config_no_cleanup.yaml", "invalid"),
        (sample_file_dir / "simulated_config_no_devices.yaml", "valid"),
        (sample_file_dir / "unsupported_device_type_config.yaml", "valid"),
        (sample_file_dir / "invalid_config_option.yaml", "invalid"),
    ):
        ajv_test_cmd = [
            f"ajv{'.cmd' if platform.system().upper() == 'WINDOWS' else ''}",
            "test",
            "-s",
            SCHEMA_OUTPUT_FILE.as_posix(),
            "--strict=false",
            "--spec=draft7",
            "--all-errors",
            "--errors=text",
            "-d",
            ajv_test_file.as_posix(),
            f"--{expected_status}",
        ]
        logger.info("Testing against %s, expected to be %s", ajv_test_file, expected_status)
        run_command(ajv_test_cmd, replace_commas_in_failure_stderr_with_newlines=True)
        logger.info("Test passed, %s is %s", ajv_test_file, expected_status)

    logger.info("Successfully generated the schema for the tm_devices configuration file")


if __name__ == "__main__":
    main()
