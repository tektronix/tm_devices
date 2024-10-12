# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The acal commands module.

These commands are used in the following models:
DMM7510

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - acal.count
    - acal.lastrun.internaltemp
    - acal.lastrun.tempdiff
    - acal.lastrun.time
    - acal.nextrun.time
    - acal.revert()
    - acal.run()
    - acal.schedule()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class AcalNextrun(BaseTSPCmd):
    """The ``acal.nextrun`` command tree.

    Properties and methods:
        - ``.time``: The ``acal.nextrun.time`` attribute.
    """

    @property
    def time(self) -> str:
        """Access the ``acal.nextrun.time`` attribute.

        Description:
            - This attribute returns the date and time when the next autocalibration is scheduled to
              be run.

        Usage:
            - Accessing this property will send the ``print(acal.nextrun.time)`` query.

        TSP Syntax:
            ```
            - print(acal.nextrun.time)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".time"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.time)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.time`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class AcalLastrun(BaseTSPCmd):
    """The ``acal.lastrun`` command tree.

    Properties and methods:
        - ``.internaltemp``: The ``acal.lastrun.internaltemp`` attribute.
        - ``.tempdiff``: The ``acal.lastrun.tempdiff`` attribute.
        - ``.time``: The ``acal.lastrun.time`` attribute.
    """

    @property
    def internaltemp(self) -> str:
        """Access the ``acal.lastrun.internaltemp`` attribute.

        Description:
            - This attribute returns the internal temperature of the instrument when autocalibration
              was run.

        Usage:
            - Accessing this property will send the ``print(acal.lastrun.internaltemp)`` query.

        TSP Syntax:
            ```
            - print(acal.lastrun.internaltemp)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".internaltemp"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.internaltemp)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.internaltemp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def tempdiff(self) -> str:
        """Access the ``acal.lastrun.tempdiff`` attribute.

        Description:
            - This attribute returns the difference between the internal temperature and the
              temperature when autocalibration was last run.

        Usage:
            - Accessing this property will send the ``print(acal.lastrun.tempdiff)`` query.

        TSP Syntax:
            ```
            - print(acal.lastrun.tempdiff)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".tempdiff"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.tempdiff)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tempdiff`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def time(self) -> str:
        """Access the ``acal.lastrun.time`` attribute.

        Description:
            - This attribute returns the date and time when autocalibration was last run.

        Usage:
            - Accessing this property will send the ``print(acal.lastrun.time)`` query.

        TSP Syntax:
            ```
            - print(acal.lastrun.time)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".time"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.time)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.time`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Acal(BaseTSPCmd):
    """The ``acal`` command tree.

    Properties and methods:
        - ``.count``: The ``acal.count`` attribute.
        - ``.lastrun``: The ``acal.lastrun`` command tree.
        - ``.nextrun``: The ``acal.nextrun`` command tree.
        - ``.revert()``: The ``acal.revert()`` function.
        - ``.run()``: The ``acal.run()`` function.
        - ``.schedule()``: The ``acal.schedule()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "acal") -> None:
        super().__init__(device, cmd_syntax)
        self._lastrun = AcalLastrun(device, f"{self._cmd_syntax}.lastrun")
        self._nextrun = AcalNextrun(device, f"{self._cmd_syntax}.nextrun")

    @property
    def count(self) -> str:
        """Access the ``acal.count`` attribute.

        Description:
            - This attribute returns the number of times autocalibration has been run.

        Usage:
            - Accessing this property will send the ``print(acal.count)`` query.

        TSP Syntax:
            ```
            - print(acal.count)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".count"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.count)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def lastrun(self) -> AcalLastrun:
        """Return the ``acal.lastrun`` command tree.

        Sub-properties and sub-methods:
            - ``.internaltemp``: The ``acal.lastrun.internaltemp`` attribute.
            - ``.tempdiff``: The ``acal.lastrun.tempdiff`` attribute.
            - ``.time``: The ``acal.lastrun.time`` attribute.
        """
        return self._lastrun

    @property
    def nextrun(self) -> AcalNextrun:
        """Return the ``acal.nextrun`` command tree.

        Sub-properties and sub-methods:
            - ``.time``: The ``acal.nextrun.time`` attribute.
        """
        return self._nextrun

    def revert(self) -> str:
        """Run the ``acal.revert()`` function.

        Description:
            - This function returns autocalibration constants to the previous constants.

        TSP Syntax:
            ```
            - acal.revert()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.revert())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.revert()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def run(self) -> None:
        """Run the ``acal.run()`` function.

        Description:
            - This function immediately runs autocalibration and stores the constants.

        TSP Syntax:
            ```
            - acal.run()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.run()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.run()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def schedule(
        self,
        action: Optional[str] = None,
        interval: Optional[str] = None,
        hour: Optional[int] = None,
    ) -> str:
        """Run the ``acal.schedule()`` function.

        Description:
            - This function sets how often autocalibration occurs or prompts you to run it.

        TSP Syntax:
            ```
            - acal.schedule()
            ```

        Args:
            action (optional): Determines when and if the instrument automatically runs
                autocalibration.
            interval (optional): Determines how often autocalibration should be run or notification
                should occur.
            hour (optional): Specify when the autocalibration should occur; specify in 24-hour time
                format (0 to 23; default is 0); not available for the 8-hour or 16-hour interval.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    action,
                    interval,
                    hour,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.schedule({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.schedule()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
