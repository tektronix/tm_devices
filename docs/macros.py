"""Macros for the documentation."""

import inspect
import os
import pathlib
import re

from importlib import import_module
from typing import Any, Generator, Optional, Set, Tuple

import tomli

from mkdocs_macros.plugin import MacrosPlugin  # pyright: ignore[reportMissingTypeStubs]

HEADER_ONE_REGEX = re.compile(r"^#\s(.+)$", re.MULTILINE)
PAGE_REPLACEMENTS = {
    "index.md": (
        (" AFGs ", r" [AFGs](default:AFG) "),
        (" AWGs ", r" [AWGs](default:AFG) "),
        (" Scopes ", r" [Scopes](default:Scope) "),
        (" PSUs ", r" [PSUs](default:PSU) "),
        (" SMUs ", r" [SMUs](default:SMU) "),
        (" MTs ", r" [MTs](default:MT) "),
        (" DMMs ", r" [DMMs](default:DMM) "),
        (" DAQs ", r" [DAQs](default:DAQ) "),
        (" SSs ", r" [SSs](default:SS) "),
        (" PI ", " <PI:>"),
        (" TSP ", " <TSP:>"),
        (" API ", " <API:>"),
        (" DPOJET ", " <DPOJET:>"),
        (" ✅ ", " [](default:✅) "),
        (" 🚧 ", " [](default:🚧) "),
        (" ❌ ", " [](default:❌) "),
        (r"> [!TIP]", "!!! tip"),
        (
            "> Visit the [Glossary",
            "    Hover over a link or icon to see its definition, or visit the [Glossary",
        ),
        ("(https://tinyurl.com/tek-tm-devices/docs/glossary.md)", "(./glossary.md)"),
        ("(https://tinyurl.com/tek-tm-devices/CODE_OF_CONDUCT.md)", "(./CODE_OF_CONDUCT.md)"),
        ("(https://tinyurl.com/tek-tm-devices/CONTRIBUTING.md)", "(./CONTRIBUTING.md)"),
        ("(https://tinyurl.com/tek-tm-devices/LICENSE.md)", "(./LICENSE.md)"),
    ),
}
FILES_TO_REMOVE_BLACK_FORMATTER_DISABLE_COMMENT = {
    "configuration.md",
    "basic_usage.md",
}


####################################################################################################
# Helper functions
####################################################################################################
def import_object(objname: str) -> Any:
    """Import a python object by its qualified name.

    Args:
        objname: The fully qualified name of the object.

    Returns:
        The imported object.

    Raises:
        ImportError: The object could not be imported.
    """
    try:
        objpath = objname.split(".")
        modname = objpath.pop(0)
        obj = import_module(modname)
        for name in objpath:
            modname += "." + name
            try:
                obj = getattr(obj, name)
            except AttributeError:
                obj = import_module(modname)
        return obj  # noqa: TRY300
    except (AttributeError, ImportError) as exc:
        msg = f"Could not import {objname}: {exc}"
        raise ImportError(msg) from exc


def get_classes(*cls_or_modules: str, strict: bool = False) -> Generator[Any, None, None]:
    """Get all classes from a tuple of classes or modules.

    Args:
        cls_or_modules: A tuple of classes or modules.
        strict: A boolean indicating to only consider classes that are strictly defined in that
            module and not imported from somewhere else.

    Yields:
        Each class that is found.

    Raises:
        ValueError: If any of the classes or modules are invalid.
    """
    for cls_or_module in cls_or_modules:
        obj = import_object(cls_or_module)

        if inspect.isclass(obj):
            yield obj

        elif inspect.ismodule(obj):
            for obj_ in obj.__dict__.values():
                if inspect.isclass(obj_) and (
                    not strict or obj_.__module__.startswith(obj.__name__)
                ):
                    yield obj_
        else:
            msg = f"{cls_or_module} is not a class nor a module"
            raise ValueError(msg)


