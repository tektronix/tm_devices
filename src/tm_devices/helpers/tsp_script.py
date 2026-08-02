"""Helpers for safely loading TSP scripts onto Tektronix instruments.

TSP devices have a hardware write buffer limited to 1000 characters per
write command (including any write-termination character appended by the
VISA layer). Sending more than this limit without an intermediate flush
causes the instrument to silently truncate or return an error (issue #500).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Protocol

    class _Writer(Protocol):
        def write(self, cmd: str) -> None: ...


# The TSP hardware write buffer limit. We use 999 to leave 1 byte of
# headroom for the write-termination character appended by the VISA layer.
TSP_WRITE_MAX_CHARS: int = 999


def load_script_chunked(
    device: "_Writer",
    name: str,
    body: str,
    run_after_load: bool = False,
) -> None:
    """Load a TSP script onto the device, chunking writes to stay within the
    1000-character hardware buffer limit.

    Parameters
    ----------
    device:
        Any object with a ``write(cmd: str)`` method — typically a
        :class:`tm_devices.drivers.TekSmua` or similar TSP device.
    name:
        Name to register the script under on the instrument.
    body:
        Full TSP script source code.
    run_after_load:
        When True, call ``<name>()`` after loading so the script runs
        immediately.
    """
    device.write(f"loadscript {name}")

    lines = body.splitlines(keepends=True)
    chunk: list[str] = []
    chunk_len: int = 0

    for line in lines:
        line_len = len(line)
        if chunk_len + line_len >= TSP_WRITE_MAX_CHARS:
            # Flush the accumulated chunk before it exceeds the buffer.
            if chunk:
                device.write("".join(chunk))
            chunk = [line]
            chunk_len = line_len
        else:
            chunk.append(line)
            chunk_len += line_len

    # Flush any remaining lines.
    if chunk:
        device.write("".join(chunk))

    device.write("endscript")

    if run_after_load:
        device.write(f"{name}()")
