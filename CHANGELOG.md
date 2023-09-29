# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com), and this
project adheres to [Semantic Versioning](https://semver.org).

<!--next-version-placeholder-->

______________________________________________________________________

## v0.1.13 (2023-09-21)

### Fixed

- Fixed bug when generating a waveform using Burst Mode on an AFG.

______________________________________________________________________

## v0.1.12 (2023-09-06)

### Added

- Support for DPOJET to TekScope5k7k70k models.

______________________________________________________________________

## v0.1.11 (2023-08-29)

### Added

- Cache `*OPT?` on first access.

______________________________________________________________________

## v0.1.10 (2023-08-29)

### Added

- Support for AWG7KB

______________________________________________________________________

## v0.1.9 (2023-08-24)

### Added

- Support for `num_dig_bits_in_ch` and `total_channels` properties to TekScope5k7k70k.

______________________________________________________________________

## v0.1.8 (2023-08-09)

### Added

- Support for AWG5KB

### Changed

- Changed waveform generation to enforce CustomStrEnum function type.

______________________________________________________________________

## v0.1.7 (2023-08-02)

### Added

- Support for connecting to instruments created on top of the `pyvisa-mock` framework.

### Changed

- Updated auto-generated API documentation to not show all inherited attributes and methods in order to speed up documentation build time.
- `SourceDeviceConstants.function_list` was changed to be `SourceDeviceConstants.functions`, which is now an Enumeration of valid functions.

______________________________________________________________________

## v0.1.6 (2023-07-25)

### Changed

- Fixed bug with not allowing empty license lists.

______________________________________________________________________

## v0.1.5 (2023-07-25)

### Changed

- Updated syntax for AFG polarities.

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

## v0.1.3 (2023-07-03)

### Changed

- Removed TRIANGLE from AFG function list.
- Added symmetry to waveform generation function call.

______________________________________________________________________

## v0.1.2 (2023-06-27)

### Changed

- Updated the add_new dynamic item methods to work with numbers higher than 9.
- Fixed malformed command syntax due to a bug in determining the preceding separator character.

______________________________________________________________________

## v0.1.1 (2023-06-20)

### Added

- Added support for .dev versions.

______________________________________________________________________

## v0.1.0 (2022-08-08)

### Added

- First release of `tm_devices`!
