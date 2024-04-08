"""An extension for including GitHub Flavored Markdown files with text replacement."""

import re

from typing import cast, List

from docutils import nodes, utils
from docutils.parsers.rst import Directive, directives
from myst_parser.parsers.docutils_ import Parser
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

GFM_ADMONITION_PATTERN = re.compile(r"> \\\[!([A-Z]+)\\]")


class GFMIncludeReplaceDirective(Directive):
    """A directive which includes a file but adds search and replace functionality.

    This directive also processes GitHub Flavored Markdown admonitions into MyST admonitions.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {  # noqa: RUF012
        "replace": directives.unchanged,
    }

    def run(self) -> List[nodes.Node]:  # pylint: disable=too-many-locals
        """Run the directive.

        This will include the file contents, then search and replace text as
        defined in the directive. This directive also processes GitHub Flavored Markdown admonitions
        into MyST admonitions.

        Returns:
            All the directive's nodes.
        """
        settings = self.state.document.settings
        # noinspection PyUnresolvedReferences
        env = cast(BuildEnvironment, self.state.document.settings.env)  # pyright: ignore[reportUnknownMemberType]
        filename = self.arguments[0]
        replace_rules_str = self.options.get("replace", "")
        replace_rules = [rule.split("->") for rule in replace_rules_str.split(";")]

        # Resolve the path relative to the source directory
        rel_filename, filename = env.relfn2path(filename)
        env.note_dependency(rel_filename)

        try:
            with open(filename, encoding="utf-8") as file:
                content = ""

                # Replace GFM admonitions with MyST admonitions
                # - https://github.com/orgs/community/discussions/16925
                # - https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html
                tracking_admonition = False
                for line in file:
                    new_line = line.rstrip()
                    if new_line.startswith("> \\["):
                        tracking_admonition = True
                        new_line = GFM_ADMONITION_PATTERN.sub(r"```{\1}", new_line).lower()
                    elif new_line.startswith("> "):
                        new_line = new_line.lstrip("> ")
                    else:
                        if tracking_admonition:
                            new_line += "```\n"
                        tracking_admonition = False
                    content += new_line + "\n"

            # Perform the search and replace
            for rule in replace_rules:
                # Check to make sure both a search item and replace item were provided
                if len(rule) == 2:  # noqa: PLR2004
                    content = content.replace(rule[0], rule[1])

            # Use the custom parser specified in the directive options
            document = utils.new_document(filename, settings)
            parser = Parser()
            parser.parse(content, document)
            # clean up doctree and complete parsing
            document.transformer.populate_from_components((parser,))
            document.transformer.apply_transforms()
            return document.children  # noqa: TRY300
        except Exception as e:  # noqa: BLE001
            message = f"Error including file {filename}: {e!s}"
            raise self.error(message) from e


def setup(app: Sphinx) -> None:
    """Set up the Sphinx application to add the new directive."""
    app.add_directive("gfm-include-replace", GFMIncludeReplaceDirective)
