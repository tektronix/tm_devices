"""Tests for tsp_script.load_script_chunked."""

from __future__ import annotations

from unittest.mock import call, MagicMock

from tm_devices.helpers.tsp_script import load_script_chunked, TSP_WRITE_MAX_CHARS


def _make_writer():
    return MagicMock()


def test_short_script_single_write():
    """A script under TSP_WRITE_MAX_CHARS is sent in one body write."""
    device = _make_writer()
    body = 'print("hello")\n'
    load_script_chunked(device, "short", body)

    calls = device.write.call_args_list
    assert calls[0] == call("loadscript short")
    assert calls[1] == call(body)
    assert calls[2] == call("endscript")
    assert len(calls) == 3


def test_long_script_is_chunked():
    """A script over TSP_WRITE_MAX_CHARS is split across multiple writes."""
    device = _make_writer()
    # Build a body where each line is 100 chars; 11 lines = 1100 chars total.
    line = "x" * 98 + "\n"  # 99 chars including newline
    body = line * 11  # 1089 chars — exceeds TSP_WRITE_MAX_CHARS

    load_script_chunked(device, "big", body)

    calls = device.write.call_args_list
    assert calls[0] == call("loadscript big")
    assert calls[-1] == call("endscript")

    # There should be at least 2 body writes (the script was chunked).
    body_calls = calls[1:-1]
    assert len(body_calls) >= 2, "Expected chunked writes for long script"

    # Reconstruct the body from all intermediate writes.
    reconstructed = "".join(c[0][0] for c in body_calls)
    assert reconstructed == body

    # No single write should exceed the buffer limit.
    for c in body_calls:
        assert len(c[0][0]) <= TSP_WRITE_MAX_CHARS


def test_run_after_load():
    """run_after_load=True appends a call invocation."""
    device = _make_writer()
    load_script_chunked(device, "myscript", 'print(1)\n', run_after_load=True)

    calls = device.write.call_args_list
    assert calls[-1] == call("myscript()")
