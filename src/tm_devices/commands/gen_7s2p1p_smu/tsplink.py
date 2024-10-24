# pylint: disable=line-too-long
# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The tsplink commands module.

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
class TsplinkTriggerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``tsplink.trigger[N]`` command tree.

    Constants:
        - ``.EVENT_ID``: Selects the event that causes a trigger to be asserted on the digital
          output line as the edge detected on the specified TSP-Link line.
    """

    EVENT_ID = "tsplink.trigger[N].EVENT_ID"
    """str: Selects the event that causes a trigger to be asserted on the digital output line as the edge detected on the specified TSP-Link line."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )


class Tsplink(BaseTSPCmd):
    """The ``tsplink`` command tree.

    Constants:
        - ``.TRIG_BYPASS``: Allows direct control of the line as a digital I/O line.
        - ``.TRIG_EITHER``: Detects rising-edge or falling-edge triggers as input. Asserts a TTL-low
          pulse for output.
        - ``.TRIG_FALLING``: Detects falling-edge triggers as input. Asserts a TTL-low pulse for
          output.
        - ``.TRIG_RISING``: If the programmed state of the line is high, the tsplink.TRIG_RISING
          mode behaves similarly to tsplink.TRIG_RISINGA.
          If the programmed state of the line is low, the tsplink.TRIG_RISING mode behaves similarly to
          tsplink.TRIG_RISINGM.
          Use tsplink.TRIG_RISINGA if the line is in the high output state.
          Use tsplink.TRIG_RISINGM if the line is in the low output state.
        - ``.TRIG_RISINGA``: Detects rising-edge triggers as input. Asserts a TTL-low pulse for
          output.
        - ``.TRIG_RISINGM``: Edge detection as an input is not available. Generates a TTL-high pulse
          as an output trigger.
        - ``.TRIG_SYNCHRONOUS``: Detects the falling-edge input triggers and automatically latches
          and drives the trigger line low. Asserts a TTL-low pulse as an output trigger.
        - ``.TRIG_SYNCHRONOUSA``: Detects the falling-edge input triggers and automatically latches
          and drives the trigger line low.
        - ``.TRIG_SYNCHRONOUSM``: Detects rising-edge triggers as an input. Asserts a TTL-low pulse
          for output.

    Properties and methods:
        - ``.trigger``: The ``tsplink.trigger[N]`` command tree.
    """  # noqa: E501

    TRIG_BYPASS = "tsplink.TRIG_BYPASS"
    """str: Allows direct control of the line as a digital I/O line."""
    TRIG_EITHER = "tsplink.TRIG_EITHER"
    """str: Detects rising-edge or falling-edge triggers as input. Asserts a TTL-low pulse for output."""  # noqa: E501
    TRIG_FALLING = "tsplink.TRIG_FALLING"
    """str: Detects falling-edge triggers as input. Asserts a TTL-low pulse for output."""
    TRIG_RISING = "tsplink.TRIG_RISING"
    """str: If the programmed state of the line is high, the tsplink.TRIG_RISING mode behaves similarly to tsplink.TRIG_RISINGA.
If the programmed state of the line is low, the tsplink.TRIG_RISING mode behaves similarly to tsplink.TRIG_RISINGM.
Use tsplink.TRIG_RISINGA if the line is in the high output state.
Use tsplink.TRIG_RISINGM if the line is in the low output state."""  # noqa: E501
    TRIG_RISINGA = "tsplink.TRIG_RISINGA"
    """str: Detects rising-edge triggers as input. Asserts a TTL-low pulse for output."""
    TRIG_RISINGM = "tsplink.TRIG_RISINGM"
    """str: Edge detection as an input is not available. Generates a TTL-high pulse as an output trigger."""  # noqa: E501
    TRIG_SYNCHRONOUS = "tsplink.TRIG_SYNCHRONOUS"
    """str: Detects the falling-edge input triggers and automatically latches and drives the trigger line low. Asserts a TTL-low pulse as an output trigger."""  # noqa: E501
    TRIG_SYNCHRONOUSA = "tsplink.TRIG_SYNCHRONOUSA"
    """str: Detects the falling-edge input triggers and automatically latches and drives the trigger line low."""  # noqa: E501
    TRIG_SYNCHRONOUSM = "tsplink.TRIG_SYNCHRONOUSM"
    """str: Detects rising-edge triggers as an input. Asserts a TTL-low pulse for output."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "tsplink") -> None:
        super().__init__(device, cmd_syntax)
        self._trigger: Dict[int, TsplinkTriggerItem] = DefaultDictPassKeyToFactory(
            lambda x: TsplinkTriggerItem(device, f"{self._cmd_syntax}.trigger[{x}]")
        )

    @property
    def trigger(self) -> Dict[int, TsplinkTriggerItem]:
        """Return the ``tsplink.trigger[N]`` command tree.

        Constants:
            - ``.EVENT_ID``: Selects the event that causes a trigger to be asserted on the digital
              output line as the edge detected on the specified TSP-Link line.
        """
        return self._trigger
