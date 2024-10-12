"""The zoom commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ZOOm {RESET|RESETLive}
    - ZOOm:GRAticule:SIZE {50|80|100}
    - ZOOm:GRAticule:SIZE?
    - ZOOm:GRAticule:SPLit {FIFtyfifty|EIGHtytwenty|FuLl}
    - ZOOm:GRAticule:SPLit?
    - ZOOm:HORizontal:POSition <NR3>
    - ZOOm:HORizontal:POSition?
    - ZOOm:HORizontal:SCAle <NR3>
    - ZOOm:HORizontal:SCAle?
    - ZOOm:MATH<x>:HORizontal:POSition <NR3>
    - ZOOm:MATH<x>:HORizontal:POSition?
    - ZOOm:MATH<x>:HORizontal:SCAle <NR3>
    - ZOOm:MATH<x>:HORizontal:SCAle?
    - ZOOm:MATH<x>:VERTical:POSition <NR3>
    - ZOOm:MATH<x>:VERTical:POSition?
    - ZOOm:MATH<x>:VERTical:SCAle <NR3>
    - ZOOm:MATH<x>:VERTical:SCAle?
    - ZOOm:MODe {ON|OFF|<NR1>}
    - ZOOm:REF<x>:HORizontal:POSition <NR3>
    - ZOOm:REF<x>:HORizontal:POSition?
    - ZOOm:REF<x>:HORizontal:SCAle <NR3>
    - ZOOm:REF<x>:HORizontal:SCAle?
    - ZOOm:REF<x>:VERTical:POSition <NR3>
    - ZOOm:REF<x>:VERTical:POSition?
    - ZOOm:REF<x>:VERTical:SCAle <NR3>
    - ZOOm:REF<x>:VERTical:SCAle?
    - ZOOm:SCROLL:DIREction {FWD|FFWD|REV|FREV|STOP}
    - ZOOm:SCROLL:DIREction?
    - ZOOm:SCROLL:LOCk {ON|OFF|<NR1>}
    - ZOOm:SCROLL:LOCk?
    - ZOOm:SCROLL:SPEED <NR1>
    - ZOOm:SCROLL:SPEED?
    - ZOOm:STATE {ON|OFF|<NR1>}
    - ZOOm:STATE?
    - ZOOm:VERTical:POSition <NR3>
    - ZOOm:VERTical:POSition?
    - ZOOm:VERTical:SCAle <NR3>
    - ZOOm:VERTical:SCAle?
    - ZOOm:ZOOM1 {RESET|RESETLive}
    - ZOOm:ZOOM1:CH<x>:DISplay {ON|OFF|<NR1>}
    - ZOOm:ZOOM1:CH<x>:DISplay?
    - ZOOm:ZOOM1:CH<x>:HORizontal:POSition <NR3>
    - ZOOm:ZOOM1:CH<x>:HORizontal:POSition?
    - ZOOm:ZOOM1:CH<x>:HORizontal:SCAle <NR3>
    - ZOOm:ZOOM1:CH<x>:HORizontal:SCAle?
    - ZOOm:ZOOM1:CH<x>:VERTical:POSition <NR3>
    - ZOOm:ZOOM1:CH<x>:VERTical:POSition?
    - ZOOm:ZOOM1:CH<x>:VERTical:SCAle <NR3>
    - ZOOm:ZOOM1:CH<x>:VERTical:SCAle?
    - ZOOm:ZOOM1:D<x>:DISplay {ON|OFF|<NR1>}
    - ZOOm:ZOOM1:D<x>:DISplay?
    - ZOOm:ZOOM1:D<x>:HORizontal:POSition <NR3>
    - ZOOm:ZOOM1:D<x>:HORizontal:POSition?
    - ZOOm:ZOOM1:D<x>:HORizontal:SCAle <NR3>
    - ZOOm:ZOOM1:D<x>:HORizontal:SCAle?
    - ZOOm:ZOOM1:D<x>:VERTical:POSition <NR3>
    - ZOOm:ZOOM1:D<x>:VERTical:POSition?
    - ZOOm:ZOOM1:D<x>:VERTical:SCAle <NR3>
    - ZOOm:ZOOM1:D<x>:VERTical:SCAle?
    - ZOOm:ZOOM1:DCHAN:DISplay {ON|OFF|<NR1>}
    - ZOOm:ZOOM1:DCHAN:DISplay?
    - ZOOm:ZOOM1:MATH<x>:DISplay {ON|OFF|<NR1>}
    - ZOOm:ZOOM1:MATH<x>:DISplay?
    - ZOOm:ZOOM1:MATH<x>:HORizontal:POSition <NR3>
    - ZOOm:ZOOM1:MATH<x>:HORizontal:POSition?
    - ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle <NR3>
    - ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle?
    - ZOOm:ZOOM1:MATH<x>:VERTical:POSition <NR3>
    - ZOOm:ZOOM1:MATH<x>:VERTical:POSition?
    - ZOOm:ZOOM1:MATH<x>:VERTical:SCAle <NR3>
    - ZOOm:ZOOM1:MATH<x>:VERTical:SCAle?
    - ZOOm:ZOOM1:REF<x>:DISplay {ON|OFF|<NR1>}
    - ZOOm:ZOOM1:REF<x>:DISplay?
    - ZOOm:ZOOM1:REF<x>:HORizontal:POSition <NR3>
    - ZOOm:ZOOM1:REF<x>:HORizontal:POSition?
    - ZOOm:ZOOM1:REF<x>:HORizontal:SCAle <NR3>
    - ZOOm:ZOOM1:REF<x>:HORizontal:SCAle?
    - ZOOm:ZOOM1:REF<x>:VERTical:POSition <NR3>
    - ZOOm:ZOOM1:REF<x>:VERTical:POSition?
    - ZOOm:ZOOM1:REF<x>:VERTical:SCAle <NR3>
    - ZOOm:ZOOM1:REF<x>:VERTical:SCAle?
    - ZOOm:ZOOM1:SCROLLLock {ON|OFF|<NR1>}
    - ZOOm:ZOOM1:SCROLLLock?
    - ZOOm:ZOOM1:STATE {ON|OFF|<NR1>}
    - ZOOm:ZOOM1:STATE?
    - ZOOm:ZOOM1?
    - ZOOm?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedChannel,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ZoomZoom1State(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:STATE`` command.

    Description:
        - This command turns the specified zoom on or off. <x> can only be 1.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:STATE value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:STATE {ON|OFF|<NR1>}
        - ZOOm:ZOOM1:STATE?
        ```

    Info:
        - ``ON`` turns Zoom 1 on.
        - ``OFF`` turns Zoom 1 off.
        - ``<NR1>`` is an integer. 0 disables the specified zoom; any other value enables the
          specified zoom.
    """


