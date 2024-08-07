"""A module with all the main device type classes."""

from typing import Final, Tuple, Type

from tm_devices.drivers.api.rest_api.margin_testers.margin_tester import MarginTester
from tm_devices.drivers.device import Device
from tm_devices.drivers.pi.data_acquisition_systems.data_acquisition_system import (
    DataAcquisitionSystem,
)
from tm_devices.drivers.pi.digital_multimeters.digital_multimeter import DigitalMultimeter
from tm_devices.drivers.pi.power_supplies.power_supply import PowerSupplyUnit
from tm_devices.drivers.pi.scopes.scope import Scope
from tm_devices.drivers.pi.signal_generators.afgs.afg import AFG
from tm_devices.drivers.pi.signal_generators.awgs.awg import AWG
from tm_devices.drivers.pi.source_measure_units.source_measure_unit import SourceMeasureUnit
from tm_devices.drivers.pi.systems_switches.systems_switch import SystemsSwitch

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
