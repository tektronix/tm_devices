"""A Module containing a metaclass that converts any class into a Singleton."""

import logging
import warnings

from typing import Any, MutableMapping
from weakref import WeakValueDictionary

_logger: logging.Logger = logging.getLogger(__name__)


class Singleton(type):
    """A metaclass that converts a standard class into a Singleton (one instance).

    Examples:
        >>> from tm_devices.helpers import Singleton
        >>> class A(metaclass=Singleton):
        ...     pass
    """

    _class_instances: MutableMapping[Any, Any] = WeakValueDictionary()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Allow any usage of the class to be performed on the same instance."""
        if cls not in cls._class_instances:
            new_instance = super(Singleton, cls).__call__(*args, **kwargs)  # noqa: UP008
            cls._class_instances[cls] = new_instance
        else:
            msg = (
                f"The {cls.__name__} has already been created and is not "
                f"allowed to be instantiated twice. Previously created instance "
                f"will be used instead."
            )
            warnings.warn(msg, stacklevel=3)
            _logger.warning(msg)
        return cls._class_instances[cls]
