# pylint: disable=line-too-long
"""The auxin commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUXIn:BANdwidth <NR3>
    - AUXIn:BANdwidth?
    - AUXIn:COUPling <NR3>
    - AUXIn:COUPling?
    - AUXIn:OFFSet <NR3>
    - AUXIn:OFFSet?
    - AUXIn:PROBEFunc:EXTAtten <NR3>
    - AUXIn:PROBEFunc:EXTAtten?
    - AUXIn:PROBEFunc:EXTDBatten <NR3>
    - AUXIn:PROBEFunc:EXTDBatten?
    - AUXIn:PROBEFunc:EXTUnits <QString>
    - AUXIn:PROBEFunc:EXTUnits?
    - AUXIn:PRObe:AUTOZero EXECute
    - AUXIn:PRObe:DEGAUSS EXECute
    - AUXIn:PRObe:DEGAUSS:STATE?
    - AUXIn:PRObe:FORCEDRange <NR3>
    - AUXIn:PRObe:FORCEDRange?
    - AUXIn:PRObe:GAIN?
    - AUXIn:PRObe:ID:SERnumber?
    - AUXIn:PRObe:ID:TYPe?
    - AUXIn:PRObe:INPUTMode {COMmonmode|DEFault|DIFFerential|A|B}
    - AUXIn:PRObe:INPUTMode:AOFFSet <NR3>
    - AUXIn:PRObe:INPUTMode:AOFFSet?
    - AUXIn:PRObe:INPUTMode:BOFFSet <NR3>
    - AUXIn:PRObe:INPUTMode:BOFFSet?
    - AUXIn:PRObe:INPUTMode:CMOFFSet <NR3>
    - AUXIn:PRObe:INPUTMode:CMOFFSet?
    - AUXIn:PRObe:INPUTMode:DMOFFSet <NR3>
    - AUXIn:PRObe:INPUTMode:DMOFFSet?
    - AUXIn:PRObe:INPUTMode?
    - AUXIn:PRObe:RANge {ATTEN1X|ATTEN1_25X|ATTEN1_5X|ATTEN1_75X|ATTEN2X|ATTEN2_5X|ATTEN3X|ATTEN3_5X|ATTEN4X|ATTEN4_5X|ATTEN5X|ATTEN5_5X|ATTEN6X|ATTEN6_5X|ATTEN7X|ATTEN7_5X|ATTEN8X|ATTEN8_5X|ATTEN9X|ATTEN9_5X|ATTEN10X|ATTEN12_5X|ATTEN15X|ATTEN17_5X|ATTEN20X|ATTEN25X|ATTEN30X|ATTEN35X|ATTEN40X|ATTEN45X|ATTEN50X|ATTEN55X|ATTEN60X|ATTEN65X|ATTEN70X|ATTEN75X|ATTEN80X|ATTEN85X|ATTEN90X|ATTEN95X|ATTEN100X|ATTEN125X|ATTEN150X|ATTEN175X|ATTEN200X|ATTEN250X|ATTEN300X|ATTEN350X|ATTEN400X|ATTEN450X|ATTEN500X|ATTEN550X|ATTEN600X|ATTEN650X|ATTEN700X|ATTEN750X|ATTEN800X|ATTEN850X|ATTEN900X|ATTEN950X|ATTEN1000X}
    - AUXIn:PRObe:RANge?
    - AUXIn:PRObe:RESistance?
    - AUXIn:PRObe:SET <QString>
    - AUXIn:PRObe:SET?
    - AUXIn:PRObe:SIGnal {PASS|BYPass}
    - AUXIn:PRObe:SIGnal?
    - AUXIn:PRObe:TIPtype {HBWStraightflex|OTHer}
    - AUXIn:PRObe:TIPtype?
    - AUXIn:PRObe:UNIts?
    - AUXIn:VTERm:DUAL:A <NR3>
    - AUXIn:VTERm:DUAL:A?
    - AUXIn:VTERm:DUAL:B <NR3>
    - AUXIn:VTERm:DUAL:B?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AuxinVtermDualB(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:VTERm:DUAL:B`` command.

    Description:
        - This command sets or queries the termination voltage for probes with dual inputs that
          support settable termination voltage.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:VTERm:DUAL:B?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:VTERm:DUAL:B?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:VTERm:DUAL:B value`` command.

    SCPI Syntax:
        ```
        - AUXIn:VTERm:DUAL:B <NR3>
        - AUXIn:VTERm:DUAL:B?
        ```

    Info:
        - ``<NR3>`` specifies the termination voltage.
    """


