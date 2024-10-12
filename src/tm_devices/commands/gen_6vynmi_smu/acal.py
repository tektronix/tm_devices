# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The acal commands module.

These commands are used in the following models:
SMU2461

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - acal.count
    - acal.lastrun.internaltemp
    - acal.lastrun.tempdiff
    - acal.lastrun.time
    - acal.run()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


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
        - ``.run()``: The ``acal.run()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "acal") -> None:
        super().__init__(device, cmd_syntax)
        self._lastrun = AcalLastrun(device, f"{self._cmd_syntax}.lastrun")

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
