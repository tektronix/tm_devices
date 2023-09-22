<p style="text-align: center;">
<a href="https://github.com/tektronix/tm_devices/actions/workflows/test-code.yml"><img alt="Code testing status" src="https://github.com/tektronix/tm_devices/actions/workflows/test-code.yml/badge.svg?branch=main"></a>
<a href="https://github.com/tektronix/tm_devices/actions/workflows/test-docs.yml"><img alt="Docs testing status" src="https://github.com/tektronix/tm_devices/actions/workflows/test-docs.yml/badge.svg?branch=main"></a>
<a href="https://github.com/tektronix/tm_devices/actions/workflows/package-build.yml"><img alt="Package build status" src="https://github.com/tektronix/tm_devices/actions/workflows/package-build.yml/badge.svg?branch=main"></a>
<a href="https://codecov.io/gh/tektronix/tm_devices"><img alt="Coverage status" src="https://codecov.io/gh/tektronix/tm_devices/branch/main/graph/badge.svg"></a>
<a href="https://www.codefactor.io/repository/github/tektronix/tm_devices"><img alt="CodeFactor grade" src="https://www.codefactor.io/repository/github/tektronix/tm_devices/badge" /></a>
<a href="https://github.com/tektronix/tm_devices/actions/workflows/codeql-analysis.yml"><img alt="CodeQL status" src="https://github.com/tektronix/tm_devices/actions/workflows/codeql-analysis.yml/badge.svg?branch=main"></a>
<a href="https://github.com/pre-commit/pre-commit"><img alt="pre-commit enabled" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit"></a>
<a href="https://results.pre-commit.ci/latest/github/tektronix/tm_devices/main"><img alt="pre-commit status" src="https://results.pre-commit.ci/badge/github/tektronix/tm_devices/main.svg"></a>
<a href="https://tm_devices.readthedocs.io/en/stable/?badge=stable"><img alt="Documentation status" src="https://readthedocs.org/projects/tm_devices/badge/?version=stable"></a>
<a href="https://github.com/tektronix/tm_devices/blob/main/LICENSE.md"><img alt="License: Apache 2.0" src="https://img.shields.io/pypi/l/tm_devices"></a>
<a href="https://pypi.org/project/tm_devices/"><img alt="PyPI: Package status" src="https://img.shields.io/pypi/status/tm_devices?logo=pypi"></a>
<a href="https://pypi.org/project/tm_devices/"><img alt="PyPI: Latest release version" src="https://img.shields.io/pypi/v/tm_devices?logo=pypi"></a>
<a href="https://pypi.org/project/tm_devices/"><img alt="PyPI: Supported Python versions" src="https://img.shields.io/pypi/pyversions/tm_devices?logo=python"></a>
<a href="https://pepy.tech/project/tm_devices"><img alt="PyPI: Downloads" src="https://pepy.tech/badge/tm_devices"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-black"></a>
<a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/imports-isort-black"></a>
<a href="https://github.com/PyCQA/docformatter"><img alt="Docstring formatter: docformatter" src="https://img.shields.io/badge/docstring%20formatter-docformatter-tan"></a>
<a href="https://google.github.io/styleguide/pyguide.html"><img alt="Docstring style: google" src="https://img.shields.io/badge/docstring%20style-google-tan"></a>
<a href="https://github.com/pytest-dev/pytest"><img alt="Test style: pytest" src="https://img.shields.io/badge/test%20style-pytest-blue"></a>
<a href="https://github.com/RobertCraigie/pyright-python"><img alt="Type Checker: pyright" src="https://img.shields.io/badge/type%20checker-pyright-yellowgreen"></a>
<a href="https://github.com/pylint-dev/pylint"><img alt="Linter: pylint" src="https://img.shields.io/badge/linter-pylint-purple"></a>
<a href="https://github.com/charliermarsh/ruff"><img alt="Linter: Ruff" src="https://img.shields.io/badge/linter-ruff-purple"></a>
</p>

______________________________________________________________________

# tm_devices: Test & Measurement Device Management

