"""The fpanel commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FPAnel:PRESS <button>
    - FPAnel:TURN <knob>,[<n>]
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
        - FPAnel:TURN <knob>,[<n>]
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


class Fpanel(SCPICmdRead):
    """The ``FPAnel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FPAnel?`` query.
        - Using the ``.verify(value)`` method will send the ``FPAnel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.press``: The ``FPAnel:PRESS`` command.
        - ``.turn``: The ``FPAnel:TURN`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "FPAnel") -> None:
        super().__init__(device, cmd_syntax)
        self._press = FpanelPress(device, f"{self._cmd_syntax}:PRESS")
        self._turn = FpanelTurn(device, f"{self._cmd_syntax}:TURN")

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
            - FPAnel:TURN <knob>,[<n>]
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
