# pyright: reportPrivateUsage=none
"""Test the AWGs."""

from typing import cast, Optional

import pytest

from tm_devices import DeviceManager
from tm_devices.drivers import (
    AWG5K,
    AWG5KB,
    AWG5KC,
    AWG7K,
    AWG7KB,
    AWG7KC,
    AWG70KA,
    AWG70KB,
    AWG5200,
)
from tm_devices.drivers.pi.signal_generators.awgs.awg import (
    AWGSourceDeviceConstants,
    ExtendedSourceDeviceConstants,
    ParameterBounds,
    SignalGeneratorFunctionsAWG,
)
from tm_devices.helpers import SignalGeneratorOutputPaths5200, SignalGeneratorOutputPathsNon5200


def check_constraints(
    constraint: ExtendedSourceDeviceConstants,
    sample_range: ParameterBounds,
    amplitude_range: ParameterBounds,
    offset_range: ParameterBounds,
    length_range: ParameterBounds,
) -> None:
    """Check to see if the waveform constraints are correct.

    Args:
        constraint: The constraints to verify.
        sample_range: The wanted sample range.
        amplitude_range: The wanted amplitude range.
        offset_range: The wanted offset_range.
        length_range: The length range of the waveform.
    """
    assert constraint == ExtendedSourceDeviceConstants(
        amplitude_range=amplitude_range,
        offset_range=offset_range,
        frequency_range=ParameterBounds(
            lower=sample_range.lower / length_range.upper,
            upper=sample_range.upper / length_range.lower,
        ),
        sample_rate_range=sample_range,
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )


