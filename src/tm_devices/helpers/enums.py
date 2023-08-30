"""Module containing Enums for the tm_devices package."""
from enum import Enum
from types import DynamicClassAttribute
from typing import cast, List


class CustomStrEnum(Enum):
    """A custom base class for string Enums.

    This class provides better type hinting for the value property.
    """

    @DynamicClassAttribute
    def name(self) -> str:  # pylint: disable=function-redefined
        """Return the name of the Enum member."""
        return self._name_  # pylint: disable=no-member

    @DynamicClassAttribute
    def value(self) -> str:
        """Return the value of the Enum member."""
        return cast(str, self._value_)  # pylint: disable=no-member

    @classmethod
    def list_values(cls) -> List[str]:
        """Return a list of all the values of the enum."""
        return [enum_entry.value for enum_entry in cls]


class ConfigFileType(CustomStrEnum):
    """Class holding valid config file extensions."""

    YAML = "yaml"
    YML = "yml"
    TOML = "toml"


class ConnectionTypes(CustomStrEnum):
    """Class holding the valid connection types supported."""

    REST_API = "REST_API"
    """An enum member representing a REST API connection made over LAN."""
    SERIAL = "SERIAL"
    """An enum member representing a VISA connection made over the Serial (ASRL) interface."""
    SOCKET = "SOCKET"
    """An enum member representing a VISA connection made over the Socket interface."""
    TCPIP = "TCPIP"
    """An enum member representing a VISA connection made over the TCPIP interface."""
    USB = "USB"
    """An enum member representing a VISA connection made over the USBTMC interface."""
    GPIB = "GPIB"
    """An enum member representing a VISA connection made over the GPIB interface."""
    MOCK = "MOCK"
    """An enum member representing a VISA connection to a MOCK device."""
    _UNIT_TEST_ONLY_CONNECTION_DO_NOT_USE = "_UNIT_TEST_ONLY_CONNECTION_DO_NOT_USE"


class DeviceTypes(CustomStrEnum):
    """Class holding the valid device types supported.

    Any additions to this class need to be added to
    the :py:obj:`~tm_devices.helpers.constants_and_dataclasses.VALID_DEVICE_CONNECTION_TYPES`
    constant as well.
    """

    # NOTE: Any additions to this enum will require the corresponding Parent class be added to the
    #       tests.test_tm_devices.test_device_method_abstraction unit test.

    AFG = "AFG"
    """An enum member representing an Arbitrary Function Generator."""
    AWG = "AWG"
    """An enum member representing an Arbitrary Waveform Generator."""
    DAQ = "DAQ"
    """An enum member representing a Data Acquisition system."""
    DMM = "DMM"
    """An enum member representing a Digital Multimeter."""
    MT = "MT"
    """An enum member representing a Margin Tester."""
    PSU = "PSU"
    """An enum member representing a Power Supply Unit."""
    SCOPE = "SCOPE"
    """An enum member representing an Oscilloscope."""
    SMU = "SMU"
    """An enum member representing a Source Measure Unit."""
    SS = "SS"
    """An enum member representing a Systems Switch."""
    _UNIT_TEST_ONLY_DEVICE_DO_NOT_USE = "_UNIT_TEST_ONLY_DEVICE_DO_NOT_USE"


