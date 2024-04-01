"""An example showing the use of waveform constraints for an AWG."""

from tm_devices import DeviceManager
from tm_devices.drivers import AWG5K
from tm_devices.helpers import SignalGeneratorFunctionsAWG

# The desired frequency.
DESIRED_FREQUENCY = 10e18

# The desired amplitude.
DESIRED_AMPLITUDE = 5.0

# The desired sample rate.
DESIRED_SAMPLE_RATE = 1

# The desired function to generate.
DESIRED_FUNCTION = SignalGeneratorFunctionsAWG.SIN

# The desired waveform length to generate.
DESIRED_WAVEFORM_LENGTH = 1000000

# Format error message for function constraints.
FORMAT_ERROR_MESSAGE_FUNCTION = (
    "The desired {desired_prop_name} ({desired_val}) is not within the device's "
    "{desired_prop_name} range for generating a {function_name} waveform. "
    "Must be in the range of [{lower}, {upper}]."
)

# Format error message for waveform length constraints.
FORMAT_ERROR_MESSAGE_WAVEFORM_LENGTH = (
    "The desired {desired_prop_name} ({desired_val}) is not within the device's "
    "{desired_prop_name} range for generating a waveform with a length of {waveform_length}. "
    "Must be in the range of [{lower}, {upper}]."
)


with DeviceManager(verbose=True) as dm:
    # Create a connection to the scope and indicate that it is an AWG5K for type hinting.
    awg5k: AWG5K = dm.add_awg("192.168.0.1")  # pyright: ignore[reportAssignmentType]

    # Get the device constraints for generating the desired function on an AWG5K.
    awg5k_constraints_function = awg5k.get_waveform_constraints(function=DESIRED_FUNCTION)

    # Get the frequency constraints.
    frequency_range = awg5k_constraints_function.frequency_range

    # Print a message if the desired frequency is not within the frequency constraints.
    if not frequency_range.lower <= DESIRED_FREQUENCY <= frequency_range.upper:
        print(
            FORMAT_ERROR_MESSAGE_FUNCTION.format(
                desired_prop_name="frequency",
                desired_val=DESIRED_FREQUENCY,
                function_name=DESIRED_FUNCTION.name,
                lower=frequency_range.lower,
                upper=frequency_range.upper,
            )
        )

    # Get the amplitude constraints.
    amplitude_range = awg5k_constraints_function.amplitude_range

    # Print a message if the desired amplitude is not within the amplitude constraints.
    if not amplitude_range.lower <= DESIRED_AMPLITUDE <= amplitude_range.upper:
        print(
            FORMAT_ERROR_MESSAGE_FUNCTION.format(
                desired_prop_name="amplitude",
                desired_val=DESIRED_AMPLITUDE,
                function_name=DESIRED_FUNCTION.name,
                lower=amplitude_range.lower,
                upper=amplitude_range.upper,
            )
        )

    # Get the device constraints for generating the desired waveform length on an AWG5K.
    awg5k_constraints_waveform_length = awg5k.get_waveform_constraints(
        waveform_length=DESIRED_WAVEFORM_LENGTH
    )

    # Get the frequency constraints.
    sample_rate_range = awg5k_constraints_waveform_length.sample_rate_range

    # Print a message if the desired sample rate is not within the sample rate constraints.
    if not sample_rate_range.lower <= DESIRED_SAMPLE_RATE <= sample_rate_range.upper:
        print(
            FORMAT_ERROR_MESSAGE_WAVEFORM_LENGTH.format(
                desired_prop_name="sample rate",
                desired_val=DESIRED_SAMPLE_RATE,
                waveform_length=DESIRED_WAVEFORM_LENGTH,
                lower=sample_rate_range.lower,
                upper=sample_rate_range.upper,
            )
        )
