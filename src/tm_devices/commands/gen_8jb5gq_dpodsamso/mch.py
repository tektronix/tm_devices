"""The mch commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MCH<x>:MAXAMPLitude <NR3>
    - MCH<x>:MINAMPLitude <NR3>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MchItemMinamplitude(SCPICmdWrite):
    """The ``MCH<x>:MINAMPLitude`` command.

    Description:
        - These commands set or query the minimum/maximum amplitude vertical setting for the
          unmapped channels on an UltraSync stack master oscilloscope. These two commands are used
          together to set the vertical amplitude range for the unmapped channels on an UltraSync
          stack master. The vertical system scales the unmapped channel so that a large signal (that
          is not clipped, 6 to 8 divisions high centered about ground or equivalent) is available to
          the trigger system. It is important to match these min/max amplitude settings to the
          actual signal under test. Briefly, in a stack of oscilloscopes, the mapped channels are
          those used to acquire data (one channel from each oscilloscope in the stack). The mapped
          channels on one of the oscilloscopes in a stack can also be used for triggering. The
          unmapped channels on a stack master are also available for triggering. These channels are
          not acquired, so no waveforms for these channels are displayed. These channels are
          designated MCH1, MCH2, MCH3, and MCH4. On an ATI stack, CH2, MCH1, and MCH3 are available
          for triggering. On a 4-channel stack, CH1, MCH2, MCH3, and MCH4 are available for
          triggering. A more detailed discussion follows. Mapped Channels In a stack configuration
          of oscilloscopes, one channel from each extension is mapped to the master along with a
          single channel on the master. The waveforms acquired from these channels on the respective
          oscilloscopes are gathered together for display on the master oscilloscope. These are the
          mapped channels. Unmapped Channels In a stack configuration of oscilloscopes, the master
          has additional channels that are not used for acquiring waveforms, but they can be used to
          trigger the oscilloscope. These channels are called the unmapped channels, and they are
          only available on the master of an UltraSync stack. These unmapped channels on the master
          have their own vertical user interface control tab, where you enter the expected minimum
          and maximum amplitude values for the device under test signals. When you set the min/max
          amplitude values, the oscilloscope hardware is configured so that the device under test
          signals present at the channel probe tip (or input connector) will provide the largest
          possible trigger stimulus without clipping or other nonlinearities. Note that waveforms
          from these unmapped channels are not acquired, and are thus not visible on the
          oscilloscope display. This means you must find a way to quantify the min/max amplitude of
          the device under test signals. One method is to temporarily take the master oscilloscope
          out of the stack (that is, go to standalone mode) to determine the best values for the
          min/max amplitudes of the device under test signals, and then put the master oscilloscope
          back into the UltraSync stack where you then set the vertical min/max amplitude for the
          unmapped channels. These non-acquired, but useful for triggering, unmapped channels on the
          master in an UltraSync stack are referenced by the terms MCH1, MCH2, MCH3, and MCH4 on the
          Vertical menu. Case 1 UltraSync ATI stack in ATI mode: In an ATI stack in ATI mode, all
          ATI channels in the stack are mapped to the master. Waveforms are acquired and displayed
          for all of these ATI channels. The non-acquired unmapped channels on the master are
          available as sources for triggering, and are referenced as MCH1 and MCH3. Case 2 UltraSync
          ATI stack in TekConnect mode: The only unmapped channel on the master is MCh2 (the ATI
          channel). It may be a trigger source. Case 3 UltraSync non-ATI stack (a stack of 4-channel
          oscilloscopes). The unmapped channels on the stack master, MCH2, MCH3, and MCH4, may be
          trigger sources. Case 4 Time-Sync stack. All channels on the master are mapped channels,
          and so are always available as trigger sources. Case 5 Standalone mode (single
          oscilloscope). All channels are mapped channels, and so are always available as trigger
          sources.

    Usage:
        - Using the ``.write(value)`` method will send the ``MCH<x>:MINAMPLitude value`` command.

    SCPI Syntax:
        ```
        - MCH<x>:MINAMPLitude <NR3>
        ```

    Info:
        - ``<NR3>`` the minimum/maximum amplitude vertical setting for the unmapped channels on an
          UltraSync stack master oscilloscope.
    """


class MchItemMaxamplitude(SCPICmdWrite):
    """The ``MCH<x>:MAXAMPLitude`` command.

    Description:
        - These commands set or query the minimum/maximum amplitude vertical setting for the
          unmapped channels on an UltraSync stack master oscilloscope. These two commands are used
          together to set the vertical amplitude range for the unmapped channels on an UltraSync
          stack master. The vertical system scales the unmapped channel so that a large signal (that
          is not clipped, 6 to 8 divisions high centered about ground or equivalent) is available to
          the trigger system. It is important to match these min/max amplitude settings to the
          actual signal under test. Briefly, in a stack of oscilloscopes, the mapped channels are
          those used to acquire data (one channel from each oscilloscope in the stack). The mapped
          channels on one of the oscilloscopes in a stack can also be used for triggering. The
          unmapped channels on a stack master are also available for triggering. These channels are
          not acquired, so no waveforms for these channels are displayed. These channels are
          designated MCH1, MCH2, MCH3, and MCH4. On an ATI stack, CH2, MCH1, and MCH3 are available
          for triggering. On a 4-channel stack, CH1, MCH2, MCH3, and MCH4 are available for
          triggering. A more detailed discussion follows. Mapped Channels In a stack configuration
          of oscilloscopes, one channel from each extension is mapped to the master along with a
          single channel on the master. The waveforms acquired from these channels on the respective
          oscilloscopes are gathered together for display on the master oscilloscope. These are the
          mapped channels. Unmapped Channels In a stack configuration of oscilloscopes, the master
          has additional channels that are not used for acquiring waveforms, but they can be used to
          trigger the oscilloscope. These channels are called the unmapped channels, and they are
          only available on the master of an UltraSync stack. These unmapped channels on the master
          have their own vertical user interface control tab, where you enter the expected minimum
          and maximum amplitude values for the device under test signals. When you set the min/max
          amplitude values, the oscilloscope hardware is configured so that the device under test
          signals present at the channel probe tip (or input connector) will provide the largest
          possible trigger stimulus without clipping or other nonlinearities. Note that waveforms
          from these unmapped channels are not acquired, and are thus not visible on the
          oscilloscope display. This means you must find a way to quantify the min/max amplitude of
          the device under test signals. One method is to temporarily take the master oscilloscope
          out of the stack (that is, go to standalone mode) to determine the best values for the
          min/max amplitudes of the device under test signals, and then put the master oscilloscope
          back into the UltraSync stack where you then set the vertical min/max amplitude for the
          unmapped channels. These non-acquired, but useful for triggering, unmapped channels on the
          master in an UltraSync stack are referenced by the terms MCH1, MCH2, MCH3, and MCH4 on the
          Vertical menu. Case 1 UltraSync ATI stack in ATI mode: In an ATI stack in ATI mode, all
          ATI channels in the stack are mapped to the master. Waveforms are acquired and displayed
          for all of these ATI channels. The non-acquired unmapped channels on the master are
          available as sources for triggering, and are referenced as MCH1 and MCH3. Case 2 UltraSync
          ATI stack in TekConnect mode: The only unmapped channel on the master is MCh2 (the ATI
          channel). It may be a trigger source. Case 3 UltraSync non-ATI stack (a stack of 4-channel
          oscilloscopes). The unmapped channels on the stack master, MCH2, MCH3, and MCH4, may be
          trigger sources. Case 4 Time-Sync stack. All channels on the master are mapped channels,
          and so are always available as trigger sources. Case 5 Standalone mode (single
          oscilloscope). All channels are mapped channels, and so are always available as trigger
          sources.

    Usage:
        - Using the ``.write(value)`` method will send the ``MCH<x>:MAXAMPLitude value`` command.

    SCPI Syntax:
        ```
        - MCH<x>:MAXAMPLitude <NR3>
        ```

    Info:
        - ``<NR3>`` the minimum/maximum amplitude vertical setting for the unmapped channels on an
          UltraSync stack master oscilloscope.
    """


class MchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MCH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.minamplitude``: The ``MCH<x>:MINAMPLitude`` command.
        - ``.maxamplitude``: The ``MCH<x>:MAXAMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MCH<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._minamplitude = MchItemMinamplitude(device, f"{self._cmd_syntax}:MINAMPLitude")
        self._maxamplitude = MchItemMaxamplitude(device, f"{self._cmd_syntax}:MAXAMPLitude")

    @property
    def minamplitude(self) -> MchItemMinamplitude:
        """Return the ``MCH<x>:MINAMPLitude`` command.

        Description:
            - These commands set or query the minimum/maximum amplitude vertical setting for the
              unmapped channels on an UltraSync stack master oscilloscope. These two commands are
              used together to set the vertical amplitude range for the unmapped channels on an
              UltraSync stack master. The vertical system scales the unmapped channel so that a
              large signal (that is not clipped, 6 to 8 divisions high centered about ground or
              equivalent) is available to the trigger system. It is important to match these min/max
              amplitude settings to the actual signal under test. Briefly, in a stack of
              oscilloscopes, the mapped channels are those used to acquire data (one channel from
              each oscilloscope in the stack). The mapped channels on one of the oscilloscopes in a
              stack can also be used for triggering. The unmapped channels on a stack master are
              also available for triggering. These channels are not acquired, so no waveforms for
              these channels are displayed. These channels are designated MCH1, MCH2, MCH3, and
              MCH4. On an ATI stack, CH2, MCH1, and MCH3 are available for triggering. On a
              4-channel stack, CH1, MCH2, MCH3, and MCH4 are available for triggering. A more
              detailed discussion follows. Mapped Channels In a stack configuration of
              oscilloscopes, one channel from each extension is mapped to the master along with a
              single channel on the master. The waveforms acquired from these channels on the
              respective oscilloscopes are gathered together for display on the master oscilloscope.
              These are the mapped channels. Unmapped Channels In a stack configuration of
              oscilloscopes, the master has additional channels that are not used for acquiring
              waveforms, but they can be used to trigger the oscilloscope. These channels are called
              the unmapped channels, and they are only available on the master of an UltraSync
              stack. These unmapped channels on the master have their own vertical user interface
              control tab, where you enter the expected minimum and maximum amplitude values for the
              device under test signals. When you set the min/max amplitude values, the oscilloscope
              hardware is configured so that the device under test signals present at the channel
              probe tip (or input connector) will provide the largest possible trigger stimulus
              without clipping or other nonlinearities. Note that waveforms from these unmapped
              channels are not acquired, and are thus not visible on the oscilloscope display. This
              means you must find a way to quantify the min/max amplitude of the device under test
              signals. One method is to temporarily take the master oscilloscope out of the stack
              (that is, go to standalone mode) to determine the best values for the min/max
              amplitudes of the device under test signals, and then put the master oscilloscope back
              into the UltraSync stack where you then set the vertical min/max amplitude for the
              unmapped channels. These non-acquired, but useful for triggering, unmapped channels on
              the master in an UltraSync stack are referenced by the terms MCH1, MCH2, MCH3, and
              MCH4 on the Vertical menu. Case 1 UltraSync ATI stack in ATI mode: In an ATI stack in
              ATI mode, all ATI channels in the stack are mapped to the master. Waveforms are
              acquired and displayed for all of these ATI channels. The non-acquired unmapped
              channels on the master are available as sources for triggering, and are referenced as
              MCH1 and MCH3. Case 2 UltraSync ATI stack in TekConnect mode: The only unmapped
              channel on the master is MCh2 (the ATI channel). It may be a trigger source. Case 3
              UltraSync non-ATI stack (a stack of 4-channel oscilloscopes). The unmapped channels on
              the stack master, MCH2, MCH3, and MCH4, may be trigger sources. Case 4 Time-Sync
              stack. All channels on the master are mapped channels, and so are always available as
              trigger sources. Case 5 Standalone mode (single oscilloscope). All channels are mapped
              channels, and so are always available as trigger sources.

        Usage:
            - Using the ``.write(value)`` method will send the ``MCH<x>:MINAMPLitude value``
              command.

        SCPI Syntax:
            ```
            - MCH<x>:MINAMPLitude <NR3>
            ```

        Info:
            - ``<NR3>`` the minimum/maximum amplitude vertical setting for the unmapped channels on
              an UltraSync stack master oscilloscope.
        """
        return self._minamplitude

    @property
    def maxamplitude(self) -> MchItemMaxamplitude:
        """Return the ``MCH<x>:MAXAMPLitude`` command.

        Description:
            - These commands set or query the minimum/maximum amplitude vertical setting for the
              unmapped channels on an UltraSync stack master oscilloscope. These two commands are
              used together to set the vertical amplitude range for the unmapped channels on an
              UltraSync stack master. The vertical system scales the unmapped channel so that a
              large signal (that is not clipped, 6 to 8 divisions high centered about ground or
              equivalent) is available to the trigger system. It is important to match these min/max
              amplitude settings to the actual signal under test. Briefly, in a stack of
              oscilloscopes, the mapped channels are those used to acquire data (one channel from
              each oscilloscope in the stack). The mapped channels on one of the oscilloscopes in a
              stack can also be used for triggering. The unmapped channels on a stack master are
              also available for triggering. These channels are not acquired, so no waveforms for
              these channels are displayed. These channels are designated MCH1, MCH2, MCH3, and
              MCH4. On an ATI stack, CH2, MCH1, and MCH3 are available for triggering. On a
              4-channel stack, CH1, MCH2, MCH3, and MCH4 are available for triggering. A more
              detailed discussion follows. Mapped Channels In a stack configuration of
              oscilloscopes, one channel from each extension is mapped to the master along with a
              single channel on the master. The waveforms acquired from these channels on the
              respective oscilloscopes are gathered together for display on the master oscilloscope.
              These are the mapped channels. Unmapped Channels In a stack configuration of
              oscilloscopes, the master has additional channels that are not used for acquiring
              waveforms, but they can be used to trigger the oscilloscope. These channels are called
              the unmapped channels, and they are only available on the master of an UltraSync
              stack. These unmapped channels on the master have their own vertical user interface
              control tab, where you enter the expected minimum and maximum amplitude values for the
              device under test signals. When you set the min/max amplitude values, the oscilloscope
              hardware is configured so that the device under test signals present at the channel
              probe tip (or input connector) will provide the largest possible trigger stimulus
              without clipping or other nonlinearities. Note that waveforms from these unmapped
              channels are not acquired, and are thus not visible on the oscilloscope display. This
              means you must find a way to quantify the min/max amplitude of the device under test
              signals. One method is to temporarily take the master oscilloscope out of the stack
              (that is, go to standalone mode) to determine the best values for the min/max
              amplitudes of the device under test signals, and then put the master oscilloscope back
              into the UltraSync stack where you then set the vertical min/max amplitude for the
              unmapped channels. These non-acquired, but useful for triggering, unmapped channels on
              the master in an UltraSync stack are referenced by the terms MCH1, MCH2, MCH3, and
              MCH4 on the Vertical menu. Case 1 UltraSync ATI stack in ATI mode: In an ATI stack in
              ATI mode, all ATI channels in the stack are mapped to the master. Waveforms are
              acquired and displayed for all of these ATI channels. The non-acquired unmapped
              channels on the master are available as sources for triggering, and are referenced as
              MCH1 and MCH3. Case 2 UltraSync ATI stack in TekConnect mode: The only unmapped
              channel on the master is MCh2 (the ATI channel). It may be a trigger source. Case 3
              UltraSync non-ATI stack (a stack of 4-channel oscilloscopes). The unmapped channels on
              the stack master, MCH2, MCH3, and MCH4, may be trigger sources. Case 4 Time-Sync
              stack. All channels on the master are mapped channels, and so are always available as
              trigger sources. Case 5 Standalone mode (single oscilloscope). All channels are mapped
              channels, and so are always available as trigger sources.

        Usage:
            - Using the ``.write(value)`` method will send the ``MCH<x>:MAXAMPLitude value``
              command.

        SCPI Syntax:
            ```
            - MCH<x>:MAXAMPLitude <NR3>
            ```

        Info:
            - ``<NR3>`` the minimum/maximum amplitude vertical setting for the unmapped channels on
              an UltraSync stack master oscilloscope.
        """
        return self._maxamplitude
