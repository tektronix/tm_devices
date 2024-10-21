"""The gpibusb commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - GPIBUsb:ID?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class GpibusbId(SCPICmdRead):
    """The ``GPIBUsb:ID`` command.

    Description:
        - Returns the identification string of the connected TEK-USB-488 adaptor option and firmware
          version. If a TEK-USB-488.2 option is not connected, the system returns 'Not detected'.

    Usage:
        - Using the ``.query()`` method will send the ``GPIBUsb:ID?`` query.
        - Using the ``.verify(value)`` method will send the ``GPIBUsb:ID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - GPIBUsb:ID?
        ```
    """


class Gpibusb(SCPICmdRead):
    """The ``GPIBUsb`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``GPIBUsb?`` query.
        - Using the ``.verify(value)`` method will send the ``GPIBUsb?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.id``: The ``GPIBUsb:ID`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "GPIBUsb") -> None:
        super().__init__(device, cmd_syntax)
        self._id = GpibusbId(device, f"{self._cmd_syntax}:ID")

    @property
    def id(self) -> GpibusbId:
        """Return the ``GPIBUsb:ID`` command.

        Description:
            - Returns the identification string of the connected TEK-USB-488 adaptor option and
              firmware version. If a TEK-USB-488.2 option is not connected, the system returns 'Not
              detected'.

        Usage:
            - Using the ``.query()`` method will send the ``GPIBUsb:ID?`` query.
            - Using the ``.verify(value)`` method will send the ``GPIBUsb:ID?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - GPIBUsb:ID?
            ```
        """
        return self._id
