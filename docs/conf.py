# pylint: disable=invalid-name
"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full list see the
documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
import os
import shutil

from importlib.metadata import metadata
from typing import Any, List, Sequence

from autoapi.mappers.python.objects import PythonPythonMapper  # type: ignore[import]
from jinja2.environment import Environment as JinjaEnvironment
from sphinx.application import Sphinx
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

disable_warnings(InsecureRequestWarning)

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
    "autoapi.extension",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
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
# rst_prolog = """
# .. role:: apisummarylabel
# """
# -- Options for extlinks -----------------------------------------------------
extlinks_detect_hardcoded_links = True
extlinks = {
    "repo_url": (
        "https://github.com/tektronix/tm_devices/blob/main/%s",
        "%s",
    )
}


# -- Options for autoapi/autodoc ---------------------------------------------
def item_in_sequence(sequence: Sequence[Any], item: Any) -> bool:
    """Check if an item is in a sequence."""
    return item in sequence


def prep_jinja_env(jinja_env: JinjaEnvironment) -> None:
    """Prepare the Jinja environment.

    Args:
        jinja_env: The Jinja environment.
    """
    jinja_env.tests["contains"] = item_in_sequence  # pyright: ignore


# FUTURE: # autoapi_prepare_jinja_env = prep_jinja_env
# FUTURE: # autoapi_template_dir = "_templates/autoapi"
autoapi_root = "_autoapi"
autoapi_keep_files = True
autoapi_dirs = ["../src"]
autoapi_member_order = "alphabetical"
autodoc_member_order = "alphabetical"
autoapi_ignore = [
    "*migrations*",
]
autoapi_modules = {
    "tm_devices": {
        "prune": True,
    }
}
autoapi_options = [
    "members",
    "undoc-members",
    "special_members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
    # "inherited-members",  # commenting this out significantly reduces documentation build time
]
autodoc_typehints = "both"
autodoc_typehints_format = "short"
autodoc_class_signature = "separated"
autoapi_python_class_content = "class"
autoclass_content = "class"
autoapi_generate_api_docs = True
# This requires Graphviz to be installed, https://graphviz.org/
if shutil.which("dot"):
    autoapi_options.append("show-inheritance-diagram")

# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["theme_overrides.css"]
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
intersphinx_disabled_reftypes = ["*"]

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
    app: Sphinx, what: str, name: str, obj: PythonPythonMapper, skip: bool, options: List[str]
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
    _package_set = {"tm_devices", "commands", "components", "driver_mixins", "drivers", "helpers"}
    _ = app
    _ = name
    _ = options
    if (
        what == "module"  # pylint: disable=too-many-boolean-expressions
        or (
            what == "package" and obj.short_name not in _package_set  # pyright: ignore [reportUnknownMemberType]
        )
        or f"{os.path.sep}commands{os.path.sep}" in obj.pathname
        or obj.pathname.endswith(f"{os.path.sep}commands")
        or ("_commands" in name and "ieee" not in name)
    ):
        skip = True

    return skip or os.getenv("SKIP_TM_DEVICES_API_GENERATION") is not None


def setup(sphinx: Sphinx) -> None:
    """Set up the Sphinx tool.

    Args:
        sphinx: The sphinx object.
    """
    sphinx.connect("autoapi-skip-member", skip_member)  # pyright: ignore
