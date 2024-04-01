# Adding a new device driver

This guide will walk through the steps needed to add a new device driver.

`drivers\<interface_type>\<device_type>[\<device_series>]\<device_driver>.py`

## Steps to follow

01. If the new device is a brand-new device type,
    [add a new device type](./add_new_device_type.md) subpackage
02. Create the new device driver python file and class that inherits the
    appropriate device type/series base class
    1. If the new device(s) are part of a series (also referred to as a family),
       add a new series subpackage for them (e.g. `power_supplies/psu2200/`)
    2. Create the device driver python file, create a class that inherits from
       the abstracted device type (or series) base class, see
       [example](#example-of-adding-a-new-device-series-parent-driver-class).
       After creating the first driver that inherits from the abstracted type
       base class, the rest should look like the
       [example](#example-of-adding-a-new-device-driver-within-an-existing-device-type)
       below
03. Add or update **all** `__init__.py` files within the device type subpackage
    (e.g. `scopes/`, `power_supplies/`) to contain all driver classes and
    subpackage classes defined at that level
    - See other `__init__.py` files for examples
04. Update the `SupportedModels` enum exposed in
    `tm_devices/helpers/__init__.py`
05. Update the `___SUPPORTED_MODEL_REGEX_STRING` regex constant inside
    `tm_devices/helpers/functions.py` to include a mapping of the new driver name (model series)
    to a regex string matching the appropriate model strings
06. Update the `DEVICE_DRIVER_MODEL_MAPPING` lookup inside
    `tm_devices/drivers/__init__.py`
07. Update the `__all__` variable inside `tm_devices/drivers/__init__.py` to
    include the new device driver
08. Update the appropriate Type Alias in `device_manager.py` (search for "Type
    Aliases")
09. If the device supports VISA USBTMC communication, update the
    `USB_MODEL_ID_LOOKUP` lookup exposed in `tm_devices/helpers/__init__.py`
10. Update the Supported Devices section in `README.rst` to include the new model
11. Update unit tests (and simulated device files)
    1. Add a new simulated device driver in the correct folder within
       `tests/sim_devices`
    2. Update `tests/sim_devices/devices.yaml` with a new resource for the new
       driver (Make sure the device name is correct in the `devices.yaml` and in
       the corresponding simulated device file)
    3. Update `tests/test_all_device_drivers.py` with the new simulated resource
12. Run the `tests/verify_physical_device_support.py` script targeting a
    physical device that will use the newly created driver to verify it is
    working properly.

## Example of adding a new device series parent driver class

A device series driver parent should inherit the abstracted type base class and
defines abstract functions that all device drivers must implement.

```{note}
The filename should be a snake-case version of the new class name. In this example
the filepath would be `tm_devices/drivers/pi/power_supplies/psu2200/new_psu.py`
```

```python
### drivers/pi/power_supplies/new_series_psu/fancy_power_supply.py
"""Fancy PSU Base device driver for the new series/family of fancy power supplies."""
from abc import ABC
from tm_devices.drivers.pi.power_supplies.power_supply import PowerSupplyUnit
from tm_devices.drivers.device import family_base_class


@family_base_class  # Mark the base class for the new family of devices
class BaseFancyPSU(PowerSupplyUnit, ABC):
    """Base Fancy PSU device driver."""

    # Abstracted functions for specific driver implementation goes here.
```

```python
### drivers/pi/power_supplies/new_series_psu/fancy_psu_123.py
"""BaseFancyPSU device driver."""
from tm_devices.drivers.pi.power_supplies.new_series_psu.fancy_power_supply import (
    BaseFancyPSU,
)


class FancyPSU123(BaseFancyPSU):
    """Fancy PSU 123 device driver."""

    # Specific driver implementation goes here.
```

A final note here, if there was no need for a "fancy" psu family series
subpackage, then the driver class can inherit directly from the device type
parent, in this example the `PowerSupplyUnit` class.

## Example of adding a new device driver within an existing device type

To add a new device driver within the `PowerSupply` device type and `PSU2200`
series:

```{note}
The filename should be a snake-case version of the new class name. In this example
the filepath would be `tm_devices/drivers/pi/power_supplies/psu2200/new_psu.py`
```

```python
"""NewPSU device driver."""

from tm_devices.drivers.pi.power_supplies.psu2200.psu2200 import PSU2200


class NewPSU(PSU2200):
    """NewPSU device driver."""

    # Specific driver implementation goes here.
```
