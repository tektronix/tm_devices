"""The sv commands module.

These commands are used in the following models:
DPO7AX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SV:WINDOW {KAISerbessel|RECTangular|HAMMing|HANNing|BLACkmanharris|FLATtop2}
    - SV:WINDOW?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SvWindow(SCPICmdWrite, SCPICmdRead):
    """The ``SV:WINDOW`` command.

    Description:
        - This command sets or queries the window type used by the windowing function of the
          Spectrum View. The windowing function is a Fast Fourier Transform (FFT) technique used to
          minimize the discontinuities between successive frames of an RF time domain signal. The
          default window type is Blackman-Harris.

    Usage:
        - Using the ``.query()`` method will send the ``SV:WINDOW?`` query.
        - Using the ``.verify(value)`` method will send the ``SV:WINDOW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SV:WINDOW value`` command.

    SCPI Syntax:
        ```
        - SV:WINDOW {KAISerbessel|RECTangular|HAMMing|HANNing|BLACkmanharris|FLATtop2}
        - SV:WINDOW?
        ```

    Info:
        - ``KAISerbessel`` specifies the Kaiser-Bessel window type (a high or moderate resolution
          window).
        - ``RECTangular`` specifies the Rectangular window type (a window function is equivalent to
          multiplying all gate data by one).
        - ``HAMMing`` specifies the Hamming window type (a high or moderate resolution window based
          on a cosine series).
        - ``HANNing`` specifies the Hanning window type (a high or moderate resolution window based
          on a cosine series).
        - ``BLACkmanharris`` specifies the Blackman-Harris window type (a low-resolution (high
          dynamic range) window based on a cosine series).
        - ``FLATtop2`` specifies the Flattop2 window type (a low-resolution (high dynamic range)
          window).
    """


class Sv(SCPICmdRead):
    """The ``SV`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SV?`` query.
        - Using the ``.verify(value)`` method will send the ``SV?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.window``: The ``SV:WINDOW`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SV") -> None:
        super().__init__(device, cmd_syntax)
        self._window = SvWindow(device, f"{self._cmd_syntax}:WINDOW")

    @property
    def window(self) -> SvWindow:
        """Return the ``SV:WINDOW`` command.

        Description:
            - This command sets or queries the window type used by the windowing function of the
              Spectrum View. The windowing function is a Fast Fourier Transform (FFT) technique used
              to minimize the discontinuities between successive frames of an RF time domain signal.
              The default window type is Blackman-Harris.

        Usage:
            - Using the ``.query()`` method will send the ``SV:WINDOW?`` query.
            - Using the ``.verify(value)`` method will send the ``SV:WINDOW?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SV:WINDOW value`` command.

        SCPI Syntax:
            ```
            - SV:WINDOW {KAISerbessel|RECTangular|HAMMing|HANNing|BLACkmanharris|FLATtop2}
            - SV:WINDOW?
            ```

        Info:
            - ``KAISerbessel`` specifies the Kaiser-Bessel window type (a high or moderate
              resolution window).
            - ``RECTangular`` specifies the Rectangular window type (a window function is equivalent
              to multiplying all gate data by one).
            - ``HAMMing`` specifies the Hamming window type (a high or moderate resolution window
              based on a cosine series).
            - ``HANNing`` specifies the Hanning window type (a high or moderate resolution window
              based on a cosine series).
            - ``BLACkmanharris`` specifies the Blackman-Harris window type (a low-resolution (high
              dynamic range) window based on a cosine series).
            - ``FLATtop2`` specifies the Flattop2 window type (a low-resolution (high dynamic range)
              window).
        """
        return self._window
