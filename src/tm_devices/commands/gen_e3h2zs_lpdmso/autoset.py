"""The autoset commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUTOSet EXECute
    - AUTOSet:ACQuisition:ENAble {ON|1|OFF|0}
    - AUTOSet:ACQuisition:ENAble?
    - AUTOSet:ENAble {ON|1|OFF|0}
    - AUTOSet:ENAble?
    - AUTOSet:HORizontal:ENAble {ON|1|OFF|0}
    - AUTOSet:HORizontal:ENAble?
    - AUTOSet:TRIGger:ENAble {ON|1|OFF|0}
    - AUTOSet:TRIGger:ENAble?
    - AUTOSet:VERTical:ENAble {ON|1|OFF|0}
    - AUTOSet:VERTical:ENAble?
    - AUTOSet:VERTical:OPTIMize {RESOlution|VISIBility}
    - AUTOSet:VERTical:OPTIMize?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AutosetVerticalOptimize(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet:VERTical:OPTIMize`` command.

    Description:
        - This command sets or queries which vertical settings Autoset will optimize when the
          display mode is set to Overlay mode (all waveforms are in one common graticule in the
          Waveform View).

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:VERTical:OPTIMize?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:VERTical:OPTIMize?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUTOSet:VERTical:OPTIMize value``
          command.

    SCPI Syntax:
        ```
        - AUTOSet:VERTical:OPTIMize {RESOlution|VISIBility}
        - AUTOSet:VERTical:OPTIMize?
        ```

    Info:
        - ``RESOlution`` uses as much of the ADC's (Analog to Digital Converter) range as possible
          to provide the best vertical resolution and measurement accuracy, but waveforms will
          overlap each other.
        - ``VISIBility`` vertically scales and positions waveforms so they are visually separated
          from each other at the expense of vertical resolution and measurement accuracy.
    """


