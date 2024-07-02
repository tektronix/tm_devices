# Signal Generation

An overview of the signal generation functionality available in this package, along with information about Tektronix signal generators.

---

## Function Generation

A function is a limited set of common waveforms that are provided by default through the instrument.
The simplicity of these waveforms allows for output parameters like waveform length and sample rate to be
abstracted away. Frequency replaces these in order to provide signals which are easy to quantify and manipulate.

Arbitrary Function Generators (\[AFGs\](default: AFG)) utilize a phase increment process and a data lookup table to provide variable frequencies.
The phase increment calculated is dependent on the waveform length and frequency requested. This has
a side effect where the phase increment can be larger than one index in the lookup table. Functions bypass this
issue by being simplistic enough that waveform length reduction doesn't have a detrimental effect on the end output.

Arbitrary Waveform Generators (\[AWGs\](default: AWG)) enforce one cycle per sample, allowing the output to be the same shape regardless of clock rate.
The number of samples that occurs during a second is referred to as a sample per second (S/s), a unit which determines the frequency of the waveform.
With low frequency functions, \[AWGs\](default: AWG) are functionally identical to \[AFGs\](default: AFG), besides offering more constrained amplitudes and offsets.

---

### Class Structure

```{mermaid}
classDiagram
    direction LR

    SignalGeneratorMixin <|-- Tekscope
    SignalGeneratorMixin <|-- AFG
    SignalGeneratorMixin <|-- AWG

```

The [`SignalGenerator`][tm_devices.drivers.pi.signal_generators.signal_generator.SignalGenerator] class is responsible
for most waveform generators, including the [`AFG`][tm_devices.drivers.pi.signal_generators.afgs.afg.AFG] and
[`AWG`][tm_devices.drivers.pi.signal_generators.awgs.awg.AWG>].
Similarly, [`TekScope`][tm_devices.drivers.pi.scopes.tekscope.tekscope.TekScope>] is responsible for the
<AFG:> internal to the scopes themselves, commonly referred to as
an <IAFG:>. All of these classes inherit
[`SignalGeneratorMixin`][tm_devices.driver_mixins.signal_generator_mixin.SignalGeneratorMixin],
which includes a list of methods which share
functionality throughout all signal generators.

```{note}
[`SignalGeneratorMixin`][tm_devices.driver_mixins.signal_generator_mixin.SignalGeneratorMixin>]
only contains abstract methods; defining the class by itself and calling
methods in it will only raise `NotImplemented` errors.
```

```{mermaid}
classDiagram
    direction LR

    Tekscope <|-- InternalAFGChannel
    AFG <|-- AFGSourceChannel

    AWG <|-- AWGSourceChannel
    AWGSourceChannel <|-- AWG5KSourceChannel
    AWG5KSourceChannel <|-- AWG7KSourceChannel
    AWGSourceChannel <|-- AWG5200SourceChannel
    AWGSourceChannel <|-- AWG70KSourceChannel
```

Each [`SignalGenerator`][tm_devices.drivers.pi.signal_generators.signal_generator.SignalGenerator] class(
[`AFG`][tm_devices.drivers.pi.signal_generators.afgs.afg.AFG],
[`AWG`][tm_devices.drivers.pi.signal_generators.awgs.awg.AWG]) and
[`TekScope`][tm_devices.drivers.pi.scopes.tekscope.tekscope.TekScope]
(if the <AFG:> license is installed) will contain a dictionary of source channel classes,
which are defined on first access.
Each of these source channel classes (
[`AFGSourceChannel`][tm_devices.drivers.pi.signal_generators.afgs.afg.AFGSourceChannel],
[`AWGSourceChannel`][tm_devices.drivers.pi.signal_generators.awgs.awg.AWGSourceChannel], and
[`InternalAFGChannel`][tm_devices.drivers.pi.scopes.tekscope.tekscope.InternalAFGChannel]
) represents an output on the signal generator
(or the <IAFG:> in the case of an oscilloscope).

These source channel classes contain methods and properties which pertain to <PI:> commands which only apply changes to one output.
For example: the `afg.source_channel\["SOURCE1"\].set_amplitude()` call will change the amplitude only for source output 1.

```{tip}
The source channel classes not only provide easy access to basic <SCPI:> commands, but also helper functions, like `set_function_properties()`
```

---

### SignalGeneratorMixin Methods

```{warning}
Each method performs little to no validation, as the end user can change aspects outside its purview.
There are several distinct instances where this can cause unwanted behavior, depending on the signal generator and what
state it was in previously. Attempting validation when changes can occur outside its scope leads to many redundant checks.
As such, it is up to the user to implement these checks.
```

Each class has children which inherit the base abstracted methods. These methods are tailored to each signal generator so the
methods handle similarly, regardless of the different <PI:> commands required.

- `source_device_constants` is a property which holds information about what functions
    and memory sizes are allowed.

```{tip}
`source_device_constants.functions` will provide an enum of possible functions to generate on the current signal generator.
```

`generate_function()` is a method which allows for the user to request a function from
any source channel, provided an amplitude, frequency and offset is supplied. Other key features
include the ability to manipulate specific aspects of certain functions. Ramp waveforms can have their symmetry changed
and duty cycle can be altered for pulse functions. The termination of the <IAFG:> and any <AFG:> can be
specified using `HIGHZ` or `FIFTY` string literals. If the output needs to be inverted,
the polarity can be changed on \[AFGs\](default: AFG).

```{warning}
`generate_function()` allows function parameters which can exceed actual generation bounds.
`get_waveform_constraints()` should be used in tandem with `generate_function()`, or utilizing the constraints provided in
[Signal Generators](#signal-generators).
```

