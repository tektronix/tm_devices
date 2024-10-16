"""An example of alias usage."""

from tm_devices import DeviceManager
from tm_devices.drivers import AWG5200, MSO5

with DeviceManager(verbose=True) as dm:
    # Add a scope and give an optional alias
    dm.add_scope("MSO56-100083", alias="BOB")
    # Add an awg using an IP address and optional alias
    dm.add_awg("192.168.0.1", alias="JILL")

    # Get the scope with the BOB alias from device manager
    bobs_scope: MSO5 = dm.get_scope("BOB")
    # Get the awg with the JILL alias from device manager
    jills_awg: AWG5200 = dm.get_awg("JILL")
