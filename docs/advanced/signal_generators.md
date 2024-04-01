# Signal Generation

An overview of the signal generation in this package, along with information about Tektronix signal generators.

______________________________________________________________________

## Function Generation

A function is a limited set of common waveforms that are provided by default through the instrument.
The simplicity of these waveforms allows for output parameters like waveform length and sample rate to be
abstracted away. Frequency replaces these in order to provide signals which easy to quantify and manipulate.

Arbitrary Function Generators (AFGs) utilize a phase increment process and a data lookup table to provide variable frequencies.
The phase increment calculated is dependent on the waveform length and frequency requested. This has
a side effect where the phase increment can be larger than one index in the lookup table. Functions bypass this
issue by being simplistic enough that waveform length reduction doesn't have a detrimental effect on the end output.

Arbitrary Waveform Generators (AWGs) enforce one cycle per sample, allowing the output to be the same shape regardless of clock rate.
With low frequency functions, AWGs are functionally identical to AFGs, besides offering more constrained amplitudes and offsets.

______________________________________________________________________

### Class Structure

```{mermaid}
classDiagram
    direction LR

    SignalGeneratorMixin <|-- Tekscope
    SignalGeneratorMixin <|-- AFG
    SignalGeneratorMixin <|-- AWG

```

The `SignalGenerator` class is responsible for most waveform generators, including the `AWG` and `AFG`.
Similarly, `TekScope` is responsible for the AFG's internal to the scopes themselves, commonly referred to as
an IAFG. All of these classes inherit `SignalGeneratorMixin`, which includes a list of methods which share
functionality throughout all signal sources.

