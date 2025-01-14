"""Module containing inner classes to use for APIs for IEEE 488.2 commands."""

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class IEEE4882Commands:
    """An inner class containing an API for all the IEEE 488.2 SCPI commands."""

    ################################################################################################
    # Magic Methods
    ################################################################################################
    def __init__(self, pi_control: "PIControl") -> None:
        """Create an instance of the IEEE 488.2 commands class."""
        self._pi_control = pi_control

    ################################################################################################
    # Public Methods
    ################################################################################################
    def cls(self) -> None:
        r"""Send the ``*CLS`` (Clear Status) command.

        This command (no query form) clears the following:

        - Event Queue
        - Standard Event Status Register
        - Status Byte Register (except the MAV bit)

        If the ``*CLS`` command immediately follows an <EOI> end-of-message terminator,
        the Output Queue and MAV bit (Status Byte Register bit 4) are also cleared.
        MAV indicates that information is in the output queue.
        The device clear (DCL) control message will clear the output queue and thus MAV.
        ``*CLS`` does not clear the output queue or MAV.

        ``*CLS`` can suppress a Service Request that is to be generated by an ``*OPC``.
        """
        self._pi_control.write("*CLS")

    def ese(self, value: Optional[int] = None) -> str:
        """Send or query the ``*ESE`` (Event Status Enable) command.

        This command sets and queries the bits in the Event Status Enable Register (ESER).
        The ESER prevents events from being reported to the Status Byte Register (STB).

        The power-on default for the ESER is 0 if ``*PSC`` is 1. If ``*PSC`` is 0, the ESER
        maintains the previous power cycle value through the current power cycle.

        Args:
            value: An integer specifying the binary bits of the ESER, from 0 to 255.

        Returns:
            The output of the query.

        Raises:
            ValueError: Indicates that the input value is not within the accepted range.
        """
        if value is not None:
            if not 0 <= value <= 255:  # noqa: PLR2004
                msg = f"{value=} is not a valid value. The value must be between 0 and 255."
                raise ValueError(msg)
            return self._pi_control.set_and_check("*ESE", value)
        return self._pi_control.query("*ESE?")

    def esr(self) -> str:
        """Query the ``*ESR?`` (Standard Event Status Register) command.

        This query-only command returns the contents of the Standard Event Status Register (SESR).
        ``*ESR?`` also clears the SESR (since reading the SESR clears it).

        Returns:
            The output of the query.
        """
        return self._pi_control.query("*ESR?")

    def idn(self) -> str:
        """Query the ``*IDN?`` (Identification) command.

        This query-only command returns the instrument identification code.

        Returns:
            The output of the query.
        """
        return self._pi_control.query("*IDN?")

    def lrn(self) -> str:
        """Query the ``*LRN?`` (Learn) command.

        This query-only command returns the commands that list the instrument settings.

        Returns:
            The output of the query.
        """
        return self._pi_control.query("*LRN?")

    def opc(self, write: bool = False) -> str:
        r"""Send or query the ``*OPC`` (Operation Complete) command.

        The ``*OPC`` command generates an operation complete event which propagates
        through the Standard Event Status Register (SESR) when all pending commands
        that block OPC are complete.

        The ``*OPC?`` query returns "1" after all blocking OPC operations are complete.
        The ``*OPC?`` query response is not available to read until all pending operations finish,
        so an appropriate timeout value should be used.

        Args:
            write: A boolean indicating if the ``*OPC`` should be set rather than queried.

        Returns:
            The output of the query, otherwise an empty string.
        """
        if write:
            self._pi_control.write("*OPC")
            return ""
        return self._pi_control.query("*OPC?")

    def opt(self) -> str:
        """Query the ``*OPT?`` (Options) command.

        This query-only command returns a comma separated list of installed options as an
        arbitrary ASCII string (no quotes) of the form:

        ``<optionCode>:<optionDescription>,<optionCode>:<optionDescription>...``

        Returns:
            The output of the query.
        """
        return self._pi_control.query("*OPT?")

    def psc(self, value: Optional[bool] = None) -> str:
        """Send or query the ``*PSC`` (Power-on Status Clear) command.

        This command sets and queries the power-on status flag that controls the automatic
        power-on handling of the SRER, and ESER registers. When ``*PSC`` is true,
        the SRER and ESER registers are set to 0 at power-on. When ``*PSC`` is false,
        the current values in the SRER and ESER registers are preserved in nonvolatile memory
        when power is shut off and are restored at power-on.

        Args:
            value: A boolean indicating the status to set the power-on status flag to.

        Returns:
            The output of the query.
        """
        if value is not None:
            return self._pi_control.set_and_check("*PSC", int(value))

        return self._pi_control.query("*PSC?")

    def rst(self) -> None:
        r"""Send the ``*RST`` (Reset) command.

        This command (no query form) does the following:

        - Recalls the default instrument setup.

        The ``*RST`` command does not change the following:

        - The Power-on Status Clear Flag (``*PSC`` command).
        - The Event Status Enable Register (``*ESE`` command).
        - The Service Request Enable Register (``*SRE`` command).

        ``*RST`` only resets the programmable interface settings, it does not change any
        user interface settings.
        """
        self._pi_control.write("*RST")

    def sre(self, value: Optional[int] = None) -> str:
        """Send or query the ``*SRE`` (Service Request Enable) command.

        The ``*SRE`` (Service Request Enable) command sets and queries the bits in the
        Service Request Enable Register.

        Args:
            value: An integer specifying the binary bits of the SRER, from 0 to 255.

        Returns:
            The output of the query.

        Raises:
            ValueError: Indicates that the input value is not within the accepted range.
        """
        if value is not None:
            if not 0 <= value <= 255:  # noqa: PLR2004
                msg = f"{value=} is not a valid value. The value must be between 0 and 255."
                raise ValueError(msg)
            return self._pi_control.set_and_check("*SRE", value)
        return self._pi_control.query("*SRE?")

    def stb(self) -> str:
        """Query the ``*STB?`` (Status Byte) command.

        The ``*STB?`` (Read Status Byte) query returns the contents of the
        Status Byte Register (SBR) using the Master Summary Status (MSS) bit.

        Returns:
            The output of the query.
        """
        return self._pi_control.query("*STB?")

    def tst(self) -> str:
        """Send the ``*TST?`` (Self-Test) command.

        Tests (self-test) the interface and returns the result.

        Returns:
            The output of the query.
        """
        return self._pi_control.query("*TST?")

    def wai(self) -> None:
        """Send the ``*WAI`` (Wait) command.

        The ``*WAI`` (Wait) command (no query form) prevents the instrument from executing further
        commands or queries until all pending commands that generate an OPC message are complete.
        """
        self._pi_control.write("*WAI")


