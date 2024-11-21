# pylint: disable=line-too-long
"""The diagnostic commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DIAGnostic:DATA?
    - DIAGnostic:IMMediate
    - DIAGnostic:IMMediate?
    - DIAGnostic:SELect {ALL|FPANel|AREGister|DTIMing|A1Memory|A2Memory|A3Memory|A4Memory|CREGister|CPLock|O1Register|O1ALevel|O1MLevel|O2Register|O2ALevel|O2MLevel}
    - DIAGnostic:SELect?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DiagnosticSelect(SCPICmdWrite, SCPICmdRead):
    """The ``DIAGnostic:SELect`` command.

    Description:
        - This command selects the self-test routines. The query form of this command returns the
          selected test routine. The following selections are available: ALL FPANel - Front panel
          read/write access test DTIMing - Data timing measurement (for AWG5000 series only)
          AREGister - AWG register read back A1Memory - CH1 waveform memory test A2Memory - CH2
          waveform memory test A3Memory - CH3 waveform memory test (for AWG5000 series only)
          A4Memory - CH4 Waveform memory test (for AWG5000 series only) CREGister - Clock register
          read back CPLock - PLL Lock/unlock O1Register - Output1 register read back O1ALevel -
          Output1 analog level O1MLevel - Output1 Marker level (for AWG7000 series only) O2Register
          - Output2 register read back O2ALevel - Output2 analog level O2MLevel - Output2 marker
          level (for AWG7000 series only)

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:SELect?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIAGnostic:SELect value`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:SELect {ALL|FPANel|AREGister|DTIMing|A1Memory|A2Memory|A3Memory|A4Memory|CREGister|CPLock|O1Register|O1ALevel|O1MLevel|O2Register|O2ALevel|O2MLevel}
        - DIAGnostic:SELect?
        ```
    """  # noqa: E501


class DiagnosticImmediate(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``DIAGnostic:IMMediate`` command.

    Description:
        - This command executes all of the NORMal diagnostic tests. The query form of this command
          executes all of the NORMal diagnostics and returns the results in the form of numeric of
          values of 0 for no errors or -330 for one or more tests failed. This changes the active
          mode to DIAGnostic, if necessary, and returns back to the original active mode when done.
          This makes a single pass of all of the NORMal diagnostics.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:IMMediate?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:IMMediate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``DIAGnostic:IMMediate`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:IMMediate
        - DIAGnostic:IMMediate?
        ```
    """


class DiagnosticData(SCPICmdRead):
    """The ``DIAGnostic:DATA`` command.

    Description:
        - This command returns the results of last executed tests for the NORMal diagnostic type in
          the form of a numeric value of 0 for no errors or -330 for one or more tests failed.
          Additional error details can be found by using the subsystem, area, and test queries such
          as ``DIAGnostic:RESult?`` <subsystem>[,<area>[,<test>]].

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:DATA?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DIAGnostic:DATA?
        ```
    """


class Diagnostic(SCPICmdRead):
    """The ``DIAGnostic`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``DIAGnostic:DATA`` command.
        - ``.select``: The ``DIAGnostic:SELect`` command.
        - ``.immediate``: The ``DIAGnostic:IMMediate`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "DIAGnostic"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._data = DiagnosticData(device, f"{self._cmd_syntax}:DATA")
        self._select = DiagnosticSelect(device, f"{self._cmd_syntax}:SELect")
        self._immediate = DiagnosticImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def data(self) -> DiagnosticData:
        """Return the ``DIAGnostic:DATA`` command.

        Description:
            - This command returns the results of last executed tests for the NORMal diagnostic type
              in the form of a numeric value of 0 for no errors or -330 for one or more tests
              failed. Additional error details can be found by using the subsystem, area, and test
              queries such as ``DIAGnostic:RESult?`` <subsystem>[,<area>[,<test>]].

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:DATA?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DIAGnostic:DATA?
            ```
        """
        return self._data

    @property
    def select(self) -> DiagnosticSelect:
        """Return the ``DIAGnostic:SELect`` command.

        Description:
            - This command selects the self-test routines. The query form of this command returns
              the selected test routine. The following selections are available: ALL FPANel - Front
              panel read/write access test DTIMing - Data timing measurement (for AWG5000 series
              only) AREGister - AWG register read back A1Memory - CH1 waveform memory test A2Memory
              - CH2 waveform memory test A3Memory - CH3 waveform memory test (for AWG5000 series
              only) A4Memory - CH4 Waveform memory test (for AWG5000 series only) CREGister - Clock
              register read back CPLock - PLL Lock/unlock O1Register - Output1 register read back
              O1ALevel - Output1 analog level O1MLevel - Output1 Marker level (for AWG7000 series
              only) O2Register - Output2 register read back O2ALevel - Output2 analog level O2MLevel
              - Output2 marker level (for AWG7000 series only)

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:SELect?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIAGnostic:SELect value`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:SELect {ALL|FPANel|AREGister|DTIMing|A1Memory|A2Memory|A3Memory|A4Memory|CREGister|CPLock|O1Register|O1ALevel|O1MLevel|O2Register|O2ALevel|O2MLevel}
            - DIAGnostic:SELect?
            ```
        """  # noqa: E501
        return self._select

    @property
    def immediate(self) -> DiagnosticImmediate:
        """Return the ``DIAGnostic:IMMediate`` command.

        Description:
            - This command executes all of the NORMal diagnostic tests. The query form of this
              command executes all of the NORMal diagnostics and returns the results in the form of
              numeric of values of 0 for no errors or -330 for one or more tests failed. This
              changes the active mode to DIAGnostic, if necessary, and returns back to the original
              active mode when done. This makes a single pass of all of the NORMal diagnostics.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:IMMediate?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:IMMediate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``DIAGnostic:IMMediate`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:IMMediate
            - DIAGnostic:IMMediate?
            ```
        """
        return self._immediate
