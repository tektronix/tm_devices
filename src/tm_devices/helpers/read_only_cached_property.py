"""A read-only version of functools.cached_property."""

import contextlib

from functools import cached_property
from typing import TypeVar

_T = TypeVar("_T")

# TODO: Drop Python 3.8: Remove pragmas and exception block when support for Python 3.8 is dropped
try:  # pragma: py-lt-39
    # pylint: disable=unsubscriptable-object,useless-suppression
    class ReadOnlyCachedProperty(cached_property[_T]):  # pyright: ignore[reportRedeclaration]
        """An implementation of cached_property that is read-only.

        Notes:
            In order for the PyCharm IDE to properly provide auto-complete hints, this class must be
            imported in the following way:

            ``from tm_devices.helpers import ReadOnlyCachedProperty as cached_property``.

        Examples:
            >>> from tm_devices.helpers import ReadOnlyCachedProperty
            >>> class ClassWithReadOnlyCachedProperty:
            ...     @ReadOnlyCachedProperty
            ...     def c(self) -> str:
            ...         return "cached value"
        """

        def __set__(self, instance: object, value: _T) -> None:
            """Raise an AttributeError when trying to set the property since it is read-only.

            Raises:
                AttributeError: Indicates that the property is read-only.
            """
            msg = f"{self.attrname} is a read-only attribute"
            raise AttributeError(msg)

        def __delete__(self, instance: object) -> None:
            """Implement the __delete__ method to enable resetting the cache."""
            cache = instance.__dict__
            # Delete the attribute from the cache, ignoring KeyErrors since that just means the
            # attribute already doesn't exist and therefore doesn't need to be deleted.
            with contextlib.suppress(KeyError):
                del cache[self.attrname]  # pyright: ignore[reportArgumentType]

        @property
        def __isabstractmethod__(self) -> bool:
            """Provide a way to check if the decorated method is an abstract method."""
            return getattr(self.func, "__isabstractmethod__", False)

except TypeError:  # pragma: py-gte-39
    # pylint: disable=unsubscriptable-object,useless-suppression
    class ReadOnlyCachedProperty(cached_property):  # pyright: ignore[reportMissingTypeArgument]
        """An implementation of cached_property that is read-only.

        Notes:
            In order for the PyCharm IDE to properly provide auto-complete hints, this class must be
            imported in the following way:

            ``from tm_devices.helpers import ReadOnlyCachedProperty as cached_property``.

        Examples:
            >>> from tm_devices.helpers import ReadOnlyCachedProperty
            >>> class ClassWithReadOnlyCachedProperty:
            ...     @ReadOnlyCachedProperty
            ...     def c(self) -> str:
            ...         return "cached value"
        """

        def __set__(self, instance: object, value: _T) -> None:  # pyright: ignore[reportInvalidTypeVarUse]
            """Raise an AttributeError when trying to set the property since it is read-only.

            Raises:
                AttributeError: Indicates that the property is read-only.
            """
            msg = f"{self.attrname} is a read-only attribute"
            raise AttributeError(msg)

        def __delete__(self, instance: object) -> None:
            """Implement the __delete__ method to enable resetting the cache."""
            cache = instance.__dict__
            # Delete the attribute from the cache, ignoring KeyErrors since that just means the
            # attribute already doesn't exist and therefore doesn't need to be deleted.
            with contextlib.suppress(KeyError):
                del cache[self.attrname]  # pyright: ignore[reportArgumentType]

        @property
        def __isabstractmethod__(self) -> bool:
            """Provide a way to check if the decorated method is an abstract method."""
            return getattr(self.func, "__isabstractmethod__", False)