####################################################################################################
# Macro functions
####################################################################################################
def class_diagram(
    *cls_or_modules: str,
    full: bool = False,
    strict: bool = False,
    namespace: Optional[str] = None,
) -> str:
    """Create a mermaid classDiagram for the provided classes or modules.

    Args:
        cls_or_modules: A tuple of classes or modules.
        full: A boolean indicating to show the complete class hierarchy.
        strict: A boolean indicating to only consider classes that are strictly defined in that
            module and not imported from somewhere else.
        namespace: Limits the diagram to only include classes defined in this namespace.

    Returns:
        The mermaid code block with complete syntax for the classDiagram.

    Raises:
        ValueError: If no classDiagram can be created.
    """
    inheritances: Set[Tuple[str, str]] = set()

    def get_tree(cls: Any) -> None:
        for base in cls.__bases__:
            if base.__name__ == "object":
                continue
            if namespace and not base.__module__.startswith(namespace):
                continue
            inheritances.add((base.__name__, cls.__name__))
            if full:
                get_tree(base)

    for cls_item in get_classes(*cls_or_modules, strict=strict):
        get_tree(cls_item)

    if not inheritances:
        msg = "No class hierarchy can be created."
        raise ValueError(msg)

    return (
        "```mermaid\nclassDiagram\n"
        + "\n".join(f"  {a} <|-- {b}" for a, b in sorted(inheritances))
        + "\n```"
    )


def create_repo_link(link_text: str, base_repo_url: str, relative_repo_path: str) -> str:
    """Create a Markdown link to a specific location in the remote repository.

    Args:
        link_text: The text to show in the Markdown link.
        base_repo_url: The base URL of the repository.
        relative_repo_path: The relative path to the location to link to in the remote repository.
    """
    return f"[{link_text}]({base_repo_url}/blob/main/{relative_repo_path})"


####################################################################################################
# Mkdocs Macros functions
####################################################################################################
def define_env(env: MacrosPlugin) -> None:
    """Define variables, macros and filters.

    Notes:
        - variables: the dictionary that contains the environment variables
        - macro: a decorator function, to declare a macro.
        - filter: a function with one of more arguments,
            used to perform a transformation
    """
    # Read in the current package version number to use in templates and files
    with open(
        pathlib.Path(f"{pathlib.Path(__file__).parents[1]}") / "pyproject.toml", "rb"
    ) as file_handle:
        pyproject_data = tomli.load(file_handle)
        package_version = "v" + pyproject_data["tool"]["poetry"]["version"]
    git_ref = "main" if os.getenv("READTHEDOCS_VERSION") == "latest" else package_version

    # Add a variable that points to the latest version of the package
    env.variables["package_version"] = package_version
    # Add a variable that points to either the latest version tag or the main branch depending
    # on where/when the docs are being built.
    env.variables["git_ref"] = git_ref
    # Add the auto_class_diagram macro
    env.macro(class_diagram, "auto_class_diagram")  # pyright: ignore[reportUnknownMemberType]
    # Add the create_repo_link macro
    env.macro(create_repo_link, "create_repo_link")  # pyright: ignore[reportUnknownMemberType]


def on_post_page_macros(env: MacrosPlugin) -> None:
    """Post-process pages."""
    # Check if there are any replacements to perform on the page
    if env.page.file.src_path in PAGE_REPLACEMENTS:  # pyright: ignore[reportUnknownMemberType]
        for search, replace in PAGE_REPLACEMENTS[env.page.file.src_path]:  # pyright: ignore[reportUnknownMemberType]
            env.markdown = env.markdown.replace(search, replace)  # pyright: ignore[reportUnknownMemberType]
    # Check if all black format disable comments should be removed from the page
    if env.page.file.src_path in FILES_TO_REMOVE_BLACK_FORMATTER_DISABLE_COMMENT:  # pyright: ignore[reportUnknownMemberType]
        env.markdown = env.markdown.replace("# fmt: off\n", "")  # pyright: ignore[reportUnknownMemberType]
    # Check if the title is correct
    if actual_title_match := HEADER_ONE_REGEX.search(env.markdown):  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
        actual_title = actual_title_match.group(1)
        if env.page.title != actual_title:  # pyright: ignore[reportUnknownMemberType]
            env.page.title = actual_title  # pyright: ignore[reportUnknownMemberType]
