"""The mapping for all device drivers."""

from types import MappingProxyType
from typing import Mapping, Type, TYPE_CHECKING

from tm_devices.drivers.afgs.afg3k import AFG3K
from tm_devices.drivers.afgs.afg3kb import AFG3KB
from tm_devices.drivers.afgs.afg3kc import AFG3KC
from tm_devices.drivers.afgs.afg31k import AFG31K
from tm_devices.drivers.awgs.awg5k import AWG5K
from tm_devices.drivers.awgs.awg5kb import AWG5KB
from tm_devices.drivers.awgs.awg5kc import AWG5KC
from tm_devices.drivers.awgs.awg7k import AWG7K
from tm_devices.drivers.awgs.awg7kb import AWG7KB
from tm_devices.drivers.awgs.awg7kc import AWG7KC
from tm_devices.drivers.awgs.awg70ka import AWG70KA
from tm_devices.drivers.awgs.awg70kb import AWG70KB
from tm_devices.drivers.awgs.awg5200 import AWG5200
from tm_devices.drivers.data_acquisition_systems.daq6510 import DAQ6510
from tm_devices.drivers.digital_multimeters.dmm75xx.dmm7510 import DMM7510
from tm_devices.drivers.digital_multimeters.dmm75xx.dmm7512 import DMM7512
from tm_devices.drivers.digital_multimeters.dmm6500 import DMM6500
from tm_devices.drivers.margin_testers.tmt4 import TMT4
from tm_devices.drivers.power_supplies.psu22xx.psu2200 import PSU2200
from tm_devices.drivers.power_supplies.psu22xx.psu2220 import PSU2220
from tm_devices.drivers.power_supplies.psu22xx.psu2230 import PSU2230
from tm_devices.drivers.power_supplies.psu22xx.psu2231 import PSU2231
from tm_devices.drivers.power_supplies.psu22xx.psu2231a import PSU2231A
from tm_devices.drivers.power_supplies.psu22xx.psu2280 import PSU2280
from tm_devices.drivers.power_supplies.psu22xx.psu2281 import PSU2281
from tm_devices.drivers.scopes.tekscope.lpd6 import LPD6
from tm_devices.drivers.scopes.tekscope.mso2 import MSO2
from tm_devices.drivers.scopes.tekscope.mso4 import MSO4
from tm_devices.drivers.scopes.tekscope.mso4b import MSO4B
from tm_devices.drivers.scopes.tekscope.mso5 import MSO5
from tm_devices.drivers.scopes.tekscope.mso5b import MSO5B
from tm_devices.drivers.scopes.tekscope.mso5lp import MSO5LP
from tm_devices.drivers.scopes.tekscope.mso6 import MSO6
from tm_devices.drivers.scopes.tekscope.mso6b import MSO6B
from tm_devices.drivers.scopes.tekscope.tekscopepc import TekScopePC
from tm_devices.drivers.scopes.tekscope_2k.dpo2k import DPO2K
from tm_devices.drivers.scopes.tekscope_2k.dpo2kb import DPO2KB
from tm_devices.drivers.scopes.tekscope_2k.mso2k import MSO2K
from tm_devices.drivers.scopes.tekscope_2k.mso2kb import MSO2KB
from tm_devices.drivers.scopes.tekscope_3k_4k.dpo4k import DPO4K
from tm_devices.drivers.scopes.tekscope_3k_4k.dpo4kb import DPO4KB
from tm_devices.drivers.scopes.tekscope_3k_4k.mdo3 import MDO3
from tm_devices.drivers.scopes.tekscope_3k_4k.mdo3k import MDO3K
from tm_devices.drivers.scopes.tekscope_3k_4k.mdo4k import MDO4K
from tm_devices.drivers.scopes.tekscope_3k_4k.mdo4kb import MDO4KB
from tm_devices.drivers.scopes.tekscope_3k_4k.mdo4kc import MDO4KC
from tm_devices.drivers.scopes.tekscope_3k_4k.mso4k import MSO4K
from tm_devices.drivers.scopes.tekscope_3k_4k.mso4kb import MSO4KB
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo5k import DPO5K
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo5kb import DPO5KB
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo7k import DPO7K
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo7kc import DPO7KC
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70k import DPO70K
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70kc import DPO70KC
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70kd import DPO70KD
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70kdx import DPO70KDX
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dpo70ksx import DPO70KSX
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dsa70k import DSA70K
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dsa70kc import DSA70KC
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.dsa70kd import DSA70KD
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.mso5k import MSO5K
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.mso5kb import MSO5KB
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.mso70k import MSO70K
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.mso70kc import MSO70KC
from tm_devices.drivers.scopes.tekscope_5k_7k_70k.mso70kdx import MSO70KDX
from tm_devices.drivers.scopes.tso.tsovu import TSOVu
from tm_devices.drivers.source_measure_units.smu24xx.smu2400 import SMU2400
from tm_devices.drivers.source_measure_units.smu24xx.smu2401 import SMU2401
from tm_devices.drivers.source_measure_units.smu24xx.smu2410 import SMU2410
from tm_devices.drivers.source_measure_units.smu24xx.smu2450 import SMU2450
from tm_devices.drivers.source_measure_units.smu24xx.smu2460 import SMU2460
from tm_devices.drivers.source_measure_units.smu24xx.smu2461 import SMU2461
from tm_devices.drivers.source_measure_units.smu24xx.smu2470 import SMU2470
from tm_devices.drivers.source_measure_units.smu26xx.smu2601a import SMU2601A
from tm_devices.drivers.source_measure_units.smu26xx.smu2601b import SMU2601B
from tm_devices.drivers.source_measure_units.smu26xx.smu2601b_pulse import SMU2601BPulse
from tm_devices.drivers.source_measure_units.smu26xx.smu2602a import SMU2602A
from tm_devices.drivers.source_measure_units.smu26xx.smu2602b import SMU2602B
from tm_devices.drivers.source_measure_units.smu26xx.smu2604a import SMU2604A
from tm_devices.drivers.source_measure_units.smu26xx.smu2604b import SMU2604B
from tm_devices.drivers.source_measure_units.smu26xx.smu2606b import SMU2606B
from tm_devices.drivers.source_measure_units.smu26xx.smu2611a import SMU2611A
from tm_devices.drivers.source_measure_units.smu26xx.smu2611b import SMU2611B
from tm_devices.drivers.source_measure_units.smu26xx.smu2612a import SMU2612A
from tm_devices.drivers.source_measure_units.smu26xx.smu2612b import SMU2612B
from tm_devices.drivers.source_measure_units.smu26xx.smu2614a import SMU2614A
from tm_devices.drivers.source_measure_units.smu26xx.smu2614b import SMU2614B
from tm_devices.drivers.source_measure_units.smu26xx.smu2634a import SMU2634A
from tm_devices.drivers.source_measure_units.smu26xx.smu2634b import SMU2634B
from tm_devices.drivers.source_measure_units.smu26xx.smu2635a import SMU2635A
from tm_devices.drivers.source_measure_units.smu26xx.smu2635b import SMU2635B
from tm_devices.drivers.source_measure_units.smu26xx.smu2636a import SMU2636A
from tm_devices.drivers.source_measure_units.smu26xx.smu2636b import SMU2636B
from tm_devices.drivers.source_measure_units.smu26xx.smu2651a import SMU2651A
from tm_devices.drivers.source_measure_units.smu26xx.smu2657a import SMU2657A
from tm_devices.drivers.source_measure_units.smu60xx.smu6430 import SMU6430
from tm_devices.drivers.source_measure_units.smu60xx.smu6514 import SMU6514
from tm_devices.drivers.source_measure_units.smu60xx.smu6517b import SMU6517B
from tm_devices.drivers.systems_switches.ss3706a import SS3706A
from tm_devices.helpers.enums import SupportedModels

