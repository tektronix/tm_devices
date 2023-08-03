# Basic Usage

A collection of examples showing the basics of how to use `tm_devices` in a
project.

## Adding devices

```{literalinclude} ../examples/miscellaneous/adding_devices.py
---
language: python
---
```

## Alias usage

Devices can be given custom alias names and can be referenced by that alias.

```{literalinclude} ../examples/miscellaneous/alias_usage.py
---
language: python
---
```

## Adding devices with environment variables

Configure device environment variables as needed using the config file or
[Python](#adding-devices). See the [Configuration guide](configuration.md) for
more information on how to do that.

```{literalinclude} ../examples/miscellaneous/adding_devices_with_env_var.py
---
language: python
---
```

## Disable command checking

This removes an extra query that verifies the property was set to the expected
value. This can be disabled at the device level or disabled for all devices by
disabling verification via the device manager.

```{literalinclude} ../examples/miscellaneous/disable_command_verification.py
---
language: python
---
```

## Generate a signal using the Internal AFG

Use the Internal AFG to generate a 1 V, 10 MHz square wave with a 200 mV offset
on CH1 of the SCOPE.

- Requires a SCOPE with a license for the Internal AFG.
- Requires the Internal AFG output to be connected to CH1 on the SCOPE

```{literalinclude} ../examples/scopes/tekscope/generate_internal_afg_signal.py
---
language: python
---
```

## Curve query saved to csv

Perform a curve query and save the results to a csv file.

- Requires an AFG connected to channel 1 on a SCOPE.

```{literalinclude} ../examples/scopes/tekscope/basic_curve_query.py
---
language: python
---
```

## Saving / recalling a waveform and session

We can save a waveform on our scope to an external file. This is useful for
recalling previously saved waveforms if we ever need to use that waveform again.

The same can be done for scope sessions, sessions are essentially a snapshot of
the current state of our scope.

```{literalinclude} ../examples/scopes/tekscope/basic_save_recall.py
---
language: python
---
```

## Directly accessing the PyVISA resource object

The [PyVISA](https://pyvisa.readthedocs.io/en/latest/) resource object can be directly
accessed if there is a specific action that is not yet available directly through
the drivers in the `tm_devices` package.

```{literalinclude} ../examples/miscellaneous/pyvisa_resource_access.py
---
language: python
---
```

## Dynamic reading buffers (SMUs)

Create and read from a dynamic buffer.

```{literalinclude} ../examples/source_measure_units/2600/reading_dynamic_buffers.py
---
language: python
---
```

## Registering the Device Manager to be closed at program termination

Sometimes using the `DeviceManager` class as a context manager isn't feasible.
In those instances there is an alternative way to enforce the device manager to
close when the Python script execution is finished without needing to explicitly
call the `.close()` method.

```{literalinclude} ../examples/miscellaneous/register_dm_atexit.py
---
language: python
---
```

## Add custom device support

Sometimes there is a need to use a device that is not currently supported by
`tm_devices`. When this is the case, custom device driver classes can be created
and passed to the {py:obj}`DeviceManager <tm_devices.DeviceManager>` when it is
first instantiated.

In order to do this a few things will need to be created:

1. A custom device class inheriting from one of the
   [main device types](advanced/architecture.md#main-device-types).
2. A mapping of the parsed model series string to the Python class.

```{literalinclude} ../examples/miscellaneous/custom_device_driver_support.py
---
language: python
emphasize-lines: 9-14,21-23,26
---
```
