# pylint: disable=line-too-long
"""The fpanel commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FPAnel:PRESS {AUTOset|BUS|CH1<x>|CLEAR|DEFaultsetup|FORCetrig|GPKNOB1|GPKNOB2|HORZPOS|MATh|REF|RUNSTop|SETTO50|SINGleseq|TOUCHSCReen|TRIGMode|USER|VERTPOS|VERTSCALE}
    - FPAnel:TURN {GPKNOB1| GPKNOB2| HORZPOS| HORZScale| TRIGLevel| VERTPOS| VERTSCALE} [,<NR1>]
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class FpanelTurn(SCPICmdWrite):
    """The ``FPAnel:TURN`` command.

    Description:
        - This command is used to emulate a knob turn. The optional NR1 specifies the number of
          clicks where negative values indicate counter clockwise. If not specified, the default of
          1 click is used indicating the knob is turned clockwise 1 click.

    Usage:
        - Using the ``.write(value)`` method will send the ``FPAnel:TURN value`` command.

    SCPI Syntax:
        ```
        - FPAnel:TURN {GPKNOB1| GPKNOB2| HORZPOS| HORZScale| TRIGLevel| VERTPOS| VERTSCALE} [,<NR1>]
        ```

    Info:
        - ``<NR1>`` is the number of clicks to turn the knob.
    """


class FpanelPress(SCPICmdWrite):
    """The ``FPAnel:PRESS`` command.

    Description:
        - This command is used to emulate a button press. When used with knob enumerations, this
          command pushes the knob. Use the ``FPANEL:TURN`` command to emulate knob turns.

    Usage:
        - Using the ``.write(value)`` method will send the ``FPAnel:PRESS value`` command.

    SCPI Syntax:
        ```
        - FPAnel:PRESS {AUTOset|BUS|CH1<x>|CLEAR|DEFaultsetup|FORCetrig|GPKNOB1|GPKNOB2|HORZPOS|MATh|REF|RUNSTop|SETTO50|SINGleseq|TOUCHSCReen|TRIGMode|USER|VERTPOS|VERTSCALE}
        ```

    Info:
        - ``AUTOset`` Arguments are the following instrument buttons.
        - ``BUS`` Arguments are the following instrument buttons.
        - ``CH1<x>`` Arguments are the following instrument buttons.
        - ``CLEAR`` Arguments are the following instrument buttons.
        - ``DEFaultsetup`` Arguments are the following instrument buttons.
        - ``FORCetrig`` Arguments are the following instrument buttons.
        - ``GPKNOB1`` Arguments are the following instrument buttons.
        - ``GPKNOB2`` Arguments are the following instrument buttons.
        - ``HORZPOS`` Arguments are the following instrument buttons.
        - ``MATh`` Arguments are the following instrument buttons.
        - ``REF`` Arguments are the following instrument buttons.
        - ``RUNSTop`` Arguments are the following instrument buttons.
        - ``SETTO50`` Arguments are the following instrument buttons.
        - ``SINGleseq`` Arguments are the following instrument buttons.
        - ``TOUCHSCReen`` Arguments are the following instrument buttons.
        - ``TRIGMode`` Arguments are the following instrument buttons.
        - ``USER`` Arguments are the following instrument buttons.
        - ``VERTPOS`` Arguments are the following instrument buttons.
        - ``VERTSCALE`` Arguments are the following instrument buttons.
    """  # noqa: E501


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
            - This command is used to emulate a button press. When used with knob enumerations, this
              command pushes the knob. Use the ``FPANEL:TURN`` command to emulate knob turns.

        Usage:
            - Using the ``.write(value)`` method will send the ``FPAnel:PRESS value`` command.

        SCPI Syntax:
            ```
            - FPAnel:PRESS {AUTOset|BUS|CH1<x>|CLEAR|DEFaultsetup|FORCetrig|GPKNOB1|GPKNOB2|HORZPOS|MATh|REF|RUNSTop|SETTO50|SINGleseq|TOUCHSCReen|TRIGMode|USER|VERTPOS|VERTSCALE}
            ```

        Info:
            - ``AUTOset`` Arguments are the following instrument buttons.
            - ``BUS`` Arguments are the following instrument buttons.
            - ``CH1<x>`` Arguments are the following instrument buttons.
            - ``CLEAR`` Arguments are the following instrument buttons.
            - ``DEFaultsetup`` Arguments are the following instrument buttons.
            - ``FORCetrig`` Arguments are the following instrument buttons.
            - ``GPKNOB1`` Arguments are the following instrument buttons.
            - ``GPKNOB2`` Arguments are the following instrument buttons.
            - ``HORZPOS`` Arguments are the following instrument buttons.
            - ``MATh`` Arguments are the following instrument buttons.
            - ``REF`` Arguments are the following instrument buttons.
            - ``RUNSTop`` Arguments are the following instrument buttons.
            - ``SETTO50`` Arguments are the following instrument buttons.
            - ``SINGleseq`` Arguments are the following instrument buttons.
            - ``TOUCHSCReen`` Arguments are the following instrument buttons.
            - ``TRIGMode`` Arguments are the following instrument buttons.
            - ``USER`` Arguments are the following instrument buttons.
            - ``VERTPOS`` Arguments are the following instrument buttons.
            - ``VERTSCALE`` Arguments are the following instrument buttons.
        """  # noqa: E501
        return self._press

    @property
    def turn(self) -> FpanelTurn:
        """Return the ``FPAnel:TURN`` command.

        Description:
            - This command is used to emulate a knob turn. The optional NR1 specifies the number of
              clicks where negative values indicate counter clockwise. If not specified, the default
              of 1 click is used indicating the knob is turned clockwise 1 click.

        Usage:
            - Using the ``.write(value)`` method will send the ``FPAnel:TURN value`` command.

        SCPI Syntax:
            ```
            - FPAnel:TURN {GPKNOB1| GPKNOB2| HORZPOS| HORZScale| TRIGLevel| VERTPOS| VERTSCALE} [,<NR1>]
            ```

        Info:
            - ``<NR1>`` is the number of clicks to turn the knob.
        """  # noqa: E501
        return self._turn
