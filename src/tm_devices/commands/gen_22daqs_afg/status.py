"""The status commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *ESE <bit_value>
    - *ESE?
    - *PSC <NR1>
    - *PSC?
    - *SRE <bit_value>
    - *SRE?
    - STATus:OPERation:CONDition?
    - STATus:OPERation:ENABle <bit_value>
    - STATus:OPERation:ENABle?
    - STATus:OPERation:EVENt?
    - STATus:PRESet
    - STATus:QUEStionable:CONDition?
    - STATus:QUEStionable:ENABle <bit_value>
    - STATus:QUEStionable:ENABle?
    - STATus:QUEStionable:EVENt?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class StatusQuestionableEvent(SCPICmdRead):
    """The ``STATus:QUEStionable:EVENt`` command.

    Description:
        - This query-only command returns the value in the Questionable Event Register and clears
          the Questionable Event Register.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:QUEStionable:EVENt?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:EVENt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - STATus:QUEStionable:EVENt?
        ```
    """


class StatusQuestionableEnable(SCPICmdWrite, SCPICmdRead):
    """The ``STATus:QUEStionable:ENABle`` command.

    Description:
        - This command sets or queries the mask for the Questionable Enable Register.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:QUEStionable:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:ENABle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``STATus:QUEStionable:ENABle value``
          command.

    SCPI Syntax:
        ```
        - STATus:QUEStionable:ENABle <bit_value>
        - STATus:QUEStionable:ENABle?
        ```
    """


class StatusQuestionableCondition(SCPICmdRead):
    """The ``STATus:QUEStionable:CONDition`` command.

    Description:
        - This query-only command returns the contents of the Questionable Condition Register.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:QUEStionable:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:CONDition?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - STATus:QUEStionable:CONDition?
        ```
    """


class StatusQuestionable(SCPICmdRead):
    """The ``STATus:QUEStionable`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:QUEStionable?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``STATus:QUEStionable:CONDition`` command.
        - ``.enable``: The ``STATus:QUEStionable:ENABle`` command.
        - ``.event``: The ``STATus:QUEStionable:EVENt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = StatusQuestionableCondition(device, f"{self._cmd_syntax}:CONDition")
        self._enable = StatusQuestionableEnable(device, f"{self._cmd_syntax}:ENABle")
        self._event = StatusQuestionableEvent(device, f"{self._cmd_syntax}:EVENt")

    @property
    def condition(self) -> StatusQuestionableCondition:
        """Return the ``STATus:QUEStionable:CONDition`` command.

        Description:
            - This query-only command returns the contents of the Questionable Condition Register.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:QUEStionable:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:CONDition?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - STATus:QUEStionable:CONDition?
            ```
        """
        return self._condition

    @property
    def enable(self) -> StatusQuestionableEnable:
        """Return the ``STATus:QUEStionable:ENABle`` command.

        Description:
            - This command sets or queries the mask for the Questionable Enable Register.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:QUEStionable:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:ENABle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``STATus:QUEStionable:ENABle value``
              command.

        SCPI Syntax:
            ```
            - STATus:QUEStionable:ENABle <bit_value>
            - STATus:QUEStionable:ENABle?
            ```
        """
        return self._enable

    @property
    def event(self) -> StatusQuestionableEvent:
        """Return the ``STATus:QUEStionable:EVENt`` command.

        Description:
            - This query-only command returns the value in the Questionable Event Register and
              clears the Questionable Event Register.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:QUEStionable:EVENt?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:EVENt?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - STATus:QUEStionable:EVENt?
            ```
        """
        return self._event


class StatusPreset(SCPICmdWriteNoArguments):
    """The ``STATus:PRESet`` command.

    Description:
        - This command presets the SCPI status registers (OENR and QENR).

    Usage:
        - Using the ``.write()`` method will send the ``STATus:PRESet`` command.

    SCPI Syntax:
        ```
        - STATus:PRESet
        ```
    """


class StatusOperationEvent(SCPICmdRead):
    """The ``STATus:OPERation:EVENt`` command.

    Description:
        - This query-only command returns the value in the Operation Event Register and clears the
          Operation Event Register.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:OPERation:EVENt?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:OPERation:EVENt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - STATus:OPERation:EVENt?
        ```
    """


class StatusOperationEnable(SCPICmdWrite, SCPICmdRead):
    """The ``STATus:OPERation:ENABle`` command.

    Description:
        - This command sets or queries the mask for the Operation Enable Register.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:OPERation:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:OPERation:ENABle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``STATus:OPERation:ENABle value``
          command.

    SCPI Syntax:
        ```
        - STATus:OPERation:ENABle <bit_value>
        - STATus:OPERation:ENABle?
        ```
    """


class StatusOperationCondition(SCPICmdRead):
    """The ``STATus:OPERation:CONDition`` command.

    Description:
        - This query-only command returns the contents of the Operation Condition Register.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:OPERation:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:OPERation:CONDition?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - STATus:OPERation:CONDition?
        ```
    """


class StatusOperation(SCPICmdRead):
    """The ``STATus:OPERation`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:OPERation?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:OPERation?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``STATus:OPERation:CONDition`` command.
        - ``.enable``: The ``STATus:OPERation:ENABle`` command.
        - ``.event``: The ``STATus:OPERation:EVENt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = StatusOperationCondition(device, f"{self._cmd_syntax}:CONDition")
        self._enable = StatusOperationEnable(device, f"{self._cmd_syntax}:ENABle")
        self._event = StatusOperationEvent(device, f"{self._cmd_syntax}:EVENt")

    @property
    def condition(self) -> StatusOperationCondition:
        """Return the ``STATus:OPERation:CONDition`` command.

        Description:
            - This query-only command returns the contents of the Operation Condition Register.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:OPERation:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:OPERation:CONDition?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - STATus:OPERation:CONDition?
            ```
        """
        return self._condition

    @property
    def enable(self) -> StatusOperationEnable:
        """Return the ``STATus:OPERation:ENABle`` command.

        Description:
            - This command sets or queries the mask for the Operation Enable Register.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:OPERation:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:OPERation:ENABle?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``STATus:OPERation:ENABle value``
              command.

        SCPI Syntax:
            ```
            - STATus:OPERation:ENABle <bit_value>
            - STATus:OPERation:ENABle?
            ```
        """
        return self._enable

    @property
    def event(self) -> StatusOperationEvent:
        """Return the ``STATus:OPERation:EVENt`` command.

        Description:
            - This query-only command returns the value in the Operation Event Register and clears
              the Operation Event Register.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:OPERation:EVENt?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:OPERation:EVENt?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - STATus:OPERation:EVENt?
            ```
        """
        return self._event


