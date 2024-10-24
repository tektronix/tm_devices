"""The auxin commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUXin:PRObe
    - AUXin:PRObe:AUTOZero {EXECute}
    - AUXin:PRObe:COMMAND <QString>, <QString>
    - AUXin:PRObe:DEGAUss {EXECute}
    - AUXin:PRObe:DEGAUss:STATE?
    - AUXin:PRObe:FORCEDRange <NR3>
    - AUXin:PRObe:FORCEDRange?
    - AUXin:PRObe:GAIN <NR3>
    - AUXin:PRObe:GAIN?
    - AUXin:PRObe:ID:SERnumber?
    - AUXin:PRObe:ID:TYPE?
    - AUXin:PRObe:RESistance?
    - AUXin:PRObe:SIGnal {BYPass|PASS}
    - AUXin:PRObe:SIGnal?
    - AUXin:PRObe:UNIts?
    - AUXin:PRObe?
    - AUXin?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AuxinProbeUnits(SCPICmdRead):
    """The ``AUXin:PRObe:UNIts`` command.

    Description:
        - Returns a string describing the units of measure of the probe attached to the Aux Input
          connector.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXin:PRObe:UNIts?
        ```
    """


class AuxinProbeSignal(SCPICmdWrite, SCPICmdRead):
    """The ``AUXin:PRObe:SIGnal`` command.

    Description:
        - This command changes the input bypass setting on VPI probes that support input bypass, for
          example the TCP0001. If sent to a probe that does not support input bypass, it is ignored.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe:SIGnal?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:SIGnal?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXin:PRObe:SIGnal value`` command.

    SCPI Syntax:
        ```
        - AUXin:PRObe:SIGnal {BYPass|PASS}
        - AUXin:PRObe:SIGnal?
        ```

    Info:
        - ``ByPass`` sets the probe to Bypass mode.
        - ``PASS`` sets the probe to Pass mode.
    """


class AuxinProbeResistance(SCPICmdRead):
    """The ``AUXin:PRObe:RESistance`` command.

    Description:
        - Returns the resistance of the probe attached to the front panel Aux In connector.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe:RESistance?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:RESistance?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXin:PRObe:RESistance?
        ```
    """


class AuxinProbeIdType(SCPICmdRead):
    """The ``AUXin:PRObe:ID:TYPE`` command.

    Description:
        - Returns the type of probe that is attached to the auxiliary input.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe:ID:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:ID:TYPE?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXin:PRObe:ID:TYPE?
        ```
    """


class AuxinProbeIdSernumber(SCPICmdRead):
    """The ``AUXin:PRObe:ID:SERnumber`` command.

    Description:
        - Returns the serial number of the probe that is attached to the Aux Input connector.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe:ID:SERnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:ID:SERnumber?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXin:PRObe:ID:SERnumber?
        ```
    """


class AuxinProbeId(SCPICmdRead):
    """The ``AUXin:PRObe:ID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe:ID?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:ID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sernumber``: The ``AUXin:PRObe:ID:SERnumber`` command.
        - ``.type``: The ``AUXin:PRObe:ID:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sernumber = AuxinProbeIdSernumber(device, f"{self._cmd_syntax}:SERnumber")
        self._type = AuxinProbeIdType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def sernumber(self) -> AuxinProbeIdSernumber:
        """Return the ``AUXin:PRObe:ID:SERnumber`` command.

        Description:
            - Returns the serial number of the probe that is attached to the Aux Input connector.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe:ID:SERnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:ID:SERnumber?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXin:PRObe:ID:SERnumber?
            ```
        """
        return self._sernumber

    @property
    def type(self) -> AuxinProbeIdType:
        """Return the ``AUXin:PRObe:ID:TYPE`` command.

        Description:
            - Returns the type of probe that is attached to the auxiliary input.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe:ID:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:ID:TYPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXin:PRObe:ID:TYPE?
            ```
        """
        return self._type


