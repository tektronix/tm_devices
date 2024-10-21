# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The digio commands module.

These commands are used in the following models:
SMU2601B_Pulse

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    BaseTSPCmd,
    DefaultDictPassKeyToFactory,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


# pylint: disable=too-few-public-methods
class DigioTriggerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``digio.trigger[N]`` command tree.

    Constants:
        - ``.EVENT_ID``: Selects the event that causes a trigger to be asserted on the digital
          output line as the edge detected on the specified digital I/O line.
    """

    EVENT_ID = "digio.trigger[N].EVENT_ID"
    """str: Selects the event that causes a trigger to be asserted on the digital output line as the edge detected on the specified digital I/O line."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )


class Digio(BaseTSPCmd):
    """The ``digio`` command tree.

    Constants:
        - ``.TRIG_BYPASS``: Sets the mode in which the trigger event detector and the output trigger
          generator operate on the specified trigger line to allow direct control of the line.
        - ``.TRIG_EITHER``: Sets the mode in which the trigger event detector and the output trigger
          generator operate on the specified trigger line to detect rising- or falling-edge triggers
          as input and assert a TTL-low pulse for output.
        - ``.TRIG_FALLING``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect falling-edge triggers as
          input and assert a TTL-low pulse for output.
        - ``.TRIG_RISING``: Sets the mode in which the trigger event detector and the output trigger
          generator operate on the specified trigger line so that if the programmed state of the
          line is high, the digio.TRIG_RISING mode behavior is similar to digio.TRIG_RISINGA. If the
          programmed state of the line is low, the digio.TRIG_RISING mode behavior is similar to
          digio.TRIG_RISINGM. Only use this setting if necessary for compatibility with other
          Keithley Instruments products.
        - ``.TRIG_RISINGA``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect rising-edge triggers as
          input and assert a TTL-low pulse for output.
        - ``.TRIG_RISINGM``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to assert a TTL-high pulse for
          output. Input edge detection is not possible in this mode.
        - ``.TRIG_SYNCHRONOUS``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect the falling-edge input
          triggers and automatically latch and drive the trigger line low. Asserts a TTL-low pulse
          as an output trigger.
        - ``.TRIG_SYNCHRONOUSA``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect the falling-edge input
          triggers and automatically latch and drive the trigger line low. Asserting the output
          trigger releases the latched line.
        - ``.TRIG_SYNCHRONOUSM``: Sets the mode in which the trigger event detector and the output
          trigger generator operate on the specified trigger line to detect rising-edge triggers as
          input and assert a TTL-low pulse for output.

    Properties and methods:
        - ``.trigger``: The ``digio.trigger[N]`` command tree.
    """

    TRIG_BYPASS = "digio.TRIG_BYPASS"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to allow direct control of the line."""  # noqa: E501
    TRIG_EITHER = "digio.TRIG_EITHER"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect rising- or falling-edge triggers as input and assert a TTL-low pulse for output."""  # noqa: E501
    TRIG_FALLING = "digio.TRIG_FALLING"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect falling-edge triggers as input and assert a TTL-low pulse for output."""  # noqa: E501
    TRIG_RISING = "digio.TRIG_RISING"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line so that if the programmed state of the line is high, the digio.TRIG_RISING mode behavior is similar to digio.TRIG_RISINGA. If the programmed state of the line is low, the digio.TRIG_RISING mode behavior is similar to digio.TRIG_RISINGM. Only use this setting if necessary for compatibility with other Keithley Instruments products."""  # noqa: E501
    TRIG_RISINGA = "digio.TRIG_RISINGA"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect rising-edge triggers as input and assert a TTL-low pulse for output."""  # noqa: E501
    TRIG_RISINGM = "digio.TRIG_RISINGM"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to assert a TTL-high pulse for output. Input edge detection is not possible in this mode."""  # noqa: E501
    TRIG_SYNCHRONOUS = "digio.TRIG_SYNCHRONOUS"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect the falling-edge input triggers and automatically latch and drive the trigger line low. Asserts a TTL-low pulse as an output trigger."""  # noqa: E501
    TRIG_SYNCHRONOUSA = "digio.TRIG_SYNCHRONOUSA"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect the falling-edge input triggers and automatically latch and drive the trigger line low. Asserting the output trigger releases the latched line."""  # noqa: E501
    TRIG_SYNCHRONOUSM = "digio.TRIG_SYNCHRONOUSM"
    """str: Sets the mode in which the trigger event detector and the output trigger generator operate on the specified trigger line to detect rising-edge triggers as input and assert a TTL-low pulse for output."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "digio") -> None:
        super().__init__(device, cmd_syntax)
        self._trigger: Dict[int, DigioTriggerItem] = DefaultDictPassKeyToFactory(
            lambda x: DigioTriggerItem(device, f"{self._cmd_syntax}.trigger[{x}]")
        )

    @property
    def trigger(self) -> Dict[int, DigioTriggerItem]:
        """Return the ``digio.trigger[N]`` command tree.

        Constants:
            - ``.EVENT_ID``: Selects the event that causes a trigger to be asserted on the digital
              output line as the edge detected on the specified digital I/O line.
        """
        return self._trigger
