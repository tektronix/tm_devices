"""The application commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - APPLication:LICENSE:SLOT<x>:LOCation?
    - APPLication:LICENSE:SLOT<x>:TRANSFER EXECute
    - APPLication:LICENSE:SLOT<x>:TYPe?
    - APPLication:TYPe {POWer|LIMITMask|VIDPic|ACTONEVent|NONe}
    - APPLication:TYPe?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ApplicationType(SCPICmdWrite, SCPICmdRead):
    """The ``APPLication:TYPe`` command.

    Description:
        - This command sets or returns the application type. The query form will return NONe if none
          of the supported test application modules are installed. Attempting to set the application
          type to a type with no application option installed will result in a settings conflict
          error event.

    Usage:
        - Using the ``.query()`` method will send the ``APPLication:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``APPLication:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``APPLication:TYPe value`` command.

    SCPI Syntax:
        ```
        - APPLication:TYPe {POWer|LIMITMask|VIDPic|ACTONEVent|NONe}
        - APPLication:TYPe?
        ```

    Info:
        - ``POWer`` sets the application type to power analysis.
        - ``LIMITMask`` sets the application type to limit mask test.
        - ``VIDPic`` sets the application type to video picture.
        - ``ACTONEVent`` sets the application type to act on event.
        - ``NONe``
    """


class ApplicationLicenseSlotItemType(SCPICmdRead):
    """The ``APPLication:LICENSE:SLOT<x>:TYPe`` command.

    Description:
        - This query returns the application license type of the option that is currently inserted
          in the specified application option slot. If there is no application option in the slot,
          NONE is returned. < x> can be slot number 1-4 (or 1-2 for 3 Series MDO models).

    Usage:
        - Using the ``.query()`` method will send the ``APPLication:LICENSE:SLOT<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``APPLication:LICENSE:SLOT<x>:TYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - APPLication:LICENSE:SLOT<x>:TYPe?
        ```
    """


class ApplicationLicenseSlotItemTransfer(SCPICmdWrite):
    """The ``APPLication:LICENSE:SLOT<x>:TRANSFER`` command.

    Description:
        - You can use this command to transfer a license from a physical application option to an
          internal memory location within the oscilloscope, and to transfer it back. Once a license
          has been transferred to an internal location, the application that it enables can be used
          without the physical application option being present; the physical application option can
          be removed, thus freeing up a slot. However, the license then needs to be transferred back
          to the physical application option in order to use the license with another instrument.
          After licenses have been transferred, the oscilloscope power must be cycled in order to
          enable/disable the features affected by the option. Applications modules must only be
          installed and removed when the oscilloscope power is off. < x> can be slot number 1-4 (1-2
          for 3 Series MDO models).

    Usage:
        - Using the ``.write(value)`` method will send the
          ``APPLication:LICENSE:SLOT<x>:TRANSFER value`` command.

    SCPI Syntax:
        ```
        - APPLication:LICENSE:SLOT<x>:TRANSFER EXECute
        ```
    """


class ApplicationLicenseSlotItemLocation(SCPICmdRead):
    """The ``APPLication:LICENSE:SLOT<x>:LOCation`` command.

    Description:
        - This query returns the license location. < x> can be slot number 1-4 (1-2 for 3 Series MDO
          models).

    Usage:
        - Using the ``.query()`` method will send the ``APPLication:LICENSE:SLOT<x>:LOCation?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``APPLication:LICENSE:SLOT<x>:LOCation?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - APPLication:LICENSE:SLOT<x>:LOCation?
        ```
    """


class ApplicationLicenseSlotItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``APPLication:LICENSE:SLOT<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``APPLication:LICENSE:SLOT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``APPLication:LICENSE:SLOT<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.location``: The ``APPLication:LICENSE:SLOT<x>:LOCation`` command.
        - ``.transfer``: The ``APPLication:LICENSE:SLOT<x>:TRANSFER`` command.
        - ``.type``: The ``APPLication:LICENSE:SLOT<x>:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._location = ApplicationLicenseSlotItemLocation(device, f"{self._cmd_syntax}:LOCation")
        self._transfer = ApplicationLicenseSlotItemTransfer(device, f"{self._cmd_syntax}:TRANSFER")
        self._type = ApplicationLicenseSlotItemType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def location(self) -> ApplicationLicenseSlotItemLocation:
        """Return the ``APPLication:LICENSE:SLOT<x>:LOCation`` command.

        Description:
            - This query returns the license location. < x> can be slot number 1-4 (1-2 for 3 Series
              MDO models).

        Usage:
            - Using the ``.query()`` method will send the ``APPLication:LICENSE:SLOT<x>:LOCation?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``APPLication:LICENSE:SLOT<x>:LOCation?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - APPLication:LICENSE:SLOT<x>:LOCation?
            ```
        """
        return self._location

    @property
    def transfer(self) -> ApplicationLicenseSlotItemTransfer:
        """Return the ``APPLication:LICENSE:SLOT<x>:TRANSFER`` command.

        Description:
            - You can use this command to transfer a license from a physical application option to
              an internal memory location within the oscilloscope, and to transfer it back. Once a
              license has been transferred to an internal location, the application that it enables
              can be used without the physical application option being present; the physical
              application option can be removed, thus freeing up a slot. However, the license then
              needs to be transferred back to the physical application option in order to use the
              license with another instrument. After licenses have been transferred, the
              oscilloscope power must be cycled in order to enable/disable the features affected by
              the option. Applications modules must only be installed and removed when the
              oscilloscope power is off. < x> can be slot number 1-4 (1-2 for 3 Series MDO models).

        Usage:
            - Using the ``.write(value)`` method will send the
              ``APPLication:LICENSE:SLOT<x>:TRANSFER value`` command.

        SCPI Syntax:
            ```
            - APPLication:LICENSE:SLOT<x>:TRANSFER EXECute
            ```
        """
        return self._transfer

    @property
    def type(self) -> ApplicationLicenseSlotItemType:
        """Return the ``APPLication:LICENSE:SLOT<x>:TYPe`` command.

        Description:
            - This query returns the application license type of the option that is currently
              inserted in the specified application option slot. If there is no application option
              in the slot, NONE is returned. < x> can be slot number 1-4 (or 1-2 for 3 Series MDO
              models).

        Usage:
            - Using the ``.query()`` method will send the ``APPLication:LICENSE:SLOT<x>:TYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``APPLication:LICENSE:SLOT<x>:TYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - APPLication:LICENSE:SLOT<x>:TYPe?
            ```
        """
        return self._type


class ApplicationLicense(SCPICmdRead):
    """The ``APPLication:LICENSE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``APPLication:LICENSE?`` query.
        - Using the ``.verify(value)`` method will send the ``APPLication:LICENSE?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.slot``: The ``APPLication:LICENSE:SLOT<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._slot: Dict[int, ApplicationLicenseSlotItem] = DefaultDictPassKeyToFactory(
            lambda x: ApplicationLicenseSlotItem(device, f"{self._cmd_syntax}:SLOT{x}")
        )

    @property
    def slot(self) -> Dict[int, ApplicationLicenseSlotItem]:
        """Return the ``APPLication:LICENSE:SLOT<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``APPLication:LICENSE:SLOT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``APPLication:LICENSE:SLOT<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.location``: The ``APPLication:LICENSE:SLOT<x>:LOCation`` command.
            - ``.transfer``: The ``APPLication:LICENSE:SLOT<x>:TRANSFER`` command.
            - ``.type``: The ``APPLication:LICENSE:SLOT<x>:TYPe`` command.
        """
        return self._slot


