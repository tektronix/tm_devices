"""The email commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - EMail {TESt|RESET}
    - EMail:ATTempts <NR1>
    - EMail:ATTempts?
    - EMail:AUTHLogin {<QString>}
    - EMail:AUTHLogin?
    - EMail:AUTHPassword {<QString>}
    - EMail:COUNt?
    - EMail:FROm {<QString>}
    - EMail:FROm?
    - EMail:HOSTwanted {<QString>}
    - EMail:HOSTwanted?
    - EMail:IMAGe {<NR1>|ON|OFF|}
    - EMail:IMAGe?
    - EMail:LIMit {ON|OFF|<NR1>}
    - EMail:LIMit?
    - EMail:MASK {ON|OFF|<NR1>}
    - EMail:MASK?
    - EMail:MAXSize {<NR1>}
    - EMail:MAXSize?
    - EMail:MEASUrement {ON|OFF|<NR1>}
    - EMail:MEASUrement?
    - EMail:NUMEMails {<NR1>}
    - EMail:NUMEMails?
    - EMail:SMTPPort {<NR1>}
    - EMail:SMTPPort?
    - EMail:SMTPServer <QString>
    - EMail:SMTPServer?
    - EMail:STATUS?
    - EMail:TIMEOut <NR1>
    - EMail:TIMEOut?
    - EMail:TO <QString>
    - EMail:TO?
    - EMail:TRIGger {ON|OFF|<NR1>}
    - EMail:TRIGger?
    - EMail:WAVEform {ON|OFF|<NR1>}
    - EMail:WAVEform?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class EmailWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:WAVEform`` command.

    Description:
        - This command sets or queries whether waveform data is included in e-mail. The waveforms to
          be included, the start and stop points (and, or, frames for Fast Frame mode), and the data
          formats are specified by the DATA and WFMOUTPRE commands within the Waveform Transfer
          Command group.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:WAVEform?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:WAVEform value`` command.

    SCPI Syntax:
        ```
        - EMail:WAVEform {ON|OFF|<NR1>}
        - EMail:WAVEform?
        ```

    Info:
        - ``<NR1>`` = 0 disables the inclusion of waveform data in the e-mail; any other value
          enables including waveform data in the e-mail.
        - ``ON`` enables the inclusion of waveform data in e-mail.
        - ``OFF`` disables the inclusion of waveform data in e-mail.
    """


