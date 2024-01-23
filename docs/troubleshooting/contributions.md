# Troubleshooting `tm_devices` Contributions

This goes over common issues which can occur when contributing to `tm_devices`
and how to deal with them.

______________________________________________________________________

## Unit tests have lots of VISA timeouts and failures in tests for areas that were not changed

### Problem:

Running unit tests takes a really long time and there are lots of VISA
failures/timeouts in tests for areas that did not have any changes.

Pytest will usually also emit failures and warnings that look like this:

```
>               raise AssertionError(message) from error_2
E               AssertionError: Unable to establish a VISA connection to TCPIP0::SS3706A-HOSTNAME::inst0::INSTR
E
E               This is the current ping output for the device at SS3706A-HOSTNAME:
E
E               Pinging SS3706A-HOSTNAME [xx.xxx.xxx.xxx] with 32 bytes of data:
E               Reply from xx.xxx.xxx.xxx: bytes=32 time=23ms TTL=56
E
E               Ping statistics for xx.xxx.xxx.xxx:
E                   Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
E               Approximate round trip times in milli-seconds:
E                   Minimum = 23ms, Maximum = 23ms, Average = 23ms
```

```
---------------------------- Captured stdout call -----------------------------
2023-04-10 08:50:21.664 - Creating Connection to SS 1 "SS-DEVICE"
------------------------------ Captured log call ------------------------------
WARNING  pyvisa:devices.py:143 No eom provided for InterfaceType.asrl, INSTR.Using LF.
WARNING  pyvisa:devices.py:143 No eom provided for InterfaceType.tcpip, INSTR.Using LF.
WARNING  pyvisa:devices.py:143 No eom provided for InterfaceType.tcpip, INSTR.Using LF.
WARNING  pyvisa:devices.py:143 No eom provided for InterfaceType.tcpip, INSTR.Using LF.
WARNING  pyvisa:devices.py:143 No eom provided for InterfaceType.tcpip, INSTR.Using LF.
WARNING  pyvisa:devices.py:143 No eom provided for InterfaceType.usb, INSTR.Using LF.
WARNING  pyvisa:devices.py:143 No eom provided for InterfaceType.tcpip, INSTR.Using LF.
```

### Solution:

This is usually caused by invalid entries in the `resources` list in the
`tests/sim_devices/devices.yaml` file.

Notice in this code example how the `device` key value doesn't match a valid
item from the `devices` list in `tests/sim_devices/psu/psu2281.yaml`. The
`device` key value **must match** a valid item (device) from the `devices` list
in the yaml file which is specified by the `filename` key.

```yaml
# tests/sim_devices/devices.yaml
resources:
  TCPIP::PSU2281-HOSTNAME::INSTR:
    device: psu2282
    filename: psu/psu2281.yaml
```

```yaml
# tests/sim_devices/psu/psu2281.yaml
spec: '1.1'
devices:
  psu2281:
    dialogues:
      - q: '*IDN?'
        r: KEITHLEY INSTRUMENTS INC.,MODEL 2281S-20-6,01234567,01.00
```

______________________________________________________________________

## Pyright is failing on unchanged code

### Problem:

When running `pre-commit`, Pyright is showing errors on lines of code that were
not touched by any recent changes.