class AutosetVerticalEnable(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet:VERTical:ENAble`` command.

    Description:
        - This command sets or queries Autoset's adjustment of vertical settings. Settings affected
          may include, but not be limited to, vertical scale, vertical position, and vertical
          offset.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:VERTical:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:VERTical:ENAble?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUTOSet:VERTical:ENAble value``
          command.

    SCPI Syntax:
        ```
        - AUTOSet:VERTical:ENAble {ON|1|OFF|0}
        - AUTOSet:VERTical:ENAble?
        ```

    Info:
        - ``ON`` or 1 enables Autoset to change vertical settings.
        - ``OFF`` or 0 disables Autoset from changing vertical settings.
    """


class AutosetVertical(SCPICmdRead):
    """The ``AUTOSet:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:VERTical?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``AUTOSet:VERTical:ENAble`` command.
        - ``.optimize``: The ``AUTOSet:VERTical:OPTIMize`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = AutosetVerticalEnable(device, f"{self._cmd_syntax}:ENAble")
        self._optimize = AutosetVerticalOptimize(device, f"{self._cmd_syntax}:OPTIMize")

    @property
    def enable(self) -> AutosetVerticalEnable:
        """Return the ``AUTOSet:VERTical:ENAble`` command.

        Description:
            - This command sets or queries Autoset's adjustment of vertical settings. Settings
              affected may include, but not be limited to, vertical scale, vertical position, and
              vertical offset.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:VERTical:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:VERTical:ENAble?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUTOSet:VERTical:ENAble value``
              command.

        SCPI Syntax:
            ```
            - AUTOSet:VERTical:ENAble {ON|1|OFF|0}
            - AUTOSet:VERTical:ENAble?
            ```

        Info:
            - ``ON`` or 1 enables Autoset to change vertical settings.
            - ``OFF`` or 0 disables Autoset from changing vertical settings.
        """
        return self._enable

    @property
    def optimize(self) -> AutosetVerticalOptimize:
        """Return the ``AUTOSet:VERTical:OPTIMize`` command.

        Description:
            - This command sets or queries which vertical settings Autoset will optimize when the
              display mode is set to Overlay mode (all waveforms are in one common graticule in the
              Waveform View).

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:VERTical:OPTIMize?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:VERTical:OPTIMize?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUTOSet:VERTical:OPTIMize value``
              command.

        SCPI Syntax:
            ```
            - AUTOSet:VERTical:OPTIMize {RESOlution|VISIBility}
            - AUTOSet:VERTical:OPTIMize?
            ```

        Info:
            - ``RESOlution`` uses as much of the ADC's (Analog to Digital Converter) range as
              possible to provide the best vertical resolution and measurement accuracy, but
              waveforms will overlap each other.
            - ``VISIBility`` vertically scales and positions waveforms so they are visually
              separated from each other at the expense of vertical resolution and measurement
              accuracy.
        """
        return self._optimize


class AutosetTriggerEnable(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet:TRIGger:ENAble`` command.

    Description:
        - This command sets or queries Autoset's adjustment of trigger settings. Settings affected
          may include, but not be limited to, trigger level, trigger source, and trigger coupling.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:TRIGger:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:TRIGger:ENAble?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUTOSet:TRIGger:ENAble value`` command.

    SCPI Syntax:
        ```
        - AUTOSet:TRIGger:ENAble {ON|1|OFF|0}
        - AUTOSet:TRIGger:ENAble?
        ```

    Info:
        - ``ON`` or 1 enables Autoset to change trigger settings.
        - ``OFF`` or 0 disables Autoset from changing trigger settings.
    """


class AutosetTrigger(SCPICmdRead):
    """The ``AUTOSet:TRIGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:TRIGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``AUTOSet:TRIGger:ENAble`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = AutosetTriggerEnable(device, f"{self._cmd_syntax}:ENAble")

    @property
    def enable(self) -> AutosetTriggerEnable:
        """Return the ``AUTOSet:TRIGger:ENAble`` command.

        Description:
            - This command sets or queries Autoset's adjustment of trigger settings. Settings
              affected may include, but not be limited to, trigger level, trigger source, and
              trigger coupling.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:TRIGger:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:TRIGger:ENAble?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUTOSet:TRIGger:ENAble value``
              command.

        SCPI Syntax:
            ```
            - AUTOSet:TRIGger:ENAble {ON|1|OFF|0}
            - AUTOSet:TRIGger:ENAble?
            ```

        Info:
            - ``ON`` or 1 enables Autoset to change trigger settings.
            - ``OFF`` or 0 disables Autoset from changing trigger settings.
        """
        return self._enable


class AutosetHorizontalEnable(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet:HORizontal:ENAble`` command.

    Description:
        - This command sets or queries Autoset's adjustment of horizontal settings. Settings
          affected may include, but not be limited to, horizontal scale, horizontal position, and
          horizontal delay mode.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:HORizontal:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:HORizontal:ENAble?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUTOSet:HORizontal:ENAble value``
          command.

    SCPI Syntax:
        ```
        - AUTOSet:HORizontal:ENAble {ON|1|OFF|0}
        - AUTOSet:HORizontal:ENAble?
        ```

    Info:
        - ``ON`` or 1 enables Autoset to change horizontal settings.
        - ``OFF`` or 0 disables Autoset from changing horizontal settings.
    """


class AutosetHorizontal(SCPICmdRead):
    """The ``AUTOSet:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:HORizontal?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``AUTOSet:HORizontal:ENAble`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = AutosetHorizontalEnable(device, f"{self._cmd_syntax}:ENAble")

    @property
    def enable(self) -> AutosetHorizontalEnable:
        """Return the ``AUTOSet:HORizontal:ENAble`` command.

        Description:
            - This command sets or queries Autoset's adjustment of horizontal settings. Settings
              affected may include, but not be limited to, horizontal scale, horizontal position,
              and horizontal delay mode.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:HORizontal:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:HORizontal:ENAble?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUTOSet:HORizontal:ENAble value``
              command.

        SCPI Syntax:
            ```
            - AUTOSet:HORizontal:ENAble {ON|1|OFF|0}
            - AUTOSet:HORizontal:ENAble?
            ```

        Info:
            - ``ON`` or 1 enables Autoset to change horizontal settings.
            - ``OFF`` or 0 disables Autoset from changing horizontal settings.
        """
        return self._enable


class AutosetEnable(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet:ENAble`` command.

    Description:
        - This command sets or queries the Autoset enable/disable feature. This is useful for
          classroom purposes where the instructor wants the students to achieve the desired
          instrument settings without the benefit of the Autoset feature.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:ENAble?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUTOSet:ENAble value`` command.

    SCPI Syntax:
        ```
        - AUTOSet:ENAble {ON|1|OFF|0}
        - AUTOSet:ENAble?
        ```

    Info:
        - ``ON`` or 1 enables Autoset.
        - ``OFF`` or 0 disables Autoset.
    """


class AutosetAcquisitionEnable(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet:ACQuisition:ENAble`` command.

    Description:
        - This command sets or queries the Autoset acquisition setting adjustment. Settings affected
          may include, but not be limited to, acquisition mode, and FastAcq mode.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:ACQuisition:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:ACQuisition:ENAble?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUTOSet:ACQuisition:ENAble value``
          command.

    SCPI Syntax:
        ```
        - AUTOSet:ACQuisition:ENAble {ON|1|OFF|0}
        - AUTOSet:ACQuisition:ENAble?
        ```

    Info:
        - ``ON`` or 1 enables Autoset to change acquisition settings.
        - ``OFF`` or 0 disables Autoset from changing acquisition settings.
    """


class AutosetAcquisition(SCPICmdRead):
    """The ``AUTOSet:ACQuisition`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:ACQuisition?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:ACQuisition?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``AUTOSet:ACQuisition:ENAble`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = AutosetAcquisitionEnable(device, f"{self._cmd_syntax}:ENAble")

    @property
    def enable(self) -> AutosetAcquisitionEnable:
        """Return the ``AUTOSet:ACQuisition:ENAble`` command.

        Description:
            - This command sets or queries the Autoset acquisition setting adjustment. Settings
              affected may include, but not be limited to, acquisition mode, and FastAcq mode.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:ACQuisition:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:ACQuisition:ENAble?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUTOSet:ACQuisition:ENAble value``
              command.

        SCPI Syntax:
            ```
            - AUTOSet:ACQuisition:ENAble {ON|1|OFF|0}
            - AUTOSet:ACQuisition:ENAble?
            ```

        Info:
            - ``ON`` or 1 enables Autoset to change acquisition settings.
            - ``OFF`` or 0 disables Autoset from changing acquisition settings.
        """
        return self._enable


class Autoset(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet`` command.

    Description:
        - This command (no query format) sets the vertical, horizontal, and trigger controls of the
          instrument to automatically acquire and display the selected waveform.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUTOSet value`` command.

    SCPI Syntax:
        ```
        - AUTOSet EXECute
        ```

    Info:
        - ``EXECute`` autosets the displayed waveform; this is equivalent to pressing the front
          panel Autoset button.

    Properties:
        - ``.acquisition``: The ``AUTOSet:ACQuisition`` command tree.
        - ``.enable``: The ``AUTOSet:ENAble`` command.
        - ``.horizontal``: The ``AUTOSet:HORizontal`` command tree.
        - ``.trigger``: The ``AUTOSet:TRIGger`` command tree.
        - ``.vertical``: The ``AUTOSet:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUTOSet") -> None:
        super().__init__(device, cmd_syntax)
        self._acquisition = AutosetAcquisition(device, f"{self._cmd_syntax}:ACQuisition")
        self._enable = AutosetEnable(device, f"{self._cmd_syntax}:ENAble")
        self._horizontal = AutosetHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._trigger = AutosetTrigger(device, f"{self._cmd_syntax}:TRIGger")
        self._vertical = AutosetVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def acquisition(self) -> AutosetAcquisition:
        """Return the ``AUTOSet:ACQuisition`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:ACQuisition?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:ACQuisition?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``AUTOSet:ACQuisition:ENAble`` command.
        """
        return self._acquisition

    @property
    def enable(self) -> AutosetEnable:
        """Return the ``AUTOSet:ENAble`` command.

        Description:
            - This command sets or queries the Autoset enable/disable feature. This is useful for
              classroom purposes where the instructor wants the students to achieve the desired
              instrument settings without the benefit of the Autoset feature.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:ENAble?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUTOSet:ENAble value`` command.

        SCPI Syntax:
            ```
            - AUTOSet:ENAble {ON|1|OFF|0}
            - AUTOSet:ENAble?
            ```

        Info:
            - ``ON`` or 1 enables Autoset.
            - ``OFF`` or 0 disables Autoset.
        """
        return self._enable

    @property
    def horizontal(self) -> AutosetHorizontal:
        """Return the ``AUTOSet:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:HORizontal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``AUTOSet:HORizontal:ENAble`` command.
        """
        return self._horizontal

    @property
    def trigger(self) -> AutosetTrigger:
        """Return the ``AUTOSet:TRIGger`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:TRIGger?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``AUTOSet:TRIGger:ENAble`` command.
        """
        return self._trigger

    @property
    def vertical(self) -> AutosetVertical:
        """Return the ``AUTOSet:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:VERTical?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``AUTOSet:VERTical:ENAble`` command.
            - ``.optimize``: The ``AUTOSet:VERTical:OPTIMize`` command.
        """
        return self._vertical
