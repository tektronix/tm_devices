"""The battery commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BATTery:ACPOWer?
    - BATTery:SLOT<1,2>:CHARGE?
    - BATTery:SLOT<1,2>:INSTalled?
    - BATTery:SLOT<1,2>:SERIALnumber?
    - BATTery:SLOT<1,2>:TIMETOEMPty?
    - BATTery:SLOT<1,2>:TIMETOFULL?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import DefaultDictPassKeyToFactory, SCPICmdRead, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class BatterySlotItemTimetofull(SCPICmdRead):
    """The ``BATTery:SLOT<1,2>:TIMETOFULL`` command.

    Description:
        - This command queries the time to full of the battery.

    Usage:
        - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:TIMETOFULL?`` query.
        - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:TIMETOFULL?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BATTery:SLOT<1,2>:TIMETOFULL?
        ```
    """


class BatterySlotItemTimetoempty(SCPICmdRead):
    """The ``BATTery:SLOT<1,2>:TIMETOEMPty`` command.

    Description:
        - This command queries the time to empty of the battery.

    Usage:
        - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:TIMETOEMPty?`` query.
        - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:TIMETOEMPty?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BATTery:SLOT<1,2>:TIMETOEMPty?
        ```
    """


class BatterySlotItemSerialnumber(SCPICmdRead):
    """The ``BATTery:SLOT<1,2>:SERIALnumber`` command.

    Description:
        - This command queries the serial number of the battery.

    Usage:
        - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:SERIALnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:SERIALnumber?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BATTery:SLOT<1,2>:SERIALnumber?
        ```
    """


class BatterySlotItemInstalled(SCPICmdRead):
    """The ``BATTery:SLOT<1,2>:INSTalled`` command.

    Description:
        - This command queries if a battery is installed.

    Usage:
        - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:INSTalled?`` query.
        - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:INSTalled?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BATTery:SLOT<1,2>:INSTalled?
        ```
    """


class BatterySlotItemCharge(SCPICmdRead):
    """The ``BATTery:SLOT<1,2>:CHARGE`` command.

    Description:
        - This command queries the current charge of the battery.

    Usage:
        - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:CHARGE?`` query.
        - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:CHARGE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BATTery:SLOT<1,2>:CHARGE?
        ```
    """


class BatterySlotItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BATTery:SLOT<1,2>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>?`` query.
        - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.charge``: The ``BATTery:SLOT<1,2>:CHARGE`` command.
        - ``.installed``: The ``BATTery:SLOT<1,2>:INSTalled`` command.
        - ``.serialnumber``: The ``BATTery:SLOT<1,2>:SERIALnumber`` command.
        - ``.timetoempty``: The ``BATTery:SLOT<1,2>:TIMETOEMPty`` command.
        - ``.timetofull``: The ``BATTery:SLOT<1,2>:TIMETOFULL`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._charge = BatterySlotItemCharge(device, f"{self._cmd_syntax}:CHARGE")
        self._installed = BatterySlotItemInstalled(device, f"{self._cmd_syntax}:INSTalled")
        self._serialnumber = BatterySlotItemSerialnumber(device, f"{self._cmd_syntax}:SERIALnumber")
        self._timetoempty = BatterySlotItemTimetoempty(device, f"{self._cmd_syntax}:TIMETOEMPty")
        self._timetofull = BatterySlotItemTimetofull(device, f"{self._cmd_syntax}:TIMETOFULL")

    @property
    def charge(self) -> BatterySlotItemCharge:
        """Return the ``BATTery:SLOT<1,2>:CHARGE`` command.

        Description:
            - This command queries the current charge of the battery.

        Usage:
            - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:CHARGE?`` query.
            - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:CHARGE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BATTery:SLOT<1,2>:CHARGE?
            ```
        """
        return self._charge

    @property
    def installed(self) -> BatterySlotItemInstalled:
        """Return the ``BATTery:SLOT<1,2>:INSTalled`` command.

        Description:
            - This command queries if a battery is installed.

        Usage:
            - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:INSTalled?`` query.
            - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:INSTalled?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BATTery:SLOT<1,2>:INSTalled?
            ```
        """
        return self._installed

    @property
    def serialnumber(self) -> BatterySlotItemSerialnumber:
        """Return the ``BATTery:SLOT<1,2>:SERIALnumber`` command.

        Description:
            - This command queries the serial number of the battery.

        Usage:
            - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:SERIALnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:SERIALnumber?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BATTery:SLOT<1,2>:SERIALnumber?
            ```
        """
        return self._serialnumber

    @property
    def timetoempty(self) -> BatterySlotItemTimetoempty:
        """Return the ``BATTery:SLOT<1,2>:TIMETOEMPty`` command.

        Description:
            - This command queries the time to empty of the battery.

        Usage:
            - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:TIMETOEMPty?`` query.
            - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:TIMETOEMPty?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BATTery:SLOT<1,2>:TIMETOEMPty?
            ```
        """
        return self._timetoempty

    @property
    def timetofull(self) -> BatterySlotItemTimetofull:
        """Return the ``BATTery:SLOT<1,2>:TIMETOFULL`` command.

        Description:
            - This command queries the time to full of the battery.

        Usage:
            - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>:TIMETOFULL?`` query.
            - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>:TIMETOFULL?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BATTery:SLOT<1,2>:TIMETOFULL?
            ```
        """
        return self._timetofull


class BatteryAcpower(SCPICmdRead):
    """The ``BATTery:ACPOWer`` command.

    Description:
        - This command queries the state of AC power being plugged in.

    Usage:
        - Using the ``.query()`` method will send the ``BATTery:ACPOWer?`` query.
        - Using the ``.verify(value)`` method will send the ``BATTery:ACPOWer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BATTery:ACPOWer?
        ```
    """


class Battery(SCPICmdRead):
    """The ``BATTery`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BATTery?`` query.
        - Using the ``.verify(value)`` method will send the ``BATTery?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.acpower``: The ``BATTery:ACPOWer`` command.
        - ``.slot``: The ``BATTery:SLOT<1,2>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BATTery") -> None:
        super().__init__(device, cmd_syntax)
        self._acpower = BatteryAcpower(device, f"{self._cmd_syntax}:ACPOWer")
        self._slot: Dict[int, BatterySlotItem] = DefaultDictPassKeyToFactory(
            lambda x: BatterySlotItem(device, f"{self._cmd_syntax}:SLOT{x}")
        )

    @property
    def acpower(self) -> BatteryAcpower:
        """Return the ``BATTery:ACPOWer`` command.

        Description:
            - This command queries the state of AC power being plugged in.

        Usage:
            - Using the ``.query()`` method will send the ``BATTery:ACPOWer?`` query.
            - Using the ``.verify(value)`` method will send the ``BATTery:ACPOWer?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BATTery:ACPOWer?
            ```
        """
        return self._acpower

    @property
    def slot(self) -> Dict[int, BatterySlotItem]:
        """Return the ``BATTery:SLOT<1,2>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BATTery:SLOT<1,2>?`` query.
            - Using the ``.verify(value)`` method will send the ``BATTery:SLOT<1,2>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.charge``: The ``BATTery:SLOT<1,2>:CHARGE`` command.
            - ``.installed``: The ``BATTery:SLOT<1,2>:INSTalled`` command.
            - ``.serialnumber``: The ``BATTery:SLOT<1,2>:SERIALnumber`` command.
            - ``.timetoempty``: The ``BATTery:SLOT<1,2>:TIMETOEMPty`` command.
            - ``.timetofull``: The ``BATTery:SLOT<1,2>:TIMETOFULL`` command.
        """
        return self._slot
