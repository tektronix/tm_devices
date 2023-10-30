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

______________________________________________________________________

## Unreleased

Things to be included in the next release go here.

### Fixed

- Updated the auto-generated commands for a handful of models to fix various issues
- Updated the function responsible for converting version strings into `Version` objects to be able to handle software versions with non-standard formats.

______________________________________________________________________

## v0.1.22 (2023-10-24)

### Merged Pull Requests

- fix: Update the version of the semantic release action used to fix a bug with the output version. ([#69](https://github.com/tektronix/tm_devices/issues/69))

### Fixed

- Fixed the package release workflow to use a version of the `python-semantic-release` GitHub action that doesn't have any bugs

______________________________________________________________________

## v0.1.21 (2023-10-24)

### Merged Pull Requests

- ci: Update macro to enable GitHub Release template to function properly. ([#68](https://github.com/tektronix/tm_devices/issues/68))

### Fixed

- Fixed the GitHub Release template generation

______________________________________________________________________

## v0.1.20 (2023-10-24)

### Merged Pull Requests

- Add template for GitHub Releases ([#67](https://github.com/tektronix/tm_devices/issues/67))

### Added

- Added a template for rendering custom Release Notes for GitHub Releases

______________________________________________________________________

## v0.1.19 (2023-10-24)

### Merged Pull Requests

- Update the code that checks for package updates ([#66](https://github.com/tektronix/tm_devices/issues/66))

### Fixed

- Fixed a potential `PermissionsError` crash that occurred when trying to check for any available package updates

### Added

- A config flag to enable checking for updates when creating a new instance of the `DeviceManager`

### Changed

- The default behavior of the `DeviceManager` is changed to **not** check for updates

______________________________________________________________________

## v0.1.18 (2023-10-23)

### Merged Pull Requests

- Update badge displaying total number of downloads ([#41](https://github.com/tektronix/tm_devices/issues/41))
- ci: Update permissions to allow the workflow to modify GitHub Releases. ([#40](https://github.com/tektronix/tm_devices/issues/40))

### Fixed

- Updated permissions for the release workflow to allow it to upload the distribution files to the GitHub Release
- Updated the README to include the correct link to the badge displaying the total number of package downloads

______________________________________________________________________

## v0.1.17 (2023-10-20)

### Merged Pull Requests

- Fix readme links and release workflow ([#39](https://github.com/tektronix/tm_devices/issues/39))

### Fixed

- Updated links in the README to properly redirect to GitHub when accessed from PyPI
- Updated the release workflow to be able to upload artifacts to the GitHub Release page

______________________________________________________________________

## v0.1.16 (2023-10-20)

### Merged Pull Requests

- Update package release workflow to build correct version ([#38](https://github.com/tektronix/tm_devices/issues/38))

### Fixed

- Updated the release workflow to properly build the latest version after `python-semantic-release` updates the main branch

______________________________________________________________________

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

______________________________________________________________________

## v0.1.14 (2023-10-05)

### Added

- Added support for Python 3.12.

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
