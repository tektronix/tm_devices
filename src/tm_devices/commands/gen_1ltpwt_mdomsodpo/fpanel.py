"""The fpanel commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FPAnel:HOLD CURsor [,<NR1>]
    - FPAnel:PRESS <button>
    - FPAnel:TURN <knob>,<n>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class FpanelTurn(SCPICmdWrite):
    """The ``FPAnel:TURN`` command.

    Description:
        - Simulates the action of turning a specified front-panel control knob. When the front panel
          is locked, the front-panel button and multipurpose knob operations are suspended. The
          ``FPANEL:PRESS`` and commands will also not work, and, they will not generate an error.
          You can work around this by using the appropriate programmatic interface commands, instead
          of the front-panel commands. For example, to set the trigger level to 50%, you could use
          ``TRIGger:A SETLevel``. To force a trigger, you could use TRIGger FORCe.

    Usage:
        - Using the ``.write(value)`` method will send the ``FPAnel:TURN value`` command.

    SCPI Syntax:
        ```
        - FPAnel:TURN <knob>,<n>
        ```

    Info:
        - ``<knob>`` is the name of a rotating control.
        - ``<n>`` represents the rotation direction and magnitude of rotation. Negative values
          represent a counterclockwise knob rotation, and positive values represent a clockwise
          rotation. The magnitude of <n> specifies the amount of the turn, where <n> = 1 represents
          turning the knob one unit, <n> = 2 represents turning the knob two units, <n> = 4
          represents turning the knob four units, and so on. The range of units depends on which
          front panel knob is specified.
        - ``Multipurpose a`` knob.
        - ``Multipurpose b`` knob.
        - ``Position`` knob.
        - ``Scale`` knob.
        - ``Level`` knob.
        - ``Position`` knob.
        - ``Scale`` knob.
    """


class FpanelPress(SCPICmdWrite):
    """The ``FPAnel:PRESS`` command.

    Description:
        - Simulates the action of pressing a specified front-panel button. When the front panel is
          locked, the front-panel button and multipurpose knob operations are suspended. The and the
          ``FPANEL:TURN`` commands will also not work. You can work around this by using the
          appropriate programmatic interface commands, instead of the front-panel commands.

    Usage:
        - Using the ``.write(value)`` method will send the ``FPAnel:PRESS value`` command.

    SCPI Syntax:
        ```
        - FPAnel:PRESS <button>
        ```

    Info:
        - ``<button>`` is the name of a front-panel button. Most of the argument names associate
          directly with their front panel buttons. For example, AUTOSet is for the Autoset button.
        - ``Acquire`` button.
        - ``Arbitrary Function Generator`` button.
        - ``Autoset`` button.
        - ``Cursors`` button.
        - ``D<x>`` button x has a minimum of 15 and a maximum of 0.
        - ``Default Setup`` button.
        - ``Fine`` button.
        - ``Force Trig`` button.
        - ``Print`` button.
        - ``Intensity`` button.
        - ``Set/Clear`` button.
        - ``M`` button.
        - ``Menu Off`` button.
        - ``Measure`` button.
        - ``R`` button.
        - ``Run/Stop`` button.
        - ``Save`` button.
        - ``Menu`` button.
        - ``Search`` button.
        - ``Select`` button.
        - ``Single`` button.
        - ``Test`` button.
        - ``Menu`` button.
        - ``Utility`` button.
    """


class FpanelHold(SCPICmdWrite):
    """The ``FPAnel:HOLD`` command.

    Description:
        - This command is used to emulate the button push-and-hold feature. Presently, only the
          Cursors button is supported by this command, even though any of the button enumerations
          described for ``FPAnel:PREss`` are accepted. (When the Cursors button on the front panel
          is held, the cursor menu is displayed on screen.) This command contains two arguments: a
          button, and an optional hold time.

    Usage:
        - Using the ``.write(value)`` method will send the ``FPAnel:HOLD value`` command.

    SCPI Syntax:
        ```
        - FPAnel:HOLD CURsor [,<NR1>]
        ```

    Info:
        - ``CURsor`` - currently this is the only button supported by this command. If the hold time
          is not specified, it defaults to 1200 milliseconds. The range is 0 to 10,000 milliseconds.
          The system expects a minimum of 1 second to recognize a hold.
        - ``<NR1>`` (optional), an integer, is the hold time - ie. the time to emulate holding the
          button down before releasing it, in milliseconds. If the hold time is not specified, it
          defaults to 1200 milliseconds.
    """


class Fpanel(SCPICmdRead):
    """The ``FPAnel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FPAnel?`` query.
        - Using the ``.verify(value)`` method will send the ``FPAnel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hold``: The ``FPAnel:HOLD`` command.
        - ``.press``: The ``FPAnel:PRESS`` command.
        - ``.turn``: The ``FPAnel:TURN`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "FPAnel") -> None:
        super().__init__(device, cmd_syntax)
        self._hold = FpanelHold(device, f"{self._cmd_syntax}:HOLD")
        self._press = FpanelPress(device, f"{self._cmd_syntax}:PRESS")
        self._turn = FpanelTurn(device, f"{self._cmd_syntax}:TURN")

    @property
    def hold(self) -> FpanelHold:
        """Return the ``FPAnel:HOLD`` command.

        Description:
            - This command is used to emulate the button push-and-hold feature. Presently, only the
              Cursors button is supported by this command, even though any of the button
              enumerations described for ``FPAnel:PREss`` are accepted. (When the Cursors button on
              the front panel is held, the cursor menu is displayed on screen.) This command
              contains two arguments: a button, and an optional hold time.

        Usage:
            - Using the ``.write(value)`` method will send the ``FPAnel:HOLD value`` command.

        SCPI Syntax:
            ```
            - FPAnel:HOLD CURsor [,<NR1>]
            ```

        Info:
            - ``CURsor`` - currently this is the only button supported by this command. If the hold
              time is not specified, it defaults to 1200 milliseconds. The range is 0 to 10,000
              milliseconds. The system expects a minimum of 1 second to recognize a hold.
            - ``<NR1>`` (optional), an integer, is the hold time - ie. the time to emulate holding
              the button down before releasing it, in milliseconds. If the hold time is not
              specified, it defaults to 1200 milliseconds.
        """
        return self._hold

    @property
    def press(self) -> FpanelPress:
        """Return the ``FPAnel:PRESS`` command.

        Description:
            - Simulates the action of pressing a specified front-panel button. When the front panel
              is locked, the front-panel button and multipurpose knob operations are suspended. The
              and the ``FPANEL:TURN`` commands will also not work. You can work around this by using
              the appropriate programmatic interface commands, instead of the front-panel commands.

        Usage:
            - Using the ``.write(value)`` method will send the ``FPAnel:PRESS value`` command.

        SCPI Syntax:
            ```
            - FPAnel:PRESS <button>
            ```

        Info:
            - ``<button>`` is the name of a front-panel button. Most of the argument names associate
              directly with their front panel buttons. For example, AUTOSet is for the Autoset
              button.
            - ``Acquire`` button.
            - ``Arbitrary Function Generator`` button.
            - ``Autoset`` button.
            - ``Cursors`` button.
            - ``D<x>`` button x has a minimum of 15 and a maximum of 0.
            - ``Default Setup`` button.
            - ``Fine`` button.
            - ``Force Trig`` button.
            - ``Print`` button.
            - ``Intensity`` button.
            - ``Set/Clear`` button.
            - ``M`` button.
            - ``Menu Off`` button.
            - ``Measure`` button.
            - ``R`` button.
            - ``Run/Stop`` button.
            - ``Save`` button.
            - ``Menu`` button.
            - ``Search`` button.
            - ``Select`` button.
            - ``Single`` button.
            - ``Test`` button.
            - ``Menu`` button.
            - ``Utility`` button.
        """
        return self._press

    @property
    def turn(self) -> FpanelTurn:
        """Return the ``FPAnel:TURN`` command.

        Description:
            - Simulates the action of turning a specified front-panel control knob. When the front
              panel is locked, the front-panel button and multipurpose knob operations are
              suspended. The ``FPANEL:PRESS`` and commands will also not work, and, they will not
              generate an error. You can work around this by using the appropriate programmatic
              interface commands, instead of the front-panel commands. For example, to set the
              trigger level to 50%, you could use ``TRIGger:A SETLevel``. To force a trigger, you
              could use TRIGger FORCe.

        Usage:
            - Using the ``.write(value)`` method will send the ``FPAnel:TURN value`` command.

        SCPI Syntax:
            ```
            - FPAnel:TURN <knob>,<n>
            ```

        Info:
            - ``<knob>`` is the name of a rotating control.
            - ``<n>`` represents the rotation direction and magnitude of rotation. Negative values
              represent a counterclockwise knob rotation, and positive values represent a clockwise
              rotation. The magnitude of <n> specifies the amount of the turn, where <n> = 1
              represents turning the knob one unit, <n> = 2 represents turning the knob two units,
              <n> = 4 represents turning the knob four units, and so on. The range of units depends
              on which front panel knob is specified.
            - ``Multipurpose a`` knob.
            - ``Multipurpose b`` knob.
            - ``Position`` knob.
            - ``Scale`` knob.
            - ``Level`` knob.
            - ``Position`` knob.
            - ``Scale`` knob.
        """
        return self._turn
