# pylint: disable=invalid-name
"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full list see the
documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import re
import shutil
import sys

from importlib.metadata import metadata
from pathlib import Path
from typing import List

from autoapi.mappers.python.objects import PythonPythonMapper  # type: ignore[import]
from jinja2.environment import Environment as JinjaEnvironment
from sphinx.application import Sphinx
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

SKIP_API_GEN = os.getenv("SKIP_TM_DEVICES_API_GENERATION") is not None


disable_warnings(InsecureRequestWarning)
sys.path.insert(0, Path(__file__).parent.as_posix())

# -- Project information -----------------------------------------------------
project = "tm_devices"
package_data = metadata(project)
author = package_data["Author"]
# noinspection PyShadowingBuiltins
copyright = f"2022, {author}"  # noqa: A001

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    # "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    "autoapi.extension",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.duration",
    "sphinx.ext.todo",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.graphviz",
    "sphinx.ext.githubpages",
    "sphinxcontrib.jquery",
    "sphinxcontrib.mermaid",
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "sphinx_tippy",
    "notfound.extension",
    "sphinx_toolbox.github",
    "sphinx_toolbox.sidebar_links",
    "sphinx_toolbox.collapse",
    "sphinx_toolbox.more_autodoc.generic_bases",
    "sphinx_toolbox.more_autodoc.overloads",
    "gfm_include_replace",  # local extension that enables including a file with text replacement
]
if sys.version_info >= (3, 9):
    extensions.append("sphinx_remove_toctrees")
remove_from_toctrees = [
    "_autoapi/tm_devices/*",
    "_autoapi/tm_devices/**/*",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
templates_path = ["_templates"]
tls_verify = False
nitpicky = False  # TODO: change this to `True`
github_username = author.lower()
github_repository = project
# -- Options for extlinks -----------------------------------------------------
extlinks_detect_hardcoded_links = True
extlinks = {
    "repo_url": (
        "https://github.com/tektronix/tm_devices/blob/main/%s",
        "%s",
    )
}


# -- Options for autoapi/autodoc/autosummary-----------------------------------
LINK_OBJS_DELIMS = r"(\s*[\[\]\(\),]\s*)"
LINK_OBJS_DELIMS_RE = re.compile(LINK_OBJS_DELIMS)


def _link_objs(value: str) -> str:
    """Create a python object link.

    Args:
        value: The object name to use to create the link.

    Returns:
        The object link.
    """
    result = ""

    sub_targets = re.split(LINK_OBJS_DELIMS, value.strip())
    for target in sub_targets:
        sub_target = target.strip()
        if LINK_OBJS_DELIMS_RE.match(sub_target):
            result += f"{sub_target}"
            if sub_target.endswith(","):
                result += " "
            else:
                result += "\\ "
        elif sub_target:
            result += f":py:obj:`~{sub_target}`\\ "

    # Strip off the extra "\ "
    return result[:-2]


def prep_jinja_env(jinja_env: JinjaEnvironment) -> None:
    """Prepare the Jinja environment.

    Args:
        jinja_env: The Jinja environment.
    """
    jinja_env.filters["link_objs_custom"] = _link_objs  # pyright: ignore[reportUnknownMemberType]


autoapi_prepare_jinja_env = prep_jinja_env
autoapi_template_dir = "_templates/autoapi"
autoapi_generate_api_docs = True
autoapi_add_toctree_entry = True
napoleon_preprocess_types = True
autoapi_root = "_autoapi"
autoapi_keep_files = True
autoapi_dirs = ["../src"]
autoapi_ignore = [
    # "*/commands/*",
]
autoapi_member_order = "alphabetical"
autodoc_member_order = "alphabetical"
autodoc_inherit_docstrings = True
autodoc_typehints = "both"
autodoc_typehints_format = "short"
autodoc_class_signature = "separated"
autoapi_python_class_content = "class"
autoclass_content = "class"
# FUTURE # autoapi_own_page_level = "module"  # TODO: investigate after sphinx-autoapi==3.1.x
autoapi_options = [
    "members",
    # "inherited-members",  # commenting this out significantly reduces documentation build time
    # "undoc-members",  # we don't want to include these
    # "private-members",  # we don't want to include these
    # "special-members",  # we don't want to include these
    "show-inheritance",
    "show-module-summary",
    # FUTURE # "imported-members",
]
# This requires Graphviz to be installed, https://graphviz.org/
if shutil.which("dot"):
    autoapi_options.append("show-inheritance-diagram")

# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_show_sourcelink = False
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["theme_overrides.css"]
html_js_files = ["insert-br.js"]
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": True,
}
html_favicon = "_static/favicon_readthedocs.png"
intersphinx_mapping = {  # pylint: disable=consider-using-namedtuple-or-dataclass
    "python": ("https://docs.python.org/3/", None),
    "pyvisa": ("https://pyvisa.readthedocs.io/en/latest/", None),
    "packaging": ("https://packaging.pypa.io/en/stable/", None),
    "requests": ("https://docs.python-requests.org/en/latest/", None),
}
notfound_context = {
    "title": "Page Not Found",
    "body": """
<h1>Page Not Found</h1>

<p>Sorry, we couldn't find that page.</p>

<p>Try using the search box or go to the homepage.</p>
""",
}

