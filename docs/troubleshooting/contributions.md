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
