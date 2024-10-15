# Adding a new device type

This guide will walk through the steps needed to add a new device type.

`drivers\<interface_type>\<device_type>[\<device_series>]\<device_driver>.py`

## Steps to follow

1. Create an abstract device type class within the `drivers/` subpackage
    1. Create a new subpackage for the new device type alongside the existing
        device type subpackages at the appropriate spot in the file tree (e.g.
        `power_supplies/`, `margin_testers/`, `scopes/`)
    2. Create a new Python file and class with appropriate inheritance for the
        new device type (e.g. `power_supply.py`, `margin_tester.py`, `scope.py`)
    3. Add an `__init__.py` file within the new device type subpackage
        containing a short docstring explaining what is in the new subpackage.
        (See other `__init__.py` files for examples)
2. Update the [`DeviceTypes`][tm_devices.helpers.DeviceTypes] enum exposed in
    `tm_devices/helpers/__init__.py`
3. Add the DeviceType enum value to the newly created device driver class as a
    class property (see existing device type classes for an example)
4. Update the [`VALID_DEVICE_CONNECTION_TYPES`][tm_devices.helpers.VALID_DEVICE_CONNECTION_TYPES] lookup exposed in
    `tm_devices/helpers/__init__.py` with the new device type and its valid
    connection types
    - If needed, update the [`ConnectionTypes`][tm_devices.helpers.ConnectionTypes] enum exposed in
        `tm_devices/helpers/__init__.py` with any new connection types
5. Create a new, empty Type Alias for the new device type inside
    [`device_manager.py`][tm_devices.device_manager] (search for "Type Aliases")
    - This Type Alias should be named after the abstracted base device type
        parent class, and it should contain all device drivers that are of its
        type
6. Create a new `add_<device_type>()` method with the appropriate signature
    inside `device_manager.py` (use other methods as examples)
7. Create a new `get_<device_type>()` method with the appropriate signature
    inside `device_manager.py` (use other methods as examples)
8. Add a new folder in `tests/sim_devices/<new_type>` for unit tests
9. Update the
    [advanced architecture](../advanced/architecture.md#main-device-types) page
    to include the new device type
10. Update anything new that needs to be in
    [configuration.md](../configuration.md#legend-for-device-configuration)
