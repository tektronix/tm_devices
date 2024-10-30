"""The opcextended commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - OPCEXtended {ON|OFF|<NR1>}
    - OPCEXtended?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Opcextended(SCPICmdWrite, SCPICmdRead):
    """The ``OPCEXtended`` command.

    Description:
        - This command sets or queries the behavior of OPC commands and queries. When enabled,
          operations referenced in the ``*OPC`` command description notify when their overlapped
          functionality has completed. When disabled, the operations notify as they have in the past
          (only once updated in the instrument state database). Command synchronization Operation PI
          sequence Single sequence with ttOff ``:ACQUIRE:STOPAFTER SEQUENCE``
          ``:ACQUIRE:STATE 1``;``*OPC?``;``:WFMOUTPRE:XZERO?`` Single sequence with Measurement
          Annotation ``:ACQUIRE:STOPAFTER SEQUENCE``;``:MEASUREMENT:MEAS1:STATE 1``;TYPE PK2PK
          ``:ACQUIRE:STATE 1``;``*OPC?``;``:MEASUREMENT:ANNOTATION:X1?`` Single sequence with
          Cursors ``:ACQUIRE:STOPAFTER SEQUENCE``;``:CURSOR:FUNCTION WAVEFORM``;SOURCE CH1;STATE 1
          ``:ACQUIRE:STATE 1``;``*OPC?`` Single sequence with Math
          ``:ACQUIRE:STOPAFTER SEQUENCE``;``:MATH1:DEFINE`` 'Ch1``*Ch2``';``:SELECT:MATH1 1``
          ``:ACQUIRE:STATE 1``;``*OPC?`` Default setup followed by Save Waveform ``*RST``;``*OPC?``
          ``:SAVE:WAVEFORM`` CH1,REF1;``*WAI`` ``:SELECT:REF1 1`` Math On during Acq Run mode
          ``:HORIZONTAL:MODE MANUAL``;RECORDLENGTH 2500000 ``:MATH1:DEFINE``
          'CH1``*CH1``';``:SELECT:MATH1 1`` ``:DATA:ENCDG ASCII``;SOURCE REF1;START 1;STOP 10
          ``:SELECT:MATH1 0`` {Wait a couple sec..longer in release mode?}
          ``:SELECT:MATH1 1``;``*WAI``;``:CURVE?`` Save Math to Ref
          ``:HORIZONTAL:MODE MANUAL``;RECORDLENGTH 2500000 ``:MATH1:DEFINE``
          'CH1``*CH1``';``:SELECT:MATH1 1``;``*WAI``; ``:SAVE:WAVEFORM``
          MATH1,REF1;``:SELECT:REF1 1`` ``:DATA:ENCDG ASCII``;SOURCE REF1;START 1;STOP 10 CURVE?
          Trigger state ``:ACQUIRE:STOPAFTER SEQUENCE``
          ``:ACQUIRE:STATE 1``;``*OPC?``;``:TRIGGER:STATE?`` Single sequence with Measurement
          ``:ACQUIRE:STOPAFTER SEQUENCE``;``:MEASUREMENT:MEAS1:STATE 1``;TYPE AMPLITUDE
          ``:ACQUIRE:STATE 1``;``*OPC?``;``:MEASUREMENT:MEAS1:VALUE?`` Single sequence with
          Measurement on Math
          ``:ACQUIRE:STOPAFTER SEQUENCE``;``:HORIZONTAL:MODE MANUAL``;RECORDLENGTH 2500000
          ``:MATH1:DEFINE`` 'CH1``*CH1``';``:SELECT:MATH1 1`` ``:MEASUREMENT:MEAS1:STATE 1``;TYPE
          AMPLITUDE;SOURCE MATH1 ``:ACQUIRE:STATE 1``;``*OPC?``;``:MEASUREMENT:MEAS1:VALUE?`` Acq
          Count ``*RST``;``*WAI``;``:ACQUIRE:NUMACQ?`` Acq state after single sequence
          ``:ACQUIRE:STOPAFTER SEQUENCE``;STATE 1;``*WAI``;``:ACQUIRE:STATE?``

    Usage:
        - Using the ``.query()`` method will send the ``OPCEXtended?`` query.
        - Using the ``.verify(value)`` method will send the ``OPCEXtended?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OPCEXtended value`` command.

    SCPI Syntax:
        ```
        - OPCEXtended {ON|OFF|<NR1>}
        - OPCEXtended?
        ```

    Info:
        - ``ON`` turns on extended OPC behavior.
        - ``OFF`` turns off extended OPC behavior.
        - ``<NR1>`` = 0 turns off extended OPC behavior; any other value turns on extended OPC
          behavior.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "OPCEXtended"
    ) -> None:
        super().__init__(device, cmd_syntax)