class AuxinVtermDualA(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:VTERm:DUAL:A`` command.

    Description:
        - This command sets or queries the termination voltage for probes with dual inputs that
          support settable termination voltage.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:VTERm:DUAL:A?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:VTERm:DUAL:A?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:VTERm:DUAL:A value`` command.

    SCPI Syntax:
        ```
        - AUXIn:VTERm:DUAL:A <NR3>
        - AUXIn:VTERm:DUAL:A?
        ```

    Info:
        - ``<NR3>`` specifies the termination voltage.
    """


class AuxinVtermDual(SCPICmdRead):
    """The ``AUXIn:VTERm:DUAL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:VTERm:DUAL?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:VTERm:DUAL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.a``: The ``AUXIn:VTERm:DUAL:A`` command.
        - ``.b``: The ``AUXIn:VTERm:DUAL:B`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._a = AuxinVtermDualA(device, f"{self._cmd_syntax}:A")
        self._b = AuxinVtermDualB(device, f"{self._cmd_syntax}:B")

    @property
    def a(self) -> AuxinVtermDualA:
        """Return the ``AUXIn:VTERm:DUAL:A`` command.

        Description:
            - This command sets or queries the termination voltage for probes with dual inputs that
              support settable termination voltage.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:VTERm:DUAL:A?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:VTERm:DUAL:A?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:VTERm:DUAL:A value`` command.

        SCPI Syntax:
            ```
            - AUXIn:VTERm:DUAL:A <NR3>
            - AUXIn:VTERm:DUAL:A?
            ```

        Info:
            - ``<NR3>`` specifies the termination voltage.
        """
        return self._a

    @property
    def b(self) -> AuxinVtermDualB:
        """Return the ``AUXIn:VTERm:DUAL:B`` command.

        Description:
            - This command sets or queries the termination voltage for probes with dual inputs that
              support settable termination voltage.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:VTERm:DUAL:B?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:VTERm:DUAL:B?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:VTERm:DUAL:B value`` command.

        SCPI Syntax:
            ```
            - AUXIn:VTERm:DUAL:B <NR3>
            - AUXIn:VTERm:DUAL:B?
            ```

        Info:
            - ``<NR3>`` specifies the termination voltage.
        """
        return self._b


class AuxinVterm(SCPICmdRead):
    """The ``AUXIn:VTERm`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:VTERm?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:VTERm?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dual``: The ``AUXIn:VTERm:DUAL`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dual = AuxinVtermDual(device, f"{self._cmd_syntax}:DUAL")

    @property
    def dual(self) -> AuxinVtermDual:
        """Return the ``AUXIn:VTERm:DUAL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:VTERm:DUAL?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:VTERm:DUAL?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.a``: The ``AUXIn:VTERm:DUAL:A`` command.
            - ``.b``: The ``AUXIn:VTERm:DUAL:B`` command.
        """
        return self._dual


class AuxinProbeUnits(SCPICmdRead):
    """The ``AUXIn:PRObe:UNIts`` command.

    Description:
        - This query-only command returns a string describing the units of measure for the probe
          attached to the AUX In input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:UNIts?
        ```
    """


class AuxinProbeTiptype(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:TIPtype`` command.

    Description:
        - This command sets or queries the type of probe tip being used.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:TIPtype?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:TIPtype?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:TIPtype value`` command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:TIPtype {HBWStraightflex|OTHer}
        - AUXIn:PRObe:TIPtype?
        ```

    Info:
        - ``HBWStraightflex`` lets the instrument know you are using a high bandwidth straight-flex
          probe tip.
        - ``OTHer`` lets the instrument know you are not using a high bandwidth straight-flex probe
          tip.
    """


class AuxinProbeSignal(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:SIGnal`` command.

    Description:
        - This command sets or queries aspects of probe accessory user interfaces. The available
          arguments for this command will vary depending on the accessory you attach to the
          instrument.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:SIGnal?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:SIGnal?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:SIGnal value`` command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:SIGnal {PASS|BYPass}
        - AUXIn:PRObe:SIGnal?
        ```

    Info:
        - ``PASS`` opens a relay passing your signal to the instrument.
        - ``BYPass`` closes a relay preventing your signal from reaching the instrument. During
          probe degauss, the signal should be bypassed.
    """


class AuxinProbeSet(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:SET`` command.

    Description:
        - This command sets or queries aspects of probe accessory user interfaces, for example probe
          attenuation factors. The available arguments for this command will vary depending on the
          accessory you attach to the instrument auxiliary trigger input. For the P7260 probe, you
          can select between two attenuation factors using either this GPIB command or the push
          switch on the probe. The probe enables the relevant path and adjusts the settings based on
          the characteristics of the path in use. The probe signal path selection is not kept in
          persistent storage. The probe will lose the selection if you reboot the instrument or
          remove the probe. Also, the instrument does not store the selection in the save/recall
          setup operation.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:SET?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:SET?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:SET value`` command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:SET <QString>
        - AUXIn:PRObe:SET?
        ```

    Info:
        - ``<QString>`` is a quoted string representing a settable aspect of the attached accessory.
        - ``ATTENUATION 5X`` sets the P7260 probe to ±0.75 V dynamic range with 6 GHz bandwidth and
          5X attenuation.
        - ``ATTENUATION 25X`` sets the P7260 probe to ±3 V dynamic range with 6 GHz bandwidth and
          25X attenuation.
        - ``VTERMsource AUTO`` sets the P7380SMA probe voltage termination source to auto.
        - ``VTERMsource INTernal`` sets the P7380SMA probe voltage termination source to internal.
        - ``VTERMsource EXTernal`` sets the P7380SMA probe voltage termination source to external.
    """

    _WRAP_ARG_WITH_QUOTES = True


class AuxinProbeResistance(SCPICmdRead):
    """The ``AUXIn:PRObe:RESistance`` command.

    Description:
        - This query-only command returns the resistance factor of the probe that is attached to the
          AUX In input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:RESistance?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:RESistance?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:RESistance?
        ```
    """


class AuxinProbeRange(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:RANge`` command.

    Description:
        - This command controls or queries the set attenuation range of the probe on the AUX In
          input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:RANge?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:RANge?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:RANge value`` command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:RANge {ATTEN1X|ATTEN1_25X|ATTEN1_5X|ATTEN1_75X|ATTEN2X|ATTEN2_5X|ATTEN3X|ATTEN3_5X|ATTEN4X|ATTEN4_5X|ATTEN5X|ATTEN5_5X|ATTEN6X|ATTEN6_5X|ATTEN7X|ATTEN7_5X|ATTEN8X|ATTEN8_5X|ATTEN9X|ATTEN9_5X|ATTEN10X|ATTEN12_5X|ATTEN15X|ATTEN17_5X|ATTEN20X|ATTEN25X|ATTEN30X|ATTEN35X|ATTEN40X|ATTEN45X|ATTEN50X|ATTEN55X|ATTEN60X|ATTEN65X|ATTEN70X|ATTEN75X|ATTEN80X|ATTEN85X|ATTEN90X|ATTEN95X|ATTEN100X|ATTEN125X|ATTEN150X|ATTEN175X|ATTEN200X|ATTEN250X|ATTEN300X|ATTEN350X|ATTEN400X|ATTEN450X|ATTEN500X|ATTEN550X|ATTEN600X|ATTEN650X|ATTEN700X|ATTEN750X|ATTEN800X|ATTEN850X|ATTEN900X|ATTEN950X|ATTEN1000X}
        - AUXIn:PRObe:RANge?
        ```
    """  # noqa: E501


class AuxinProbeInputmodeDmoffset(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:INPUTMode:DMOFFSet`` command.

    Description:
        - This command sets or queries the requested differential mode offset control of the probe
          that is attached to the AUX In input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode:DMOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode:DMOFFSet?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:INPUTMode:DMOFFSet value``
          command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:INPUTMode:DMOFFSet <NR3>
        - AUXIn:PRObe:INPUTMode:DMOFFSet?
        ```

    Info:
        - ``<NR3>`` specifies the differential mode offset control.
    """


class AuxinProbeInputmodeCmoffset(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:INPUTMode:CMOFFSet`` command.

    Description:
        - This command sets or queries the requested common mode offset control of the probe that is
          attached to the AUX In input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode:CMOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode:CMOFFSet?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:INPUTMode:CMOFFSet value``
          command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:INPUTMode:CMOFFSet <NR3>
        - AUXIn:PRObe:INPUTMode:CMOFFSet?
        ```

    Info:
        - ``<NR3>`` specifies the common mode offset control.
    """


class AuxinProbeInputmodeBoffset(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:INPUTMode:BOFFSet`` command.

    Description:
        - This command sets or queries the requested B mode offset control of the probe that is
          attached to the AUX In input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode:BOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode:BOFFSet?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:INPUTMode:BOFFSet value``
          command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:INPUTMode:BOFFSet <NR3>
        - AUXIn:PRObe:INPUTMode:BOFFSet?
        ```

    Info:
        - ``<NR3>`` specifies the B mode offset control.
    """


class AuxinProbeInputmodeAoffset(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:INPUTMode:AOFFSet`` command.

    Description:
        - This command sets or queries the requested A mode offset control of the probe that is
          attached to the AUX In input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode:AOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode:AOFFSet?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:INPUTMode:AOFFSet value``
          command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:INPUTMode:AOFFSet <NR3>
        - AUXIn:PRObe:INPUTMode:AOFFSet?
        ```

    Info:
        - ``<NR3>`` specifies the A mode offset control.
    """


class AuxinProbeInputmode(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:INPUTMode`` command.

    Description:
        - This command sets or queries one of the probe's four input modes on the AUX In input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:INPUTMode value`` command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:INPUTMode {COMmonmode|DEFault|DIFFerential|A|B}
        - AUXIn:PRObe:INPUTMode?
        ```

    Info:
        - ``COMmonmode`` sets the probe to route common-mode signals to the host.
        - ``DEFault`` sets the probe to the default mode.
        - ``DIFFerential`` sets the probe to route differential signals to the host.
        - ``A`` sets the probe to route single-ended A signals to the host.
        - ``B`` sets the probe to route single-ended B signals to the host.

    Properties:
        - ``.aoffset``: The ``AUXIn:PRObe:INPUTMode:AOFFSet`` command.
        - ``.boffset``: The ``AUXIn:PRObe:INPUTMode:BOFFSet`` command.
        - ``.cmoffset``: The ``AUXIn:PRObe:INPUTMode:CMOFFSet`` command.
        - ``.dmoffset``: The ``AUXIn:PRObe:INPUTMode:DMOFFSet`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aoffset = AuxinProbeInputmodeAoffset(device, f"{self._cmd_syntax}:AOFFSet")
        self._boffset = AuxinProbeInputmodeBoffset(device, f"{self._cmd_syntax}:BOFFSet")
        self._cmoffset = AuxinProbeInputmodeCmoffset(device, f"{self._cmd_syntax}:CMOFFSet")
        self._dmoffset = AuxinProbeInputmodeDmoffset(device, f"{self._cmd_syntax}:DMOFFSet")

    @property
    def aoffset(self) -> AuxinProbeInputmodeAoffset:
        """Return the ``AUXIn:PRObe:INPUTMode:AOFFSet`` command.

        Description:
            - This command sets or queries the requested A mode offset control of the probe that is
              attached to the AUX In input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode:AOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode:AOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AUXIn:PRObe:INPUTMode:AOFFSet value`` command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:INPUTMode:AOFFSet <NR3>
            - AUXIn:PRObe:INPUTMode:AOFFSet?
            ```

        Info:
            - ``<NR3>`` specifies the A mode offset control.
        """
        return self._aoffset

    @property
    def boffset(self) -> AuxinProbeInputmodeBoffset:
        """Return the ``AUXIn:PRObe:INPUTMode:BOFFSet`` command.

        Description:
            - This command sets or queries the requested B mode offset control of the probe that is
              attached to the AUX In input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode:BOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode:BOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AUXIn:PRObe:INPUTMode:BOFFSet value`` command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:INPUTMode:BOFFSet <NR3>
            - AUXIn:PRObe:INPUTMode:BOFFSet?
            ```

        Info:
            - ``<NR3>`` specifies the B mode offset control.
        """
        return self._boffset

    @property
    def cmoffset(self) -> AuxinProbeInputmodeCmoffset:
        """Return the ``AUXIn:PRObe:INPUTMode:CMOFFSet`` command.

        Description:
            - This command sets or queries the requested common mode offset control of the probe
              that is attached to the AUX In input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode:CMOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode:CMOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AUXIn:PRObe:INPUTMode:CMOFFSet value`` command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:INPUTMode:CMOFFSet <NR3>
            - AUXIn:PRObe:INPUTMode:CMOFFSet?
            ```

        Info:
            - ``<NR3>`` specifies the common mode offset control.
        """
        return self._cmoffset

    @property
    def dmoffset(self) -> AuxinProbeInputmodeDmoffset:
        """Return the ``AUXIn:PRObe:INPUTMode:DMOFFSet`` command.

        Description:
            - This command sets or queries the requested differential mode offset control of the
              probe that is attached to the AUX In input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode:DMOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode:DMOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AUXIn:PRObe:INPUTMode:DMOFFSet value`` command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:INPUTMode:DMOFFSet <NR3>
            - AUXIn:PRObe:INPUTMode:DMOFFSet?
            ```

        Info:
            - ``<NR3>`` specifies the differential mode offset control.
        """
        return self._dmoffset


class AuxinProbeIdType(SCPICmdRead):
    """The ``AUXIn:PRObe:ID:TYPe`` command.

    Description:
        - This query-only command returns the probe type.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:ID:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:ID:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:ID:TYPe?
        ```
    """


class AuxinProbeIdSernumber(SCPICmdRead):
    """The ``AUXIn:PRObe:ID:SERnumber`` command.

    Description:
        - This query-only command returns the probe serial number.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:ID:SERnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:ID:SERnumber?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:ID:SERnumber?
        ```
    """


class AuxinProbeId(SCPICmdRead):
    """The ``AUXIn:PRObe:ID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:ID?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:ID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sernumber``: The ``AUXIn:PRObe:ID:SERnumber`` command.
        - ``.type``: The ``AUXIn:PRObe:ID:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sernumber = AuxinProbeIdSernumber(device, f"{self._cmd_syntax}:SERnumber")
        self._type = AuxinProbeIdType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def sernumber(self) -> AuxinProbeIdSernumber:
        """Return the ``AUXIn:PRObe:ID:SERnumber`` command.

        Description:
            - This query-only command returns the probe serial number.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:ID:SERnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:ID:SERnumber?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:ID:SERnumber?
            ```
        """
        return self._sernumber

    @property
    def type(self) -> AuxinProbeIdType:
        """Return the ``AUXIn:PRObe:ID:TYPe`` command.

        Description:
            - This query-only command returns the probe type.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:ID:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:ID:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:ID:TYPe?
            ```
        """
        return self._type


class AuxinProbeGain(SCPICmdRead):
    """The ``AUXIn:PRObe:GAIN`` command.

    Description:
        - This query-only command returns the gain factor of the probe that is attached to the AUX
          In input. The 'gain' of a probe is the output divided by the input transfer ratio. For
          example, a common 10x probe has a gain of 0.1.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:GAIN?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:GAIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:GAIN?
        ```
    """


class AuxinProbeForcedrange(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:FORCEDRange`` command.

    Description:
        - This command sets the probe attached to the AUX In input to the specified range, or the
          command queries the probe range.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:FORCEDRange?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:FORCEDRange?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:FORCEDRange value``
          command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:FORCEDRange <NR3>
        - AUXIn:PRObe:FORCEDRange?
        ```

    Info:
        - ``<NR3>`` specifies the probe range.
    """


class AuxinProbeDegaussState(SCPICmdRead):
    """The ``AUXIn:PRObe:DEGAUSS:STATE`` command.

    Description:
        - This command queries whether the probe attached to the AUX In input is degaussed.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe:DEGAUSS:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:DEGAUSS:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:DEGAUSS:STATE?
        ```
    """


class AuxinProbeDegauss(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PRObe:DEGAUSS`` command.

    Description:
        - This command starts a degauss cycle of the probe attached to the AUX In input. The degauss
          cycle will change with an appropriate probe attached.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:DEGAUSS value`` command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:DEGAUSS EXECute
        ```

    Info:
        - ``EXECute`` starts a probe degauss cycle.

    Properties:
        - ``.state``: The ``AUXIn:PRObe:DEGAUSS:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = AuxinProbeDegaussState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> AuxinProbeDegaussState:
        """Return the ``AUXIn:PRObe:DEGAUSS:STATE`` command.

        Description:
            - This command queries whether the probe attached to the AUX In input is degaussed.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:DEGAUSS:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:DEGAUSS:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:DEGAUSS:STATE?
            ```
        """
        return self._state


class AuxinProbeAutozero(SCPICmdWrite):
    """The ``AUXIn:PRObe:AUTOZero`` command.

    Description:
        - The command sets the probe attached to the AUX In input to autozero.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:AUTOZero value`` command.

    SCPI Syntax:
        ```
        - AUXIn:PRObe:AUTOZero EXECute
        ```

    Info:
        - ``EXECute`` sets the probe to autozero.
    """


#  pylint: disable=too-many-instance-attributes
class AuxinProbe(SCPICmdRead):
    """The ``AUXIn:PRObe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autozero``: The ``AUXIn:PRObe:AUTOZero`` command.
        - ``.degauss``: The ``AUXIn:PRObe:DEGAUSS`` command.
        - ``.forcedrange``: The ``AUXIn:PRObe:FORCEDRange`` command.
        - ``.gain``: The ``AUXIn:PRObe:GAIN`` command.
        - ``.id``: The ``AUXIn:PRObe:ID`` command tree.
        - ``.inputmode``: The ``AUXIn:PRObe:INPUTMode`` command.
        - ``.range``: The ``AUXIn:PRObe:RANge`` command.
        - ``.resistance``: The ``AUXIn:PRObe:RESistance`` command.
        - ``.set``: The ``AUXIn:PRObe:SET`` command.
        - ``.signal``: The ``AUXIn:PRObe:SIGnal`` command.
        - ``.tiptype``: The ``AUXIn:PRObe:TIPtype`` command.
        - ``.units``: The ``AUXIn:PRObe:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autozero = AuxinProbeAutozero(device, f"{self._cmd_syntax}:AUTOZero")
        self._degauss = AuxinProbeDegauss(device, f"{self._cmd_syntax}:DEGAUSS")
        self._forcedrange = AuxinProbeForcedrange(device, f"{self._cmd_syntax}:FORCEDRange")
        self._gain = AuxinProbeGain(device, f"{self._cmd_syntax}:GAIN")
        self._id = AuxinProbeId(device, f"{self._cmd_syntax}:ID")
        self._inputmode = AuxinProbeInputmode(device, f"{self._cmd_syntax}:INPUTMode")
        self._range = AuxinProbeRange(device, f"{self._cmd_syntax}:RANge")
        self._resistance = AuxinProbeResistance(device, f"{self._cmd_syntax}:RESistance")
        self._set = AuxinProbeSet(device, f"{self._cmd_syntax}:SET")
        self._signal = AuxinProbeSignal(device, f"{self._cmd_syntax}:SIGnal")
        self._tiptype = AuxinProbeTiptype(device, f"{self._cmd_syntax}:TIPtype")
        self._units = AuxinProbeUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def autozero(self) -> AuxinProbeAutozero:
        """Return the ``AUXIn:PRObe:AUTOZero`` command.

        Description:
            - The command sets the probe attached to the AUX In input to autozero.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:AUTOZero value``
              command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:AUTOZero EXECute
            ```

        Info:
            - ``EXECute`` sets the probe to autozero.
        """
        return self._autozero

    @property
    def degauss(self) -> AuxinProbeDegauss:
        """Return the ``AUXIn:PRObe:DEGAUSS`` command.

        Description:
            - This command starts a degauss cycle of the probe attached to the AUX In input. The
              degauss cycle will change with an appropriate probe attached.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:DEGAUSS value``
              command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:DEGAUSS EXECute
            ```

        Info:
            - ``EXECute`` starts a probe degauss cycle.

        Sub-properties:
            - ``.state``: The ``AUXIn:PRObe:DEGAUSS:STATE`` command.
        """
        return self._degauss

    @property
    def forcedrange(self) -> AuxinProbeForcedrange:
        """Return the ``AUXIn:PRObe:FORCEDRange`` command.

        Description:
            - This command sets the probe attached to the AUX In input to the specified range, or
              the command queries the probe range.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:FORCEDRange?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:FORCEDRange?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:FORCEDRange value``
              command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:FORCEDRange <NR3>
            - AUXIn:PRObe:FORCEDRange?
            ```

        Info:
            - ``<NR3>`` specifies the probe range.
        """
        return self._forcedrange

    @property
    def gain(self) -> AuxinProbeGain:
        """Return the ``AUXIn:PRObe:GAIN`` command.

        Description:
            - This query-only command returns the gain factor of the probe that is attached to the
              AUX In input. The 'gain' of a probe is the output divided by the input transfer ratio.
              For example, a common 10x probe has a gain of 0.1.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:GAIN?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:GAIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:GAIN?
            ```
        """
        return self._gain

    @property
    def id(self) -> AuxinProbeId:
        """Return the ``AUXIn:PRObe:ID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:ID?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:ID?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sernumber``: The ``AUXIn:PRObe:ID:SERnumber`` command.
            - ``.type``: The ``AUXIn:PRObe:ID:TYPe`` command.
        """
        return self._id

    @property
    def inputmode(self) -> AuxinProbeInputmode:
        """Return the ``AUXIn:PRObe:INPUTMode`` command.

        Description:
            - This command sets or queries one of the probe's four input modes on the AUX In input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:INPUTMode?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:INPUTMode?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:INPUTMode value``
              command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:INPUTMode {COMmonmode|DEFault|DIFFerential|A|B}
            - AUXIn:PRObe:INPUTMode?
            ```

        Info:
            - ``COMmonmode`` sets the probe to route common-mode signals to the host.
            - ``DEFault`` sets the probe to the default mode.
            - ``DIFFerential`` sets the probe to route differential signals to the host.
            - ``A`` sets the probe to route single-ended A signals to the host.
            - ``B`` sets the probe to route single-ended B signals to the host.

        Sub-properties:
            - ``.aoffset``: The ``AUXIn:PRObe:INPUTMode:AOFFSet`` command.
            - ``.boffset``: The ``AUXIn:PRObe:INPUTMode:BOFFSet`` command.
            - ``.cmoffset``: The ``AUXIn:PRObe:INPUTMode:CMOFFSet`` command.
            - ``.dmoffset``: The ``AUXIn:PRObe:INPUTMode:DMOFFSet`` command.
        """
        return self._inputmode

    @property
    def range(self) -> AuxinProbeRange:
        """Return the ``AUXIn:PRObe:RANge`` command.

        Description:
            - This command controls or queries the set attenuation range of the probe on the AUX In
              input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:RANge?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:RANge?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:RANge value`` command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:RANge {ATTEN1X|ATTEN1_25X|ATTEN1_5X|ATTEN1_75X|ATTEN2X|ATTEN2_5X|ATTEN3X|ATTEN3_5X|ATTEN4X|ATTEN4_5X|ATTEN5X|ATTEN5_5X|ATTEN6X|ATTEN6_5X|ATTEN7X|ATTEN7_5X|ATTEN8X|ATTEN8_5X|ATTEN9X|ATTEN9_5X|ATTEN10X|ATTEN12_5X|ATTEN15X|ATTEN17_5X|ATTEN20X|ATTEN25X|ATTEN30X|ATTEN35X|ATTEN40X|ATTEN45X|ATTEN50X|ATTEN55X|ATTEN60X|ATTEN65X|ATTEN70X|ATTEN75X|ATTEN80X|ATTEN85X|ATTEN90X|ATTEN95X|ATTEN100X|ATTEN125X|ATTEN150X|ATTEN175X|ATTEN200X|ATTEN250X|ATTEN300X|ATTEN350X|ATTEN400X|ATTEN450X|ATTEN500X|ATTEN550X|ATTEN600X|ATTEN650X|ATTEN700X|ATTEN750X|ATTEN800X|ATTEN850X|ATTEN900X|ATTEN950X|ATTEN1000X}
            - AUXIn:PRObe:RANge?
            ```
        """  # noqa: E501
        return self._range

    @property
    def resistance(self) -> AuxinProbeResistance:
        """Return the ``AUXIn:PRObe:RESistance`` command.

        Description:
            - This query-only command returns the resistance factor of the probe that is attached to
              the AUX In input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:RESistance?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:RESistance?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:RESistance?
            ```
        """
        return self._resistance

    @property
    def set_(self) -> AuxinProbeSet:
        """Return the ``AUXIn:PRObe:SET`` command.

        Description:
            - This command sets or queries aspects of probe accessory user interfaces, for example
              probe attenuation factors. The available arguments for this command will vary
              depending on the accessory you attach to the instrument auxiliary trigger input. For
              the P7260 probe, you can select between two attenuation factors using either this GPIB
              command or the push switch on the probe. The probe enables the relevant path and
              adjusts the settings based on the characteristics of the path in use. The probe signal
              path selection is not kept in persistent storage. The probe will lose the selection if
              you reboot the instrument or remove the probe. Also, the instrument does not store the
              selection in the save/recall setup operation.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:SET?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:SET?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:SET value`` command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:SET <QString>
            - AUXIn:PRObe:SET?
            ```

        Info:
            - ``<QString>`` is a quoted string representing a settable aspect of the attached
              accessory.
            - ``ATTENUATION 5X`` sets the P7260 probe to ±0.75 V dynamic range with 6 GHz bandwidth
              and 5X attenuation.
            - ``ATTENUATION 25X`` sets the P7260 probe to ±3 V dynamic range with 6 GHz bandwidth
              and 25X attenuation.
            - ``VTERMsource AUTO`` sets the P7380SMA probe voltage termination source to auto.
            - ``VTERMsource INTernal`` sets the P7380SMA probe voltage termination source to
              internal.
            - ``VTERMsource EXTernal`` sets the P7380SMA probe voltage termination source to
              external.
        """
        return self._set

    @property
    def signal(self) -> AuxinProbeSignal:
        """Return the ``AUXIn:PRObe:SIGnal`` command.

        Description:
            - This command sets or queries aspects of probe accessory user interfaces. The available
              arguments for this command will vary depending on the accessory you attach to the
              instrument.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:SIGnal?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:SIGnal?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:SIGnal value`` command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:SIGnal {PASS|BYPass}
            - AUXIn:PRObe:SIGnal?
            ```

        Info:
            - ``PASS`` opens a relay passing your signal to the instrument.
            - ``BYPass`` closes a relay preventing your signal from reaching the instrument. During
              probe degauss, the signal should be bypassed.
        """
        return self._signal

    @property
    def tiptype(self) -> AuxinProbeTiptype:
        """Return the ``AUXIn:PRObe:TIPtype`` command.

        Description:
            - This command sets or queries the type of probe tip being used.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:TIPtype?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:TIPtype?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:PRObe:TIPtype value``
              command.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:TIPtype {HBWStraightflex|OTHer}
            - AUXIn:PRObe:TIPtype?
            ```

        Info:
            - ``HBWStraightflex`` lets the instrument know you are using a high bandwidth
              straight-flex probe tip.
            - ``OTHer`` lets the instrument know you are not using a high bandwidth straight-flex
              probe tip.
        """
        return self._tiptype

    @property
    def units(self) -> AuxinProbeUnits:
        """Return the ``AUXIn:PRObe:UNIts`` command.

        Description:
            - This query-only command returns a string describing the units of measure for the probe
              attached to the AUX In input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXIn:PRObe:UNIts?
            ```
        """
        return self._units


class AuxinProbefuncExtunits(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PROBEFunc:EXTUnits`` command.

    Description:
        - This command sets the unit of measurement for the external attenuator of the AUX In input.
          There is also a corresponding query that returns the user-specified unit of measurement
          for the external attenuator. Unless these units are set to the factory default string
          value of 'None', they become the attenuated units of measurement for the input. It is
          assumed that the probe connected to the input is of the correct type to receive the output
          of the user's external transducer or network.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PROBEFunc:EXTUnits?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PROBEFunc:EXTUnits?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PROBEFunc:EXTUnits value``
          command.

    SCPI Syntax:
        ```
        - AUXIn:PROBEFunc:EXTUnits <QString>
        - AUXIn:PROBEFunc:EXTUnits?
        ```

    Info:
        - ``<QString>`` can contain a string of up to eight characters to indicate the attenuation
          unit of measurement for the AUX In input. However, most instrument attenuators only
          display the first two characters.
    """

    _WRAP_ARG_WITH_QUOTES = True


class AuxinProbefuncExtdbatten(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PROBEFunc:EXTDBatten`` command.

    Description:
        - This command sets the input-output ratio (expressed in decibel units) of external
          attenuation or gain between the signal and the instrument AUX In input. The query form of
          this command returns the user-specified attenuation in decibels: 1X = 0 dB, 10X = 20 dB,
          100X = 40 dB, and similar things. This command is equivalent to selecting Attenuation from
          the Vertical menu, and then either viewing or setting Ext Att(dB).

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PROBEFunc:EXTDBatten?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PROBEFunc:EXTDBatten?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PROBEFunc:EXTDBatten value``
          command.

    SCPI Syntax:
        ```
        - AUXIn:PROBEFunc:EXTDBatten <NR3>
        - AUXIn:PROBEFunc:EXTDBatten?
        ```

    Info:
        - ``<NR3>`` is the attenuation value, which is specified in the range from -200.00 dB to
          200.00 dB.
    """


class AuxinProbefuncExtatten(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:PROBEFunc:EXTAtten`` command.

    Description:
        - This command sets the input-output ratio, of external attenuation or gain, between the
          signal and the AUX In input. The query form of this command returns the user-specified
          attenuation. Note that this command deals with an attenuation factor, not a gain factor,
          unlike ``CHX:PROBE`` (This command returns a value independent of the external
          attenuation). For example, if you specify a 20X attenuation factor, the commands return
          the following values (assuming that a 1x probe is presently attached, since the external
          attenuation is used in combination with the probe attenuation): ``AUXIN:PROBE:EXTA?``
          20.00E+0 ``AUXIN:PROBE?`` 1.0E+0 This command is equivalent to selecting Attenuation from
          the Vertical menu, and then either viewing or setting Ext Atten.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PROBEFunc:EXTAtten?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PROBEFunc:EXTAtten?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:PROBEFunc:EXTAtten value``
          command.

    SCPI Syntax:
        ```
        - AUXIn:PROBEFunc:EXTAtten <NR3>
        - AUXIn:PROBEFunc:EXTAtten?
        ```

    Info:
        - ``<NR3>`` is the attenuation value, which is specified as a multiplier in the range from
          1.00E-10 to 1.00E+10.
    """


class AuxinProbefunc(SCPICmdRead):
    """The ``AUXIn:PROBEFunc`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:PROBEFunc?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:PROBEFunc?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.extatten``: The ``AUXIn:PROBEFunc:EXTAtten`` command.
        - ``.extdbatten``: The ``AUXIn:PROBEFunc:EXTDBatten`` command.
        - ``.extunits``: The ``AUXIn:PROBEFunc:EXTUnits`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._extatten = AuxinProbefuncExtatten(device, f"{self._cmd_syntax}:EXTAtten")
        self._extdbatten = AuxinProbefuncExtdbatten(device, f"{self._cmd_syntax}:EXTDBatten")
        self._extunits = AuxinProbefuncExtunits(device, f"{self._cmd_syntax}:EXTUnits")

    @property
    def extatten(self) -> AuxinProbefuncExtatten:
        """Return the ``AUXIn:PROBEFunc:EXTAtten`` command.

        Description:
            - This command sets the input-output ratio, of external attenuation or gain, between the
              signal and the AUX In input. The query form of this command returns the user-specified
              attenuation. Note that this command deals with an attenuation factor, not a gain
              factor, unlike ``CHX:PROBE`` (This command returns a value independent of the external
              attenuation). For example, if you specify a 20X attenuation factor, the commands
              return the following values (assuming that a 1x probe is presently attached, since the
              external attenuation is used in combination with the probe attenuation):
              ``AUXIN:PROBE:EXTA?`` 20.00E+0 ``AUXIN:PROBE?`` 1.0E+0 This command is equivalent to
              selecting Attenuation from the Vertical menu, and then either viewing or setting Ext
              Atten.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PROBEFunc:EXTAtten?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PROBEFunc:EXTAtten?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:PROBEFunc:EXTAtten value``
              command.

        SCPI Syntax:
            ```
            - AUXIn:PROBEFunc:EXTAtten <NR3>
            - AUXIn:PROBEFunc:EXTAtten?
            ```

        Info:
            - ``<NR3>`` is the attenuation value, which is specified as a multiplier in the range
              from 1.00E-10 to 1.00E+10.
        """
        return self._extatten

    @property
    def extdbatten(self) -> AuxinProbefuncExtdbatten:
        """Return the ``AUXIn:PROBEFunc:EXTDBatten`` command.

        Description:
            - This command sets the input-output ratio (expressed in decibel units) of external
              attenuation or gain between the signal and the instrument AUX In input. The query form
              of this command returns the user-specified attenuation in decibels: 1X = 0 dB, 10X =
              20 dB, 100X = 40 dB, and similar things. This command is equivalent to selecting
              Attenuation from the Vertical menu, and then either viewing or setting Ext Att(dB).

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PROBEFunc:EXTDBatten?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PROBEFunc:EXTDBatten?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:PROBEFunc:EXTDBatten value``
              command.

        SCPI Syntax:
            ```
            - AUXIn:PROBEFunc:EXTDBatten <NR3>
            - AUXIn:PROBEFunc:EXTDBatten?
            ```

        Info:
            - ``<NR3>`` is the attenuation value, which is specified in the range from -200.00 dB to
              200.00 dB.
        """
        return self._extdbatten

    @property
    def extunits(self) -> AuxinProbefuncExtunits:
        """Return the ``AUXIn:PROBEFunc:EXTUnits`` command.

        Description:
            - This command sets the unit of measurement for the external attenuator of the AUX In
              input. There is also a corresponding query that returns the user-specified unit of
              measurement for the external attenuator. Unless these units are set to the factory
              default string value of 'None', they become the attenuated units of measurement for
              the input. It is assumed that the probe connected to the input is of the correct type
              to receive the output of the user's external transducer or network.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PROBEFunc:EXTUnits?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PROBEFunc:EXTUnits?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:PROBEFunc:EXTUnits value``
              command.

        SCPI Syntax:
            ```
            - AUXIn:PROBEFunc:EXTUnits <QString>
            - AUXIn:PROBEFunc:EXTUnits?
            ```

        Info:
            - ``<QString>`` can contain a string of up to eight characters to indicate the
              attenuation unit of measurement for the AUX In input. However, most instrument
              attenuators only display the first two characters.
        """
        return self._extunits


class AuxinOffset(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:OFFSet`` command.

    Description:
        - This command sets or queries the vertical offset for the AUX In input. This command is
          equivalent to selecting Offset from the Vertical menu. This command offsets the vertical
          acquisition window (moves the level at the vertical center of the acquisition window) for
          the input. Visualize offset as scrolling the acquisition window towards the top of a large
          signal for increased offset values, and scrolling towards the bottom for decreased offset
          values. The resolution of the vertical window sets the offset increment for this control.
          Offset adjusts only the vertical center of the acquisition window to help determine what
          data is acquired. The instrument always displays the input signal minus the offset value.
          The channel reference marker will move to the vertical graticule position given by the
          negative of the offset value divided by the scale factor, unless that position is
          off-screen. If the computed coordinate for the reference mark is off-screen, the mark
          moves to the nearest screen limit and changes from a right-pointing arrow ( →) to an arrow
          pointing in the appropriate off-screen direction.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:OFFSet?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:OFFSet value`` command.

    SCPI Syntax:
        ```
        - AUXIn:OFFSet <NR3>
        - AUXIn:OFFSet?
        ```

    Info:
        - ``<NR3>`` is the offset value for the specified channel.
    """


class AuxinCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:COUPling`` command.

    Description:
        - This command sets or queries the input attenuator coupling setting for the AUX In input.
          The coupling will change with an appropriate probe attached. This command is equivalent to
          selecting Coupling from the Vertical menu.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:COUPling?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:COUPling value`` command.

    SCPI Syntax:
        ```
        - AUXIn:COUPling <NR3>
        - AUXIn:COUPling?
        ```

    Info:
        - ``<NR3>`` is one of the supported input attenuator couplings on the attached probe.
    """


class AuxinBandwidth(SCPICmdWrite, SCPICmdRead):
    """The ``AUXIn:BANdwidth`` command.

    Description:
        - This command sets or queries the selectable low-pass bandwidth limit filter of the AUX In
          input. The bandwidth will change with an appropriate probe attached. This is equivalent to
          selecting Bandwidth from the Vertical menu. The query form of this command always returns
          the maximum bandwidth of the AUX In input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn:BANdwidth?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn:BANdwidth?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXIn:BANdwidth value`` command.

    SCPI Syntax:
        ```
        - AUXIn:BANdwidth <NR3>
        - AUXIn:BANdwidth?
        ```

    Info:
        - ``<NR3>`` is one of the supported bandwidths on the attached probe.
    """


class Auxin(SCPICmdRead):
    """The ``AUXIn`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXIn?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXIn?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bandwidth``: The ``AUXIn:BANdwidth`` command.
        - ``.coupling``: The ``AUXIn:COUPling`` command.
        - ``.offset``: The ``AUXIn:OFFSet`` command.
        - ``.probefunc``: The ``AUXIn:PROBEFunc`` command tree.
        - ``.probe``: The ``AUXIn:PRObe`` command tree.
        - ``.vterm``: The ``AUXIn:VTERm`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUXIn") -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = AuxinBandwidth(device, f"{self._cmd_syntax}:BANdwidth")
        self._coupling = AuxinCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._offset = AuxinOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._probefunc = AuxinProbefunc(device, f"{self._cmd_syntax}:PROBEFunc")
        self._probe = AuxinProbe(device, f"{self._cmd_syntax}:PRObe")
        self._vterm = AuxinVterm(device, f"{self._cmd_syntax}:VTERm")

    @property
    def bandwidth(self) -> AuxinBandwidth:
        """Return the ``AUXIn:BANdwidth`` command.

        Description:
            - This command sets or queries the selectable low-pass bandwidth limit filter of the AUX
              In input. The bandwidth will change with an appropriate probe attached. This is
              equivalent to selecting Bandwidth from the Vertical menu. The query form of this
              command always returns the maximum bandwidth of the AUX In input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:BANdwidth?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:BANdwidth?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:BANdwidth value`` command.

        SCPI Syntax:
            ```
            - AUXIn:BANdwidth <NR3>
            - AUXIn:BANdwidth?
            ```

        Info:
            - ``<NR3>`` is one of the supported bandwidths on the attached probe.
        """
        return self._bandwidth

    @property
    def coupling(self) -> AuxinCoupling:
        """Return the ``AUXIn:COUPling`` command.

        Description:
            - This command sets or queries the input attenuator coupling setting for the AUX In
              input. The coupling will change with an appropriate probe attached. This command is
              equivalent to selecting Coupling from the Vertical menu.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:COUPling?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:COUPling value`` command.

        SCPI Syntax:
            ```
            - AUXIn:COUPling <NR3>
            - AUXIn:COUPling?
            ```

        Info:
            - ``<NR3>`` is one of the supported input attenuator couplings on the attached probe.
        """
        return self._coupling

    @property
    def offset(self) -> AuxinOffset:
        """Return the ``AUXIn:OFFSet`` command.

        Description:
            - This command sets or queries the vertical offset for the AUX In input. This command is
              equivalent to selecting Offset from the Vertical menu. This command offsets the
              vertical acquisition window (moves the level at the vertical center of the acquisition
              window) for the input. Visualize offset as scrolling the acquisition window towards
              the top of a large signal for increased offset values, and scrolling towards the
              bottom for decreased offset values. The resolution of the vertical window sets the
              offset increment for this control. Offset adjusts only the vertical center of the
              acquisition window to help determine what data is acquired. The instrument always
              displays the input signal minus the offset value. The channel reference marker will
              move to the vertical graticule position given by the negative of the offset value
              divided by the scale factor, unless that position is off-screen. If the computed
              coordinate for the reference mark is off-screen, the mark moves to the nearest screen
              limit and changes from a right-pointing arrow ( →) to an arrow pointing in the
              appropriate off-screen direction.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXIn:OFFSet value`` command.

        SCPI Syntax:
            ```
            - AUXIn:OFFSet <NR3>
            - AUXIn:OFFSet?
            ```

        Info:
            - ``<NR3>`` is the offset value for the specified channel.
        """
        return self._offset

    @property
    def probefunc(self) -> AuxinProbefunc:
        """Return the ``AUXIn:PROBEFunc`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PROBEFunc?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PROBEFunc?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.extatten``: The ``AUXIn:PROBEFunc:EXTAtten`` command.
            - ``.extdbatten``: The ``AUXIn:PROBEFunc:EXTDBatten`` command.
            - ``.extunits``: The ``AUXIn:PROBEFunc:EXTUnits`` command.
        """
        return self._probefunc

    @property
    def probe(self) -> AuxinProbe:
        """Return the ``AUXIn:PRObe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:PRObe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autozero``: The ``AUXIn:PRObe:AUTOZero`` command.
            - ``.degauss``: The ``AUXIn:PRObe:DEGAUSS`` command.
            - ``.forcedrange``: The ``AUXIn:PRObe:FORCEDRange`` command.
            - ``.gain``: The ``AUXIn:PRObe:GAIN`` command.
            - ``.id``: The ``AUXIn:PRObe:ID`` command tree.
            - ``.inputmode``: The ``AUXIn:PRObe:INPUTMode`` command.
            - ``.range``: The ``AUXIn:PRObe:RANge`` command.
            - ``.resistance``: The ``AUXIn:PRObe:RESistance`` command.
            - ``.set``: The ``AUXIn:PRObe:SET`` command.
            - ``.signal``: The ``AUXIn:PRObe:SIGnal`` command.
            - ``.tiptype``: The ``AUXIn:PRObe:TIPtype`` command.
            - ``.units``: The ``AUXIn:PRObe:UNIts`` command.
        """
        return self._probe

    @property
    def vterm(self) -> AuxinVterm:
        """Return the ``AUXIn:VTERm`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn:VTERm?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn:VTERm?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dual``: The ``AUXIn:VTERm:DUAL`` command tree.
        """
        return self._vterm
