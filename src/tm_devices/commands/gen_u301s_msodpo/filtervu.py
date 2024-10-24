"""The filtervu commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FILTERVu:FREQuency <NR3>
    - FILTERVu:FREQuency:AVAILable?
    - FILTERVu:FREQuency?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class FiltervuFrequencyAvailable(SCPICmdRead):
    """The ``FILTERVu:FREQuency:AVAILable`` command.

    Description:
        - Returns a comma separated list of filter frequencies available based on the current
          instrument settings. The source waveform (as specified by the ``DATA:SOURCE``) must be
          turned on for this query to generate a response.

    Usage:
        - Using the ``.query()`` method will send the ``FILTERVu:FREQuency:AVAILable?`` query.
        - Using the ``.verify(value)`` method will send the ``FILTERVu:FREQuency:AVAILable?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FILTERVu:FREQuency:AVAILable?
        ```
    """


class FiltervuFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``FILTERVu:FREQuency`` command.

    Description:
        - Sets or queries the FilterVu frequency to the closest value supported with the current
          acquisition settings.

    Usage:
        - Using the ``.query()`` method will send the ``FILTERVu:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``FILTERVu:FREQuency?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FILTERVu:FREQuency value`` command.

    SCPI Syntax:
        ```
        - FILTERVu:FREQuency <NR3>
        - FILTERVu:FREQuency?
        ```

    Info:
        - ``<NR3>`` is the integer format for the current FilterVu frequency setting.

    Properties:
        - ``.available``: The ``FILTERVu:FREQuency:AVAILable`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._available = FiltervuFrequencyAvailable(device, f"{self._cmd_syntax}:AVAILable")

    @property
    def available(self) -> FiltervuFrequencyAvailable:
        """Return the ``FILTERVu:FREQuency:AVAILable`` command.

        Description:
            - Returns a comma separated list of filter frequencies available based on the current
              instrument settings. The source waveform (as specified by the ``DATA:SOURCE``) must be
              turned on for this query to generate a response.

        Usage:
            - Using the ``.query()`` method will send the ``FILTERVu:FREQuency:AVAILable?`` query.
            - Using the ``.verify(value)`` method will send the ``FILTERVu:FREQuency:AVAILable?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILTERVu:FREQuency:AVAILable?
            ```
        """
        return self._available


class Filtervu(SCPICmdRead):
    """The ``FILTERVu`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FILTERVu?`` query.
        - Using the ``.verify(value)`` method will send the ``FILTERVu?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``FILTERVu:FREQuency`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "FILTERVu") -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = FiltervuFrequency(device, f"{self._cmd_syntax}:FREQuency")

    @property
    def frequency(self) -> FiltervuFrequency:
        """Return the ``FILTERVu:FREQuency`` command.

        Description:
            - Sets or queries the FilterVu frequency to the closest value supported with the current
              acquisition settings.

        Usage:
            - Using the ``.query()`` method will send the ``FILTERVu:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``FILTERVu:FREQuency?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FILTERVu:FREQuency value`` command.

        SCPI Syntax:
            ```
            - FILTERVu:FREQuency <NR3>
            - FILTERVu:FREQuency?
            ```

        Info:
            - ``<NR3>`` is the integer format for the current FilterVu frequency setting.

        Sub-properties:
            - ``.available``: The ``FILTERVu:FREQuency:AVAILable`` command.
        """
        return self._frequency
