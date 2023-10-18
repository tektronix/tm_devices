.. start-custom-roles
   Custom roles and substitutions are defined below and can be used in this document.

.. role:: term

.. role:: doc

.. end-custom-roles

.. start-badges

.. list-table::
   :stub-columns: 1

   * - Testing
     - |Code testing status| |Docs testing status| |Coverage status|
   * - Code Quality
     - |CodeQL status| |CodeFactor grade| |pre-commit status|
   * - Package
     - |PyPI: Package status| |PyPI: Latest release version| |PyPI: Supported Python versions| |License: Apache 2.0| |PyPI: Downloads| |Package build status| |PyPI upload status| |TestPyPI upload status|
   * - Documentation
     - |Documentation status|
   * - Code Style
     - |Test style: pytest| |Code style: black| |Imports: isort| |Docstring style: google|
   * - Linting
     - |pre-commit enabled| |Docstring formatter: docformatter| |Type Checker: pyright| |Linter: pylint| |Linter: Ruff|

.. |Code testing status| image:: https://github.com/tektronix/tm_devices/actions/workflows/test-code.yml/badge.svg?branch=main
   :target: https://github.com/tektronix/tm_devices/actions/workflows/test-code.yml

.. |Docs testing status| image:: https://github.com/tektronix/tm_devices/actions/workflows/test-docs.yml/badge.svg?branch=main
   :target: https://github.com/tektronix/tm_devices/actions/workflows/test-docs.yml

.. |Package build status| image:: https://github.com/tektronix/tm_devices/actions/workflows/package-build.yml/badge.svg?branch=main
   :target: https://github.com/tektronix/tm_devices/actions/workflows/package-build.yml

.. |PyPI upload status| image:: https://github.com/tektronix/tm_devices/actions/workflows/package-release.yml/badge.svg?branch=main
   :target: https://github.com/tektronix/tm_devices/actions/workflows/package-release.yml

.. |TestPyPI upload status| image:: https://github.com/tektronix/tm_devices/actions/workflows/package-testpypi.yml/badge.svg?branch=main
   :target: https://github.com/tektronix/tm_devices/actions/workflows/package-testpypi.yml

.. |Coverage status| image:: https://codecov.io/gh/tektronix/tm_devices/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/tektronix/tm_devices

.. |CodeFactor grade| image:: https://www.codefactor.io/repository/github/tektronix/tm_devices/badge
   :target: https://www.codefactor.io/repository/github/tektronix/tm_devices

.. |CodeQL status| image:: https://github.com/tektronix/tm_devices/actions/workflows/codeql-analysis.yml/badge.svg?branch=main
   :target: https://github.com/tektronix/tm_devices/actions/workflows/codeql-analysis.yml

.. |pre-commit enabled| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
   :target: https://github.com/pre-commit/pre-commit

.. |pre-commit status| image:: https://results.pre-commit.ci/badge/github/tektronix/tm_devices/main.svg
   :target: https://results.pre-commit.ci/latest/github/tektronix/tm_devices/main

.. |Documentation status| image:: https://readthedocs.org/projects/tm-devices/badge/?version=latest
   :target: https://tm-devices.readthedocs.io/en/latest/?badge=latest

.. |License: Apache 2.0| image:: https://img.shields.io/pypi/l/tm_devices
   :target: https://tinyurl.com/tek-tm-devices/LICENSE.md

.. |PyPI: Package status| image:: https://img.shields.io/pypi/status/tm_devices?logo=pypi
   :target: https://pypi.org/project/tm_devices/

.. |PyPI: Latest release version| image:: https://img.shields.io/pypi/v/tm_devices?logo=pypi
   :target: https://pypi.org/project/tm_devices/

.. |PyPI: Supported Python versions| image:: https://img.shields.io/pypi/pyversions/tm_devices?logo=python
   :target: https://pypi.org/project/tm_devices/

.. |PyPI: Downloads| image:: https://pepy.tech/badge/tm_devices
   :target: https://pepy.tech/project/tm_devices

.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-black
   :target: https://github.com/psf/black