# -- Options for docstring coverage ------------------------------------------
coverage_show_missing_items = True
coverage_ignore_modules = [
    "^.*_commands$",
]

# -- Options for MyST --------------------------------------------------------
myst_heading_anchors = 4
myst_enable_extensions = [
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_image",
    "replacements",
    "strikethrough",
    "tasklist",
]

# -- Options for tippy -------------------------------------------------------
tippy_rtd_urls = [
    "https://www.sphinx-doc.org/en/master/",
    "https://py-pkgs-cookiecutter.readthedocs.io/en/latest/",
    "https://cookiecutter.readthedocs.io/en/latest/",
    "https://pyvisa.readthedocs.io/projects/pyvisa-py/en/latest/",
    "https://pyvisa.readthedocs.io/en/latest/",
    "https://python-semantic-release.readthedocs.io/en/latest/",
    "https://docs.pytest.org/en/latest/",
    "https://pytest-cov.readthedocs.io/en/latest/",
    "https://pytest-html.readthedocs.io/en/latest/",
    "https://pyvisa.readthedocs.io/projects/pyvisa-sim/en/latest/",
]
tippy_anchor_parent_selector = "div.document"

# -- Options for mermaid -----------------------------------------------------
mermaid_params = ["-p", "puppeteer-config.json"]


# -- Sphinx setup functions --------------------------------------------------


def skip_member(
    app: Sphinx,  # noqa: ARG001
    what: str,
    name: str,
    obj: PythonPythonMapper,
    skip: bool,
    options: List[str],  # noqa: ARG001
) -> bool:
    """Skip certain members of the API.

    Skips the subpackage which contains all the commands inner classes.

    Args:
        app: The Sphinx application object.
        what: The type of the object which the docstring belongs to.
            This can be one of: "attribute", "class", "data", "exception",
            "function", "method", "module", "package".
        name: The fully qualified name of the object.
        obj: The object itself.
        skip: Whether AutoAPI will skip this member if the handler does not override the decision.
        options: The options given to the directive.

    Returns:
        A boolean indicating if the member should be skipped.
    """
    if (
        what == "module"
        or f"{os.path.sep}commands{os.path.sep}" in obj.pathname
        or obj.pathname.endswith(f"{os.path.sep}commands")
        or ("_commands" in name and "ieee" not in name)
    ):
        skip = True
    return skip or SKIP_API_GEN


def setup(sphinx: Sphinx) -> None:
    """Set up the Sphinx tool.

    Args:
        sphinx: The sphinx object.
    """
    sphinx.connect("autoapi-skip-member", skip_member)  # pyright: ignore[reportUnknownMemberType]