class EmailTrigger(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:TRIGger`` command.

    Description:
        - This command sets or queries whether e-mail is sent when a trigger occurs. The e-mail is
          sent after the acquisition is complete.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:TRIGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:TRIGger value`` command.

    SCPI Syntax:
        ```
        - EMail:TRIGger {ON|OFF|<NR1>}
        - EMail:TRIGger?
        ```

    Info:
        - ``<NR1>`` = 0 disables sending e-mail when a trigger occurs; any other value enables
          sending e-mail when a trigger occurs.
        - ``ON`` argument enables sending e-mail when a trigger occurs.
        - ``OFF`` disables sending e-mail when a trigger occurs.
    """


class EmailTo(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:TO`` command.

    Description:
        - This command sets or queries the address of the recipient(s) of an e-mail.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:TO?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:TO?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:TO value`` command.

    SCPI Syntax:
        ```
        - EMail:TO <QString>
        - EMail:TO?
        ```

    Info:
        - ``<QString>`` argument is the e-mail address of the recipient (or recipients). Multiple
          addresses are separated with semicolons (;). For example,
          'johndoe@tek.com;billsmith@tek.com' specifies that both johndoe and billsmith at tek.com
          will receive e-mail when the event occurs. The length of this string is limited to 252
          characters.
    """

    _WRAP_ARG_WITH_QUOTES = True


class EmailTimeout(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:TIMEOut`` command.

    Description:
        - This command sets or queries the global timeout in seconds. The default is 30 seconds. You
          use this timeout for socket connections and might need to change it from the default on
          some networks.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:TIMEOut?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:TIMEOut?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:TIMEOut value`` command.

    SCPI Syntax:
        ```
        - EMail:TIMEOut <NR1>
        - EMail:TIMEOut?
        ```

    Info:
        - ``<NR1>`` argument is the global timeout in seconds. The value for NR1 can be 0 through
          500.
    """


class EmailStatus(SCPICmdRead):
    """The ``EMail:STATUS`` command.

    Description:
        - This query only command returns the status of the last e-mail you attempted to send.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:STATUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - EMail:STATUS?
        ```
    """


class EmailSmtpserver(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:SMTPServer`` command.

    Description:
        - This command sets or queries the address of the SMTP mail server.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:SMTPServer?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:SMTPServer?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:SMTPServer value`` command.

    SCPI Syntax:
        ```
        - EMail:SMTPServer <QString>
        - EMail:SMTPServer?
        ```

    Info:
        - ``<QString>`` argument is the address of the SMTP mail server that will handle the mail
          service request. For example, 'smtp.tek.com'.
    """

    _WRAP_ARG_WITH_QUOTES = True


class EmailSmtpport(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:SMTPPort`` command.

    Description:
        - This command sets or queries the SMTP port number that the e-mail server uses if other
          than the default of 25.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:SMTPPort?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:SMTPPort?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:SMTPPort value`` command.

    SCPI Syntax:
        ```
        - EMail:SMTPPort {<NR1>}
        - EMail:SMTPPort?
        ```

    Info:
        - ``<NR1>`` can be 1 through 65535. This number specifies the TCPIP port number.
    """


class EmailNumemails(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:NUMEMails`` command.

    Description:
        - This command sets or queries the number of e-mails you can send when Email on Event is
          armed, from 1 to 50. This limit is to restrict e-mail floods.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:NUMEMails?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:NUMEMails?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:NUMEMails value`` command.

    SCPI Syntax:
        ```
        - EMail:NUMEMails {<NR1>}
        - EMail:NUMEMails?
        ```

    Info:
        - ``<NR1>`` can be 1 through 50. This is the number of e-mails you can send before the
          number of sent e-mails must be reset with the EMail RESet command.
    """


class EmailMeasurement(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:MEASUrement`` command.

    Description:
        - This command sets or queries whether measurement data is included as an attachment to
          e-mail. You must specify the saved measurement selection and the measurement format using
          the Email on Event setup menu. There are no remote commands for this purpose.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:MEASUrement?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:MEASUrement?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:MEASUrement value`` command.

    SCPI Syntax:
        ```
        - EMail:MEASUrement {ON|OFF|<NR1>}
        - EMail:MEASUrement?
        ```

    Info:
        - ``<NR1>`` = 0 disables the inclusion of measurement data in the e-mail; any other value
          enables including measurement data in the e-mail.
        - ``ON`` enables the inclusion of measurement data in e-mail.
        - ``OFF`` disables the inclusion of measurement data in e-mail.
    """


class EmailMaxsize(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:MAXSize`` command.

    Description:
        - This command sets or queries the maximum size (in megabytes) of e-mail that can be sent to
          the SMTP server.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:MAXSize?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:MAXSize?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:MAXSize value`` command.

    SCPI Syntax:
        ```
        - EMail:MAXSize {<NR1>}
        - EMail:MAXSize?
        ```

    Info:
        - ``<NR1>`` can be 0 through 2000 (megabytes). This is the maximum size of each e-mail that
          can be sent to the SMTP server.
    """


class EmailMask(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:MASK`` command.

    Description:
        - This command sets or queries whether e-mail is sent when a mask test failure occurs.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:MASK?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:MASK?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:MASK value`` command.

    SCPI Syntax:
        ```
        - EMail:MASK {ON|OFF|<NR1>}
        - EMail:MASK?
        ```

    Info:
        - ``<NR1>`` = 0 disables sending e-mail when a mask test failure occurs; any other value
          enables sending e-mail when a mask test failure occurs.
        - ``ON`` argument enables sending e-mail when a mask test failure occurs.
        - ``OFF`` disables sending e-mail when a mask test failure occurs.
    """


class EmailLimit(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:LIMit`` command.

    Description:
        - This command sets or queries whether e-mail is sent when a limit test failure occurs. This
          command is the same as the ``LIMit:EMail`` command.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:LIMit?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:LIMit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:LIMit value`` command.

    SCPI Syntax:
        ```
        - EMail:LIMit {ON|OFF|<NR1>}
        - EMail:LIMit?
        ```

    Info:
        - ``ON`` argument enables sending e-mail when a limit test failure occurs.
        - ``OFF`` disables sending e-mail when a limit test failure occurs.
        - ``<NR1>`` = 0 disables sending e-mail when a limit test failure occurs; any other value
          enables sending e-mail when a limit test failure occurs.
    """


class EmailImage(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:IMAGe`` command.

    Description:
        - This command sets or queries whether a screen image is included in e-mail. If this command
          is set to ON, the format and content of the screen image included is specified using the
          EXPort commands within the Hard Copy Command group.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:IMAGe?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:IMAGe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:IMAGe value`` command.

    SCPI Syntax:
        ```
        - EMail:IMAGe {<NR1>|ON|OFF|}
        - EMail:IMAGe?
        ```

    Info:
        - ``<NR1>`` = 0 disables the inclusion of a screen image in e-mail; any other value enables
          the inclusion of a screen image in e-mail.
        - ``ON`` argument enables the inclusion of a screen image in e-mail.
        - ``OFF`` argument disables the inclusion of a screen image in e-mail.
    """


class EmailHostwanted(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:HOSTwanted`` command.

    Description:
        - This command sets or queries the host name that will be used when e-mail is sent to the
          SMTP e-mail server if the DPO host name will not work.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:HOSTwanted?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:HOSTwanted?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:HOSTwanted value`` command.

    SCPI Syntax:
        ```
        - EMail:HOSTwanted {<QString>}
        - EMail:HOSTwanted?
        ```

    Info:
        - ``<QString>`` argument is a string that specifies the host name to be used with the SMTP
          e-mail server if the default DPO host name will not work.
    """


class EmailFrom(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:FROm`` command.

    Description:
        - This command sets or queries the From line in the e-mail. The default for the From line is
          the instrument model and serial number.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:FROm?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:FROm?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:FROm value`` command.

    SCPI Syntax:
        ```
        - EMail:FROm {<QString>}
        - EMail:FROm?
        ```

    Info:
        - ``<QString>`` argument is a string that is placed in the From line of the e-mail. An
          example is 'johnz'.
    """


class EmailCount(SCPICmdRead):
    """The ``EMail:COUNt`` command.

    Description:
        - This query only command returns the number of e-mails that have been sent since Email on
          Event was armed. The range of values returned can be from 0 to 50.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:COUNt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - EMail:COUNt?
        ```
    """


class EmailAuthpassword(SCPICmdWrite):
    """The ``EMail:AUTHPassword`` command.

    Description:
        - This command (no query form) sets the password that will be used if the SMTP e-mail server
          requires one for authentication.

    Usage:
        - Using the ``.write(value)`` method will send the ``EMail:AUTHPassword value`` command.

    SCPI Syntax:
        ```
        - EMail:AUTHPassword {<QString>}
        ```

    Info:
        - ``<QString>`` argument is a string that specifies the password to be used with the SMTP
          e-mail server.
    """


class EmailAuthlogin(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:AUTHLogin`` command.

    Description:
        - This command sets or queries the login name that will be used if the SMTP e-mail server
          requires one for authentication.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:AUTHLogin?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:AUTHLogin?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:AUTHLogin value`` command.

    SCPI Syntax:
        ```
        - EMail:AUTHLogin {<QString>}
        - EMail:AUTHLogin?
        ```

    Info:
        - ``<QString>`` argument is a string that specifies the login name to be used with the SMTP
          e-mail server.
    """


class EmailAttempts(SCPICmdWrite, SCPICmdRead):
    """The ``EMail:ATTempts`` command.

    Description:
        - This command sets or queries the number of times that an attempt will be made to send
          e-mail to the SMTP e-mail server. The default is 1.

    Usage:
        - Using the ``.query()`` method will send the ``EMail:ATTempts?`` query.
        - Using the ``.verify(value)`` method will send the ``EMail:ATTempts?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMail:ATTempts value`` command.

    SCPI Syntax:
        ```
        - EMail:ATTempts <NR1>
        - EMail:ATTempts?
        ```

    Info:
        - ``<NR1>`` can be 1 through 20. This number is the specified number of attempts that will
          be made to send e-mail to the SMTP server.
    """


#  pylint: disable=too-many-instance-attributes
class Email(SCPICmdWrite, SCPICmdRead):
    """The ``EMail`` command.

    Description:
        - This command (no query form) sends a test e-mail message or sets the current e-mail sent
          count to zero.

    Usage:
        - Using the ``.write(value)`` method will send the ``EMail value`` command.

    SCPI Syntax:
        ```
        - EMail {TESt|RESET}
        ```

    Info:
        - ``TESt`` argument sends a test e-mail message.
        - ``RESET`` argument sets the e-mail sent count to zero.

    Properties:
        - ``.attempts``: The ``EMail:ATTempts`` command.
        - ``.authlogin``: The ``EMail:AUTHLogin`` command.
        - ``.authpassword``: The ``EMail:AUTHPassword`` command.
        - ``.count``: The ``EMail:COUNt`` command.
        - ``.from``: The ``EMail:FROm`` command.
        - ``.hostwanted``: The ``EMail:HOSTwanted`` command.
        - ``.image``: The ``EMail:IMAGe`` command.
        - ``.limit``: The ``EMail:LIMit`` command.
        - ``.mask``: The ``EMail:MASK`` command.
        - ``.maxsize``: The ``EMail:MAXSize`` command.
        - ``.measurement``: The ``EMail:MEASUrement`` command.
        - ``.numemails``: The ``EMail:NUMEMails`` command.
        - ``.smtpport``: The ``EMail:SMTPPort`` command.
        - ``.smtpserver``: The ``EMail:SMTPServer`` command.
        - ``.status``: The ``EMail:STATUS`` command.
        - ``.timeout``: The ``EMail:TIMEOut`` command.
        - ``.to``: The ``EMail:TO`` command.
        - ``.trigger``: The ``EMail:TRIGger`` command.
        - ``.waveform``: The ``EMail:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "EMail") -> None:
        super().__init__(device, cmd_syntax)
        self._attempts = EmailAttempts(device, f"{self._cmd_syntax}:ATTempts")
        self._authlogin = EmailAuthlogin(device, f"{self._cmd_syntax}:AUTHLogin")
        self._authpassword = EmailAuthpassword(device, f"{self._cmd_syntax}:AUTHPassword")
        self._count = EmailCount(device, f"{self._cmd_syntax}:COUNt")
        self._from = EmailFrom(device, f"{self._cmd_syntax}:FROm")
        self._hostwanted = EmailHostwanted(device, f"{self._cmd_syntax}:HOSTwanted")
        self._image = EmailImage(device, f"{self._cmd_syntax}:IMAGe")
        self._limit = EmailLimit(device, f"{self._cmd_syntax}:LIMit")
        self._mask = EmailMask(device, f"{self._cmd_syntax}:MASK")
        self._maxsize = EmailMaxsize(device, f"{self._cmd_syntax}:MAXSize")
        self._measurement = EmailMeasurement(device, f"{self._cmd_syntax}:MEASUrement")
        self._numemails = EmailNumemails(device, f"{self._cmd_syntax}:NUMEMails")
        self._smtpport = EmailSmtpport(device, f"{self._cmd_syntax}:SMTPPort")
        self._smtpserver = EmailSmtpserver(device, f"{self._cmd_syntax}:SMTPServer")
        self._status = EmailStatus(device, f"{self._cmd_syntax}:STATUS")
        self._timeout = EmailTimeout(device, f"{self._cmd_syntax}:TIMEOut")
        self._to = EmailTo(device, f"{self._cmd_syntax}:TO")
        self._trigger = EmailTrigger(device, f"{self._cmd_syntax}:TRIGger")
        self._waveform = EmailWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def attempts(self) -> EmailAttempts:
        """Return the ``EMail:ATTempts`` command.

        Description:
            - This command sets or queries the number of times that an attempt will be made to send
              e-mail to the SMTP e-mail server. The default is 1.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:ATTempts?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:ATTempts?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:ATTempts value`` command.

        SCPI Syntax:
            ```
            - EMail:ATTempts <NR1>
            - EMail:ATTempts?
            ```

        Info:
            - ``<NR1>`` can be 1 through 20. This number is the specified number of attempts that
              will be made to send e-mail to the SMTP server.
        """
        return self._attempts

    @property
    def authlogin(self) -> EmailAuthlogin:
        """Return the ``EMail:AUTHLogin`` command.

        Description:
            - This command sets or queries the login name that will be used if the SMTP e-mail
              server requires one for authentication.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:AUTHLogin?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:AUTHLogin?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:AUTHLogin value`` command.

        SCPI Syntax:
            ```
            - EMail:AUTHLogin {<QString>}
            - EMail:AUTHLogin?
            ```

        Info:
            - ``<QString>`` argument is a string that specifies the login name to be used with the
              SMTP e-mail server.
        """
        return self._authlogin

    @property
    def authpassword(self) -> EmailAuthpassword:
        """Return the ``EMail:AUTHPassword`` command.

        Description:
            - This command (no query form) sets the password that will be used if the SMTP e-mail
              server requires one for authentication.

        Usage:
            - Using the ``.write(value)`` method will send the ``EMail:AUTHPassword value`` command.

        SCPI Syntax:
            ```
            - EMail:AUTHPassword {<QString>}
            ```

        Info:
            - ``<QString>`` argument is a string that specifies the password to be used with the
              SMTP e-mail server.
        """
        return self._authpassword

    @property
    def count(self) -> EmailCount:
        """Return the ``EMail:COUNt`` command.

        Description:
            - This query only command returns the number of e-mails that have been sent since Email
              on Event was armed. The range of values returned can be from 0 to 50.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:COUNt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EMail:COUNt?
            ```
        """
        return self._count

    @property
    def from_(self) -> EmailFrom:
        """Return the ``EMail:FROm`` command.

        Description:
            - This command sets or queries the From line in the e-mail. The default for the From
              line is the instrument model and serial number.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:FROm?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:FROm?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:FROm value`` command.

        SCPI Syntax:
            ```
            - EMail:FROm {<QString>}
            - EMail:FROm?
            ```

        Info:
            - ``<QString>`` argument is a string that is placed in the From line of the e-mail. An
              example is 'johnz'.
        """
        return self._from

    @property
    def hostwanted(self) -> EmailHostwanted:
        """Return the ``EMail:HOSTwanted`` command.

        Description:
            - This command sets or queries the host name that will be used when e-mail is sent to
              the SMTP e-mail server if the DPO host name will not work.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:HOSTwanted?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:HOSTwanted?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:HOSTwanted value`` command.

        SCPI Syntax:
            ```
            - EMail:HOSTwanted {<QString>}
            - EMail:HOSTwanted?
            ```

        Info:
            - ``<QString>`` argument is a string that specifies the host name to be used with the
              SMTP e-mail server if the default DPO host name will not work.
        """
        return self._hostwanted

    @property
    def image(self) -> EmailImage:
        """Return the ``EMail:IMAGe`` command.

        Description:
            - This command sets or queries whether a screen image is included in e-mail. If this
              command is set to ON, the format and content of the screen image included is specified
              using the EXPort commands within the Hard Copy Command group.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:IMAGe?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:IMAGe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:IMAGe value`` command.

        SCPI Syntax:
            ```
            - EMail:IMAGe {<NR1>|ON|OFF|}
            - EMail:IMAGe?
            ```

        Info:
            - ``<NR1>`` = 0 disables the inclusion of a screen image in e-mail; any other value
              enables the inclusion of a screen image in e-mail.
            - ``ON`` argument enables the inclusion of a screen image in e-mail.
            - ``OFF`` argument disables the inclusion of a screen image in e-mail.
        """
        return self._image

    @property
    def limit(self) -> EmailLimit:
        """Return the ``EMail:LIMit`` command.

        Description:
            - This command sets or queries whether e-mail is sent when a limit test failure occurs.
              This command is the same as the ``LIMit:EMail`` command.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:LIMit?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:LIMit?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:LIMit value`` command.

        SCPI Syntax:
            ```
            - EMail:LIMit {ON|OFF|<NR1>}
            - EMail:LIMit?
            ```

        Info:
            - ``ON`` argument enables sending e-mail when a limit test failure occurs.
            - ``OFF`` disables sending e-mail when a limit test failure occurs.
            - ``<NR1>`` = 0 disables sending e-mail when a limit test failure occurs; any other
              value enables sending e-mail when a limit test failure occurs.
        """
        return self._limit

    @property
    def mask(self) -> EmailMask:
        """Return the ``EMail:MASK`` command.

        Description:
            - This command sets or queries whether e-mail is sent when a mask test failure occurs.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:MASK?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:MASK?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:MASK value`` command.

        SCPI Syntax:
            ```
            - EMail:MASK {ON|OFF|<NR1>}
            - EMail:MASK?
            ```

        Info:
            - ``<NR1>`` = 0 disables sending e-mail when a mask test failure occurs; any other value
              enables sending e-mail when a mask test failure occurs.
            - ``ON`` argument enables sending e-mail when a mask test failure occurs.
            - ``OFF`` disables sending e-mail when a mask test failure occurs.
        """
        return self._mask

    @property
    def maxsize(self) -> EmailMaxsize:
        """Return the ``EMail:MAXSize`` command.

        Description:
            - This command sets or queries the maximum size (in megabytes) of e-mail that can be
              sent to the SMTP server.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:MAXSize?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:MAXSize?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:MAXSize value`` command.

        SCPI Syntax:
            ```
            - EMail:MAXSize {<NR1>}
            - EMail:MAXSize?
            ```

        Info:
            - ``<NR1>`` can be 0 through 2000 (megabytes). This is the maximum size of each e-mail
              that can be sent to the SMTP server.
        """
        return self._maxsize

    @property
    def measurement(self) -> EmailMeasurement:
        """Return the ``EMail:MEASUrement`` command.

        Description:
            - This command sets or queries whether measurement data is included as an attachment to
              e-mail. You must specify the saved measurement selection and the measurement format
              using the Email on Event setup menu. There are no remote commands for this purpose.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:MEASUrement?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:MEASUrement?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:MEASUrement value`` command.

        SCPI Syntax:
            ```
            - EMail:MEASUrement {ON|OFF|<NR1>}
            - EMail:MEASUrement?
            ```

        Info:
            - ``<NR1>`` = 0 disables the inclusion of measurement data in the e-mail; any other
              value enables including measurement data in the e-mail.
            - ``ON`` enables the inclusion of measurement data in e-mail.
            - ``OFF`` disables the inclusion of measurement data in e-mail.
        """
        return self._measurement

    @property
    def numemails(self) -> EmailNumemails:
        """Return the ``EMail:NUMEMails`` command.

        Description:
            - This command sets or queries the number of e-mails you can send when Email on Event is
              armed, from 1 to 50. This limit is to restrict e-mail floods.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:NUMEMails?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:NUMEMails?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:NUMEMails value`` command.

        SCPI Syntax:
            ```
            - EMail:NUMEMails {<NR1>}
            - EMail:NUMEMails?
            ```

        Info:
            - ``<NR1>`` can be 1 through 50. This is the number of e-mails you can send before the
              number of sent e-mails must be reset with the EMail RESet command.
        """
        return self._numemails

    @property
    def smtpport(self) -> EmailSmtpport:
        """Return the ``EMail:SMTPPort`` command.

        Description:
            - This command sets or queries the SMTP port number that the e-mail server uses if other
              than the default of 25.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:SMTPPort?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:SMTPPort?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:SMTPPort value`` command.

        SCPI Syntax:
            ```
            - EMail:SMTPPort {<NR1>}
            - EMail:SMTPPort?
            ```

        Info:
            - ``<NR1>`` can be 1 through 65535. This number specifies the TCPIP port number.
        """
        return self._smtpport

    @property
    def smtpserver(self) -> EmailSmtpserver:
        """Return the ``EMail:SMTPServer`` command.

        Description:
            - This command sets or queries the address of the SMTP mail server.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:SMTPServer?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:SMTPServer?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:SMTPServer value`` command.

        SCPI Syntax:
            ```
            - EMail:SMTPServer <QString>
            - EMail:SMTPServer?
            ```

        Info:
            - ``<QString>`` argument is the address of the SMTP mail server that will handle the
              mail service request. For example, 'smtp.tek.com'.
        """
        return self._smtpserver

    @property
    def status(self) -> EmailStatus:
        """Return the ``EMail:STATUS`` command.

        Description:
            - This query only command returns the status of the last e-mail you attempted to send.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:STATUS?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:STATUS?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EMail:STATUS?
            ```
        """
        return self._status

    @property
    def timeout(self) -> EmailTimeout:
        """Return the ``EMail:TIMEOut`` command.

        Description:
            - This command sets or queries the global timeout in seconds. The default is 30 seconds.
              You use this timeout for socket connections and might need to change it from the
              default on some networks.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:TIMEOut?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:TIMEOut?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:TIMEOut value`` command.

        SCPI Syntax:
            ```
            - EMail:TIMEOut <NR1>
            - EMail:TIMEOut?
            ```

        Info:
            - ``<NR1>`` argument is the global timeout in seconds. The value for NR1 can be 0
              through 500.
        """
        return self._timeout

    @property
    def to(self) -> EmailTo:
        """Return the ``EMail:TO`` command.

        Description:
            - This command sets or queries the address of the recipient(s) of an e-mail.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:TO?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:TO?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:TO value`` command.

        SCPI Syntax:
            ```
            - EMail:TO <QString>
            - EMail:TO?
            ```

        Info:
            - ``<QString>`` argument is the e-mail address of the recipient (or recipients).
              Multiple addresses are separated with semicolons (;). For example,
              'johndoe@tek.com;billsmith@tek.com' specifies that both johndoe and billsmith at
              tek.com will receive e-mail when the event occurs. The length of this string is
              limited to 252 characters.
        """
        return self._to

    @property
    def trigger(self) -> EmailTrigger:
        """Return the ``EMail:TRIGger`` command.

        Description:
            - This command sets or queries whether e-mail is sent when a trigger occurs. The e-mail
              is sent after the acquisition is complete.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:TRIGger?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:TRIGger value`` command.

        SCPI Syntax:
            ```
            - EMail:TRIGger {ON|OFF|<NR1>}
            - EMail:TRIGger?
            ```

        Info:
            - ``<NR1>`` = 0 disables sending e-mail when a trigger occurs; any other value enables
              sending e-mail when a trigger occurs.
            - ``ON`` argument enables sending e-mail when a trigger occurs.
            - ``OFF`` disables sending e-mail when a trigger occurs.
        """
        return self._trigger

    @property
    def waveform(self) -> EmailWaveform:
        """Return the ``EMail:WAVEform`` command.

        Description:
            - This command sets or queries whether waveform data is included in e-mail. The
              waveforms to be included, the start and stop points (and, or, frames for Fast Frame
              mode), and the data formats are specified by the DATA and WFMOUTPRE commands within
              the Waveform Transfer Command group.

        Usage:
            - Using the ``.query()`` method will send the ``EMail:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``EMail:WAVEform?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMail:WAVEform value`` command.

        SCPI Syntax:
            ```
            - EMail:WAVEform {ON|OFF|<NR1>}
            - EMail:WAVEform?
            ```

        Info:
            - ``<NR1>`` = 0 disables the inclusion of waveform data in the e-mail; any other value
              enables including waveform data in the e-mail.
            - ``ON`` enables the inclusion of waveform data in e-mail.
            - ``OFF`` disables the inclusion of waveform data in e-mail.
        """
        return self._waveform