class ZoomZoom1Scrolllock(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:SCROLLLock`` command.

    Description:
        - This command sets or queries Scroll Lock for the specified zoom, where x is an integer
          from 1 to 4 representing the desired zoom window.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:SCROLLLock?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:SCROLLLock?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:SCROLLLock value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:SCROLLLock {ON|OFF|<NR1>}
        - ZOOm:ZOOM1:SCROLLLock?
        ```

    Info:
        - ``ON`` locks waveforms for the specified zoom window <x>.
        - ``OFF`` unlocks waveforms for the specified zoom window <x>.
        - ``<NR1>`` = 0 unlocks waveforms for the specified zoom window <x>; any other value locks
          waveforms for the specified zoom window <x>.
    """


class ZoomZoom1RefItemVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle`` command.

    Description:
        - This command sets or queries the zoom vertical scale of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1,
          Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:REF<x>:VERTical:SCAle <NR3>
        - ZOOm:ZOOM1:REF<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of vertical expansion or compression, which operates on a 1-2-5
          sequence (for example, 1, 2, 5, 10, 20, 50, 100...). Based on the value that you entered,
          this command uses the nearest scale factor. Setting the vertical scale to 1 indicates
          unity (no zoom).
    """


class ZoomZoom1RefItemVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:REF<x>:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The setting of the ``ZOOm:1:SCROLLLOCk`` command determines the waveforms that are
          affected. The <wfm> can be a channel, math, or reference waveform. The waveform affected
          is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4,
          Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:REF<x>:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:REF<x>:VERTical:POSition <NR3>
        - ZOOm:ZOOM1:REF<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position, expressed in divisions.
    """


class ZoomZoom1RefItemVertical(SCPICmdRead):
    """The ``ZOOm:ZOOM1:REF<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:ZOOM1:REF<x>:VERTical:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomZoom1RefItemVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomZoom1RefItemVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomZoom1RefItemVerticalPosition:
        """Return the ``ZOOm:ZOOM1:REF<x>:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The setting of the ``ZOOm:1:SCROLLLOCk`` command determines the waveforms that
              are affected. The <wfm> can be a channel, math, or reference waveform. The waveform
              affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2,
              Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:REF<x>:VERTical:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:REF<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:REF<x>:VERTical:POSition <NR3>
            - ZOOm:ZOOM1:REF<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position, expressed in divisions.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1RefItemVerticalScale:
        """Return the ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle`` command.

        Description:
            - This command sets or queries the zoom vertical scale of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
              CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:REF<x>:VERTical:SCAle <NR3>
            - ZOOm:ZOOM1:REF<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of vertical expansion or compression, which operates on a
              1-2-5 sequence (for example, 1, 2, 5, 10, 20, 50, 100...). Based on the value that you
              entered, this command uses the nearest scale factor. Setting the vertical scale to 1
              indicates unity (no zoom).
        """
        return self._scale


class ZoomZoom1RefItemHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle`` command.

    Description:
        - This command sets or queries the zoom horizontal scale factor of the specified waveform
          for the specified zoom, where x is an integer from 1 to 4 representing the desired zoom
          window. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
          CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:REF<x>:HORizontal:SCAle <NR3>
        - ZOOm:ZOOM1:REF<x>:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
    """


class ZoomZoom1RefItemHorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal position of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The setting of the ``ZOOM:ZOOMX:SCROLLLOCK`` command determines the waveforms that are
          affected. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
          CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:REF<x>:HORizontal:POSition <NR3>
        - ZOOm:ZOOM1:REF<x>:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to the
          left of screen center, when the zoom factor is 1× or greater.
    """


class ZoomZoom1RefItemHorizontal(SCPICmdRead):
    """The ``ZOOm:ZOOM1:REF<x>:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:HORizontal?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomZoom1RefItemHorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomZoom1RefItemHorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomZoom1RefItemHorizontalPosition:
        """Return the ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal position of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The setting of the ``ZOOM:ZOOMX:SCROLLLOCK`` command determines the waveforms
              that are affected. The waveform affected is determine by <wfm> which can vary from
              CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:REF<x>:HORizontal:POSition <NR3>
            - ZOOm:ZOOM1:REF<x>:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to
              the left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1RefItemHorizontalScale:
        """Return the ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle`` command.

        Description:
            - This command sets or queries the zoom horizontal scale factor of the specified
              waveform for the specified zoom, where x is an integer from 1 to 4 representing the
              desired zoom window. The waveform affected is determine by <wfm> which can vary from
              CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:REF<x>:HORizontal:SCAle <NR3>
            - ZOOm:ZOOM1:REF<x>:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
        """
        return self._scale


class ZoomZoom1RefItemDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:REF<x>:DISplay`` command.

    Description:
        - This command sets or queries the display of the specified waveform for the specified zoom,
          where x is an integer from 1 to 4 representing the desired zoom window. The waveform
          affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2,
          Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:DISplay value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:REF<x>:DISplay {ON|OFF|<NR1>}
        - ZOOm:ZOOM1:REF<x>:DISplay?
        ```

    Info:
        - ``<NR1>`` A zero disables the specified zoom; any other value enables the specified zoom.
        - ``OFF`` disables the specified zoom.
        - ``ON`` displays the specified zoom.
    """


class ZoomZoom1RefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``ZOOm:ZOOM1:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.display``: The ``ZOOm:ZOOM1:REF<x>:DISplay`` command.
        - ``.horizontal``: The ``ZOOm:ZOOM1:REF<x>:HORizontal`` command tree.
        - ``.vertical``: The ``ZOOm:ZOOM1:REF<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._display = ZoomZoom1RefItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._horizontal = ZoomZoom1RefItemHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._vertical = ZoomZoom1RefItemVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def display(self) -> ZoomZoom1RefItemDisplay:
        """Return the ``ZOOm:ZOOM1:REF<x>:DISplay`` command.

        Description:
            - This command sets or queries the display of the specified waveform for the specified
              zoom, where x is an integer from 1 to 4 representing the desired zoom window. The
              waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1,
              Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:DISplay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:DISplay value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:REF<x>:DISplay {ON|OFF|<NR1>}
            - ZOOm:ZOOM1:REF<x>:DISplay?
            ```

        Info:
            - ``<NR1>`` A zero disables the specified zoom; any other value enables the specified
              zoom.
            - ``OFF`` disables the specified zoom.
            - ``ON`` displays the specified zoom.
        """
        return self._display

    @property
    def horizontal(self) -> ZoomZoom1RefItemHorizontal:
        """Return the ``ZOOm:ZOOM1:REF<x>:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:HORizontal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:ZOOM1:REF<x>:HORizontal:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:REF<x>:HORizontal:SCAle`` command.
        """
        return self._horizontal

    @property
    def vertical(self) -> ZoomZoom1RefItemVertical:
        """Return the ``ZOOm:ZOOM1:REF<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>:VERTical?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:ZOOM1:REF<x>:VERTical:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:REF<x>:VERTical:SCAle`` command.
        """
        return self._vertical


class ZoomZoom1MathItemVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle`` command.

    Description:
        - This command sets or queries the zoom vertical scale of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1,
          Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:MATH<x>:VERTical:SCAle <NR3>
        - ZOOm:ZOOM1:MATH<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of vertical expansion or compression, which operates on a 1-2-5
          sequence (for example, 1, 2, 5, 10, 20, 50, 100...). Based on the value that you entered,
          this command uses the nearest scale factor. Setting the vertical scale to 1 indicates
          unity (no zoom).
    """


class ZoomZoom1MathItemVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The setting of the ``ZOOm:1:SCROLLLOCk`` command determines the waveforms that are
          affected. The <wfm> can be a channel, math, or reference waveform. The waveform affected
          is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4,
          Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:MATH<x>:VERTical:POSition <NR3>
        - ZOOm:ZOOM1:MATH<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position, expressed in divisions.
    """


class ZoomZoom1MathItemVertical(SCPICmdRead):
    """The ``ZOOm:ZOOM1:MATH<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:VERTical?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomZoom1MathItemVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomZoom1MathItemVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomZoom1MathItemVerticalPosition:
        """Return the ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The setting of the ``ZOOm:1:SCROLLLOCk`` command determines the waveforms that
              are affected. The <wfm> can be a channel, math, or reference waveform. The waveform
              affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2,
              Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:MATH<x>:VERTical:POSition <NR3>
            - ZOOm:ZOOM1:MATH<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position, expressed in divisions.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1MathItemVerticalScale:
        """Return the ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle`` command.

        Description:
            - This command sets or queries the zoom vertical scale of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
              CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:MATH<x>:VERTical:SCAle <NR3>
            - ZOOm:ZOOM1:MATH<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of vertical expansion or compression, which operates on a
              1-2-5 sequence (for example, 1, 2, 5, 10, 20, 50, 100...). Based on the value that you
              entered, this command uses the nearest scale factor. Setting the vertical scale to 1
              indicates unity (no zoom).
        """
        return self._scale


class ZoomZoom1MathItemHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle`` command.

    Description:
        - This command sets or queries the zoom horizontal scale factor of the specified waveform
          for the specified zoom, where x is an integer from 1 to 4 representing the desired zoom
          window. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
          CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle?``
          query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle <NR3>
        - ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
    """


class ZoomZoom1MathItemHorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal position of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The setting of the ``ZOOM:ZOOMX:SCROLLLOCK`` command determines the waveforms that are
          affected. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
          CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:MATH<x>:HORizontal:POSition <NR3>
        - ZOOm:ZOOM1:MATH<x>:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to the
          left of screen center, when the zoom factor is 1× or greater.
    """


class ZoomZoom1MathItemHorizontal(SCPICmdRead):
    """The ``ZOOm:ZOOM1:MATH<x>:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:HORizontal?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomZoom1MathItemHorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomZoom1MathItemHorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomZoom1MathItemHorizontalPosition:
        """Return the ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal position of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The setting of the ``ZOOM:ZOOMX:SCROLLLOCK`` command determines the waveforms
              that are affected. The waveform affected is determine by <wfm> which can vary from
              CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the
              ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:MATH<x>:HORizontal:POSition <NR3>
            - ZOOm:ZOOM1:MATH<x>:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to
              the left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1MathItemHorizontalScale:
        """Return the ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle`` command.

        Description:
            - This command sets or queries the zoom horizontal scale factor of the specified
              waveform for the specified zoom, where x is an integer from 1 to 4 representing the
              desired zoom window. The waveform affected is determine by <wfm> which can vary from
              CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle <NR3>
            - ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
        """
        return self._scale


class ZoomZoom1MathItemDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:MATH<x>:DISplay`` command.

    Description:
        - This command sets or queries the display of the specified waveform for the specified zoom,
          where x is an integer from 1 to 4 representing the desired zoom window. The waveform
          affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2,
          Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:DISplay?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:DISplay value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:MATH<x>:DISplay {ON|OFF|<NR1>}
        - ZOOm:ZOOM1:MATH<x>:DISplay?
        ```

    Info:
        - ``<NR1>`` A zero disables the specified zoom; any other value enables the specified zoom.
        - ``OFF`` disables the specified zoom.
        - ``ON`` displays the specified zoom.
    """


class ZoomZoom1MathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``ZOOm:ZOOM1:MATH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.display``: The ``ZOOm:ZOOM1:MATH<x>:DISplay`` command.
        - ``.horizontal``: The ``ZOOm:ZOOM1:MATH<x>:HORizontal`` command tree.
        - ``.vertical``: The ``ZOOm:ZOOM1:MATH<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._display = ZoomZoom1MathItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._horizontal = ZoomZoom1MathItemHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._vertical = ZoomZoom1MathItemVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def display(self) -> ZoomZoom1MathItemDisplay:
        """Return the ``ZOOm:ZOOM1:MATH<x>:DISplay`` command.

        Description:
            - This command sets or queries the display of the specified waveform for the specified
              zoom, where x is an integer from 1 to 4 representing the desired zoom window. The
              waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1,
              Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:DISplay?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:DISplay value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:MATH<x>:DISplay {ON|OFF|<NR1>}
            - ZOOm:ZOOM1:MATH<x>:DISplay?
            ```

        Info:
            - ``<NR1>`` A zero disables the specified zoom; any other value enables the specified
              zoom.
            - ``OFF`` disables the specified zoom.
            - ``ON`` displays the specified zoom.
        """
        return self._display

    @property
    def horizontal(self) -> ZoomZoom1MathItemHorizontal:
        """Return the ``ZOOm:ZOOM1:MATH<x>:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:HORizontal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:ZOOM1:MATH<x>:HORizontal:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:MATH<x>:HORizontal:SCAle`` command.
        """
        return self._horizontal

    @property
    def vertical(self) -> ZoomZoom1MathItemVertical:
        """Return the ``ZOOm:ZOOM1:MATH<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>:VERTical?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:ZOOM1:MATH<x>:VERTical:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:MATH<x>:VERTical:SCAle`` command.
        """
        return self._vertical


class ZoomZoom1DchanDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:DCHAN:DISplay`` command.

    Description:
        - This command sets or queries the display of the digital waveforms for the specified zoom,
          where x is an integer from 1 to 4 representing the desired zoom window. The digital
          waveforms affected vary from CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4, and D0
          through D15. When zoom is set on any one of the waveforms from D0 through D15, it would
          apply to all of the waveforms (D0 through D15).

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:DCHAN:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:DCHAN:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:DCHAN:DISplay value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:DCHAN:DISplay {ON|OFF|<NR1>}
        - ZOOm:ZOOM1:DCHAN:DISplay?
        ```

    Info:
        - ``<NR1>`` = 0 disables the specified zoom; any other value enables the specified zoom.
        - ``OFF`` disables the specified zoom.
        - ``ON`` displays the specified zoom.
    """


class ZoomZoom1Dchan(SCPICmdRead):
    """The ``ZOOm:ZOOM1:DCHAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:DCHAN?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:DCHAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.display``: The ``ZOOm:ZOOM1:DCHAN:DISplay`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._display = ZoomZoom1DchanDisplay(device, f"{self._cmd_syntax}:DISplay")

    @property
    def display(self) -> ZoomZoom1DchanDisplay:
        """Return the ``ZOOm:ZOOM1:DCHAN:DISplay`` command.

        Description:
            - This command sets or queries the display of the digital waveforms for the specified
              zoom, where x is an integer from 1 to 4 representing the desired zoom window. The
              digital waveforms affected vary from CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4,
              and D0 through D15. When zoom is set on any one of the waveforms from D0 through D15,
              it would apply to all of the waveforms (D0 through D15).

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:DCHAN:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:DCHAN:DISplay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:DCHAN:DISplay value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:DCHAN:DISplay {ON|OFF|<NR1>}
            - ZOOm:ZOOM1:DCHAN:DISplay?
            ```

        Info:
            - ``<NR1>`` = 0 disables the specified zoom; any other value enables the specified zoom.
            - ``OFF`` disables the specified zoom.
            - ``ON`` displays the specified zoom.
        """
        return self._display


class ZoomZoom1DigitalBitVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:D<x>:VERTical:SCAle`` command.

    Description:
        - This command sets or queries the zoom vertical scale of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1,
          Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical:SCAle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical:SCAle value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:D<x>:VERTical:SCAle <NR3>
        - ZOOm:ZOOM1:D<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of vertical expansion or compression, which operates on a 1-2-5
          sequence (for example, 1, 2, 5, 10, 20, 50, 100...). Based on the value that you entered,
          this command uses the nearest scale factor. Setting the vertical scale to 1 indicates
          unity (no zoom).
    """


class ZoomZoom1DigitalBitVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:D<x>:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The setting of the ``ZOOm:1:SCROLLLOCk`` command determines the waveforms that are
          affected. The <wfm> can be a channel, math, or reference waveform. The waveform affected
          is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4,
          Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:D<x>:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:D<x>:VERTical:POSition <NR3>
        - ZOOm:ZOOM1:D<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position, expressed in divisions.
    """


class ZoomZoom1DigitalBitVertical(SCPICmdRead):
    """The ``ZOOm:ZOOM1:D<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:ZOOM1:D<x>:VERTical:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:D<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomZoom1DigitalBitVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomZoom1DigitalBitVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomZoom1DigitalBitVerticalPosition:
        """Return the ``ZOOm:ZOOM1:D<x>:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The setting of the ``ZOOm:1:SCROLLLOCk`` command determines the waveforms that
              are affected. The <wfm> can be a channel, math, or reference waveform. The waveform
              affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2,
              Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:D<x>:VERTical:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:D<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:D<x>:VERTical:POSition <NR3>
            - ZOOm:ZOOM1:D<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position, expressed in divisions.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1DigitalBitVerticalScale:
        """Return the ``ZOOm:ZOOM1:D<x>:VERTical:SCAle`` command.

        Description:
            - This command sets or queries the zoom vertical scale of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
              CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical:SCAle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:D<x>:VERTical:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:D<x>:VERTical:SCAle <NR3>
            - ZOOm:ZOOM1:D<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of vertical expansion or compression, which operates on a
              1-2-5 sequence (for example, 1, 2, 5, 10, 20, 50, 100...). Based on the value that you
              entered, this command uses the nearest scale factor. Setting the vertical scale to 1
              indicates unity (no zoom).
        """
        return self._scale


class ZoomZoom1DigitalBitHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle`` command.

    Description:
        - This command sets or queries the zoom horizontal scale factor of the specified waveform
          for the specified zoom, where x is an integer from 1 to 4 representing the desired zoom
          window. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
          CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:D<x>:HORizontal:SCAle <NR3>
        - ZOOm:ZOOM1:D<x>:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
    """


class ZoomZoom1DigitalBitHorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:D<x>:HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal position of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The setting of the ``ZOOM:ZOOMX:SCROLLLOCK`` command determines the waveforms that are
          affected. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
          CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:D<x>:HORizontal:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:D<x>:HORizontal:POSition <NR3>
        - ZOOm:ZOOM1:D<x>:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to the
          left of screen center, when the zoom factor is 1× or greater.
    """


class ZoomZoom1DigitalBitHorizontal(SCPICmdRead):
    """The ``ZOOm:ZOOM1:D<x>:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:ZOOM1:D<x>:HORizontal:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomZoom1DigitalBitHorizontalPosition(
            device, f"{self._cmd_syntax}:POSition"
        )
        self._scale = ZoomZoom1DigitalBitHorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomZoom1DigitalBitHorizontalPosition:
        """Return the ``ZOOm:ZOOM1:D<x>:HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal position of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The setting of the ``ZOOM:ZOOMX:SCROLLLOCK`` command determines the waveforms
              that are affected. The waveform affected is determine by <wfm> which can vary from
              CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:D<x>:HORizontal:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:D<x>:HORizontal:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:D<x>:HORizontal:POSition <NR3>
            - ZOOm:ZOOM1:D<x>:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to
              the left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1DigitalBitHorizontalScale:
        """Return the ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle`` command.

        Description:
            - This command sets or queries the zoom horizontal scale factor of the specified
              waveform for the specified zoom, where x is an integer from 1 to 4 representing the
              desired zoom window. The waveform affected is determine by <wfm> which can vary from
              CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:D<x>:HORizontal:SCAle <NR3>
            - ZOOm:ZOOM1:D<x>:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
        """
        return self._scale


class ZoomZoom1DigitalBitDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:D<x>:DISplay`` command.

    Description:
        - This command sets or queries the display of the specified waveform for the specified zoom,
          where x is an integer from 1 to 4 representing the desired zoom window. The waveform
          affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2,
          Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:D<x>:DISplay value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:D<x>:DISplay {ON|OFF|<NR1>}
        - ZOOm:ZOOM1:D<x>:DISplay?
        ```

    Info:
        - ``<NR1>`` A zero disables the specified zoom; any other value enables the specified zoom.
        - ``OFF`` disables the specified zoom.
        - ``ON`` displays the specified zoom.
    """


class ZoomZoom1DigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``ZOOm:ZOOM1:D<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.display``: The ``ZOOm:ZOOM1:D<x>:DISplay`` command.
        - ``.horizontal``: The ``ZOOm:ZOOM1:D<x>:HORizontal`` command tree.
        - ``.vertical``: The ``ZOOm:ZOOM1:D<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._display = ZoomZoom1DigitalBitDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._horizontal = ZoomZoom1DigitalBitHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._vertical = ZoomZoom1DigitalBitVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def display(self) -> ZoomZoom1DigitalBitDisplay:
        """Return the ``ZOOm:ZOOM1:D<x>:DISplay`` command.

        Description:
            - This command sets or queries the display of the specified waveform for the specified
              zoom, where x is an integer from 1 to 4 representing the desired zoom window. The
              waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1,
              Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:DISplay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:D<x>:DISplay value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:D<x>:DISplay {ON|OFF|<NR1>}
            - ZOOm:ZOOM1:D<x>:DISplay?
            ```

        Info:
            - ``<NR1>`` A zero disables the specified zoom; any other value enables the specified
              zoom.
            - ``OFF`` disables the specified zoom.
            - ``ON`` displays the specified zoom.
        """
        return self._display

    @property
    def horizontal(self) -> ZoomZoom1DigitalBitHorizontal:
        """Return the ``ZOOm:ZOOM1:D<x>:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:HORizontal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:ZOOM1:D<x>:HORizontal:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:D<x>:HORizontal:SCAle`` command.
        """
        return self._horizontal

    @property
    def vertical(self) -> ZoomZoom1DigitalBitVertical:
        """Return the ``ZOOm:ZOOM1:D<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>:VERTical?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:ZOOM1:D<x>:VERTical:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:D<x>:VERTical:SCAle`` command.
        """
        return self._vertical


class ZoomZoom1ChannelVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle`` command.

    Description:
        - This command sets or queries the zoom vertical scale of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1,
          Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:CH<x>:VERTical:SCAle <NR3>
        - ZOOm:ZOOM1:CH<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of vertical expansion or compression, which operates on a 1-2-5
          sequence (for example, 1, 2, 5, 10, 20, 50, 100...). Based on the value that you entered,
          this command uses the nearest scale factor. Setting the vertical scale to 1 indicates
          unity (no zoom).
    """


class ZoomZoom1ChannelVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:CH<x>:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The setting of the ``ZOOm:1:SCROLLLOCk`` command determines the waveforms that are
          affected. The <wfm> can be a channel, math, or reference waveform. The waveform affected
          is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4,
          Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:CH<x>:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:CH<x>:VERTical:POSition <NR3>
        - ZOOm:ZOOM1:CH<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position, expressed in divisions.
    """


class ZoomZoom1ChannelVertical(SCPICmdRead):
    """The ``ZOOm:ZOOM1:CH<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:ZOOM1:CH<x>:VERTical:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomZoom1ChannelVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomZoom1ChannelVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomZoom1ChannelVerticalPosition:
        """Return the ``ZOOm:ZOOM1:CH<x>:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The setting of the ``ZOOm:1:SCROLLLOCk`` command determines the waveforms that
              are affected. The <wfm> can be a channel, math, or reference waveform. The waveform
              affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2,
              Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:CH<x>:VERTical:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:CH<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:CH<x>:VERTical:POSition <NR3>
            - ZOOm:ZOOM1:CH<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position, expressed in divisions.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1ChannelVerticalScale:
        """Return the ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle`` command.

        Description:
            - This command sets or queries the zoom vertical scale of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
              CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle?``
              query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:CH<x>:VERTical:SCAle <NR3>
            - ZOOm:ZOOM1:CH<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of vertical expansion or compression, which operates on a
              1-2-5 sequence (for example, 1, 2, 5, 10, 20, 50, 100...). Based on the value that you
              entered, this command uses the nearest scale factor. Setting the vertical scale to 1
              indicates unity (no zoom).
        """
        return self._scale


class ZoomZoom1ChannelHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle`` command.

    Description:
        - This command sets or queries the zoom horizontal scale factor of the specified waveform
          for the specified zoom, where x is an integer from 1 to 4 representing the desired zoom
          window. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
          CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:CH<x>:HORizontal:SCAle <NR3>
        - ZOOm:ZOOM1:CH<x>:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
    """


class ZoomZoom1ChannelHorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal position of the specified waveform for the
          specified zoom, where x is an integer from 1 to 4 representing the desired zoom window.
          The setting of the ``ZOOM:ZOOMX:SCROLLLOCK`` command determines the waveforms that are
          affected. The waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3,
          CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:CH<x>:HORizontal:POSition <NR3>
        - ZOOm:ZOOM1:CH<x>:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to the
          left of screen center, when the zoom factor is 1× or greater.
    """


class ZoomZoom1ChannelHorizontal(SCPICmdRead):
    """The ``ZOOm:ZOOM1:CH<x>:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:HORizontal?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition`` command.
        - ``.scale``: The ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomZoom1ChannelHorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomZoom1ChannelHorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomZoom1ChannelHorizontalPosition:
        """Return the ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal position of the specified waveform for the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The setting of the ``ZOOM:ZOOMX:SCROLLLOCK`` command determines the waveforms
              that are affected. The waveform affected is determine by <wfm> which can vary from
              CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:CH<x>:HORizontal:POSition <NR3>
            - ZOOm:ZOOM1:CH<x>:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to
              the left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomZoom1ChannelHorizontalScale:
        """Return the ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle`` command.

        Description:
            - This command sets or queries the zoom horizontal scale factor of the specified
              waveform for the specified zoom, where x is an integer from 1 to 4 representing the
              desired zoom window. The waveform affected is determine by <wfm> which can vary from
              CH1, CH2, CH3, CH4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:CH<x>:HORizontal:SCAle <NR3>
            - ZOOm:ZOOM1:CH<x>:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
        """
        return self._scale


class ZoomZoom1ChannelDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1:CH<x>:DISplay`` command.

    Description:
        - This command sets or queries the display of the specified waveform for the specified zoom,
          where x is an integer from 1 to 4 representing the desired zoom window. The waveform
          affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1, Math2,
          Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:DISplay value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1:CH<x>:DISplay {ON|OFF|<NR1>}
        - ZOOm:ZOOM1:CH<x>:DISplay?
        ```

    Info:
        - ``<NR1>`` A zero disables the specified zoom; any other value enables the specified zoom.
        - ``OFF`` disables the specified zoom.
        - ``ON`` displays the specified zoom.
    """


class ZoomZoom1Channel(ValidatedChannel, SCPICmdRead):
    """The ``ZOOm:ZOOM1:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.display``: The ``ZOOm:ZOOM1:CH<x>:DISplay`` command.
        - ``.horizontal``: The ``ZOOm:ZOOM1:CH<x>:HORizontal`` command tree.
        - ``.vertical``: The ``ZOOm:ZOOM1:CH<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._display = ZoomZoom1ChannelDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._horizontal = ZoomZoom1ChannelHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._vertical = ZoomZoom1ChannelVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def display(self) -> ZoomZoom1ChannelDisplay:
        """Return the ``ZOOm:ZOOM1:CH<x>:DISplay`` command.

        Description:
            - This command sets or queries the display of the specified waveform for the specified
              zoom, where x is an integer from 1 to 4 representing the desired zoom window. The
              waveform affected is determine by <wfm> which can vary from CH1, CH2, CH3, CH4, Math1,
              Math2, Math3, Math4, Ref1, Ref2, Ref3, or Ref4.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:DISplay?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:DISplay value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:CH<x>:DISplay {ON|OFF|<NR1>}
            - ZOOm:ZOOM1:CH<x>:DISplay?
            ```

        Info:
            - ``<NR1>`` A zero disables the specified zoom; any other value enables the specified
              zoom.
            - ``OFF`` disables the specified zoom.
            - ``ON`` displays the specified zoom.
        """
        return self._display

    @property
    def horizontal(self) -> ZoomZoom1ChannelHorizontal:
        """Return the ``ZOOm:ZOOM1:CH<x>:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:HORizontal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:ZOOM1:CH<x>:HORizontal:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:CH<x>:HORizontal:SCAle`` command.
        """
        return self._horizontal

    @property
    def vertical(self) -> ZoomZoom1ChannelVertical:
        """Return the ``ZOOm:ZOOM1:CH<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>:VERTical?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:ZOOM1:CH<x>:VERTical:POSition`` command.
            - ``.scale``: The ``ZOOm:ZOOM1:CH<x>:VERTical:SCAle`` command.
        """
        return self._vertical


class ZoomZoom1(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:ZOOM1`` command.

    Description:
        - This command resets the zoom transforms to default values for all traces of the specified
          zoom, where x is an integer from 1 to 4 representing the desired zoom window. The
          ``ZOOM:REFX:VERTICAL:SCALE?`` query returns the current vertical and horizontal
          positioning and scaling of the display.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:ZOOM1?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1 value`` command.

    SCPI Syntax:
        ```
        - ZOOm:ZOOM1 {RESET|RESETLive}
        - ZOOm:ZOOM1?
        ```

    Info:
        - ``RESET`` resets the zoom transforms to default values for all traces of the specified
          zoom.
        - ``RESETLive`` resets the zoom transforms to default values for live traces of the
          specified zoom.

    Properties:
        - ``.dchan``: The ``ZOOm:ZOOM1:DCHAN`` command tree.
        - ``.scrolllock``: The ``ZOOm:ZOOM1:SCROLLLock`` command.
        - ``.state``: The ``ZOOm:ZOOM1:STATE`` command.
        - ``.ch``: The ``ZOOm:ZOOM1:CH<x>`` command tree.
        - ``.math``: The ``ZOOm:ZOOM1:MATH<x>`` command tree.
        - ``.ref``: The ``ZOOm:ZOOM1:REF<x>`` command tree.
        - ``.d``: The ``ZOOm:ZOOM1:D<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dchan = ZoomZoom1Dchan(device, f"{self._cmd_syntax}:DCHAN")
        self._scrolllock = ZoomZoom1Scrolllock(device, f"{self._cmd_syntax}:SCROLLLock")
        self._state = ZoomZoom1State(device, f"{self._cmd_syntax}:STATE")
        self._ch: Dict[int, ZoomZoom1Channel] = DefaultDictPassKeyToFactory(
            lambda x: ZoomZoom1Channel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math: Dict[int, ZoomZoom1MathItem] = DefaultDictPassKeyToFactory(
            lambda x: ZoomZoom1MathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )
        self._ref: Dict[int, ZoomZoom1RefItem] = DefaultDictPassKeyToFactory(
            lambda x: ZoomZoom1RefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._d: Dict[int, ZoomZoom1DigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: ZoomZoom1DigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def dchan(self) -> ZoomZoom1Dchan:
        """Return the ``ZOOm:ZOOM1:DCHAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:DCHAN?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:DCHAN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.display``: The ``ZOOm:ZOOM1:DCHAN:DISplay`` command.
        """
        return self._dchan

    @property
    def scrolllock(self) -> ZoomZoom1Scrolllock:
        """Return the ``ZOOm:ZOOM1:SCROLLLock`` command.

        Description:
            - This command sets or queries Scroll Lock for the specified zoom, where x is an integer
              from 1 to 4 representing the desired zoom window.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:SCROLLLock?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:SCROLLLock?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:SCROLLLock value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:SCROLLLock {ON|OFF|<NR1>}
            - ZOOm:ZOOM1:SCROLLLock?
            ```

        Info:
            - ``ON`` locks waveforms for the specified zoom window <x>.
            - ``OFF`` unlocks waveforms for the specified zoom window <x>.
            - ``<NR1>`` = 0 unlocks waveforms for the specified zoom window <x>; any other value
              locks waveforms for the specified zoom window <x>.
        """
        return self._scrolllock

    @property
    def state(self) -> ZoomZoom1State:
        """Return the ``ZOOm:ZOOM1:STATE`` command.

        Description:
            - This command turns the specified zoom on or off. <x> can only be 1.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1:STATE value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1:STATE {ON|OFF|<NR1>}
            - ZOOm:ZOOM1:STATE?
            ```

        Info:
            - ``ON`` turns Zoom 1 on.
            - ``OFF`` turns Zoom 1 off.
            - ``<NR1>`` is an integer. 0 disables the specified zoom; any other value enables the
              specified zoom.
        """
        return self._state

    @property
    def ch(self) -> Dict[int, ZoomZoom1Channel]:
        """Return the ``ZOOm:ZOOM1:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.display``: The ``ZOOm:ZOOM1:CH<x>:DISplay`` command.
            - ``.horizontal``: The ``ZOOm:ZOOM1:CH<x>:HORizontal`` command tree.
            - ``.vertical``: The ``ZOOm:ZOOM1:CH<x>:VERTical`` command tree.
        """
        return self._ch

    @property
    def math(self) -> Dict[int, ZoomZoom1MathItem]:
        """Return the ``ZOOm:ZOOM1:MATH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:MATH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.display``: The ``ZOOm:ZOOM1:MATH<x>:DISplay`` command.
            - ``.horizontal``: The ``ZOOm:ZOOM1:MATH<x>:HORizontal`` command tree.
            - ``.vertical``: The ``ZOOm:ZOOM1:MATH<x>:VERTical`` command tree.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, ZoomZoom1RefItem]:
        """Return the ``ZOOm:ZOOM1:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:REF<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.display``: The ``ZOOm:ZOOM1:REF<x>:DISplay`` command.
            - ``.horizontal``: The ``ZOOm:ZOOM1:REF<x>:HORizontal`` command tree.
            - ``.vertical``: The ``ZOOm:ZOOM1:REF<x>:VERTical`` command tree.
        """
        return self._ref

    @property
    def d(self) -> Dict[int, ZoomZoom1DigitalBit]:
        """Return the ``ZOOm:ZOOM1:D<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1:D<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.display``: The ``ZOOm:ZOOM1:D<x>:DISplay`` command.
            - ``.horizontal``: The ``ZOOm:ZOOM1:D<x>:HORizontal`` command tree.
            - ``.vertical``: The ``ZOOm:ZOOM1:D<x>:VERTical`` command tree.
        """
        return self._d


class ZoomVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:VERTical:SCAle`` command.

    Description:
        - This command sets or queries the zoom vertical scale factor around which the zoom waveform
          is displayed.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:VERTical:SCAle?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:VERTical:SCAle value`` command.

    SCPI Syntax:
        ```
        - ZOOm:VERTical:SCAle <NR3>
        - ZOOm:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the vertical direction in 1-2-5 increments.
    """


class ZoomVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position around which the zoom waveform is
          displayed. It is freely movable within the confines of the acquired waveform (0% to 100%)
          and measured from left to right of the acquired waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:VERTical:POSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:VERTical:POSition <NR3>
        - ZOOm:VERTical:POSition?
        ```

    Info:
        - ``NR3`` is a value from 0 to 100.00 and is the percent of the waveform that is to the left
          of screen center, when the zoom factor is 1× or greater.
    """


class ZoomVertical(SCPICmdRead):
    """The ``ZOOm:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:VERTical?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:VERTical:POSition`` command.
        - ``.scale``: The ``ZOOm:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomVerticalPosition:
        """Return the ``ZOOm:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position around which the zoom waveform is
              displayed. It is freely movable within the confines of the acquired waveform (0% to
              100%) and measured from left to right of the acquired waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:VERTical:POSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:VERTical:POSition value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:VERTical:POSition <NR3>
            - ZOOm:VERTical:POSition?
            ```

        Info:
            - ``NR3`` is a value from 0 to 100.00 and is the percent of the waveform that is to the
              left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomVerticalScale:
        """Return the ``ZOOm:VERTical:SCAle`` command.

        Description:
            - This command sets or queries the zoom vertical scale factor around which the zoom
              waveform is displayed.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:VERTical:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:VERTical:SCAle value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:VERTical:SCAle <NR3>
            - ZOOm:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the vertical direction in 1-2-5 increments.
        """
        return self._scale


class ZoomState(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:STATE`` command.

    Description:
        - This command sets or queries the specified zoom on or off.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:STATE value`` command.

    SCPI Syntax:
        ```
        - ZOOm:STATE {ON|OFF|<NR1>}
        - ZOOm:STATE?
        ```

    Info:
        - ``ON`` turns zoom on or off.
        - ``OFF`` turns zoom on or off.
        - ``<NR1>`` = 0 disables the zoom; any other value enables the zoom.
    """


