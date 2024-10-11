"""The mapping for all device drivers."""

from types import MappingProxyType
from typing import Mapping, Type

from tm_devices.drivers.api.rest_api.margin_testers.tmt4 import TMT4
from tm_devices.drivers.device import Device
from tm_devices.drivers.pi.data_acquisition_systems.daq6510 import DAQ6510
from tm_devices.drivers.pi.digital_multimeters.dmm75xx.dmm7510 import DMM7510
from tm_devices.drivers.pi.digital_multimeters.dmm75xx.dmm7512 import DMM7512
from tm_devices.drivers.pi.digital_multimeters.dmm6500 import DMM6500
from tm_devices.drivers.pi.power_supplies.psu2200.psu2200 import PSU2200
from tm_devices.drivers.pi.power_supplies.psu2200.psu2220 import PSU2220
from tm_devices.drivers.pi.power_supplies.psu2200.psu2230 import PSU2230
from tm_devices.drivers.pi.power_supplies.psu2200.psu2231 import PSU2231
from tm_devices.drivers.pi.power_supplies.psu2200.psu2231a import PSU2231A
from tm_devices.drivers.pi.power_supplies.psu2200.psu2280 import PSU2280
from tm_devices.drivers.pi.power_supplies.psu2200.psu2281 import PSU2281
from tm_devices.drivers.pi.scopes.tekscope.lpd6 import LPD6
from tm_devices.drivers.pi.scopes.tekscope.mso2 import MSO2
from tm_devices.drivers.pi.scopes.tekscope.mso4 import MSO4
from tm_devices.drivers.pi.scopes.tekscope.mso4b import MSO4B
from tm_devices.drivers.pi.scopes.tekscope.mso5 import MSO5
from tm_devices.drivers.pi.scopes.tekscope.mso5b import MSO5B
from tm_devices.drivers.pi.scopes.tekscope.mso5lp import MSO5LP
from tm_devices.drivers.pi.scopes.tekscope.mso6 import MSO6
from tm_devices.drivers.pi.scopes.tekscope.mso6b import MSO6B
from tm_devices.drivers.pi.scopes.tekscope.tekscopesw import TekScopePC
from tm_devices.drivers.pi.scopes.tekscope_2k.dpo2k import DPO2K
from tm_devices.drivers.pi.scopes.tekscope_2k.dpo2kb import DPO2KB
from tm_devices.drivers.pi.scopes.tekscope_2k.mso2k import MSO2K
from tm_devices.drivers.pi.scopes.tekscope_2k.mso2kb import MSO2KB
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.dpo4k import DPO4K
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.dpo4kb import DPO4KB
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.mdo3 import MDO3
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.mdo3k import MDO3K
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.mdo4k import MDO4K
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.mdo4kb import MDO4KB
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.mdo4kc import MDO4KC
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.mso4k import MSO4K
from tm_devices.drivers.pi.scopes.tekscope_3k_4k.mso4kb import MSO4KB
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo5k import DPO5K
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo5kb import DPO5KB
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo7k import DPO7K
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo7kc import DPO7KC
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo70k import DPO70K
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo70kc import DPO70KC
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo70kd import DPO70KD
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo70kdx import DPO70KDX
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dpo70ksx import DPO70KSX
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dsa70k import DSA70K
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dsa70kc import DSA70KC
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.dsa70kd import DSA70KD
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.mso5k import MSO5K
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.mso5kb import MSO5KB
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.mso70k import MSO70K
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.mso70kc import MSO70KC
from tm_devices.drivers.pi.scopes.tekscope_5k_7k_70k.mso70kdx import MSO70KDX
from tm_devices.drivers.pi.scopes.tso.tsovu import TSOVu
from tm_devices.drivers.pi.signal_generators.afgs.afg3k import AFG3K
from tm_devices.drivers.pi.signal_generators.afgs.afg3kb import AFG3KB
from tm_devices.drivers.pi.signal_generators.afgs.afg3kc import AFG3KC
from tm_devices.drivers.pi.signal_generators.afgs.afg31k import AFG31K
from tm_devices.drivers.pi.signal_generators.awgs.awg5k import AWG5K
from tm_devices.drivers.pi.signal_generators.awgs.awg5kb import AWG5KB
from tm_devices.drivers.pi.signal_generators.awgs.awg5kc import AWG5KC
from tm_devices.drivers.pi.signal_generators.awgs.awg7k import AWG7K
from tm_devices.drivers.pi.signal_generators.awgs.awg7kb import AWG7KB
from tm_devices.drivers.pi.signal_generators.awgs.awg7kc import AWG7KC
from tm_devices.drivers.pi.signal_generators.awgs.awg70ka import AWG70KA
from tm_devices.drivers.pi.signal_generators.awgs.awg70kb import AWG70KB
from tm_devices.drivers.pi.signal_generators.awgs.awg5200 import AWG5200
from tm_devices.drivers.pi.source_measure_units.smu24xx.smu2400 import SMU2400
from tm_devices.drivers.pi.source_measure_units.smu24xx.smu2401 import SMU2401
from tm_devices.drivers.pi.source_measure_units.smu24xx.smu2410 import SMU2410
from tm_devices.drivers.pi.source_measure_units.smu24xx.smu2450 import SMU2450
from tm_devices.drivers.pi.source_measure_units.smu24xx.smu2460 import SMU2460
from tm_devices.drivers.pi.source_measure_units.smu24xx.smu2461 import SMU2461
from tm_devices.drivers.pi.source_measure_units.smu24xx.smu2470 import SMU2470
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2601a import SMU2601A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2601b import SMU2601B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2601b_pulse import SMU2601BPulse
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2602a import SMU2602A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2602b import SMU2602B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2604a import SMU2604A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2604b import SMU2604B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2606b import SMU2606B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2611a import SMU2611A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2611b import SMU2611B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2612a import SMU2612A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2612b import SMU2612B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2614a import SMU2614A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2614b import SMU2614B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2634a import SMU2634A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2634b import SMU2634B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2635a import SMU2635A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2635b import SMU2635B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2636a import SMU2636A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2636b import SMU2636B
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2651a import SMU2651A
from tm_devices.drivers.pi.source_measure_units.smu26xx.smu2657a import SMU2657A
from tm_devices.drivers.pi.source_measure_units.smu60xx.smu6430 import SMU6430
from tm_devices.drivers.pi.source_measure_units.smu60xx.smu6514 import SMU6514
from tm_devices.drivers.pi.source_measure_units.smu60xx.smu6517b import SMU6517B
from tm_devices.drivers.pi.systems_switches.ss3706a import SS3706A
from tm_devices.helpers.enums import SupportedModels

