"""The usbdevice commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - USBDevice:CONFigure {DISabled|IMAge|USBTmc}
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
        - Enables or disables the rear USB port for use with Pictbridge printers.

    Usage:
        - Using the ``.query()`` method will send the ``USBDevice:CONFigure?`` query.
        - Using the ``.verify(value)`` method will send the ``USBDevice:CONFigure?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``USBDevice:CONFigure value`` command.

    SCPI Syntax:
        ```
        - USBDevice:CONFigure {DISabled|IMAge|USBTmc}
        - USBDevice:CONFigure?
        ```

    Info:
        - ``DISabled`` disables the rear USB port.
        - ``IMAge`` enables the rear USB port as an SIC device.
        - ``USBTmc`` enables the rear USB port as a USBTMC device.
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
            - Enables or disables the rear USB port for use with Pictbridge printers.

        Usage:
            - Using the ``.query()`` method will send the ``USBDevice:CONFigure?`` query.
            - Using the ``.verify(value)`` method will send the ``USBDevice:CONFigure?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``USBDevice:CONFigure value``
              command.

        SCPI Syntax:
            ```
            - USBDevice:CONFigure {DISabled|IMAge|USBTmc}
            - USBDevice:CONFigure?
            ```

        Info:
            - ``DISabled`` disables the rear USB port.
            - ``IMAge`` enables the rear USB port as an SIC device.
            - ``USBTmc`` enables the rear USB port as a USBTMC device.
        """
        return self._configure
