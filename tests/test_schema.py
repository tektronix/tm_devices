"""Test the official JSON schema for the tm_devices config file."""

import json

from pathlib import Path

import pytest
import tomli
import yaml

from jsonschema import validate, ValidationError

import tm_devices

SCHEMA_FILE = Path(tm_devices.__file__).parent / "tm_devices_config_schema.json"
SCHEMA_DICT = json.loads(SCHEMA_FILE.read_text(encoding="utf-8"))
SAMPLE_FILE_DIR = Path(__file__).parent / "samples/"


@pytest.mark.parametrize(
    ("filename", "expected_passing"),
    [
        ("sample_devices.yaml", True),
        ("sample_devices.toml", True),
        ("simulated_config_no_cleanup.yaml", False),
        ("simulated_config_no_devices.yaml", True),
        ("unsupported_device_type_config.yaml", True),
        ("invalid_config_option.yaml", False),
        ("invalid_sample_devices.yaml", False),
    ],
)
def test_schema(filename: str, expected_passing: bool) -> None:
    """Verify the JSON schema correctly validates config files.

    Args:
        filename: The name of the config file to test.
        expected_passing: Whether the config file should pass validation.
    """
    config_file = SAMPLE_FILE_DIR / filename
    config_file_contents = config_file.read_text(encoding="utf-8")

    # Load the file based on its extension
    if config_file.suffix == ".toml":
        contents = tomli.loads(config_file_contents)
    else:
        contents = yaml.safe_load(config_file_contents)

    # Validate the loaded content against the schema
    if expected_passing:
        try:
            validate(instance=contents, schema=SCHEMA_DICT)
        except ValidationError as e:
            msg = f"Validation failed for {config_file}: {e}"
            raise AssertionError(msg) from e
    else:
        with pytest.raises(ValidationError):
            validate(instance=contents, schema=SCHEMA_DICT)
