"""A module with all the main device type classes."""

from typing import Final, Tuple, Type

from tm_devices.driver_mixins.device_control.device import Device
from tm_devices.drivers.afgs.afg import AFG
from tm_devices.drivers.awgs.awg import AWG
from tm_devices.drivers.data_acquisition_systems.data_acquisition_system import (
    DataAcquisitionSystem,
)
from tm_devices.drivers.digital_multimeters.digital_multimeter import DigitalMultimeter
from tm_devices.drivers.margin_testers.margin_tester import MarginTester
from tm_devices.drivers.power_supplies.power_supply import PowerSupplyUnit
from tm_devices.drivers.scopes.scope import Scope
from tm_devices.drivers.source_measure_units.source_measure_unit import SourceMeasureUnit
from tm_devices.drivers.systems_switches.systems_switch import SystemsSwitch

# TODO: nfelt14: remove this tuple, I don't see a need for it.
DEVICE_TYPE_CLASSES: Final[Tuple[Type[Device], ...]] = (
    AFG,
    AWG,
    DataAcquisitionSystem,
    DigitalMultimeter,
    PowerSupplyUnit,
    SourceMeasureUnit,
    Scope,
    SystemsSwitch,
    MarginTester,
)
"""A tuple containing all the different supported device type classes."""

__all__ = [
    "DEVICE_TYPE_CLASSES",
    "AFG",
    "AWG",
    "DataAcquisitionSystem",
    "DigitalMultimeter",
    "PowerSupplyUnit",
    "SourceMeasureUnit",
    "Scope",
    "SystemsSwitch",
    "MarginTester",
]
