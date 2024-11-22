"""Generate the code reference pages and navigation."""

from pathlib import Path
from typing import Tuple

import mkdocs_gen_files

from mkdocs_gen_files.nav import Nav

nav = Nav()

root = Path(__file__).parent.parent
src = root / "src"


def sort_paths(path_object: Path) -> Tuple[int, str]:
    """A helper function to provide a way to sort a list of Path objects.

    This allows for sorting based on the name, but places modules above subpackages.

    Args:
        path_object: A Path object representing a Python module.

    Returns:
        The key to use in the sorting method/function.
    """
    # Count the number of parts in the path minus 1 (to ignore the file itself)
    # This effectively gives us the "depth" of the file
    depth = len(path_object.parts) - 1
    # Sort by depth first, then alphabetically
    return depth, path_object.as_posix().lower()


file_list = sorted(src.rglob("*.py"), key=sort_paths)
for path in file_list:
    module_path = path.relative_to(src).with_suffix("")
    doc_path = path.relative_to(src).with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__" or parts[-1].startswith("_"):
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)  # pylint: disable=invalid-name
        source_link = (
            f'<div class="top-right-link" markdown="1">'
            f'<a href="{{{{ config.repo_url }}}}'
            f'/blob/{{{{ git_ref }}}}/src/'
            f'{"/".join(module_path.parts)}.py">[python source code]</a>'
            f'</div>\n\n'
        )
        fd.write(source_link)
        fd.write(f"::: {ident}\n")
        if module_path.parts[-2:] in {
            ("helpers", "enums"),
            ("helpers", "__init__"),
        }:
            fd.write("    options:\n        show_if_no_docstring: true\n")
        if module_path.parts[-2:] == ("commands", "__init__"):
            fd.write(
                "    options:\n"
                "        inherited_members: false\n"
                "        filters: ['!^_', '^__init__', '^gen_']\n"
                "        members_order: source\n"
                "        merge_init_into_class: false\n"
            )
        elif module_path.parts[1] == "commands":
            fd.write(
                "    options:\n"
                "        inherited_members: false\n"
                "        merge_init_into_class: false\n"
                "        show_inheritance_diagram: false\n"
                "        filters: ['!^_']\n"
            )
        if module_path.parts[-2:] == ("drivers", "__init__"):
            fd.write("    options:\n        members_order: source\n\n")

    mkdocs_gen_files.set_edit_path(full_doc_path, path.relative_to(root))

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
