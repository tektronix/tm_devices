"""The status commands module.

These commands are used in the following models:
AWG5200, AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - STATus:OPERation:CONDition?
    - STATus:OPERation:ENABle <NR1>
    - STATus:OPERation:ENABle?
    - STATus:OPERation:EVENt?
    - STATus:OPERation:NTRansition <bit_value>
    - STATus:OPERation:NTRansition?
    - STATus:OPERation:PTRansition <bit_value>
    - STATus:OPERation:PTRansition?
    - STATus:PRESet
    - STATus:QUEStionable:CONDition?
    - STATus:QUEStionable:ENABle <bit_value>
    - STATus:QUEStionable:ENABle?
    - STATus:QUEStionable:EVENt?
    - STATus:QUEStionable:NTRansition <bit_value>
    - STATus:QUEStionable:NTRansition?
    - STATus:QUEStionable:PTRansition <bit_value>
    - STATus:QUEStionable:PTRansition?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class StatusQuestionablePtransition(SCPICmdWrite, SCPICmdRead):
    """The ``STATus:QUEStionable:PTRansition`` command.

    Description:
        - This command sets or queries the positive transition filter value of the Questionable
          Transition Register (QTR). Refer to the Status and event reporting system section for
          additional information.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:QUEStionable:PTRansition?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:PTRansition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``STATus:QUEStionable:PTRansition value``
          command.

    SCPI Syntax:
        ```
        - STATus:QUEStionable:PTRansition <bit_value>
        - STATus:QUEStionable:PTRansition?
        ```
    """


class StatusQuestionableNtransition(SCPICmdWrite, SCPICmdRead):
    """The ``STATus:QUEStionable:NTRansition`` command.

    Description:
        - This command sets or returns the negative transition filter value of the Questionable
          Transition Register (QTR). Refer to the Status and event reporting system section for
          additional information.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:QUEStionable:NTRansition?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:NTRansition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``STATus:QUEStionable:NTRansition value``
          command.

    SCPI Syntax:
        ```
        - STATus:QUEStionable:NTRansition <bit_value>
        - STATus:QUEStionable:NTRansition?
        ```
    """


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
        - ``.ntransition``: The ``STATus:QUEStionable:NTRansition`` command.
        - ``.ptransition``: The ``STATus:QUEStionable:PTRansition`` command.
        - ``.event``: The ``STATus:QUEStionable:EVENt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = StatusQuestionableCondition(device, f"{self._cmd_syntax}:CONDition")
        self._enable = StatusQuestionableEnable(device, f"{self._cmd_syntax}:ENABle")
        self._ntransition = StatusQuestionableNtransition(device, f"{self._cmd_syntax}:NTRansition")
        self._ptransition = StatusQuestionablePtransition(device, f"{self._cmd_syntax}:PTRansition")
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
    def ntransition(self) -> StatusQuestionableNtransition:
        """Return the ``STATus:QUEStionable:NTRansition`` command.

        Description:
            - This command sets or returns the negative transition filter value of the Questionable
              Transition Register (QTR). Refer to the Status and event reporting system section for
              additional information.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:QUEStionable:NTRansition?``
              query.
            - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:NTRansition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``STATus:QUEStionable:NTRansition value`` command.

        SCPI Syntax:
            ```
            - STATus:QUEStionable:NTRansition <bit_value>
            - STATus:QUEStionable:NTRansition?
            ```
        """
        return self._ntransition

    @property
    def ptransition(self) -> StatusQuestionablePtransition:
        """Return the ``STATus:QUEStionable:PTRansition`` command.

        Description:
            - This command sets or queries the positive transition filter value of the Questionable
              Transition Register (QTR). Refer to the Status and event reporting system section for
              additional information.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:QUEStionable:PTRansition?``
              query.
            - Using the ``.verify(value)`` method will send the ``STATus:QUEStionable:PTRansition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``STATus:QUEStionable:PTRansition value`` command.

        SCPI Syntax:
            ```
            - STATus:QUEStionable:PTRansition <bit_value>
            - STATus:QUEStionable:PTRansition?
            ```
        """
        return self._ptransition

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


class StatusOperationPtransition(SCPICmdWrite, SCPICmdRead):
    """The ``STATus:OPERation:PTRansition`` command.

    Description:
        - This command sets or returns the positive transition filter value of the Operation
          Transition Register (OTR).

    Usage:
        - Using the ``.query()`` method will send the ``STATus:OPERation:PTRansition?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:OPERation:PTRansition?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``STATus:OPERation:PTRansition value``
          command.

    SCPI Syntax:
        ```
        - STATus:OPERation:PTRansition <bit_value>
        - STATus:OPERation:PTRansition?
        ```
    """


class StatusOperationNtransition(SCPICmdWrite, SCPICmdRead):
    """The ``STATus:OPERation:NTRansition`` command.

    Description:
        - This command sets or returns the negative transition filter value of the Operation
          Transition Register (OTR).

    Usage:
        - Using the ``.query()`` method will send the ``STATus:OPERation:NTRansition?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:OPERation:NTRansition?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``STATus:OPERation:NTRansition value``
          command.

    SCPI Syntax:
        ```
        - STATus:OPERation:NTRansition <bit_value>
        - STATus:OPERation:NTRansition?
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
        - This command sets or returns the mask for the Operation Enable Register.

    Usage:
        - Using the ``.query()`` method will send the ``STATus:OPERation:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the ``STATus:OPERation:ENABle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``STATus:OPERation:ENABle value``
          command.

    SCPI Syntax:
        ```
        - STATus:OPERation:ENABle <NR1>
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
        - ``.ntransition``: The ``STATus:OPERation:NTRansition`` command.
        - ``.ptransition``: The ``STATus:OPERation:PTRansition`` command.
        - ``.event``: The ``STATus:OPERation:EVENt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = StatusOperationCondition(device, f"{self._cmd_syntax}:CONDition")
        self._enable = StatusOperationEnable(device, f"{self._cmd_syntax}:ENABle")
        self._ntransition = StatusOperationNtransition(device, f"{self._cmd_syntax}:NTRansition")
        self._ptransition = StatusOperationPtransition(device, f"{self._cmd_syntax}:PTRansition")
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
            - This command sets or returns the mask for the Operation Enable Register.

        Usage:
            - Using the ``.query()`` method will send the ``STATus:OPERation:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:OPERation:ENABle?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``STATus:OPERation:ENABle value``
              command.

        SCPI Syntax:
            ```
            - STATus:OPERation:ENABle <NR1>
            - STATus:OPERation:ENABle?
            ```
        """
        return self._enable

    @property
    def ntransition(self) -> StatusOperationNtransition:
        """Return the ``STATus:OPERation:NTRansition`` command.

        Description:
            - This command sets or returns the negative transition filter value of the Operation
              Transition Register (OTR).

        Usage:
            - Using the ``.query()`` method will send the ``STATus:OPERation:NTRansition?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:OPERation:NTRansition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``STATus:OPERation:NTRansition value`` command.

        SCPI Syntax:
            ```
            - STATus:OPERation:NTRansition <bit_value>
            - STATus:OPERation:NTRansition?
            ```
        """
        return self._ntransition

    @property
    def ptransition(self) -> StatusOperationPtransition:
        """Return the ``STATus:OPERation:PTRansition`` command.

        Description:
            - This command sets or returns the positive transition filter value of the Operation
              Transition Register (OTR).

        Usage:
            - Using the ``.query()`` method will send the ``STATus:OPERation:PTRansition?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus:OPERation:PTRansition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``STATus:OPERation:PTRansition value`` command.

        SCPI Syntax:
            ```
            - STATus:OPERation:PTRansition <bit_value>
            - STATus:OPERation:PTRansition?
            ```
        """
        return self._ptransition

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
            - ``.ntransition``: The ``STATus:OPERation:NTRansition`` command.
            - ``.ptransition``: The ``STATus:OPERation:PTRansition`` command.
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
            - ``.ntransition``: The ``STATus:QUEStionable:NTRansition`` command.
            - ``.ptransition``: The ``STATus:QUEStionable:PTRansition`` command.
            - ``.event``: The ``STATus:QUEStionable:EVENt`` command.
        """
        return self._questionable
