"""Unit tests for the decorators package."""

import pytest

from tm_devices.helpers import Singleton


# pylint: disable=too-few-public-methods
class DummyClass(metaclass=Singleton):
    """Dummy class to use during testing."""

    init_count = 0

    def __init__(self, value: bool = False) -> None:
        """Create an instance of the dummy class."""
        print("running init")
        self.init_count += 1
        self.value = value


def test_singleton(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that the singleton decorator works properly."""
    # Create the first instance
    dummy = DummyClass()
    assert not dummy.value
    assert dummy.init_count == 1

    # Try to create a new instance
    with pytest.warns(UserWarning):
        new_dummy = DummyClass(value=True)
    assert dummy == new_dummy
    assert dummy is new_dummy
    assert new_dummy.init_count == 1
    assert not dummy.value
    assert dummy.init_count == 1

    stdout = capsys.readouterr().out
    assert stdout.count("running init") == 1
