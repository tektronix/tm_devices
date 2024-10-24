"""A Module containing a custom dictionary class that works with alias keys."""

import sys

from typing import Any, Dict, MutableMapping, Type

# TODO: Drop Python 3.8: Once Python 3.8 is no longer supported,
#  the dynamic parent class can be removed
# pylint: disable=unsubscriptable-object,useless-suppression
ParentDictClass: Type[Dict[Any, Any]] = dict if sys.version_info < (3, 9) else dict[Any, Any]


# TODO: Drop Python 3.8: Once Python 3.8 is no longer supported,
#  replace the parent class with `dict[Any, Any]`
class AliasDict(ParentDictClass):
    """A custom dictionary class that supports aliases as secondary keys.

    Each alias and key that is added must be unique, no duplicate aliases or keys are allowed.

    Examples:
        >>> from tm_devices.helpers.alias_dict import AliasDict
        >>> new_dict = AliasDict()
        >>> test_string = "value"
        >>> new_dict["key"] = test_string
        >>> new_dict["alias"] = test_string
        >>> print(new_dict["key"])
        value
        >>> print(new_dict["alias"])
        value
        >>> assert id(new_dict["key"]) == id(new_dict["alias"])
        >>> print(new_dict)
        {'key': 'value'}
        >>> print(len(new_dict))
        1
        >>> for key, value in new_dict.items():
        ...     print(f"{key=}, {value=}")
        key='key', value='value'
        >>> print(new_dict["key_2"])
        Traceback (most recent call last):
            ...
        KeyError: 'key_2'
    """

    def __init__(self) -> None:
        """Create an instance of the AliasDict with an empty alias lookup."""
        super().__init__()
        # a mapping of alias key to original key
        self._aliases: MutableMapping[Any, Any] = {}

    def __delitem__(self, key: Any) -> None:
        """Delete the value for the given key.

        This will also remove any aliases tied to the given key.

        Args:
            key: The key to delete the value for.
        """
        value_id = id(self.get(key))
        linked_aliases = [x for x in self._aliases if id(self.get(x) == value_id)]
        super().__delitem__(key)
        for alias in linked_aliases:
            del self._aliases[alias]

    def __getitem__(self, key: Any) -> Any:
        """Get the item for the given key.

        This first checks if the key is an alias, then defaults to the standard method.

        Args:
            key: The key to use to get a value.

        Returns:
            The value associated with the key.
        """
        if key in self._aliases:
            return self[self._aliases[key]]

        return super().__getitem__(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        """Set a new key value pair.

        This first checks if the value's id already exists, if so an alias will be created
        instead of a new dictionary entry.

        Args:
            key: The key to set to the value.
            value: The value to set.

        Raises:
            KeyError: Indicates that a duplicate key was provided.
        """
        if (key not in self and key in self._aliases) or (key in self):
            msg = (
                f"{key=} is already in use as a key or alias for "
                f"{self.__getitem__(key)!r}, duplicate keys and aliases are not allowed."
            )
            raise KeyError(msg)
        # find any existing value and create alias, else add new entry
        value_id = id(value)
        for _key, _val in self.items():
            if id(_val) == value_id:
                self._aliases[key] = _key
                break  # this skips over the else clause
        else:
            super().__setitem__(key, value)

    def __len__(self) -> int:  # pylint: disable=useless-parent-delegation
        """Return the length of the dictionary."""
        return super().__len__()
