"""The d commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - D<x>:LABEL <QString>
    - D<x>:LABEL?
    - D<x>:POSition <NR3>
    - D<x>:POSition?
    - D<x>:PROBE:ID:SERnumber?
    - D<x>:PROBE:ID:TYPe?
    - D<x>:THRESHold <NR3>
    - D<x>:THRESHold?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDigitalBit

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DigitalBitThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``D<x>:THRESHold`` command.

    Description:
        - This command sets or queries the threshold level for the specified digital signal.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:THRESHold?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``D<x>:THRESHold value`` command.

    SCPI Syntax:
        ```
        - D<x>:THRESHold <NR3>
        - D<x>:THRESHold?
        ```

    Info:
        - ``<NR3>`` specifies the threshold level in volts.
    """


class DigitalBitProbeIdType(SCPICmdRead):
    """The ``D<x>:PROBE:ID:TYPe`` command.

    Description:
        - This command queries the type of digital probe that provides the specified digital signal.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:PROBE:ID:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:PROBE:ID:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - D<x>:PROBE:ID:TYPe?
        ```
    """


class DigitalBitProbeIdSernumber(SCPICmdRead):
    """The ``D<x>:PROBE:ID:SERnumber`` command.

    Description:
        - This command queries the serial number of the digital probe that provides the specified
          digital signal.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:PROBE:ID:SERnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:PROBE:ID:SERnumber?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - D<x>:PROBE:ID:SERnumber?
        ```
    """


class DigitalBitProbeId(SCPICmdRead):
    """The ``D<x>:PROBE:ID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:PROBE:ID?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:PROBE:ID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sernumber``: The ``D<x>:PROBE:ID:SERnumber`` command.
        - ``.type``: The ``D<x>:PROBE:ID:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sernumber = DigitalBitProbeIdSernumber(device, f"{self._cmd_syntax}:SERnumber")
        self._type = DigitalBitProbeIdType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def sernumber(self) -> DigitalBitProbeIdSernumber:
        """Return the ``D<x>:PROBE:ID:SERnumber`` command.

        Description:
            - This command queries the serial number of the digital probe that provides the
              specified digital signal.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:PROBE:ID:SERnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:PROBE:ID:SERnumber?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - D<x>:PROBE:ID:SERnumber?
            ```
        """
        return self._sernumber

    @property
    def type(self) -> DigitalBitProbeIdType:
        """Return the ``D<x>:PROBE:ID:TYPe`` command.

        Description:
            - This command queries the type of digital probe that provides the specified digital
              signal.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:PROBE:ID:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:PROBE:ID:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - D<x>:PROBE:ID:TYPe?
            ```
        """
        return self._type


class DigitalBitProbe(SCPICmdRead):
    """The ``D<x>:PROBE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:PROBE?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:PROBE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.id``: The ``D<x>:PROBE:ID`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._id = DigitalBitProbeId(device, f"{self._cmd_syntax}:ID")

    @property
    def id(self) -> DigitalBitProbeId:
        """Return the ``D<x>:PROBE:ID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:PROBE:ID?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:PROBE:ID?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sernumber``: The ``D<x>:PROBE:ID:SERnumber`` command.
            - ``.type``: The ``D<x>:PROBE:ID:TYPe`` command.
        """
        return self._id


class DigitalBitPosition(SCPICmdWrite, SCPICmdRead):
    """The ``D<x>:POSition`` command.

    Description:
        - This command specifies the vertical position for digital channel <x>, where x is the
          channel number.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:POSition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``D<x>:POSition value`` command.

    SCPI Syntax:
        ```
        - D<x>:POSition <NR3>
        - D<x>:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the position of the digital channel,
          in slot units. Use the oscilloscope front-panel controls to place the channel; then query
          the channel to obtain an exact value for the position.
    """


class DigitalBitLabel(SCPICmdWrite, SCPICmdRead):
    """The ``D<x>:LABEL`` command.

    Description:
        - This command sets or queries the label that appears for the specified digital input on the
          display.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:LABEL?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:LABEL?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``D<x>:LABEL value`` command.

    SCPI Syntax:
        ```
        - D<x>:LABEL <QString>
        - D<x>:LABEL?
        ```

    Info:
        - ``<QString>`` is an alphanumeric string of characters, enclosed in quotes, that defines
          the label text.
    """

    _WRAP_ARG_WITH_QUOTES = True


class DigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``D<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.label``: The ``D<x>:LABEL`` command.
        - ``.position``: The ``D<x>:POSition`` command.
        - ``.probe``: The ``D<x>:PROBE`` command tree.
        - ``.threshold``: The ``D<x>:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "D<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._label = DigitalBitLabel(device, f"{self._cmd_syntax}:LABEL")
        self._position = DigitalBitPosition(device, f"{self._cmd_syntax}:POSition")
        self._probe = DigitalBitProbe(device, f"{self._cmd_syntax}:PROBE")
        self._threshold = DigitalBitThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def label(self) -> DigitalBitLabel:
        """Return the ``D<x>:LABEL`` command.

        Description:
            - This command sets or queries the label that appears for the specified digital input on
              the display.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:LABEL?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:LABEL?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``D<x>:LABEL value`` command.

        SCPI Syntax:
            ```
            - D<x>:LABEL <QString>
            - D<x>:LABEL?
            ```

        Info:
            - ``<QString>`` is an alphanumeric string of characters, enclosed in quotes, that
              defines the label text.
        """
        return self._label

    @property
    def position(self) -> DigitalBitPosition:
        """Return the ``D<x>:POSition`` command.

        Description:
            - This command specifies the vertical position for digital channel <x>, where x is the
              channel number.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:POSition?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``D<x>:POSition value`` command.

        SCPI Syntax:
            ```
            - D<x>:POSition <NR3>
            - D<x>:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the position of the digital
              channel, in slot units. Use the oscilloscope front-panel controls to place the
              channel; then query the channel to obtain an exact value for the position.
        """
        return self._position

    @property
    def probe(self) -> DigitalBitProbe:
        """Return the ``D<x>:PROBE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:PROBE?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:PROBE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.id``: The ``D<x>:PROBE:ID`` command tree.
        """
        return self._probe

    @property
    def threshold(self) -> DigitalBitThreshold:
        """Return the ``D<x>:THRESHold`` command.

        Description:
            - This command sets or queries the threshold level for the specified digital signal.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:THRESHold?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``D<x>:THRESHold value`` command.

        SCPI Syntax:
            ```
            - D<x>:THRESHold <NR3>
            - D<x>:THRESHold?
            ```

        Info:
            - ``<NR3>`` specifies the threshold level in volts.
        """
        return self._threshold
