# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The ptp commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - ptp.domain
    - ptp.ds.info
    - ptp.enable
    - ptp.portstate
    - ptp.slavepreferred
    - ptp.time()
    - ptp.utcoffset
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class PtpDs(BaseTSPCmd):
    """The ``ptp.ds`` command tree.

    Properties and methods:
        - ``.info``: The ``ptp.ds.info`` function.
    """

    def info(self) -> str:
        """Run the ``ptp.ds.info`` function.

        Description:
            - This function is a read-only string that returns the settings of the different data
              sets (DS) associated with the IEEE-1588 2008 specification.

        TSP Syntax:
            ```
            - ptp.ds.info
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.info())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.info()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Ptp(BaseTSPCmd):
    """The ``ptp`` command tree.

    Properties and methods:
        - ``.domain``: The ``ptp.domain`` attribute.
        - ``.ds``: The ``ptp.ds`` command tree.
        - ``.enable``: The ``ptp.enable`` attribute.
        - ``.portstate``: The ``ptp.portstate`` attribute.
        - ``.slavepreferred``: The ``ptp.slavepreferred`` attribute.
        - ``.time()``: The ``ptp.time()`` function.
        - ``.utcoffset``: The ``ptp.utcoffset`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "ptp") -> None:
        super().__init__(device, cmd_syntax)
        self._ds = PtpDs(device, f"{self._cmd_syntax}.ds")

    @property
    def domain(self) -> str:
        """Access the ``ptp.domain`` attribute.

        Description:
            - This attribute describes the IEEE Std 1588-2008 precision time protocol (PTP) domain.

        Usage:
            - Accessing this property will send the ``print(ptp.domain)`` query.
            - Setting this property to a value will send the ``ptp.domain = value`` command.

        TSP Syntax:
            ```
            - ptp.domain = value
            - print(ptp.domain)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".domain"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.domain)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.domain`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @domain.setter
    def domain(self, value: Union[str, float]) -> None:
        """Access the ``ptp.domain`` attribute.

        Description:
            - This attribute describes the IEEE Std 1588-2008 precision time protocol (PTP) domain.

        Usage:
            - Accessing this property will send the ``print(ptp.domain)`` query.
            - Setting this property to a value will send the ``ptp.domain = value`` command.

        TSP Syntax:
            ```
            - ptp.domain = value
            - print(ptp.domain)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".domain", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.domain = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.domain`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ds(self) -> PtpDs:
        """Return the ``ptp.ds`` command tree.

        Sub-properties and sub-methods:
            - ``.info``: The ``ptp.ds.info`` function.
        """
        return self._ds

    @property
    def enable(self) -> str:
        """Access the ``ptp.enable`` attribute.

        Description:
            - This attribute enables or disables the precision time protocol (PTP) described in
              IEEE-1588 on the Series 3700A.

        Usage:
            - Accessing this property will send the ``print(ptp.enable)`` query.
            - Setting this property to a value will send the ``ptp.enable = value`` command.

        TSP Syntax:
            ```
            - ptp.enable = value
            - print(ptp.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``ptp.enable`` attribute.

        Description:
            - This attribute enables or disables the precision time protocol (PTP) described in
              IEEE-1588 on the Series 3700A.

        Usage:
            - Accessing this property will send the ``print(ptp.enable)`` query.
            - Setting this property to a value will send the ``ptp.enable = value`` command.

        TSP Syntax:
            ```
            - ptp.enable = value
            - print(ptp.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def portstate(self) -> str:
        """Access the ``ptp.portstate`` attribute.

        Description:
            - This attribute is a read-only value that indicates the state of the IEEE-1588
              precision time protocol (PTP).

        Usage:
            - Accessing this property will send the ``print(ptp.portstate)`` query.

        TSP Syntax:
            ```
            - print(ptp.portstate)
            ```

        Info:
            - ``state``, the ptp.INITIALIZING (0)
              ptp.FAULTY (1)
              ptp.DISABLE (2)
              ptp.LISTENING (3)
              ptp.PRE_MASTER (4)
              ptp.MASTER (5)
              ptp.PASSIVE (6)
              ptp.UNCALIBRATED (7)
              ptp.SLAVE (8)
              ptp.UNKNOWN (9).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".portstate"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.portstate)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.portstate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def slavepreferred(self) -> str:
        """Access the ``ptp.slavepreferred`` attribute.

        Description:
            - This attribute describes whether you prefer to have the instrument be a subordinate
              clock or not.

        Usage:
            - Accessing this property will send the ``print(ptp.slavepreferred)`` query.
            - Setting this property to a value will send the ``ptp.slavepreferred = value`` command.

        TSP Syntax:
            ```
            - ptp.slavepreferred = value
            - print(ptp.slavepreferred)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".slavepreferred"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.slavepreferred)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slavepreferred`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @slavepreferred.setter
    def slavepreferred(self, value: Union[str, float]) -> None:
        """Access the ``ptp.slavepreferred`` attribute.

        Description:
            - This attribute describes whether you prefer to have the instrument be a subordinate
              clock or not.

        Usage:
            - Accessing this property will send the ``print(ptp.slavepreferred)`` query.
            - Setting this property to a value will send the ``ptp.slavepreferred = value`` command.

        TSP Syntax:
            ```
            - ptp.slavepreferred = value
            - print(ptp.slavepreferred)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".slavepreferred", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.slavepreferred = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slavepreferred`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def utcoffset(self) -> str:
        """Access the ``ptp.utcoffset`` attribute.

        Description:
            - This attribute describes the offset, in seconds, between UTC and PTP.

        Usage:
            - Accessing this property will send the ``print(ptp.utcoffset)`` query.
            - Setting this property to a value will send the ``ptp.utcoffset = value`` command.

        TSP Syntax:
            ```
            - ptp.utcoffset = value
            - print(ptp.utcoffset)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".utcoffset"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.utcoffset)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.utcoffset`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @utcoffset.setter
    def utcoffset(self, value: Union[str, float]) -> None:
        """Access the ``ptp.utcoffset`` attribute.

        Description:
            - This attribute describes the offset, in seconds, between UTC and PTP.

        Usage:
            - Accessing this property will send the ``print(ptp.utcoffset)`` query.
            - Setting this property to a value will send the ``ptp.utcoffset = value`` command.

        TSP Syntax:
            ```
            - ptp.utcoffset = value
            - print(ptp.utcoffset)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".utcoffset", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.utcoffset = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.utcoffset`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def time(self) -> str:
        """Run the ``ptp.time()`` function.

        Description:
            - This function is a read-only string that returns the PTP time in seconds and
              fractional seconds.

        TSP Syntax:
            ```
            - ptp.time()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.time())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.time()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
