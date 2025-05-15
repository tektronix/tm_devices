# Configuration

How to configure the Device Manager to be able to connect to devices.

---

## Python Code

The Device Manager can be instantiated without any connections defined. Devices
can then be added to the Device Manager directly in the python code. Specific
configuration options can also be changed during runtime.

```python
# fmt: off
--8<-- "examples/miscellaneous/adding_devices.py"
```

See the [Example Usage](basic_usage.md) for more usage examples.

Also see the [`DeviceManager`][tm_devices.DeviceManager] API reference.

---

## Config File

Use a yaml (or toml) configuration file to avoid hard coding specific devices
into your scripts. The config file stores a list of device entries and runtime
behavior options.

The file allows you to set up a list of devices once and is easy to edit when
things change, but does not require modification with every script execution.

A config file can be **overruled** by an
[environment variable](#environment-variable) configuration. That means that if
you have both a config file defined and **either** of the environment variables set, the
config parser will **always** prioritize the environment variables. Make sure to
delete the environment variables if you want to switch back to the config file.

### Config File Path

The default location for the config file should be in the current working
directory:

`./tm_devices.yaml`

If an alternative path to the config file is needed, set the environment
variable:

`TM_DEVICES_CONFIG=<path_to_config_file>`

### Select a Pre-Configured Device from Device Manager

The Device Manager will look for any pre-configured devices and options on
instantiation and immediately open connections with all of them. Each device is
assigned a device number which can be used to recall a reference to that device.
Device numbers (1, 2,...) are determined sequentially by device type. That is,
the first SCOPE found will become "SCOPE 1", the second "SCOPE 2", etc.

Relying on device numbers means relying on order of declaration when working
with multiple devices of the same type. To avoid that, you are encouraged to
declare a unique name in the `alias` field with each device. Selecting your
device then looks like the code below:

```python
# Given a config file with a device entry with alias="custom_alias"
from tm_devices import DeviceManager

with DeviceManager() as device_manager:
    my_device = device_manager.get_device(alias="custom_alias")
```

### Device Configuration

#### Yaml Devices Syntax

```yaml
devices:
  - address: <ip_address_or_hostname>
    alias: <alias>
    connection_type: <connection_type>
    device_type: <device_type>
# TCPIP connection
  - address: <ip_address_or_hostname>
    alias: <alias>
    connection_type: TCPIP
    device_type: <device_type>
    lan_device_name: <lan_device_name>
# USB connection
  - address: <model>-<serial_number>
    alias: <alias>
    connection_type: USB
    device_type: <device_type>
# SOCKET connection
  - address: <ip_address_or_hostname>
    alias: <alias>
    connection_type: SOCKET
    device_type: <device_type>
    lan_port: <port_number>
# SERIAL connection
  - address: <serial_port>
    alias: <alias>
    connection_type: SERIAL
    device_type: <device_type>
    serial_config:
      baud_rate: 9600
      data_bits: 8
      flow_control: xon_xoff
      parity: none
      end_input: none
# GPIB connection
  - address: <gpib_address>
    gpib_board_number: <gpib_board_number>
    alias: <alias>
    connection_type: GPIB
    device_type: <device_type>
# REST API connection
  - address: <ip_address_or_hostname>
    alias: <alias>
    connection_type: REST_API
    device_type: <device_type>
    lan_port: <port_number>
    device_driver: <device_driver>
```

#### Legend for Device Configuration

- `device_type`
    - Valid options for `<device_type>`:
        - `AFG`: An Arbitrary Function Generator
        - `AWG`: An Arbitrary Waveform Generator
        - `DAQ`: An Data Acquisition Unit
        - `DMM`: An Digital Multimeter
        - `MT`: A Margin Tester
        - `PSU`: A Power Supply Unit
        - `SCOPE`: An Oscilloscope
        - `SMU`: A Source Measure Unit
        - `SS`: A Systems Switch
- `connection_type`
    - Defaults to `TCPIP` when not explicitly defined.
    - Valid options for `<connection_type>`:
        - VISA connection types:
            - `TCPIP`: A VISA connection over the TCPIP interface (default)
            - `USB`: A VISA connection over a physical USBTMC interface
            - `SERIAL`: A VISA connection over the serial (ASRL / RS-232 / RS-485) interface
            - `SOCKET`: A VISA connection over the SOCKET interface
            - `GPIB` : A VISA connection over the GPIB interface
        - Other valid connection types:
            - `REST_API`: A REST API connection over the network
- `address`
    - `<ip_address_or_hostname>`
        - Either the full IP address or system hostname is required to initialize
            the connection to the device.
        - Hostname is preferable, since it will gracefully handle a new DHCP lease
            which results in a potentially new IP address, but sometimes hostnames
            have resolution problems. In that case, an IP address usually works.
    - `<model>-<serial_number>`
        - If using the `USB` connection type for a VISA connection, address must be
            specified in the format `<model>-<serial_number>` so that the proper VISA
            resource expression can be created.
    - `<serial_port>`
        - The COM port to use, usually a number. For example, an usb-to-serial
            adapter connected to the USB port number 1 would show up as "COM1", so
            `address='1'`.
    - `<gpib_address>`
        - The GPIB address, a number in the range 0 to 30.
- `alias`
    - An optional field for a case-insensitive string that can be used as a key to
        select the device in the Device Manager instead of the device type and
        number. Without an alias, the device can still be accessed through a key
        generated from `<device_type>` string and the number of devices of the same
        type that were defined before it. For example: If there are two SCOPEs in
        the device list, one should be `SCOPE 1` and the other should be `SCOPE 2`.
    - Underscores and dashes are allowed, but other special characters are not
        allowed. Any alias provided will be converted into all capital letters for
        use later.
- `lan_port`
    - The open port, a number in the range 0 to 65535.
    - Required when the `<connection_type>` is `SOCKET`.
    - Optional when `<connection_type>` is `REST_API`
- `lan_device_name`
    - The LAN device name to connect on when `<connection_type>` is `TCPIP`.
    - If no LAN device name is provided in the configuration, `inst0` is used.
- `serial_config`
    - Configuration data for `SERIAL` connection type, which VISA documentation
        commonly refers to as ASRL.
    - **Both sides must be using the same settings, otherwise data looks like
        gibberish.**
        - `baud_rate:` The baud rate controls the communication frequency:.
            - Common rates: \[115200, 57600, 38400, 19200, 9600, 4800, 2400, 1200,
                600, 300\].
            - Different products may support ranges outside the commonly used rates
                listed here.
        - `data_bits:` The number of data bits in each character.
            - One of \[5, 6,
                7, 8\].
        - `flow_control:` Control for pausing/resuming data stream between slower
            devices.
            - Valid options: `none`, `xon_xoff`, `dtr_dsr`, or `rts_cts`
        - `parity:` Parity controls checksum bit (added to each data character)
            behavior.
            - Valid options: `none`, `odd` ,`even`, `mark`, or `space`.
        - `stop_bits:` Number of bits to use to indicate end of a character.
            - Valid options: `one`, `one_and_a_half`, or `two`.
        - `end_input:` Character(s) to indicate the end of a message transmission.
            - Valid options: `termination_break`, `termination_char`, `last_bit`, or
                `none`.
- `gpib_board_number`
    - The GPIB board number (also referred to as a controller) that the device is connected to.
    - If no board number is provided in the configuration, a board number of `0` is assumed.
- `device_driver`
    - The name of the Python driver class to use for the device (see the
        [`tm_devices.drivers`][] API reference for a complete list of all driver
        names).
    - Required when `<connection_type>` is `REST_API`
    - Ignored when `<connection_type>` is not `REST_API`

### Config Options

These options are used to configure runtime behaviors of `tm_devices`.

#### Yaml Options Syntax

```yaml
options:
  verbose_mode: false
  verbose_visa: false
  standalone: false
  setup_cleanup: false
  teardown_cleanup: false
  disable_command_verification: false
  retry_visa_connection: false
  default_visa_timeout: 5000
  check_for_updates: false
  log_console_level: INFO
  log_file_level: DEBUG
  log_file_directory: ./logs
  log_file_name: tm_devices_<timestamp>.log
  log_colored_output: false
  log_pyvisa_messages: false
  log_uncaught_exceptions: true
```

These are all `false` by default if not defined, set to `true` to modify the
runtime behavior configuration.

- `verbose_mode`
    - This config option will turn on more printouts to stdout.
- `verbose_visa`
    - This config option will turn on extremely verbose VISA logging to stdout.
- `standalone`
    - This config option specifies to use the PyVISA-py VISA backend, which
        does not require any actual visa.dll to exist on the system to work.
    - By default, the Device Manager will default to using whatever visa.dll it
        can find on the system.
- `setup_cleanup`
    - This config option will make the Device Manager run a cleanup on setup, so
        devices will get reset on connection.
- `teardown_cleanup`
    - This config option will make the Device Manager run a cleanup on teardown,
        so devices will get reset on close.
- `disable_command_verification`
    - This config option will disable command verification for all devices.
        - By default, command verification is enabled for all devices. Disabling the command verification
            (after verifying the script is working as intended) can have the effect of speeding up
            automation scripts by no longer checking each command after it is sent via the `.set_and_check()` method.
- `retry_visa_connection`
    - This config option will enable a second attempt when creating VISA connections,
        the second attempt is made after waiting, to allow the device time to become available.
- `default_visa_timeout`
    - This config option is used to set the default VISA timeout value in milliseconds.
        The default value of this config option is 5000 ms.
- `check_for_updates`
    - This config option will enable a check for any available updates on pypi.org for the
        package when the `DeviceManager` is instantiated.
- `log_console_level`
    - This config option is used to set the log level for the console output.
        The default value of this config option is "INFO". See the
        [`configure_logging()`][tm_devices.helpers.logging.configure_logging] function for more information.
- `log_file_level`
    - This config option is used to set the log level for the file output.
        The default value of this config option is "DEBUG". See the
        [`configure_logging()`][tm_devices.helpers.logging.configure_logging] function for more information.
- `log_file_directory`
    - This config option is used to set the directory where the log files will be saved.
        The default value of this config option is "./logs". See the
        [`configure_logging()`][tm_devices.helpers.logging.configure_logging] function for more information.
- `log_file_name`
    - This config option is used to set the name of the log file.
        The default value of this config option is a timestamped filename with the .log extension. See the
        [`configure_logging()`][tm_devices.helpers.logging.configure_logging] function for more information.
- `log_colored_output`
    - This config option is used to enable or disable colored output in the console.
        The default value of this config option is false. See the
        [`configure_logging()`][tm_devices.helpers.logging.configure_logging] function for more information.
- `log_pyvisa_messages`
    - This config option is used to enable or disable logging of PyVISA messages within the
        configured log file. The default value of this config option is false. See the
        [`configure_logging()`][tm_devices.helpers.logging.configure_logging] function for more information.
- `log_uncaught_exceptions`
    - This config option is used to enable or disable logging uncaught exceptions in the log file. The
        default value of this config option is true. Setting the `log_file_level` parameter
        to "NONE" will disable this feature regardless of the value of `log_uncaught_exceptions`. See the
        [`configure_logging()`][tm_devices.helpers.logging.configure_logging] function for more information.

### Sample Config File

#### YAML

```yaml
#########################[tm_devices.yaml]#########################
devices:
# TCPIP connection to SCOPE using hostname
  - address: MSO54-123456
    alias: my_scope_by_hostname
    device_type: SCOPE
# TCPIP connection to SMU using IP
  - address: 123.45.67.255
    alias: my_smu_by_ip
    connection_type: TCPIP
    device_type: SMU
# TCPIP connection to SCOPE using the High Speed LAN Instrument Protocol (HiSLIP)
  - address: MSO54-123456
    alias: my_scope_on_hislip0
    device_type: SCOPE
    lan_device_name: hislip0
# SOCKET connection to SCOPE types needs lan_port number
  - address: 123.45.67.255
    alias: my_scope_port4000
    connection_type: SOCKET
    device_type: SCOPE
    lan_port: 4000
# USB connection to SCOPE using hostname
  - address: MSO54-123456
    alias: my_scope
    connection_type: USB
    device_type: SCOPE
# SERIAL (aka ASRL) connection using serial COM1
  - address: '1'
    alias: my_smu_serial
    connection_type: SERIAL
    device_type: SMU
    # serial_config data defines parameters specific to serial communication protocols
    serial_config:
      baud_rate: 9600
      data_bits: 8
      flow_control: xon_xoff
      parity: none
      end_input: none
# REST_API connection to Margin Tester (MT)
  - address: TMT4-200015
    alias: my_mt
    connection_type: REST_API
    device_type: MT
    device_driver: TMT4
    lan_port: 5000
options:
  setup_cleanup: true
  teardown_cleanup: true
  disable_command_verification: true
  standalone: false
  verbose_mode: false
  verbose_visa: false
  retry_visa_connection: false
  default_visa_timeout: 10000  # 10 second default VISA timeout
  check_for_updates: false
  log_console_level: NONE    # completely disable console output
  log_file_level: DEBUG
  log_file_directory: ./logs
  log_file_name: custom_logfile.log    # customize the log file name
  log_colored_output: false
  log_pyvisa_messages: true  # log PyVISA messages in the log file
  log_uncaught_exceptions: true
```

#### TOML

```toml
#########################[tm_devices.toml]#########################
# TCPIP connection to SCOPE using hostname
[[devices]]
address = "MSO54-123456"
alias = "my_scope_by_hostname"
connection_type = "TCPIP"
device_type = "SCOPE"

# TCPIP connection to SMU using hostname
[[devices]]
address = "123.45.67.255"
alias = "my_smu_by_ip"
connection_type = "TCPIP"
device_type = "SMU"

# TCPIP connection to SCOPE using the High Speed LAN Instrument Protocol (HiSLIP)
[[devices]]
address = "MSO54-123456"
alias = "my_scope_by_hostname"
connection_type = "TCPIP"
device_type = "SCOPE"
lan_device_name = "hislip0"

# SOCKET connection to SCOPE types needs lan_port number
[[devices]]
address = "123.45.67.255"
alias = "my_scope_port4000"
connection_type = "SOCKET"
device_type = "SCOPE"
lan_port = 4000

# USB connection to SCOPE using hostname
[[devices]]
address = "MSO54-123456"
alias = "my_scope"
connection_type = "USB"
device_type = "SCOPE"

# SERIAL (aka ASRL) connection using serial COM1
[[devices]]
address = "1"
alias = "my_smu_serial"
connection_type = "SERIAL"
device_type = "SMU"
# serial_config data defines parameters specific to serial communication protocol
[devices.serial_config]
baud_rate = 9600
data_bits = 8
end_input = "none"
flow_control = "xon_xoff"
parity = "none"

# REST_API connection to Margin Tester
[[devices]]
address = "TMT4-200015"
alias = "my_mt"
connection_type = "REST_API"
device_type = "MT"
device_driver = "TMT4"
lan_port = 5000

[options]
setup_cleanup = true
teardown_cleanup = true
disable_command_verification = true
standalone = false
verbose_mode = false
verbose_visa = false
retry_visa_connection = false
default_visa_timeout = 10000         # 10 second default VISA timeout
check_for_updates = false
log_console_level = "NONE"           # completely disable console output
log_file_level = "DEBUG"
log_file_directory = "./logs"
log_file_name = "custom_logfile.log" # customize the log file name
log_colored_output = false
log_pyvisa_messages = true           # log PyVISA messages in the log file
log_uncaught_exceptions = true
```

---

## Environment Variable

Two environment variables, `TM_OPTIONS` and `TM_DEVICES`, can be used for
runtime configurations and have a **HIGHER** priority than the config file.

- `TM_OPTIONS` is a comma-delimited, all-uppercase list of enabled options
    names and values. Config options that act as boolean flags can be set simply by
    adding the option name to the environment variable. Config options that require non-boolean
    inputs should be specified with the option name followed by an equals sign and the value.
- `TM_DEVICES` is a `~~~`-delimited list of device entries.
    - Each device entry is a comma-delimited list of `<key>=<value>` pairs.

The main benefit of the environment variables over a config file is for
convenience in load-balanced or dynamic setups. For instance, in headless
execution scenarios where the list of devices needs to be temporary and
workspace variables can be changed easily per script executor.

There is no mechanism for merging the options and devices between the two config
methods; if **either** of the `TM_DEVICES` or `TM_OPTIONS` environment variables is
defined, the config file is completely ignored. If **either** of the environment variable(s) exist,
either permanently or temporarily, for the lifetime of the shell instance, they
will override any existing config file you have.

### Sample Environment Variable

Sample environment variable device configurations (with comments, not allowed in
environment variable)

```python
# fmt: off
# Sample SMU using IP address and PyVISA-py
TM_OPTIONS = "STANDALONE"
TM_DEVICES = "address=123.45.67.255,device_type=SMU"

# Sample scope using hostname and AFG using IP address with cleanup and a non-standard default VISA timeout
TM_OPTIONS = "SETUP_CLEANUP,TEARDOWN_CLEANUP,DEFAULT_VISA_TIMEOUT=10000"
TM_DEVICES = "address=MDO9876-C543210,device_type=SCOPE~~~address=123.45.67.255,device_type=AFG"

# Sample scope using IP address and AWG using hostname
TM_DEVICES = "address=123.45.67.255,device_type=SCOPE~~~address=AWG9876-C543210,device_type=AWG"

# Sample scope using IP address and port for socket connection
TM_DEVICES = "address=123.45.67.255,connection_type=SOCKET,device_type=SCOPE,lan_port=4000"

# Sample scope using USBTMC with an alias
TM_DEVICES = "address=MSO58-300026,alias=my-alias,connection_type=USB,device_type=SCOPE"

# Sample Margin Tester using IP address
TM_DEVICES = "address=123.45.6.789,connection_type=REST_API,device_type=MT,device_driver=TMT4"
```
