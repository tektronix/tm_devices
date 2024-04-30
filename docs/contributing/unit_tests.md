# Creating & Updating Unit Tests

This guide will walk through details needed when updating existing unit tests or creating new ones.

The tests for `tm_devices` are located in the {{ create_repo_link('tests', config.repo_url, 'tests') }} folder.

## Test Style & Standards

The `tm_devices` package uses the [pytest](https://docs.pytest.org/en/latest/) package
for testing and enforces 100% code coverage through the
[pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html) plugin.

All tests must conform to the same coding standards as the rest of the `tm_devices`
package, and are subject to the same static code analysis requirements.

## Testing First Steps

When adding or modifying source code:

1. Search through the codebase to find usages of the code being worked on.
2. Determine if the existing tests should be modified or if new tests should be created.

## Testing Details

### `DeviceManager` fixture

There is a session-scoped
[pytest fixture](https://docs.pytest.org/en/latest/explanation/fixtures.html),
`device_manager`, that provides access to simulated VISA devices throughout the entire test run.
This fixture is defined in the {{ create_repo_link('tests/conftest.py', config.repo_url, 'tests/conftest.py') }} file and returns a
[DeviceManager][tm_devices.DeviceManager] instance which can be used by any test that
needs to test device driver behavior.

### Simulated VISA devices

The unit tests make use of simulated devices to fully test each device driver.
These simulated devices are created using the
[pyvisa-sim](https://pyvisa.readthedocs.io/projects/pyvisa-sim/en/latest/)
package which has a schema for defining simulated devices.

The simulated devices primarily consist of error handling definitions and
defined commands and optional responses. In addition to these basic building blocks,
the simulated devices can also contain settable properties, see the
[pyvisa-sim docs](https://pyvisa.readthedocs.io/projects/pyvisa-sim/en/latest/definitions.html)
and the existing simulated devices for more details and examples.

The simulated devices used during testing are located in the
{{ create_repo_link('tests/sim_devices', config.repo_url, 'tests/sim_devices') }} folder, organized in sub-folders by device type.
The devices that are available for VISA connections during test runs are
defined in the {{ create_repo_link('tests/sim_devices/devices.yaml', config.repo_url, 'tests/sim_devices/devices.yaml') }} file, under
the `resources` key.

- In either of the following two scenarios, reference the
    [pyvisa-sim simulated instrument definition docs](https://pyvisa.readthedocs.io/projects/pyvisa-sim/en/latest/definitions.html)
    for details on how the simulated instruments are defined.
    1. If a new feature or driver update introduces any new commands to existing drivers:
        - The simulation definition files for the affected devices will need to be updated.
    2. If a new device driver is added:
        - A new simulation definition file for the new device will need to be added, and the
            primary `resources` list in {{ create_repo_link('tests/sim_devices/devices.yaml', config.repo_url, 'tests/sim_devices/devices.yaml') }} will need the new driver
            added, see the walkthrough for [adding a new device driver](./add_new_driver.md).
