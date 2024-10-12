# pylint: disable=line-too-long
"""The linktraining commands module.

These commands are used in the following models:
DPO70KSX

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
    - LINKTRaining:STANdard <Ethernet_10G_KR | Ethernet_25G_KR | Ethernet_25G_CR | Ethernet_40G_KR4 | Ethernet_40G_CR4 | Ethernet_50G_KR | Ethernet_50G_CR | Ethernet_100G_CR10 | Ethernet_100G_CR4 | Ethernet_100G_KR4 | Ethernet_100G_CR2 | Ethernet_100G_KR2 | Ethernet_200G_KR4 | Ethernet_200G_CR4>
    - LINKTRaining:STANdard?
    - LINKTRaining:STAte <OFF | ON>
    - LINKTRaining:STAte?
    - LINKTRaining:TRIGgeron <FIRst_frame | LASt_frame | ALL_frames>
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class LinktrainingTriggeron(SCPICmdWrite):
    r"""The ``LINKTRaining:TRIGgeron`` command.

    Description:
        - This DPO70000SX command sets or queries the TriggerOn setting of the Link Training
          application. The default argument value is ``ALL_FRAMES``, which attempts to trigger the
          scope whenever any Frame Control Channel contains new (changed) data values to capture
          FastFrame record waveforms. When the TriggerOn argument is ``FIRST_FRAME`` or
          ``LAST_FRAME``, a single record waveform is captured, and the user may select the record
          length and horizontal position, among other settings, for this waveform. When the
          TriggerOn argument is ``ALL_FRAMES``, FastFrame records are captured containing the
          decoded and marked Control Channel information. The user may select the FastFrame Length
          and maximum number of Frames (< 512 at this writing). Note that the Results Table captures
          all of the Control Channel data on both scope channels of a given lane, no matter what the
          TriggerOn argument value is chosen, because the data is captured by hardware in real-time
          ('100% live'). This means that the data in the Results Table is derived directly from the
          signal, not from the digitized waveform (that would be decoding, and we do that where
          possible). However, only some of the Control Channel values in the Results Table will be
          backed with Waveforms on the display, because the Frames may arrive faster than the
          Acquisition System can capture and store the FastFrame waveforms, or because the Link
          Training process takes more time, up to 500ms, than can be captured in a single long
          record at any reasonable sample rate. When rows in the Results Table are not backed by an
          acquired waveform on the display, three asterisks (\*\*\*) are shown in the Frame column.
          Remember, all of the Control Channel data is captured in the Results Table for all three
          Triggeron settings. So, you should rely on the data in the Results Table, using the
          waveform decoding as confirmation. Don't forget that you can use cursor-gated DPOJET
          measurements to analyze the marked waveforms that are captured. The cursor positioning is
          made easier if you set the Link Training Marks to be TRAining to delineate the PRBS
          Training Data section of the Frames. Then you can use the extents of the MARK to better
          position the cursors for the measurements. Link Training is only available on the
          DPO70000SX family of oscilloscopes.

    Usage:
        - Using the ``.write(value)`` method will send the ``LINKTRaining:TRIGgeron value`` command.

    SCPI Syntax:
        ```
        - LINKTRaining:TRIGgeron <FIRst_frame | LASt_frame | ALL_frames>
        ```

    Info:
        - ``FIRst_frame`` sets Link Training TRIGgeron to ``FIRst_frame``.
        - ``LASt_frame`` sets Link Training TRIGgeron to ``LASt_frame``.
        - ``ALL_frames`` sets Link Training TRIGgeron to ``ALL_frames``.
    """


class LinktrainingState(SCPICmdWrite, SCPICmdRead):
    """The ``LINKTRaining:STAte`` command.

    Description:
        - This DPO70000SX command sets or queries the state of the Link Training application on the
          DPO70000SX family of oscilloscopes. The default argument value is OFF. To use the Link
          Training application, the State argument must first be set to ON. At a minimum, to capture
          the Link Training data into a Results Table, the ``LINKTRaining:ARMscope ON`` command also
          must be issued after the Link Training State is ON. Once the State is ON and the ARMscope
          is ON, the Link Training Results Table data will be captured when Link Training is
          initiated on the DUT. Initiating Link Training on the DUT is a DUT-dependent operation
          that is usually accomplished by a (serial or other bus) command to the DUT to power-up the
          Lane under test. Sometimes, it can be as simple as un-plugging and re-plugging the signal
          connector for the lane. To summarize, the minimum sequence of events to capture 100G
          Ethernet KR4 from Default Setup is ``:LINKTRaining:STATE ON``
          ``:LINKTRaining:ARMscope ON`` Initiate Link Training on the Lane under test on the DUT.
          The Results Table and Waveforms are captured on the scope. Link Training is only available
          on the DPO70000SX oscilloscopes.

    Usage:
        - Using the ``.query()`` method will send the ``LINKTRaining:STAte?`` query.
        - Using the ``.verify(value)`` method will send the ``LINKTRaining:STAte?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LINKTRaining:STAte value`` command.

    SCPI Syntax:
        ```
        - LINKTRaining:STAte <OFF | ON>
        - LINKTRaining:STAte?
        ```

    Info:
        - ``OFF`` sets Link Training State to OFF.
        - ``ON`` sets Link Training State to ON.
    """


class LinktrainingStandard(SCPICmdWrite, SCPICmdRead):
    """The ``LINKTRaining:STANdard`` command.

    Description:
        - This DPO70000SX command sets or queries the communication standard for the Link Training
          application on DPO70000SX oscilloscopes. The default argument value is
          ``Ethernet_100G_KR4``. Link Training is only available on the DPO70000SX family of
          oscilloscopes.

    Usage:
        - Using the ``.query()`` method will send the ``LINKTRaining:STANdard?`` query.
        - Using the ``.verify(value)`` method will send the ``LINKTRaining:STANdard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LINKTRaining:STANdard value`` command.

    SCPI Syntax:
        ```
        - LINKTRaining:STANdard <Ethernet_10G_KR | Ethernet_25G_KR | Ethernet_25G_CR | Ethernet_40G_KR4 | Ethernet_40G_CR4 | Ethernet_50G_KR | Ethernet_50G_CR | Ethernet_100G_CR10 | Ethernet_100G_CR4 | Ethernet_100G_KR4 | Ethernet_100G_CR2 | Ethernet_100G_KR2 | Ethernet_200G_KR4 | Ethernet_200G_CR4>
        - LINKTRaining:STANdard?
        ```

    Info:
        - ``Ethernet_10G_KR``
        - ``Ethernet_25G_KR``
        - ``Ethernet_25G_CR``
        - ``Ethernet_40G_KR4``
        - ``Ethernet_40G_CR4``
        - ``Ethernet_50G_KR``
        - ``Ethernet_50G_CR``
        - ``Ethernet_100G_CR10``
        - ``Ethernet_100G_CR4``
        - ``Ethernet_100G_KR4``
        - ``Ethernet_100G_CR2``
        - ``Ethernet_100G_KR2``
        - ``Ethernet_200G_KR4``
        - ``Ethernet_200G_CR4``
    """  # noqa: E501


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


#  pylint: disable=too-many-instance-attributes
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
        - ``.standard``: The ``LINKTRaining:STANdard`` command.
        - ``.state``: The ``LINKTRaining:STAte`` command.
        - ``.triggeron``: The ``LINKTRaining:TRIGgeron`` command.
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
        self._standard = LinktrainingStandard(device, f"{self._cmd_syntax}:STANdard")
        self._state = LinktrainingState(device, f"{self._cmd_syntax}:STAte")
        self._triggeron = LinktrainingTriggeron(device, f"{self._cmd_syntax}:TRIGgeron")

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

    @property
    def standard(self) -> LinktrainingStandard:
        """Return the ``LINKTRaining:STANdard`` command.

        Description:
            - This DPO70000SX command sets or queries the communication standard for the Link
              Training application on DPO70000SX oscilloscopes. The default argument value is
              ``Ethernet_100G_KR4``. Link Training is only available on the DPO70000SX family of
              oscilloscopes.

        Usage:
            - Using the ``.query()`` method will send the ``LINKTRaining:STANdard?`` query.
            - Using the ``.verify(value)`` method will send the ``LINKTRaining:STANdard?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LINKTRaining:STANdard value``
              command.

        SCPI Syntax:
            ```
            - LINKTRaining:STANdard <Ethernet_10G_KR | Ethernet_25G_KR | Ethernet_25G_CR | Ethernet_40G_KR4 | Ethernet_40G_CR4 | Ethernet_50G_KR | Ethernet_50G_CR | Ethernet_100G_CR10 | Ethernet_100G_CR4 | Ethernet_100G_KR4 | Ethernet_100G_CR2 | Ethernet_100G_KR2 | Ethernet_200G_KR4 | Ethernet_200G_CR4>
            - LINKTRaining:STANdard?
            ```

        Info:
            - ``Ethernet_10G_KR``
            - ``Ethernet_25G_KR``
            - ``Ethernet_25G_CR``
            - ``Ethernet_40G_KR4``
            - ``Ethernet_40G_CR4``
            - ``Ethernet_50G_KR``
            - ``Ethernet_50G_CR``
            - ``Ethernet_100G_CR10``
            - ``Ethernet_100G_CR4``
            - ``Ethernet_100G_KR4``
            - ``Ethernet_100G_CR2``
            - ``Ethernet_100G_KR2``
            - ``Ethernet_200G_KR4``
            - ``Ethernet_200G_CR4``
        """  # noqa: E501
        return self._standard

    @property
    def state(self) -> LinktrainingState:
        """Return the ``LINKTRaining:STAte`` command.

        Description:
            - This DPO70000SX command sets or queries the state of the Link Training application on
              the DPO70000SX family of oscilloscopes. The default argument value is OFF. To use the
              Link Training application, the State argument must first be set to ON. At a minimum,
              to capture the Link Training data into a Results Table, the
              ``LINKTRaining:ARMscope ON`` command also must be issued after the Link Training State
              is ON. Once the State is ON and the ARMscope is ON, the Link Training Results Table
              data will be captured when Link Training is initiated on the DUT. Initiating Link
              Training on the DUT is a DUT-dependent operation that is usually accomplished by a
              (serial or other bus) command to the DUT to power-up the Lane under test. Sometimes,
              it can be as simple as un-plugging and re-plugging the signal connector for the lane.
              To summarize, the minimum sequence of events to capture 100G Ethernet KR4 from Default
              Setup is ``:LINKTRaining:STATE ON`` ``:LINKTRaining:ARMscope ON`` Initiate Link
              Training on the Lane under test on the DUT. The Results Table and Waveforms are
              captured on the scope. Link Training is only available on the DPO70000SX
              oscilloscopes.

        Usage:
            - Using the ``.query()`` method will send the ``LINKTRaining:STAte?`` query.
            - Using the ``.verify(value)`` method will send the ``LINKTRaining:STAte?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LINKTRaining:STAte value`` command.

        SCPI Syntax:
            ```
            - LINKTRaining:STAte <OFF | ON>
            - LINKTRaining:STAte?
            ```

        Info:
            - ``OFF`` sets Link Training State to OFF.
            - ``ON`` sets Link Training State to ON.
        """
        return self._state

    @property
    def triggeron(self) -> LinktrainingTriggeron:
        r"""Return the ``LINKTRaining:TRIGgeron`` command.

        Description:
            - This DPO70000SX command sets or queries the TriggerOn setting of the Link Training
              application. The default argument value is ``ALL_FRAMES``, which attempts to trigger
              the scope whenever any Frame Control Channel contains new (changed) data values to
              capture FastFrame record waveforms. When the TriggerOn argument is ``FIRST_FRAME`` or
              ``LAST_FRAME``, a single record waveform is captured, and the user may select the
              record length and horizontal position, among other settings, for this waveform. When
              the TriggerOn argument is ``ALL_FRAMES``, FastFrame records are captured containing
              the decoded and marked Control Channel information. The user may select the FastFrame
              Length and maximum number of Frames (< 512 at this writing). Note that the Results
              Table captures all of the Control Channel data on both scope channels of a given lane,
              no matter what the TriggerOn argument value is chosen, because the data is captured by
              hardware in real-time ('100% live'). This means that the data in the Results Table is
              derived directly from the signal, not from the digitized waveform (that would be
              decoding, and we do that where possible). However, only some of the Control Channel
              values in the Results Table will be backed with Waveforms on the display, because the
              Frames may arrive faster than the Acquisition System can capture and store the
              FastFrame waveforms, or because the Link Training process takes more time, up to
              500ms, than can be captured in a single long record at any reasonable sample rate.
              When rows in the Results Table are not backed by an acquired waveform on the display,
              three asterisks (\*\*\*) are shown in the Frame column. Remember, all of the Control
              Channel data is captured in the Results Table for all three Triggeron settings. So,
              you should rely on the data in the Results Table, using the waveform decoding as
              confirmation. Don't forget that you can use cursor-gated DPOJET measurements to
              analyze the marked waveforms that are captured. The cursor positioning is made easier
              if you set the Link Training Marks to be TRAining to delineate the PRBS Training Data
              section of the Frames. Then you can use the extents of the MARK to better position the
              cursors for the measurements. Link Training is only available on the DPO70000SX family
              of oscilloscopes.

        Usage:
            - Using the ``.write(value)`` method will send the ``LINKTRaining:TRIGgeron value``
              command.

        SCPI Syntax:
            ```
            - LINKTRaining:TRIGgeron <FIRst_frame | LASt_frame | ALL_frames>
            ```

        Info:
            - ``FIRst_frame`` sets Link Training TRIGgeron to ``FIRst_frame``.
            - ``LASt_frame`` sets Link Training TRIGgeron to ``LASt_frame``.
            - ``ALL_frames`` sets Link Training TRIGgeron to ``ALL_frames``.
        """
        return self._triggeron
