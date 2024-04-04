<div class="custom-badge-table">

|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Testing**       | [![Code testing status](https://github.com/tektronix/tm_devices/actions/workflows/test-code.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/test-code.yml) [![Docs testing status](https://github.com/tektronix/tm_devices/actions/workflows/test-docs.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/test-docs.yml) [![Coverage status](https://codecov.io/gh/tektronix/tm_devices/branch/main/graph/badge.svg)](https://codecov.io/gh/tektronix/tm_devices)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Code Quality**  | [![CodeQL status](https://github.com/tektronix/tm_devices/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/codeql-analysis.yml) [![CodeFactor grade](https://www.codefactor.io/repository/github/tektronix/tm_devices/badge)](https://www.codefactor.io/repository/github/tektronix/tm_devices) [![pre-commit status](https://results.pre-commit.ci/badge/github/tektronix/tm_devices/main.svg)](https://results.pre-commit.ci/latest/github/tektronix/tm_devices/main)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Package**       | [![PyPI: Package status](https://img.shields.io/pypi/status/tm_devices?logo=pypi)](https://pypi.org/project/tm_devices/) [![PyPI: Latest release version](https://img.shields.io/pypi/v/tm_devices?logo=pypi)](https://pypi.org/project/tm_devices/) [![PyPI: Supported Python versions](https://img.shields.io/pypi/pyversions/tm_devices?logo=python)](https://pypi.org/project/tm_devices/) [![PyPI: Downloads](https://pepy.tech/badge/tm-devices)](https://pepy.tech/project/tm_devices) [![License: Apache 2.0](https://img.shields.io/pypi/l/tm_devices)](https://tinyurl.com/tek-tm-devices/LICENSE.md) [![Package build status](https://github.com/tektronix/tm_devices/actions/workflows/package-build.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/package-build.yml) [![PyPI upload status](https://github.com/tektronix/tm_devices/actions/workflows/package-release.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/package-release.yml) |
| **Documentation** | [![GitHub Pages status](https://github.com/tektronix/tm_devices/actions/workflows/deploy-documentation.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/deploy-documentation.yml)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Code Style**    | [![Test style: pytest](https://img.shields.io/badge/test%20style-pytest-blue)](https://github.com/pytest-dev/pytest) [![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-black)](https://docs.astral.sh/ruff/formatter/) [![Docstring style: google](https://img.shields.io/badge/docstring%20style-google-tan)](https://google.github.io/styleguide/pyguide.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Linting**       | [![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) [![Docstring formatter: docformatter](https://img.shields.io/badge/docstring%20formatter-docformatter-tan)](https://github.com/PyCQA/docformatter) [![Type Checker: pyright](https://img.shields.io/badge/type%20checker-pyright-yellowgreen)](https://github.com/RobertCraigie/pyright-python) [![Linter: pylint](https://img.shields.io/badge/linter-pylint-purple)](https://github.com/pylint-dev/pylint) [![Linter: Ruff](https://img.shields.io/badge/linter-ruff-purple)](https://github.com/charliermarsh/ruff)                                                                                                                                                                                                                                                                                                                                                                |

</div>

______________________________________________________________________

# tm_devices: Test & Measurement Device Management

`tm_devices` is a device management package which allows for better
control and usage of Test & Measurement devices in python scripts. This
is accomplished by using the
[PyVISA](https://pyvisa.readthedocs.io/en/latest/) package to manage
connections and communication with devices. `tm_devices` gives users
access to a much higher level abstraction of device control by providing
access to device drivers with a complete Python API.

## Dependencies

`tm_devices` can be used without any external (non-python) dependencies
on any operating system thanks to the
[PyVISA-py](https://pyvisa.readthedocs.io/projects/pyvisa-py/en/latest/)
VISA backend. However, in order to use any VISA functionality that
PyVISA-py does not implement, a third-party VISA backend such as
[TekVISA](https://www.tek.com/en/search?keywords=tekvisa&facets=_templatename%3dsoftware%26parsedsoftwaretype%3dDriver&sort=)
(>=4.2.0) or
[NI-VISA](https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html)
can be installed. `tm_devices` will use an available VISA backend if one
is found and will fall back to using PyVISA-py if no other VISA backends
are installed.

## Installation

```shell
pip install tm_devices
```

## Basic Usage

### Print Available VISA Devices

```console
$ list-visa-resources
[
  "TCPIP0::192.168.0.100::inst0::INSTR",
  "ASRL4::INSTR"
]
```

### Basic Script

```python
from tm_devices import DeviceManager

with DeviceManager() as device_manager:
    scope = device_manager.add_scope("192.168.0.100")
    scope.query("*IDN?")
    print(scope)
```

### Supported Devices & Software Solutions

```{admonition} Legend
---
class: hint
---
| Symbol/Term | Definition       |
| ----------- | ---------------- |
| 🚧          | Work in progress |
| ✅          | Implemented      |
| ❌          | Not Supported    |

See the {doc}`glossary` for more information on abbreviations.
```

<div class="custom-table-center-cells device-support-table" title="Device Support Levels">

<div class="custom-table-title">

_Device Support Levels_

</div>

| Type                   | Series/Model             | Command<br>Type | Basic<br>Control | Python API<br>Validation<br>Status |
| ---------------------- | ------------------------ | --------------- | ---------------- | ---------------------------------- |
| {term}`AFGs <AFG>`     | **AFG3000**              | {term}`PI`      | ✅                |                                    |
|                        | **AFG31xxx**             | {term}`PI`      | ✅                |                                    |
| {term}`AWGs <AWG>`     | **AWG5000**              | {term}`PI`      | ✅                |                                    |
|                        | **AWG5200**              | {term}`PI`      | ✅                |                                    |
|                        | **AWG7000**              | {term}`PI`      | ✅                |                                    |
|                        | **AWG70000**             | {term}`PI`      | ✅                |                                    |
| {term}`Scopes <Scope>` | **2 Series MSO**         | {term}`PI`      | ✅                | ✅                                  |
|                        | **3 Series MDO**         | {term}`PI`      | ✅                |                                    |
|                        | **4 Series MSO**         | {term}`PI`      | ✅                | ✅                                  |
|                        | **4 Series B MSO**       | {term}`PI`      | ✅                | ✅                                  |
|                        | **5 Series MSO**         | {term}`PI`      | ✅                | ✅                                  |
|                        | **5 Series B MSO**       | {term}`PI`      | ✅                | ✅                                  |
|                        | **5 Series MSO (LP)**    | {term}`PI`      | ✅                | ✅                                  |
|                        | **6 Series MSO**         | {term}`PI`      | ✅                | ✅                                  |
|                        | **6 Series B MSO**       | {term}`PI`      | ✅                | ✅                                  |
|                        | **6 Series LPD**         | {term}`PI`      | ✅                | ✅                                  |
|                        | **MSO2000/B**            | {term}`PI`      | ✅                |                                    |
|                        | **DPO2000/B**            | {term}`PI`      | ✅                |                                    |
|                        | **MDO3000**              | {term}`PI`      | ✅                | ✅                                  |
|                        | **MDO4000/B/C**          | {term}`PI`      | ✅                | ✅                                  |
|                        | **MSO4000/B**            | {term}`PI`      | ✅                | ✅                                  |
|                        | **DPO4000/B**            | {term}`PI`      | ✅                | ✅                                  |
|                        | **MSO5000/B**            | {term}`PI`      | ✅                | ✅                                  |
|                        | **DPO5000/B**            | {term}`PI`      | ✅                | ✅                                  |
|                        | **DPO7000/C**            | {term}`PI`      | ✅                | ✅                                  |
|                        | **DPO70000/C/D/DX/SX**   | {term}`PI`      | ✅                | ✅                                  |
|                        | **DSA70000/C/D**         | {term}`PI`      | ✅                | ✅                                  |
|                        | **MSO70000/C/DX**        | {term}`PI`      | ✅                | ✅                                  |
|                        | **TSOVu**                | {term}`PI`      | ✅                |                                    |
|                        | **TekScope**             | {term}`PI`      | ✅                |                                    |
| {term}`PSUs <PSU>`     | **2200**                 | {term}`PI`      | ✅                |                                    |
|                        | **2220**                 | {term}`PI`      | ✅                |                                    |
|                        | **2230**                 | {term}`PI`      | ✅                |                                    |
|                        | **2231**                 | {term}`PI`      | ✅                |                                    |
|                        | **2280S**                | {term}`PI`      | ✅                |                                    |
|                        | **2281S**                | {term}`PI`      | ✅                |                                    |
| {term}`SMUs <SMU>`     | **24xx Standard**        | {term}`PI`      | ✅                |                                    |
|                        | **24xx Interactive**     | {term}`PI`      | ✅                | ✅                                  |
|                        | **26xxB**                | {term}`PI`      | ✅                | 🚧                                  |
|                        | **2636B**                | {term}`PI`      | ✅                | ✅                                  |
|                        | **Model 2601B-PULSE**    | {term}`PI`      | ✅                |                                    |
|                        | **Model 2606B**          | {term}`PI`      | ✅                | 🚧                                  |
|                        | **2651A**                | {term}`PI`      | ✅                | ✅                                  |
|                        | **2657A**                | {term}`PI`      | ✅                |                                    |
|                        | **6430 (electrometer)**  | {term}`PI`      | ✅                |                                    |
|                        | **6514 (electrometer)**  | {term}`PI`      | ✅                |                                    |
|                        | **6517B (electrometer)** | {term}`PI`      | ✅                |                                    |
| {term}`MTs <MT>`       | **TMT4**                 | {term}`PI`      | ✅                |                                    |
| {term}`DMMs <DMM>`     | **DMM6500**              | {term}`PI`      | ✅                |                                    |
|                        | **DMM7510**              | {term}`PI`      | ✅                |                                    |
|                        | **DMM7512**              | {term}`PI`      | ✅                |                                    |
| {term}`DAQs <DAQ>`     | **DAQ6510**              | {term}`PI`      | ✅                |                                    |
| {term}`SSs <SS>`       | **3706A**                | {term}`PI`      | ✅                |                                    |

</div>

<div class="custom-table-center-cells device-support-table" title="Software Solution Support Levels">

<div class="custom-table-title">

_Software Solution Support Levels_

</div>

| Software<br>Solution | Command<br>Type | Basic<br>Control | Python API<br>Validation<br>Status |
| -------------------- | --------------- | ---------------- | ---------------------------------- |
| {term}`DPOJET`       | {term}`PI`      | ✅                | ✅                                  |

</div>

### Supported Connections

- REST API
- VISA *(TekVISA, NI-VISA and PyVISA-py)*
  - TCPIP
  - ASRL / Serial / RS-232 / RS-485
  - SOCKET
  - USBTMC *(no PyVISA-py support)*
  - GPIB *(no PyVISA-py support)*

## Documentation

See the full documentation at <https://tektronix.github.io/tm_devices/>

## Maintainers

Before reaching out to any maintainers directly, please first check if
your issue or question is already covered by any [open
issues](https://github.com/tektronix/tm_devices/issues). If the issue or
question you have is not already covered, please [file a new
issue](https://github.com/tektronix/tm_devices/issues/new/choose) or
start a
[discussion](https://github.com/tektronix/tm_devices/discussions) and
the maintainers will review and respond there.

- <tmdevicessupport@tektronix.com> - For technical support and
  questions.
- <opensource@tektronix.com> - For open-source policy and license
  questions.

## Contributing

Interested in contributing? Check out the [contributing
guidelines](https://tinyurl.com/tek-tm-devices/CONTRIBUTING.md). Please
note that this project is released with a [Code of
Conduct](https://tinyurl.com/tek-tm-devices/CODE_OF_CONDUCT.md). By
contributing to this project, you agree to abide by its terms.

## License

`tm_devices` was created by Tektronix. It is licensed under the terms of
the [Apache License 2.0](https://tinyurl.com/tek-tm-devices/LICENSE.md).

## Credits

`tm_devices` was created with
[cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html)
and the `py-pkgs-cookiecutter`
[template](https://py-pkgs-cookiecutter.readthedocs.io/en/latest/).
