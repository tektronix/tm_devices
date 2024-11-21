<div markdown="1" class="custom-badge-table">

|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Testing**       | [![Code testing status](https://github.com/tektronix/tm_devices/actions/workflows/test-code.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/test-code.yml) [![Docs testing status](https://github.com/tektronix/tm_devices/actions/workflows/test-docs.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/test-docs.yml) [![Coverage status](https://codecov.io/gh/tektronix/tm_devices/branch/main/graph/badge.svg)](https://codecov.io/gh/tektronix/tm_devices)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Code Quality**  | [![CodeQL status](https://github.com/tektronix/tm_devices/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/codeql-analysis.yml) [![CodeFactor grade](https://www.codefactor.io/repository/github/tektronix/tm_devices/badge)](https://www.codefactor.io/repository/github/tektronix/tm_devices) [![pre-commit status](https://results.pre-commit.ci/badge/github/tektronix/tm_devices/main.svg)](https://results.pre-commit.ci/latest/github/tektronix/tm_devices/main)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Package**       | [![PyPI: Package status](https://img.shields.io/pypi/status/tm_devices?logo=pypi)](https://pypi.org/project/tm_devices/) [![PyPI: Latest release version](https://img.shields.io/pypi/v/tm_devices?logo=pypi)](https://pypi.org/project/tm_devices/) [![PyPI: Supported Python versions](https://img.shields.io/pypi/pyversions/tm_devices?logo=python)](https://pypi.org/project/tm_devices/) [![PyPI: Downloads](https://static.pepy.tech/badge/tm-devices)](https://pepy.tech/project/tm_devices) [![License: Apache 2.0](https://img.shields.io/pypi/l/tm_devices)](https://github.com/tektronix/tm_devices/blob/main/LICENSE.md) [![Package build status](https://github.com/tektronix/tm_devices/actions/workflows/package-build.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/package-build.yml) [![PyPI upload status](https://github.com/tektronix/tm_devices/actions/workflows/package-release.yml/badge.svg?branch=main)](https://github.com/tektronix/tm_devices/actions/workflows/package-release.yml) |
| **Documentation** | [![ReadtheDocs Status](https://img.shields.io/readthedocs/tm-devices/stable?logo=readthedocs)](https://tm-devices.readthedocs.io/stable)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Code Style**    | [![Test style: pytest](https://img.shields.io/badge/test%20style-pytest-blue)](https://github.com/pytest-dev/pytest) [![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-black)](https://docs.astral.sh/ruff/formatter/) [![Docstring style: google](https://img.shields.io/badge/docstring%20style-google-tan)](https://google.github.io/styleguide/pyguide.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Linting**       | [![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) [![Docstring formatter: docformatter](https://img.shields.io/badge/docstring%20formatter-docformatter-tan)](https://github.com/PyCQA/docformatter) [![Type Checker: pyright](https://img.shields.io/badge/type%20checker-pyright-yellowgreen)](https://github.com/RobertCraigie/pyright-python) [![Linter: pylint](https://img.shields.io/badge/linter-pylint-purple)](https://github.com/pylint-dev/pylint) [![Linter: Ruff](https://img.shields.io/badge/linter-ruff-purple)](https://github.com/charliermarsh/ruff)                                                                                                                                                                                                                                                                                                                                                                                      |

</div>

---

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
[TekVISA](https://www.tek.com/en/search?keywords=tekvisa&facets=_templatename%3dsoftware%26parsedsoftwaretype%3dDriver&sort=desc)
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
  "TCPIP0::192.168.0.1::inst0::INSTR",
  "ASRL4::INSTR"
]
```

### Basic Script

```python
from tm_devices import DeviceManager

with DeviceManager() as device_manager:
    scope = device_manager.add_scope("192.168.0.1")
    scope.query("*IDN?")
    print(scope)
```

### Supported Devices & Software Solutions

> [!TIP]
> Visit the [Glossary](https://github.com/tektronix/tm_devices/blob/main/docs/glossary.md) to see definitions for all symbols and abbreviations.

<div markdown="1" class="custom-table-center-cells device-support-table">

<div markdown="1" class="custom-table-title">

_Device Support Levels_

</div>

| Type   | Series/Model             | Command<br>Type | Basic<br>Control | Python API<br>Validation<br>Status |
| ------ | ------------------------ | --------------- | ---------------- | ---------------------------------- |
| AFGs   | **AFG3000**              | PI              | ✅               |                                    |
|        | **AFG31xxx**             | PI              | ✅               |                                    |
| AWGs   | **AWG5000**              | PI              | ✅               |                                    |
|        | **AWG5200**              | PI              | ✅               |                                    |
|        | **AWG7000**              | PI              | ✅               | ✅                                 |
|        | **AWG70000**             | PI              | ✅               | ✅                                 |
| Scopes | **2 Series MSO**         | PI              | ✅               | ✅                                 |
|        | **3 Series MDO**         | PI              | ✅               | ✅                                 |
|        | **4 Series MSO**         | PI              | ✅               | ✅                                 |
|        | **4 Series B MSO**       | PI              | ✅               | ✅                                 |
|        | **5 Series MSO**         | PI              | ✅               | ✅                                 |
|        | **5 Series B MSO**       | PI              | ✅               | ✅                                 |
|        | **5 Series MSO (LP)**    | PI              | ✅               | ✅                                 |
|        | **6 Series MSO**         | PI              | ✅               | ✅                                 |
|        | **6 Series B MSO**       | PI              | ✅               | ✅                                 |
|        | **6 Series LPD**         | PI              | ✅               | ✅                                 |
|        | **MSO2000/B**            | PI              | ✅               |                                    |
|        | **DPO2000/B**            | PI              | ✅               |                                    |
|        | **MDO3000**              | PI              | ✅               | ✅                                 |
|        | **MDO4000/B/C**          | PI              | ✅               | ✅                                 |
|        | **MSO4000/B**            | PI              | ✅               | ✅                                 |
|        | **DPO4000/B**            | PI              | ✅               | ✅                                 |
|        | **MSO5000/B**            | PI              | ✅               | ✅                                 |
|        | **DPO5000/B**            | PI              | ✅               | ✅                                 |
|        | **DPO7000/C**            | PI              | ✅               | ✅                                 |
|        | **DPO70000/C/D/DX/SX**   | PI              | ✅               | ✅                                 |
|        | **DSA70000/C/D**         | PI              | ✅               | ✅                                 |
|        | **MSO70000/C/DX**        | PI              | ✅               | ✅                                 |
|        | **TSOVu**                | PI              | ✅               |                                    |
|        | **TekScope**             | PI              | ✅               | ✅                                 |
| PSUs   | **2200**                 | PI              | ✅               |                                    |
|        | **2220**                 | PI              | ✅               |                                    |
|        | **2230**                 | PI              | ✅               |                                    |
|        | **2231**                 | PI              | ✅               |                                    |
|        | **2280S**                | PI              | ✅               |                                    |
|        | **2281S**                | PI              | ✅               |                                    |
| SMUs   | **24xx Standard**        | PI              | ✅               |                                    |
|        | **24xx Interactive**     | TSP             | ✅               | ✅                                 |
|        | **26xxB**                | TSP             | ✅               | 🚧                                 |
|        | **2636B**                | TSP             | ✅               | ✅                                 |
|        | **Model 2601B-PULSE**    | TSP             | ✅               |                                    |
|        | **Model 2606B**          | TSP             | ✅               | 🚧                                 |
|        | **2651A**                | TSP             | ✅               | ✅                                 |
|        | **2657A**                | TSP             | ✅               |                                    |
|        | **6430 (electrometer)**  | PI              | ✅               |                                    |
|        | **6514 (electrometer)**  | PI              | ✅               |                                    |
|        | **6517B (electrometer)** | PI              | ✅               |                                    |
| MTs    | **TMT4**                 | API             | ✅               |                                    |
| DMMs   | **DMM6500**              | TSP             | ✅               |                                    |
|        | **DMM7510**              | TSP             | ✅               |                                    |
|        | **DMM7512**              | TSP             | ✅               |                                    |
| DAQs   | **DAQ6510**              | TSP             | ✅               |                                    |
| SSs    | **3706A**                | TSP             | ✅               |                                    |

</div>

<div markdown="1" class="custom-table-center-cells device-support-table">

<div markdown="1" class="custom-table-title">

_Software Solution Support Levels_

</div>

| Software<br>Solution | Command<br>Type | Basic<br>Control | Python API<br>Validation<br>Status |
| -------------------- | --------------- | ---------------- | ---------------------------------- |
| DPOJET               | PI              | ✅               | ✅                                 |
| SourceXpress         | PI              | ✅               | ✅                                 |

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

See the full documentation at <https://tm-devices.readthedocs.io/stable/>

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

Interested in contributing? Check out the [contributing guidelines](https://github.com/tektronix/tm_devices/blob/main/CONTRIBUTING.md). Please
note that this project is released with a [Code of Conduct](https://github.com/tektronix/tm_devices/blob/main/CODE_OF_CONDUCT.md). By
contributing to this project, you agree to abide by its terms.

## License

`tm_devices` was created by Tektronix. It is licensed under the terms of
the [Apache License 2.0](https://github.com/tektronix/tm_devices/blob/main/LICENSE.md).

## Security

The signatures of the files uploaded to [PyPI](https://pypi.org/project/tm-devices/) and each
[GitHub Release](https://github.com/tektronix/tm_devices/releases) can be verified using
the [GitHub CLI `attestation verify` command](https://cli.github.com/manual/gh_attestation_verify).
The artifact attestations can also be directly downloaded from the
[GitHub repo attestations page](https://github.com/tektronix/tm_devices/attestations) if desired.

```shell
gh attestation verify --owner tektronix <file>
```

## Credits

`tm_devices` was created with
[cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html)
and the `py-pkgs-cookiecutter`
[template](https://py-pkgs-cookiecutter.readthedocs.io/en/latest/).
