"""The gpibusb commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - GPIBUsb:ADDress?
    - GPIBUsb:HWVersion
    - GPIBUsb:HWVersion?
    - GPIBUsb:ID?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWriteNoArguments

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


class GpibusbHwversion(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``GPIBUsb:HWVersion`` command.

    Description:
        - This command sets or returns the current GPIB hardware version for a connected TEK-USB-488
          adaptor module.

    Usage:
        - Using the ``.query()`` method will send the ``GPIBUsb:HWVersion?`` query.
        - Using the ``.verify(value)`` method will send the ``GPIBUsb:HWVersion?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``GPIBUsb:HWVersion`` command.

    SCPI Syntax:
        ```
        - GPIBUsb:HWVersion
        - GPIBUsb:HWVersion?
        ```
    """


class GpibusbAddress(SCPICmdRead):
    """The ``GPIBUsb:ADDress`` command.

    Description:
        - Returns the current GPIB address setting for a connected TEK-USB-488 adaptor option.

    Usage:
        - Using the ``.query()`` method will send the ``GPIBUsb:ADDress?`` query.
        - Using the ``.verify(value)`` method will send the ``GPIBUsb:ADDress?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - GPIBUsb:ADDress?
        ```
    """


class Gpibusb(SCPICmdRead):
    """The ``GPIBUsb`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``GPIBUsb?`` query.
        - Using the ``.verify(value)`` method will send the ``GPIBUsb?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``GPIBUsb:ADDress`` command.
        - ``.hwversion``: The ``GPIBUsb:HWVersion`` command.
        - ``.id``: The ``GPIBUsb:ID`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "GPIBUsb") -> None:
        super().__init__(device, cmd_syntax)
        self._address = GpibusbAddress(device, f"{self._cmd_syntax}:ADDress")
        self._hwversion = GpibusbHwversion(device, f"{self._cmd_syntax}:HWVersion")
        self._id = GpibusbId(device, f"{self._cmd_syntax}:ID")

    @property
    def address(self) -> GpibusbAddress:
        """Return the ``GPIBUsb:ADDress`` command.

        Description:
            - Returns the current GPIB address setting for a connected TEK-USB-488 adaptor option.

        Usage:
            - Using the ``.query()`` method will send the ``GPIBUsb:ADDress?`` query.
            - Using the ``.verify(value)`` method will send the ``GPIBUsb:ADDress?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - GPIBUsb:ADDress?
            ```
        """
        return self._address

    @property
    def hwversion(self) -> GpibusbHwversion:
        """Return the ``GPIBUsb:HWVersion`` command.

        Description:
            - This command sets or returns the current GPIB hardware version for a connected
              TEK-USB-488 adaptor module.

        Usage:
            - Using the ``.query()`` method will send the ``GPIBUsb:HWVersion?`` query.
            - Using the ``.verify(value)`` method will send the ``GPIBUsb:HWVersion?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``GPIBUsb:HWVersion`` command.

        SCPI Syntax:
            ```
            - GPIBUsb:HWVersion
            - GPIBUsb:HWVersion?
            ```
        """
        return self._hwversion

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
