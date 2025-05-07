# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com), and this
project adheres to [Semantic Versioning](https://semver.org).

Valid subsections within a version are:

- Added
- Changed
- Deprecated
- Removed
- Fixed
- Security

---

## Unreleased

Things to be included in the next release go here.

### Removed

- Python 3.8 support has been removed from the package. The minimum supported version is now Python 3.9.

---

## v3.2.0 (2025-05-07)

### Merged Pull Requests

- feat: Add disable_command_verification config file and environment variable option to enable speeding up automation scripts ([#428](https://github.com/tektronix/tm_devices/pull/428))
- python-deps(deps-dev): update ruff requirement from 0.11.7 to 0.11.8 in the python-dependencies group ([#422](https://github.com/tektronix/tm_devices/pull/422))
- fix: Ensure VISA timeout is reset after reboot in pi_control ([#425](https://github.com/tektronix/tm_devices/pull/425))
- python-deps(deps-dev): bump the python-dependencies group with 2 updates ([#416](https://github.com/tektronix/tm_devices/pull/416))
- Add tip in contribution guide pointing users to online docs for better viewing ([#419](https://github.com/tektronix/tm_devices/pull/419))
- fix: Fixed the `limit[Y]` commands on certain models which were being generated incorrectly ([#415](https://github.com/tektronix/tm_devices/pull/415))
- gh-actions(deps): bump tektronix/python-package-ci-cd ([#412](https://github.com/tektronix/tm_devices/pull/412))
- python-deps(deps-dev): update ruff requirement from 0.11.2 to 0.11.4 in the python-dependencies group ([#413](https://github.com/tektronix/tm_devices/pull/413))

### Added

- Added a new config option (settable via config file or environment variable) to allow users to
    disable command verification (primarily affecting the `.set_and_check()` method) in order to
    speed up automation scripts that have verified, known good command sequences.

### Fixed

- Fixed a bug in the auto-generated commands for certain models where the `limit[Y]` commands were incorrectly generated.
- Ensure the VISA timeout is reset after a VISA device is rebooted.

---

## v3.1.10 (2025-04-04)

### Merged Pull Requests

- Set offset after impedance so that it is properly adjusted ([#411](https://github.com/tektronix/tm_devices/pull/411))

### Fixed

- Fixed a bug in `set_function_properties` in the drivers for the internal AFG of the TekScope that could cause the offset value to change after setting impedance.

---

## v3.1.9 (2025-04-03)

### Merged Pull Requests

- fix: Fixed the method of determining the total number of physical channel connectors on the 70kSX scope series ([#408](https://github.com/tektronix/tm_devices/pull/408))
- python-deps(deps-dev): update pyright requirement from 1.1.397 to 1.1.398 in the python-dependencies group ([#405](https://github.com/tektronix/tm_devices/pull/405))
- python-deps(deps-dev): bump the python-dependencies group with 2 updates ([#404](https://github.com/tektronix/tm_devices/pull/404))
- gh-actions(deps): bump tektronix/python-package-ci-cd ([#403](https://github.com/tektronix/tm_devices/pull/403))

### Fixed

- Fixed the method of determining the total number of physical channel connectors on the 70kSX scope series to properly list all physical channels, even if not all channels can be used simultaneously, as is the case on SX scopes with the Asynchronous Time Interleaving (ATI) feature.

---

## v3.1.8 (2025-03-21)

### Merged Pull Requests

- chore: Relax psutil version requirement to >=6.0.0 ([#402](https://github.com/tektronix/tm_devices/pull/402))

### Changed

- Relaxed the required version of `psutil` to allow for easier installation of `tm_devices` into more environments.

---

## v3.1.7 (2025-03-19)

### Merged Pull Requests

- fix: Updated the logging configuration function to properly display the correct timestamp precision when using colored console logging ([#401](https://github.com/tektronix/tm_devices/pull/401))
- python-deps(deps-dev): update ruff requirement from 0.9.10 to 0.11.0 in the python-dependencies group ([#400](https://github.com/tektronix/tm_devices/pull/400))
- test: Move all distributions built during tox into a subdirectory ([#399](https://github.com/tektronix/tm_devices/pull/399))

### Fixed

- Updated the logging configuration function to properly display the correct timestamp precision when using colored console logging.

---

## v3.1.6 (2025-03-11)

### Merged Pull Requests

- Update AWG70K driver to properly handle when the DCA output signal path is not supported ([#398](https://github.com/tektronix/tm_devices/pull/398))

### Fixed

- Updated the expected error message for the `set_output_signal_path()` method in the AWG70K driver.

---

## v3.1.5 (2025-03-10)

### Merged Pull Requests

- python-deps(deps): bump the python-dependencies group across 1 directory with 2 updates ([#395](https://github.com/tektronix/tm_devices/pull/395))
- ci: Allow retries for CI testing on MacOS. ([#394](https://github.com/tektronix/tm_devices/pull/394))
- gh-actions(deps): bump tektronix/python-package-ci-cd ([#393](https://github.com/tektronix/tm_devices/pull/393))
- Fixed microsecond representation in log formatting ([#392](https://github.com/tektronix/tm_devices/pull/392))
- chore: Bump development dependencies ([#390](https://github.com/tektronix/tm_devices/pull/390))

### Changed

- Modified the logging time format to use microseconds for more precise logging.

---

## v3.1.4 (2025-03-04)

### Merged Pull Requests

- feat: Converted the previously private `_name_and_alias` property on the `Device` class into a public, cached property called `name_and_alias` ([#388](https://github.com/tektronix/tm_devices/pull/388))
- test: Ignore pull request URLs when checking links ([#384](https://github.com/tektronix/tm_devices/pull/384))

### Added

- Added a new `name_and_alias` cached property to the `Device` class that all drivers inherit from to provide easy access to a unique identifier for the device.
    - This property was previously implemented as the private `_name_and_alias` property, now it is a public, cached property.

---

## v3.1.3 (2025-02-19)

### Merged Pull Requests

- refactor: Update all error messages for VISA devices to always include the failed command unless explicitly called with the method's `verbose` parameter set to False ([#383](https://github.com/tektronix/tm_devices/pull/383))

### Changed

- The error messages for exceptions raised during VISA communication have been updated to always include the command that was being executed when the error occurred, unless the method was explicitly called with the `verbose` parameter set to False.

---

## v3.1.2 (2025-02-12)

### Merged Pull Requests

- feat: Enable turning down the verbosity of failure messages during reboot of a VISA device ([#381](https://github.com/tektronix/tm_devices/pull/381))
- gh-actions(deps): bump tektronix/python-package-ci-cd ([#378](https://github.com/tektronix/tm_devices/pull/378))

### Added

- Added a new parameter to the `create_visa_connection()` function which can be used to turn down the verbosity of the printouts to stdout during a reboot from `ERROR` to `DEBUG` to avoid cluttering the console with unnecessary failures while the device is still rebooting.

---

## v3.1.1 (2025-02-04)

### Merged Pull Requests

- feat: Added support for a new custom version string format, `"1.2.3-custom.1234+abcdefghi"` ([#376](https://github.com/tektronix/tm_devices/pull/376))

### Added

- Updated the `get_version()` function to support more custom version string formats, e.g. `"1.2.3-custom.1234+abcdefghi"`.

---

## v3.1.0 (2025-01-22)

### Merged Pull Requests

- refactor: Separate out the custom handling of different devices' software/firmware version parsing ([#373](https://github.com/tektronix/tm_devices/pull/373))
- fix: Remove unused commands files ([#371](https://github.com/tektronix/tm_devices/pull/371))
- feat: Improved VISA device error messages ([#370](https://github.com/tektronix/tm_devices/pull/370))

### Removed

- Removed the `traceback-with-variables` package as a dependency. If users would like to maintain the functionality, they will need to install this package separately and activate it within their code.

### Added

- Added a new configuration option `log_uncaught_exceptions` to enable/disable logging uncaught exceptions in the log file that is created. The default behavior is to enable logging uncaught exceptions to the log file.

### Changed

- Updated the error messages when VISA connections fail so that the messages are more informative (they now include the device type, resource expression, and VISA backend) and are logged to the main log file.
- Updated the error messages which occur when VISA communication fails (write/query) to be more concise on the console while still maintaining the verbosity needed for debugging in the log file.
- Updated the VISA communication error messages to include the device name and alias for faster identification when debugging.

---

## v3.0.0 (2025-01-13)

### Merged Pull Requests

- feat: added fast acq support for the mso2 model. ([#368](https://github.com/tektronix/tm_devices/pull/368))
- python-deps(deps-dev): update ruff requirement from 0.8.4 to 0.8.6 in the python-dependencies group ([#366](https://github.com/tektronix/tm_devices/pull/366))
- gh-actions(deps): bump tektronix/python-package-ci-cd ([#346](https://github.com/tektronix/tm_devices/pull/346))
- fix: updated get_buffers() with logic to handle empty buffer ([#364](https://github.com/tektronix/tm_devices/pull/364))
- python-deps(deps-dev): bump the python-dependencies group with 2 updates ([#347](https://github.com/tektronix/tm_devices/pull/347))
- fix: allow empty returns from tsp_device.get_buffers() ([#362](https://github.com/tektronix/tm_devices/pull/362))
- python-deps(deps-dev): update ruff requirement from 0.8.2 to 0.8.3 in the python-dependencies group ([#361](https://github.com/tektronix/tm_devices/pull/361))
- docs: Remove section of contribution guide that duplicates a later section ([#358](https://github.com/tektronix/tm_devices/pull/358))
- python-deps(deps-dev): update ruff requirement from 0.7.4 to 0.8.0 in the python-dependencies group ([#355](https://github.com/tektronix/tm_devices/pull/355))
- fix: Fix the documentation to not show the mermaid tooltip clipping at the top of each page with an inheritance diagram ([#354](https://github.com/tektronix/tm_devices/pull/354))
- chore: Remove unused env var from .readthedocs.yml ([#353](https://github.com/tektronix/tm_devices/pull/353))
- Enable pawamoy insiders docs features ([#352](https://github.com/tektronix/tm_devices/pull/352))
- feat: Added Full python API support for MDO3 model. ([#349](https://github.com/tektronix/tm_devices/pull/349))
- python-deps(deps-dev): update ruff requirement from 0.7.3 to 0.7.4 in the python-dependencies group ([#351](https://github.com/tektronix/tm_devices/pull/351))
- Use logging module instead of prints ([#345](https://github.com/tektronix/tm_devices/pull/345))
- chore: Update pyright dependency and use more reliable method of installing local nodejs for it ([#344](https://github.com/tektronix/tm_devices/pull/344))
- python-deps(deps-dev): update ruff requirement from 0.7.1 to 0.7.2 in the python-dependencies group ([#343](https://github.com/tektronix/tm_devices/pull/343))
- Add screen capture functionality for TekScope device driver family ([#342](https://github.com/tektronix/tm_devices/pull/342))
- Refactor the internal package structure and change how driver classes inherit functionality ([#333](https://github.com/tektronix/tm_devices/pull/333))
- python-deps(deps): bump the python-dependencies group with 3 updates ([#341](https://github.com/tektronix/tm_devices/pull/341))

### Added

- Added a new mixin, `ScreenCaptureMixin`, that defines methods/properties used for capturing screenshots from devices.
- Added screen capture capabilities to the `TekScope` family of device drivers.
- Testing/linting on Python 3.13.
- Added the `get_errors()` method to the `Device` class to enable easy access to the current error code and messages on any device.
- Added more details to the Architectural Overview page of the documentation as well as highlighting to the device driver diagram on the page.
- Added regex matching to the `verify_values()` helper function to allow for more flexible value verification.
- A main logfile is now created by default (can be disabled if desired) that contains all the logging output of the entire tm_devices package during execution.
    - Use the `configure_logging()` function to set the logging levels for stdout and file logging.
    - The default settings will log all messages to the log file and maintain the current printout functionality on stdout.
- A logfile is now created that contains each command sent to a VISA device.
    - This file is located next to the main log file and will start with the same name, but have the unique address of the device appended.
    - This file will only be created if file logging is enabled for the package (which is the default behavior).
- Full Python API support for the MDO3 model.
- Added fast acquisition command support for the MSO2 model.

### Changed

NOTE: Despite all the officially breaking changes, the actual drivers were only affected in
very minor ways. The primary impact to the drivers was simply the removal of previously
deprecated functionality. Almost all changes only impacted the internal workings of `tm_devices`.
However, please read through all changes to be aware of what may potentially impact your code.

- _**<span style="color:orange">minor breaking change</span>**_: Moved `SignalGenerator` class to the `driver_mixins` submodule and renamed it to `_TektronixPIAFGAWGMixin` (also made it a private mixin).
- _**<span style="color:orange">minor breaking change</span>**_: Renamed the `PIDevice`, `TSPDevice`, and `RESTAPIDevice` classes to `PIControl`, `TSPControl`, and `RESTAPIControl` respectively.
- _**<span style="color:orange">minor breaking change</span>**_: Moved the `PIControl`, `TSPControl`, and `RESTAPIControl` classes into a mixin folder so that they can be used as mixins rather than being part of the required inheritance structure.
    - In order to use these control mixins, they must be inherited at the family base class level in the driver hierarchy, along with the device type class (or any class that inherits from the base `Device` class and defines a `device_type` property and the other required abstract property implementations).
    - Due to this change, it is recommended that the specific device driver (or at least the family base class) for the device being controlled is used for type hinting.
- _**<span style="color:orange">minor breaking change</span>**_: Moved all device type subpackages (AWGs, AFGs, Scopes, SMUs, etc.) up to the top level of the `drivers` subpackage.
- _**<span style="color:orange">minor breaking change</span>**_: Converted all family base classes to inherit from the device control mixins.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Renamed the `get_eventlog_status()` method to `_get_errors()` and made it a required, abstract method for all devices to implement.
    - To get similar functionality to the previous `get_eventlog_status()` method, switch to using the new `get_errors()` method.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Changed the behavior of the `expect_esr()` method to expect an integer error code input and an optional tuple of error messages to compare against the actual error code and messages returned by the `_get_errors()` private method.
- _**<span style="color:orange">minor breaking change</span>**_: Converted the `device_type` property into an abstract, cached property to force all children of the `Device` class to specify what type of device they are.
- Updated the auto-generated command mixin classes to no longer use an `__init__()` method to enable the driver API documentation to render in a more usable way.
- Switched from using standard `print()` calls to using the `logging` module for all logging in the `tm_devices` package.
    - A configuration function provides the ability to set different logging levels for stdout and file logging.
    - The config file and environment variable can also be used to control the logging functionality.
    - The debug logging from the `pyvisa` package is also included in the log file by default.
- Updated `get_buffers()` in `TSPControl` to not error out if the buffer is found to be empty.

### Removed

- _**<span style="color:red">BREAKING CHANGE</span>**_: Removed previously deprecated `TekScopeSW` alias to the `TekScopePC` class.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Removed previously deprecated `write_buffers()` from the `TSPControl` class.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Removed Internal AFG methods from the `TekScopePC` driver, since they wouldn't have worked due to its lack of an IAFG.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Removed previously deprecated `DEVICE_DRIVER_MODEL_MAPPING` constant.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Removed the `DEVICE_TYPE_CLASSES` constant and the `device_type_classes.py` module.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Removed many hacky implementations of `total_channels` and `all_channel_names_list` properties from drivers that don't need them anymore.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Removed the `verify_values()`, `raise_failure()`, and `raise_error()` methods from all device drivers.
    - These methods have been converted to helper functions and can be imported from the `tm_devices.helpers` subpackage now.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Removed the `print_with_timestamp()` function since this functionality is now handled by the `logging` module.
- _**<span style="color:red">BREAKING CHANGE</span>**_: Removed the `get_timestamp_string()` function since this functionality is now handled by the `logging` module.

---

## v2.5.0 (2024-10-30)

### Merged Pull Requests

- TekScope2K - turn on HEADER and VERBOSE options to query available data sources correctly ([#327](https://github.com/tektronix/tm_devices/pull/327))
- fix: line fix ([#339](https://github.com/tektronix/tm_devices/pull/339))
- ci: Skip updating the mdformat repo during the dependency updater workflow ([#335](https://github.com/tektronix/tm_devices/pull/335))
- gh-actions(deps): bump tektronix/python-package-ci-cd ([#320](https://github.com/tektronix/tm_devices/pull/320))
- TSP environment cleanup ([#328](https://github.com/tektronix/tm_devices/pull/328))
- feat: Added USB support for AFG31K and MDO3 models ([#331](https://github.com/tektronix/tm_devices/pull/331))
- ci: Remove pre-commit hook that no longer works on Python 3.8 and replace with one that does ([#323](https://github.com/tektronix/tm_devices/pull/323))
- python-deps(deps-dev): bump the python-dependencies group with 2 updates ([#311](https://github.com/tektronix/tm_devices/pull/311))
- python-deps(deps): bump the python-dependencies group with 3 updates ([#318](https://github.com/tektronix/tm_devices/pull/318))
- test: Ignore googletagmanager links during doctests ([#312](https://github.com/tektronix/tm_devices/pull/312))
- ci: Enable testing for Python 3.13 ([#309](https://github.com/tektronix/tm_devices/pull/309))

### Fixed

- fix: TekScope2K active channel query needs HEADER options enabled to function properly

### Added

- `collectgarbage()` is now called during cleanup of `TSPControl` children.
- Added USBTMC Support for the AFG31K and MDO3 drivers.

---

## v2.4.0 (2024-09-19)

### Merged Pull Requests

- Update TSPDevice.load_script() to accept raw strings ([#308](https://github.com/tektronix/tm_devices/pull/308))
- fix: Update stub generation helper function to handle classes followed by dataclasses ([#307](https://github.com/tektronix/tm_devices/pull/307))
- Add function to register USBTMC connection information for devices that don't have native USBTMC connection support in tm_devices ([#306](https://github.com/tektronix/tm_devices/pull/306))
- python-deps(deps-dev): Bump the python-dependencies group with 2 updates ([#304](https://github.com/tektronix/tm_devices/pull/304))
- fix: Ensure that the default VISA timeout value is not overwritten if a new config is loaded that doesn't specify a default VISA timeout. ([#303](https://github.com/tektronix/tm_devices/pull/303))
- gh-actions(deps): Bump tektronix/python-package-ci-cd ([#287](https://github.com/tektronix/tm_devices/pull/287))
- chore: Bump the version of tektronix/python-package-ci-cd to v1.3.0 in workflows ([#301](https://github.com/tektronix/tm_devices/pull/301))
- build: Update license identifier ([#299](https://github.com/tektronix/tm_devices/pull/299))
- python-deps(deps): Bump the python-dependencies group with 3 updates ([#300](https://github.com/tektronix/tm_devices/pull/300))
- Enable customizing the default visa timeout ([#293](https://github.com/tektronix/tm_devices/pull/293))
- python-deps(deps-dev): Bump the python-dependencies group with 4 updates ([#296](https://github.com/tektronix/tm_devices/pull/296))
- Update python-pacage-ci-cd to v1.1.0 and use tokens to upload to PyPI ([#291](https://github.com/tektronix/tm_devices/pull/291))
- python-deps(deps): Bump the python-dependencies group across 1 directory with 2 updates ([#288](https://github.com/tektronix/tm_devices/pull/288))
- chore: Remove an unneeded development dependency ([#286](https://github.com/tektronix/tm_devices/pull/286))
- Convert to using reusable workflows from the `tektronix/python-package-ci-cd` repo ([#284](https://github.com/tektronix/tm_devices/pull/284))

### Added

- Added a config option (`default_visa_timeout`) to specify the default VISA timeout for all initial VISA device connections.
- Added a new function, `register_additional_usbtmc_mapping()`, to enable users to add USBTMC connection information for devices that don't have native support for USBTMC connections in `tm_devices` yet.
- Added `TSPDevice.export_buffers()` to write tsp buffer data fields to file, default is comma separated values with buffer names header.

### Changed

- Switched all workflows to use the new [`tektronix/python-package-ci-cd`](https://github.com/tektronix/python-package-ci-cd) reusable workflows.
- Reduced the out-of-the box `default_visa_timeout` value from 30 seconds to 5 seconds.
- _**SEMI-BREAKING CHANGE**_: Changed the `USB_MODEL_ID_LOOKUP` constant to use `SupportedModels` as keys instead of values to make the documentation clearer.
- _**SEMI-BREAKING CHANGE**_: Changed the `DEVICE_DRIVER_MODEL_MAPPING` constant to use `SupportedModels` as keys instead of values to make the documentation clearer.
- _**SEMI-BREAKING CHANGE**_: Changed the input parameter order in `TSPDevice.load_script()` and updated it to accept raw string input in addition to the `file_path` parameter for the script content.
- Verbosity with `PIDevice.write()` now handles multiline input printouts.

### Deprecated

- Renamed `TSPDevice.write_buffers()` to `TSPDevice.export_buffers()` for clarity.

### Fixed

- Fixed a bug in the stubgen helper code responsible for adding dynamically added methods to stub files that caused invalid stub files to be created if a dataclass immediately followed a class that was being dynamically updated.

---

## v2.3.0 (2024-08-23)

### Merged Pull Requests

- feat: Added Full API support for TekscopePC. ([#282](https://github.com/tektronix/tm_devices/pull/282))
- feat: Add curve query support for MSO2KB series scopes ([#269](https://github.com/tektronix/tm_devices/pull/269))
- python-deps(deps-dev): bump the python-dependencies group with 2 updates ([#279](https://github.com/tektronix/tm_devices/pull/279))
- ci: Use nodeenv to install node during tox runs, and install node with nodeenv during initial contributor setup ([#278](https://github.com/tektronix/tm_devices/pull/278))

### Added

- Added curve query support for the MSO2KB series scopes
- Full Python API support for TekScopePC device.

---

## v2.2.2 (2024-08-14)

### Merged Pull Requests

- Fix the stubgen helper function to attach stubs to the correct class in modules with multiple classes ([#276](https://github.com/tektronix/tm_devices/pull/276))
- python-deps(deps-dev): bump the python-dependencies group with 2 updates ([#273](https://github.com/tektronix/tm_devices/pull/273))
- docs: Update the contribution guide to provide details on how to track the status of changes in the GitHub repo using issues ([#271](https://github.com/tektronix/tm_devices/pull/271))

### Fixed

- Fixed the stubgen helper to properly attach stubs to the correct class in modules that have multiple classes.

---

## v2.2.1 (2024-08-07)

### Merged Pull Requests

- feat: Custom LAN Device Name for TCPIP Connections ([#267](https://github.com/tektronix/tm_devices/pull/267))
- docs: Update links on the Readme to point to the full GitHub URL ([#266](https://github.com/tektronix/tm_devices/pull/266))
- ci: Update the script that updates the pre-commit dependencies to update them with frozen hashes ([#265](https://github.com/tektronix/tm_devices/pull/265))
- Convert test-docs.yml to a reusable workflow ([#264](https://github.com/tektronix/tm_devices/pull/264))
- python-deps(deps-dev): bump the python-dependencies group with 3 updates ([#263](https://github.com/tektronix/tm_devices/pull/263))

### Changed

- Changed `DeviceConfigEntry` dataclass by adding an optional `lan_device_name` field, which allows connecting to instruments through TCPIP on LAN device names other than `inst0`.

---

## v2.2.0 (2024-08-02)

### Merged Pull Requests

- Enable adding unsupported device types via the DeviceManager ([#262](https://github.com/tektronix/tm_devices/pull/262))
- test: Ignore http-rate-limited warnings to avoid failure due to the abundance of GitHub URLs in the Changelog ([#261](https://github.com/tektronix/tm_devices/pull/261))

### Added

- Added a new method to the `DeviceManager` class, `add_unsupported_device()`, which enables adding an unsupported device type.

---

## v2.1.0 (2024-07-31)

### Merged Pull Requests

- feat: Added SourceXpress API support and AWG defects fix ([#260](https://github.com/tektronix/tm_devices/pull/260))
- gh-actions(deps): bump hynek/build-and-inspect-python-package ([#258](https://github.com/tektronix/tm_devices/pull/258))
- python-deps(deps-dev): bump the python-dependencies group with 2 updates ([#257](https://github.com/tektronix/tm_devices/pull/257))
- Update jinja templates ([#254](https://github.com/tektronix/tm_devices/pull/254))

### Added

- Full Python API support for SourceXpress to AWG70KA, AWG70KB and AWG7K models.

### Fixed

- Fixed APIs with writes and queries accepting arguments for AWG70KA and AWG70KB models drivers.

---

## v2.0.0 (2024-07-24)

### Merged Pull Requests

- Downgrade python-semantic-release to allow release workflow to run ([#253](https://github.com/tektronix/tm_devices/pull/253))
- docs: Updated the signal generation docs to fix some bugs that were found ([#252](https://github.com/tektronix/tm_devices/pull/252))
- Signal Generation Restructure and addition of high level methods ([#246](https://github.com/tektronix/tm_devices/pull/246))
- gh-actions(deps): bump the gh-actions-dependencies group with 2 updates ([#250](https://github.com/tektronix/tm_devices/pull/250))
- python-deps(deps-dev): bump the python-dependencies group with 3 updates ([#242](https://github.com/tektronix/tm_devices/pull/242))
- gh-actions(deps): bump anchore/scan-action ([#248](https://github.com/tektronix/tm_devices/pull/248))
- python-deps(deps-dev): bump the python-dependencies group with 2 updates ([#238](https://github.com/tektronix/tm_devices/pull/238))
- gh-actions(deps): bump python-semantic-release/python-semantic-release ([#244](https://github.com/tektronix/tm_devices/pull/244))
- ci: Add back file sorter hook to pre-commit ([#243](https://github.com/tektronix/tm_devices/pull/243))
- python-deps(deps): bump the python-dependencies group with 3 updates ([#241](https://github.com/tektronix/tm_devices/pull/241))
- gh-actions(deps): bump the gh-actions-dependencies group across 1 directory with 3 updates ([#239](https://github.com/tektronix/tm_devices/pull/239))
- refactor: Miscellaneous refactors to reduce technical debt in variable declarations and comparison operations ([#236](https://github.com/tektronix/tm_devices/pull/236))

### Added

- Added the constraint ranges for all signal generators
- Added drivers for AWG and AFG channels
- Added a property named `source_channel` in AWG's and AFG's.
- Added drivers for the internal AFG in TekScopes.
- Added a property named `internal_afg` in TekScope.
- Added implementation of `generate_function` for all AWG models.
- Added two burst functions to `SignalGeneratorMixin`: one to set up burst and one to generate the burst by forcing trigger.
    - NOTE: Only the AFGs and Internal AFGs have these functions implemented.
- Added `OutputSignalPath` enum attribute in AWGs representing output signal path options.
- Added two functions for loading waveform set files in the AWG70k and AWG5200 drivers: one for loading a waveform set file and another for loading a specific waveform from a waveform set file.
- Added `sample_waveform_set_file` attribute in the AWG70k and AWG5200 drivers to define the default waveform set file.

### Changed

- _**<span style="color:red">BREAKING CHANGE</span>**_. Changed the term "signal source" to "signal generator".
    - All uses of this term are changed. Import paths now use `signal_generator` instead of `signal_source`.
- _**<span style="color:red">BREAKING CHANGE</span>**_. Changed the function name of `generate_waveform()` to `generate_function()`.
    - `generate_waveform()` only exists on AWGs now, however the functionality is entirely changed.
- _**<span style="color:red">BREAKING CHANGE</span>**_. Changed the `generate_function()` function by removing burst functionality.
    - Any use of burst now must use `setup_burst()` and `generate_burst()` instead.
- Updated AWGs such that the `family_base_class` is at the series level.

---

## v1.5.0 (2024-06-10)

### Merged Pull Requests

- fix: Update the commands to have uniform spacing of arguments. ([#234](https://github.com/tektronix/tm_devices/pull/234))
- ci: Update the updater workflow to skip running poetry-audit during the updater process ([#235](https://github.com/tektronix/tm_devices/pull/235))
- python-deps(deps-dev): bump the python-dependencies group with 3 updates ([#233](https://github.com/tektronix/tm_devices/pull/233))
- gh-actions(deps): bump the gh-actions-dependencies group with 2 updates ([#218](https://github.com/tektronix/tm_devices/pull/218))
- docs: Properly sort modules when building the API documentation ([#231](https://github.com/tektronix/tm_devices/pull/231))
- Enable Virtual GPIB connections to supported instruments ([#230](https://github.com/tektronix/tm_devices/pull/230))
- ci: Update build and release workflows to verify the package can be installed for all supported Python versions and Operating Systems ([#229](https://github.com/tektronix/tm_devices/pull/229))
- python-deps(deps-dev): bump the python-dependencies group with 2 updates ([#225](https://github.com/tektronix/tm_devices/pull/225))
- Add workflows to check for changes that break public APIs ([#227](https://github.com/tektronix/tm_devices/pull/227))
- gh-actions(deps): bump the gh-actions-dependencies group across 1 directory with 2 updates ([#226](https://github.com/tektronix/tm_devices/pull/226))
- docs: Update the trademark symbols ([#223](https://github.com/tektronix/tm_devices/pull/223))
- docs: Add analytics code for documentation ([#222](https://github.com/tektronix/tm_devices/pull/222))
- Sign all published files ([#221](https://github.com/tektronix/tm_devices/pull/221))
- Add attestations to artifacts ([#220](https://github.com/tektronix/tm_devices/pull/220))
- python-deps(deps-dev): update pylint requirement from 3.2.0 to 3.2.1 in the python-dependencies group ([#219](https://github.com/tektronix/tm_devices/pull/219))
- docs: Update wording of API package Modules section ([#217](https://github.com/tektronix/tm_devices/pull/217))
- Update api template usage ([#216](https://github.com/tektronix/tm_devices/pull/216))
- Cleanup init files and rename abstract classes ([#215](https://github.com/tektronix/tm_devices/pull/215))
- gh-actions(deps): bump python-semantic-release/python-semantic-release from 9.6.0 to 9.7.2 in the gh-actions-dependencies group ([#213](https://github.com/tektronix/tm_devices/pull/213))
- python-deps(deps-dev): update ruff requirement from 0.4.3 to 0.4.4 in the python-dependencies group ([#214](https://github.com/tektronix/tm_devices/pull/214))
- docs: Update copy code button to not show up on doc signatures in the API documentation ([#212](https://github.com/tektronix/tm_devices/pull/212))

### Added

- Added a new section in the documentation of each package/subpackage that shows the submodules (files) of that package/subpackage.
- Added signed build provenance attestations to workflow artifacts for the built package.
- Added signed build provenance attestations to the generated SBOMs.
- Documentation was added explaining how to verify the attestations on uploaded files.
- Enabled support for Virtual GPIB connections to supported devices.

### Removed

- docs: Removed the copy code button from the Python API signatures in the documentation.

### Changed

- Updated most `__init__.py` files to not include `__all__` variable definitions.
- Renamed some of the abstract base classes to separate them from the actual device driver classes.
- Updated the documentation templates to use the new jinja template style that `mkdocstrings-python` is switching to.

### Fixed

- Fixed the API documentation to properly sort all the modules so that the Table of Contents is readable.

---

## v1.4.2 (2024-05-09)

### Merged Pull Requests

- docs: Add a copy button to the code blocks in the documentation ([#211](https://github.com/tektronix/tm_devices/pull/211))
- docs: Update mkdocs-ezglossary-plugin version used for building docs ([#210](https://github.com/tektronix/tm_devices/pull/210))
- docs: Add styling for a new method label ([#209](https://github.com/tektronix/tm_devices/pull/209))

### Added

- Added a click to copy button to all code blocks.

### Fixed

- Updated `mkdocs-ezglossary-plugin` to a version that allows linking to glossary entries from the
    home page of documentation that is hosted on ReadtheDocs.

---

## v1.4.1 (2024-05-06)

### Merged Pull Requests

- ci: Revert python-semantic-release version bump since the GitHub Action no longer properly signs commits ([#208](https://github.com/tektronix/tm_devices/pull/208))
- gh-actions(deps): bump the gh-actions-dependencies group with 2 updates ([#207](https://github.com/tektronix/tm_devices/pull/207))
- Update contribution guide to remove outdated instructions ([#205](https://github.com/tektronix/tm_devices/pull/205))
- fix: Update Changelog template to prevent pre-commit failures. when creating new versions with python-semantic-version ([#204](https://github.com/tektronix/tm_devices/pull/204))

### Fixed

- Updated the changelog template to not cause `pre-commit` failures when it is used to update the changelog.
- Updated the readme to properly render on PyPI.

### Removed

- Removed outdated instructions from the contribution guide.

---

## v1.4.0 (2024-05-03)

### Merged Pull Requests

- fix: Update release notes generator script to account for markdown formatting changes ([#203](https://github.com/tektronix/tm_devices/pull/203))
- Update package to point to ReadtheDocs for official documentation ([#201](https://github.com/tektronix/tm_devices/pull/201))
- Fix ReadtheDocs builds by installing nodejs ([#200](https://github.com/tektronix/tm_devices/pull/200))
- docs: Switch from Sphinx to Mkdocs for building documentation. ([#11](https://github.com/tektronix/tm_devices/pull/11))
- gh-actions(deps): bump python-semantic-release/python-semantic-release ([#197](https://github.com/tektronix/tm_devices/pull/197))
- python-deps(deps): bump the python-dependencies group with 2 updates ([#192](https://github.com/tektronix/tm_devices/pull/192))
- gh-actions(deps): bump the gh-actions-dependencies group with 2 updates ([#191](https://github.com/tektronix/tm_devices/pull/191))
- gh-actions(deps): bump the gh-actions-dependencies group with 3 updates ([#190](https://github.com/tektronix/tm_devices/pull/190))
- python-deps(deps-dev): update pyright requirement from 1.1.356 to 1.1.357 in the python-dependencies group ([#189](https://github.com/tektronix/tm_devices/pull/189))

### Changed

- Switched from using `sphinx` to `mkdocs` for building the documentation. This enables building the
    documentation in under 10 minutes while using less than 6 GB of RAM and saving almost 2 GB of
    disk space. Fixes [#77](https://github.com/tektronix/tm_devices/issues/77).
- Switched from GitHub Pages to ReadtheDocs for official documentation hosting.

### Fixed

- Fixed the Readme to display as intended in GitHub and PyPI while maintaining all functionality in
    the generated documentation site.

---

## v1.3.0 (2024-04-04)

### Merged Pull Requests

- Updated the get_acquisition_data example to select source for the measurement. ([#187](https://github.com/tektronix/tm_devices/issues/187))

### Changed

- Updated get_acquisition_data example to select source for the measurement.

---

## v1.2.3 (2024-04-03)

### Merged Pull Requests

- Update SBOM scanning workflow to be able to upload artifacts to GitHub releases ([#186](https://github.com/tektronix/tm_devices/issues/186))

### Security

- Updated the workflow that creates SBOMs to be able to upload the SBOM as an artifact to a GitHub release.

---

## v1.2.2 (2024-04-03)

### Merged Pull Requests

- Fix packaging workflows to correctly gate on the repo name. ([#185](https://github.com/tektronix/tm_devices/issues/185))
- Convert PyPI upload workflows into reusable workflows. ([#184](https://github.com/tektronix/tm_devices/issues/184))
- ci: Update docformatter version, it no longer causes issues. ([#182](https://github.com/tektronix/tm_devices/issues/182))
- Add test results to job summary and pull request comments ([#181](https://github.com/tektronix/tm_devices/issues/181))
- Convert workflows into reusable workflows ([#178](https://github.com/tektronix/tm_devices/issues/178))
- Update file checker workflow ([#179](https://github.com/tektronix/tm_devices/issues/179))
- gh-actions(deps): bump the gh-actions-dependencies group with 2 updates ([#177](https://github.com/tektronix/tm_devices/issues/177))
- python-deps(deps-dev): bump the python-dependencies group with 1 update ([#176](https://github.com/tektronix/tm_devices/issues/176))
- Update admonition in readme to fix a glitch/bug in GitHub web UI ([#174](https://github.com/tektronix/tm_devices/issues/174))
- Update supported devices and VISA backends in the readme ([#170](https://github.com/tektronix/tm_devices/issues/170))
- fix: Updated the measurement source selection command for the MDO3K, MDO4K, MSO4K and DPO4K models to work properly. ([#173](https://github.com/tektronix/tm_devices/issues/173))
- ci: Update codecov-action to v4. ([#140](https://github.com/tektronix/tm_devices/issues/140))
- Handle Visa IO Error on first connection ([#172](https://github.com/tektronix/tm_devices/issues/172))
- Misc. workflow updates ([#171](https://github.com/tektronix/tm_devices/issues/171))
- gh-actions(deps): Bump the gh-actions-dependencies group with 1 update ([#158](https://github.com/tektronix/tm_devices/issues/158))
- python-deps(deps): Bump the python-dependencies group with 2 updates ([#159](https://github.com/tektronix/tm_devices/issues/159))
- gh-actions(deps): Bump the gh-actions-dependencies group with 2 updates ([#166](https://github.com/tektronix/tm_devices/issues/166))
- ci: Update documentation builds to use node.js version 20. ([#163](https://github.com/tektronix/tm_devices/issues/163))
- refactor: Update the type aliases used by the `DeviceManager` add/get methods to return `TypeVar`s with default values that are bound to the appropriate device type. ([#162](https://github.com/tektronix/tm_devices/issues/162))
- ci: Add a step to upload the sarif file as a workflow artifact. ([#157](https://github.com/tektronix/tm_devices/issues/157))
- refactor: Update the get_model_series() method to only warn the user if the model isn't contained in the list of supported models. ([#156](https://github.com/tektronix/tm_devices/issues/156))
- test: Update tox to test building the package in a unique environment to prevent race conditions when running tox environments in parallel. ([#155](https://github.com/tektronix/tm_devices/issues/155))
- ci: Add permissions to write security events for the SBOM scan. ([#154](https://github.com/tektronix/tm_devices/issues/154))
- Add SBOM generation and scanning workflow ([#153](https://github.com/tektronix/tm_devices/issues/153))

### Added

- Added TekVISA as one of the VISA backends supported.

### Changed

- Updated the `get_model_series()` function to only warn the user if the model is not found in the `SupportedModels` enumeration. This also eliminates false warnings during unit tests.

### Fixed

- Updated the measurement source selection command for the MDO3K, MDO4K, MSO4K and DPO4K models to work properly.

---

## v1.2.1 (2024-02-27)

### Merged Pull Requests

- python-deps(deps-dev): Bump the python-dependencies group with 1 update ([#151](https://github.com/tektronix/tm_devices/issues/151))
- gh-actions(deps): Bump the gh-actions-dependencies group with 2 updates ([#147](https://github.com/tektronix/tm_devices/issues/147))
- Update read only cached property for PyCharm auto-complete support ([#149](https://github.com/tektronix/tm_devices/issues/149))
- Update release workflow to print out incoming changes in job summary for easy review ([#148](https://github.com/tektronix/tm_devices/issues/148))
- ci: Created a workflow to update python linting dependencies and pre-commit hook versions inside of a PR. ([#146](https://github.com/tektronix/tm_devices/issues/146))
- refactor: Updated the `get_model_series()` function to make it simpler for future maintenance and additions. ([#145](https://github.com/tektronix/tm_devices/issues/145))
- gh-actions(deps): Bump the gh-actions-dependencies group with 1 update ([#144](https://github.com/tektronix/tm_devices/issues/144))

### Changed

- Updated the `get_model_series()` function to use a regex mapping instead of complicated logic to reduce maintenance costs.

### Fixed

- Updated import statements for the `ReadOnlyCachedProperty` decorator to allow PyCharm auto-complete to work properly.

---

## v1.2.0 (2024-02-09)

### Merged Pull Requests

- fix: Removed unused command files. ([#143](https://github.com/tektronix/tm_devices/issues/143))
- fix: modified API under MSO 2,4,5,6 modules ([#142](https://github.com/tektronix/tm_devices/issues/142))
- Update PI Device close method to catch VisaIOErrors ([#141](https://github.com/tektronix/tm_devices/issues/141))
- ci: Update pre-commit hooks and linter versions. ([#139](https://github.com/tektronix/tm_devices/issues/139))
- gh-actions(deps): Bump the gh-actions-dependencies group with 1 update ([#123](https://github.com/tektronix/tm_devices/issues/123))
- python-deps(deps): Bump the python-dependencies group with 1 update ([#136](https://github.com/tektronix/tm_devices/issues/136))
- fix: Update the function that detects a VISA resource expression to work properly for SOCKET resource expressions. ([#134](https://github.com/tektronix/tm_devices/issues/134))
- style: Update linting rules. ([#132](https://github.com/tektronix/tm_devices/issues/132))
- Pin the linters used (ruff, pyright, pylint) to specific versions ([#131](https://github.com/tektronix/tm_devices/issues/131))
- Update doc workflow runners ([#128](https://github.com/tektronix/tm_devices/issues/128))
- build: Update version of ruff for pre-commit. Remove unused noqa comment. ([#126](https://github.com/tektronix/tm_devices/issues/126))
- MSO5k, DPO5k, and DPO7k full driver support ([#125](https://github.com/tektronix/tm_devices/issues/125))
- gh-actions(deps): Bump the gh-actions-dependencies group with 3 updates ([#121](https://github.com/tektronix/tm_devices/issues/121))
- Update GitHub action versions used in workflows ([#120](https://github.com/tektronix/tm_devices/issues/120))
- feat: Added a mechanism to reset cached properties whenever a device is rebooted. ([#118](https://github.com/tektronix/tm_devices/issues/118))
- refactor(code-style): Switch to `ruff format` instead of `black` for code formatting. ([#117](https://github.com/tektronix/tm_devices/issues/117))
- gh-actions(deps): Bump the gh-actions-dependencies group with 2 updates ([#116](https://github.com/tektronix/tm_devices/issues/116))

### Added

- Added a step during a device reboot that will reset all the cached properties in the event that one of them changed.
- Added command API support for MSO5K, DPO5K, and DPO7K models.
- Added a custom, read-only implementation of the [`cached_property`](https://docs.python.org/3/library/functools.html#functools.cached_property) decorator.
- Added default buffer API for SMU 26xx series models.

### Changed

- Switched to ruff's formatter instead of black's formatter for python code.
- Updated the version of `python-semantic-release` that is used to avoid needing to store a copy of the previous changelog in the repo.
- Pinned the linters (ruff, pyright, pylint, docformatter) to specific versions to reduce failures when updates are released that add new rules or break existing rules.

### Fixed

- Fixed the code that detects VISA resource expressions to be able to detect SOCKET resource expressions properly.
- Fixed PI device close method to catch VisaIOErrors and throw a warning, rather than an exception, when closing a PI device connection.
- Fixed APIs with query attributes missing under MSO4, MSO5, MSO6 and MSO2 model drivers.

---

## v1.1.0 (2023-12-07)

### Merged Pull Requests

- feat: Added support for MSO4B device ([#115](https://github.com/tektronix/tm_devices/issues/115))
- gh-actions(deps): Bump the gh-actions-dependencies group with 1 update ([#112](https://github.com/tektronix/tm_devices/issues/112))
- test: Update tests to try to eliminate false failures when running tests on macOS. ([#114](https://github.com/tektronix/tm_devices/issues/114))
- ci: Add the admin team as reviewers to all Pull Requests. ([#113](https://github.com/tektronix/tm_devices/issues/113))
- Update config docs and release workflow ([#111](https://github.com/tektronix/tm_devices/issues/111))

### Added

- Added support for MSO4B device.

---

## v1.0.1 (2023-12-01)

### Merged Pull Requests

- Fix import error on mac with system integrity protection ([#109](https://github.com/tektronix/tm_devices/issues/109))
- feat(rest_api_device): Enable sending raw data for restful api devices. ([#107](https://github.com/tektronix/tm_devices/issues/107))
- build: Update package classifiers. ([#106](https://github.com/tektronix/tm_devices/issues/106))

### Added

- Added an option to send raw data for RESTful API devices

### Changed

- Updated the package classifiers for PyPI

### Fixed

- Fixed a crash observed on macOS when importing `tm_devices`, issue [#108](https://github.com/tektronix/tm_devices/issues/108)

---

## v1.0.0 (2023-11-13)

### Merged Pull Requests

- docs: Remove the TestPyPI badge from the readme, it is not important. ([#105](https://github.com/tektronix/tm_devices/issues/105))
- Update the Readme ([#100](https://github.com/tektronix/tm_devices/issues/100))
- ci: Increase timeout when installing tm_devices from pypi servers to avoid issues caused by long wheel build times for packages that tm_devices depends on (such as zeroconf). ([#98](https://github.com/tektronix/tm_devices/issues/98))
- feat: Add USBTMC support for the 3706A device. ([#97](https://github.com/tektronix/tm_devices/issues/97))
- Add new options for REST API devices ([#96](https://github.com/tektronix/tm_devices/issues/96))
- ci: Update how the changelog generation macro selects PR numbers. ([#95](https://github.com/tektronix/tm_devices/issues/95))
- gh-actions(deps): Bump the gh-actions-dependencies group with 5 updates ([#93](https://github.com/tektronix/tm_devices/issues/93))
- ci: Added a workflow to scan for security issues in dependencies on all PRs. ([#91](https://github.com/tektronix/tm_devices/issues/91))
- fix: Update a few comments to have better wording. ([#85](https://github.com/tektronix/tm_devices/issues/85))
- Update the basic usage docs and Readme ([#84](https://github.com/tektronix/tm_devices/issues/84))
- docs: Update basic usage with better wording for examples. ([#83](https://github.com/tektronix/tm_devices/issues/83))
- refactor: Removed some API files that are no longer needed (outdated/broken) ([#82](https://github.com/tektronix/tm_devices/issues/82))

### Added

- New examples added to the basic usage guide showing how to use the commands for some scope drivers
- Added an example showing how to change the VISA backend that is used for connecting to devices
- Added a new support table in the Readme showing the API support for Software Solutions
- Added an option to bypass SSL certificate verification for RESTful API devices
- Added an option to allow URL redirects for RESTful API devices
- Added the 3706a to the list of supported usb devices

### Changed

- Updated the support level tables in the Readme

### Removed

- Removed some outdated and broken API files

---

## v0.1.24 (2023-10-30)

### Merged Pull Requests

- fix: Build docs without parallelization to fix pop-up issues with sphinx-tippy ([#80](https://github.com/tektronix/tm_devices/issues/80))

### Fixed

- Fixed the `tippy.js` pop-ups in the documentation

---

## v0.1.23 (2023-10-30)

### Merged Pull Requests

- fix: Handle non-standard software versions with alpha characters in the last part of the version. ([#81](https://github.com/tektronix/tm_devices/issues/81))
- docs: Updated the custom styling for the badge table in the readme to make sure the badges are spaced vertically properly. ([#79](https://github.com/tektronix/tm_devices/issues/79))
- Update contribution guide and documentation publishing workflow ([#78](https://github.com/tektronix/tm_devices/issues/78))
- docs: Added new workflow which can deploy the documentation to GitHub Pages ([#76](https://github.com/tektronix/tm_devices/issues/76))
- Update version of GitHub action used to build the package ([#75](https://github.com/tektronix/tm_devices/issues/75))
- fix: Update auto-generated command API files to fix various issues. ([#72](https://github.com/tektronix/tm_devices/issues/72))
- fix: Remove outdated comment. ([#71](https://github.com/tektronix/tm_devices/issues/71))
- ci: Update workflow name and add Python 3.12 classifier ([#70](https://github.com/tektronix/tm_devices/issues/70))

### Fixed

- Updated the auto-generated commands for a handful of models to fix various issues
- Updated the function responsible for converting version strings into `Version` objects to be able to handle software versions with non-standard formats.

---

## v0.1.22 (2023-10-24)

### Merged Pull Requests

- fix: Update the version of the semantic release action used to fix a bug with the output version. ([#69](https://github.com/tektronix/tm_devices/issues/69))

### Fixed

- Fixed the package release workflow to use a version of the `python-semantic-release` GitHub action that doesn't have any bugs

---

## v0.1.21 (2023-10-24)

### Merged Pull Requests

- ci: Update macro to enable GitHub Release template to function properly. ([#68](https://github.com/tektronix/tm_devices/issues/68))

### Fixed

- Fixed the GitHub Release template generation

---

## v0.1.20 (2023-10-24)

### Merged Pull Requests

- Add template for GitHub Releases ([#67](https://github.com/tektronix/tm_devices/issues/67))

### Added

- Added a template for rendering custom Release Notes for GitHub Releases

---

## v0.1.19 (2023-10-24)

### Merged Pull Requests

- Update the code that checks for package updates ([#66](https://github.com/tektronix/tm_devices/issues/66))

### Fixed

- Fixed a potential `PermissionsError` crash that occurred when trying to check for any available package updates

### Added

- A config flag to enable checking for updates when creating a new instance of the `DeviceManager`

### Changed

- The default behavior of the `DeviceManager` is changed to **not** check for updates

---

## v0.1.18 (2023-10-23)

### Merged Pull Requests

- Update badge displaying total number of downloads ([#41](https://github.com/tektronix/tm_devices/issues/41))
- ci: Update permissions to allow the workflow to modify GitHub Releases. ([#40](https://github.com/tektronix/tm_devices/issues/40))

### Fixed

- Updated permissions for the release workflow to allow it to upload the distribution files to the GitHub Release
- Updated the README to include the correct link to the badge displaying the total number of package downloads

---

## v0.1.17 (2023-10-20)

### Merged Pull Requests

- Fix readme links and release workflow ([#39](https://github.com/tektronix/tm_devices/issues/39))

### Fixed

- Updated links in the README to properly redirect to GitHub when accessed from PyPI
- Updated the release workflow to be able to upload artifacts to the GitHub Release page

---

## v0.1.16 (2023-10-20)

### Merged Pull Requests

- Update package release workflow to build correct version ([#38](https://github.com/tektronix/tm_devices/issues/38))

### Fixed

- Updated the release workflow to properly build the latest version after `python-semantic-release` updates the main branch

---

## v0.1.15 (2023-10-20)

### Merged Pull Requests

- ci: Update workflow to enable signed commits. ([#37](https://github.com/tektronix/tm_devices/issues/37))
- ci: Add missing command to workflow. ([#36](https://github.com/tektronix/tm_devices/issues/36))
- ci: Update semantic release step to not use the docker container. ([#35](https://github.com/tektronix/tm_devices/issues/35))
- Update packaging workflow ([#34](https://github.com/tektronix/tm_devices/issues/34))
- Update package release workflow with necessary permissions ([#33](https://github.com/tektronix/tm_devices/issues/33))
- docs: Update links in readme. Also add badge for project publish workflow. ([#32](https://github.com/tektronix/tm_devices/issues/32))
- Update changelog update process ([#31](https://github.com/tektronix/tm_devices/issues/31))
- ci: Update git config during package release. ([#30](https://github.com/tektronix/tm_devices/issues/30))
- ci: Added a workflow and necessary support scripts/templates to enable automated released via GitHub's workflow_dispatch trigger. ([#29](https://github.com/tektronix/tm_devices/issues/29))
- Added a command-line script to print the available VISA resources. ([#26](https://github.com/tektronix/tm_devices/issues/26))
- Update test.pypi.org upload workflow ([#25](https://github.com/tektronix/tm_devices/issues/25))
- Add a wait time to allow for the package to be available to install. ([#24](https://github.com/tektronix/tm_devices/issues/24))
- Custom testpypi version creation script ([#23](https://github.com/tektronix/tm_devices/issues/23))
- Fix TestPyPI upload ([#22](https://github.com/tektronix/tm_devices/issues/22))
- Update python-semantic-release config settings. ([#21](https://github.com/tektronix/tm_devices/issues/21))
- Implement separate TestPyPI upload workflow ([#20](https://github.com/tektronix/tm_devices/issues/20))
- Upload unique dev packages to test.pypi.org ([#19](https://github.com/tektronix/tm_devices/issues/19))

### Added

- A command-line script to list all available VISA resources, `list-visa-resources`

---

## v0.1.14 (2023-10-05)

### Added

- Added support for Python 3.12.

---

## v0.1.13 (2023-09-21)

### Fixed

- Fixed bug when generating a waveform using Burst Mode on an AFG.

---

## v0.1.12 (2023-09-06)

### Added

- Support for DPOJET to TekScope5k7k70k models.

---

## v0.1.11 (2023-08-29)

### Added

- Cache `*OPT?` on first access.

---

## v0.1.10 (2023-08-29)

### Added

- Support for AWG7KB

---

## v0.1.9 (2023-08-24)

### Added

- Support for `num_dig_bits_in_ch` and `total_channels` properties to TekScope5k7k70k.

---

## v0.1.8 (2023-08-09)

### Added

- Support for AWG5KB

### Changed

- Changed waveform generation to enforce CustomStrEnum function type.

---

## v0.1.7 (2023-08-02)

### Added

- Support for connecting to instruments created on top of the `pyvisa-mock` framework.

### Changed

- Updated auto-generated API documentation to not show all inherited attributes and methods in order to speed up documentation build time.
- `SourceDeviceConstants.function_list` was changed to be `SourceDeviceConstants.functions`, which is now an Enumeration of valid functions.

---

## v0.1.6 (2023-07-25)

### Changed

- Fixed bug with not allowing empty license lists.

---

## v0.1.5 (2023-07-25)

### Changed

- Updated syntax for AFG polarities.

---

## v0.1.4 (2023-07-21)

### Added

- `channel` property to TekScope
- Abstract mixin classes for licenses, analysis objects, and usb drives.
- @family_base_class to denote and enforce end of method definitions in the inheritance tree.

### Changed

- Refactored abstract method inheritance to use Mixins for many methods and properties for ease of expandability.
- Channel specific functions now only accept strings as input.

### Removed

- `all_channel_numbers_list` property since MSO2 breaks convention so can no longer rely on sequential channel numbering.

---

## v0.1.3 (2023-07-03)

### Changed

- Removed TRIANGLE from AFG function list.
- Added symmetry to waveform generation function call.

---

## v0.1.2 (2023-06-27)

### Changed

- Updated the add_new dynamic item methods to work with numbers higher than 9.
- Fixed malformed command syntax due to a bug in determining the preceding separator character.

---

## v0.1.1 (2023-06-20)

### Added

- Added support for .dev versions.

---

## v0.1.0 (2022-08-08)

### Added

- First release of `tm_devices`!