class Application(SCPICmdRead):
    """The ``APPLication`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``APPLication?`` query.
        - Using the ``.verify(value)`` method will send the ``APPLication?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.license``: The ``APPLication:LICENSE`` command tree.
        - ``.type``: The ``APPLication:TYPe`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "APPLication"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._license = ApplicationLicense(device, f"{self._cmd_syntax}:LICENSE")
        self._type = ApplicationType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def license(self) -> ApplicationLicense:
        """Return the ``APPLication:LICENSE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``APPLication:LICENSE?`` query.
            - Using the ``.verify(value)`` method will send the ``APPLication:LICENSE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.slot``: The ``APPLication:LICENSE:SLOT<x>`` command tree.
        """
        return self._license

    @property
    def type(self) -> ApplicationType:
        """Return the ``APPLication:TYPe`` command.

        Description:
            - This command sets or returns the application type. The query form will return NONe if
              none of the supported test application modules are installed. Attempting to set the
              application type to a type with no application option installed will result in a
              settings conflict error event.

        Usage:
            - Using the ``.query()`` method will send the ``APPLication:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``APPLication:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``APPLication:TYPe value`` command.

        SCPI Syntax:
            ```
            - APPLication:TYPe {POWer|LIMITMask|VIDPic|ACTONEVent|NONe}
            - APPLication:TYPe?
            ```

        Info:
            - ``POWer`` sets the application type to power analysis.
            - ``LIMITMask`` sets the application type to limit mask test.
            - ``VIDPic`` sets the application type to video picture.
            - ``ACTONEVent`` sets the application type to act on event.
            - ``NONe``
        """
        return self._type
