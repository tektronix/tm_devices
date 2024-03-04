"""An example of adding devices via Python code."""

from tm_devices import DeviceManager
from tm_devices.helpers import (
    DMConfigOptions,
    PYVISA_PY_BACKEND,
    SerialConfig,
    SYSTEM_DEFAULT_VISA_BACKEND,
)

# Specific config options can optionally be passed in when creating
# the DeviceManager via a dataclass, they are used to update any existing
# configuration options from a config file.
CONFIG_OPTIONS = DMConfigOptions(
    setup_cleanup=True,  # update the value for this option, all other options will remain untouched
)


# Create the DeviceManager, turning on verbosity and passing in some specific configuration values.
with DeviceManager(
    verbose=True,  # optional argument
    config_options=CONFIG_OPTIONS,  # optional argument
) as device_manager:
    # Explicitly specify to use the system VISA backend, this is the default,
    # **this code is not required** to use the system default.
    device_manager.visa_library = SYSTEM_DEFAULT_VISA_BACKEND

    # Enable resetting the devices when connecting and closing
    device_manager.setup_cleanup_enabled = True
    device_manager.teardown_cleanup_enabled = True

    # Note: USB and GPIB connections are not supported with PyVISA-py backend
    psu = device_manager.add_psu("MODEL-SERIAL", connection_type="USB")

    # Use the PyVISA-py backend
    device_manager.visa_library = PYVISA_PY_BACKEND

    # Add a device using a hostname
    scope = device_manager.add_scope("MSO56-100083")
    print(scope)

    # Add a device using an IP address and optional alias
    awg = device_manager.add_awg("192.168.0.1", alias="AWG5k")
    print(awg)

    # Add a device using a VISA resource address string,
    # it auto-detects the connection type is TCPIP.
    scope_2 = device_manager.add_scope("TCPIP0::192.168.0.3::inst0::INSTR")

    # Add a device using an IP address and optional alias and socket port
    mt = device_manager.add_mt("192.168.0.2", "TMT4", alias="margin tester", port=5000)

    # Add a device using a serial connection, define a SerialConfig for serial settings
    serial_settings = SerialConfig(
        baud_rate=9600,
        data_bits=8,
        flow_control=SerialConfig.FlowControl.xon_xoff,
        parity=SerialConfig.Parity.none,
        stop_bits=SerialConfig.StopBits.one,
        end_input=SerialConfig.Termination.none,
    )
    smu = device_manager.add_smu("1", connection_type="SERIAL", serial_config=serial_settings)

    # Remove devices
    device_manager.remove_all_devices()