class AuxinProbeGain(SCPICmdWrite, SCPICmdRead):
    """The ``AUXin:PRObe:GAIN`` command.

    Description:
        - Specifies the gain factor of a probe that is attached to the Aux Input connector.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe:GAIN?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:GAIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXin:PRObe:GAIN value`` command.

    SCPI Syntax:
        ```
        - AUXin:PRObe:GAIN <NR3>
        - AUXin:PRObe:GAIN?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the probe gain, which is probe
          dependent.
    """


class AuxinProbeForcedrange(SCPICmdWrite, SCPICmdRead):
    """The ``AUXin:PRObe:FORCEDRange`` command.

    Description:
        - Changes or returns the range on a TekVPI probe attached to the Aux Input connector.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe:FORCEDRange?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:FORCEDRange?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXin:PRObe:FORCEDRange value``
          command.

    SCPI Syntax:
        ```
        - AUXin:PRObe:FORCEDRange <NR3>
        - AUXin:PRObe:FORCEDRange?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the probe range, which is probe
          dependent.
    """


class AuxinProbeDegaussState(SCPICmdRead):
    """The ``AUXin:PRObe:DEGAUss:STATE`` command.

    Description:
        - Returns the state of the probe degauss ( NEEDED, RECOMMENDED, PASSED, FAILED, RUNNING ).
          The command will return PASSED for probes that do not support degauss operations.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe:DEGAUss:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:DEGAUss:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXin:PRObe:DEGAUss:STATE?
        ```
    """