```console
pyright..................................................................Failed
- hook id: pyright
- exit code: 1
No configuration file found.
pyproject.toml file found at <file-path>.
Loading pyproject.toml file at <file-path>\pyproject.toml
No include entries specified; assuming <file-path>
Auto-excluding **/node_modules
Auto-excluding **/__pycache__
Auto-excluding **/.*
Searching for source files
Found 825 source files
pyright 1.1.305
<file-path>\docs\conf.py
  <file-path>\docs\conf.py:155:40 - error: Type of parameter "obj" is unknown (reportUnknownParameterType)
  <file-path>\docs\conf.py:190:50 - error: Type of "pathname" is unknown (reportUnknownMemberType)
  <file-path>\docs\conf.py:191:12 - error: Type of "pathname" is unknown (reportUnknownMemberType)
  <file-path>\docs\conf.py:191:12 - error: Type of "endswith" is unknown (reportUnknownMemberType)
<file-path>\tests\conftest.py
  <file-path>\tests\conftest.py:11:25 - error: Type of "mocker_server" is unknown (reportUnknownVariableType)
<file-path>\tests\mock_server.py
  <file-path>\tests\mock_server.py:29:1 - error: Type of "mocker_server" is unknown (reportUnknownVariableType)
  <file-path>\tests\mock_server.py:33:2 - error: Type of "route" is unknown (reportUnknownMemberType)
  <file-path>\tests\mock_server.py:33:2 - error: Untyped function decorator obscures type of function; ignoring decorator (reportUntypedFunctionDecorator)
  <file-path>\tests\mock_server.py:43:2 - error: Type of "route" is unknown (reportUnknownMemberType)
  <file-path>\tests\mock_server.py:43:2 - error: Untyped function decorator obscures type of function; ignoring decorator (reportUntypedFunctionDecorator)
  <file-path>\tests\mock_server.py:53:2 - error: Type of "route" is unknown (reportUnknownMemberType)
  <file-path>\tests\mock_server.py:53:2 - error: Untyped function decorator obscures type of function; ignoring decorator (reportUntypedFunctionDecorator)
  <file-path>\tests\mock_server.py:63:2 - error: Type of "route" is unknown (reportUnknownMemberType)
  <file-path>\tests\mock_server.py:63:2 - error: Untyped function decorator obscures type of function; ignoring decorator (reportUntypedFunctionDecorator)
  <file-path>\tests\mock_server.py:73:2 - error: Type of "route" is unknown (reportUnknownMemberType)
  <file-path>\tests\mock_server.py:73:2 - error: Untyped function decorator obscures type of function; ignoring decorator (reportUntypedFunctionDecorator)
  <file-path>\tests\mock_server.py:83:2 - error: Type of "route" is unknown (reportUnknownMemberType)
  <file-path>\tests\mock_server.py:83:2 - error: Untyped function decorator obscures type of function; ignoring decorator (reportUntypedFunctionDecorator)
18 errors, 0 warnings, 0 informations
Completed in 58.189sec
```

### Solution:

This is caused by running `pre-commit` in a Python environment that doesn't have the
proper development dependencies installed.

See the [contributing guide](../CONTRIBUTING.md) for details on how to properly set up
and test changes using a virtual environment.

______________________________________________________________________

## Executable not found during `pre-commit`

Pre-commit is failing with "Executable not found" errors.

### Problem:

When running pre-commit, in either an Integrated Development Environment (IDE) or through
the command line, the virtual environment must be used so that all necessary
executables can be found.

