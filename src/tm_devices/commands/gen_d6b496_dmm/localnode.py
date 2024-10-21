# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The localnode commands module.

These commands are used in the following models:
DMM7510

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - localnode.access
    - localnode.gettime()
    - localnode.internaltemp
    - localnode.linefreq
    - localnode.model
    - localnode.password
    - localnode.prompts
    - localnode.prompts4882
    - localnode.serialno
    - localnode.settime()
    - localnode.showevents
    - localnode.version
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Localnode(BaseTSPCmd):
    """The ``localnode`` command tree.

    Constants:
        - ``.ACCESS_EXCLUSIVE``: Allows access by one remote interface at a time with logins
          required from other interfaces.
        - ``.ACCESS_FULL``: Full access for all users from all interfaces.
        - ``.ACCESS_LOCKOUT``: Allows access by one interface (including the front panel) at a time
          with passwords required on all interfaces.
        - ``.ACCESS_PROTECTED``: Allows access by one remote interface at a time with passwords
          required on all interfaces.
        - ``.DISABLE``: Do not generate prompts in response to command messages.
        - ``.ENABLE``: Generate prompts in response to command messages.

    Properties and methods:
        - ``.access``: The ``localnode.access`` attribute.
        - ``.gettime()``: The ``localnode.gettime()`` function.
        - ``.internaltemp``: The ``localnode.internaltemp`` attribute.
        - ``.linefreq``: The ``localnode.linefreq`` attribute.
        - ``.model``: The ``localnode.model`` attribute.
        - ``.password``: The ``localnode.password`` attribute.
        - ``.prompts``: The ``localnode.prompts`` attribute.
        - ``.prompts4882``: The ``localnode.prompts4882`` attribute.
        - ``.serialno``: The ``localnode.serialno`` attribute.
        - ``.settime()``: The ``localnode.settime()`` function.
        - ``.showevents``: The ``localnode.showevents`` attribute.
        - ``.version``: The ``localnode.version`` attribute.
    """

    ACCESS_EXCLUSIVE = "localnode.ACCESS_EXCLUSIVE"
    """str: Allows access by one remote interface at a time with logins required from other interfaces."""  # noqa: E501
    ACCESS_FULL = "localnode.ACCESS_FULL"
    """str: Full access for all users from all interfaces."""
    ACCESS_LOCKOUT = "localnode.ACCESS_LOCKOUT"
    """str: Allows access by one interface (including the front panel) at a time with passwords required on all interfaces."""  # noqa: E501
    ACCESS_PROTECTED = "localnode.ACCESS_PROTECTED"
    """str: Allows access by one remote interface at a time with passwords required on all interfaces."""  # noqa: E501
    DISABLE = "localnode.DISABLE"
    """str: Do not generate prompts in response to command messages."""
    ENABLE = "localnode.ENABLE"
    """str: Generate prompts in response to command messages."""

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "localnode"
    ) -> None:
        super().__init__(device, cmd_syntax)

    @property
    def access(self) -> str:
        """Access the ``localnode.access`` attribute.

        Description:
            - This attribute contains the type of access users have to the instrument through
              different interfaces.

        Usage:
            - Accessing this property will send the ``print(localnode.access)`` query.
            - Setting this property to a value will send the ``localnode.access = value`` command.

        TSP Syntax:
            ```
            - localnode.access = value
            - print(localnode.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".access"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.access)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @access.setter
    def access(self, value: Union[str, float]) -> None:
        """Access the ``localnode.access`` attribute.

        Description:
            - This attribute contains the type of access users have to the instrument through
              different interfaces.

        Usage:
            - Accessing this property will send the ``print(localnode.access)`` query.
            - Setting this property to a value will send the ``localnode.access = value`` command.

        TSP Syntax:
            ```
            - localnode.access = value
            - print(localnode.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".access", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.access = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def internaltemp(self) -> str:
        """Access the ``localnode.internaltemp`` attribute.

        Description:
            - This attribute returns the internal temperature of the instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.internaltemp)`` query.

        TSP Syntax:
            ```
            - print(localnode.internaltemp)
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
    def linefreq(self) -> str:
        """Access the ``localnode.linefreq`` attribute.

        Description:
            - This attribute contains the power line frequency setting that is used for NPLC
              calculations.

        Usage:
            - Accessing this property will send the ``print(localnode.linefreq)`` query.

        TSP Syntax:
            ```
            - print(localnode.linefreq)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".linefreq"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.linefreq)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.linefreq`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def model(self) -> str:
        """Access the ``localnode.model`` attribute.

        Description:
            - This attribute stores the model number.

        Usage:
            - Accessing this property will send the ``print(localnode.model)`` query.

        TSP Syntax:
            ```
            - print(localnode.model)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".model"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.model)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.model`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def password(self) -> str:
        """Access the ``localnode.password`` attribute.

        Description:
            - This attribute stores the instrument password.

        Usage:
            - Setting this property to a value will send the ``localnode.password = value`` command.

        TSP Syntax:
            ```
            - localnode.password = value
            ```

        Raises:
            AttributeError: Indicates that this attribute is write-only.
        """
        if self._device.command_syntax_enabled:  # type: ignore[union-attr]
            return self._cmd_syntax + ".password"
        msg = f"``{self._cmd_syntax}.password`` is a write-only attribute."
        raise AttributeError(msg)

    @password.setter
    def password(self, value: Union[str, float]) -> None:
        """Access the ``localnode.password`` attribute.

        Description:
            - This attribute stores the instrument password.

        Usage:
            - Setting this property to a value will send the ``localnode.password = value`` command.

        TSP Syntax:
            ```
            - localnode.password = value
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.password = {value}"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.password`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def prompts(self) -> str:
        """Access the ``localnode.prompts`` attribute.

        Description:
            - This attribute determines if the instrument generates prompts in response to command
              messages.

        Usage:
            - Accessing this property will send the ``print(localnode.prompts)`` query.
            - Setting this property to a value will send the ``localnode.prompts = value`` command.

        TSP Syntax:
            ```
            - localnode.prompts = value
            - print(localnode.prompts)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".prompts"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.prompts)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.prompts`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @prompts.setter
    def prompts(self, value: Union[str, float]) -> None:
        """Access the ``localnode.prompts`` attribute.

        Description:
            - This attribute determines if the instrument generates prompts in response to command
              messages.

        Usage:
            - Accessing this property will send the ``print(localnode.prompts)`` query.
            - Setting this property to a value will send the ``localnode.prompts = value`` command.

        TSP Syntax:
            ```
            - localnode.prompts = value
            - print(localnode.prompts)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".prompts", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.prompts = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.prompts`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def prompts4882(self) -> str:
        """Access the ``localnode.prompts4882`` attribute.

        Description:
            - This attribute enables and disables the generation of prompts for IEEE Std 488.2
              common commands.

        Usage:
            - Accessing this property will send the ``print(localnode.prompts4882)`` query.
            - Setting this property to a value will send the ``localnode.prompts4882 = value``
              command.

        TSP Syntax:
            ```
            - localnode.prompts4882 = value
            - print(localnode.prompts4882)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".prompts4882"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.prompts4882)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.prompts4882`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @prompts4882.setter
    def prompts4882(self, value: Union[str, float]) -> None:
        """Access the ``localnode.prompts4882`` attribute.

        Description:
            - This attribute enables and disables the generation of prompts for IEEE Std 488.2
              common commands.

        Usage:
            - Accessing this property will send the ``print(localnode.prompts4882)`` query.
            - Setting this property to a value will send the ``localnode.prompts4882 = value``
              command.

        TSP Syntax:
            ```
            - localnode.prompts4882 = value
            - print(localnode.prompts4882)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".prompts4882", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.prompts4882 = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.prompts4882`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def serialno(self) -> str:
        """Access the ``localnode.serialno`` attribute.

        Description:
            - This attribute stores the serial number of the instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.serialno)`` query.

        TSP Syntax:
            ```
            - print(localnode.serialno)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".serialno"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.serialno)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.serialno`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def showevents(self) -> str:
        """Access the ``localnode.showevents`` attribute.

        Description:
            - This attribute sets whether or not the instrument automatically outputs generated
              events to the remote interface.

        Usage:
            - Accessing this property will send the ``print(localnode.showevents)`` query.
            - Setting this property to a value will send the ``localnode.showevents = value``
              command.

        TSP Syntax:
            ```
            - localnode.showevents = value
            - print(localnode.showevents)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".showevents"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.showevents)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.showevents`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @showevents.setter
    def showevents(self, value: Union[str, float]) -> None:
        """Access the ``localnode.showevents`` attribute.

        Description:
            - This attribute sets whether or not the instrument automatically outputs generated
              events to the remote interface.

        Usage:
            - Accessing this property will send the ``print(localnode.showevents)`` query.
            - Setting this property to a value will send the ``localnode.showevents = value``
              command.

        TSP Syntax:
            ```
            - localnode.showevents = value
            - print(localnode.showevents)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".showevents", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.showevents = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.showevents`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def version(self) -> str:
        """Access the ``localnode.version`` attribute.

        Description:
            - This attribute stores the firmware version of the instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.version)`` query.

        TSP Syntax:
            ```
            - print(localnode.version)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".version"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.version)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.version`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def gettime(self) -> None:
        """Run the ``localnode.gettime()`` function.

        Description:
            - This function retrieves the instrument date and time.

        TSP Syntax:
            ```
            - localnode.gettime()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.gettime()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.gettime()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def settime(
        self,
        year: Optional[str] = None,
        month: Optional[int] = None,
        day: Optional[int] = None,
        hour: Optional[int] = None,
        minute: Optional[int] = None,
        second: Optional[int] = None,
    ) -> None:
        """Run the ``localnode.settime()`` function.

        Description:
            - This function sets the date and time of the instrument.

        TSP Syntax:
            ```
            - localnode.settime()
            ```

        Args:
            year (optional): Year; must be more than 1970.
            month (optional): Month (1 to 12).
            day (optional): Day (1 to 31).
            hour (optional): Hour in 24-hour time format (0 to 23).
            minute (optional): Minute (0 to 59).
            second (optional): Second (0 to 59).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    year,
                    month,
                    day,
                    hour,
                    minute,
                    second,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.settime({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.settime()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
