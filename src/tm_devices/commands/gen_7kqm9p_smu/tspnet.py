# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The tspnet commands module.

These commands are used in the following models:
SMU2450, SMU2460, SMU2461, SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - tspnet.clear()
    - tspnet.connect()
    - tspnet.disconnect()
    - tspnet.execute()
    - tspnet.idn()
    - tspnet.read()
    - tspnet.readavailable()
    - tspnet.reset()
    - tspnet.termination()
    - tspnet.timeout
    - tspnet.tsp.abort()
    - tspnet.tsp.abortonconnect
    - tspnet.tsp.rbtablecopy()
    - tspnet.tsp.runscript()
    - tspnet.write()
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class TspnetTsp(BaseTSPCmd):
    """The ``tspnet.tsp`` command tree.

    Properties and methods:
        - ``.abort()``: The ``tspnet.tsp.abort()`` function.
        - ``.abortonconnect``: The ``tspnet.tsp.abortonconnect`` attribute.
        - ``.rbtablecopy()``: The ``tspnet.tsp.rbtablecopy()`` function.
        - ``.runscript()``: The ``tspnet.tsp.runscript()`` function.
    """

    @property
    def abortonconnect(self) -> str:
        """Access the ``tspnet.tsp.abortonconnect`` attribute.

        Description:
            - This attribute contains the setting for abort on connect to a TSP-enabled instrument.

        Usage:
            - Accessing this property will send the ``print(tspnet.tsp.abortonconnect)`` query.
            - Setting this property to a value will send the ``tspnet.tsp.abortonconnect = value``
              command.

        TSP Syntax:
            ```
            - tspnet.tsp.abortonconnect = value
            - print(tspnet.tsp.abortonconnect)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".abortonconnect"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.abortonconnect)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.abortonconnect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @abortonconnect.setter
    def abortonconnect(self, value: Union[str, float]) -> None:
        """Access the ``tspnet.tsp.abortonconnect`` attribute.

        Description:
            - This attribute contains the setting for abort on connect to a TSP-enabled instrument.

        Usage:
            - Accessing this property will send the ``print(tspnet.tsp.abortonconnect)`` query.
            - Setting this property to a value will send the ``tspnet.tsp.abortonconnect = value``
              command.

        TSP Syntax:
            ```
            - tspnet.tsp.abortonconnect = value
            - print(tspnet.tsp.abortonconnect)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".abortonconnect", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.abortonconnect = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.abortonconnect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def abort(self, connection_id: str) -> None:
        """Run the ``tspnet.tsp.abort()`` function.

        Description:
            - This function causes the TSP-enabled instrument to stop executing any of the commands
              that were sent to it.

        TSP Syntax:
            ```
            - tspnet.tsp.abort()
            ```

        Args:
            connection_id: Integer value used as a handle for other tspnet commands.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.abort({connection_id})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.abort()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def rbtablecopy(
        self,
        connection_id: str,
        name: str,
        start_index: Optional[int] = None,
        end_index: Optional[int] = None,
    ) -> str:
        """Run the ``tspnet.tsp.rbtablecopy()`` function.

        Description:
            - This function copies a reading buffer synchronous table from a remote instrument to a
              TSP-enabled instrument.

        TSP Syntax:
            ```
            - tspnet.tsp.rbtablecopy()
            ```

        Args:
            connection_id: Integer value used as a handle for other tspnet commands.
            name: The full name of the reading buffer name and synchronous table to copy.
            start_index (optional): Integer start value.
            end_index (optional): Integer end value.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    connection_id,
                    f'"{name}"',
                    start_index,
                    end_index,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rbtablecopy({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.rbtablecopy()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def runscript(self, connection_id: str, name: str, script: str) -> None:
        """Run the ``tspnet.tsp.runscript()`` function.

        Description:
            - This function loads and runs a script on a remote TSP-enabled instrument.

        TSP Syntax:
            ```
            - tspnet.tsp.runscript()
            ```

        Args:
            connection_id: Integer value used as an identifier for other tspnet commands.
            name: The name that is assigned to the script.
            script: The body of the script as a string.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.runscript({connection_id}, "{name}", "{script}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.runscript()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Tspnet(BaseTSPCmd):
    """The ``tspnet`` command tree.

    Constants:
        - ``.TERM_CR``: Set the device line termination sequence to CR.
        - ``.TERM_CRLF``: Set the device line termination sequence to CRLF.
        - ``.TERM_LF``: Set the device line termination sequence to LF.
        - ``.TERM_LFCR``: Set the device line termination sequence to LFCR.

    Properties and methods:
        - ``.clear()``: The ``tspnet.clear()`` function.
        - ``.connect()``: The ``tspnet.connect()`` function.
        - ``.disconnect()``: The ``tspnet.disconnect()`` function.
        - ``.execute()``: The ``tspnet.execute()`` function.
        - ``.idn()``: The ``tspnet.idn()`` function.
        - ``.read()``: The ``tspnet.read()`` function.
        - ``.readavailable()``: The ``tspnet.readavailable()`` function.
        - ``.reset()``: The ``tspnet.reset()`` function.
        - ``.termination()``: The ``tspnet.termination()`` function.
        - ``.timeout``: The ``tspnet.timeout`` attribute.
        - ``.tsp``: The ``tspnet.tsp`` command tree.
        - ``.write()``: The ``tspnet.write()`` function.
    """

    TERM_CR = "tspnet.TERM_CR"
    """str: Set the device line termination sequence to CR."""
    TERM_CRLF = "tspnet.TERM_CRLF"
    """str: Set the device line termination sequence to CRLF."""
    TERM_LF = "tspnet.TERM_LF"
    """str: Set the device line termination sequence to LF."""
    TERM_LFCR = "tspnet.TERM_LFCR"
    """str: Set the device line termination sequence to LFCR."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "tspnet") -> None:
        super().__init__(device, cmd_syntax)
        self._tsp = TspnetTsp(device, f"{self._cmd_syntax}.tsp")

    @property
    def timeout(self) -> str:
        """Access the ``tspnet.timeout`` attribute.

        Description:
            - This attribute sets the timeout value for the tspnet.connect(), tspnet.execute(), and
              tspnet.read() commands.

        Usage:
            - Accessing this property will send the ``print(tspnet.timeout)`` query.
            - Setting this property to a value will send the ``tspnet.timeout = value`` command.

        TSP Syntax:
            ```
            - tspnet.timeout = value
            - print(tspnet.timeout)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".timeout"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.timeout)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.timeout`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @timeout.setter
    def timeout(self, value: Union[str, float]) -> None:
        """Access the ``tspnet.timeout`` attribute.

        Description:
            - This attribute sets the timeout value for the tspnet.connect(), tspnet.execute(), and
              tspnet.read() commands.

        Usage:
            - Accessing this property will send the ``print(tspnet.timeout)`` query.
            - Setting this property to a value will send the ``tspnet.timeout = value`` command.

        TSP Syntax:
            ```
            - tspnet.timeout = value
            - print(tspnet.timeout)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".timeout", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.timeout = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.timeout`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def tsp(self) -> TspnetTsp:
        """Return the ``tspnet.tsp`` command tree.

        Sub-properties and sub-methods:
            - ``.abort()``: The ``tspnet.tsp.abort()`` function.
            - ``.abortonconnect``: The ``tspnet.tsp.abortonconnect`` attribute.
            - ``.rbtablecopy()``: The ``tspnet.tsp.rbtablecopy()`` function.
            - ``.runscript()``: The ``tspnet.tsp.runscript()`` function.
        """
        return self._tsp

    def clear(self, connection_id: str) -> None:
        """Run the ``tspnet.clear()`` function.

        Description:
            - This function clears any pending output data from the instrument.

        TSP Syntax:
            ```
            - tspnet.clear()
            ```

        Args:
            connection_id: The connection ID returned from tspnet.connect().

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clear({connection_id})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.clear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def connect(
        self,
        ip_address: str,
        port_number: Optional[int] = None,
        init_string: Optional[str] = None,
        use_t_l_s: Optional[str] = None,
    ) -> str:
        """Run the ``tspnet.connect()`` function.

        Description:
            - This function establishes a network connection with another LAN instrument or device
              through the LAN interface.

        TSP Syntax:
            ```
            - tspnet.connect()
            ```

        Args:
            ip_address: IP address to which to connect in a string; accepts IP address or host name
                when trying to connect.
            port_number (optional): Port number (default 5025).
            init_string (optional): Initialization string to send to ipAddress; when useTLS is set
                to 1; set this to null.
            use_t_l_s (optional): Determine if the TLS security protocol is negotiated when
                connecting the instrument to the host or IP address.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{ip_address}"',
                    port_number,
                    f'"{init_string}"' if init_string is not None else None,
                    use_t_l_s,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.connect({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.connect()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def disconnect(self, connection_id: str) -> None:
        """Run the ``tspnet.disconnect()`` function.

        Description:
            - This function disconnects a specified TSP-Net session.

        TSP Syntax:
            ```
            - tspnet.disconnect()
            ```

        Args:
            connection_id: The connection ID returned from tspnet.connect().

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.disconnect({connection_id})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.disconnect()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def execute(
        self, connection_id: str, command_string: str, format_string: Optional[str] = None
    ) -> str:
        """Run the ``tspnet.execute()`` function.

        Description:
            - This function sends a command string to the remote device.

        TSP Syntax:
            ```
            - tspnet.execute()
            ```

        Args:
            connection_id: The connection ID returned from tspnet.connect().
            command_string: The command to send to the remote device.
            format_string (optional): Format string for the output.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{connection_id}"',
                    f'"{command_string}"',
                    format_string,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.execute({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.execute()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def idn(self, connection_id: str) -> str:
        """Run the ``tspnet.idn()`` function.

        Description:
            - This function retrieves the response of the remote device to ``*IDN?``.

        TSP Syntax:
            ```
            - tspnet.idn()
            ```

        Args:
            connection_id: The connection ID returned from tspnet.connect().

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.idn({connection_id}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.idn()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def read(self, connection_id: str, format_string: Optional[str] = None) -> str:
        """Run the ``tspnet.read()`` function.

        Description:
            - This function reads data from a remote device.

        TSP Syntax:
            ```
            - tspnet.read()
            ```

        Args:
            connection_id: The connection ID returned from tspnet.connect().
            format_string (optional): Format string for the output, maximum of 10 specifiers.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    connection_id,
                    format_string,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.read({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.read()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readavailable(self, connection_id: str) -> str:
        """Run the ``tspnet.readavailable()`` function.

        Description:
            - This function checks to see if data is available from the remote device.

        TSP Syntax:
            ```
            - tspnet.readavailable()
            ```

        Args:
            connection_id: The connection ID returned from tspnet.connect().

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readavailable({connection_id}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.readavailable()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self) -> None:
        """Run the ``tspnet.reset()`` function.

        Description:
            - This function disconnects all TSP-Net sessions.

        TSP Syntax:
            ```
            - tspnet.reset()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def termination(self, connection_id: str, term_sequence: Optional[str] = None) -> str:
        """Run the ``tspnet.termination()`` function.

        Description:
            - This function sets the device line termination sequence.

        TSP Syntax:
            ```
            - tspnet.termination()
            ```

        Args:
            connection_id: The connection ID returned from tspnet.connect().
            term_sequence (optional): The termination sequence.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    connection_id,
                    term_sequence,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.termination({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.termination()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def write(self, connection_id: str, input_string: str) -> None:
        """Run the ``tspnet.write()`` function.

        Description:
            - This function writes a string to the remote instrument.

        TSP Syntax:
            ```
            - tspnet.write()
            ```

        Args:
            connection_id: The connection ID returned from tspnet.connect().
            input_string: The string to be written.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.write({connection_id}, "{input_string}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.write()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
