"""Generate the code reference pages and navigation."""

from pathlib import Path

import mkdocs_gen_files

from mkdocs_gen_files.nav import Nav

nav = Nav()

root = Path(__file__).parent.parent
src = root / "src"

for path in src.rglob("*.py"):
    module_path = path.relative_to(src).with_suffix("")
    doc_path = path.relative_to(src).with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
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
                "        filters: ['!^_']\n"
            )
        if module_path.parts[-2:] == ("drivers", "__init__"):
            fd.write("    options:\n        members_order: source\n\n")

    mkdocs_gen_files.set_edit_path(full_doc_path, path.relative_to(root))

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
