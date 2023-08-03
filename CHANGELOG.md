# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com), and this
project adheres to [Semantic Versioning](https://semver.org).

<!--next-version-placeholder-->

______________________________________________________________________

## v0.1.7 (2023-08-02)

### Added

- Support for connecting to instruments created on top of the `pyvisa-mock` framework.

### Changed

- Updated auto-generated API documentation to not show all inherited attributes and methods in order to speed up documentation build time.
- `SourceDeviceConstants.function_list` was changed to be `SourceDeviceConstants.functions`, which is now an Enumeration of valid functions.

______________________________________________________________________

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

______________________________________________________________________

## v0.1.0 (2022-08-08)

### Added

- First release of `tm_devices`!
