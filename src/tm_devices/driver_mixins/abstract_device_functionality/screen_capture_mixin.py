"""A mixin class providing common methods for devices that can perform screen captures."""

import os

from abc import ABC, abstractmethod
from pathlib import Path
from typing import final, Optional, Tuple, Union


class ScreenCaptureMixin(ABC):
    """A mixin class providing common methods for devices that can perform screen captures."""

    @property
    @abstractmethod
    def valid_image_extensions(self) -> Tuple[str, ...]:
        """Return a tuple of valid image extensions for this device.

        The extensions will be in the format '.ext', where 'ext' is the lowercase extension,
        e.g. (".png", ".jpg").

        Returns:
            Tuple[str, ...]: A tuple of valid, lowercase image extensions for this device.
        """

    @final
    def capture_screen(
        self,
        filename: Union[str, os.PathLike[str]],
        *,
        colors: Optional[str] = None,
        view_type: Optional[str] = None,
        local_folder: Union[str, os.PathLike[str]] = "./",
        device_folder: Union[str, os.PathLike[str]] = "./",
        keep_device_file: bool = False,
    ) -> None:
        """Capture a screenshot from the device and save it locally.

        Args:
            filename: The name of the file to save the screenshot as.
            colors: The color scheme to use for the screenshot.
            view_type: The type of view to capture.
            local_folder: The local folder to save the screenshot in. Defaults to "./".
            device_folder: The folder on the device to save the screenshot in. Defaults to "./".
            keep_device_file: Whether to keep the file on the device after downloading it.
                Defaults to False.
        """
        filename_path = Path(filename)
        if filename_path.suffix.lower() not in self.valid_image_extensions:
            msg = (
                f"Invalid image extension: {filename_path.suffix!r}, "
                f"valid extensions are {self.valid_image_extensions!r}"
            )
            raise ValueError(msg)
        self._capture_screen(
            filename=filename_path,
            colors=colors,
            view_type=view_type,
            local_folder=Path(local_folder),
            device_folder=Path(device_folder),
            keep_device_file=keep_device_file,
        )

    @abstractmethod
    def _capture_screen(
        self,
        filename: Path,
        *,
        colors: Optional[str],
        view_type: Optional[str],
        local_folder: Path,
        device_folder: Path,
        keep_device_file: bool = False,
    ) -> None:
        """Capture a screenshot from the device and save it locally.

        Args:
            filename: The name of the file to save the screenshot as.
            colors: The color scheme to use for the screenshot.
            view_type: The type of view to capture.
            local_folder: The local folder to save the screenshot in. Defaults to "./".
            device_folder: The folder on the device to save the screenshot in. Defaults to "./".
            keep_device_file: Whether to keep the file on the device after downloading it.
                Defaults to False.
        """
