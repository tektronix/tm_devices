"""Helper functions for adding to previously generated stub files."""
import inspect
import os
import re

from typing import Any, List

_TYPING_IMPORT_REGEX = re.compile(r"typing\.([a-zA-Z]+)")


def _get_data_type(data_object: Any) -> str:
    """Get the data type of the given object.

    Args:
        data_object: The object to get the data type for.
    """
    try:
        if "." in str(data_object):
            raise AttributeError
        data_type = str(data_object.__name__) if data_object else str(data_object)
    except AttributeError:
        data_type = str(
            re.sub(r"(?:[a-z0-9_]+\.)+", "", str(data_object)).replace("NoneType", "None")
        )
        data_type = data_type.replace("<class '", "").replace("'>", "")
    return data_type


# pylint: disable=too-many-locals
def add_info_to_stub(cls: Any, method: Any, is_property: bool = False) -> None:  # noqa: C901
    """Add information to a stub file.

    This method requires that an environment variable named ``TM_DEVICES_STUB_DIR`` is defined that
    points to the stub directory for ``tm_devices``.

    Args:
        cls: The class object that the method is being added to.
        method: The method to add to a stub.
        is_property: A boolean indicating the method is a property.

    Raises:
        AssertionError: Indicates that the file that needs to be updated does not exist.
    """
    if stub_dir := os.getenv("TM_DEVICES_STUB_DIR"):
        method_filepath = inspect.getfile(cls)
        stub_dir = (
            os.path.join(stub_dir, "tm_devices")
            if not stub_dir.endswith("tm_devices")
            else stub_dir
        )
        method_filepath = os.path.join(
            stub_dir, method_filepath.rsplit("tm_devices", maxsplit=1)[-1].lstrip(os.path.sep)
        )
        method_filepath += "i"  # stub files have the .pyi extension
        if not os.path.exists(method_filepath):
            msg = (
                f'The stub file "{method_filepath}" must already exist in order to use this '
                f"functionality to add method stubs."
            )
            raise AssertionError(msg)
        # Create the signature of the new method
        argspec = inspect.getfullargspec(method)
        parameters: List[str] = []
        for param in inspect.signature(method).parameters.values():
            if (param_sig := param.name) != "self":
                param_sig += ": " + _get_data_type(param.annotation)
                if param.default != param.empty:
                    if isinstance(param.default, str):
                        param_value = f'"{param.default}"'
                    else:
                        param_value = str(param.default)
                    param_sig += " = " + param_value
            parameters.append(param_sig)
        if not parameters:
            parameters.append("self")
        # Check if any imports need to be added
        typing_imports = set(_TYPING_IMPORT_REGEX.findall(str(argspec)))

        method_signature = (
            f"    def {method.__name__}({', '.join(parameters)}) -> "
            f"{_get_data_type(argspec.annotations.get('return'))}:\n"
        )
        if is_property:
            method_signature = "    @property\n" + method_signature
        method_stub_content = method_signature + "        " + '"""' + method.__doc__ + '"""' + "\n"
        # Read in the content of the stub file to avoid adding duplicate methods
        with open(method_filepath, encoding="utf-8") as file_pointer:
            contents = file_pointer.read()
        if f" def {method.__name__}(" not in contents:
            contents += method_stub_content
            if typing_imports:
                contents = f"from typing import {', '.join(typing_imports)}\n" + contents
            with open(method_filepath, "w", encoding="utf-8") as file_pointer:
                file_pointer.write(contents)
