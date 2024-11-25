"""Python drivers for all supported devices."""

# NOTE: For documentation purposes, these imports must be sorted manually, not automatically
# ruff: isort: skip_file
from tm_devices.helpers.enums import SupportedModels
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
from tm_devices.drivers.data_acquisition_systems.daq6510 import DAQ6510
from tm_devices.drivers.digital_multimeters.dmm6500 import DMM6500
from tm_devices.drivers.digital_multimeters.dmm75xx.dmm7510 import DMM7510
from tm_devices.drivers.digital_multimeters.dmm75xx.dmm7512 import DMM7512
from tm_devices.drivers.power_supplies.psu22xx.psu2200 import PSU2200
from tm_devices.drivers.power_supplies.psu22xx.psu2220 import PSU2220
from tm_devices.drivers.power_supplies.psu22xx.psu2230 import PSU2230
from tm_devices.drivers.power_supplies.psu22xx.psu2231 import PSU2231
from tm_devices.drivers.power_supplies.psu22xx.psu2231a import PSU2231A
from tm_devices.drivers.power_supplies.psu22xx.psu2280 import PSU2280
from tm_devices.drivers.power_supplies.psu22xx.psu2281 import PSU2281
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
from tm_devices.drivers.margin_testers.tmt4 import TMT4


__all__ = [
    "AFG3K",
    "AFG3KB",
    "AFG3KC",
    "AFG31K",
    "AWG5K",
    "AWG5KB",
    "AWG5KC",
    "AWG7K",
    "AWG7KB",
    "AWG7KC",
    "AWG70KA",
    "AWG70KB",
    "AWG5200",
    "DAQ6510",
    "DMM6500",
    "DMM7510",
    "DMM7512",
    "DPO2K",
    "DPO2KB",
    "DPO4K",
    "DPO4KB",
    "DPO5K",
    "DPO5KB",
    "DPO7K",
    "DPO7KC",
    "DPO70K",
    "DPO70KC",
    "DPO70KD",
    "DPO70KDX",
    "DPO70KSX",
    "DSA70K",
    "DSA70KC",
    "DSA70KD",
    "LPD6",
    "MDO3",
    "MDO3K",
    "MDO4K",
    "MDO4KB",
    "MDO4KC",
    "MSO2",
    "MSO2K",
    "MSO2KB",
    "MSO4",
    "MSO4B",
    "MSO4K",
    "MSO4KB",
    "MSO5",
    "MSO5B",
    "MSO5K",
    "MSO5KB",
    "MSO5LP",
    "MSO6",
    "MSO6B",
    "MSO70K",
    "MSO70KC",
    "MSO70KDX",
    "PSU2200",
    "PSU2220",
    "PSU2230",
    "PSU2231",
    "PSU2231A",
    "PSU2280",
    "PSU2281",
    "SMU2400",
    "SMU2401",
    "SMU2410",
    "SMU2450",
    "SMU2460",
    "SMU2461",
    "SMU2470",
    "SMU2601A",
    "SMU2601B",
    "SMU2602A",
    "SMU2602B",
    "SMU2604A",
    "SMU2604B",
    "SMU2606B",
    "SMU2611A",
    "SMU2611B",
    "SMU2612A",
    "SMU2612B",
    "SMU2614A",
    "SMU2614B",
    "SMU2634A",
    "SMU2634B",
    "SMU2635A",
    "SMU2635B",
    "SMU2636A",
    "SMU2636B",
    "SMU2651A",
    "SMU2657A",
    "SMU6430",
    "SMU6514",
    "SMU6517B",
    "SS3706A",
    "TMT4",
    "SMU2601BPulse",
    "SupportedModels",
    "TSOVu",
    "TekScopePC",
]
