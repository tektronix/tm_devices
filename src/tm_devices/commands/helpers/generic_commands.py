"""A collection of classes and other helpful objects to use when generating command drivers.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

import re
import sys

from collections import defaultdict
from functools import total_ordering
from typing import Any, Callable, DefaultDict, Optional, Type, Union

END_OF_STRING_DIGITS = re.compile(r"([-\d]+)]?$")
MIDDLE_OF_STRING_DIGITS = re.compile(r"([-\d]+)]?")
# TODO: Drop Python 3.8: Once Python 3.8 is no longer supported,
#  the dynamic parent class can be removed
# pylint: disable=unsubscriptable-object,useless-suppression
ParentDefaultDictClass: Type[DefaultDict[Any, Any]] = (
    defaultdict if sys.version_info < (3, 9) else defaultdict[Any, Any]
)


####################################################################################################
# Exceptions
####################################################################################################
class NoDeviceProvidedError(Exception):
    """A custom exception indicating that no device was provided."""


####################################################################################################
# Classes
####################################################################################################
class DefaultDictPassKeyToFactory(ParentDefaultDictClass):
    """A custom defaultdict.

    This custom defaultdict passes the key used to access a missing value into the stored
    default_factory function as the only parameter.
    """

    def __init__(self, default_factory: Callable[[Union[int, str]], Any], **kwargs: Any) -> None:
        """Create an instance of the class.

        Args:
            default_factory: The factory function used to create new values in the dictionary.
            kwargs: The keyword arguments.
        """
        super().__init__(default_factory, **kwargs)  # type: ignore[arg-type]

    def __missing__(self, key: Any) -> Any:
        """Call the ``default_factory()`` function and pass the key as the only parameter.

        Args:
            key: The key that doesn't pair with a value yet.
        """
        if self.default_factory:
            # noinspection PyArgumentList  # pylint: disable=not-callable
            dict.__setitem__(self, key, self.default_factory(key))  # type: ignore[arg-type]
            return self[key]
        return super().__missing__(key)


@total_ordering  # If comparisons are slowing down the code, implementing the rest would speed it up
class BaseCmd:
    """A class defining the base syntax of a command class.

    The syntax is accessible through the ``.cmd_syntax`` property.
    """

    def __init__(self, device: Optional[Any], cmd_syntax: str) -> None:
        """Instantiate the command.

        Args:
            device: The optional device object,
                if ``None`` is passed in then device communication will not be allowed.
            cmd_syntax: The command syntax.
        """
        self._cmd_syntax = cmd_syntax
        self._device = device

    def __eq__(self, other: object) -> bool:
        """Compare equality by comparing the syntax of two commands."""
        if not isinstance(other, BaseCmd):
            return NotImplemented
        return str(self) == str(other)

    def __lt__(self, other: Any) -> bool:
        """Check if the command is less than another command by comparing the syntax."""
        if not isinstance(other, BaseCmd):
            return NotImplemented
        return str(self) < str(other)

    def __hash__(self) -> int:
        """Provide a hash."""
        return hash(str(self))

    def __str__(self) -> str:
        """Return the syntax as the string representation of the instance object."""
        return self._cmd_syntax

    @property
    def cmd_syntax(self) -> str:
        """Return the syntax."""
        return self._cmd_syntax


class ValidatedDynamicNumberCmd(BaseCmd):  # pylint: disable=too-few-public-methods
    """A mixin class that is used to validate the dynamix item number is valid.

    This class checks the dynamic item number at the end of the SCPI syntax (``.cmd_syntax``
    attribute) to determine if it is a valid dynamic item number (greater than or equal to 1).
    """

    def __init__(self, device: Optional[Any], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)

        # Validate the dynamic item number
        if (match := END_OF_STRING_DIGITS.search(self._cmd_syntax)) is None:
            match = MIDDLE_OF_STRING_DIGITS.search(
                self._cmd_syntax.rsplit(":", maxsplit=1)[-1].rsplit(".", maxsplit=1)[-1]
            )
        if (item_number := int(match.group(1))) < 1:  # type: ignore[union-attr]
            msg = (
                f"{item_number=} is not a valid item number, "
                f"the number must be greater than or equal to 1"
            )
            raise ValueError(msg)