```{note}
SignalGeneratorMixin only contains abstract methods, defining the class by itself and calling methods in it will only raise NotImplemented errors.
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

Each Source class (`AFG`, `AWG`) and `Tekscope` (If the AFG license is installed) will contain a dictionary of source channel classes,
which are defined on first access. Each of these source channel classes represents an output on the source, or the IAFG in the case
of an oscilloscope.

These channels contain methods and properties which pertain to PI commands which only apply changes to one output channel.
For example: the afg.source_channel\["SOURCE1"\].set_amplitude() call will change the amplitude only for source output 1.

```{tip}
These channel classes not only provide easy access to basic scipy commands, but also helper functions, like `set_function_properties`
```

______________________________________________________________________

### Class Methods

```{warning}
Each method exclude most attempts at validation, as the end user can change aspects outside its purview.
There are several distinct instances where this can cause unwanted behavior, depending on the source and what
state it was in before it is used. Attempting validation when changes can occur outside it's scope leads to many redundant checks.
As such, it is up to the user to implement these checks.
```

Each class has children which inherit the base abstracted methods. These methods are tailored to each signal generator so the
methods handle similarly, regardless of the different PI commands required.

- `source_device_constants` is a property which holds information about what functions
  and memory sizes are allowed.

```{tip}
`source_device_constants.functions` will provide an enum of possible functions to generate on the signal generator used.
```

`generate_function` is a method which allows for the user to request a function from
any source channel provided an amplitude, frequency and offset is supplied. Other key features
include the ability to manipulate specific aspects of certain functions. Ramp waveforms can have their symmetry changed
and duty cycle can be altered for pulse functions. The termination of the IAFG and any AFG can be
specified using `HIGHZ` or `FIFTY` string literals. If the output needs to be inverted,
the polarity can be changed on AFGs.

```{warning}
`generate_function` allows function parameters which can exceed actual generation bounds.
`get_waveform_constraints` should be used in tandem with `generate_function`, or utilizing the constraints provided in
[Signal Generators](#signal-generators).
```

The `setup_burst` method places the source into a state for waveforms to be generated a set number
of times. All parameters passed into the method are functionally identical to generate_function, besides burst_count,
which specifies how many cycles of the waveform are to be generated.

```{warning}
`setup_burst` will set parameters which can effect the signal generators behavior. Changing these parameters
will likely cause burst to stop functioning.
```

`generate_burst`  writes a trigger to the source, initiating the generation of a burst of waveforms.

`get_waveform_constraints` will return a series of constraints that the signal generators must be within to be generated.
These constraints can be used before generating a function to make sure that the parameters you will be supplying
are not outside the bounds. The method only requires the function (except on AWGs) to be provided.
However, different aspects may need to be provided to get a more accurate representation of what can actually be generated.
If no other inputs are provided, the smallest range of the attribute is chosen.
AWGs signal path effects the range of the offset and amplitude.
Higher frequencies on AFGs will lower the upper bound of the amplitude,
alongside the which impedance is set.

`set_waveform_properties` is functionally identical to generate_function, but does not turn the channel
off or on, nor will it stop or start an AWG.

## Signal Generators

An overview of the different signal generators which are covered when using `tm_devices`.

______________________________________________________________________

## TekScope Internal Arbitrary Function Generators

```{autoclasstree} tm_devices.drivers.pi.scopes.tekscope
---
full:
namespace: tm_devices.drivers.pi.scopes.tekscope
align: center
alt: Complete device driver class diagram
---
```

Requesting function generation on an IAFG will initially turn it off. The frequency, offset,
function, impedance and amplitude are set in the stated order.
If the function is a `SQUARE` wave, the duty cycle is used
to set how long the pulses are. Symmetry decides what direction the skews towards if the `RAMP` function
is provided. After all parameters are set, the channel is then turned back on.

Setting up bursts of the IAFG involves setting it to burst mode and loading in a specified number of bursts.

AFGs have access to the following functions:
`SIN`, `SQUARE`, `RAMP`, `PULSE`, `PRNOISE`, `DC`, `SINC`, `GAUSSIAN`, `LORENTZ`, `ERISE`, `EDECAY`, `HAVERSINE`, `CARDIAC`, `ARBITRARY`

```{note}
IAFGs are only accessible if the oscilloscope has the AFG license installed.
```

```{note}
IAFGs contain no waveform list, editable memory or user defined waveforms. This means arbitrary waveforms
must be loaded from the hard drive.
```

```{note}
Some functions, like `SINC`, `GAUSSIAN`, `LORENTZ`, `ERISE`, `EDECAY` and `HAVERSINE` already have an inbuilt offset.
```

```{note}
If the output termination matching is set to FIFTY ohms instead of HIGHZ, then the offset and amplitude bounds will be halved.
```

```{caution}
Although `Arbitrary` is a valid function, it will not generate properly when using `generate_function`.
```

### MSO2, MSO4, MSO4B, MSO5, MSO5LP, MSO6, MSO6B, LPD6

#### Constraints:

The amplitude and frequency range for the Internal AFG varies on the function set.
All functions have the same lower bound, 20 mV and 100 mHz. Similarly, all offset ranges stay consistent,
plus or minus 2.5 volts along with all sample rates being 250 MHz.
The higher bound of amplitude and frequency, however, vary between functions.

```{table} IAFG Constraints
---
widths: auto
width: 50%
align: center
---
|                | Sin      | Square<br/>Pulse<br/>Arbitrary | Ramp<br/>Triangle<br/>Cardiac | Sinc     | Gaussian<br/>Haversine | Lorentz  |
| -------------- | -------- | ------------------------------ | ----------------------------- | -------- | ---------------------- | -------- |
| Frequency (Hz) | 0.1–50M  | 0.1–25M                        | 0.1–0.5M                      | 0.1–2M   | 0.1–5M                 | 0.1–5M   |
| Amplitude (V)  | 20m–5    | 20m–5                          | 20m–5                         | 20m–3    | 20m–5                  | 20m–2.4  |
| Offset (V)     | -2.5–2.5 | -2.5–2.5                       | -2.5–2.5                      | -2.5–2.5 | -2.5–2.5               | -2.5–2.5 |
```

### MSO5B

#### Constraints:

The constraints for the MSO5B are identical to [other tekscope models](#mso2-mso4-mso4b-mso5-mso5lp-mso6-mso6b-lpd6), except the upper frequency bound is doubled.

______________________________________________________________________

## Arbitrary Function Generators

```{autoclasstree} tm_devices.drivers.pi.signal_generators.afgs
---
full:
namespace: tm_devices.drivers.pi.signal_generators.afgs
align: center
alt: Complete device driver class diagram
---
```

AFGs handles function generation identically to [IAFGs](#tekscope-internal-arbitrary-function-generators),
besides the order in which the parameters are set.

Setting up bursts of the AFG involves setting the AFG trigger to external, so the burst doesn't activate
on the internal trigger. Following this, the burst state is set to `ON` and mode set to `TRIGGERED`.

AFGs have access to the following functions:
`SIN`, `SQUARE`, `RAMP`, `PULSE`, `DC`, `SINC`, `GAUSSIAN`, `LORENTZ`, `ERISE`, `EDECAY`, `HAVERSINE`, `CARDIAC`, `NOISE`, `ARBITRARY`

```{note}
If the output termination matching is set to 50 ohms instead of INFINITY, then the offset and amplitude bounds will be halved.
```

```{caution}
Although `Arbitrary` is a valid function, it will not generate properly when using `generate_function`.
```

### AFG3K, AFG3KB, AFG3KC

The AFG3K series are function generating devices that also offer the capacity to generate arbitrary waveforms. They accept
communication through LAN, TCPIP and GPIB interfaces.

#### Constraints:

The amplitude, offset and frequency range for AFG3Ks is extremely varied dependent on model number, frequency and function.
However, The sample rate of the entire AFG3K series is 250MS/s.

```{table} AFG3K Constraints
---
widths: auto
width: 50%
align: center
---
|                | Sin         | Square      | Pulse       | Ramp<br/>Sinc<br/>Gaussian<br/>Lorentz<br/>ERise<br/>EDecay<br/>Haversine | Arbitrary     |
|----------------| ----------- | ----------- | ----------- | ------------------------------------------------------------------------- | ------------- |
| **3011/C:**    |             |             |             |                                                                           |               |
| Frequency (Hz) | 1µ–10M      | 1µ–5M       | 1m–5M       | 1µ–0.1M                                                                   | 1m–5M         |
| Amplitude (V)  | 40m–40      | 40m–40      | 40m–40      | 40m–40                                                                    | 40m–40        |
| Offset (V)     | -20–20      | -20–20      | -20–20      | -20–20                                                                    | -20–20        |
| **302xB/C:**   |             |             |             |                                                                           |               |
| Frequency (Hz) | 1µ–25M      | 1µ–25M[^TA] | 1m–25M[^TA] | 1µ–0.5M[^TA]                                                              | 1m–12.5M      |
| Amplitude (V)  | 20m–20      | 20m–20      | 20m–20      | 20m–20                                                                    | 20m–20        |
| Offset (V)     | -10–10      | -10–10      | -10–10      | -10–10                                                                    | -10–10        |
| **305xC:**     |             |             |             |                                                                           |               |
| Frequency (Hz) | 1µ–50M      | 1µ–40M      | 1m–40M      | 1µ–0.8M                                                                   | 1m–25M        |
| Amplitude (V)  | 20m–20      | 20m–20      | 20m–20      | 20m–20                                                                    | 20m–20        |
| Offset (V)     | -10–10      | -10–10      | -10–10      | -10–10                                                                    | -10–10        |
| **310x/C:**    |             |             |             |                                                                           |               |
| Frequency (Hz) | 1µ–0.1G     | 1µ–50M      | 1m–50M      | 1µ–1M                                                                     | 1m–50M        |
| Amplitude (V)  | 40m–20      | 40m–20      | 40m–20      | 4m–20                                                                     | 40m–20        |
| Offset (V)     | -10–10      | -10–10      | -10–10      | -10–10                                                                    | -10–10        |
| **315xC:**     |             |             |             |                                                                           |               |
| Frequency (Hz) | 1µ–0.15G    | 1µ–0.1G     | 1m–0.1G     | 1µ–1.5M                                                                   | 1m–0.1G       |
| Amplitude (V)  | 40m–20[^TB] | 40m–20      | 40m–20      | 40m–20                                                                    | 40m–20        |
| Offset (V)     | -10–10      | -10–10      | -10–10      | -10–10                                                                    | -10–10        |
| **325x/C:**    |             |             |             |                                                                           |               |
| Frequency (Hz) | 1µ–0.24G    | 1µ–0.12G    | 1m–0.12G    | 1µ–2.4M                                                                   | 1m–0.12G<br/> |
| Amplitude (V)  | 0.1–10[^TC] | 0.1–10      | 0.1–10      | 0.1–10                                                                    | 0.1–10        |
| Offset (V)     | -5–5        | -5–5        | -5–5        | -5–5                                                                      | -5–5          |

[^TA]: AFG302xB has its upper bound for frequency halved for these functions.

[^TB]: Amplitude upper bound is reduced to 16 when frequency is greater than 100MHz.

[^TC]: Amplitude upper bound is reduced to 8 when frequency is greater than 200MHz.

```

### AFG31K

The AFG31K series are function generating devices that also offer the capacity to generate arbitrary waveforms. They accept
communication through LAN, TCPIP and GPIB interfaces.

#### Constraints:

```{table} AFG31K Constraints
---
widths: auto
width: 50%
align: center
---
|                   | Sin         | Square<br/>Pulse | Pulse    | Ramp<br/>Sinc<br/>Gaussian<br/>Lorentz<br/>ERise<br/>EDecay<br/>Haversine | Arbitrary |
|-------------------| ----------- | ---------------- | -------- | ------------------------------------------------------------------------- | --------- |
| **3102x:**        |             |                  |          |                                                                           |           |
| Frequency (Hz)    | 1µ–25M      | 1µ–20M           | 1m–25M   | 1µ–0.5M                                                                   | 1m–12.5M  |
| Amplitude (V)     | 2m–20       | 2m–20            | 2m–20    | 2m–20                                                                     | 2m–20     |
| Offset (V)        | -10–10      | -10–10           | -10–10   | -10–10                                                                    | -10–10    |
| Sample Rate (S/s) |             |                  |          |                                                                           | 250M      |
| **3105x:**        |             |                  |          |                                                                           |           |
| Frequency (Hz)    | 1µ–50M      | 1µ–40M           | 1m–40M   | 1µ–0.8M                                                                   | 1m–25M    |
| Amplitude (V)     | 2m–20       | 2m–20            | 2m–20    | 2m–20                                                                     | 2m–20     |
| Offset (V)        | -10–10      | -10–10           | -10–10   | -10–10                                                                    | -10–10    |
| Sample Rate (S/s) |             |                  |          |                                                                           | 1G[^TOA]  |
| **3110x:**        |             |                  |          |                                                                           |           |
| Frequency (Hz)    | 1µ–0.1G     | 1µ–80M           | 1m–50M   | 1µ–1M                                                                     | 1m–50M    |
| Amplitude (V)     | 2m–20[^TOB] | 2m–20[^TOB]      | 2m–20    | 2m–20                                                                     | 2m–20     |
| Offset (V)        | -10–10      | -10–10           | -10–10   | -10–10                                                                    | -10–10    |
| Sample Rate       |             |                  |          |                                                                           | 1G[^TOA]  |
| **3115x:**        |             |                  |          |                                                                           |           |
| Frequency (Hz)    | 1µ–0.15G    | 1µ–0.12G         | 1m–0.1G  | 1µ–1.5M                                                                   | 1m–75M    |
| Amplitude (V)     | 2m–10       | 2m–10            | 2m–10    | 2m–10                                                                     | 2m–10     |
| Offset (V)        | -5–5        | -5–5             | -5–5     | -5–5                                                                      | -5–5      |
| Sample Rate (S/s) |             |                  |          |                                                                           | 2G[^TOA]  |
| **3125x:**        |             |                  |          |                                                                           |           |
| Frequency (Hz)    | 1µ–0.25G    | 1µ–0.16G         | 1m–0.12G | 1µ–2.5M                                                                   | 1m–0.125G |
| Amplitude (V)     | 2m–10[^TOC] | 2m–10            | 2m–10    | 2m–10                                                                     | 2m–10     |
| Offset (V)        | -5–5        | -5–5             | -5–5     | -5–5                                                                      | -5–5      |
| Sample Rate (S/s) |             |                  |          |                                                                           | 2G[^TOA]  |

[^TOA]: When waveform length is greater than 16Kb, otherwise, the sample rate is 250MS/s.

[^TOB]: Amplitude upper bound is reduced to 16 when the frequency is greater than 60MHz. It is further reduced to 12 when the frequency is greater than 80 MHz

[^TOC]: Amplitude upper bound is reduced to 8 when the frequency is greater than 200MHz.

```

______________________________________________________________________

## Arbitrary Waveform Generators

```{autoclasstree} tm_devices.drivers.pi.signal_generators.awgs
---
full:
namespace: tm_devices.drivers.pi.signal_generators.awgs
align: center
alt: Complete device driver class diagram
---
```

Arbitrary Waveform Generators require several different parameters to be specified for a waveform to be generated.

Function generation on AWGs are fundamentally different from AFGs. The AWG is stopped and the channel being changed
is turned off. Predefined waveforms provided with the AWG
are then loaded from the hard drive into the waveform list for the AWG5200 and AWG70K. Sample rate is not channel dependant,
instead being set through the source class. The channel provided has its waveform, offset, amplitude and signal path set.
These attributes can take a while to be set, though once complete, the channels are turned back on and the `AWGCONTROL:RUN`
is set.

```{note}
If the waveform is `RAMP`, a symmetry of 50 will set the waveform to a `TRIANGLE`.
```

The AWG class has some methods specific to it. `generate_waveform` allows for a waveform name from the waveform list
to be provided, instead of a function. The method is also distinctly different from generate function as it relies on a sample
rate also being provided to actually generate the waveform.

AWGs have access to the following functions:
`SIN`, `SQUARE`, `RAMP`, `TRIANGLE`, `DC`, `CLOCK`

### AWG5K/AWG7K

The AWG5K/7K series are signal sources focused on waveform generation which operate on Windows XP (Windows 7 for model C).
They accept communication through LAN and GPIB interfaces.

`set_output_signal_path` is uniquely defined within the AWG5K and AWG7K classes, as it will set the value for
`AWGCONTROL:DOUTPUTx:STATE`, which is a unique option not seen in the other AWGs.

`set_offset` is conditioned to make sure that the AWG output signal path is not DIR, as the VISA query will time
out otherwise.

```{note}
Operation complete commands will always return 1 on the AWG5K/7K series.
```

```{caution}
All waveforms must be of the same length on requesting AWGCONTROL:RUN.
```

#### AWG5K, AWG5KB, AWG5KC

#### Constraints:

The AWG5K series offers a upper sample rate range from 600 MS/s to 1.2 GS/s dependent on the model number. The amplitude range is dependent on
the signal output path, and if the direct option is selected, it will reduce the amplitude range to 50mV to 1 V and the
offset to 0. Otherwise, the amplitude ranges from 20 mV to 2.25 V and an offset range of plus or minus 2.25 V.

```{table} AWG5K Constraints
---
widths: auto
width: 50%
align: center
---
|                   | 500x/B/C   | AWG501x/B/C |
| ----------------- | ---------- | ----------- |
| Sample Rate (S/s) | 10M–600M   | 10M–1.2M    |
| Amplitude (V)     | 20m–2.25   | 20m–2.25    |
| Offset (V)        | -2.25–2.25 | -2.25–2.25  |

```

```{note}
AWG5K's have digitized outputs on the rear of the device.
```

#### AWG7K, AWG7KB, AWG7KC

#### Constraints:

The AWG7K series functions identically to the [AWG5K](#awg5k-awg5kb-awg5kc) series, excluding the higher sample rate and lower amplitude and offset range.

```{table} AWG7K Constraints
---
widths: auto
width: 50%
align: center
---
|                   | 705x     | 710x     | 706xB    | 712xB/C  | 708xC    |
| ----------------- | -------- | -------- | -------- | -------- | -------- |
| Sample Rate (S/s) | 10M–5G   | 10M–10G  | 10M–6G   | 10M–12G  | 10M–8G   |
| Amplitude (V)     | 50m–2    | 50m–2    | 50m–2    | 50m–2    | 50m–2    |
| Offset (V)        | -0.5–0.5 | -0.5–0.5 | -0.5–0.5 | -0.5–0.5 | -0.5–0.5 |

```

The AWG7K also includes varying options which directly effect these ranges, such as option 02 and 06. These options will enforce the
output signal path to always be direct.

```{table} AWG7K Option Constraints
---
widths: auto
width: 50%
align: center
---
|                   | 7102 OPT 06  | 7122B/C OPT 06 | 7xxx OPT 02 |
| ----------------- | ------------ | -------------- | ----------- |
| Sample Rate (S/s) | 10M–20G[^SA] | 10M–24G[^SA]   | "           |
| Amplitude (V)     | 0.5–1.0      | 0.5–1.0        | 0.5–1.0     |
| Offset (V)        | N/A          | N/A            | N/A         |

[^SA]: Samples rates higher than 10GS/S(12GS/s for B/C) can only be done through Interleave.

```

### AWG5200

The AWG5200 series are signal sources focused on waveform generation which operate on Windows 10.
They accept communication through USB, LAN and GPIB interfaces.

`set_output_signal_path` is uniquely defined within the AWG5200 as it has special output signal paths.

`load_waveform` inherently has an operation complete check as attempting to run overlapping commands while loading a waveform can lead to
unintended behavior.

#### Constraints:

The AWG5200 does not have a sample rate range dependent on model number, but instead of what option is installed.
Option 25 on the devices means that the maximum rate is 2.5 GS/s, whereas option 50 has a maximum rate of 5.0 GS/s.

```{table} AWG5200 Constraints
---
widths: auto
width: 50%
align: center
---
|                   | OPT 25      | OPT 50      | OPT DC         |
| ----------------- | ----------- | ----------- | -------------- |
| Sample Rate (S/s) | 0.298k–2.5G | 0.298k–5.0G | "              |
| Amplitude (V)     | 25m–0.75    | 25m–0.75    | 25m–1.5        |
| Offset (V)        | -2–2        | -2–2        | -2–2           |

```

#### Sequential, Blocking and Overlapping Commands:

The AWG5200's programming commands are seperated into three seperated categories: Sequential, Blocking, Overlapping.
The type of command is important to consider as an incorrect order can lead to unintended results.

Sequential commands function as the standard PI commands. They will not start until the previous command has finished. These commands
tend to be fast and will allow for quick response times even if they are queued in the input buffer.

Blocking commands are very similar to sequential commands. The main difference between these commands is that
blocking commands often take longer to execute.

```{caution}
Due to the length of blocking commands, a query may time out when sent if performed immediately after a large series of consecutive blocking commands.
```

Some commands can perform data analysis on another thread, these are referred to as overlapping commands. They allow any command to be started
while they are being executed. They cannot begin if the previous command was blocking or sequential, or if the operation complete status register is
not set.

```{tip}
Overlapping commands run in parralel with any other command, so placing them first in a sequence is always preferable.
```

```{tip}
There are multiple ways of synchronizing overlapping commands. This includes using Operation Complete (OPC) or Wait (WAI) to
wait for the operation complete to clear in the SESR (Standard Event Status Register). This can also be done using an SRQ (Service Request),
along with the waiting for trigger bit in the OCR (Operation Condition Register).
```

```{caution}
The operation complete register will only wait for the first overlapping command to finish before clearing. This means
that if multiple overlapping commands are run, then subsequent overlapping commands being finished will be ignored.
```

```{danger}
Overlapping commands can cause unintended behavior when performed alongside critical hardware functionality.
If the AWG5200 is experiencing problems, this may be a cause.
```

### AWG70KA, AWG70KB

The AWG70K series are signal sources focused on waveform generation which operate on Windows 10.
They accept communication through USB, LAN and GPIB interfaces.

#### Constraints:

The AWG70K is a special case, where only the direct signal output path is allowed (unless option AC is installed). This means the amplitude is limited,
and offset is not allowed to be set by default. However, there is a secondary device which allows for DC amplification, the MDC4500-4B. The MDC4500-4B is an amplifier
which provides an AWG70K the ability to utilize DC offset. It also provides a large range for amplitude.

```{tip}
Though the AWG70K has no offset by default, one can be simulated by changing the raw data in the waveform.
As long as all points are within the amplitude bounds, this can be achieved using WLIST:WAVEFORM:AOFFSET.
```

`set_output_signal_path` is uniquely defined within the AWG70KA and AWG70KB classes. By default, it will first attempt to set the output signal path to DCA.
If this fails (implying an MDC4500-4B is not connected), then a direct (DIR) signal path will be set.

`set_offset` is conditioned to make sure that the AWG output signal path is not DIR, as the VISA query will time
out otherwise.

```{table} AWG70K Constraints
---
widths: auto
width: 50%
align: center
---
|                   | OPT 150   | OPT 225   | OPT 216   | OPT 208   | MDC4500       |
| ----------------- | --------- | --------- | --------- | --------- | ------------- |
| Sample Rate (S/s) | 1.49k–50G | 1.49k–25G | 1.49k–16G | 1.49k–8G  | "             |
| Amplitude (V)     | 0.125–0.5 | 0.125–0.5 | 0.125–0.5 | 0.125–0.5 | 31m–1.6[^SZA] |
| Offset (V)        | N/A       | N/A       | N/A       | N/A       | -0.4–0.8      |

[^SZA]: Although the MOD4500-4B allows for greater than 1.0 amplitude, there is a drop off in accuracy.

```

#### Stipulations:

The AWG70K also houses infrastructure to support [sequential, blocking and overlapping commands](#sequential-blocking-and-overlapping-commands).