class TSPIEEE4882Commands(IEEE4882Commands):
    """An inner class containing an API for all the IEEE488.2 TSP commands."""

    ################################################################################################
    # Public Methods
    ################################################################################################
    def cls(self) -> None:
        r"""Send Clear Status commands (``errorqueue.clear()``, ``status.clear()``).

        This command (no query form) clears the following:

        - Event Queue
        - Standard Event Status Register
        - Status Byte Register
        """
        self._pi_control.write("errorqueue.clear()")
        self._pi_control.write("status.reset()")

    def ese(self, value: Optional[int] = None) -> str:
        """Send or query the Event Status Enable (``status.standard.enable``) command.

        This command sets and queries the bits in the Event Status Enable Register (ESER).
        The ESER prevents events from being reported to the Status Byte Register (STB).

        Args:
            value: An integer specifying the binary bits of the ESER, from 0 to 255.

        Returns:
            The output of the query.

        Raises:
            ValueError: Indicates that the input value is not within the accepted range.
        """
        if value is not None:
            if not 0 <= value <= 255:  # noqa: PLR2004
                msg = f"{value=} is not a valid value. The value must be between 0 and 255."
                raise ValueError(msg)
            return self._pi_control.set_and_check("status.standard.enable", value)
        return self._pi_control.query("print(status.standard.enable)")

    def esr(self) -> str:
        """Query the Standard Event Status Register (``print(status.standard.event)``) command.

        This query-only command returns the contents of the Standard Event Status Register (SESR).
        ``print(status.standard.event)`` also clears the SESR (since reading the SESR clears it).

        Returns:
            The output of the query.
        """
        return self._pi_control.query("print(status.standard.event)")

    def opc(self, write: bool = False) -> str:
        r"""Send or query the Operation Complete command.

        The OPC command generates an operation complete event which propagates
        through the Standard Event Status Register (SESR) when all pending commands
        that block OPC are complete.

        Args:
            write: A boolean indicating if the command should be set rather than queried.

        Returns:
            The output of the query, otherwise an empty string.
        """
        if write:
            self._pi_control.write("opc()")
            return ""
        return self._pi_control.query("waitcomplete() print([[1]])")

    def rst(self) -> None:
        r"""Send the Reset (``reset()``) command."""
        self._pi_control.write("reset()")

    def sre(self, value: Optional[int] = None) -> str:
        """Send or query the Service Request Enable (``status.request_enable``) command.

        The ``status.request_enable`` (Service Request Enable) command sets and
        queries the bits in the Service Request Enable Register.

        Args:
            value: An integer specifying the binary bits of the SRER, from 0 to 255.

        Returns:
            The output of the query.

        Raises:
            ValueError: Indicates that the input value is not within the accepted range.
        """
        if value is not None:
            if not 0 <= value <= 255:  # noqa: PLR2004
                msg = f"{value=} is not a valid value. The value must be between 0 and 255."
                raise ValueError(msg)
            return self._pi_control.set_and_check("status.request_enable", value)
        return self._pi_control.query("print(status.request_enable)")

    def stb(self) -> str:
        """Query the Status Byte (``print(status.condition)``) command.

        Returns:
            The output of the query.
        """
        return self._pi_control.query("print(status.condition)")

    def tst(self) -> str:
        """Send the (``print([[0]])``) (Self-Test) command.

        Tests (self-test) the interface and returns the result.

        Returns:
            The output of the query.
        """
        return self._pi_control.query("print([[0]])")

    def wai(self) -> None:
        """Send the ``waitcomplete()`` command."""
        self._pi_control.write("waitcomplete()")


class LegacyTSPIEEE4882Commands(TSPIEEE4882Commands):
    """An inner class containing an API for all the IEEE 488.2 commands for legacy TSP models."""

    ################################################################################################
    # Public Methods
    ################################################################################################
    def cls(self) -> None:
        r"""Send Clear Status commands (``eventlog.clear()``, ``status.clear()``).

        This command (no query form) clears the following:

        - Event Queue
        - Standard Event Status Register
        - Status Byte Register
        """
        self._pi_control.write("eventlog.clear()")
        self._pi_control.write("status.clear()")