`tm_devices` uses a few [local pre-commit hooks](https://pre-commit.com/#repository-local-hooks),
so if the environment is not correctly enabled, those hooks will fail.

```console
pre-commit run --all
check yaml...............................................................Passed
check toml...............................................................Passed
check json...............................................................Passed
fix requirements.txt.....................................................Passed
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
check for case conflicts.................................................Passed
check for merge conflicts................................................Passed
check for added large files..............................................Passed
forbid new submodules................................(no files to check)Skipped
pretty format json.......................................................Passed
Tabs remover.............................................................Passed
No-tabs checker..........................................................Passed
Validate ReadTheDocs Config..............................................Passed
Validate Dependabot Config (v2)..........................................Passed
Validate GitHub Actions..............................(no files to check)Skipped
Validate GitHub Workflows................................................Passed
blacken-docs.............................................................Passed
yamlfix..................................................................Passed
mdformat.................................................................Passed
Poetry check.............................................................Failed
- hook id: check-poetry
- exit code: 1

Executable `poetry` not found

toml-sort................................................................Failed
- hook id: toml-sort
- exit code: 1

Executable `toml-sort` not found

pylint...................................................................Failed
- hook id: pylint
- exit code: 1

Executable `pylint` not found

pyright..................................................................Failed
- hook id: pyright
- exit code: 1

Executable `pyright` not found

pyright-verifytypes......................................................Failed
- hook id: pyright-verifytypes
- exit code: 1

Executable `pyright` not found

pyroma...................................................................Failed
- hook id: pyroma
- exit code: 1

Executable `pyroma` not found

ruff.....................................................................Passed
black....................................................................Passed
docformatter.............................................................Passed
```

### Solution:

In order to fix this issue, first activate the virtual environment
(or set your IDE to use the correct Python interpreter for pre-commit hooks),
then update the installed dependencies,
then retry the command.

```console
# Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate.bat

# Update installed dependencies
python scripts/update_development_dependencies.py

# Re-run original, failing command
```

______________________________________________________________________

## `FileNotFoundError` when running tests

### Problem:

When running tests with a specified html output file, sometimes an internal error
can be raised causing the test run to crash.

```console
> pytest -k "test_docs" --self-contained-html --html=.results_doctests/results.html

platform win32 -- Python 3.11.4, pytest-7.4.1, pluggy-1.3.0 -- .env\Scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.11.4', 'Platform': 'Windows-10-10.0.19045-SP0', 'Packages': {'pytest': '7.4.1', 'pluggy': '1.3.0'}, 'Plugins': {'cov': '4.1.0', 'html': '4.0.0', 'metadata': '3.0.0', 'order': '1.1.0', 'profiling': '1.7.0'}}
configfile: pyproject.toml
plugins: cov-4.1.0, html-4.0.0, metadata-3.0.0, order-1.1.0, profiling-1.7.0
collected 177 items / 174 deselected / 3 selected

tests/test_docs.py::TestDocs::test_docs_linkcheck                                                                                                                                                                                                   [ 33%]
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File ".env\Lib\site-packages\_pytest\main.py", line 270, in wrap_session
INTERNALERROR>     session.exitstatus = doit(config, session) or 0
INTERNALERROR>                          ^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\_pytest\main.py", line 324, in _main
INTERNALERROR>     config.hook.pytest_runtestloop(session=session)
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_hooks.py", line 493, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_manager.py", line 115, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_callers.py", line 152, in _multicall
INTERNALERROR>     return outcome.get_result()
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_result.py", line 114, in get_result
INTERNALERROR>     raise exc.with_traceback(exc.__traceback__)
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_callers.py", line 77, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\_pytest\main.py", line 349, in pytest_runtestloop
INTERNALERROR>     item.config.hook.pytest_runtest_protocol(item=item, nextitem=nextitem)
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_hooks.py", line 493, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_manager.py", line 115, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_callers.py", line 152, in _multicall
INTERNALERROR>     return outcome.get_result()
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_result.py", line 114, in get_result
INTERNALERROR>     raise exc.with_traceback(exc.__traceback__)
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_callers.py", line 77, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\_pytest\runner.py", line 114, in pytest_runtest_protocol
INTERNALERROR>     runtestprotocol(item, nextitem=nextitem)
INTERNALERROR>   File ".env\Lib\site-packages\_pytest\runner.py", line 133, in runtestprotocol
INTERNALERROR>     reports.append(call_and_report(item, "call", log))
INTERNALERROR>                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\_pytest\runner.py", line 226, in call_and_report
INTERNALERROR>     hook.pytest_runtest_logreport(report=report)
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_hooks.py", line 493, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_manager.py", line 115, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_callers.py", line 113, in _multicall
INTERNALERROR>     raise exception.with_traceback(exception.__traceback__)
INTERNALERROR>   File ".env\Lib\site-packages\pluggy\_callers.py", line 77, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>           ^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".env\Lib\site-packages\pytest_html\basereport.py", line 251, in pytest_runtest_logreport
INTERNALERROR>     self._generate_report()
INTERNALERROR>   File ".env\Lib\site-packages\pytest_html\selfcontained_report.py", line 39, in _generate_report
INTERNALERROR>     super()._generate_report(self_contained=True)
INTERNALERROR>   File ".env\Lib\site-packages\pytest_html\basereport.py", line 65, in _generate_report
INTERNALERROR>     self._write_report(rendered_report)
INTERNALERROR>   File ".env\Lib\site-packages\pytest_html\basereport.py", line 134, in _write_report
INTERNALERROR>     with self._report_path.open("w", encoding="utf-8") as f:
INTERNALERROR>          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File "C:\Python311_64bit\Lib\pathlib.py", line 1044, in open
INTERNALERROR>     return io.open(self, mode, buffering, encoding, errors, newline)
INTERNALERROR>            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR> FileNotFoundError: [Errno 2] No such file or directory: '.results_doctests\\results.html'

```

### Solution:

This is caused by passing in a relative path to the html output file via the `--html` flag. Some
versions of [`pytest-html`](https://pytest-html.readthedocs.io/en/latest/index.html) don't convert
the path to an absolute path, so if a test changes the current working directory the html
reporter plugin will raise a `FileNotFoundError`.

In order to prevent this issue from occurring, simply pass in the full path to the html output
file when running pytest.

```console
# Linux
source .venv/bin/activate
pytest -k "test_docs" --self-contained-html --html=$(pwd)/.results_doctests/results.html

# Windows
.venv\Scripts\activate.bat
pytest -k "test_docs" --self-contained-html --html=%CD%\.results_doctests\results.html
```