`tm_devices` is a device management package which allows for better control and
usage of Test & Measurement devices in python scripts. This is accomplished by
using the [PyVISA](https://pyvisa.readthedocs.io/en/latest/) package to manage
connections and communication with devices. `tm_devices` gives users access to a
much higher level abstraction of device control by providing access to device
drivers with a complete Python API.

## Dependencies

`tm_devices` can be used without any external (non-python) dependencies on any operating system
thanks to the [PyVISA-py](https://pyvisa.readthedocs.io/projects/pyvisa-py/en/latest/)
VISA backend. However, in order to use any VISA functionality that PyVISA-py
does not implement, a third-party VISA backend such as
[NI-VISA](https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html)
can be installed. `tm_devices` will use an available VISA backend if one is
found and will fall back to using PyVISA-py if no other VISA backends are
installed.

## Installation

```console
pip install tm_devices
```

## Basic Usage

```python
from tm_devices import DeviceManager

with DeviceManager() as device_manager:
    scope = device_manager.add_scope("192.168.0.100")
    scope.query("*IDN?")
    print(scope)
```

### Supported Devices

```{admonition} Legend
---
class: hint
---
  | Symbol/Term | Definition       |
  |:-----------:|:-----------------|
  |  &#128679;  | Work in progress |
  |   &#9989;   | Implemented      |
  |  &#10060;   | Not Supported    |


See the [Glossary](#glossary) for information on abbreviations.
```

```{csv-table} Device Support Levels
---
name: device-support-table
align: center
header: Type, Series/Model, Command<br>Type, Basic<br>Control, Individual<br>Command<br>Python
  API
widths: auto
stub-columns: 1
class: custom-table-center-cells device-support-table
---
{term}`AFGs <AFG>`, **AFG3000**, {term}`PI`, ✅, 🚧
, **AFG31xxx**, {term}`PI`, ✅,
{term}`AWGs <AWG>`, **AWG5000**, {term}`PI`, ✅, 🚧
, **AWG5200**, {term}`PI`, ✅, 🚧
, **AWG7000**, {term}`PI`, ✅, 🚧
, **AWG70000**, {term}`PI`, ✅, 🚧
{term}`Scopes <Scope>`, **2 Series MSO**, {term}`PI`, ✅, 🚧
, **3 Series MDO**, {term}`PI`, ✅, 🚧
, **4 Series MSO**, {term}`PI`, ✅, 🚧
, **5 Series MSO**, {term}`PI`, ✅, 🚧
, **5 Series B MSO**, {term}`PI`, ✅, 🚧
, **5 Series MSO (LP)**, {term}`PI`, ✅, 🚧
, **6 Series MSO**, {term}`PI`, ✅, 🚧
, **6 Series B MSO**, {term}`PI`, ✅, 🚧
, **6 Series LPD**, {term}`PI`, ✅, 🚧
, **MSO2000/B**, {term}`PI`, ✅, 🚧
, **DPO2000/B**, {term}`PI`, ✅, 🚧
, **MDO3000**, {term}`PI`, ✅, 🚧
, **MDO4000/B/C**, {term}`PI`, ✅, 🚧
, **MSO4000/B**, {term}`PI`, ✅, 🚧
, **DPO4000/B**, {term}`PI`, ✅, 🚧
, **MSO5000/B**, {term}`PI`, ✅, 🚧
, **DPO5000/B**, {term}`PI`, ✅, 🚧
, **DPO7000/C**, {term}`PI`, ✅, 🚧
, **DPO70000/C/D/DX/SX**, {term}`PI`, ✅, 🚧
, **DSA70000/C/D**, {term}`PI`, ✅, 🚧
, **MSO70000/C/DX**, {term}`PI`, ✅, 🚧
, **TSOVu**, {term}`PI`, ✅,
, **TekScope**, {term}`PI`, ✅,
{term}`PSUs <PSU>`, **2200**, {term}`PI`, ✅,
, **2220**, {term}`PI`, ✅,
, **2230**, {term}`PI`, ✅,
, **2231**, {term}`PI`, ✅,
, **2280S**, {term}`PI`, ✅,
, **2281S**, {term}`PI`, ✅,
{term}`SMUs <SMU>`, **24xx Standard**, {term}`PI`, ✅,
, **24xx Interactive**, {term}`TSP`, ✅, 🚧
, **26xxB**, {term}`TSP`, ✅, 🚧
, **Model 2601B-PULSE**, {term}`TSP`, ✅, 🚧
, **Model 2606B**, {term}`TSP`, ✅, 🚧
, **2651A**, {term}`TSP`, ✅, 🚧
, **2657A**, {term}`TSP`, ✅, 🚧
, **6430 (electrometer)**, {term}`PI`, ✅,
, **6514 (electrometer)**, {term}`PI`, ✅,
, **6517B (electrometer)**, {term}`PI`, ✅,
{term}`MTs <MT>`, **TMT4**, {term}`API`, ✅,
{term}`DMMs <DMM>`, **DMM6500**, {term}`TSP`, ✅, 🚧
, **DMM7510**, {term}`TSP`, ✅, 🚧
, **DMM7512**, {term}`TSP`, ✅,
{term}`DAQs <DAQ>`, **DAQ6510**, {term}`TSP`, ✅, 🚧
{term}`SSs <SS>`, **3706A**, {term}`TSP`, ✅, 🚧
```

### Supported Connections

- REST API
- VISA _(NI-VISA and PyVISA-py)_
  - TCPIP
  - ASRL / Serial / RS-232 / RS-485
  - SOCKET
  - USBTMC _(no PyVISA-py support)_
  - GPIB _(no PyVISA-py support)_

## Maintainers

- Tektronix <https://pypi.org/user/Tektronix/>
- Nicholas Felt [nicholas.felt@tektronix.com](mailto:nicholas.felt@tektronix.com)

## Contributing

Interested in contributing? Check out the
[contributing guidelines](CONTRIBUTING.md). Please note that this project is
released with a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing to this
project, you agree to abide by its terms.

## License

`tm_devices` was created by Tektronix. It is licensed under the terms of the
[Apache License 2.0 license](LICENSE.md).

## Credits

`tm_devices` was created with
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/README.html) and the
`py-pkgs-cookiecutter`
[template](https://py-pkgs-cookiecutter.readthedocs.io/en/latest/).
