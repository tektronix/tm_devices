"""Systems Switches package init file."""
from tm_devices.drivers.pi.systems_switches.ss3706a import SS3706A
from tm_devices.drivers.pi.systems_switches.systems_switch import SystemsSwitch

__all__ = [
    "SystemsSwitch",
    "SS3706A",
]