# pylint: disable=too-many-locals
def test_awg5200(device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]) -> None:
    """Test the AWG5200 driver.

    Args:
        device_manager: The DeviceManager object.
        capsys: The captured stdout and stderr.
    """
    awg520050 = cast(AWG5200, device_manager.add_awg("awg5200opt50-hostname", alias="awg520050"))
    awg520025 = cast(AWG5200, device_manager.add_awg("awg5200opt25-hostname", alias="awg520025"))
    assert id(device_manager.get_awg(number_or_alias="awg520050")) == id(awg520050)
    assert id(device_manager.get_awg(number_or_alias=awg520050.device_number)) == id(awg520050)
    assert awg520050.total_channels == 4
    assert awg520050.all_channel_names_list == ("SOURCE1", "SOURCE2", "SOURCE3", "SOURCE4")
    awg520050.write("*SRE 256")
    awg520050.expect_esr(32, '1, "Command error"\n0,"No error"')
    with pytest.raises(AssertionError):
        awg520050.expect_esr(32, '1, Command error\n0,"No error"')
    _ = capsys.readouterr().out  # throw away stdout
    awg520050.load_waveform("test", "file_path.txt", "TXT")
    assert 'MMEMory:IMPort "test", "file_path.txt", TXT' in capsys.readouterr().out
    awg520050.load_waveform("test", '"file_path.txt"', "TXT")
    assert 'MMEMory:IMPort "test", "file_path.txt", TXT' in capsys.readouterr().out
    assert awg520050.source_device_constants == AWGSourceDeviceConstants(
        memory_page_size=1,
        memory_max_record_length=16200000,
        memory_min_record_length=1,
    )
    assert awg520050.opt_string == "50,SEQ"
    awg520050_constraints = awg520050.get_waveform_constraints(SignalGeneratorFunctionsAWG.SIN)
    min_smaple_50 = 300.0
    max_sample_50 = 5.0e9
    assert awg520050_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=25.0e-3, upper=750.0e-3),
        offset_range=ParameterBounds(lower=-2.0, upper=2.0),
        frequency_range=ParameterBounds(lower=min_smaple_50 / 3600.0, upper=max_sample_50 / 10.0),
        sample_rate_range=ParameterBounds(lower=min_smaple_50, upper=max_sample_50),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    awg520050_constraints = awg520050.get_waveform_constraints(
        SignalGeneratorFunctionsAWG.SIN,
        output_signal_path=awg520050.OutputSignalPath.DCHV,
    )
    min_smaple_50 = 300.0
    max_sample_50 = 5.0e9
    assert awg520050_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=10.0e-3, upper=5.0),
        offset_range=ParameterBounds(lower=-2.0, upper=2.0),
        frequency_range=ParameterBounds(lower=min_smaple_50 / 3600.0, upper=max_sample_50 / 10.0),
        sample_rate_range=ParameterBounds(lower=min_smaple_50, upper=max_sample_50),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )

    # Set output signal path as default.
    default_path = awg520050.OutputSignalPath.DCHB
    awg520050.source_channel["SOURCE1"].set_output_signal_path()
    output_path = awg520050.query("OUTPUT1:PATH?")
    assert output_path == default_path.value

    _ = capsys.readouterr().out  # throw away stdout
    awg520050.load_waveform_from_set(
        "*SINE100",
        awg520050.sample_waveform_set_file,
    )
    sasset_waveform_cmd = (
        "MMEMORY:OPEN:SASSET:WAVEFORM "
        '"C:\\\\Program Files\\\\Tektronix\\\\AWG5200\\\\Samples\\\\AWG5k7k Predefined Waveforms'
        '.awgx", "*SINE100"'
    )
    stdout = capsys.readouterr().out
    assert sasset_waveform_cmd in stdout

    # Invalid file type for waveform file.
    with pytest.raises(ValueError, match=".txt is an invalid waveform file extension."):
        awg520050.load_waveform_set(
            "unittest.txt",
        )

    assert awg520025.opt_string == "25,DC"
    awg520025_constraints = awg520025.get_waveform_constraints(waveform_length=500)
    min_smaple_25 = 300.0
    max_sample_25 = 2.5e9
    assert awg520025_constraints == ExtendedSourceDeviceConstants(
        amplitude_range=ParameterBounds(lower=25.0e-3, upper=1.5),
        offset_range=ParameterBounds(lower=-2.0, upper=2.0),
        frequency_range=ParameterBounds(lower=min_smaple_25 / 500.0, upper=max_sample_25 / 500.0),
        sample_rate_range=ParameterBounds(lower=min_smaple_25, upper=max_sample_25),
        square_duty_cycle_range=None,
        pulse_width_range=None,
        ramp_symmetry_range=None,
    )
    error = "AWG Constraints require exclusively function or waveform_length."
    with pytest.raises(ValueError, match=error):
        awg520025.get_waveform_constraints()

    with pytest.raises(ValueError, match=r"Output state value must be 1 \(ON\) or 0 \(OFF\)\."):
        awg520025.source_channel["SOURCE1"].set_state(-1)

    # Coverage for setting frequency with absolute tolerance.
    awg520050.set_sample_rate(5000000000, absolute_tolerance=0)
    query_val = awg520050.query("CLOCK:SRATE?")
    assert float(query_val) == 5000000000


