"""The usbdevice commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - USBDevice:CONFigure {DISabled|USBTmc}
    - USBDevice:CONFigure?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class UsbdeviceConfigure(SCPICmdWrite, SCPICmdRead):
    """The ``USBDevice:CONFigure`` command.

    Description:
        - This command may be used to configure the rear USB port to be off or enabled as a USBTMC
          device. Users should be cautious using this command via the USBTMC interface as a change
          to the configuration of this interface from a USBTMC device will cause USBTMC
          communication to cease. It is intended to be used via the Ethernet interface to control
          the USB device interface.

    Usage:
        - Using the ``.query()`` method will send the ``USBDevice:CONFigure?`` query.
        - Using the ``.verify(value)`` method will send the ``USBDevice:CONFigure?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``USBDevice:CONFigure value`` command.

    SCPI Syntax:
        ```
        - USBDevice:CONFigure {DISabled|USBTmc}
        - USBDevice:CONFigure?
        ```

    Info:
        - ``DISabled`` will disable the rear USB port.
        - ``USBTmc`` enables the rear USB port.
    """


class Usbdevice(SCPICmdRead):
    """The ``USBDevice`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``USBDevice?`` query.
        - Using the ``.verify(value)`` method will send the ``USBDevice?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.configure``: The ``USBDevice:CONFigure`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "USBDevice") -> None:
        super().__init__(device, cmd_syntax)
        self._configure = UsbdeviceConfigure(device, f"{self._cmd_syntax}:CONFigure")

    @property
    def configure(self) -> UsbdeviceConfigure:
        """Return the ``USBDevice:CONFigure`` command.

        Description:
            - This command may be used to configure the rear USB port to be off or enabled as a
              USBTMC device. Users should be cautious using this command via the USBTMC interface as
              a change to the configuration of this interface from a USBTMC device will cause USBTMC
              communication to cease. It is intended to be used via the Ethernet interface to
              control the USB device interface.

        Usage:
            - Using the ``.query()`` method will send the ``USBDevice:CONFigure?`` query.
            - Using the ``.verify(value)`` method will send the ``USBDevice:CONFigure?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``USBDevice:CONFigure value``
              command.

        SCPI Syntax:
            ```
            - USBDevice:CONFigure {DISabled|USBTmc}
            - USBDevice:CONFigure?
            ```

        Info:
            - ``DISabled`` will disable the rear USB port.
            - ``USBTmc`` enables the rear USB port.
        """
        return self._configure