class SupportedModels(CustomStrEnum):
    """Class containing all model series supported by the device management system."""

    # AFGs
    AFG3K = "AFG3K"
    AFG3KB = "AFG3KB"
    AFG3KC = "AFG3KC"
    AFG31K = "AFG31K"
    # AWGs
    AWG5200 = "AWG5200"
    AWG5K = "AWG5K"
    AWG5KB = "AWG5KB"
    AWG5KC = "AWG5KC"
    AWG7K = "AWG7K"
    AWG7KB = "AWG7KB"
    AWG7KC = "AWG7KC"
    AWG70KA = "AWG70KA"
    AWG70KB = "AWG70KB"
    # Scopes
    DPO5K = "DPO5K"
    DPO5KB = "DPO5KB"
    DPO7K = "DPO7K"
    DPO7KC = "DPO7KC"
    DPO70K = "DPO70K"
    DPO70KC = "DPO70KC"
    DPO70KD = "DPO70KD"
    DPO70KDX = "DPO70KDX"
    DPO70KSX = "DPO70KSX"
    DSA70K = "DSA70K"
    DSA70KC = "DSA70KC"
    DSA70KD = "DSA70KD"
    LPD6 = "LPD6"
    MSO2 = "MSO2"
    MSO4 = "MSO4"
    MSO5 = "MSO5"
    MSO5B = "MSO5B"
    MSO5LP = "MSO5LP"
    MSO6 = "MSO6"
    MSO6B = "MSO6B"
    MSO2K = "MSO2K"
    MSO2KB = "MSO2KB"
    DPO2K = "DPO2K"
    DPO2KB = "DPO2KB"
    MDO3 = "MDO3"
    MDO3K = "MDO3K"
    MSO4K = "MSO4K"
    MSO4KB = "MSO4KB"
    MDO4K = "MDO4K"
    MDO4KB = "MDO4KB"
    MDO4KC = "MDO4KC"
    DPO4K = "DPO4K"
    DPO4KB = "DPO4KB"
    MSO5K = "MSO5K"
    MSO5KB = "MSO5KB"
    MSO70K = "MSO70K"
    MSO70KC = "MSO70KC"
    MSO70KDX = "MSO70KDX"
    TEKSCOPESW = "TekScopeSW"
    TSOVU = "TSOVu"
    # Margin Testers
    TMT4 = "TMT4"
    # SMUs
    SMU2400 = "SMU2400"
    SMU2401 = "SMU2401"
    SMU2410 = "SMU2410"
    SMU2450 = "SMU2450"
    SMU2460 = "SMU2460"
    SMU2461 = "SMU2461"
    SMU2470 = "SMU2470"
    SMU2601B = "SMU2601B"
    SMU2601B_PULSE = "SMU2601BPulse"
    SMU2602B = "SMU2602B"
    SMU2604B = "SMU2604B"
    SMU2606B = "SMU2606B"
    SMU2611B = "SMU2611B"
    SMU2612B = "SMU2612B"
    SMU2614B = "SMU2614B"
    SMU2634B = "SMU2634B"
    SMU2635B = "SMU2635B"
    SMU2636B = "SMU2636B"
    SMU2651A = "SMU2651A"
    SMU2657A = "SMU2657A"
    SMU2601A = "SMU2601A"
    SMU2602A = "SMU2602A"
    SMU2604A = "SMU2604A"
    SMU2611A = "SMU2611A"
    SMU2612A = "SMU2612A"
    SMU2614A = "SMU2614A"
    SMU2634A = "SMU2634A"
    SMU2635A = "SMU2635A"
    SMU2636A = "SMU2636A"
    SMU6430 = "SMU6430"
    SMU6514 = "SMU6514"
    SMU6517B = "SMU6517B"
    # PSUs
    PSU2200 = "PSU2200"
    PSU2220 = "PSU2220"
    PSU2230 = "PSU2230"
    PSU2231 = "PSU2231"
    PSU2231A = "PSU2231A"
    PSU2280 = "PSU2280"
    PSU2281 = "PSU2281"
    # DAQ
    DAQ6510 = "DAQ6510"
    # DMMs
    DMM6500 = "DMM6500"
    DMM7510 = "DMM7510"
    DMM7512 = "DMM7512"
    # SSs
    SS3706A = "SS3706A"


class SupportedRequestTypes(CustomStrEnum):
    """All request types supported by a RESTAPIDevice."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class SignalSourceFunctionBase(Enum):
    """Base Enum function names."""


class SignalSourceFunctionsAWG(SignalSourceFunctionBase):
    """AWG function names."""

    SIN = "Sine"
    SQUARE = "Square"
    RAMP = "Ramp"
    TRIANGLE = "Triangle"
    CLOCK = "Clock"
    DC = "DC"


class SignalSourceFunctionsAFG(SignalSourceFunctionBase):
    """AFG function names."""

    SIN = "SIN"
    SQUARE = "SQU"
    PULSE = "PULS"
    RAMP = "RAMP"
    PRNOISE = "PRN"
    DC = "DC"
    SINC = "SINC"
    GAUSSIAN = "GAUS"
    LORENTZ = "LOR"
    ERISE = "ERIS"
    EDECAY = "EDEC"
    HAVERSINE = "HAV"
    ARBITRARY = "ARB"


class SignalSourceFunctionsIAFG(SignalSourceFunctionBase):
    """IAFG function names."""

    SIN = "SINE"
    SQUARE = "SQUARE"
    RAMP = "RAMP"
    PULSE = "PULSE"
    DC = "DC"
    SINC = "SINC"
    GAUSSIAN = "GAUSSIAN"
    LORENTZ = "LORENTZ"
    ERISE = "ERISE"
    EDECAY = "EDECAY"
    HAVERSINE = "HAVERSINE"
    CARDIAC = "CARDIAC"
    NOISE = "NOISE"
    ARBITRARY = "ARBITRARY"
