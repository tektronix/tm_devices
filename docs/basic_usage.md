# Basic Usage

A collection of examples showing the basics of how to use `tm_devices` in a
project.

## List available VISA devices

This will print the available VISA devices to the console when run from a shell terminal.

```console
$ list-visa-resources
[
  "TCPIP0::192.168.0.100::inst0::INSTR",
  "ASRL4::INSTR"
]
```

## Adding devices

Configure device connections as needed using the
[config file](configuration.md#config-file), an
[environment variable](configuration.md#environment-variable), or
via [Python code](configuration.md#python-code) (shown here). See the
[Configuration guide](configuration.md) for more information on how to
configure devices to connect with.

```python
# fmt: off
--8<-- "examples/miscellaneous/adding_devices.py"
```

## VISA backend selection

The [`DeviceManager`][tm_devices.DeviceManager] can be configured to use VISA backends from different VISA implementations.

```python
# fmt: off
--8<-- "examples/miscellaneous/visa_connection_selectivity.py"
```

## Alias usage

Devices can be given custom alias names and can be referenced by that alias.

```python
# fmt: off
--8<-- "examples/miscellaneous/alias_usage.py"
```

## Adding devices with environment variables

Device configuration information can be defined in an
[environment variable](configuration.md#environment-variable), usually done
outside the Python code for ease of automation
(shown inside the Python code here for demonstration purposes).

```python
# fmt: off
--8<-- "examples/miscellaneous/adding_devices_with_env_var.py"
```

## Disable command checking

This removes an extra query that verifies the property was set to the expected
value. This can be disabled at the device level or disabled for all devices by
disabling verification via the device manager.

```python
# fmt: off
--8<-- "examples/miscellaneous/disable_command_verification.py"
```

## Generate a signal using the Internal AFG

Use the Internal AFG to generate a 1 V, 10 MHz square wave with a 200 mV offset
on CH1 of the SCOPE.

- Requires a SCOPE with a license for the Internal AFG.
- Requires the Internal AFG output to be connected to CH1 on the SCOPE

```python
# fmt: off
--8<-- "examples/scopes/tekscope/generate_internal_afg_signal.py"
```

## Curve query saved to csv

Perform a curve query and save the results to a csv file.

- Requires an AFG connected to channel 1 on a SCOPE.

```python
# fmt: off
--8<-- "examples/scopes/tekscope/basic_curve_query.py"
```

## Saving / recalling a waveform and session

We can save a waveform on our scope to an external file. This is useful for
recalling previously saved waveforms if we ever need to use that waveform again.

The same can be done for scope sessions, sessions are essentially a snapshot of
the current state of our scope.

```python
# fmt: off
--8<-- "examples/scopes/tekscope/basic_save_recall.py"
```

## Configuring a measurement on a single sequence

A scope can be configured for a measurement on a single acquisition by setting the appropriate acquisition parameters
and adding the desired measurement on the selected channel.

```python
# fmt: off
--8<-- "examples/scopes/tekscope/get_acquisition_data.py"
```

## Adding DPOJET measurements and plots

DPOJET measurements and plots can be added on a DPO70KSX/C/7KC/DPO5KB scope.
Measurements report can be saved in a `.pdf` format.

```python
# fmt: off
--8<-- "examples/scopes/tekscope_70k/dpojet/adding_dpojet_measurements.py"
```

## Directly accessing the PyVISA resource object

The [PyVISA](https://pyvisa.readthedocs.io/en/latest/) resource object can be directly
accessed if there is a specific action that is not yet available directly through
the drivers in the `tm_devices` package.

```python
# fmt: off
--8<-- "examples/miscellaneous/pyvisa_resource_access.py"
```

## Dynamic reading buffers (SMUs)

Create and read from a dynamic buffer.

```python
# fmt: off
--8<-- "examples/source_measure_units/2600/reading_dynamic_buffers.py"
```

## Registering the Device Manager to be closed at program termination

Sometimes using the [`DeviceManager`][tm_devices.DeviceManager] class as a context manager is not feasible.
In those instances there is an alternative way to enforce the device manager to
close when the Python script execution is finished without needing to explicitly
call the [`.close()`][tm_devices.DeviceManager.close] method.

```python
# fmt: off
--8<-- "examples/miscellaneous/register_dm_atexit.py"
```

## Add custom device support

Sometimes there is a need to use a device that is not currently supported by
`tm_devices`. When this is the case, custom device driver classes can be created
and passed to the [`DeviceManager`][tm_devices.DeviceManager] when it is
first instantiated.

In order to do this a few things will need to be created:

1. A custom device class inheriting from one of the
    [main device types](advanced/architecture.md#main-device-types).
2. A mapping of the parsed model series string to the Python class.

```python
# fmt: off
--8<-- "examples/miscellaneous/custom_device_driver_support.py"
```
