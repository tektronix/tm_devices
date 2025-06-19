"""Test design patterns and requirements of tm_devices."""

import inspect

from abc import ABC
from collections.abc import Generator

# noinspection PyUnresolvedReferences
from functools import _lru_cache_wrapper, cached_property  # pyright: ignore [reportPrivateUsage]
from types import FunctionType
from typing import Any, List, Set, Type

import pytest

from packaging.version import InvalidVersion, Version

import tm_devices
import tm_devices.drivers
import tm_devices.helpers

from tm_devices.drivers.device import (
    _FAMILY_BASE_CLASS_PROPERTY_NAME,  # pyright: ignore [reportPrivateUsage]
    Device,
)


@pytest.fixture(autouse=True, scope="module")
def _reset_dm(device_manager: tm_devices.DeviceManager) -> Generator[None, None, None]:  # pyright: ignore[reportUnusedFunction]
    """Reset the device_manager settings before and after running the tests in this module.

    Args:
        device_manager: The device manager fixture.
    """
    device_manager.remove_all_devices()
    yield
    device_manager.remove_all_devices()


def get_all_drivers() -> List[Type[object]]:
    """Get all non-abstract device drivers."""
    all_drivers: List[Type[object]] = []
    for driver in get_all_subclasses(Device):
        if not (
            "UnitTestOnly" in driver.__name__
            or inspect.isabstract(driver)
            or ABC in driver.__bases__
        ):
            all_drivers.append(driver)  # noqa: PERF401
    all_drivers.sort(
        key=lambda x: getattr(
            getattr(x, _FAMILY_BASE_CLASS_PROPERTY_NAME, x), "__name__", x.__name__
        )
    )
    return all_drivers


# noinspection PyArgumentList
def get_all_subclasses(class_object: Type[object]) -> Set[Type[object]]:
    """Get all the subclasses for a given class object.

    Args:
        class_object: The object to find all subclasses for.

    Returns:
        The set of all subclasses for the given class.
    """
    if not class_object:
        return set()
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
    """Verify that the DeviceTypes is kept up to date."""
    abstract_device_list = sorted(
        {
            x.__name__
            for x in Device.__subclasses__()
            if not x.__name__.startswith(("Custom", "UnitTest"))
        }
    )
    supported_device_types = sorted(
        [
            x
            for x in tm_devices.helpers.DeviceTypes.list_values()
            if "UNIT_TEST" not in x and "UNSUPPORTED" not in x
        ]
    )
    if len(abstract_device_list) != len(supported_device_types):
        msg = (
            f"Not all abstract device types are represented in "
            f"abstract_device_list={abstract_device_list}\n"
            f"Supported device type abbreviations are {supported_device_types}, "
            f"please update abstract_device_list in this test with any missing abstract classes."
        )
        raise ValueError(msg)


@pytest.mark.parametrize("driver", get_all_drivers())
def test_driver_has_family_base_class(driver: Type[object]) -> None:
    """Test that each driver has a family base class."""
    assert hasattr(driver, _FAMILY_BASE_CLASS_PROPERTY_NAME), (
        f"{driver.__name__} is not part of a Family, "
        f"all instantiable drivers must inherit from a single "
        f"family base class decorated with the @family_base_class decorator"
    )


@pytest.mark.parametrize(
    "family_base_class",
    sorted(
        {
            getattr(driver, _FAMILY_BASE_CLASS_PROPERTY_NAME)
            for driver in get_all_drivers()
            if hasattr(driver, _FAMILY_BASE_CLASS_PROPERTY_NAME)
        },
        key=lambda x: x.__name__,  # pyright: ignore[reportUnknownMemberType,reportUnknownLambdaType,reportAttributeAccessIssue]
    ),
)
def test_family_base_class_inheritance(family_base_class: Type[object]) -> None:
    """Test that family base classes do not inherit from another family base class."""
    for family_class_base in family_base_class.__bases__:
        inherited_family_class_base = getattr(
            family_class_base, _FAMILY_BASE_CLASS_PROPERTY_NAME, None
        )
        assert not inherited_family_class_base, (
            f"{family_base_class.__name__} is not a unique family base class, overwriting "
            f"{inherited_family_class_base.__name__}"
        )


@pytest.mark.parametrize(
    ("family_base_class", "driver"),
    [
        (getattr(driver, _FAMILY_BASE_CLASS_PROPERTY_NAME), driver)
        for driver in get_all_drivers()
        if hasattr(driver, _FAMILY_BASE_CLASS_PROPERTY_NAME)
    ],
)
def test_no_new_methods_in_subclasses(
    family_base_class: Type[object], driver: Type[object]
) -> None:
    """Test that no new methods are defined in subclasses."""
    family_base_class_methods = get_all_method_names(family_base_class)
    driver_methods = get_all_method_names(driver)
    assert driver_methods.issubset(family_base_class_methods), (
        f"{driver.__name__} defines methods not present in "
        f"{family_base_class.__name__}: {driver_methods - family_base_class_methods}"
    )


@pytest.mark.parametrize("driver", get_all_drivers())
def test_mixin_import_order(driver: Type[object]) -> None:
    """Test that the Mixin import order is correct."""
    mro = [x.__name__ for x in driver.__mro__]
    if (mixin_name := driver.__name__ + "Mixin") in mro:
        assert mro[1] == mixin_name, f"The {mixin_name} was not the second item in the MRO ({mro})"


@pytest.mark.parametrize("driver", get_all_drivers())
def test_no_lru_cache_in_methods(driver: Type[object]) -> None:
    """Test that lru_cache is never used in methods."""
    lru_cached_methods = {
        name
        for name, method in inspect.getmembers(driver, predicate=is_defined_function)
        if is_lru_cached(method)
    }
    assert not lru_cached_methods, f"{driver.__name__} has lru_cached methods: {lru_cached_methods}"


def test_supported_models_in_device_driver_mapping() -> None:
    """Verify that all supported models are in the device driver mapping and drivers init file."""
    from tm_devices.drivers import _device_driver_mapping  # noqa: PLC0415

    supported_models_list = sorted(x.value for x in tm_devices.SupportedModels)
    device_driver_list: List[str] = sorted(
        _device_driver_mapping._DEVICE_DRIVER_MODEL_STR_MAPPING  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    )
    module_list: List[str] = list(tm_devices.drivers.__all__)
    # Remove a few non-driver items
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
