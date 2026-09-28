"""A mixin class providing common methods for devices that can save waveform data to a file."""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import final, TYPE_CHECKING

from dateutil.tz import tzlocal

if TYPE_CHECKING:
    import os


class WaveformSaveMixin(ABC):
    """A mixin class providing common methods for devices that can save waveform data to a file."""

    @property
    @abstractmethod
    def valid_waveform_extensions(self) -> tuple[str, ...]:
        """Return a tuple of valid waveform file extensions for this device.

        The extensions will be in the format '.ext', where 'ext' is the lowercase extension,
        e.g. (".wfm", ".csv", ".mat").

        Returns:
            Tuple[str, ...]: A tuple of valid, lowercase waveform file extensions for this device.
        """

    @final
    def save_waveform(
        self,
        filename: str | os.PathLike[str] | None = None,
        *,
        source: str = "ALL",
        local_folder: str | os.PathLike[str] = "./",
        device_folder: str | os.PathLike[str] = "./",
        keep_device_file: bool = False,
    ) -> None:
        """Save waveform data from the device and download it locally.

        Args:
            filename: The name of the file to save the waveform as. Defaults to a timestamped
                name using the first valid waveform extension.
            source: The waveform source to save, e.g. "CH1" or "MATH1". Defaults to "ALL", which
                saves every displayed waveform (excluding serial bus waveforms) to a single file.
            local_folder: The local folder to save the waveform file in. Defaults to "./".
            device_folder: The folder on the device to save the waveform file in. Defaults to
                "./".
            keep_device_file: Whether to keep the file on the device after downloading it.
                Defaults to False.
        """
        if not filename:
            filename_path = Path(
                datetime.now(tz=tzlocal()).strftime(
                    f"%Y%m%d_%H%M%S{self.valid_waveform_extensions[0]}"
                )
            )
        else:
            filename_path = Path(filename)
        if filename_path.suffix.lower() not in self.valid_waveform_extensions:
            msg = (
                f"Invalid waveform extension: {filename_path.suffix!r}, "
                f"valid extensions are {self.valid_waveform_extensions!r}"
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
        self._save_waveform(
            filename=filename_path,
            source=source,
            local_folder=Path(local_folder),
            device_folder=Path(device_folder),
            keep_device_file=keep_device_file,
        )

    @abstractmethod
    def _save_waveform(
        self,
        filename: Path,
        *,
        source: str,
        local_folder: Path,
        device_folder: Path,
        keep_device_file: bool = False,
    ) -> None:
        """Save waveform data from the device and download it locally.

        Args:
            filename: The name of the file to save the waveform as.
            source: The waveform source to save.
            local_folder: The local folder to save the waveform file in. Defaults to "./".
            device_folder: The folder on the device to save the waveform file in. Defaults to
                "./".
            keep_device_file: Whether to keep the file on the device after downloading it.
                Defaults to False.
        """
