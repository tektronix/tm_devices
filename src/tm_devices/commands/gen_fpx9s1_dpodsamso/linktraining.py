"""The linktraining commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB, MSO70KC,
MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - LINKTRaining:ACQTime <NR1>
    - LINKTRaining:ACQTime?
    - LINKTRaining:ARMscope <OFF | ON>
    - LINKTRaining:ARMscope?
    - LINKTRaining:DECOde <OFF | ON>
    - LINKTRaining:DECOde?
    - LINKTRaining:EQUalizationCH<x> <NR1>
    - LINKTRaining:EQUalizationCH<x>?
    - LINKTRaining:LANE <x> {<NR1>|OFF|ON}
    - LINKTRaining:LANE?
    - LINKTRaining:MARK <FRAme | CONtrol | TRAining>
    - LINKTRaining:SETUP <SAVe |RESTore>
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class LinktrainingSetup(SCPICmdWrite):
    """The ``LINKTRaining:SETUP`` command.

    Description:
        - This 70KSX command saves or restores custom Link Training setup files. The setup files are
          complete instrument setup files. The setup files are saved/restored depending on the
          current values for Link Training Standard, Trigger-On, and Lane selections. You only need
          to use this command when you desire to preserve custom Vertical, Horizontal, or Zoom
          settings for the particular Link Training mode you are using. When Link Training is
          enabled, you may dismiss the pop-up control window and make custom changes to the
          Vertical, Horizontal, or Zoom settings, for example, to accommodate various probes or
          record length requirements. If you want to save these settings for future use, just issue
          the ``LINKTRaining:SETUP SAVe`` command. You can restore the factory Link Training setup
          at any time by using the ``LINKTRaining:SETUP RESTore`` command. UI buttons for these
          operations are also supplied via the Customize button on the pop-up UI for Link Training.
          You do not need to enter any file or directory names to use these commands. When you save
          your custom setup with this command, the Link Training setup file pertaining to the
          current Standard, Trigger-On, and Lane selections is overwritten with your new setup. You
          may restore the factory Link Training setup file at any time. Again, these commands
          save/restore the complete instrument setup for the particular Link Training mode currently
          selected. The Link Training application is only available on the 70KSX scopes.

    Usage:
        - Using the ``.write(value)`` method will send the ``LINKTRaining:SETUP value`` command.

    SCPI Syntax:
        ```
        - LINKTRaining:SETUP <SAVe |RESTore>
        ```

    Info:
        - ``SAVe`` saves your custom Link Training setup.
        - ``RESTore`` restores the custom Link Training setup.
    """


class LinktrainingMark(SCPICmdWrite):
    """The ``LINKTRaining:MARK`` command.

    Description:
        - This command sets or queries the Mark setting of the Link Training application. The
          default argument value is FRAme, which marks the Frame Marker. When the argument is set to
          CONtrol, the frame Control Channel information is marked (32 cells of
          differential-Manchester-encoded request/response data). When the argument is TRAining, the
          PRBS Training Data is marked. Marking the PRBS Training Data is useful for giving you the
          beginning/ending of the Training Data section of the frame when you want to use
          cursor-gated DPOJET measurements. Link Training is only available on the 70KSX family of
          oscilloscopes.

    Usage:
        - Using the ``.write(value)`` method will send the ``LINKTRaining:MARK value`` command.

    SCPI Syntax:
        ```
        - LINKTRaining:MARK <FRAme | CONtrol | TRAining>
        ```

    Info:
        - ``FRAme`` sets Link Training MARK to FRAME.
        - ``CONtrol`` sets Link Training MARK to CONTROL.
        - ``TRAining`` sets Link Training MARK to TRAINING.
    """


class LinktrainingLane(SCPICmdWrite, SCPICmdRead):
    """The ``LINKTRaining:LANE`` command.

    Description:
        - This command sets or queries the activation of the individual communications lanes under
          test. The defaults are Lane1 ON, and Lane2 OFF. It is taken as given that Lane1 uses
          oscilloscope Ch1 and Ch3, Lane2 uses oscilloscope Ch2 and Ch4 (to maximize sample rate).
          ATI DPO70000SX oscilloscopes only support Lane1 (on Ch1 and Ch3). <X> is the lane number
          and can be 1 or 2. One or two lanes may be tested on a single 4-channel DPO70000SX
          oscilloscope. To test up to 4 lanes simultaneously, two oscilloscopes running in
          Standalone mode may be used. This is necessary because the Time-Sync Standalone mode does
          not support independent triggering by multiple oscilloscopes. The associated Link Training
          Arm PI command or UI button, may be used to arm each oscilloscope individually. When the
          Link Training signal is generated by the devices under test, the individual oscilloscopes
          will each trigger, capturing the waveforms on their respective displays and the protocol
          information in their respective Results Tables. Note that each Lane requires two
          oscilloscope channels, because the lanes are bi-directional (Full Duplex). Link Training
          is available on DPO70000SX oscilloscopes only.

    Usage:
        - Using the ``.query()`` method will send the ``LINKTRaining:LANE?`` query.
        - Using the ``.verify(value)`` method will send the ``LINKTRaining:LANE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LINKTRaining:LANE value`` command.

    SCPI Syntax:
        ```
        - LINKTRaining:LANE <x> {<NR1>|OFF|ON}
        - LINKTRaining:LANE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the specified lane; any other value enables the specified lane.
        - ``OFF`` disables the specified lane.
        - ``ON`` enables the specified lane.
    """


class LinktrainingEqualizationchItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``LINKTRaining:EQUalizationCH<x>`` command.

    Description:
        - This 70KSX command sets the equalization value for Link Training of the specified channel.
          The default setting is zero. The units are dB. If you are probing a signal near to the
          transmitter, you likely do not need to increase the equalization value. However, if you
          are probing on a backplane, or other situation where the signal is seriously attenuated,
          you may want to increase the equalization value. Note that this equalization only applies
          to the trigger path in the oscilloscope. It does not apply to the data path. Use the SDLA
          option to provide equalization/de-embedding on the data path. Increasing the trigger path
          equalization value will improve the protocol data recovered into the Link Training Results
          Table when you are probing a seriously attenuated signal. Use the SDLA option to improve
          the equalization of the data path waveforms displayed on the oscilloscope. Since the
          protocol data (Ethernet Control Channel Coefficient Updates and Status Responses) is
          transmitted at ¼ the nominal bit rate (25 Gb/s for 100G Ethernet), the equalization value
          should be set considering ½ that reduced bitrate. For example, for 100G Ethernet, the
          protocol data is transmitted at 6.25 Gb/s, so set the equalization value considering half
          of that rate, 3.125 Gb/s. The Link Training application is only available on the 70KSX
          scopes.

    Usage:
        - Using the ``.query()`` method will send the ``LINKTRaining:EQUalizationCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``LINKTRaining:EQUalizationCH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LINKTRaining:EQUalizationCH<x> value``
          command.

    SCPI Syntax:
        ```
        - LINKTRaining:EQUalizationCH<x> <NR1>
        - LINKTRaining:EQUalizationCH<x>?
        ```
    """


class LinktrainingDecode(SCPICmdWrite, SCPICmdRead):
    """The ``LINKTRaining:DECOde`` command.

    Description:
        - This 70KSX command sets or queries the Decode setting of the Link Training application.
          The default argument value is ON, which decodes the Control Channel information on the
          waveform display. Other system decode parameters optionally allow the Control Channel Hex
          Decode to be expanded to also include bit-level decode. The only plausible reason to turn
          off decoding is to save time when you are capturing a very long record using TRIGgeron
          ``FIRst_frame`` or ``LASt_frame``. With TRIGgeron ``ALL_frames``, the overhead for
          decoding is very small. Link Training is only available on the 70KSX family of
          oscilloscopes.

    Usage:
        - Using the ``.query()`` method will send the ``LINKTRaining:DECOde?`` query.
        - Using the ``.verify(value)`` method will send the ``LINKTRaining:DECOde?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LINKTRaining:DECOde value`` command.

    SCPI Syntax:
        ```
        - LINKTRaining:DECOde <OFF | ON>
        - LINKTRaining:DECOde?
        ```

    Info:
        - ``OFF`` indicates decode is OFF.
        - ``ON`` indicates decode is ON.
    """


class LinktrainingArmscope(SCPICmdWrite, SCPICmdRead):
    """The ``LINKTRaining:ARMscope`` command.

    Description:
        - This 70KSX command sets or queries the ARMscope setting of the Link Training application
          on the 70KSX family of scopes. The default argument value is OFF. To use the Link Training
          application, the State argument must first be set to ON. With the DUT Lane 'powered down'
          (flat-line), you then Arm the scope for single-step capture using this command. When you
          subsequently initiate Link Training on the DUT ('power-up' the lane), the Control Channel
          data and digitized waveforms are captured by the scope. At a minimum, to capture the Link
          Training data into a Results Table, both the ``LINKTTRaining:STAte ON`` and
          ``LINKTRaining:ARMscope ON`` commands must be issued, in that order. When Link Training is
          initiated on the DUT lane, the Results Table data and digitized waveforms will be
          captured. You may select other Link Training settings using the related commands shown
          below to control those features. Initiating Link Training on the DUT is a DUT-dependent
          operation that is usually accomplished by a (serial or other bus) command to the DUT to
          power-up the Lane under test. Sometimes, it can be as simple as un-plugging and
          re-plugging the signal connector for the lane. Note that it is not necessary to set the
          ARMscope to OFF as this is done automatically by the system. To summarize, the minimum
          sequence of events to capture 100G Ethernet KR4 from Default Setup is
          ``:LINKTRaining:STATE ON`` ``:LINKTRaining:ARMscope ON`` Initiate Link Training on the
          Lane under test on the DUT. The Results Table and Waveforms are captured on the scope. To
          repeat the experiment, all you have to do is power-down the lane on the DUT, re-issue the
          ARMscope command, and power-up the lane on the DUT again. Link Training is only available
          on the 70KSX oscilloscopes.

    Usage:
        - Using the ``.query()`` method will send the ``LINKTRaining:ARMscope?`` query.
        - Using the ``.verify(value)`` method will send the ``LINKTRaining:ARMscope?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LINKTRaining:ARMscope value`` command.

    SCPI Syntax:
        ```
        - LINKTRaining:ARMscope <OFF | ON>
        - LINKTRaining:ARMscope?
        ```

    Info:
        - ``OFF`` indicates ARMscope is OFF.
        - ``ON`` indicates ARMscope is ON.
    """


class LinktrainingAcqtime(SCPICmdWrite, SCPICmdRead):
    """The ``LINKTRaining:ACQTime`` command.

    Description:
        - This 70KSX command sets the maximum Acquire Time for Link Training from 1 to 10 seconds.
          The default value is 2 seconds. The link training process is defined by the IEEE to
          complete within 500 ms. So, the default 2 seconds is sufficient for most purposes.
          However, some devices can be put into a mode where the Link Training process is repeated
          continuously. In this special case you may want to increase the acquire time. Increasing
          the acquire time will capture more rows of protocol data into the Link Training Results
          Table. Naturally, you will have to wait a little longer for the acquisition to complete.
          The Link Training application is only available on the 70KSX oscilloscopes.

    Usage:
        - Using the ``.query()`` method will send the ``LINKTRaining:ACQTime?`` query.
        - Using the ``.verify(value)`` method will send the ``LINKTRaining:ACQTime?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LINKTRaining:ACQTime value`` command.

    SCPI Syntax:
        ```
        - LINKTRaining:ACQTime <NR1>
        - LINKTRaining:ACQTime?
        ```

    Info:
        - ``<NR1>`` is the maximum Acquire Time for Link Training from 1 to 10 seconds.
    """


class Linktraining(SCPICmdRead):
    """The ``LINKTRaining`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``LINKTRaining?`` query.
        - Using the ``.verify(value)`` method will send the ``LINKTRaining?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.acqtime``: The ``LINKTRaining:ACQTime`` command.
        - ``.armscope``: The ``LINKTRaining:ARMscope`` command.
        - ``.decode``: The ``LINKTRaining:DECOde`` command.
        - ``.equalizationch``: The ``LINKTRaining:EQUalizationCH<x>`` command.
        - ``.lane``: The ``LINKTRaining:LANE`` command.
        - ``.mark``: The ``LINKTRaining:MARK`` command.
        - ``.setup``: The ``LINKTRaining:SETUP`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "LINKTRaining"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._acqtime = LinktrainingAcqtime(device, f"{self._cmd_syntax}:ACQTime")
        self._armscope = LinktrainingArmscope(device, f"{self._cmd_syntax}:ARMscope")
        self._decode = LinktrainingDecode(device, f"{self._cmd_syntax}:DECOde")
        self._equalizationch: Dict[int, LinktrainingEqualizationchItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: LinktrainingEqualizationchItem(
                    device, f"{self._cmd_syntax}:EQUalizationCH{x}"
                )
            )
        )
        self._lane = LinktrainingLane(device, f"{self._cmd_syntax}:LANE")
        self._mark = LinktrainingMark(device, f"{self._cmd_syntax}:MARK")
        self._setup = LinktrainingSetup(device, f"{self._cmd_syntax}:SETUP")

    @property
    def acqtime(self) -> LinktrainingAcqtime:
        """Return the ``LINKTRaining:ACQTime`` command.

        Description:
            - This 70KSX command sets the maximum Acquire Time for Link Training from 1 to 10
              seconds. The default value is 2 seconds. The link training process is defined by the
              IEEE to complete within 500 ms. So, the default 2 seconds is sufficient for most
              purposes. However, some devices can be put into a mode where the Link Training process
              is repeated continuously. In this special case you may want to increase the acquire
              time. Increasing the acquire time will capture more rows of protocol data into the
              Link Training Results Table. Naturally, you will have to wait a little longer for the
              acquisition to complete. The Link Training application is only available on the 70KSX
              oscilloscopes.

        Usage:
            - Using the ``.query()`` method will send the ``LINKTRaining:ACQTime?`` query.
            - Using the ``.verify(value)`` method will send the ``LINKTRaining:ACQTime?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LINKTRaining:ACQTime value``
              command.

        SCPI Syntax:
            ```
            - LINKTRaining:ACQTime <NR1>
            - LINKTRaining:ACQTime?
            ```

        Info:
            - ``<NR1>`` is the maximum Acquire Time for Link Training from 1 to 10 seconds.
        """
        return self._acqtime

    @property
    def armscope(self) -> LinktrainingArmscope:
        """Return the ``LINKTRaining:ARMscope`` command.

        Description:
            - This 70KSX command sets or queries the ARMscope setting of the Link Training
              application on the 70KSX family of scopes. The default argument value is OFF. To use
              the Link Training application, the State argument must first be set to ON. With the
              DUT Lane 'powered down' (flat-line), you then Arm the scope for single-step capture
              using this command. When you subsequently initiate Link Training on the DUT
              ('power-up' the lane), the Control Channel data and digitized waveforms are captured
              by the scope. At a minimum, to capture the Link Training data into a Results Table,
              both the ``LINKTTRaining:STAte ON`` and ``LINKTRaining:ARMscope ON`` commands must be
              issued, in that order. When Link Training is initiated on the DUT lane, the Results
              Table data and digitized waveforms will be captured. You may select other Link
              Training settings using the related commands shown below to control those features.
              Initiating Link Training on the DUT is a DUT-dependent operation that is usually
              accomplished by a (serial or other bus) command to the DUT to power-up the Lane under
              test. Sometimes, it can be as simple as un-plugging and re-plugging the signal
              connector for the lane. Note that it is not necessary to set the ARMscope to OFF as
              this is done automatically by the system. To summarize, the minimum sequence of events
              to capture 100G Ethernet KR4 from Default Setup is ``:LINKTRaining:STATE ON``
              ``:LINKTRaining:ARMscope ON`` Initiate Link Training on the Lane under test on the
              DUT. The Results Table and Waveforms are captured on the scope. To repeat the
              experiment, all you have to do is power-down the lane on the DUT, re-issue the
              ARMscope command, and power-up the lane on the DUT again. Link Training is only
              available on the 70KSX oscilloscopes.

        Usage:
            - Using the ``.query()`` method will send the ``LINKTRaining:ARMscope?`` query.
            - Using the ``.verify(value)`` method will send the ``LINKTRaining:ARMscope?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LINKTRaining:ARMscope value``
              command.

        SCPI Syntax:
            ```
            - LINKTRaining:ARMscope <OFF | ON>
            - LINKTRaining:ARMscope?
            ```

        Info:
            - ``OFF`` indicates ARMscope is OFF.
            - ``ON`` indicates ARMscope is ON.
        """
        return self._armscope

    @property
    def decode(self) -> LinktrainingDecode:
        """Return the ``LINKTRaining:DECOde`` command.

        Description:
            - This 70KSX command sets or queries the Decode setting of the Link Training
              application. The default argument value is ON, which decodes the Control Channel
              information on the waveform display. Other system decode parameters optionally allow
              the Control Channel Hex Decode to be expanded to also include bit-level decode. The
              only plausible reason to turn off decoding is to save time when you are capturing a
              very long record using TRIGgeron ``FIRst_frame`` or ``LASt_frame``. With TRIGgeron
              ``ALL_frames``, the overhead for decoding is very small. Link Training is only
              available on the 70KSX family of oscilloscopes.

        Usage:
            - Using the ``.query()`` method will send the ``LINKTRaining:DECOde?`` query.
            - Using the ``.verify(value)`` method will send the ``LINKTRaining:DECOde?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LINKTRaining:DECOde value``
              command.

        SCPI Syntax:
            ```
            - LINKTRaining:DECOde <OFF | ON>
            - LINKTRaining:DECOde?
            ```

        Info:
            - ``OFF`` indicates decode is OFF.
            - ``ON`` indicates decode is ON.
        """
        return self._decode

    @property
    def equalizationch(self) -> Dict[int, LinktrainingEqualizationchItem]:
        """Return the ``LINKTRaining:EQUalizationCH<x>`` command.

        Description:
            - This 70KSX command sets the equalization value for Link Training of the specified
              channel. The default setting is zero. The units are dB. If you are probing a signal
              near to the transmitter, you likely do not need to increase the equalization value.
              However, if you are probing on a backplane, or other situation where the signal is
              seriously attenuated, you may want to increase the equalization value. Note that this
              equalization only applies to the trigger path in the oscilloscope. It does not apply
              to the data path. Use the SDLA option to provide equalization/de-embedding on the data
              path. Increasing the trigger path equalization value will improve the protocol data
              recovered into the Link Training Results Table when you are probing a seriously
              attenuated signal. Use the SDLA option to improve the equalization of the data path
              waveforms displayed on the oscilloscope. Since the protocol data (Ethernet Control
              Channel Coefficient Updates and Status Responses) is transmitted at ¼ the nominal bit
              rate (25 Gb/s for 100G Ethernet), the equalization value should be set considering ½
              that reduced bitrate. For example, for 100G Ethernet, the protocol data is transmitted
              at 6.25 Gb/s, so set the equalization value considering half of that rate, 3.125 Gb/s.
              The Link Training application is only available on the 70KSX scopes.

        Usage:
            - Using the ``.query()`` method will send the ``LINKTRaining:EQUalizationCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``LINKTRaining:EQUalizationCH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``LINKTRaining:EQUalizationCH<x> value`` command.

        SCPI Syntax:
            ```
            - LINKTRaining:EQUalizationCH<x> <NR1>
            - LINKTRaining:EQUalizationCH<x>?
            ```
        """
        return self._equalizationch

    @property
    def lane(self) -> LinktrainingLane:
        """Return the ``LINKTRaining:LANE`` command.

        Description:
            - This command sets or queries the activation of the individual communications lanes
              under test. The defaults are Lane1 ON, and Lane2 OFF. It is taken as given that Lane1
              uses oscilloscope Ch1 and Ch3, Lane2 uses oscilloscope Ch2 and Ch4 (to maximize sample
              rate). ATI DPO70000SX oscilloscopes only support Lane1 (on Ch1 and Ch3). <X> is the
              lane number and can be 1 or 2. One or two lanes may be tested on a single 4-channel
              DPO70000SX oscilloscope. To test up to 4 lanes simultaneously, two oscilloscopes
              running in Standalone mode may be used. This is necessary because the Time-Sync
              Standalone mode does not support independent triggering by multiple oscilloscopes. The
              associated Link Training Arm PI command or UI button, may be used to arm each
              oscilloscope individually. When the Link Training signal is generated by the devices
              under test, the individual oscilloscopes will each trigger, capturing the waveforms on
              their respective displays and the protocol information in their respective Results
              Tables. Note that each Lane requires two oscilloscope channels, because the lanes are
              bi-directional (Full Duplex). Link Training is available on DPO70000SX oscilloscopes
              only.

        Usage:
            - Using the ``.query()`` method will send the ``LINKTRaining:LANE?`` query.
            - Using the ``.verify(value)`` method will send the ``LINKTRaining:LANE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LINKTRaining:LANE value`` command.

        SCPI Syntax:
            ```
            - LINKTRaining:LANE <x> {<NR1>|OFF|ON}
            - LINKTRaining:LANE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the specified lane; any other value enables the specified lane.
            - ``OFF`` disables the specified lane.
            - ``ON`` enables the specified lane.
        """
        return self._lane

    @property
    def mark(self) -> LinktrainingMark:
        """Return the ``LINKTRaining:MARK`` command.

        Description:
            - This command sets or queries the Mark setting of the Link Training application. The
              default argument value is FRAme, which marks the Frame Marker. When the argument is
              set to CONtrol, the frame Control Channel information is marked (32 cells of
              differential-Manchester-encoded request/response data). When the argument is TRAining,
              the PRBS Training Data is marked. Marking the PRBS Training Data is useful for giving
              you the beginning/ending of the Training Data section of the frame when you want to
              use cursor-gated DPOJET measurements. Link Training is only available on the 70KSX
              family of oscilloscopes.

        Usage:
            - Using the ``.write(value)`` method will send the ``LINKTRaining:MARK value`` command.

        SCPI Syntax:
            ```
            - LINKTRaining:MARK <FRAme | CONtrol | TRAining>
            ```

        Info:
            - ``FRAme`` sets Link Training MARK to FRAME.
            - ``CONtrol`` sets Link Training MARK to CONTROL.
            - ``TRAining`` sets Link Training MARK to TRAINING.
        """
        return self._mark

    @property
    def setup(self) -> LinktrainingSetup:
        """Return the ``LINKTRaining:SETUP`` command.

        Description:
            - This 70KSX command saves or restores custom Link Training setup files. The setup files
              are complete instrument setup files. The setup files are saved/restored depending on
              the current values for Link Training Standard, Trigger-On, and Lane selections. You
              only need to use this command when you desire to preserve custom Vertical, Horizontal,
              or Zoom settings for the particular Link Training mode you are using. When Link
              Training is enabled, you may dismiss the pop-up control window and make custom changes
              to the Vertical, Horizontal, or Zoom settings, for example, to accommodate various
              probes or record length requirements. If you want to save these settings for future
              use, just issue the ``LINKTRaining:SETUP SAVe`` command. You can restore the factory
              Link Training setup at any time by using the ``LINKTRaining:SETUP RESTore`` command.
              UI buttons for these operations are also supplied via the Customize button on the
              pop-up UI for Link Training. You do not need to enter any file or directory names to
              use these commands. When you save your custom setup with this command, the Link
              Training setup file pertaining to the current Standard, Trigger-On, and Lane
              selections is overwritten with your new setup. You may restore the factory Link
              Training setup file at any time. Again, these commands save/restore the complete
              instrument setup for the particular Link Training mode currently selected. The Link
              Training application is only available on the 70KSX scopes.

        Usage:
            - Using the ``.write(value)`` method will send the ``LINKTRaining:SETUP value`` command.

        SCPI Syntax:
            ```
            - LINKTRaining:SETUP <SAVe |RESTore>
            ```

        Info:
            - ``SAVe`` saves your custom Link Training setup.
            - ``RESTore`` restores the custom Link Training setup.
        """
        return self._setup
