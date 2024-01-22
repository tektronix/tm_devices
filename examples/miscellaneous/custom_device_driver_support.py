"""An example of external device support via a custom driver."""
from tm_devices import DeviceManager
from tm_devices.drivers import MSO5
from tm_devices.drivers.pi.scopes.scope import Scope


class CustomScope(Scope):
    """Custom scope class."""

    def custom_method(self, value: str) -> None:
        """Add a custom method to the custom driver."""
        print(f"{self.name}, {value=}")


# For VISA devices, the model series is based on the model that is returned from
# the ``*IDN?`` query. (See the ``tm_devices.helpers.get_model_series()`` function for details)
# For REST API devices, the model series is provided via the ``device_driver`` parameter in
# the configuration file, environment variable, or python code.
CUSTOM_DEVICE_DRIVERS = {  # A mapping of custom model series strings to Python driver classes
    "CustomModelSeries": CustomScope,
}


with DeviceManager(external_device_drivers=CUSTOM_DEVICE_DRIVERS) as device_manager:
    # Add a scope that is currently supported by the package
    mso5: MSO5 = device_manager.add_scope("192.168.0.1")  # pyright: ignore[reportAssignmentType]
    # Add the custom scope
    custom_scope: CustomScope = device_manager.add_scope("192.168.0.2")  # pyright: ignore[reportAssignmentType]

    # Custom drivers inherit all methods
    custom_scope.expect_esr(0)  # check for no errors
    custom_scope.cleanup()  # cleanup the custom scope

    # Custom drivers can also use added methods
    custom_scope.custom_method("value")
