# pylint: disable=line-too-long
"""The fpanel commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FPAnel:PRESS {AUTOset|BUS|CH<x>|CLEAR|CURsor|DEFaultsetup|FASTAcq|FORCetrig|GPKNOB1|GPKNOB2|HIGHRES|HORZPOS|HORZScale|MATh|NEXt|PREv|REF|RUNSTop|SETTO50|SINGleseq|TOUCHSCReen|TRIGMode|TRIGSlope|USER|VERTPOS|VERTSCALE|ZOOM}
    - FPAnel:TURN {GPKNOB<x>|HORZPOS|HORZScale|PANKNOB| TRIGLevel|VERTPOS|VERTSCALE|ZOOM} [,<NR1>]
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
        - FPAnel:TURN {GPKNOB<x>|HORZPOS|HORZScale|PANKNOB| TRIGLevel|VERTPOS|VERTSCALE|ZOOM} [,<NR1>]
        ```

    Info:
        - ``GPKNOB1`` emulates a Multipurpose A knob turn.
        - ``GPKNOB2`` emulates a Multipurpose B knob turn.
        - ``HORZPOS`` emulates a Horizontal knob turn.
        - ``HORZScale`` emulates a Horizontal Scale knob turn.
        - ``PANKNOB`` emulates a Pan knob turn.
        - ``TRIGLevel`` emulates a Trigger Level knob turn.
        - ``VERTPOS`` emulates a Vertical Position knob turn.
        - ``VERTSCALE`` emulates a Vertical Scale knob turn.
        - ``ZOOM`` emulates a Zoom knob turn.
        - ``<NR1>`` is the number of clicks to turn the knob.
    """  # noqa: E501


class FpanelPress(SCPICmdWrite):
    """The ``FPAnel:PRESS`` command.

    Description:
        - This command is used to emulate a button press. When used with knob enumerations, this
          command pushes the knob. Use the ``FPANEL:TURN`` command to emulate knob turns.

    Usage:
        - Using the ``.write(value)`` method will send the ``FPAnel:PRESS value`` command.

    SCPI Syntax:
        ```
        - FPAnel:PRESS {AUTOset|BUS|CH<x>|CLEAR|CURsor|DEFaultsetup|FASTAcq|FORCetrig|GPKNOB1|GPKNOB2|HIGHRES|HORZPOS|HORZScale|MATh|NEXt|PREv|REF|RUNSTop|SETTO50|SINGleseq|TOUCHSCReen|TRIGMode|TRIGSlope|USER|VERTPOS|VERTSCALE|ZOOM}
        ```

    Info:
        - ``AUTOset`` emulates a Autoset button press.
        - ``BUS`` emulates a Bus button press.
        - ``CH<x>`` emulates a Channel button press. The channel number is specified by x.
        - ``CLEAR`` emulates a Clear button press.
        - ``CURsor`` emulates a Cursor button press.
        - ``DEFaultsetup`` emulates a Default Setup button press.
        - ``FASTAcq`` emulates a Fast Acq button press.
        - ``FORCetrig`` emulates a Force trigger button press.
        - ``GPKNOB1`` emulates a Multipurpose A knob press.
        - ``GPKNOB2`` emulates a Multipurpose B knob press.
        - ``HIGHRES`` emulates a High Res button press.
        - ``HORZPOS`` emulates a Horizontal knob press.
        - ``HORZScale`` emulates a Horizontal Scale knob press.
        - ``MATh`` emulates a Math button press.
        - ``NEXt`` emulates a Next button press.
        - ``PREv`` emulates a Previous button press.
        - ``REF`` emulates a Ref button press.
        - ``RUNSTop`` emulates a Run/Stop button press.
        - ``SETTO50`` emulates a Set to 50% threshold button press.
        - ``SINGleseq`` emulates a Single/Seq button press.
        - ``TOUCHSCReen`` emulates a Touch Screen button press.
        - ``TRIGMode`` emulates a Trigger Mode button press.
        - ``TRIGSlope`` emulates a Trigger Slope button press.
        - ``USER`` emulates a User button press.
        - ``VERTPOS`` emulates a Vertical Position knob press.
        - ``VERTSCALE`` emulates a Vertical Scale knob press.
        - ``ZOOM`` emulates a Zoom button press.
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
            - FPAnel:PRESS {AUTOset|BUS|CH<x>|CLEAR|CURsor|DEFaultsetup|FASTAcq|FORCetrig|GPKNOB1|GPKNOB2|HIGHRES|HORZPOS|HORZScale|MATh|NEXt|PREv|REF|RUNSTop|SETTO50|SINGleseq|TOUCHSCReen|TRIGMode|TRIGSlope|USER|VERTPOS|VERTSCALE|ZOOM}
            ```

        Info:
            - ``AUTOset`` emulates a Autoset button press.
            - ``BUS`` emulates a Bus button press.
            - ``CH<x>`` emulates a Channel button press. The channel number is specified by x.
            - ``CLEAR`` emulates a Clear button press.
            - ``CURsor`` emulates a Cursor button press.
            - ``DEFaultsetup`` emulates a Default Setup button press.
            - ``FASTAcq`` emulates a Fast Acq button press.
            - ``FORCetrig`` emulates a Force trigger button press.
            - ``GPKNOB1`` emulates a Multipurpose A knob press.
            - ``GPKNOB2`` emulates a Multipurpose B knob press.
            - ``HIGHRES`` emulates a High Res button press.
            - ``HORZPOS`` emulates a Horizontal knob press.
            - ``HORZScale`` emulates a Horizontal Scale knob press.
            - ``MATh`` emulates a Math button press.
            - ``NEXt`` emulates a Next button press.
            - ``PREv`` emulates a Previous button press.
            - ``REF`` emulates a Ref button press.
            - ``RUNSTop`` emulates a Run/Stop button press.
            - ``SETTO50`` emulates a Set to 50% threshold button press.
            - ``SINGleseq`` emulates a Single/Seq button press.
            - ``TOUCHSCReen`` emulates a Touch Screen button press.
            - ``TRIGMode`` emulates a Trigger Mode button press.
            - ``TRIGSlope`` emulates a Trigger Slope button press.
            - ``USER`` emulates a User button press.
            - ``VERTPOS`` emulates a Vertical Position knob press.
            - ``VERTSCALE`` emulates a Vertical Scale knob press.
            - ``ZOOM`` emulates a Zoom button press.
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
            - FPAnel:TURN {GPKNOB<x>|HORZPOS|HORZScale|PANKNOB| TRIGLevel|VERTPOS|VERTSCALE|ZOOM} [,<NR1>]
            ```

        Info:
            - ``GPKNOB1`` emulates a Multipurpose A knob turn.
            - ``GPKNOB2`` emulates a Multipurpose B knob turn.
            - ``HORZPOS`` emulates a Horizontal knob turn.
            - ``HORZScale`` emulates a Horizontal Scale knob turn.
            - ``PANKNOB`` emulates a Pan knob turn.
            - ``TRIGLevel`` emulates a Trigger Level knob turn.
            - ``VERTPOS`` emulates a Vertical Position knob turn.
            - ``VERTSCALE`` emulates a Vertical Scale knob turn.
            - ``ZOOM`` emulates a Zoom knob turn.
            - ``<NR1>`` is the number of clicks to turn the knob.
        """  # noqa: E501
        return self._turn
