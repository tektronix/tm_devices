"""Get a complete list of all auto-generated commands."""

import glob
import importlib
import json
import os

from pathlib import Path
from typing import List, Set

import pytest

from tm_devices import commands

with open(Path(__file__).parent / "auto_gen_cmds_list.json", encoding="utf-8") as file_pointer:
    json_dict = json.load(file_pointer)
MASTER_COMMAND_SET: Set[str] = set(json_dict["commands"])


def get_driver_command_list() -> List[str]:
    """Return a list of all auto-generated files with command definitions."""
    commands_dir = Path(commands.__file__).parent
    auto_generated_file_list = [Path(x) for x in glob.glob(f"{commands_dir}/**", recursive=True)]
    auto_generated_file_list = list(
        filter(
            lambda x: x.is_file()
            and x.suffix == ".py"  # Only grab python files
            and not x.name.endswith("_commands.py")  # These files don't contain any command classes
            and x.name != "__init__.py",  # These files don't contain any command classes
            auto_generated_file_list,
        )
    )

    command_list: List[str] = []
    for file_name in auto_generated_file_list:
        # Create an importable string
        module_import_path = str(file_name).rsplit("tm_devices", maxsplit=1)[-1]
        module_import_path = "tm_devices" + module_import_path.split(".")[0].replace(
            os.path.sep, "."
        )
        # Import the module
        module = importlib.import_module(module_import_path)
        # Get the docstring of the module
        docstring = str(module.__doc__)
        # Add to the list of commands, convert known substrings to the proper format
        command_list.extend(
            list(
                {
                    x.strip().split()[1].rstrip("?")
                    for x in docstring.split("\n")
                    if x.strip().startswith("-")
                }
            )
        )
    return command_list


@pytest.mark.xfail(reason="The auto-generated code docstrings need to be updated")
def test_auto_generated_commands() -> None:
    """Verify all auto-generated commands are valid.

    This test isn't perfect because it only tests that the module docstrings contain valid commands,
    but it is the only easy way to validate the auto-generated command modules.
    """
    assert set(get_driver_command_list()).issubset(MASTER_COMMAND_SET)
