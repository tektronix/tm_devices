"""The multiscope commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MULTiscope:CONFig {ATI|TEKCONnect|TIMESYnc}
    - MULTiscope:EXIT
    - MULTiscope:RESTART
    - MULTiscope:STATUS?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MultiscopeStatus(SCPICmdRead):
    """The ``MULTiscope:STATUS`` command.

    Description:
        - This query returns the current state of oscilloscopes in the MultiScope system.

    Usage:
        - Using the ``.query()`` method will send the ``MULTiscope:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``MULTiscope:STATUS?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MULTiscope:STATUS?
        ```
    """


class MultiscopeRestart(SCPICmdWriteNoArguments):
    """The ``MULTiscope:RESTART`` command.

    Description:
        - This command instructs the Configuration Managers (and active scope applications) across
          the entire MultiScope configuration to exit and restart themselves.

    Usage:
        - Using the ``.write()`` method will send the ``MULTiscope:RESTART`` command.

    SCPI Syntax:
        ```
        - MULTiscope:RESTART
        ```
    """


class MultiscopeExit(SCPICmdWriteNoArguments):
    """The ``MULTiscope:EXIT`` command.

    Description:
        - This command instructs the Configuration Managers (and active scope applications) across
          the entire MultiScope configuration to shutdown.

    Usage:
        - Using the ``.write()`` method will send the ``MULTiscope:EXIT`` command.

    SCPI Syntax:
        ```
        - MULTiscope:EXIT
        ```
    """


class MultiscopeConfig(SCPICmdWrite):
    """The ``MULTiscope:CONFig`` command.

    Description:
        - This command sets or queries the current MultiScope operational configuration. This
          command is for the Master instrument in the multi-instrument configuration.

    Usage:
        - Using the ``.write(value)`` method will send the ``MULTiscope:CONFig value`` command.

    SCPI Syntax:
        ```
        - MULTiscope:CONFig {ATI|TEKCONnect|TIMESYnc}
        ```

    Info:
        - ``ATI`` sets the MultiScope system to use the ATI channels.
        - ``TEKCONNECT`` sets the MultiScope system to use the TekConnect channels.
        - ``TIMESYNC`` sets the MultiScope system to use the TekConnect channels in TimeSync mode.
          TimeSync mode is only available on some instruments. The Master instrument controls the
          instrument hardware such as the horizontal and trigger settings. Desired results are only
          achieved in Single Sequence acquisition mode. Data from all channels can be acquired using
          programmable interface commands.
    """


class Multiscope(SCPICmdRead):
    """The ``MULTiscope`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MULTiscope?`` query.
        - Using the ``.verify(value)`` method will send the ``MULTiscope?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.config``: The ``MULTiscope:CONFig`` command.
        - ``.exit``: The ``MULTiscope:EXIT`` command.
        - ``.restart``: The ``MULTiscope:RESTART`` command.
        - ``.status``: The ``MULTiscope:STATUS`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "MULTiscope"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._config = MultiscopeConfig(device, f"{self._cmd_syntax}:CONFig")
        self._exit = MultiscopeExit(device, f"{self._cmd_syntax}:EXIT")
        self._restart = MultiscopeRestart(device, f"{self._cmd_syntax}:RESTART")
        self._status = MultiscopeStatus(device, f"{self._cmd_syntax}:STATUS")

    @property
    def config(self) -> MultiscopeConfig:
        """Return the ``MULTiscope:CONFig`` command.

        Description:
            - This command sets or queries the current MultiScope operational configuration. This
              command is for the Master instrument in the multi-instrument configuration.

        Usage:
            - Using the ``.write(value)`` method will send the ``MULTiscope:CONFig value`` command.

        SCPI Syntax:
            ```
            - MULTiscope:CONFig {ATI|TEKCONnect|TIMESYnc}
            ```

        Info:
            - ``ATI`` sets the MultiScope system to use the ATI channels.
            - ``TEKCONNECT`` sets the MultiScope system to use the TekConnect channels.
            - ``TIMESYNC`` sets the MultiScope system to use the TekConnect channels in TimeSync
              mode. TimeSync mode is only available on some instruments. The Master instrument
              controls the instrument hardware such as the horizontal and trigger settings. Desired
              results are only achieved in Single Sequence acquisition mode. Data from all channels
              can be acquired using programmable interface commands.
        """
        return self._config

    @property
    def exit(self) -> MultiscopeExit:
        """Return the ``MULTiscope:EXIT`` command.

        Description:
            - This command instructs the Configuration Managers (and active scope applications)
              across the entire MultiScope configuration to shutdown.

        Usage:
            - Using the ``.write()`` method will send the ``MULTiscope:EXIT`` command.

        SCPI Syntax:
            ```
            - MULTiscope:EXIT
            ```
        """
        return self._exit

    @property
    def restart(self) -> MultiscopeRestart:
        """Return the ``MULTiscope:RESTART`` command.

        Description:
            - This command instructs the Configuration Managers (and active scope applications)
              across the entire MultiScope configuration to exit and restart themselves.

        Usage:
            - Using the ``.write()`` method will send the ``MULTiscope:RESTART`` command.

        SCPI Syntax:
            ```
            - MULTiscope:RESTART
            ```
        """
        return self._restart

    @property
    def status(self) -> MultiscopeStatus:
        """Return the ``MULTiscope:STATUS`` command.

        Description:
            - This query returns the current state of oscilloscopes in the MultiScope system.

        Usage:
            - Using the ``.query()`` method will send the ``MULTiscope:STATUS?`` query.
            - Using the ``.verify(value)`` method will send the ``MULTiscope:STATUS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MULTiscope:STATUS?
            ```
        """
        return self._status