if TYPE_CHECKING:
    from tm_devices.drivers.device import Device

####################################################################################################
# Private Attributes
####################################################################################################
_DEVICE_DRIVER_MODEL_STR_MAPPING: "Mapping[str, Type[Device]]" = MappingProxyType(
    {
        # AFGs
        SupportedModels.AFG3K.value: AFG3K,
        SupportedModels.AFG3KB.value: AFG3KB,
        SupportedModels.AFG3KC.value: AFG3KC,
        SupportedModels.AFG31K.value: AFG31K,
        # AWGs
        SupportedModels.AWG5200.value: AWG5200,
        SupportedModels.AWG5K.value: AWG5K,
        SupportedModels.AWG5KB.value: AWG5KB,
        SupportedModels.AWG5KC.value: AWG5KC,
        SupportedModels.AWG7K.value: AWG7K,
        SupportedModels.AWG7KB.value: AWG7KB,
        SupportedModels.AWG7KC.value: AWG7KC,
        SupportedModels.AWG70KA.value: AWG70KA,
        SupportedModels.AWG70KB.value: AWG70KB,
        # Scopes
        SupportedModels.DPO5K.value: DPO5K,
        SupportedModels.DPO5KB.value: DPO5KB,
        SupportedModels.DPO7K.value: DPO7K,
        SupportedModels.DPO7KC.value: DPO7KC,
        SupportedModels.DPO70K.value: DPO70K,
        SupportedModels.DPO70KC.value: DPO70KC,
        SupportedModels.DPO70KD.value: DPO70KD,
        SupportedModels.DPO70KDX.value: DPO70KDX,
        SupportedModels.DPO70KSX.value: DPO70KSX,
        SupportedModels.DSA70K.value: DSA70K,
        SupportedModels.DSA70KC.value: DSA70KC,
        SupportedModels.DSA70KD.value: DSA70KD,
        SupportedModels.LPD6.value: LPD6,
        SupportedModels.MSO2K.value: MSO2K,
        SupportedModels.MSO2KB.value: MSO2KB,
        SupportedModels.DPO2K.value: DPO2K,
        SupportedModels.DPO2KB.value: DPO2KB,
        SupportedModels.MDO3.value: MDO3,
        SupportedModels.MDO3K.value: MDO3K,
        SupportedModels.MDO4K.value: MDO4K,
        SupportedModels.MDO4KB.value: MDO4KB,
        SupportedModels.MDO4KC.value: MDO4KC,
        SupportedModels.MSO4K.value: MSO4K,
        SupportedModels.MSO4KB.value: MSO4KB,
        SupportedModels.DPO4K.value: DPO4K,
        SupportedModels.DPO4KB.value: DPO4KB,
        SupportedModels.MSO2.value: MSO2,
        SupportedModels.MSO4.value: MSO4,
        SupportedModels.MSO4B.value: MSO4B,
        SupportedModels.MSO5.value: MSO5,
        SupportedModels.MSO5B.value: MSO5B,
        SupportedModels.MSO5LP.value: MSO5LP,
        SupportedModels.MSO6.value: MSO6,
        SupportedModels.MSO6B.value: MSO6B,
        SupportedModels.MSO5K.value: MSO5K,
        SupportedModels.MSO5KB.value: MSO5KB,
        SupportedModels.MSO70K.value: MSO70K,
        SupportedModels.MSO70KC.value: MSO70KC,
        SupportedModels.MSO70KDX.value: MSO70KDX,
        SupportedModels.TEKSCOPEPC.value: TekScopePC,
        SupportedModels.TSOVU.value: TSOVu,
        # Margin Testers
        SupportedModels.TMT4.value: TMT4,
        # Source Measure Units
        SupportedModels.SMU2400.value: SMU2400,
        SupportedModels.SMU2401.value: SMU2401,
        SupportedModels.SMU2410.value: SMU2410,
        SupportedModels.SMU2450.value: SMU2450,
        SupportedModels.SMU2460.value: SMU2460,
        SupportedModels.SMU2461.value: SMU2461,
        SupportedModels.SMU2470.value: SMU2470,
        SupportedModels.SMU2601B.value: SMU2601B,
        SupportedModels.SMU2601B_PULSE.value: SMU2601BPulse,
        SupportedModels.SMU2602B.value: SMU2602B,
        SupportedModels.SMU2604B.value: SMU2604B,
        SupportedModels.SMU2606B.value: SMU2606B,
        SupportedModels.SMU2611B.value: SMU2611B,
        SupportedModels.SMU2612B.value: SMU2612B,
        SupportedModels.SMU2614B.value: SMU2614B,
        SupportedModels.SMU2634B.value: SMU2634B,
        SupportedModels.SMU2635B.value: SMU2635B,
        SupportedModels.SMU2636B.value: SMU2636B,
        SupportedModels.SMU2651A.value: SMU2651A,
        SupportedModels.SMU2657A.value: SMU2657A,
        SupportedModels.SMU2601A.value: SMU2601A,
        SupportedModels.SMU2602A.value: SMU2602A,
        SupportedModels.SMU2604A.value: SMU2604A,
        SupportedModels.SMU2611A.value: SMU2611A,
        SupportedModels.SMU2612A.value: SMU2612A,
        SupportedModels.SMU2614A.value: SMU2614A,
        SupportedModels.SMU2634A.value: SMU2634A,
        SupportedModels.SMU2635A.value: SMU2635A,
        SupportedModels.SMU2636A.value: SMU2636A,
        SupportedModels.SMU6430.value: SMU6430,
        SupportedModels.SMU6514.value: SMU6514,
        SupportedModels.SMU6517B.value: SMU6517B,
        # Power Supplies
        SupportedModels.PSU2200.value: PSU2200,
        SupportedModels.PSU2220.value: PSU2220,
        SupportedModels.PSU2230.value: PSU2230,
        SupportedModels.PSU2231.value: PSU2231,
        SupportedModels.PSU2231A.value: PSU2231A,
        SupportedModels.PSU2280.value: PSU2280,
        SupportedModels.PSU2281.value: PSU2281,
        # Digital Multimeters
        SupportedModels.DMM6500.value: DMM6500,
        SupportedModels.DMM7510.value: DMM7510,
        SupportedModels.DMM7512.value: DMM7512,
        # Data Acquisition System
        SupportedModels.DAQ6510.value: DAQ6510,
        # Systems Switches
        SupportedModels.SS3706A.value: SS3706A,
    }
)