.. |Imports: isort| image:: https://img.shields.io/badge/imports-isort-black
   :target: https://pycqa.github.io/isort/

.. |Docstring formatter: docformatter| image:: https://img.shields.io/badge/docstring%20formatter-docformatter-tan
   :target: https://github.com/PyCQA/docformatter

.. |Docstring style: google| image:: https://img.shields.io/badge/docstring%20style-google-tan
   :target: https://google.github.io/styleguide/pyguide.html

.. |Test style: pytest| image:: https://img.shields.io/badge/test%20style-pytest-blue
   :target: https://github.com/pytest-dev/pytest

.. |Type Checker: pyright| image:: https://img.shields.io/badge/type%20checker-pyright-yellowgreen
   :target: https://github.com/RobertCraigie/pyright-python

.. |Linter: pylint| image:: https://img.shields.io/badge/linter-pylint-purple
   :target: https://github.com/pylint-dev/pylint

.. |Linter: Ruff| image:: https://img.shields.io/badge/linter-ruff-purple
   :target: https://github.com/charliermarsh/ruff

.. end-badges

--------------

tm_devices: Test & Measurement Device Management
================================================

``tm_devices`` is a device management package which allows for better
control and usage of Test & Measurement devices in python scripts. This
is accomplished by using the
`PyVISA <https://pyvisa.readthedocs.io/en/latest/>`__ package to manage
connections and communication with devices. ``tm_devices`` gives users
access to a much higher level abstraction of device control by providing
access to device drivers with a complete Python API.

Dependencies
------------

``tm_devices`` can be used without any external (non-python)
dependencies on any operating system thanks to the
`PyVISA-py <https://pyvisa.readthedocs.io/projects/pyvisa-py/en/latest/>`__
VISA backend. However, in order to use any VISA functionality that
PyVISA-py does not implement, a third-party VISA backend such as
`NI-VISA <https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html>`__
can be installed. ``tm_devices`` will use an available VISA backend if
one is found and will fall back to using PyVISA-py if no other VISA
backends are installed.

Installation
------------

.. code-block:: console

   pip install tm_devices


Basic Usage
-----------

Print Available VISA Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

   $ list-visa-resources
   [
     "TCPIP0::192.168.0.100::inst0::INSTR",
     "ASRL4::INSTR"
   ]

Basic Script
~~~~~~~~~~~~

.. code-block:: python

   from tm_devices import DeviceManager

   with DeviceManager() as device_manager:
       scope = device_manager.add_scope("192.168.0.100")
       scope.query("*IDN?")
       print(scope)


Supported Devices
~~~~~~~~~~~~~~~~~

.. admonition:: Legend
   :class: hint

   =========== ================
   Symbol/Term Definition
   =========== ================
   🚧          Work in progress
   ✅          Implemented
   ❌          Not Supported
   =========== ================

   See the :doc:`glossary` for information on abbreviations.


