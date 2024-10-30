# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The scan commands module.

These commands are used in the following models:
DAQ6510

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - scan.add()
    - scan.addsinglestep()
    - scan.addwrite()
    - scan.buffer
    - scan.bypass
    - scan.channel.stimulus
    - scan.create()
    - scan.export()
    - scan.learnlimits()
    - scan.list()
    - scan.measure.interval
    - scan.measure.stimulus
    - scan.mode
    - scan.monitor.channel
    - scan.monitor.limit.high.value
    - scan.monitor.limit.low.value
    - scan.monitor.mode
    - scan.restart
    - scan.scancount
    - scan.scaninterval
    - scan.start.stimulus
    - scan.state()
    - scan.stepcount
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class ScanStart(BaseTSPCmd):
    """The ``scan.start`` command tree.

    Properties and methods:
        - ``.stimulus``: The ``scan.start.stimulus`` attribute.
    """

    @property
    def stimulus(self) -> str:
        """Access the ``scan.start.stimulus`` attribute.

        Description:
            - This attribute determines which event starts the scan.

        Usage:
            - Accessing this property will send the ``print(scan.start.stimulus)`` query.
            - Setting this property to a value will send the ``scan.start.stimulus = value``
              command.

        TSP Syntax:
            ```
            - scan.start.stimulus = value
            - print(scan.start.stimulus)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``scan.start.stimulus`` attribute.

        Description:
            - This attribute determines which event starts the scan.

        Usage:
            - Accessing this property will send the ``print(scan.start.stimulus)`` query.
            - Setting this property to a value will send the ``scan.start.stimulus = value``
              command.

        TSP Syntax:
            ```
            - scan.start.stimulus = value
            - print(scan.start.stimulus)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class ScanMonitorLimitLow(BaseTSPCmd):
    """The ``scan.monitor.limit.low`` command tree.

    Properties and methods:
        - ``.value``: The ``scan.monitor.limit.low.value`` attribute.
    """

    @property
    def value(self) -> str:
        """Access the ``scan.monitor.limit.low.value`` attribute.

        Description:
            - This attribute defines the low limit to be used by the scan monitor.

        Usage:
            - Accessing this property will send the ``print(scan.monitor.limit.low.value)`` query.
            - Setting this property to a value will send the
              ``scan.monitor.limit.low.value = value`` command.

        TSP Syntax:
            ```
            - scan.monitor.limit.low.value = value
            - print(scan.monitor.limit.low.value)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".value"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.value)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.value`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @value.setter
    def value(self, value: Union[str, float]) -> None:
        """Access the ``scan.monitor.limit.low.value`` attribute.

        Description:
            - This attribute defines the low limit to be used by the scan monitor.

        Usage:
            - Accessing this property will send the ``print(scan.monitor.limit.low.value)`` query.
            - Setting this property to a value will send the
              ``scan.monitor.limit.low.value = value`` command.

        TSP Syntax:
            ```
            - scan.monitor.limit.low.value = value
            - print(scan.monitor.limit.low.value)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".value", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.value = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.value`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class ScanMonitorLimitHigh(BaseTSPCmd):
    """The ``scan.monitor.limit.high`` command tree.

    Properties and methods:
        - ``.value``: The ``scan.monitor.limit.high.value`` attribute.
    """

    @property
    def value(self) -> str:
        """Access the ``scan.monitor.limit.high.value`` attribute.

        Description:
            - This attribute specifies the high limit to be used by the scan monitor.

        Usage:
            - Accessing this property will send the ``print(scan.monitor.limit.high.value)`` query.
            - Setting this property to a value will send the
              ``scan.monitor.limit.high.value = value`` command.

        TSP Syntax:
            ```
            - scan.monitor.limit.high.value = value
            - print(scan.monitor.limit.high.value)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".value"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.value)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.value`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @value.setter
    def value(self, value: Union[str, float]) -> None:
        """Access the ``scan.monitor.limit.high.value`` attribute.

        Description:
            - This attribute specifies the high limit to be used by the scan monitor.

        Usage:
            - Accessing this property will send the ``print(scan.monitor.limit.high.value)`` query.
            - Setting this property to a value will send the
              ``scan.monitor.limit.high.value = value`` command.

        TSP Syntax:
            ```
            - scan.monitor.limit.high.value = value
            - print(scan.monitor.limit.high.value)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".value", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.value = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.value`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class ScanMonitorLimit(BaseTSPCmd):
    """The ``scan.monitor.limit`` command tree.

    Properties and methods:
        - ``.high``: The ``scan.monitor.limit.high`` command tree.
        - ``.low``: The ``scan.monitor.limit.low`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = ScanMonitorLimitHigh(device, f"{self._cmd_syntax}.high")
        self._low = ScanMonitorLimitLow(device, f"{self._cmd_syntax}.low")

    @property
    def high(self) -> ScanMonitorLimitHigh:
        """Return the ``scan.monitor.limit.high`` command tree.

        Sub-properties and sub-methods:
            - ``.value``: The ``scan.monitor.limit.high.value`` attribute.
        """
        return self._high

    @property
    def low(self) -> ScanMonitorLimitLow:
        """Return the ``scan.monitor.limit.low`` command tree.

        Sub-properties and sub-methods:
            - ``.value``: The ``scan.monitor.limit.low.value`` attribute.
        """
        return self._low


class ScanMonitor(BaseTSPCmd):
    """The ``scan.monitor`` command tree.

    Properties and methods:
        - ``.channel``: The ``scan.monitor.channel`` attribute.
        - ``.limit``: The ``scan.monitor.limit`` command tree.
        - ``.mode``: The ``scan.monitor.mode`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._limit = ScanMonitorLimit(device, f"{self._cmd_syntax}.limit")

    @property
    def channel(self) -> str:
        """Access the ``scan.monitor.channel`` attribute.

        Description:
            - This attribute defines which channel to monitor for a limit to be reached before
              starting the scan.

        Usage:
            - Accessing this property will send the ``print(scan.monitor.channel)`` query.
            - Setting this property to a value will send the ``scan.monitor.channel = value``
              command.

        TSP Syntax:
            ```
            - scan.monitor.channel = value
            - print(scan.monitor.channel)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".channel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.channel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.channel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @channel.setter
    def channel(self, value: Union[str, float]) -> None:
        """Access the ``scan.monitor.channel`` attribute.

        Description:
            - This attribute defines which channel to monitor for a limit to be reached before
              starting the scan.

        Usage:
            - Accessing this property will send the ``print(scan.monitor.channel)`` query.
            - Setting this property to a value will send the ``scan.monitor.channel = value``
              command.

        TSP Syntax:
            ```
            - scan.monitor.channel = value
            - print(scan.monitor.channel)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".channel", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.channel = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.channel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limit(self) -> ScanMonitorLimit:
        """Return the ``scan.monitor.limit`` command tree.

        Sub-properties and sub-methods:
            - ``.high``: The ``scan.monitor.limit.high`` command tree.
            - ``.low``: The ``scan.monitor.limit.low`` command tree.
        """
        return self._limit

    @property
    def mode(self) -> str:
        """Access the ``scan.monitor.mode`` attribute.

        Description:
            - This attribute determines if a scan starts immediately when triggered or after
              measurements reach a set value.

        Usage:
            - Accessing this property will send the ``print(scan.monitor.mode)`` query.
            - Setting this property to a value will send the ``scan.monitor.mode = value`` command.

        TSP Syntax:
            ```
            - scan.monitor.mode = value
            - print(scan.monitor.mode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".mode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.mode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @mode.setter
    def mode(self, value: Union[str, float]) -> None:
        """Access the ``scan.monitor.mode`` attribute.

        Description:
            - This attribute determines if a scan starts immediately when triggered or after
              measurements reach a set value.

        Usage:
            - Accessing this property will send the ``print(scan.monitor.mode)`` query.
            - Setting this property to a value will send the ``scan.monitor.mode = value`` command.

        TSP Syntax:
            ```
            - scan.monitor.mode = value
            - print(scan.monitor.mode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".mode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.mode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class ScanMeasure(BaseTSPCmd):
    """The ``scan.measure`` command tree.

    Properties and methods:
        - ``.interval``: The ``scan.measure.interval`` attribute.
        - ``.stimulus``: The ``scan.measure.stimulus`` attribute.
    """

    @property
    def interval(self) -> str:
        """Access the ``scan.measure.interval`` attribute.

        Description:
            - This attribute specifies the interval time between measurement requests.

        Usage:
            - Accessing this property will send the ``print(scan.measure.interval)`` query.
            - Setting this property to a value will send the ``scan.measure.interval = value``
              command.

        TSP Syntax:
            ```
            - scan.measure.interval = value
            - print(scan.measure.interval)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".interval"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.interval)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.interval`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @interval.setter
    def interval(self, value: Union[str, float]) -> None:
        """Access the ``scan.measure.interval`` attribute.

        Description:
            - This attribute specifies the interval time between measurement requests.

        Usage:
            - Accessing this property will send the ``print(scan.measure.interval)`` query.
            - Setting this property to a value will send the ``scan.measure.interval = value``
              command.

        TSP Syntax:
            ```
            - scan.measure.interval = value
            - print(scan.measure.interval)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".interval", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.interval = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.interval`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``scan.measure.stimulus`` attribute.

        Description:
            - This attribute selects the trigger for the measurement.

        Usage:
            - Accessing this property will send the ``print(scan.measure.stimulus)`` query.
            - Setting this property to a value will send the ``scan.measure.stimulus = value``
              command.

        TSP Syntax:
            ```
            - scan.measure.stimulus = value
            - print(scan.measure.stimulus)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``scan.measure.stimulus`` attribute.

        Description:
            - This attribute selects the trigger for the measurement.

        Usage:
            - Accessing this property will send the ``print(scan.measure.stimulus)`` query.
            - Setting this property to a value will send the ``scan.measure.stimulus = value``
              command.

        TSP Syntax:
            ```
            - scan.measure.stimulus = value
            - print(scan.measure.stimulus)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class ScanChannel(BaseTSPCmd):
    """The ``scan.channel`` command tree.

    Properties and methods:
        - ``.stimulus``: The ``scan.channel.stimulus`` attribute.
    """

    @property
    def stimulus(self) -> str:
        """Access the ``scan.channel.stimulus`` attribute.

        Description:
            - This attribute determines which trigger event causes the channel action to occur.

        Usage:
            - Accessing this property will send the ``print(scan.channel.stimulus)`` query.
            - Setting this property to a value will send the ``scan.channel.stimulus = value``
              command.

        TSP Syntax:
            ```
            - scan.channel.stimulus = value
            - print(scan.channel.stimulus)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``scan.channel.stimulus`` attribute.

        Description:
            - This attribute determines which trigger event causes the channel action to occur.

        Usage:
            - Accessing this property will send the ``print(scan.channel.stimulus)`` query.
            - Setting this property to a value will send the ``scan.channel.stimulus = value``
              command.

        TSP Syntax:
            ```
            - scan.channel.stimulus = value
            - print(scan.channel.stimulus)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Scan(BaseTSPCmd):
    """The ``scan`` command tree.

    Constants:
        - ``.ABORTED``: The scan was canceled.
        - ``.BUILDING``: The instrument is building the scan.
        - ``.COUNT_INFINITE``: Set the number of times the scan is repeated to repeated until
          aborted.
        - ``.EMPTY``: Scan is not set up.
        - ``.FAILED``: The scan failed.
        - ``.MODE_FIXED_ABR``: Sets the relay action when the scan starts to automatic backplane
          relay.
        - ``.MODE_HIGH``: Start the scan when the measurement exceeds the value set by
          scan.monitor.limit.high.value.
        - ``.MODE_LOW``: Start the scan when the measurement is below the value set by
          scan.monitor.limit.low.value.
        - ``.MODE_OFF``: Start the scan without waiting for a specific value.
        - ``.MODE_OPEN_ALL``: Sets the relay action when the scan starts to open all.
        - ``.MODE_OPEN_USED``: Sets the relay action when the scan starts to use an intelligent
          open.
        - ``.MODE_OUTSIDE``: Start the scan when the measurement is less than the lower limit or
          more than the upper limit.
        - ``.MODE_WINDOW``: Start the scan when the measurement is between the lower limit and the
          upper limit.
        - ``.OFF``: Do not restart scan.
        - ``.ON``: Restart scan.
        - ``.PAUSED``: The scan was paused.
        - ``.RUNNING``: The scan is running the trigger model portion of the scan.
        - ``.STEPPING``: The scan is running the channel action portion of the scan.
        - ``.SUCCESS``: The scan completed successfully.
        - ``.WRITE_AFTER_SCAN``: Write scan data to a file on a USB flash drive at completion of
          each scan.
        - ``.WRITE_AFTER_STEP``: Write scan data to a file on a USB flash drive at completion of
          each scan step.
        - ``.WRITE_AT_END``: Write scan data to a file on a USB flash drive at completion of all
          scans.
        - ``.WRITE_NEVER``: Do not write data to a file.

    Properties and methods:
        - ``.add()``: The ``scan.add()`` function.
        - ``.addsinglestep()``: The ``scan.addsinglestep()`` function.
        - ``.addwrite()``: The ``scan.addwrite()`` function.
        - ``.buffer``: The ``scan.buffer`` attribute.
        - ``.bypass``: The ``scan.bypass`` attribute.
        - ``.channel``: The ``scan.channel`` command tree.
        - ``.create()``: The ``scan.create()`` function.
        - ``.export()``: The ``scan.export()`` function.
        - ``.learnlimits()``: The ``scan.learnlimits()`` function.
        - ``.list()``: The ``scan.list()`` function.
        - ``.measure``: The ``scan.measure`` command tree.
        - ``.mode``: The ``scan.mode`` attribute.
        - ``.monitor``: The ``scan.monitor`` command tree.
        - ``.restart``: The ``scan.restart`` attribute.
        - ``.scancount``: The ``scan.scancount`` attribute.
        - ``.scaninterval``: The ``scan.scaninterval`` attribute.
        - ``.start``: The ``scan.start`` command tree.
        - ``.state()``: The ``scan.state()`` function.
        - ``.stepcount``: The ``scan.stepcount`` attribute.
    """

    ABORTED = "scan.ABORTED"
    """str: The scan was canceled."""
    BUILDING = "scan.BUILDING"
    """str: The instrument is building the scan."""
    COUNT_INFINITE = "scan.COUNT_INFINITE"
    """str: Set the number of times the scan is repeated to repeated until aborted."""
    EMPTY = "scan.EMPTY"
    """str: Scan is not set up."""
    FAILED = "scan.FAILED"
    """str: The scan failed."""
    MODE_FIXED_ABR = "scan.MODE_FIXED_ABR"
    """str: Sets the relay action when the scan starts to automatic backplane relay."""
    MODE_HIGH = "scan.MODE_HIGH"
    """str: Start the scan when the measurement exceeds the value set by scan.monitor.limit.high.value."""  # noqa: E501
    MODE_LOW = "scan.MODE_LOW"
    """str: Start the scan when the measurement is below the value set by scan.monitor.limit.low.value."""  # noqa: E501
    MODE_OFF = "scan.MODE_OFF"
    """str: Start the scan without waiting for a specific value."""
    MODE_OPEN_ALL = "scan.MODE_OPEN_ALL"
    """str: Sets the relay action when the scan starts to open all."""
    MODE_OPEN_USED = "scan.MODE_OPEN_USED"
    """str: Sets the relay action when the scan starts to use an intelligent open."""
    MODE_OUTSIDE = "scan.MODE_OUTSIDE"
    """str: Start the scan when the measurement is less than the lower limit or more than the upper limit."""  # noqa: E501
    MODE_WINDOW = "scan.MODE_WINDOW"
    """str: Start the scan when the measurement is between the lower limit and the upper limit."""
    OFF = "scan.OFF"
    """str: Do not restart scan."""
    ON = "scan.ON"
    """str: Restart scan."""
    PAUSED = "scan.PAUSED"
    """str: The scan was paused."""
    RUNNING = "scan.RUNNING"
    """str: The scan is running the trigger model portion of the scan."""
    STEPPING = "scan.STEPPING"
    """str: The scan is running the channel action portion of the scan."""
    SUCCESS = "scan.SUCCESS"
    """str: The scan completed successfully."""
    WRITE_AFTER_SCAN = "scan.WRITE_AFTER_SCAN"
    """str: Write scan data to a file on a USB flash drive at completion of each scan."""
    WRITE_AFTER_STEP = "scan.WRITE_AFTER_STEP"
    """str: Write scan data to a file on a USB flash drive at completion of each scan step."""
    WRITE_AT_END = "scan.WRITE_AT_END"
    """str: Write scan data to a file on a USB flash drive at completion of all scans."""
    WRITE_NEVER = "scan.WRITE_NEVER"
    """str: Do not write data to a file."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "scan") -> None:
        super().__init__(device, cmd_syntax)
        self._channel = ScanChannel(device, f"{self._cmd_syntax}.channel")
        self._measure = ScanMeasure(device, f"{self._cmd_syntax}.measure")
        self._monitor = ScanMonitor(device, f"{self._cmd_syntax}.monitor")
        self._start = ScanStart(device, f"{self._cmd_syntax}.start")

    @property
    def buffer(self) -> str:
        """Access the ``scan.buffer`` attribute.

        Description:
            - This attribute defines which buffer is used with the scan.

        Usage:
            - Accessing this property will send the ``print(scan.buffer)`` query.
            - Setting this property to a value will send the ``scan.buffer = value`` command.

        TSP Syntax:
            ```
            - scan.buffer = value
            - print(scan.buffer)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".buffer"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.buffer)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.buffer`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @buffer.setter
    def buffer(self, value: Union[str, float]) -> None:
        """Access the ``scan.buffer`` attribute.

        Description:
            - This attribute defines which buffer is used with the scan.

        Usage:
            - Accessing this property will send the ``print(scan.buffer)`` query.
            - Setting this property to a value will send the ``scan.buffer = value`` command.

        TSP Syntax:
            ```
            - scan.buffer = value
            - print(scan.buffer)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".buffer", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.buffer = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.buffer`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def bypass(self) -> str:
        """Access the ``scan.bypass`` attribute.

        Description:
            - This attribute indicates whether the first channel of the scan waits for the channel
              stimulus event to be satisfied before closing.

        Usage:
            - Accessing this property will send the ``print(scan.bypass)`` query.
            - Setting this property to a value will send the ``scan.bypass = value`` command.

        TSP Syntax:
            ```
            - scan.bypass = value
            - print(scan.bypass)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".bypass"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.bypass)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.bypass`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @bypass.setter
    def bypass(self, value: Union[str, float]) -> None:
        """Access the ``scan.bypass`` attribute.

        Description:
            - This attribute indicates whether the first channel of the scan waits for the channel
              stimulus event to be satisfied before closing.

        Usage:
            - Accessing this property will send the ``print(scan.bypass)`` query.
            - Setting this property to a value will send the ``scan.bypass = value`` command.

        TSP Syntax:
            ```
            - scan.bypass = value
            - print(scan.bypass)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".bypass", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.bypass = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.bypass`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def channel(self) -> ScanChannel:
        """Return the ``scan.channel`` command tree.

        Sub-properties and sub-methods:
            - ``.stimulus``: The ``scan.channel.stimulus`` attribute.
        """
        return self._channel

    @property
    def measure(self) -> ScanMeasure:
        """Return the ``scan.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.interval``: The ``scan.measure.interval`` attribute.
            - ``.stimulus``: The ``scan.measure.stimulus`` attribute.
        """
        return self._measure

    @property
    def mode(self) -> str:
        """Access the ``scan.mode`` attribute.

        Description:
            - This attribute sets the relay action when the scan starts.

        Usage:
            - Accessing this property will send the ``print(scan.mode)`` query.
            - Setting this property to a value will send the ``scan.mode = value`` command.

        TSP Syntax:
            ```
            - scan.mode = value
            - print(scan.mode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".mode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.mode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @mode.setter
    def mode(self, value: Union[str, float]) -> None:
        """Access the ``scan.mode`` attribute.

        Description:
            - This attribute sets the relay action when the scan starts.

        Usage:
            - Accessing this property will send the ``print(scan.mode)`` query.
            - Setting this property to a value will send the ``scan.mode = value`` command.

        TSP Syntax:
            ```
            - scan.mode = value
            - print(scan.mode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".mode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.mode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def monitor(self) -> ScanMonitor:
        """Return the ``scan.monitor`` command tree.

        Sub-properties and sub-methods:
            - ``.channel``: The ``scan.monitor.channel`` attribute.
            - ``.limit``: The ``scan.monitor.limit`` command tree.
            - ``.mode``: The ``scan.monitor.mode`` attribute.
        """
        return self._monitor

    @property
    def restart(self) -> str:
        """Access the ``scan.restart`` attribute.

        Description:
            - This function causes a scan to automatically restart if it was interrupted by a power
              failure.

        Usage:
            - Accessing this property will send the ``print(scan.restart)`` query.
            - Setting this property to a value will send the ``scan.restart = value`` command.

        TSP Syntax:
            ```
            - scan.restart = value
            - print(scan.restart)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".restart"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.restart)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.restart`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @restart.setter
    def restart(self, value: Union[str, float]) -> None:
        """Access the ``scan.restart`` attribute.

        Description:
            - This function causes a scan to automatically restart if it was interrupted by a power
              failure.

        Usage:
            - Accessing this property will send the ``print(scan.restart)`` query.
            - Setting this property to a value will send the ``scan.restart = value`` command.

        TSP Syntax:
            ```
            - scan.restart = value
            - print(scan.restart)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".restart", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.restart = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.restart`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def scancount(self) -> str:
        """Access the ``scan.scancount`` attribute.

        Description:
            - This attribute sets the number of times the scan is repeated.

        Usage:
            - Accessing this property will send the ``print(scan.scancount)`` query.
            - Setting this property to a value will send the ``scan.scancount = value`` command.

        TSP Syntax:
            ```
            - scan.scancount = value
            - print(scan.scancount)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".scancount"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.scancount)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.scancount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @scancount.setter
    def scancount(self, value: Union[str, float]) -> None:
        """Access the ``scan.scancount`` attribute.

        Description:
            - This attribute sets the number of times the scan is repeated.

        Usage:
            - Accessing this property will send the ``print(scan.scancount)`` query.
            - Setting this property to a value will send the ``scan.scancount = value`` command.

        TSP Syntax:
            ```
            - scan.scancount = value
            - print(scan.scancount)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".scancount", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.scancount = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.scancount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def scaninterval(self) -> str:
        """Access the ``scan.scaninterval`` attribute.

        Description:
            - This attribute specifies the interval time between scan starts when the scan count is
              more than one.

        Usage:
            - Accessing this property will send the ``print(scan.scaninterval)`` query.
            - Setting this property to a value will send the ``scan.scaninterval = value`` command.

        TSP Syntax:
            ```
            - scan.scaninterval = value
            - print(scan.scaninterval)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".scaninterval"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.scaninterval)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.scaninterval`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @scaninterval.setter
    def scaninterval(self, value: Union[str, float]) -> None:
        """Access the ``scan.scaninterval`` attribute.

        Description:
            - This attribute specifies the interval time between scan starts when the scan count is
              more than one.

        Usage:
            - Accessing this property will send the ``print(scan.scaninterval)`` query.
            - Setting this property to a value will send the ``scan.scaninterval = value`` command.

        TSP Syntax:
            ```
            - scan.scaninterval = value
            - print(scan.scaninterval)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".scaninterval", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.scaninterval = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.scaninterval`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def start(self) -> ScanStart:
        """Return the ``scan.start`` command tree.

        Sub-properties and sub-methods:
            - ``.stimulus``: The ``scan.start.stimulus`` attribute.
        """
        return self._start

    @property
    def stepcount(self) -> str:
        """Access the ``scan.stepcount`` attribute.

        Description:
            - This attribute returns the number of steps in the present scan.

        Usage:
            - Accessing this property will send the ``print(scan.stepcount)`` query.

        TSP Syntax:
            ```
            - print(scan.stepcount)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stepcount"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stepcount)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stepcount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def add(
        self, channel_list: str, config_list: Optional[str] = None, index: Optional[int] = None
    ) -> None:
        """Run the ``scan.add()`` function.

        Description:
            - This function adds channels to the scan list.

        TSP Syntax:
            ```
            - scan.add()
            ```

        Args:
            channel_list: List of channels to add, in the order in which they should occur in the
                scan.
            config_list (optional): A string that defines the configuration list to recall.
            index (optional): The index in the configuration list to recall; default is 1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{channel_list}"',
                    f'"{config_list}"' if config_list is not None else None,
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.add({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.add()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def addsinglestep(
        self, channel_list: str, config_list: Optional[str] = None, index: Optional[int] = None
    ) -> None:
        """Run the ``scan.addsinglestep()`` function.

        Description:
            - This function allows you to include multiple channels in a single scan step.

        TSP Syntax:
            ```
            - scan.addsinglestep()
            ```

        Args:
            channel_list: List of channels to add, in the order in which they should occur in the
                scan.
            config_list (optional): A string that defines the configuration list to recall.
            index (optional): The index in the configuration list to recall; default is 1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{channel_list}"',
                    config_list,
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.addsinglestep({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.addsinglestep()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def addwrite(self, channel_list: str, write_value: str) -> None:
        """Run the ``scan.addwrite()`` function.

        Description:
            - This function writes a specified value to a channel at the added step in the scan.

        TSP Syntax:
            ```
            - scan.addwrite()
            ```

        Args:
            channel_list: String specifying channels to add using normal channel list syntax.
            write_value: The value to write to the channel for this scan step.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.addwrite("{channel_list}", {write_value})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.addwrite()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def create(
        self,
        channel_list: Optional[str] = None,
        config_list: Optional[str] = None,
        index: Optional[int] = None,
    ) -> None:
        """Run the ``scan.create()`` function.

        Description:
            - This function deletes the existing scan list and creates a new list of channels to
              scan.

        TSP Syntax:
            ```
            - scan.create()
            ```

        Args:
            channel_list (optional): String specifying channels to add to the new scan list.
            config_list (optional): A string that defines the configuration list to recall.
            index (optional): The index in the configuration list to recall; default is 1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{channel_list}"' if channel_list is not None else None,
                    config_list,
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.create({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.create()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def export(self, filename: str, when: str, what: Optional[str] = None) -> None:
        """Run the ``scan.export()`` function.

        Description:
            - This command stores data from a scan to a file on a USB flash drive.

        TSP Syntax:
            ```
            - scan.export()
            ```

        Args:
            filename: The name of the file to be created on the USB flash drive.
            when: When to write the data to the file.
            what (optional): Which data to include; see Details for options.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    filename,
                    when,
                    what,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.export({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.export()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def learnlimits(self, window: str, iterations: Optional[str] = None) -> None:
        """Run the ``scan.learnlimits()`` function.

        Description:
            - This function calculates alarm limits based on the present configuration of the
              system.

        TSP Syntax:
            ```
            - scan.learnlimits()
            ```

        Args:
            window: Percentage of deviation from the measurement that is within limits.
            iterations (optional): Number of times to run the scan to set limits.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    window,
                    iterations,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.learnlimits({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.learnlimits()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def list(self) -> str:
        """Run the ``scan.list()`` function.

        Description:
            - This function returns a list that includes the initial open or close state of any
              cards installed in the instrument and the settings at each step of the scan.

        TSP Syntax:
            ```
            - scan.list()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.list())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.list()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def state(self) -> str:
        """Run the ``scan.state()`` function.

        Description:
            - This function provides the present state of a running background scan.

        TSP Syntax:
            ```
            - scan.state()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.state())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.state()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