# IMPORTANT: Any additions to this class which support a USBTMC connection need to be added to the
# tm_devices.helpers.constants_and_dataclasses.USB_MODEL_ID_LOOKUP constant as well.
DEVICE_DRIVER_MODEL_MAPPING: Mapping[SupportedModels, Type[Device]] = MappingProxyType(
    {
        # AFGs
        SupportedModels.AFG3K: AFG3K,
        SupportedModels.AFG3KB: AFG3KB,
        SupportedModels.AFG3KC: AFG3KC,
        SupportedModels.AFG31K: AFG31K,
        # AWGs
        SupportedModels.AWG5200: AWG5200,
        SupportedModels.AWG5K: AWG5K,
        SupportedModels.AWG5KB: AWG5KB,
        SupportedModels.AWG5KC: AWG5KC,
        SupportedModels.AWG7K: AWG7K,
        SupportedModels.AWG7KB: AWG7KB,
        SupportedModels.AWG7KC: AWG7KC,
        SupportedModels.AWG70KA: AWG70KA,
        SupportedModels.AWG70KB: AWG70KB,
        # Scopes
        SupportedModels.DPO5K: DPO5K,
        SupportedModels.DPO5KB: DPO5KB,
        SupportedModels.DPO7K: DPO7K,
        SupportedModels.DPO7KC: DPO7KC,
        SupportedModels.DPO70K: DPO70K,
        SupportedModels.DPO70KC: DPO70KC,
        SupportedModels.DPO70KD: DPO70KD,
        SupportedModels.DPO70KDX: DPO70KDX,
        SupportedModels.DPO70KSX: DPO70KSX,
        SupportedModels.DSA70K: DSA70K,
        SupportedModels.DSA70KC: DSA70KC,
        SupportedModels.DSA70KD: DSA70KD,
        SupportedModels.LPD6: LPD6,
        SupportedModels.MSO2K: MSO2K,
        SupportedModels.MSO2KB: MSO2KB,
        SupportedModels.DPO2K: DPO2K,
        SupportedModels.DPO2KB: DPO2KB,
        SupportedModels.MDO3: MDO3,
        SupportedModels.MDO3K: MDO3K,
        SupportedModels.MDO4K: MDO4K,
        SupportedModels.MDO4KB: MDO4KB,
        SupportedModels.MDO4KC: MDO4KC,
        SupportedModels.MSO4K: MSO4K,
        SupportedModels.MSO4KB: MSO4KB,
        SupportedModels.DPO4K: DPO4K,
        SupportedModels.DPO4KB: DPO4KB,
        SupportedModels.MSO2: MSO2,
        SupportedModels.MSO4: MSO4,
        SupportedModels.MSO4B: MSO4B,
        SupportedModels.MSO5: MSO5,
        SupportedModels.MSO5B: MSO5B,
        SupportedModels.MSO5LP: MSO5LP,
        SupportedModels.MSO6: MSO6,
        SupportedModels.MSO6B: MSO6B,
        SupportedModels.MSO5K: MSO5K,
        SupportedModels.MSO5KB: MSO5KB,
        SupportedModels.MSO70K: MSO70K,
        SupportedModels.MSO70KC: MSO70KC,
        SupportedModels.MSO70KDX: MSO70KDX,
        SupportedModels.TEKSCOPEPC: TekScopePC,
        SupportedModels.TSOVU: TSOVu,
        # Margin Testers
        SupportedModels.TMT4: TMT4,
        # Source Measure Units
        SupportedModels.SMU2400: SMU2400,
        SupportedModels.SMU2401: SMU2401,
        SupportedModels.SMU2410: SMU2410,
        SupportedModels.SMU2450: SMU2450,
        SupportedModels.SMU2460: SMU2460,
        SupportedModels.SMU2461: SMU2461,
        SupportedModels.SMU2470: SMU2470,
        SupportedModels.SMU2601B: SMU2601B,
        SupportedModels.SMU2601B_PULSE: SMU2601BPulse,
        SupportedModels.SMU2602B: SMU2602B,
        SupportedModels.SMU2604B: SMU2604B,
        SupportedModels.SMU2606B: SMU2606B,
        SupportedModels.SMU2611B: SMU2611B,
        SupportedModels.SMU2612B: SMU2612B,
        SupportedModels.SMU2614B: SMU2614B,
        SupportedModels.SMU2634B: SMU2634B,
        SupportedModels.SMU2635B: SMU2635B,
        SupportedModels.SMU2636B: SMU2636B,
        SupportedModels.SMU2651A: SMU2651A,
        SupportedModels.SMU2657A: SMU2657A,
        SupportedModels.SMU2601A: SMU2601A,
        SupportedModels.SMU2602A: SMU2602A,
        SupportedModels.SMU2604A: SMU2604A,
        SupportedModels.SMU2611A: SMU2611A,
        SupportedModels.SMU2612A: SMU2612A,
        SupportedModels.SMU2614A: SMU2614A,
        SupportedModels.SMU2634A: SMU2634A,
        SupportedModels.SMU2635A: SMU2635A,
        SupportedModels.SMU2636A: SMU2636A,
        SupportedModels.SMU6430: SMU6430,
        SupportedModels.SMU6514: SMU6514,
        SupportedModels.SMU6517B: SMU6517B,
        # Power Supplies
        SupportedModels.PSU2200: PSU2200,
        SupportedModels.PSU2220: PSU2220,
        SupportedModels.PSU2230: PSU2230,
        SupportedModels.PSU2231: PSU2231,
        SupportedModels.PSU2231A: PSU2231A,
        SupportedModels.PSU2280: PSU2280,
        SupportedModels.PSU2281: PSU2281,
        # Digital Multimeters
        SupportedModels.DMM6500: DMM6500,
        SupportedModels.DMM7510: DMM7510,
        SupportedModels.DMM7512: DMM7512,
        # Data Acquisition System
        SupportedModels.DAQ6510: DAQ6510,
        # Systems Switches
        SupportedModels.SS3706A: SS3706A,
    }
)
"""A mapping of device model series names to their device driver objects.

Any additions to this class which support a USBTMC connection need to be added to
the [`tm_devices.helpers.constants_and_dataclasses.USB_MODEL_ID_LOOKUP`][] constant as well.

!!! danger "Deprecated"
    This mapping is deprecated since it is only used internally by the
    [`DeviceManager`][tm_devices.DeviceManager].
"""

####################################################################################################
# Private Attributes
####################################################################################################
# TODO: deprecation: Move the contents of DEVICE_DRIVER_MODEL_MAPPING into this attribute,
#  remove the old DEVICE_DRIVER_MODEL_MAPPING constant, and make this entire module (file) private
#  in the next major release
_DEVICE_DRIVER_MODEL_STR_MAPPING: "Mapping[str, Type[Device]]" = MappingProxyType(
    {key.value: value for key, value in DEVICE_DRIVER_MODEL_MAPPING.items()}
)
