"""The console output and level of logging outputs in the log file can be configured as needed."""

from tm_devices import configure_logging, DeviceManager, LoggingLevels
from tm_devices.drivers import MSO6B

# NOTE: This configuration will prevent any logging config options from a config file or
# environment variable from being used.
configure_logging(
    log_console_level=LoggingLevels.NONE,  # completely disable console logging
    log_file_level=LoggingLevels.DEBUG,  # log everything to the file
    log_file_directory="./log_files",  # save the log file in the "./log_files" directory
    log_file_name="custom_log_filename.log",  # customize the filename
    log_pyvisa_messages=True,  # include all the pyvisa debug messages in the same log file
    log_uncaught_exceptions=True,  # log uncaught exceptions (this is the default behavior)
)

with DeviceManager(verbose=False) as dm:
    scope: MSO6B = dm.add_scope("192.168.0.1")
    scope.curve_query(1)
    scope.check_port_connection(4000)
    scope.check_network_connection()
    scope.check_visa_connection()