def test_awg70k(  # noqa: PLR0915  # pylint: disable=too-many-locals
    device_manager: DeviceManager, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test the AWG70K driver.

    Args:
        device_manager: The DeviceManager object.
        capsys: The captured stdout and stderr.
    """
    awg70ka150 = cast(
        AWG70KA, device_manager.add_awg("awg70001aopt150-hostname", alias="awg70ka150")
    )
    awg70ka225 = cast(
        AWG70KA, device_manager.add_awg("awg70002aopt225-hostname", alias="awg70ka225")
    )
    awg70ka216 = cast(
        AWG70KA, device_manager.add_awg("awg70002aopt216-hostname", alias="awg70ka216")
    )
    awg70kb208 = cast(
        AWG70KB, device_manager.add_awg("awg70002bopt208-hostname", alias="awg70kb208")
    )
    length_range = ParameterBounds(lower=10, upper=1000)
    min_smaple = 1.5e3
    awg_list = [awg70ka150, awg70ka225, awg70ka216, awg70kb208]
    output_path: Optional[SignalGeneratorOutputPathsNon5200] = None
    for awg in awg_list:
        option = awg.alias[-3:]
        assert awg.opt_string == option

        if not output_path:
            offset_range = ParameterBounds(lower=-0.0, upper=0.0)
            ampl_range = ParameterBounds(lower=0.125, upper=0.5)
        else:
            offset_range = ParameterBounds(lower=-0.4, upper=0.8)
            ampl_range = ParameterBounds(lower=31.0e-3, upper=1.2)

        constraints = awg.get_waveform_constraints(
            SignalGeneratorFunctionsAWG.RAMP,
            output_signal_path=output_path,
        )

        output_path = awg.OutputSignalPath.DCA

        sample_range = ParameterBounds(lower=min_smaple, upper=int(option[1:3]) * 1.0e9)
        check_constraints(
            constraints,
            sample_range,
            ampl_range,
            offset_range,
            length_range,
        )

    # Invalid output signal path.
    with pytest.raises(ValueError, match="DCHB is an invalid output signal path for AWG70001."):
        awg70ka150.source_channel["SOURCE1"].set_output_signal_path(
            SignalGeneratorOutputPaths5200.DCHB
        )

    # Set default output signal path (will try DCA and succeed).
    awg70ka150.source_channel["SOURCE1"].set_output_signal_path()
    output_path_query = awg70ka150.query("OUTPUT1:PATH?")
    assert output_path_query == awg70ka150.OutputSignalPath.DCA.value

    # Set output signal path to DIR.
    awg70ka150.source_channel["SOURCE1"].set_output_signal_path(awg70ka150.OutputSignalPath.DIR)
    output_path_query = awg70ka150.query("OUTPUT1:PATH?")
    assert output_path_query == SignalGeneratorOutputPathsNon5200.DIR.value
    # Cannot set offset with output signal path set to DIR.
    with pytest.raises(
        ValueError,
        match="The offset can only be set with an output signal path of DCA.",
    ):
        awg70ka150.source_channel["SOURCE1"].set_offset(0.1)

    # Even with output signal path set to DIR, no errors raised because offset is being set to 0.
    _ = capsys.readouterr().out  # throw away stdout
    awg70ka150.source_channel["SOURCE1"].set_offset(0)
    stdout = capsys.readouterr().out
    assert "SOURCE1:VOLTAGE:OFFSET" not in stdout

    # DCA as output signal path.
    awg70ka150.source_channel["SOURCE1"].set_output_signal_path(awg70ka150.OutputSignalPath.DCA)
    output_path_query = awg70ka150.query("OUTPUT1:PATH?")
    assert output_path_query == SignalGeneratorOutputPathsNon5200.DCA.value
    awg70ka150.source_channel["SOURCE1"].set_offset(0.1)
    offset = float(awg70ka150.query("SOURCE1:VOLTAGE:OFFSET?"))
    assert offset == 0.1

    awg70ka150.set_sample_rate(500000000)
    current_frequency = awg70ka150.query("SOURCE1:FREQUENCY?")
    assert float(current_frequency) == 500000000

    # Load specific waveform.
    _ = capsys.readouterr().out  # throw away stdout
    awg70ka150.load_waveform_from_set(
        "*SINE100",
        awg70ka150.sample_waveform_set_file,
    )
    sasset_waveform_cmd = (
        "MMEMORY:OPEN:SASSET:WAVEFORM "
        '"C:\\\\Program Files\\\\Tektronix\\\\AWG70000\\\\Samples\\\\AWG5k7k Predefined Waveforms'
        '.awgx", "*SINE100"'
    )
    stdout = capsys.readouterr().out
    assert sasset_waveform_cmd in stdout

    # Invalid file type for waveform file.
    with pytest.raises(ValueError, match=".txt is an invalid waveform file extension."):
        awg70ka150.load_waveform_set(
            "unittest.txt",
        )

    # Coverage for setting frequency with absolute tolerance.
    awg70ka150.set_sample_rate(5000000000, absolute_tolerance=0)
    query_val = awg70ka150.query("SOURCE1:FREQUENCY?")
    assert float(query_val) == 5000000000


def test_awg7k(device_manager: DeviceManager) -> None:  # pylint: disable=too-many-locals
    """Test the AWG7K driver.

    Args:
        device_manager: The DeviceManager object.
    """
    awg7k01 = cast(AWG7K, device_manager.add_awg("awg7051opt01-hostname", alias="awg7k01"))
    awg7k06 = cast(AWG7K, device_manager.add_awg("awg7102opt06-hostname", alias="awg7k06"))
    awg7kb02 = cast(AWG7KB, device_manager.add_awg("awg7062bopt02-hostname", alias="awg7kb02"))
    awg7kb01 = cast(AWG7KB, device_manager.add_awg("awg7121bopt01-hostname", alias="awg7kb01"))
    awg7kc06 = cast(AWG7KC, device_manager.add_awg("awg7082copt01-hostname", alias="awg7kc01"))
    awg7kc01 = cast(AWG7KC, device_manager.add_awg("awg7122copt06-hostname", alias="awg7kc06"))
    length_range = ParameterBounds(lower=10, upper=1000)
    awg_list = [awg7k01, awg7k06, awg7kb02, awg7kb01, awg7kc06, awg7kc01]

    output_path: Optional[SignalGeneratorOutputPathsNon5200] = None
    for awg in awg_list:
        option = awg.alias[-2:]
        assert awg.opt_string == option

        sample_range = ParameterBounds(lower=10.0e6, upper=int(awg.model[4:6]) * 1.0e9)

        if option in {"02", "06"}:
            ampl_range = ParameterBounds(lower=0.5, upper=1.0)
            offset_range = ParameterBounds(lower=-0.0, upper=0.0)
        else:
            if not output_path:
                offset_range = ParameterBounds(lower=-0.5, upper=0.5)
            else:
                offset_range = ParameterBounds(lower=-0.0, upper=0.0)

            ampl_range = ParameterBounds(lower=50.0e-3, upper=2.0)

        constraints = awg.get_waveform_constraints(
            SignalGeneratorFunctionsAWG.TRIANGLE,
            output_signal_path=output_path,
        )
        output_path = awg.OutputSignalPath.DIR
        check_constraints(
            constraints,
            sample_range,
            ampl_range,
            offset_range,
            length_range,
        )


def test_awg5k(device_manager: DeviceManager) -> None:
    """Test the AWG5K driver.

    Args:
        device_manager: The DeviceManager object.
    """
    awg5k = cast(AWG5K, device_manager.add_awg("awg5012-hostname", alias="awg5k"))
    awg5kb = cast(AWG5KB, device_manager.add_awg("awg5002b-hostname", alias="awg5kb"))
    awg5kc = cast(AWG5KC, device_manager.add_awg("awg5012c-hostname", alias="awg5kc"))
    length_range = ParameterBounds(lower=960, upper=960)
    awg_list = [awg5k, awg5kb, awg5kc]
    offset_range = ParameterBounds(lower=-2.25, upper=2.25)
    ampl_range = ParameterBounds(lower=20.0e-3, upper=4.5)

    for awg in awg_list:
        sample_range = ParameterBounds(lower=10.0e6, upper=int(awg.model[5]) * 600.0e6 + 600.0e6)

        constraints = awg.get_waveform_constraints(SignalGeneratorFunctionsAWG.CLOCK)

        check_constraints(
            constraints,
            sample_range,
            ampl_range,
            offset_range,
            length_range,
        )

    # With DIR output signal path.
    constraints = awg5k.get_waveform_constraints(
        SignalGeneratorFunctionsAWG.CLOCK, output_signal_path=awg5k.OutputSignalPath.DIR
    )
    sample_range = ParameterBounds(lower=10.0e6, upper=int(awg5k.model[5]) * 600.0e6 + 600.0e6)
    offset_range = ParameterBounds(lower=0, upper=0)
    check_constraints(
        constraints,
        sample_range,
        ampl_range,
        offset_range,
        length_range,
    )

    # Coverage for setting frequency with absolute tolerance.
    awg5k.set_sample_rate(10.0e6, absolute_tolerance=0)
    query_val = awg5k.query("SOURCE1:FREQUENCY?")
    assert float(query_val) == 10.0e6