class Status(SCPICmdRead):
    """The ``STATus`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.operation``: The ``STATus:OPERation`` command tree.
        - ``.preset``: The ``STATus:PRESet`` command.
        - ``.questionable``: The ``STATus:QUEStionable`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "STATus") -> None:
        super().__init__(device, cmd_syntax)
        self._operation = StatusOperation(device, f"{self._cmd_syntax}:OPERation")
        self._preset = StatusPreset(device, f"{self._cmd_syntax}:PRESet")
        self._questionable = StatusQuestionable(device, f"{self._cmd_syntax}:QUEStionable")

    @property
    def operation(self) -> StatusOperation:
        """Return the ``STATus:OPERation`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:OPERation?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:OPERation?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``STATus:OPERation:CONDition`` command.
            - ``.enable``: The ``STATus:OPERation:ENABle`` command.
            - ``.event``: The ``STATus:OPERation:EVENt`` command.
        """
        return self._operation

    @property
    def preset(self) -> StatusPreset:
        """Return the ``STATus:PRESet`` command.

        Description:
            - This command presets the SCPI status registers (OENR and QENR).

        Usage:
            - Using the ``.write()`` method will send the ``STATus:PRESet`` command.

        SCPI Syntax:
            ```
            - STATus:PRESet
            ```
        """
        return self._preset

    @property
    def questionable(self) -> StatusQuestionable:
        """Return the ``STATus:QUEStionable`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:QUEStionable?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``STATus:QUEStionable:CONDition`` command.
            - ``.enable``: The ``STATus:QUEStionable:ENABle`` command.
            - ``.event``: The ``STATus:QUEStionable:EVENt`` command.
        """
        return self._questionable


class Sre(SCPICmdWrite, SCPICmdRead):
    """The ``*SRE`` command.

    Description:
        - This command sets and queries the bits in the Service Request Enable Register (SRER).

    Usage:
        - Using the ``.query()`` method will send the ``*SRE?`` query.
        - Using the ``.verify(value)`` method will send the ``*SRE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*SRE value`` command.

    SCPI Syntax:
        ```
        - *SRE <bit_value>
        - *SRE?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*SRE") -> None:
        super().__init__(device, cmd_syntax)


class Psc(SCPICmdWrite, SCPICmdRead):
    """The ``*PSC`` command.

    Description:
        - This command sets and queries the power-on status flag that controls the automatic
          power-on execution of SRER and ESER. When ``*PSC`` is true, SRER and ESER are set to 0 at
          power-on. When ``*PSC`` is false, the current values in the SRER and ESER are preserved in
          nonvolatile memory when power is shut off and are restored at power-on.

    Usage:
        - Using the ``.query()`` method will send the ``*PSC?`` query.
        - Using the ``.verify(value)`` method will send the ``*PSC?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*PSC value`` command.

    SCPI Syntax:
        ```
        - *PSC <NR1>
        - *PSC?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*PSC") -> None:
        super().__init__(device, cmd_syntax)


class Ese(SCPICmdWrite, SCPICmdRead):
    """The ``*ESE`` command.

    Description:
        - This command sets or queries the bits in the Event Status Enable Register (ESER) used in
          the status and events reporting system of the arbitrary function generator. The query
          command returns the contents of the ESER.

    Usage:
        - Using the ``.query()`` method will send the ``*ESE?`` query.
        - Using the ``.verify(value)`` method will send the ``*ESE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*ESE value`` command.

    SCPI Syntax:
        ```
        - *ESE <bit_value>
        - *ESE?
        ```

    Info:
        - ``<bit_value>::=<NR1>``
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*ESE") -> None:
        super().__init__(device, cmd_syntax)
