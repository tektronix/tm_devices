# Troubleshooting `tm_devices` Usage

This goes over common issues which can occur when using `tm_devices` and how to
avoid them.

______________________________________________________________________

## Issues connecting to devices that are simulated using PyVISA-sim

### Problem:

The `DeviceManager` can't connect to devices that are defined in a PyVISA-sim
`yaml` file.

### Solution:

Make sure that the resource definitions in the `yaml` file are defined using all
CAPS. This is required because of how the configuration parser handles adding
new devices.

```yaml
spec: '1.1'

resources:
  TCPIP::DEVICE-HOSTNAME::INSTR:
    device: device 1
```

The `DeviceManager` will not be able to connect to a device defined as
`TCPIP::device-hostname::INSTR` in the `yaml` file. Changing the resource
definition to `TCPIP::DEVICE-HOSTNAME::INSTR` will allow the `DeviceManager` to
connect to the device.