The `setup_burst()` method places the signal generator into a state for waveforms to be generated a set number
of times. All parameters passed into the method are functionally identical to `generate_function()`, besides `burst_count`.
`burst_count` specifies how many cycles of the waveform are to be generated.

```{warning}
`setup_burst()` will set parameters which can affect the signal generators behavior. Changing these parameters
manually will likely cause burst to stop functioning.
```

`generate_burst()`  writes a trigger to the signal generator, initiating the generation of a burst of waveforms.

`get_waveform_constraints()` will return a series of ranges that a waveform's parameters must
be within to be generated. These constraints can be used before generating a function to
make sure that the parameters you will be supplying
are not outside the bounds. The method only requires the desired waveform function (except on \[AWGs\](default: AWG)) to be provided.
However, different aspects may need to be provided to get a more accurate representation of what can actually be generated.
If no other inputs are provided, the smallest range of the attribute is chosen.
An \[AWG's\](default: AWG) signal path affects the range of the offset and amplitude.
Higher frequencies on \[AFGs\](default: AFG) will lower the upper bound of the amplitude,
alongside the which impedance is set.

`set_waveform_properties()` is functionally identical to `generate_function()`, but does not turn the
source channel off or on, nor will it stop or start an <AWG:>.

## Signal Generators

An overview of the different signal generators which are available in `tm_devices`.
This includes:

- Features unique to each which should be kept in mind.
- Constraints for each waveform parameter.

---

### TekScope Internal Arbitrary Function Generators

```{autoclasstree} tm_devices.drivers.pi.scopes.tekscope
---
full:
namespace: tm_devices.drivers.pi.scopes.tekscope
align: center
alt: Tekscope `IAFG` Class Diagram
---
```

The TekScope series instruments are signal generators focused on waveform generation which operate on the Windows operating systems.
They accept communication through <USB:> and <TCPIP:> interfaces.

Requesting function generation on an <IAFG:> will initially turn it off. The frequency, offset,
function, impedance, and amplitude are set in the stated order.
If the function is a `SQUARE` wave, the duty cycle is used
to set how long the pulses are. Symmetry decides what direction the `RAMP` function
skews. After all parameters are set, the source channel is then turned back on.

Setting up bursts of the <IAFG:> involves setting it to burst mode and loading in a specified number of bursts.

IAFGs have access to the following functions, listed within
[`SignalGeneratorFunctionsIAFG`][tm_devices.helpers.enums.SignalGeneratorFunctionsIAFG]:
`SIN`, `SQUARE`, `RAMP`, `PULSE`, `PRNOISE`, `DC`, `SINC`, `GAUSSIAN`, `LORENTZ`, `ERISE`, `EDECAY`, `HAVERSINE`, `CARDIAC`, `ARBITRARY`

```{note}
[IAFGs](default: IAFG) are only accessible if the oscilloscope has the `AFG` license installed.
```

```{note}
[IAFGs](default: IAFG) contain no waveform list, editable memory or user defined waveforms. This means arbitrary waveforms
must be loaded from the hard drive.
```

```{note}
Some functions, like `SINC`, `GAUSSIAN`, `LORENTZ`, `ERISE`, `EDECAY` and `HAVERSINE` already have an inbuilt offset.
```

```{note}
If the output termination matching is set to FIFTY instead of HIGHZ, then the offset and amplitude bounds will be halved.
```

```{caution}
Although `ARBITRARY` is a valid function, it will not generate properly when using `generate_function()`.
```

#### MSO2, MSO4, MSO4B, MSO5, MSO5LP, MSO6, MSO6B, LPD6

##### Constraints:

The amplitude and frequency range for the <IAFG:> varies based on the desired function.
These ranges are the same for each of the classes listed:
[`MSO2`][tm_devices.drivers.pi.scopes.tekscope.mso2.MSO2]
[`MSO4`][tm_devices.drivers.pi.scopes.tekscope.mso4.MSO4]
[`MSO4B`][tm_devices.drivers.pi.scopes.tekscope.mso4b.MSO4B]
[`MSO5`][tm_devices.drivers.pi.scopes.tekscope.mso5.MSO5]
[`MSO5LP`][tm_devices.drivers.pi.scopes.tekscope.mso5.MSO5LP]
[`MSO6`][tm_devices.drivers.pi.scopes.tekscope.mso6.MSO6]
[`MSO6B`][tm_devices.drivers.pi.scopes.tekscope.mso6b.MSO6B]
[`LPD6`][tm_devices.drivers.pi.scopes.tekscope.lpd6.LPD6]

Sample rates are 250.0MS/s for `ARBITRARY` waveforms.

```{table} IAFG Constraints
---
widths: auto
width: 50%
align: center
---
|                                          | Sin                                          | Square<br/>Pulse<br/>Arbitrary                | Ramp<br/>Triangle<br/>Cardiac               | Sinc                                        | Gaussian<br/>Haversine                      | Lorentz                                     |
|------------------------------------------|----------------------------------------------|-----------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|
| <span style="font-size:0.7em;">Frequency | <span style="font-size:0.7em;">0.1Hz–50.0MHz | <span style="font-size:0.7em;">0.1Hz–25.0MHz  | <span style="font-size:0.7em;">0.1Hz–0.5MHz | <span style="font-size:0.7em;">0.1Hz–2.0MHz | <span style="font-size:0.7em;">0.1Hz–5.0MHz | <span style="font-size:0.7em;">0.1Hz–5.0MHz |
| <span style="font-size:0.7em;">Amplitude | <span style="font-size:0.7em;">20.0mV–5.0V   | <span style="font-size:0.7em;">20.0mV–5.0V    | <span style="font-size:0.7em;">20.0mV–5.0V  | <span style="font-size:0.7em;">20.0mV–3.0V  | <span style="font-size:0.7em;">20.0mV–5.0V  | <span style="font-size:0.7em;">20.0mV–2.4V  |
| <span style="font-size:0.7em;">Offset    | <span style="font-size:0.7em;">-2.5V–2.5V    | <span style="font-size:0.7em;">-2.5V–2.5V     | <span style="font-size:0.7em;">-2.5V–2.5V   | <span style="font-size:0.7em;">-2.5V–2.5V   | <span style="font-size:0.7em;">-2.5V–2.5V   | <span style="font-size:0.7em;">-2.5V–2.5V   |
```

#### MSO5B

##### Constraints:

The constraints for the [`MSO5B`][tm_devices.drivers.pi.scopes.tekscope.mso5b.MSO5B] are identical to
[other tekscope models](#mso2-mso4-mso4b-mso5-mso5lp-mso6-mso6b-lpd6), except the upper frequency bound is doubled.

---

### Arbitrary Function Generators

```{autoclasstree} tm_devices.drivers.pi.signal_generators.afgs
---
full:
namespace: tm_devices.drivers.pi.signal_generators.afgs
align: center
alt: AFG Class Diagram
---
```

\[AFGs\](default: AFG) handle [function generation](#tekscope-internal-arbitrary-function-generators) identically to <IAFG:>,
except for the order in which the parameters are set.

All functions which are shared by each <AFG:> exist within the
[`AFG`][tm_devices.drivers.pi.signal_generators.afgs.afg.AFG] class.

Setting up bursts of the <AFG:> involves setting the <AFG:> trigger to external, so the burst doesn't activate
on the internal trigger. Following this, the burst state is set to `ON` and mode set to `TRIGGERED`.

\[AFGs\](default: AFG) have access to the following functions, listed within
[`SignalGeneratorFunctionsAFG`][tm_devices.helpers.enums.SignalGeneratorFunctionsAFG]:
`SIN`, `SQUARE`, `RAMP`, `PULSE`, `DC`, `SINC`, `GAUSSIAN`, `LORENTZ`, `ERISE`, `EDECAY`, `HAVERSINE`, `CARDIAC`, `NOISE`, `ARBITRARY`

```{note}
If the output termination matching is set to 50.0Ω instead of INFINITY, then the offset and amplitude bounds will be halved.
```

```{caution}
Although `Arbitrary` is a valid function, it will not generate properly when using `generate_function`.
```

#### AFG3K, AFG3KB, AFG3KC

The AFG3K series instruments are function generating devices that also offer the capacity to generate arbitrary waveforms. They accept
communication through <USB:>, <TCPIP:> and <GPIB:> interfaces. These instruments have their
own class representations, corresponding to the
[`AFG3K`][tm_devices.drivers.pi.signal_generators.afgs.afg3k.AFG3K],
[`AFG3KB`][tm_devices.drivers.pi.signal_generators.afgs.afg3kb.AFG3KB], and
[`AFG3KC`][tm_devices.drivers.pi.signal_generators.afgs.afg3kc.AFG3KC].

##### Constraints:

The amplitude, offset, and frequency range for AFG3Ks is extremely varied dependent on model number, frequency, and function.
However, the sample rate of the entire AFG3K series is 250.0MS/s.

```{table} AFG3K Constraints
---
widths: auto
width: 50%
align: center
---
|                                          | Sin                                              | Square                                             | Pulse                                              | Ramp<br/>Sinc<br/>Gaussian<br/>Lorentz<br/>ERise<br/>EDecay<br/>Haversine | Arbitrary                                     |
|------------------------------------------|--------------------------------------------------|----------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------|
| **3011/C:**                              |                                                  |                                                    |                                                    |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency | <span style="font-size:0.7em;">1.0µHz–10.0MHz    | <span style="font-size:0.7em;">1.0µHz–5.0MHz       | <span style="font-size:0.7em;">1.0mHz–5.0MHz       | <span style="font-size:0.7em;">1.0µHz–0.1MHz                              | <span style="font-size:0.7em;">1.0mHz–5.0MHz  |
| <span style="font-size:0.7em;">Amplitude | <span style="font-size:0.7em;">40.0mV–40.0V      | <span style="font-size:0.7em;">40.0mV–40.0V        | <span style="font-size:0.7em;">40.0mV–40.0V        | <span style="font-size:0.7em;">40.0mV–40.0V                               | <span style="font-size:0.7em;">40.0mV–40.0V   |
| <span style="font-size:0.7em;">Offset    | <span style="font-size:0.7em;">-20.0V–20.0V      | <span style="font-size:0.7em;">-20.0V–20.0V        | <span style="font-size:0.7em;">-20.0V–20.0V        | <span style="font-size:0.7em;">-20.0V–20.0V                               | <span style="font-size:0.7em;">-20.0V–20.0V   |
| **302xB/C:**                             |                                                  |                                                    |                                                    |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency | <span style="font-size:0.7em;">1.0µHz–25.0MHz    | <span style="font-size:0.7em;">1.0µHz–25.0MHz[^TA] | <span style="font-size:0.7em;">1.0mHz–25.0MHz[^TA] | <span style="font-size:0.7em;">1.0µHz–0.5MHz[^TA]                         | <span style="font-size:0.7em;">1.0mHz–12.5MHz |
| <span style="font-size:0.7em;">Amplitude | <span style="font-size:0.7em;">20.0mV–20V        | <span style="font-size:0.7em;">20.0mV–20.0V        | <span style="font-size:0.7em;">20.0mV–20.0V        | <span style="font-size:0.7em;">20.0mV–20.0V                               | <span style="font-size:0.7em;">20.0mV–20.0V   |
| <span style="font-size:0.7em;">Offset    | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V        | <span style="font-size:0.7em;">-10.0V–10.0V        | <span style="font-size:0.7em;">-10.0V–10.0V                               | <span style="font-size:0.7em;">-10.0V–10.0V   |
| **305xC:**                               |                                                  |                                                    |                                                    |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency | <span style="font-size:0.7em;">1.0µHz–50MHz      | <span style="font-size:0.7em;">1.0µHz–40.0MHz      | <span style="font-size:0.7em;">1.0mHz–40.0MHz      | <span style="font-size:0.7em;">1.0µHz–0.8MHz                              | <span style="font-size:0.7em;">1.0mHz–25.0MHz |
| <span style="font-size:0.7em;">Amplitude | <span style="font-size:0.7em;">20.0mV–20.0V      | <span style="font-size:0.7em;">20.0mV–20.0V        | <span style="font-size:0.7em;">20.0mV–20.0V        | <span style="font-size:0.7em;">20.0mV–20.0V                               | <span style="font-size:0.7em;">20.0mV–20.0V   |
| <span style="font-size:0.7em;">Offset    | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V        | <span style="font-size:0.7em;">-10.0V–10.0V        | <span style="font-size:0.7em;">-10.0V–10.0V                               | <span style="font-size:0.7em;">-10.0V–10.0V   |
| **310x/C:**                              |                                                  |                                                    |                                                    |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency | <span style="font-size:0.7em;">1.0µHz–0.1GHz     | <span style="font-size:0.7em;">1.0µHz–50.0MHz      | <span style="font-size:0.7em;">1.0mHz–50.0MHz      | <span style="font-size:0.7em;">1.0µHz–1.0MHz                              | <span style="font-size:0.7em;">1.0mHz–50.0MHz |
| <span style="font-size:0.7em;">Amplitude | <span style="font-size:0.7em;">40.0mV–20.0V      | <span style="font-size:0.7em;">40.0mV–20.0V        | <span style="font-size:0.7em;">40.0mV–20.0V        | <span style="font-size:0.7em;">4.0mV–20.0V                                | <span style="font-size:0.7em;">40.0mV–20.0V   |
| <span style="font-size:0.7em;">Offset    | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V        | <span style="font-size:0.7em;">-10.0V–10.0V        | <span style="font-size:0.7em;">-10.0V–10.0V                               | <span style="font-size:0.7em;">-10.0V–10.0V   |
| **315xC:**                               |                                                  |                                                    |                                                    |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency | <span style="font-size:0.7em;">1.0µHz–0.15GHz    | <span style="font-size:0.7em;">1.0µHz–0.1GHz       | <span style="font-size:0.7em;">1.0mHz–0.1GHz       | <span style="font-size:0.7em;">1.0µHz–1.5MHz                              | <span style="font-size:0.7em;">1.0mHz–0.1GHz  |
| <span style="font-size:0.7em;">Amplitude | <span style="font-size:0.7em;">40.0mV–20.0V[^TB] | <span style="font-size:0.7em;">40.0mV–20.0V        | <span style="font-size:0.7em;">40.0mV–20.0V        | <span style="font-size:0.7em;">40.0mV–20.0V                               | <span style="font-size:0.7em;">40.0mV–20.0V   |
| <span style="font-size:0.7em;">Offset    | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V        | <span style="font-size:0.7em;">-10.0V–10.0V        | <span style="font-size:0.7em;">-10.0V–10.0V                               | <span style="font-size:0.7em;">-10.0V–10.0V   |
| **325x/C:**                              |                                                  |                                                    |                                                    |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency | <span style="font-size:0.7em;">1.0µHz–0.24GHz    | <span style="font-size:0.7em;">1.0µHz–0.12GHz      | <span style="font-size:0.7em;">1.0mHz–0.12GHz      | <span style="font-size:0.7em;">1.0µHz–2.4MHz                              | <span style="font-size:0.7em;">1.0mHz–0.12GHz |
| <span style="font-size:0.7em;">Amplitude | <span style="font-size:0.7em;">0.1V–10.0V[^TC]   | <span style="font-size:0.7em;">0.1V–10.0V          | <span style="font-size:0.7em;">0.1V–10.0V          | <span style="font-size:0.7em;">0.1V–10.0V                                 | <span style="font-size:0.7em;">0.1V–10.0V     |
| <span style="font-size:0.7em;">Offset    | <span style="font-size:0.7em;">-5.0V–5.0V        | <span style="font-size:0.7em;">-5.0V–5.0V          | <span style="font-size:0.7em;"> -5.0V–5.0V         | <span style="font-size:0.7em;">-5.0V–5.0V                                 | <span style="font-size:0.7em;">-5.0V–5.0V     |

[^TA]: AFG302xB has its upper bound for frequency halved for these functions.

[^TB]: Amplitude upper bound is reduced to 16.0V when frequency is greater than 100.0MHz.

[^TC]: Amplitude upper bound is reduced to 8.0V when frequency is greater than 200.0MHz.

```

#### AFG31K

The AFG31K series instruments are function generating devices that also offer the capacity to generate arbitrary waveforms. They accept
communication through <USB:>, <TCPIP:>, and <GPIB:> interfaces. The AFG31K has its
own class representation, corresponding to
[`AFG31K`][tm_devices.drivers.pi.signal_generators.afgs.afg31k.AFG31K].

##### Constraints:

```{table} AFG31K Constraints
---
widths: auto
align: center
---
|                                            | Sin                                              | Square<br/>Pulse                                 | Pulse                                         | Ramp<br/>Sinc<br/>Gaussian<br/>Lorentz<br/>ERise<br/>EDecay<br/>Haversine | Arbitrary                                     |
|--------------------------------------------|--------------------------------------------------|--------------------------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------|
| **3102x:**                                 |                                                  |                                                  |                                               |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency   | <span style="font-size:0.7em;">1.0µHz–25.0MHz    | <span style="font-size:0.7em;">1.0µHz–20.0MHz    | <span style="font-size:0.7em;">1.0m–25.0MHz   | <span style="font-size:0.7em;">1.0µHz–0.5MHz                              | <span style="font-size:0.7em;">1.0mHz–12.5MHz |
| <span style="font-size:0.7em;">Amplitude   | <span style="font-size:0.7em;">2.0mV–20.0V       | <span style="font-size:0.7em;">2.0mV–20.0V       | <span style="font-size:0.7em;">2.0mV–20.0V    | <span style="font-size:0.7em;">2.0mV–20.0V                                | <span style="font-size:0.7em;">2.0mV–20.0V    |
| <span style="font-size:0.7em;">Offset      | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V   | <span style="font-size:0.7em;">-10.0V–10.0V                               | <span style="font-size:0.7em;">-10.0V–10.0V   |
| <span style="font-size:0.7em;">Sample Rate |                                                  |                                                  |                                               |                                                                           | <span style="font-size:0.7em;">250.0MS/s      |
| **3105x:**                                 |                                                  |                                                  |                                               |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency   | <span style="font-size:0.7em;">1.0µHz–50.0MHz    | <span style="font-size:0.7em;">1.0µHz–40.0MHz    | <span style="font-size:0.7em;">1.0mHz–40.0MHz | <span style="font-size:0.7em;">1.0µHz–0.8MHz                              | <span style="font-size:0.7em;">1.0mHz–25.0MHz |
| <span style="font-size:0.7em;">Amplitude   | <span style="font-size:0.7em;">2.0mV–20.0V       | <span style="font-size:0.7em;">2.0mV–20.0V       | <span style="font-size:0.7em;">2.0mV–20.0V    | <span style="font-size:0.7em;">2.0Vm–20.0V                                | <span style="font-size:0.7em;">2.0mV–20.0V    |
| <span style="font-size:0.7em;">Offset      | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V   | <span style="font-size:0.7em;">-10.0V–10.0V                               | <span style="font-size:0.7em;">-10.0V–10.0V   |
| <span style="font-size:0.7em;">Sample Rate |                                                  |                                                  |                                               |                                                                           | <span style="font-size:0.7em;">1.0GS/s[^TOA]  |
| **3110x:**                                 |                                                  |                                                  |                                               |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency   | <span style="font-size:0.7em;">1.0µHz–0.1GHz     | <span style="font-size:0.7em;">1.0µHz–80.0MHz    | <span style="font-size:0.7em;">1.0mHz–50.0MHz | <span style="font-size:0.7em;">1.0µHz–1.0MHz                              | <span style="font-size:0.7em;">1.0mHz–50.0MHz |
| <span style="font-size:0.7em;">Amplitude   | <span style="font-size:0.7em;">2.0mV–20.0V[^TOB] | <span style="font-size:0.7em;">2.0mV–20.0V[^TOB] | <span style="font-size:0.7em;">2.0mV–20.0V    | <span style="font-size:0.7em;">2.0Vm–20.0V                                | <span style="font-size:0.7em;">2.0mV–20.0V    |
| <span style="font-size:0.7em;">Offset      | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V      | <span style="font-size:0.7em;">-10.0V–10.0V   | <span style="font-size:0.7em;">-10.0V–10.0V                               | <span style="font-size:0.7em;">-10.0V–10.0V   |
| <span style="font-size:0.7em;">Sample Rate |                                                  |                                                  |                                               |                                                                           | <span style="font-size:0.7em;">1.0GS/s[^TOA]  |
| **3115x:**                                 |                                                  |                                                  |                                               |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency   | <span style="font-size:0.7em;">1.0µHz–0.15GHz    | <span style="font-size:0.7em;">1.0µHz–0.12G      | <span style="font-size:0.7em;">1mHz–0.1GHz    | <span style="font-size:0.7em;">1.0µHz–1.5MHz                              | <span style="font-size:0.7em;">1.0mHz–75.0MHz |
| <span style="font-size:0.7em;">Amplitude   | <span style="font-size:0.7em;">2.0mV–10.0V       | <span style="font-size:0.7em;">2.0mV–10.0V       | <span style="font-size:0.7em;">2mV–10V        | <span style="font-size:0.7em;">2.0Vm–10.0V                                | <span style="font-size:0.7em;">2.0mV–10.0V    |
| <span style="font-size:0.7em;">Offset      | <span style="font-size:0.7em;">-5.0V–5.0V        | <span style="font-size:0.7em;">-5.0V–5.0V        | <span style="font-size:0.7em;">-5V–5V         | <span style="font-size:0.7em;">-5.0V–5.0V                                 | <span style="font-size:0.7em;">-5.0V–5.0V     |
| <span style="font-size:0.7em;">Sample Rate |                                                  |                                                  |                                               |                                                                           | <span style="font-size:0.7em;">2.0GS/s[^TOA]  |
| **3125x:**                                 |                                                  |                                                  |                                               |                                                                           |                                               |
| <span style="font-size:0.7em;">Frequency   | <span style="font-size:0.7em;">1.0µHz–0.25GHz    | <span style="font-size:0.7em;">1.0µHz–0.16GHz    | <span style="font-size:0.7em;">1mHz–0.12GHz   | <span style="font-size:0.7em;">1.0µHz–2.5MHz                              | <span style="font-size:0.7em;">1.0m–0.125G    |
| <span style="font-size:0.7em;">Amplitude   | <span style="font-size:0.7em;">2.0mV–10.0V[^TOC] | <span style="font-size:0.7em;">2.0mV–10.0V       | <span style="font-size:0.7em;">2mV–10V        | <span style="font-size:0.7em;">2.0Vm–10.0V                                | <span style="font-size:0.7em;">2.0mV–10.0V    |
| <span style="font-size:0.7em;">Offset      | <span style="font-size:0.7em;">-5.0V–5.0V        | <span style="font-size:0.7em;">-5.0V–5.0V        | <span style="font-size:0.7em;">-5V–5V         | <span style="font-size:0.7em;">-5.0V–5.0V                                 | <span style="font-size:0.7em;">-5.0V–5.0V     |
| <span style="font-size:0.7em;">Sample Rate |                                                  |                                                  |                                               |                                                                           | <span style="font-size:0.7em;">2.0GS/s[^TOA]  |

[^TOA]: When waveform length is greater than 16Kb, otherwise, the sample rate is 250.0MS/s.

[^TOB]: Amplitude upper bound is reduced to 16.0V when the frequency is greater than 60.0MHz. It is further reduced to 12.0V when the frequency is greater than 80.0MHz

[^TOC]: Amplitude upper bound is reduced to 8.0V when the frequency is greater than 200.0MHz.

```

---

### Arbitrary Waveform Generators

```{autoclasstree} tm_devices.drivers.pi.signal_generators.awgs
---
full:
namespace: tm_devices.drivers.pi.signal_generators.awgs
align: center
alt: AWG Class Diagram
---
```

All functions which are shared by each <AWG:> exist within the
[`AWG`][tm_devices.drivers.pi.signal_generators.awgs.awg.AWG] class.

Function generation on \[AWGs\](default: AWG) is fundamentally different from \[AFGs\](default: AFG). The <AWG:> is stopped and the source channel being used
is turned off. Predefined waveforms provided with the <AWG:>
are then loaded from the hard drive into the waveform list for the AWG5200 and AWG70K. Sample rate is not source dependant,
instead it is set through the `SignalGenerator` class. The source channel provided has its waveform, offset, amplitude, and signal path set.
These attributes can take a while to be set, though once complete, the source channels are turned back on and `AWGCONTROL:RUN`
is sent to begin the transmission of the waveform.

```{note}
If the waveform is `RAMP`, a symmetry of 50 will set the waveform to a `TRIANGLE`.
```

The [`AWG`][tm_devices.drivers.pi.signal_generators.awgs.awg.AWG] class has some unique methods.
`generate_waveform()` allows for a waveform name from the waveform list
to be provided, instead of a function. The method is also distinctly different from generate function as it relies on a sample
rate also being provided to actually generate the waveform. All functions which are generic to the <AWG:>
exist within the [`AWG`][tm_devices.drivers.pi.signal_generators.awgs.awg.AWG] class.

\[AWGs\](default: AWG) have access to the following functions, listed within
[`SignalGeneratorFunctionsAWG`][tm_devices.helpers.enums.SignalGeneratorFunctionsAWG]:
`SIN`, `SQUARE`, `RAMP`, `TRIANGLE`, `DC`, `CLOCK`

#### AWG5K/AWG7K

The AWG5K/7K series instruments are signal generators focused on waveform generation which operate on Windows.
They accept communication through <TCPIP:> and <GPIB:> interfaces.

`set_output_signal_path()` is uniquely defined within the AWG5K and AWG7K classes, as it will set the value for
`AWGCONTROL:DOUTPUTx:STATE`, which is a unique option not seen in the other \[AWGs\](default: AWG).

`set_offset()` is conditioned to make sure that the <AWG:> output signal path is not DIR, as the <VISA:> query will time
out otherwise.

```{note}
Operation complete commands will always return 1 on the AWG5K/7K series.
```

```{caution}
All waveforms must be the same length when sending the AWGCONTROL:RUN command.
```

##### AWG5K, AWG5KB, AWG5KC

The AWG5K series instruments have their
own class representations, corresponding to the
[`AWG5K`][tm_devices.drivers.pi.signal_generators.awgs.awg5k.AWG5K],
[`AWG5KB`][tm_devices.drivers.pi.signal_generators.awgs.awg5kb.AWG5KB], and
[`AWG5KC`][tm_devices.drivers.pi.signal_generators.awgs.awg5kc.AWG5KC].

###### Constraints:

The AWG5K series offers an upper sample rate range from 600.0MS/s to 1.2GS/s dependent on the model number.
Sending `AWGControl:DOUTput[n] 1` or using `DIR` in `set_output_signal_path()` will reduce the maximum amplitude
to 0.6V. This occurs by bypassing the internal amplifier, which reroutes the <DAC:> directly to the
differential output.

```{table} AWG5K Constraints
---
widths: auto
width: 50%
align: center
---
|                                             | 500x/B/C                                          | 501x/B/C                                        | 5xxx/B/C DIR                                 |
|---------------------------------------------|---------------------------------------------------|-------------------------------------------------|----------------------------------------------|
| <span style="font-size:0.7em;">Sample Rate  | <span style="font-size:0.7em;">10.0MS/s–600.0MS/s | <span style="font-size:0.7em;">10.0MS/s–1.2MS/s | *                                            |
| <span style="font-size:0.7em;">Amplitude    | <span style="font-size:0.7em;">20.0mV–2.25V       | <span style="font-size:0.7em;">20.0mV–2.25V     | <span style="font-size:0.7em;">20.0mV-0.6.0V |
| <span style="font-size:0.7em;">Offset       | <span style="font-size:0.7em;">-2.25V–2.25V       | <span style="font-size:0.7em;">-2.25V–2.25V     | <span style="font-size:0.7em;">N/A           |

```

```{note}
AWG5K's have digitized outputs on the rear of the device.
```

##### AWG7K, AWG7KB, AWG7KC

The AWG7K series instruments have their
own class representations, corresponding to the
[`AWG7K`][tm_devices.drivers.pi.signal_generators.awgs.awg7k.AWG7K],
[`AWG7KB`][tm_devices.drivers.pi.signal_generators.awgs.awg7kb.AWG7KB], and
[`AWG7KC`][tm_devices.drivers.pi.signal_generators.awgs.awg7kc.AWG7KC].

###### Constraints:

The AWG7K series instruments functions identically to the AWG5K series,
excluding the higher sample rate, lower amplitude, and offset range.
The model number conveys information about the unit, with the second and third number indicating
the maximum sample rate in gigahertz allowed on the unit.

```{table} AWG7K Constraints
---
widths: auto
width: 50%
align: center
---
|                                            | 705x                                            | 710x                                             | 706xB                                           | 712xB/C                                          | 708xC                                           |
|--------------------------------------------|-------------------------------------------------|--------------------------------------------------|-------------------------------------------------|--------------------------------------------------|-------------------------------------------------|
| <span style="font-size:0.7em;">Sample Rate | <span style="font-size:0.7em;">10.0MS/s–5.0GS/s | <span style="font-size:0.7em;">10.0MS/s–10.0GS/s | <span style="font-size:0.7em;">10.0MS/s–6.0GS/s | <span style="font-size:0.7em;">10.0MS/s–12.0GS/s | <span style="font-size:0.7em;">10.0MS/s–8.0GS/s |
| <span style="font-size:0.7em;">Amplitude   | <span style="font-size:0.7em;">50.0mV–2.0V      | <span style="font-size:0.7em;">50.0mV–2.0V       | <span style="font-size:0.7em;">50.0mV–2.0V      | <span style="font-size:0.7em;">50.0mV–2.0V       | <span style="font-size:0.7em;">50.0mV–2.0V      |
| <span style="font-size:0.7em;">Offset      | <span style="font-size:0.7em;">-0.5V–0.5V       | <span style="font-size:0.7em;">-0.5V–0.5V        | <span style="font-size:0.7em;">-0.5V–0.5V       | <span style="font-size:0.7em;">-0.5V–0.5V        | <span style="font-size:0.7em;">-0.5V–0.5V       |

```

The AWG7K also includes varying options which directly affects these ranges, such as option 02 and 06.
These options will enforce the output signal path to always go directly from the <DAC:> to the differential output.

```{table} AWG7K Option Constraints
---
widths: auto
width: 50%
align: center
---
|                                            | 7102 OPT 06                                           | 7122B/C OPT 06                                        | 7xxx/B/C OPT 02                          | 7xxx/B/C DIR                               |
|--------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|------------------------------------------|--------------------------------------------|
| <span style="font-size:0.7em;">Sample Rate | <span style="font-size:0.7em;">10.0MS/s–20.0GS/s[^SA] | <span style="font-size:0.7em;">10.0MS/s–24.0GS/s[^SA] | *                                        | *                                          |
| <span style="font-size:0.7em;">Amplitude   | <span style="font-size:0.7em;">0.5V–1.0V              | <span style="font-size:0.7em;">0.5V–1.0V              | <span style="font-size:0.7em;">0.5V–1.0V | <span style="font-size:0.7em;">50.0mV-1.0V |
| <span style="font-size:0.7em;">Offset      | <span style="font-size:0.7em;">N/A                    | <span style="font-size:0.7em;">N/A                    | <span style="font-size:0.7em;">N/A       | <span style="font-size:0.7em;">N/A         |

[^SA]: Samples rates higher than 10GS/S(12GS/s for B/C) can only be done through Interleave.

```

#### AWG5200

The AWG5200 series instruments are signal generators focused on waveform generation which operate on Windows.
They accept communication through <USB:>, <TCPIP:>, and <GPIB:> interfaces.

The AWG52000 has its
own class representation, corresponding to
[`AWG5200`][tm_devices.drivers.pi.signal_generators.awgs.awg5200.AWG5200].

`set_output_signal_path()` is uniquely defined within the AWG5200 as it has special output signal paths.

`load_waveform()` inherently has an operation complete check as attempting to run overlapping commands while loading a waveform can lead to
unintended behavior.

##### Constraints:

The AWG5200 does not have a sample rate range dependent on model number. Instead, it refers to
which option is installed to provide the range of the sample rate. Option 25 on the devices provides
a maximum rate is 2.5GS/s, whereas option 50 allows a maximum rate of 5.0GS/s.
If option DC is provided, the DCHB signal output path will amplitude range will be increased to have a maximum
of 1.5V. The DCHV signal path increases this range further to 5.0V by including another amplifier.

```{table} AWG5200 Constraints
---
widths: auto
width: 50%
align: center
---
|                                            | OPT 25                                           | OPT 50                                           | OPT DC DCHB                                | OPT HV DCHV                                |
|--------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------|--------------------------------------------|
| <span style="font-size:0.7em;">Sample Rate | <span style="font-size:0.7em;">0.298kS/s–2.5GS/s | <span style="font-size:0.7em;">0.298kS/s–5.0GS/s | *                                          | *                                          |
| <span style="font-size:0.7em;">Amplitude   | <span style="font-size:0.7em;">25.0mV–0.75V      | <span style="font-size:0.7em;">25.0mV–0.75V      | <span style="font-size:0.7em;">25.0mV–1.5V | <span style="font-size:0.7em;">10.0mV-5.0V |
| <span style="font-size:0.7em;">Offset      | <span style="font-size:0.7em;">-2.0V–2.0V        | <span style="font-size:0.7em;">-2.0V–2.0V        | <span style="font-size:0.7em;">-2.0V–2.0V  | <span style="font-size:0.7em;">-2.0V-2.0V  |

```

##### Sequential, Blocking and Overlapping Commands:

The AWG5200's programming commands are seperated into three seperated categories: Sequential, Blocking, and Overlapping.
The type of command is important to consider, as using them in an incorrect order can lead to unintended results.

Sequential commands function as standard <PI:> commands. They will not start until the previous command has finished. These commands
tend to be fast and will allow for quick response times even if they are queued in the input buffer.

Blocking commands are very similar to Sequential commands. The main difference between Sequential and Blocking is that
Blocking commands often take longer to execute.

```{caution}
Due to the length of Blocking commands, a query may time out when sent if performed immediately after a large series of consecutive Blocking commands.
```

Some commands can perform data analysis on another thread, these are referred to as Overlapping commands. They allow any command to be started
while they are being executed. They cannot begin if the previous command was blocking or sequential, or if the operation complete status register is
not set.

```{tip}
Overlapping commands run in parallel with any other command, so placing them first in a sequence is always preferable.
```

```{tip}
There are multiple ways of synchronizing overlapping commands. This includes using <OPC:> or <WAI:> to
wait for the operation complete to clear in the <SESR:>. This can also be done using an <SRQ:>,
along with waiting for the trigger bit in the <OCR:>.
```

```{caution}
The operation complete register will only wait for the first overlapping command to finish before clearing. This means
that if multiple overlapping commands are run, then subsequent overlapping commands being finished will be ignored.
```

```{danger}
Overlapping commands can cause unintended behavior when performed alongside critical hardware functionality.
If the AWG5200 is experiencing problems, this may be a cause.
```

#### AWG70KA, AWG70KB

The AWG70K series instruments are signal generators focused on waveform generation which operate on Windows.
They accept communication through <USB:>, <TCPIP:>, and <GPIB:> interfaces.

`set_output_signal_path()` is uniquely defined within the
[`AWG70KA`][tm_devices.drivers.pi.signal_generators.awgs.awg70ka.AWG70KA] and
[`AWG70KB`][tm_devices.drivers.pi.signal_generators.awgs.awg70kb.AWG70KB] classes.
By default, it will first attempt to set the output signal path to <DCA:>.
If this fails (implying an MDC4500-4B is not connected), then a direct signal path will be set.

`set_offset()` is conditioned to make sure that the <AWG:> output signal path is <DCA:>, as the <VISA:> query will time
out otherwise.

##### Constraints:

The AWG70K signal generator is a special case, where only the direct signal output path is allowed
(unless option AC is installed). This means the amplitude is limited,
and offset is not allowed to be set by default. However, there is a secondary device which allows for DC amplification, the MDC4500-4B.
The MDC4500-4B is an amplifier which provides the ability to utilize DC offset on an AWG70K. It also provides a larger range of amplitude.

Just like the AWG5200, the frequency is dependent on the option installed (150, 225, 216, 208).
The first numbers in the option provides the number of source channels the AWG70K has, the next two numbers
indicate the sample rate in gigahertz.

```{tip}
Though the AWG70K has no offset by default, one can be simulated by changing the raw data in the waveform.
As long as all points are within the amplitude bounds, this can be achieved using `WLIST:WAVEFORM:AOFFSET`.
```

```{table} AWG70K Constraints
---
widths: auto
width: 50%
align: center
---
|                                            | OPT 150                                        | OPT 225                                          | OPT 216                                          | OPT 208                                         | MDC4500 DCA                                    |
|--------------------------------------------|------------------------------------------------|--------------------------------------------------|--------------------------------------------------|-------------------------------------------------|------------------------------------------------|
| <span style="font-size:0.7em;">Sample Rate | <span style="font-size:0.7em;">1.49kS/s–50GS/s | <span style="font-size:0.7em;">1.49kS/s–25.0GS/s | <span style="font-size:0.7em;">1.49kS/s–16.0GS/s | <span style="font-size:0.7em;">1.49kS/s–8.0GS/s | *                                              |
| <span style="font-size:0.7em;">Amplitude   | <span style="font-size:0.7em;">0.125V–0.5V     | <span style="font-size:0.7em;">0.125V–0.5V       | <span style="font-size:0.7em;">0.125V–0.5V       | <span style="font-size:0.7em;">0.125V–0.5V      | <span style="font-size:0.7em;">31mV–1.2V[^SZA] |
| <span style="font-size:0.7em;">Offset      | <span style="font-size:0.7em;">N/A             | <span style="font-size:0.7em;">N/A               | <span style="font-size:0.7em;">N/A               | <span style="font-size:0.7em;">N/A              | <span style="font-size:0.7em;">-0.4V–0.8V      |

[^SZA]: Although the MOD4500-4B allows for greater than 1.0V amplitude, there is a drop off in accuracy.

```

##### Sequential, Blocking and Overlapping Commands:

The AWG70K also supports the [Sequential, Blocking, and Overlapping commands](#awg5200) mentioned in
the AWG5200 section.
