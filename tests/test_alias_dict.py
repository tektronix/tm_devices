"""Test for the AliasDict class."""

import pytest

from tm_devices.helpers.alias_dict import AliasDict


def test_alias_dict() -> None:
    """Test the alias dict."""
    test_dict = AliasDict()
    assert not test_dict

    # Add a key with a value
    test_value = "value"
    test_dict["key"] = test_value
    assert len(test_dict) == 1
    assert test_dict["key"] == test_value

    # Add an alias to an existing value
    test_dict["alias"] = test_value
    assert len(test_dict) == 1
    assert test_dict["key"] == test_value
    assert test_dict["alias"] == test_value
    assert id(test_dict["key"]) == id(test_dict["alias"])

    # Add a new key and value
    test_value_2 = "value 2"
    test_dict["key_2"] = test_value_2
    test_dict["alias_2"] = test_value_2
    assert len(test_dict) == 2
    assert test_dict["key"] == test_value
    assert test_dict["alias"] == test_value
    assert test_dict["key_2"] == test_value_2
    assert id(test_dict["key"]) == id(test_dict["alias"])
    assert id(test_dict["key_2"]) == id(test_dict["alias_2"])
    assert id(test_dict["key"]) != id(test_dict["key_2"])

    # Verify that duplicate keys are not allowed
    with pytest.raises(KeyError):
        test_dict["key"] = "more data"

    # Verify that duplicate aliases are not allowed
    with pytest.raises(KeyError):
        test_dict["alias"] = "more data"

    # Remove a value, make sure alias and key both raise KeyError
    del test_dict["key"]
    with pytest.raises(KeyError):
        _ = test_dict["key"]
    with pytest.raises(KeyError):
        _ = test_dict["alias"]
    del test_dict["key_2"]
    with pytest.raises(KeyError):
        _ = test_dict["key_2"]
    with pytest.raises(KeyError):
        _ = test_dict["alias_2"]