class ZoomScrollSpeed(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:SCROLL:SPEED`` command.

    Description:
        - This command sets or queries the speed of automatic scrolling.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:SCROLL:SPEED?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:SCROLL:SPEED?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:SCROLL:SPEED value`` command.

    SCPI Syntax:
        ```
        - ZOOm:SCROLL:SPEED <NR1>
        - ZOOm:SCROLL:SPEED?
        ```

    Info:
        - ``<NR1>`` is a value from 1 to 10.
    """


class ZoomScrollLock(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:SCROLL:LOCk`` command.

    Description:
        - This command sets or queries the state of Scroll Lock, which 'locks' zoomed waveforms
          under common control.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:SCROLL:LOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:SCROLL:LOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:SCROLL:LOCk value`` command.

    SCPI Syntax:
        ```
        - ZOOm:SCROLL:LOCk {ON|OFF|<NR1>}
        - ZOOm:SCROLL:LOCk?
        ```

    Info:
        - ``ON`` enables Scroll Lock.
        - ``OFF`` disables Scroll Lock.
        - ``<NR1>`` = 0 disables Scroll Lock for all zoom windows; any other value enables Scroll
          Lock for all zoom windows.
    """


class ZoomScrollDirection(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:SCROLL:DIREction`` command.

    Description:
        - This command sets or queries the direction for automatic scrolling of zoomed waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:SCROLL:DIREction?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:SCROLL:DIREction?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:SCROLL:DIREction value`` command.

    SCPI Syntax:
        ```
        - ZOOm:SCROLL:DIREction {FWD|FFWD|REV|FREV|STOP}
        - ZOOm:SCROLL:DIREction?
        ```

    Info:
        - ``FWD`` starts AutoScroll. The Zoom Box moves from left to right.
        - ``FFWD`` starts AutoScroll. Increases the scrolling speed in the forward direction.
        - ``REV`` starts AutoScroll. The Zoom Box moves from right to left.
        - ``FREV`` starts AutoScroll. Increases the scrolling speed in the reverse direction.
        - ``STOP`` halts AutoScroll.
    """


class ZoomScroll(SCPICmdRead):
    """The ``ZOOm:SCROLL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:SCROLL?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:SCROLL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.direction``: The ``ZOOm:SCROLL:DIREction`` command.
        - ``.lock``: The ``ZOOm:SCROLL:LOCk`` command.
        - ``.speed``: The ``ZOOm:SCROLL:SPEED`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = ZoomScrollDirection(device, f"{self._cmd_syntax}:DIREction")
        self._lock = ZoomScrollLock(device, f"{self._cmd_syntax}:LOCk")
        self._speed = ZoomScrollSpeed(device, f"{self._cmd_syntax}:SPEED")

    @property
    def direction(self) -> ZoomScrollDirection:
        """Return the ``ZOOm:SCROLL:DIREction`` command.

        Description:
            - This command sets or queries the direction for automatic scrolling of zoomed
              waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:SCROLL:DIREction?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:SCROLL:DIREction?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:SCROLL:DIREction value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:SCROLL:DIREction {FWD|FFWD|REV|FREV|STOP}
            - ZOOm:SCROLL:DIREction?
            ```

        Info:
            - ``FWD`` starts AutoScroll. The Zoom Box moves from left to right.
            - ``FFWD`` starts AutoScroll. Increases the scrolling speed in the forward direction.
            - ``REV`` starts AutoScroll. The Zoom Box moves from right to left.
            - ``FREV`` starts AutoScroll. Increases the scrolling speed in the reverse direction.
            - ``STOP`` halts AutoScroll.
        """
        return self._direction

    @property
    def lock(self) -> ZoomScrollLock:
        """Return the ``ZOOm:SCROLL:LOCk`` command.

        Description:
            - This command sets or queries the state of Scroll Lock, which 'locks' zoomed waveforms
              under common control.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:SCROLL:LOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:SCROLL:LOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:SCROLL:LOCk value`` command.

        SCPI Syntax:
            ```
            - ZOOm:SCROLL:LOCk {ON|OFF|<NR1>}
            - ZOOm:SCROLL:LOCk?
            ```

        Info:
            - ``ON`` enables Scroll Lock.
            - ``OFF`` disables Scroll Lock.
            - ``<NR1>`` = 0 disables Scroll Lock for all zoom windows; any other value enables
              Scroll Lock for all zoom windows.
        """
        return self._lock

    @property
    def speed(self) -> ZoomScrollSpeed:
        """Return the ``ZOOm:SCROLL:SPEED`` command.

        Description:
            - This command sets or queries the speed of automatic scrolling.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:SCROLL:SPEED?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:SCROLL:SPEED?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:SCROLL:SPEED value`` command.

        SCPI Syntax:
            ```
            - ZOOm:SCROLL:SPEED <NR1>
            - ZOOm:SCROLL:SPEED?
            ```

        Info:
            - ``<NR1>`` is a value from 1 to 10.
        """
        return self._speed


class ZoomRefItemVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:REF<x>:VERTical:SCAle`` command.

    Description:
        - This command sets or queries the zoom vertical scale of the specified reference waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:REF<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:VERTical:SCAle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:REF<x>:VERTical:SCAle value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:REF<x>:VERTical:SCAle <NR3>
        - ZOOm:REF<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` sets the horizontal scale factor of the specified Reference 1 waveform to 10.
    """


class ZoomRefItemVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:REF<x>:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position of the specified reference waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:REF<x>:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:VERTical:POSition?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:REF<x>:VERTical:POSition value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:REF<x>:VERTical:POSition <NR3>
        - ZOOm:REF<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position, expressed in divisions.
    """


class ZoomRefItemVertical(SCPICmdRead):
    """The ``ZOOm:REF<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:REF<x>:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:VERTical?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:REF<x>:VERTical:POSition`` command.
        - ``.scale``: The ``ZOOm:REF<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomRefItemVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomRefItemVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomRefItemVerticalPosition:
        """Return the ``ZOOm:REF<x>:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position of the specified reference
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:REF<x>:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:VERTical:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:REF<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:REF<x>:VERTical:POSition <NR3>
            - ZOOm:REF<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position, expressed in divisions.
        """
        return self._position

    @property
    def scale(self) -> ZoomRefItemVerticalScale:
        """Return the ``ZOOm:REF<x>:VERTical:SCAle`` command.

        Description:
            - This command sets or queries the zoom vertical scale of the specified reference
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:REF<x>:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:VERTical:SCAle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:REF<x>:VERTical:SCAle value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:REF<x>:VERTical:SCAle <NR3>
            - ZOOm:REF<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` sets the horizontal scale factor of the specified Reference 1 waveform to
              10.
        """
        return self._scale


class ZoomRefItemHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:REF<x>:HORizontal:SCAle`` command.

    Description:
        - This command sets or queries the zoom horizontal scale factor of the specified reference
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:REF<x>:HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:HORizontal:SCAle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:REF<x>:HORizontal:SCAle value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:REF<x>:HORizontal:SCAle <NR3>
        - ZOOm:REF<x>:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
    """


class ZoomRefItemHorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:REF<x>:HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal position of the specified reference waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:REF<x>:HORizontal:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:HORizontal:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:REF<x>:HORizontal:POSition value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:REF<x>:HORizontal:POSition <NR3>
        - ZOOm:REF<x>:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to the
          left of screen center, when the zoom factor is 1× or greater.
    """


class ZoomRefItemHorizontal(SCPICmdRead):
    """The ``ZOOm:REF<x>:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:REF<x>:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:HORizontal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:REF<x>:HORizontal:POSition`` command.
        - ``.scale``: The ``ZOOm:REF<x>:HORizontal:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomRefItemHorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomRefItemHorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomRefItemHorizontalPosition:
        """Return the ``ZOOm:REF<x>:HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal position of the specified reference
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:REF<x>:HORizontal:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:HORizontal:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:REF<x>:HORizontal:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:REF<x>:HORizontal:POSition <NR3>
            - ZOOm:REF<x>:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to
              the left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomRefItemHorizontalScale:
        """Return the ``ZOOm:REF<x>:HORizontal:SCAle`` command.

        Description:
            - This command sets or queries the zoom horizontal scale factor of the specified
              reference waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:REF<x>:HORizontal:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:HORizontal:SCAle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:REF<x>:HORizontal:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:REF<x>:HORizontal:SCAle <NR3>
            - ZOOm:REF<x>:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
        """
        return self._scale


class ZoomRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``ZOOm:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.horizontal``: The ``ZOOm:REF<x>:HORizontal`` command tree.
        - ``.vertical``: The ``ZOOm:REF<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = ZoomRefItemHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._vertical = ZoomRefItemVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def horizontal(self) -> ZoomRefItemHorizontal:
        """Return the ``ZOOm:REF<x>:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:REF<x>:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:HORizontal?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:REF<x>:HORizontal:POSition`` command.
            - ``.scale``: The ``ZOOm:REF<x>:HORizontal:SCAle`` command.
        """
        return self._horizontal

    @property
    def vertical(self) -> ZoomRefItemVertical:
        """Return the ``ZOOm:REF<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:REF<x>:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>:VERTical?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:REF<x>:VERTical:POSition`` command.
            - ``.scale``: The ``ZOOm:REF<x>:VERTical:SCAle`` command.
        """
        return self._vertical


class ZoomMode(SCPICmdWrite):
    """The ``ZOOm:MODe`` command.

    Description:
        - This command turns Zoom mode on or off. The Zoom query returns the current state of Zoom
          mode. This command is equivalent to pressing the ZOOM button located on the front panel.

    Usage:
        - Using the ``.write(value)`` method will send the ``ZOOm:MODe value`` command.

    SCPI Syntax:
        ```
        - ZOOm:MODe {ON|OFF|<NR1>}
        ```

    Info:
        - ``ON`` turns on Zoom mode.
        - ``OFF`` turns off Zoom mode.
        - ``<NR1>`` = 0 turns off Zoom mode; any other value turns on Zoom mode.
    """


class ZoomMathItemVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:MATH<x>:VERTical:SCAle`` command.

    Description:
        - This command sets or queries the zoom vertical scale of the specified math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:VERTical:SCAle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:MATH<x>:VERTical:SCAle value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:MATH<x>:VERTical:SCAle <NR3>
        - ZOOm:MATH<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` sets the horizontal scale factor of the specified Math 1 waveform to 10.
    """


class ZoomMathItemVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:MATH<x>:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position of the specified math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:VERTical:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:MATH<x>:VERTical:POSition value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:MATH<x>:VERTical:POSition <NR3>
        - ZOOm:MATH<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position, expressed in divisions.
    """


class ZoomMathItemVertical(SCPICmdRead):
    """The ``ZOOm:MATH<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:VERTical?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:MATH<x>:VERTical:POSition`` command.
        - ``.scale``: The ``ZOOm:MATH<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomMathItemVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomMathItemVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomMathItemVerticalPosition:
        """Return the ``ZOOm:MATH<x>:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position of the specified math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:VERTical:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:MATH<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:MATH<x>:VERTical:POSition <NR3>
            - ZOOm:MATH<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position, expressed in divisions.
        """
        return self._position

    @property
    def scale(self) -> ZoomMathItemVerticalScale:
        """Return the ``ZOOm:MATH<x>:VERTical:SCAle`` command.

        Description:
            - This command sets or queries the zoom vertical scale of the specified math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:VERTical:SCAle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:MATH<x>:VERTical:SCAle value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:MATH<x>:VERTical:SCAle <NR3>
            - ZOOm:MATH<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` sets the horizontal scale factor of the specified Math 1 waveform to 10.
        """
        return self._scale


class ZoomMathItemHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:MATH<x>:HORizontal:SCAle`` command.

    Description:
        - This command sets or queries the zoom horizontal scale factor of the specified math
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:HORizontal:SCAle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:MATH<x>:HORizontal:SCAle value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:MATH<x>:HORizontal:SCAle <NR3>
        - ZOOm:MATH<x>:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
    """


class ZoomMathItemHorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:MATH<x>:HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal position of the specified math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:HORizontal:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:HORizontal:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ZOOm:MATH<x>:HORizontal:POSition value`` command.

    SCPI Syntax:
        ```
        - ZOOm:MATH<x>:HORizontal:POSition <NR3>
        - ZOOm:MATH<x>:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to the
          left of screen center, when the zoom factor is 1× or greater.
    """


class ZoomMathItemHorizontal(SCPICmdRead):
    """The ``ZOOm:MATH<x>:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:HORizontal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:MATH<x>:HORizontal:POSition`` command.
        - ``.scale``: The ``ZOOm:MATH<x>:HORizontal:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomMathItemHorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomMathItemHorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomMathItemHorizontalPosition:
        """Return the ``ZOOm:MATH<x>:HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal position of the specified math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:HORizontal:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ZOOm:MATH<x>:HORizontal:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:MATH<x>:HORizontal:POSition value`` command.

        SCPI Syntax:
            ```
            - ZOOm:MATH<x>:HORizontal:POSition <NR3>
            - ZOOm:MATH<x>:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to
              the left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomMathItemHorizontalScale:
        """Return the ``ZOOm:MATH<x>:HORizontal:SCAle`` command.

        Description:
            - This command sets or queries the zoom horizontal scale factor of the specified math
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:HORizontal:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:HORizontal:SCAle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ZOOm:MATH<x>:HORizontal:SCAle value`` command.

        SCPI Syntax:
            ```
            - ZOOm:MATH<x>:HORizontal:SCAle <NR3>
            - ZOOm:MATH<x>:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
        """
        return self._scale


class ZoomMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``ZOOm:MATH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.horizontal``: The ``ZOOm:MATH<x>:HORizontal`` command tree.
        - ``.vertical``: The ``ZOOm:MATH<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = ZoomMathItemHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._vertical = ZoomMathItemVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def horizontal(self) -> ZoomMathItemHorizontal:
        """Return the ``ZOOm:MATH<x>:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:HORizontal?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:MATH<x>:HORizontal:POSition`` command.
            - ``.scale``: The ``ZOOm:MATH<x>:HORizontal:SCAle`` command.
        """
        return self._horizontal

    @property
    def vertical(self) -> ZoomMathItemVertical:
        """Return the ``ZOOm:MATH<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:MATH<x>:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>:VERTical?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:MATH<x>:VERTical:POSition`` command.
            - ``.scale``: The ``ZOOm:MATH<x>:VERTical:SCAle`` command.
        """
        return self._vertical


class ZoomHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:HORizontal:SCAle`` command.

    Description:
        - This command sets or queries the zoom horizontal scale factor around which the zoom
          waveform is displayed.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:HORizontal:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:HORizontal:SCAle value`` command.

    SCPI Syntax:
        ```
        - ZOOm:HORizontal:SCAle <NR3>
        - ZOOm:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
    """


class ZoomHorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal position around which the zoom waveform is
          displayed. It is freely movable within the confines of the acquired waveform (0% to 100%)
          and measured from left to right of the acquired waveform.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:HORizontal:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:HORizontal:POSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:HORizontal:POSition value``
          command.

    SCPI Syntax:
        ```
        - ZOOm:HORizontal:POSition <NR3>
        - ZOOm:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to the
          left of screen center, when the zoom factor is 1× or greater.
    """


class ZoomHorizontal(SCPICmdRead):
    """The ``ZOOm:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:HORizontal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``ZOOm:HORizontal:POSition`` command.
        - ``.scale``: The ``ZOOm:HORizontal:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = ZoomHorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = ZoomHorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> ZoomHorizontalPosition:
        """Return the ``ZOOm:HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal position around which the zoom waveform is
              displayed. It is freely movable within the confines of the acquired waveform (0% to
              100%) and measured from left to right of the acquired waveform.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:HORizontal:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:HORizontal:POSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:HORizontal:POSition value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:HORizontal:POSition <NR3>
            - ZOOm:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to
              the left of screen center, when the zoom factor is 1× or greater.
        """
        return self._position

    @property
    def scale(self) -> ZoomHorizontalScale:
        """Return the ``ZOOm:HORizontal:SCAle`` command.

        Description:
            - This command sets or queries the zoom horizontal scale factor around which the zoom
              waveform is displayed.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:HORizontal:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:HORizontal:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:HORizontal:SCAle value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:HORizontal:SCAle <NR3>
            - ZOOm:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-5 increments.
        """
        return self._scale


class ZoomGraticuleSplit(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:GRAticule:SPLit`` command.

    Description:
        - This command sets or queries the sizes of the acquisition and zoom windows when Zoom is
          selected.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:GRAticule:SPLit?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:GRAticule:SPLit?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:GRAticule:SPLit value`` command.

    SCPI Syntax:
        ```
        - ZOOm:GRAticule:SPLit {FIFtyfifty|EIGHtytwenty|FuLl}
        - ZOOm:GRAticule:SPLit?
        ```

    Info:
        - ``FIFtyfifty`` argument sets half of the available display to the zoomed graticule and
          half of the available display to the acquisition graticule; this argument is the default
          value.
        - ``EIGHtytwenty`` argument sets 80% of the available display to the zoomed graticule and
          20% to the acquisition graticule.
        - ``FULl`` argument sets the entire display to the zoomed graticule.
    """


class ZoomGraticuleSize(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm:GRAticule:SIZE`` command.

    Description:
        - This command sets or queries the size in percent, of the Zoom (lower) graticule.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:GRAticule:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:GRAticule:SIZE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm:GRAticule:SIZE value`` command.

    SCPI Syntax:
        ```
        - ZOOm:GRAticule:SIZE {50|80|100}
        - ZOOm:GRAticule:SIZE?
        ```

    Info:
        - ``50`` sets the size of the Zoom graticule to 50%.
        - ``80`` set the size of the Zoom graticule to 80%.
        - ``100`` sets the size of the Zoom graticule to 100%.
    """


class ZoomGraticule(SCPICmdRead):
    """The ``ZOOm:GRAticule`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm:GRAticule?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm:GRAticule?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``ZOOm:GRAticule:SIZE`` command.
        - ``.split``: The ``ZOOm:GRAticule:SPLit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = ZoomGraticuleSize(device, f"{self._cmd_syntax}:SIZE")
        self._split = ZoomGraticuleSplit(device, f"{self._cmd_syntax}:SPLit")

    @property
    def size(self) -> ZoomGraticuleSize:
        """Return the ``ZOOm:GRAticule:SIZE`` command.

        Description:
            - This command sets or queries the size in percent, of the Zoom (lower) graticule.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:GRAticule:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:GRAticule:SIZE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:GRAticule:SIZE value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:GRAticule:SIZE {50|80|100}
            - ZOOm:GRAticule:SIZE?
            ```

        Info:
            - ``50`` sets the size of the Zoom graticule to 50%.
            - ``80`` set the size of the Zoom graticule to 80%.
            - ``100`` sets the size of the Zoom graticule to 100%.
        """
        return self._size

    @property
    def split(self) -> ZoomGraticuleSplit:
        """Return the ``ZOOm:GRAticule:SPLit`` command.

        Description:
            - This command sets or queries the sizes of the acquisition and zoom windows when Zoom
              is selected.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:GRAticule:SPLit?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:GRAticule:SPLit?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:GRAticule:SPLit value``
              command.

        SCPI Syntax:
            ```
            - ZOOm:GRAticule:SPLit {FIFtyfifty|EIGHtytwenty|FuLl}
            - ZOOm:GRAticule:SPLit?
            ```

        Info:
            - ``FIFtyfifty`` argument sets half of the available display to the zoomed graticule and
              half of the available display to the acquisition graticule; this argument is the
              default value.
            - ``EIGHtytwenty`` argument sets 80% of the available display to the zoomed graticule
              and 20% to the acquisition graticule.
            - ``FULl`` argument sets the entire display to the zoomed graticule.
        """
        return self._split


#  pylint: disable=too-many-instance-attributes
class Zoom(SCPICmdWrite, SCPICmdRead):
    """The ``ZOOm`` command.

    Description:
        - This command resets the zoom transforms to default values for all traces or live traces.
          The ``ZOOm`` query returns the current vertical and horizontal positioning and scaling of
          the display.

    Usage:
        - Using the ``.query()`` method will send the ``ZOOm?`` query.
        - Using the ``.verify(value)`` method will send the ``ZOOm?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ZOOm value`` command.

    SCPI Syntax:
        ```
        - ZOOm {RESET|RESETLive}
        - ZOOm?
        ```

    Info:
        - ``RESET`` resets the zoom transforms to default values for all traces.
        - ``RESETLive`` resets the zoom transforms to default values for live traces.

    Properties:
        - ``.graticule``: The ``ZOOm:GRAticule`` command tree.
        - ``.horizontal``: The ``ZOOm:HORizontal`` command tree.
        - ``.math``: The ``ZOOm:MATH<x>`` command tree.
        - ``.mode``: The ``ZOOm:MODe`` command.
        - ``.ref``: The ``ZOOm:REF<x>`` command tree.
        - ``.scroll``: The ``ZOOm:SCROLL`` command tree.
        - ``.state``: The ``ZOOm:STATE`` command.
        - ``.vertical``: The ``ZOOm:VERTical`` command tree.
        - ``.zoom1``: The ``ZOOm:ZOOM1`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ZOOm") -> None:
        super().__init__(device, cmd_syntax)
        self._graticule = ZoomGraticule(device, f"{self._cmd_syntax}:GRAticule")
        self._horizontal = ZoomHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._math: Dict[int, ZoomMathItem] = DefaultDictPassKeyToFactory(
            lambda x: ZoomMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )
        self._mode = ZoomMode(device, f"{self._cmd_syntax}:MODe")
        self._ref: Dict[int, ZoomRefItem] = DefaultDictPassKeyToFactory(
            lambda x: ZoomRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._scroll = ZoomScroll(device, f"{self._cmd_syntax}:SCROLL")
        self._state = ZoomState(device, f"{self._cmd_syntax}:STATE")
        self._vertical = ZoomVertical(device, f"{self._cmd_syntax}:VERTical")
        self._zoom1 = ZoomZoom1(device, f"{self._cmd_syntax}:ZOOM1")

    @property
    def graticule(self) -> ZoomGraticule:
        """Return the ``ZOOm:GRAticule`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:GRAticule?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:GRAticule?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``ZOOm:GRAticule:SIZE`` command.
            - ``.split``: The ``ZOOm:GRAticule:SPLit`` command.
        """
        return self._graticule

    @property
    def horizontal(self) -> ZoomHorizontal:
        """Return the ``ZOOm:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:HORizontal?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:HORizontal:POSition`` command.
            - ``.scale``: The ``ZOOm:HORizontal:SCAle`` command.
        """
        return self._horizontal

    @property
    def math(self) -> Dict[int, ZoomMathItem]:
        """Return the ``ZOOm:MATH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.horizontal``: The ``ZOOm:MATH<x>:HORizontal`` command tree.
            - ``.vertical``: The ``ZOOm:MATH<x>:VERTical`` command tree.
        """
        return self._math

    @property
    def mode(self) -> ZoomMode:
        """Return the ``ZOOm:MODe`` command.

        Description:
            - This command turns Zoom mode on or off. The Zoom query returns the current state of
              Zoom mode. This command is equivalent to pressing the ZOOM button located on the front
              panel.

        Usage:
            - Using the ``.write(value)`` method will send the ``ZOOm:MODe value`` command.

        SCPI Syntax:
            ```
            - ZOOm:MODe {ON|OFF|<NR1>}
            ```

        Info:
            - ``ON`` turns on Zoom mode.
            - ``OFF`` turns off Zoom mode.
            - ``<NR1>`` = 0 turns off Zoom mode; any other value turns on Zoom mode.
        """
        return self._mode

    @property
    def ref(self) -> Dict[int, ZoomRefItem]:
        """Return the ``ZOOm:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.horizontal``: The ``ZOOm:REF<x>:HORizontal`` command tree.
            - ``.vertical``: The ``ZOOm:REF<x>:VERTical`` command tree.
        """
        return self._ref

    @property
    def scroll(self) -> ZoomScroll:
        """Return the ``ZOOm:SCROLL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:SCROLL?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:SCROLL?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.direction``: The ``ZOOm:SCROLL:DIREction`` command.
            - ``.lock``: The ``ZOOm:SCROLL:LOCk`` command.
            - ``.speed``: The ``ZOOm:SCROLL:SPEED`` command.
        """
        return self._scroll

    @property
    def state(self) -> ZoomState:
        """Return the ``ZOOm:STATE`` command.

        Description:
            - This command sets or queries the specified zoom on or off.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:STATE value`` command.

        SCPI Syntax:
            ```
            - ZOOm:STATE {ON|OFF|<NR1>}
            - ZOOm:STATE?
            ```

        Info:
            - ``ON`` turns zoom on or off.
            - ``OFF`` turns zoom on or off.
            - ``<NR1>`` = 0 disables the zoom; any other value enables the zoom.
        """
        return self._state

    @property
    def vertical(self) -> ZoomVertical:
        """Return the ``ZOOm:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:VERTical?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``ZOOm:VERTical:POSition`` command.
            - ``.scale``: The ``ZOOm:VERTical:SCAle`` command.
        """
        return self._vertical

    @property
    def zoom1(self) -> ZoomZoom1:
        """Return the ``ZOOm:ZOOM1`` command.

        Description:
            - This command resets the zoom transforms to default values for all traces of the
              specified zoom, where x is an integer from 1 to 4 representing the desired zoom
              window. The ``ZOOM:REFX:VERTICAL:SCALE?`` query returns the current vertical and
              horizontal positioning and scaling of the display.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm:ZOOM1?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm:ZOOM1?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm:ZOOM1 value`` command.

        SCPI Syntax:
            ```
            - ZOOm:ZOOM1 {RESET|RESETLive}
            - ZOOm:ZOOM1?
            ```

        Info:
            - ``RESET`` resets the zoom transforms to default values for all traces of the specified
              zoom.
            - ``RESETLive`` resets the zoom transforms to default values for live traces of the
              specified zoom.

        Sub-properties:
            - ``.dchan``: The ``ZOOm:ZOOM1:DCHAN`` command tree.
            - ``.scrolllock``: The ``ZOOm:ZOOM1:SCROLLLock`` command.
            - ``.state``: The ``ZOOm:ZOOM1:STATE`` command.
            - ``.ch``: The ``ZOOm:ZOOM1:CH<x>`` command tree.
            - ``.math``: The ``ZOOm:ZOOM1:MATH<x>`` command tree.
            - ``.ref``: The ``ZOOm:ZOOM1:REF<x>`` command tree.
            - ``.d``: The ``ZOOm:ZOOM1:D<x>`` command tree.
        """
        return self._zoom1
