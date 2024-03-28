"""Temporary test file to get to 100% coverage."""

import inspect
import itertools
import operator

from abc import ABC

# pylint: disable=import-private-name
# noinspection PyUnresolvedReferences,PyProtectedMember
from functools import _lru_cache_wrapper, cached_property  # pyright: ignore [reportPrivateUsage]
from types import FunctionType
from typing import Any, List, Set, Type

import pytest

from packaging.version import InvalidVersion, Version

import tm_devices
import tm_devices.device_manager
import tm_devices.drivers
import tm_devices.helpers


# noinspection PyProtectedMember
from tm_devices.drivers.device import (
    _FAMILY_BASE_CLASS_PROPERTY_NAME,  # pyright: ignore [reportPrivateUsage]
    Device,
)


# noinspection PyArgumentList
def get_all_subclasses(class_object: Type[object]) -> Set[Type[object]]:
    """Get all the subclasses for a given class object.

    Args:
        class_object: The object to find all subclasses for.

    Returns:
        The set of all subclasses for the given class.
    """
    return set(class_object.__subclasses__()).union(
        [s for c in class_object.__subclasses__() for s in get_all_subclasses(c)]
    )


def get_all_method_names(class_object: Type[object]) -> Set[str]:
    """Get all the methods for a given class object.

    Args:
        class_object: The object to find all methods for.

    Returns:
        The set of all methods for the given class.
    """
    # Check if it is callable and filter out private methods
    return {
        attribute
        for attribute, _ in inspect.getmembers(class_object, predicate=is_defined_function)
        if not attribute.startswith("_")
    }


def is_lru_cached(function: Any) -> bool:
    """Helper for detecting @functools.lru_cache decorated function."""
    # actual method at getattr(method, "__wrapped__"))
    return hasattr(function, "__wrapped__") and isinstance(function, _lru_cache_wrapper)


def is_defined_function(function: Any) -> bool:
    """Helper for detecting method types."""
    return isinstance(function, (FunctionType, property, cached_property, _lru_cache_wrapper))


def test_device_types() -> None:
    """Verify that the DEVICE_TYPES is kept up to date."""
    abstract_device_list = tm_devices.drivers.DEVICE_TYPE_CLASSES
    supported_device_types = sorted(
        [x for x in tm_devices.helpers.DeviceTypes.list_values() if "UNIT_TEST" not in x]
    )
    if len(abstract_device_list) != len(supported_device_types):
        msg = (
            f"Not all abstract device types are represented in "
            f"abstract_device_list={sorted([x.__name__ for x in abstract_device_list])}\n"
            f"Supported device type abbreviations are {supported_device_types}, "
            f"please update abstract_device_list in this test with any missing abstract classes."
        )
        raise ValueError(msg)


def test_device_method_abstraction() -> None:
    """Verify the abstract device inheritance structure is being followed."""
    # dynamically determine all device drivers
    all_drivers: List[Type[object]] = []
    for driver in get_all_subclasses(Device):
        # disregard anything made specifically for unit test coverage
        if not (
            "UnitTestOnly" in driver.__name__
            or inspect.isabstract(driver)
            or ABC in driver.__bases__
        ):
            assert hasattr(driver, _FAMILY_BASE_CLASS_PROPERTY_NAME), (
                f"{driver.__name__} is not part of a Family, "
                f"all instantiable drivers must inherit from have a single,"
                f"family base class decorated with the @family_base_class decorator"
            )
            all_drivers.append(driver)

    all_drivers.sort(key=operator.attrgetter(_FAMILY_BASE_CLASS_PROPERTY_NAME + ".__name__"))
    # verify family path and not adding unique methods to specific drivers
    for family_base_class, family_subclass_drivers_iter in itertools.groupby(
        all_drivers,
        key=operator.attrgetter(_FAMILY_BASE_CLASS_PROPERTY_NAME),
    ):
        # ensure family base classes never inherit from another family base class by
        # checking if any parent class's have the _product_family_base_class field
        for family_class_base in family_base_class.__bases__:
            inherited_family_class_base = getattr(
                family_class_base, _FAMILY_BASE_CLASS_PROPERTY_NAME, None
            )
            assert not inherited_family_class_base, (
                f"{family_base_class.__name__} is not a unique family base class, overwriting "
                f"{inherited_family_class_base.__name__}"
            )

        # Test that no new methods are defined in subclasses
        family_base_class_methods = get_all_method_names(family_base_class)
        for driver in family_subclass_drivers_iter:
            driver_methods = get_all_method_names(driver)

            assert driver_methods.issubset(family_base_class_methods), (
                f"{driver.__name__} defines methods not present in "
                f"{family_base_class.__name__}: {driver_methods - family_base_class_methods}"
            )

            # Test that the Mixin import order is correct
            mro: List[str] = [x.__name__ for x in driver.__mro__]
            if (mixin_name := driver.__name__ + "Mixin") in mro:
                assert mro[1] == mixin_name, f"The {mixin_name} was not the second item in the MRO"

    for driver in all_drivers:
        for name, method in inspect.getmembers(driver, predicate=is_defined_function):
            # Check that lru_cache is never used
            if is_lru_cached(method):
                # avoid anything that holds a reference to an instance longer than needed.
                # See https://docs.python.org/3/faq/programming.html#faq-cache-method-calls
                msg = f"method {name!r} is lru_cached which is banned from tm_devices."
                raise AssertionError(msg)


def test_supported_models_in_device_driver_mapping() -> None:
    """Verify that all supported models are in the device driver mapping and drivers init file."""
    supported_models_list = sorted(x.value for x in tm_devices.SupportedModels)
    device_driver_list = sorted(tm_devices.drivers.DEVICE_DRIVER_MODEL_MAPPING)
    module_list: List[str] = list(tm_devices.drivers.__all__)
    # Remove a few non-driver items
    module_list.remove("DEVICE_DRIVER_MODEL_MAPPING")
    module_list.remove("DEVICE_TYPE_CLASSES")
    module_list.remove("SupportedModels")
    module_list.sort()

    assert supported_models_list == device_driver_list
    assert module_list == device_driver_list


def test_tm_devices() -> None:
    """Verify the version is valid."""
    try:
        Version(tm_devices.__version__)
    except InvalidVersion as exc:
        pytest.fail(f"{tm_devices.__version__} is not a valid version:\n{exc}")