.. csv-table:: Device Support Levels
   :name: device-support-table
   :align: center
   :header-rows: 1
   :widths: auto
   :stub-columns: 1
   :class: custom-table-center-cells device-support-table

   "| Type", "| Series/Model", "| Command
   | Type", "| Basic
   | Control", "| Python API
   | Validation
   | Status"
   :term:`AFGs <AFG>`, **AFG3000**, :term:`PI`, ✅, 🚧
   , **AFG31xxx**, :term:`PI`, ✅,
   :term:`AWGs <AWG>`, **AWG5000**, :term:`PI`, ✅, 🚧
   , **AWG5200**, :term:`PI`, ✅, 🚧
   , **AWG7000**, :term:`PI`, ✅, 🚧
   , **AWG70000**, :term:`PI`, ✅, 🚧
   :term:`Scopes <Scope>`, **2 Series MSO**, :term:`PI`, ✅, 🚧
   , **3 Series MDO**, :term:`PI`, ✅, 🚧
   , **4 Series MSO**, :term:`PI`, ✅, 🚧
   , **5 Series MSO**, :term:`PI`, ✅, 🚧
   , **5 Series B MSO**, :term:`PI`, ✅, 🚧
   , **5 Series MSO (LP)**, :term:`PI`, ✅, 🚧
   , **6 Series MSO**, :term:`PI`, ✅, 🚧
   , **6 Series B MSO**, :term:`PI`, ✅, 🚧
   , **6 Series LPD**, :term:`PI`, ✅, 🚧
   , **MSO2000/B**, :term:`PI`, ✅, 🚧
   , **DPO2000/B**, :term:`PI`, ✅, 🚧
   , **MDO3000**, :term:`PI`, ✅, 🚧
   , **MDO4000/B/C**, :term:`PI`, ✅, 🚧
   , **MSO4000/B**, :term:`PI`, ✅, 🚧
   , **DPO4000/B**, :term:`PI`, ✅, 🚧
   , **MSO5000/B**, :term:`PI`, ✅, 🚧
   , **DPO5000/B**, :term:`PI`, ✅, 🚧
   , **DPO7000/C**, :term:`PI`, ✅, 🚧
   , **DPO70000/C/D/DX/SX**, :term:`PI`, ✅, 🚧
   , **DSA70000/C/D**, :term:`PI`, ✅, 🚧
   , **MSO70000/C/DX**, :term:`PI`, ✅, 🚧
   , **TSOVu**, :term:`PI`, ✅,
   , **TekScope**, :term:`PI`, ✅,
   :term:`PSUs <PSU>`, **2200**, :term:`PI`, ✅,
   , **2220**, :term:`PI`, ✅,
   , **2230**, :term:`PI`, ✅,
   , **2231**, :term:`PI`, ✅,
   , **2280S**, :term:`PI`, ✅,
   , **2281S**, :term:`PI`, ✅,
   :term:`SMUs <SMU>`, **24xx Standard**, :term:`PI`, ✅,
   , **24xx Interactive**, :term:`TSP`, ✅, 🚧
   , **26xxB**, :term:`TSP`, ✅, 🚧
   , **Model 2601B-PULSE**, :term:`TSP`, ✅, 🚧
   , **Model 2606B**, :term:`TSP`, ✅, 🚧
   , **2651A**, :term:`TSP`, ✅, 🚧
   , **2657A**, :term:`TSP`, ✅, 🚧
   , **6430 (electrometer)**, :term:`PI`, ✅,
   , **6514 (electrometer)**, :term:`PI`, ✅,
   , **6517B (electrometer)**, :term:`PI`, ✅,
   :term:`MTs <MT>`, **TMT4**, :term:`API`, ✅,
   :term:`DMMs <DMM>`, **DMM6500**, :term:`TSP`, ✅, 🚧
   , **DMM7510**, :term:`TSP`, ✅, 🚧
   , **DMM7512**, :term:`TSP`, ✅,
   :term:`DAQs <DAQ>`, **DAQ6510**, :term:`TSP`, ✅, 🚧
   :term:`SSs <SS>`, **3706A**, :term:`TSP`, ✅, 🚧

Supported Connections
~~~~~~~~~~~~~~~~~~~~~

-  REST API
-  VISA *(NI-VISA and PyVISA-py)*

   -  TCPIP
   -  ASRL / Serial / RS-232 / RS-485
   -  SOCKET
   -  USBTMC *(no PyVISA-py support)*
   -  GPIB *(no PyVISA-py support)*

Documentation
-------------

See the full documentation at `<https://tm-devices.readthedocs.io>`__

Maintainers
-----------

-  Tektronix opensource@tektronix.com
-  Nicholas Felt nicholas.felt@tektronix.com

Contributing
------------

Interested in contributing? Check out the `contributing
guidelines <CONTRIBUTING.md>`_. Please note that this project is
released with a `Code of Conduct <CODE_OF_CONDUCT.md>`_. By
contributing to this project, you agree to abide by its terms.

License
-------

``tm_devices`` was created by Tektronix. It is licensed under the terms
of the `Apache License 2.0 <LICENSE.md>`_.

Credits
-------

``tm_devices`` was created with
`cookiecutter <https://cookiecutter.readthedocs.io/en/latest/README.html>`__
and the ``py-pkgs-cookiecutter``
`template <https://py-pkgs-cookiecutter.readthedocs.io/en/latest/>`__.
