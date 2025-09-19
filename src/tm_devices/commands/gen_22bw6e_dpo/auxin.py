"""The auxin commands module.

These commands are used in the following models:
DPO7AX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUXIn:PRObe:GAIN?
    - AUXIn:VTERM:DUAL:A <NR3>
    - AUXIn:VTERM:DUAL:A?
    - AUXIn:VTERM:DUAL:B <NR3>
    - AUXIn:VTERM:DUAL:B?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AuxinVtermDualB(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:VTERM:DUAL:B`` command.

    Description:
        - This command sets or queries the B voltage termination for probes with dual inputs that
          support settable termination voltage.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:VTERM:DUAL:B?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:VTERM:DUAL:B?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:VTERM:DUAL:B value`` command.

    SCPI Syntax:
        ```
        - AUXIn:VTERM:DUAL:B <NR3>
        - AUXIn:VTERM:DUAL:B?
        ```

    Info:
        - ``<NR3>`` is the voltage termination to be set to the B side.
    """


class AuxinVtermDualA(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:VTERM:DUAL:A`` command.

    Description:
        - This command sets or queries the A voltage termination for probes with dual inputs that
          support settable termination voltage.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:VTERM:DUAL:A?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:VTERM:DUAL:A?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:VTERM:DUAL:A value`` command.

    SCPI Syntax:
        ```
        - AUXIn:VTERM:DUAL:A <NR3>
        - AUXIn:VTERM:DUAL:A?
        ```

    Info:
        - ``<NR3>`` is the voltage termination to be set to the A side.
    """


class AuxinVtermDual(SCPICmdRead):
    """The ``AUXIn:VTERM:DUAL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:VTERM:DUAL?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:VTERM:DUAL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.a``: The ``AUXIn:VTERM:DUAL:A`` command.
        - ``.b``: The ``AUXIn:VTERM:DUAL:B`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._a = AuxinVtermDualA(device, f"{self._cmd_syntax}:A")
        self._b = AuxinVtermDualB(device, f"{self._cmd_syntax}:B")

    @property
    def a(self) -> AuxinVtermDualA:
        """Return the ``AUXIn:VTERM:DUAL:A`` command.

        Description:
            - This command sets or queries the A voltage termination for probes with dual inputs
              that support settable termination voltage.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:VTERM:DUAL:A?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:VTERM:DUAL:A?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:VTERM:DUAL:A value`` command.

        SCPI Syntax:
            ```
            - AUXIn:VTERM:DUAL:A <NR3>
            - AUXIn:VTERM:DUAL:A?
            ```

        Info:
            - ``<NR3>`` is the voltage termination to be set to the A side.
        """
        return self._a

    @property
    def b(self) -> AuxinVtermDualB:
        """Return the ``AUXIn:VTERM:DUAL:B`` command.

        Description:
            - This command sets or queries the B voltage termination for probes with dual inputs
              that support settable termination voltage.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:VTERM:DUAL:B?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:VTERM:DUAL:B?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:VTERM:DUAL:B value`` command.

        SCPI Syntax:
            ```
            - AUXIn:VTERM:DUAL:B <NR3>
            - AUXIn:VTERM:DUAL:B?
            ```

        Info:
            - ``<NR3>`` is the voltage termination to be set to the B side.
        """
        return self._b


class AuxinVterm(SCPICmdRead):
    """The ``AUXIn:VTERM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:VTERM?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:VTERM?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dual``: The ``AUXIn:VTERM:DUAL`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dual = AuxinVtermDual(device, f"{self._cmd_syntax}:DUAL")

    @property
    def dual(self) -> AuxinVtermDual:
        """Return the ``AUXIn:VTERM:DUAL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:VTERM:DUAL?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:VTERM:DUAL?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.a``: The ``AUXIn:VTERM:DUAL:A`` command.
            - ``.b``: The ``AUXIn:VTERM:DUAL:B`` command.
        """
        return self._dual


class AuxinProbeGain(SCPICmdRead):
    """The ``AUXIn:PRObe:GAIN`` command.

    Description:
        - The gain of a probe is the output divided by the input transfer ratio. For example, a
          common 10x probe has a gain of 0.1.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:GAIN?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:GAIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:GAIN?
        ```
    """


class AuxinProbe(SCPICmdRead):
    """The ``AUXIn:PRObe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.gain``: The ``AUXIn:PRObe:GAIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._gain = AuxinProbeGain(device, f"{self._cmd_syntax}:GAIN")

    @property
    def gain(self) -> AuxinProbeGain:
        """Return the ``AUXIn:PRObe:GAIN`` command.

        Description:
            - The gain of a probe is the output divided by the input transfer ratio. For example, a
              common 10x probe has a gain of 0.1.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:GAIN?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:GAIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:GAIN?
            ```
        """
        return self._gain


class Auxin(SCPICmdRead):
    """The ``AUXIn`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.probe``: The ``AUXIn:PRObe`` command tree.
        - ``.vterm``: The ``AUXIn:VTERM`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUXIn") -> None:
        super().__init__(device, cmd_syntax)
        self._probe = AuxinProbe(device, f"{self._cmd_syntax}:PRObe")
        self._vterm = AuxinVterm(device, f"{self._cmd_syntax}:VTERM")

    @property
    def probe(self) -> AuxinProbe:
        """Return the ``AUXIn:PRObe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.gain``: The ``AUXIn:PRObe:GAIN`` command.
        """
        return self._probe

    @property
    def vterm(self) -> AuxinVterm:
        """Return the ``AUXIn:VTERM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:VTERM?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:VTERM?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dual``: The ``AUXIn:VTERM:DUAL`` command tree.
        """
        return self._vterm
