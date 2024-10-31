"""A mixin class providing common methods for devices that can perform screen captures."""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import final, Optional, Tuple, TYPE_CHECKING, Union

from dateutil.tz import tzlocal

if TYPE_CHECKING:
    import os


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
    def save_screenshot(
        self,
        filename: Optional[Union[str, os.PathLike[str]]] = None,
        *,
        colors: Optional[str] = None,
        view_type: Optional[str] = None,
        local_folder: Union[str, os.PathLike[str]] = "./",
        device_folder: Union[str, os.PathLike[str]] = "./",
        keep_device_file: bool = False,
    ) -> None:
        """Capture a screenshot from the device and save it locally.

        Args:
            filename: The name of the file to save the screenshot as. Defaults to a timestamped
                name using the first valid image extension.
            colors: The color scheme to use for the screenshot. (Not used by all devices)
            view_type: The type of view to capture. (Not used by all devices)
            local_folder: The local folder to save the screenshot in. Defaults to "./".
            device_folder: The folder on the device to save the screenshot in. Defaults to "./".
            keep_device_file: Whether to keep the file on the device after downloading it.
                Defaults to False.
        """
        if not filename:
            filename_path = Path(
                datetime.now(tz=tzlocal()).strftime(
                    f"%Y%m%d_%H%M%S{self.valid_image_extensions[0]}"
                )
            )
        else:
            filename_path = Path(filename)
        if filename_path.suffix.lower() not in self.valid_image_extensions:
            msg = (
                f"Invalid image extension: {filename_path.suffix!r}, "
                f"valid extensions are {self.valid_image_extensions!r}"
            )
            raise ValueError(msg)
        local_folder_path = Path(local_folder)
        device_folder_path = Path(device_folder)
        if local_folder_path.is_file() or local_folder_path.suffix:
            msg = f"Local folder path ({local_folder_path.as_posix()}) is a file, not a directory."
            raise ValueError(msg)
        if device_folder_path.is_file() or device_folder_path.suffix:
            msg = (
                f"Device folder path ({device_folder_path.as_posix()}) is a file, not a directory."
            )
            raise ValueError(msg)
        if not local_folder_path.exists():
            local_folder_path.mkdir(parents=True)
        self._save_screenshot(
            filename=filename_path,
            colors=colors,
            view_type=view_type,
            local_folder=Path(local_folder),
            device_folder=Path(device_folder),
            keep_device_file=keep_device_file,
        )

    @abstractmethod
    def _save_screenshot(
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
