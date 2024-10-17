# pyright: reportInvalidTypeVarUse=none
"""A mixin class providing class methods for expanding a class with decorators."""

from functools import cached_property, wraps
from typing import Callable, Optional, overload, Type, TypeVar, Union

from typing_extensions import Concatenate, ParamSpec

# bound is used to allow anything that subclasses from Device
_EM = TypeVar("_EM", bound="_ExtendableMixin")
_T = TypeVar("_T")
_P = ParamSpec(
    "_P",
)


class _ExtendableMixin:
    """A mixin class which adds methods for expanding a class."""

    ################################################################################################
    # Class Methods
    ################################################################################################
    @classmethod
    def add_method(
        cls: Type[_EM],
        method: Callable[Concatenate[_EM, _P], _T],
    ) -> None:
        """Add a method to the class.

        This class method is best used as a decorator on functions in order to add them to a class.

        Examples:
            >>> from tm_devices.drivers.device import Device
            >>>
            >>> @Device.add_method
            ... def print_hello(self: Device, var: str):
            ...     print("Hello World!")
            ...     print(f"I am a {self.__class__.__name__}!")
            ...     print(f"My var is {var}")

        Args:
            method: The method to add to the class.
        """
        setattr(cls, method.__name__, method)

        # Helper code to modify stub (.pyi) files
        # pylint: disable=import-outside-toplevel
        from tm_devices.helpers.stubgen import add_info_to_stub

        add_info_to_stub(cls, method)

    @classmethod
    @overload
    def add_property(
        cls: Type[_EM],
        method: Callable[Concatenate[_EM, _P], _T],
    ) -> None: ...  # pragma: no cover

    @classmethod
    @overload
    def add_property(
        cls: Type[_EM],
        method: None = None,
        /,
        *,
        is_cached: bool = False,
    ) -> Callable[[Callable[Concatenate[_EM, _P], _T]], None]: ...  # pragma: no cover

    @classmethod
    def add_property(  # pyright: ignore[reportInconsistentOverload]
        cls: Type[_EM],
        method: Optional[Callable[[_EM], _T]] = None,
        /,
        *,
        is_cached: bool = False,
    ) -> Optional[Callable[[Callable[[_EM], _T]], None]]:
        """Add a property to the class.

        This class method is best used as a decorator on functions in order to add them to a class.

        Examples:
            >>> from tm_devices.drivers.device import Device
            >>>
            >>> @Device.add_property
            ... def foo(self: Device):
            ...     return "bar"
            >>>
            >>> @Device.add_property(is_cached=True)
            ... def foo(self: Device):
            ...     return self.name + self.address

        Args:
            method: The property to add to the class.
            is_cached: Whether the property is only evaluated once and cached.
        """

        @wraps(method)  # type: ignore[arg-type]
        def wrap(function: Callable[[_EM], _T]) -> None:
            """Wrap function in property class and attach that function to class."""
            func: Union[property, cached_property[_T]]
            if is_cached:
                func = cached_property(function)
                func.__set_name__(owner=cls, name=function.__name__)
            else:
                func = property(function)
            setattr(cls, function.__name__, func)

            # Helper code to modify stub (.pyi) files
            # pylint: disable=import-outside-toplevel
            from tm_devices.helpers.stubgen import add_info_to_stub

            add_info_to_stub(cls, function, is_property=True)

        # Handle being called as @add_property() with parens.
        if method is None:
            return wrap  # pyright: ignore[reportUnknownVariableType]

        # called as @add_property without parens.
        return wrap(method)
