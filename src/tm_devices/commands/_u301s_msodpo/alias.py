"""The alias commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - ALIas {OFF|ON|<NR1>}
    - ALIas:CATalog?
    - ALIas:DEFine <QString><,>{<QString>|<Block>}? <QString>
    - ALIas:DELEte <QString>
    - ALIas:DELEte:ALL
    - ALIas:DELEte:NAMe <QString>
    - ALIas:STATE {<NR1>|OFF|ON}
    - ALIas:STATE?
    - ALIas?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class AliasState(SCPICmdWrite, SCPICmdRead):
    """The ``ALIas:STATE`` command.

    **Description:**
        - Turns aliases on or off.

    **Usage:**
        - Using the ``.query()`` method will send the ``ALIas:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ALIas:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ALIas:STATE value`` command.

    **SCPI Syntax:**

    ::

        - ALIas:STATE {<NR1>|OFF|ON}
        - ALIas:STATE?

    **Info:**
        - ``OFF`` or <NR1> = 0 turns alias expansion off. If a defined alias is sent when
          ``ALIas:STATE`` is OFF, a command error (102) is generated.
        - ``ON`` or <NR1>0 turns alias expansion on. When a defined alias is received, the specified
          command sequence is substituted for the alias and executed.
    """


class AliasDeleteName(SCPICmdWrite):
    """The ``ALIas:DELEte:NAMe`` command.

    **Description:**
        - Removes a specified alias.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``ALIas:DELEte:NAMe value`` command.

    **SCPI Syntax:**

    ::

        - ALIas:DELEte:NAMe <QString>

    **Info:**
        - ``<QString>`` is the name of the alias to remove. Using <QString> must be an existing
          alias.
    """

    _WRAP_ARG_WITH_QUOTES = True


class AliasDeleteAll(SCPICmdWriteNoArguments):
    """The ``ALIas:DELEte:ALL`` command.

    **Description:**
        - This command deletes all existing aliases.

    **Usage:**
        - Using the ``.write()`` method will send the ``ALIas:DELEte:ALL`` command.

    **SCPI Syntax:**

    ::

        - ALIas:DELEte:ALL
    """


class AliasDelete(SCPICmdWrite, SCPICmdRead):
    """The ``ALIas:DELEte`` command.

    **Description:**
        - This command removes a specified alias and is identical to ``ALIas:DELEte:NAMe``. An error
          message is generated if the named alias does not exist.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``ALIas:DELEte value`` command.

    **SCPI Syntax:**

    ::

        - ALIas:DELEte <QString>

    **Info:**
        - ``<QString>`` is the name of the alias to be removed. Using <QString> must be a previously
          defined value.

    Properties:
        - ``.all``: The ``ALIas:DELEte:ALL`` command.
        - ``.name``: The ``ALIas:DELEte:NAMe`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._all = AliasDeleteAll(device, f"{self._cmd_syntax}:ALL")
        self._name = AliasDeleteName(device, f"{self._cmd_syntax}:NAMe")

    @property
    def all(self) -> AliasDeleteAll:
        """Return the ``ALIas:DELEte:ALL`` command.

        **Description:**
            - This command deletes all existing aliases.

        **Usage:**
            - Using the ``.write()`` method will send the ``ALIas:DELEte:ALL`` command.

        **SCPI Syntax:**

        ::

            - ALIas:DELEte:ALL
        """
        return self._all

    @property
    def name(self) -> AliasDeleteName:
        """Return the ``ALIas:DELEte:NAMe`` command.

        **Description:**
            - Removes a specified alias.

        **Usage:**
            - Using the ``.write(value)`` method will send the ``ALIas:DELEte:NAMe value`` command.

        **SCPI Syntax:**

        ::

            - ALIas:DELEte:NAMe <QString>

        **Info:**
            - ``<QString>`` is the name of the alias to remove. Using <QString> must be an existing
              alias.
        """
        return self._name


class AliasDefine(SCPICmdWrite):
    """The ``ALIas:DEFine`` command.

    **Description:**
        - Assigns a sequence of program messages to an alias label. These messages are then
          substituted for the alias whenever it is received as a command or query, provided that
          ``ALIas:STATE`` has been turned on. The query form of this command returns the definitions
          of a selected alias.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``ALIas:DEFine value`` command.

    **SCPI Syntax:**

    ::

        - ALIas:DEFine <QString><,>{<QString>|<Block>}? <QString>

    **Info:**
        - ``<QString>`` is the alias label.
        - ``<QString>`` or <Block> is a complete sequence of program messages.
    """


class AliasCatalog(SCPICmdRead):
    """The ``ALIas:CATalog`` command.

    **Description:**
        - This query-only command returns a list of the currently defined alias labels, separated by
          commas. If no aliases are defined, the query returns the string ''.

    **Usage:**
        - Using the ``.query()`` method will send the ``ALIas:CATalog?`` query.
        - Using the ``.verify(value)`` method will send the ``ALIas:CATalog?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - ALIas:CATalog?
    """


class Alias(SCPICmdWrite, SCPICmdRead):
    """The ``ALIas`` command.

    **Description:**
        - This command sets or queries the state of alias functionality, and it is identical to the
          ``ALIAS:STATE`` command.

    **Usage:**
        - Using the ``.query()`` method will send the ``ALIas?`` query.
        - Using the ``.verify(value)`` method will send the ``ALIas?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ALIas value`` command.

    **SCPI Syntax:**

    ::

        - ALIas {OFF|ON|<NR1>}
        - ALIas?

    **Info:**
        - ``OFF`` turns Alias expansion off.
        - ``ON`` turns Alias expansion on. When a defined alias is received, the specified command
          sequence is substituted for the alias and executed.
        - ``<NR1>`` = 0 disables Alias mode; any other value enables Alias mode.

    Properties:
        - ``.catalog``: The ``ALIas:CATalog`` command.
        - ``.define``: The ``ALIas:DEFine`` command.
        - ``.delete``: The ``ALIas:DELEte`` command.
        - ``.state``: The ``ALIas:STATE`` command.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "ALIas") -> None:
        super().__init__(device, cmd_syntax)
        self._catalog = AliasCatalog(device, f"{self._cmd_syntax}:CATalog")
        self._define = AliasDefine(device, f"{self._cmd_syntax}:DEFine")
        self._delete = AliasDelete(device, f"{self._cmd_syntax}:DELEte")
        self._state = AliasState(device, f"{self._cmd_syntax}:STATE")

    @property
    def catalog(self) -> AliasCatalog:
        """Return the ``ALIas:CATalog`` command.

        **Description:**
            - This query-only command returns a list of the currently defined alias labels,
              separated by commas. If no aliases are defined, the query returns the string ''.

        **Usage:**
            - Using the ``.query()`` method will send the ``ALIas:CATalog?`` query.
            - Using the ``.verify(value)`` method will send the ``ALIas:CATalog?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - ALIas:CATalog?
        """
        return self._catalog

    @property
    def define(self) -> AliasDefine:
        """Return the ``ALIas:DEFine`` command.

        **Description:**
            - Assigns a sequence of program messages to an alias label. These messages are then
              substituted for the alias whenever it is received as a command or query, provided that
              ``ALIas:STATE`` has been turned on. The query form of this command returns the
              definitions of a selected alias.

        **Usage:**
            - Using the ``.write(value)`` method will send the ``ALIas:DEFine value`` command.

        **SCPI Syntax:**

        ::

            - ALIas:DEFine <QString><,>{<QString>|<Block>}? <QString>

        **Info:**
            - ``<QString>`` is the alias label.
            - ``<QString>`` or <Block> is a complete sequence of program messages.
        """
        return self._define

    @property
    def delete(self) -> AliasDelete:
        """Return the ``ALIas:DELEte`` command.

        **Description:**
            - This command removes a specified alias and is identical to ``ALIas:DELEte:NAMe``. An
              error message is generated if the named alias does not exist.

        **Usage:**
            - Using the ``.write(value)`` method will send the ``ALIas:DELEte value`` command.

        **SCPI Syntax:**

        ::

            - ALIas:DELEte <QString>

        **Info:**
            - ``<QString>`` is the name of the alias to be removed. Using <QString> must be a
              previously defined value.

        Sub-properties:
            - ``.all``: The ``ALIas:DELEte:ALL`` command.
            - ``.name``: The ``ALIas:DELEte:NAMe`` command.
        """
        return self._delete

    @property
    def state(self) -> AliasState:
        """Return the ``ALIas:STATE`` command.

        **Description:**
            - Turns aliases on or off.

        **Usage:**
            - Using the ``.query()`` method will send the ``ALIas:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ALIas:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ALIas:STATE value`` command.

        **SCPI Syntax:**

        ::

            - ALIas:STATE {<NR1>|OFF|ON}
            - ALIas:STATE?

        **Info:**
            - ``OFF`` or <NR1> = 0 turns alias expansion off. If a defined alias is sent when
              ``ALIas:STATE`` is OFF, a command error (102) is generated.
            - ``ON`` or <NR1>0 turns alias expansion on. When a defined alias is received, the
              specified command sequence is substituted for the alias and executed.
        """
        return self._state
