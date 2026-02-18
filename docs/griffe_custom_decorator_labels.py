"""Add labels to items decorated with custom decorators from this package.

This will cause them to be classified correctly when the documentation is built.
"""

from griffe import Extension, stdlib_decorators  # pyright: ignore[reportMissingTypeStubs]


class CustomDecoratorLabels(Extension):
    """A griffe extension that adds labels to items decorated with custom decorators."""

    def __init__(self) -> None:
        """Initialize the extension and add the labels to the stdlib_decorators mapping."""
        # Note: this is a hack, add an item to the `stdlib_decorators` dictionary as a side effect
        # when instantiating the extension to cause decorated methods to be classified correctly.
        stdlib_decorators["tm_devices.helpers.read_only_cached_property.ReadOnlyCachedProperty"] = {
            "cached",
            "property",
        }
        stdlib_decorators["tm_devices.helpers.ReadOnlyCachedProperty"] = {
            "cached",
            "property",
        }
