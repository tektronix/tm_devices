"""A mixin class providing common methods and attributes for devices with installable licenses."""

from abc import ABC, abstractmethod
from typing import final, Tuple

from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813


class LicensedMixin(ABC):
    """A mixin class which adds methods and properties for handling licenses."""

    @cached_property
    @abstractmethod
    def license_list(self) -> Tuple[str, ...]:
        """Return the list of licenses installed on the device."""

    @final
    def has_license(self, license_name: str) -> bool:
        """Check if the given license name is in the license list of the device.

        Args:
            license_name: The name of the license to check for in the license list.

        Returns:
            A boolean indicating if the license name is in the list.
        """
        return license_name in self.license_list
