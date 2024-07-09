"""Module containing helper mixins for dataclasses."""

import operator

from enum import Enum
from typing import Any, Dict, TYPE_CHECKING

from tm_devices.helpers.enums import CustomStrEnum

if TYPE_CHECKING:
    from collections.abc import ItemsView


# pylint: disable=too-few-public-methods
class AsDictionaryMixin:
    """Functionality for a class's public attributes to get cast to a dictionary."""

    # reference:
    # https://realpython.com/inheritance-composition-python/#mixing-features-with-mixin-classes
    def to_dict(self, ignore_none: bool = False, sort_keys: bool = True) -> Dict[str, Any]:
        """Transform public attributes of this class to dictionary.

        Examples:
            >>> import dataclasses
            >>> from tm_devices.helpers.dataclass_mixins import AsDictionaryMixin
            >>> ClassA = dataclasses.make_dataclass("A",["a","_b", "c"], bases=(AsDictionaryMixin,))
            >>> foo = ClassA("public", "secret", 5)
            >>> foo.to_dict()
            {'a': 'public', 'c': 5}
            >>> vars(foo)  # see how this differs from the builtin function vars
            {'a': 'public', '_b': 'secret', 'c': 5}
        """
        self_vars: ItemsView[str, Any] = vars(self).items()
        return {
            prop: self._represent(value, ignore_none=ignore_none, sort_keys=sort_keys)
            for prop, value in (
                self_vars if not sort_keys else sorted(self_vars, key=operator.itemgetter(0))
            )
            if not (prop.startswith("_") or (ignore_none and value is None))
        }

    @staticmethod
    def _represent(value: Any, **kwargs: bool) -> Any:
        """Handle nested values transforms."""
        if isinstance(value, object) and isinstance(value, AsDictionaryMixin):  # pragma: no cover
            # handle nested properties that extend AsDictionaryMixin
            return value.to_dict(**kwargs)
        return value


# pylint: disable=too-few-public-methods
class AsDictionaryUseEnumNameUseCustEnumStrValueMixin(AsDictionaryMixin):
    """Format the class's public attributes as a dictionary with string values from enums.

    On Enums will use the ``name`` property.

    On CustomStrEnum types will use their ``value`` property.
    """

    @staticmethod
    def _represent(value: Any, **kwargs: bool) -> Any:
        """Handle nested values transforms."""
        if isinstance(value, object):
            if isinstance(value, AsDictionaryMixin):  # pragma: no cover
                # handle nested properties that extend AsDictionaryMixin
                return value.to_dict(**kwargs)
            if isinstance(value, Enum):
                # handle enums
                if isinstance(value, CustomStrEnum):
                    return value.value
                return value.name
        return value