class AuxinProbeDegauss(SCPICmdWrite, SCPICmdRead):
    """The ``AUXin:PRObe:DEGAUss`` command.

    Description:
        - Starts a degauss/autozero cycle on a TekVPI current probe attached to the Aux Input
          connector. If you send this command to a probe that does not support this function, it is
          ignored.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUXin:PRObe:DEGAUss value`` command.

    SCPI Syntax:
        ```
        - AUXin:PRObe:DEGAUss {EXECute}
        ```

    Info:
        - ``EXECute`` starts a probe degauss cycle.

    Properties:
        - ``.state``: The ``AUXin:PRObe:DEGAUss:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = AuxinProbeDegaussState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> AuxinProbeDegaussState:
        """Return the ``AUXin:PRObe:DEGAUss:STATE`` command.

        Description:
            - Returns the state of the probe degauss ( NEEDED, RECOMMENDED, PASSED, FAILED, RUNNING
              ). The command will return PASSED for probes that do not support degauss operations.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe:DEGAUss:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:DEGAUss:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXin:PRObe:DEGAUss:STATE?
            ```
        """
        return self._state


class AuxinProbeCommand(SCPICmdWrite):
    """The ``AUXin:PRObe:COMMAND`` command.

    Description:
        - Sets the state of the probe control specified with the first argument to the state
          specified with the second argument. The commands and states are unique to the attached
          probe type. Only certain VPI probes support this command. See the probe documentation for
          how to set these string arguments.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUXin:PRObe:COMMAND value`` command.

    SCPI Syntax:
        ```
        - AUXin:PRObe:COMMAND <QString>, <QString>
        ```

    Info:
        - ``<QString>`` are quoted strings specifying the probe command and value to set in the
          probe attached to the Aux Input connector.
    """


class AuxinProbeAutozero(SCPICmdWrite):
    """The ``AUXin:PRObe:AUTOZero`` command.

    Description:
        - Sets the TekVPI probe attached to the Aux In input to autozero. The oscilloscope will
          ignore this command if the Auxiliary input does not have a TekVPI probe connected to it.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUXin:PRObe:AUTOZero value`` command.

    SCPI Syntax:
        ```
        - AUXin:PRObe:AUTOZero {EXECute}
        ```

    Info:
        - ``EXECute`` sets the probe to autozero.
    """


#  pylint: disable=too-many-instance-attributes
class AuxinProbe(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``AUXin:PRObe`` command.

    Description:
        - Returns all information concerning the probe attached to Aux Input connector.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin:PRObe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``AUXin:PRObe`` command.

    SCPI Syntax:
        ```
        - AUXin:PRObe
        - AUXin:PRObe?
        ```

    Properties:
        - ``.autozero``: The ``AUXin:PRObe:AUTOZero`` command.
        - ``.command``: The ``AUXin:PRObe:COMMAND`` command.
        - ``.degauss``: The ``AUXin:PRObe:DEGAUss`` command.
        - ``.forcedrange``: The ``AUXin:PRObe:FORCEDRange`` command.
        - ``.gain``: The ``AUXin:PRObe:GAIN`` command.
        - ``.id``: The ``AUXin:PRObe:ID`` command tree.
        - ``.resistance``: The ``AUXin:PRObe:RESistance`` command.
        - ``.signal``: The ``AUXin:PRObe:SIGnal`` command.
        - ``.units``: The ``AUXin:PRObe:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autozero = AuxinProbeAutozero(device, f"{self._cmd_syntax}:AUTOZero")
        self._command = AuxinProbeCommand(device, f"{self._cmd_syntax}:COMMAND")
        self._degauss = AuxinProbeDegauss(device, f"{self._cmd_syntax}:DEGAUss")
        self._forcedrange = AuxinProbeForcedrange(device, f"{self._cmd_syntax}:FORCEDRange")
        self._gain = AuxinProbeGain(device, f"{self._cmd_syntax}:GAIN")
        self._id = AuxinProbeId(device, f"{self._cmd_syntax}:ID")
        self._resistance = AuxinProbeResistance(device, f"{self._cmd_syntax}:RESistance")
        self._signal = AuxinProbeSignal(device, f"{self._cmd_syntax}:SIGnal")
        self._units = AuxinProbeUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def autozero(self) -> AuxinProbeAutozero:
        """Return the ``AUXin:PRObe:AUTOZero`` command.

        Description:
            - Sets the TekVPI probe attached to the Aux In input to autozero. The oscilloscope will
              ignore this command if the Auxiliary input does not have a TekVPI probe connected to
              it.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUXin:PRObe:AUTOZero value``
              command.

        SCPI Syntax:
            ```
            - AUXin:PRObe:AUTOZero {EXECute}
            ```

        Info:
            - ``EXECute`` sets the probe to autozero.
        """
        return self._autozero

    @property
    def command(self) -> AuxinProbeCommand:
        """Return the ``AUXin:PRObe:COMMAND`` command.

        Description:
            - Sets the state of the probe control specified with the first argument to the state
              specified with the second argument. The commands and states are unique to the attached
              probe type. Only certain VPI probes support this command. See the probe documentation
              for how to set these string arguments.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUXin:PRObe:COMMAND value``
              command.

        SCPI Syntax:
            ```
            - AUXin:PRObe:COMMAND <QString>, <QString>
            ```

        Info:
            - ``<QString>`` are quoted strings specifying the probe command and value to set in the
              probe attached to the Aux Input connector.
        """
        return self._command

    @property
    def degauss(self) -> AuxinProbeDegauss:
        """Return the ``AUXin:PRObe:DEGAUss`` command.

        Description:
            - Starts a degauss/autozero cycle on a TekVPI current probe attached to the Aux Input
              connector. If you send this command to a probe that does not support this function, it
              is ignored.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUXin:PRObe:DEGAUss value``
              command.

        SCPI Syntax:
            ```
            - AUXin:PRObe:DEGAUss {EXECute}
            ```

        Info:
            - ``EXECute`` starts a probe degauss cycle.

        Sub-properties:
            - ``.state``: The ``AUXin:PRObe:DEGAUss:STATE`` command.
        """
        return self._degauss

    @property
    def forcedrange(self) -> AuxinProbeForcedrange:
        """Return the ``AUXin:PRObe:FORCEDRange`` command.

        Description:
            - Changes or returns the range on a TekVPI probe attached to the Aux Input connector.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe:FORCEDRange?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:FORCEDRange?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXin:PRObe:FORCEDRange value``
              command.

        SCPI Syntax:
            ```
            - AUXin:PRObe:FORCEDRange <NR3>
            - AUXin:PRObe:FORCEDRange?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the probe range, which is probe
              dependent.
        """
        return self._forcedrange

    @property
    def gain(self) -> AuxinProbeGain:
        """Return the ``AUXin:PRObe:GAIN`` command.

        Description:
            - Specifies the gain factor of a probe that is attached to the Aux Input connector.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe:GAIN?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:GAIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXin:PRObe:GAIN value`` command.

        SCPI Syntax:
            ```
            - AUXin:PRObe:GAIN <NR3>
            - AUXin:PRObe:GAIN?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the probe gain, which is probe
              dependent.
        """
        return self._gain

    @property
    def id(self) -> AuxinProbeId:
        """Return the ``AUXin:PRObe:ID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe:ID?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:ID?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sernumber``: The ``AUXin:PRObe:ID:SERnumber`` command.
            - ``.type``: The ``AUXin:PRObe:ID:TYPE`` command.
        """
        return self._id

    @property
    def resistance(self) -> AuxinProbeResistance:
        """Return the ``AUXin:PRObe:RESistance`` command.

        Description:
            - Returns the resistance of the probe attached to the front panel Aux In connector.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe:RESistance?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:RESistance?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXin:PRObe:RESistance?
            ```
        """
        return self._resistance

    @property
    def signal(self) -> AuxinProbeSignal:
        """Return the ``AUXin:PRObe:SIGnal`` command.

        Description:
            - This command changes the input bypass setting on VPI probes that support input bypass,
              for example the TCP0001. If sent to a probe that does not support input bypass, it is
              ignored.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe:SIGnal?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:SIGnal?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXin:PRObe:SIGnal value`` command.

        SCPI Syntax:
            ```
            - AUXin:PRObe:SIGnal {BYPass|PASS}
            - AUXin:PRObe:SIGnal?
            ```

        Info:
            - ``ByPass`` sets the probe to Bypass mode.
            - ``PASS`` sets the probe to Pass mode.
        """
        return self._signal

    @property
    def units(self) -> AuxinProbeUnits:
        """Return the ``AUXin:PRObe:UNIts`` command.

        Description:
            - Returns a string describing the units of measure of the probe attached to the Aux
              Input connector.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXin:PRObe:UNIts?
            ```
        """
        return self._units


class Auxin(SCPICmdRead):
    """The ``AUXin`` command.

    Description:
        - Returns all Aux Input connector parameters.

    Usage:
        - Using the ``.query()`` method will send the ``AUXin?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXin?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXin?
        ```

    Properties:
        - ``.probe``: The ``AUXin:PRObe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUXin") -> None:
        super().__init__(device, cmd_syntax)
        self._probe = AuxinProbe(device, f"{self._cmd_syntax}:PRObe")

    @property
    def probe(self) -> AuxinProbe:
        """Return the ``AUXin:PRObe`` command.

        Description:
            - Returns all information concerning the probe attached to Aux Input connector.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin:PRObe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``AUXin:PRObe`` command.

        SCPI Syntax:
            ```
            - AUXin:PRObe
            - AUXin:PRObe?
            ```

        Sub-properties:
            - ``.autozero``: The ``AUXin:PRObe:AUTOZero`` command.
            - ``.command``: The ``AUXin:PRObe:COMMAND`` command.
            - ``.degauss``: The ``AUXin:PRObe:DEGAUss`` command.
            - ``.forcedrange``: The ``AUXin:PRObe:FORCEDRange`` command.
            - ``.gain``: The ``AUXin:PRObe:GAIN`` command.
            - ``.id``: The ``AUXin:PRObe:ID`` command tree.
            - ``.resistance``: The ``AUXin:PRObe:RESistance`` command.
            - ``.signal``: The ``AUXin:PRObe:SIGnal`` command.
            - ``.units``: The ``AUXin:PRObe:UNIts`` command.
        """
        return self._probe
