"""The email commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - EMAIL:SETUp:FROMADDRess <QString>
    - EMAIL:SETUp:FROMADDRess?
    - EMAIL:SETUp:HOSTALIASNAMe <QString>
    - EMAIL:SETUp:HOSTALIASNAMe?
    - EMAIL:SETUp:SMTPLOGIn <QString>
    - EMAIL:SETUp:SMTPLOGIn?
    - EMAIL:SETUp:SMTPPASSWord <QString>
    - EMAIL:SETUp:SMTPPort <NR1>
    - EMAIL:SETUp:SMTPPort?
    - EMAIL:SETUp:SMTPServer <QString>
    - EMAIL:SETUp:SMTPServer?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class EmailSetupSmtpserver(SCPICmdWrite, SCPICmdRead):
    """The ``EMAIL:SETUp:SMTPServer`` command.

    Description:
        - Sets or returns the email SMTP server DNS name for the common server setup information
          that is shared between the Act on Event commands and the Hardcopy Email commands.

    Usage:
        - Using the ``.query()`` method will send the ``EMAIL:SETUp:SMTPServer?`` query.
        - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:SMTPServer?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:SMTPServer value`` command.

    SCPI Syntax:
        ```
        - EMAIL:SETUp:SMTPServer <QString>
        - EMAIL:SETUp:SMTPServer?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class EmailSetupSmtpport(SCPICmdWrite, SCPICmdRead):
    """The ``EMAIL:SETUp:SMTPPort`` command.

    Description:
        - Sets or returns the email SMTP server port number for the common server setup information
          that is shared between the Act on Event commands and the Hardcopy Email commands. The
          default port number is 25.

    Usage:
        - Using the ``.query()`` method will send the ``EMAIL:SETUp:SMTPPort?`` query.
        - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:SMTPPort?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:SMTPPort value`` command.

    SCPI Syntax:
        ```
        - EMAIL:SETUp:SMTPPort <NR1>
        - EMAIL:SETUp:SMTPPort?
        ```
    """


class EmailSetupSmtppassword(SCPICmdWrite):
    """The ``EMAIL:SETUp:SMTPPASSWord`` command.

    Description:
        - Sets the email SMTP server login password for the common server setup information that is
          shared between the Act on Event commands and the Hardcopy Email commands. For security
          reasons, no query form is provided.

    Usage:
        - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:SMTPPASSWord value``
          command.

    SCPI Syntax:
        ```
        - EMAIL:SETUp:SMTPPASSWord <QString>
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class EmailSetupSmtplogin(SCPICmdWrite, SCPICmdRead):
    """The ``EMAIL:SETUp:SMTPLOGIn`` command.

    Description:
        - Sets or returns the email SMTP server login ID for the common server setup information
          that is shared between the Act on Event commands and the Hardcopy Email commands.

    Usage:
        - Using the ``.query()`` method will send the ``EMAIL:SETUp:SMTPLOGIn?`` query.
        - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:SMTPLOGIn?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:SMTPLOGIn value`` command.

    SCPI Syntax:
        ```
        - EMAIL:SETUp:SMTPLOGIn <QString>
        - EMAIL:SETUp:SMTPLOGIn?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class EmailSetupHostaliasname(SCPICmdWrite, SCPICmdRead):
    """The ``EMAIL:SETUp:HOSTALIASNAMe`` command.

    Description:
        - Sets (or queries) the email host alias name for the common server setup information that
          is shared between the Act on Event commands and the Hardcopy Email commands. If this is an
          empty string, the DNS name of the instrument is used. This string is included in the email
          message.

    Usage:
        - Using the ``.query()`` method will send the ``EMAIL:SETUp:HOSTALIASNAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:HOSTALIASNAMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:HOSTALIASNAMe value``
          command.

    SCPI Syntax:
        ```
        - EMAIL:SETUp:HOSTALIASNAMe <QString>
        - EMAIL:SETUp:HOSTALIASNAMe?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class EmailSetupFromaddress(SCPICmdWrite, SCPICmdRead):
    """The ``EMAIL:SETUp:FROMADDRess`` command.

    Description:
        - Sets (or queries) the sender's email address for the common server setup information that
          is shared between the Act on Event commands and the Hardcopy Email commands. Note: to set
          the email recipient address for Act on Event commands, use
          ``ACTONEVENT:ACTION:EMAIL:SETUP:TOADDRESS``.

    Usage:
        - Using the ``.query()`` method will send the ``EMAIL:SETUp:FROMADDRess?`` query.
        - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:FROMADDRess?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:FROMADDRess value``
          command.

    SCPI Syntax:
        ```
        - EMAIL:SETUp:FROMADDRess <QString>
        - EMAIL:SETUp:FROMADDRess?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class EmailSetup(SCPICmdRead):
    """The ``EMAIL:SETUp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EMAIL:SETUp?`` query.
        - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fromaddress``: The ``EMAIL:SETUp:FROMADDRess`` command.
        - ``.hostaliasname``: The ``EMAIL:SETUp:HOSTALIASNAMe`` command.
        - ``.smtplogin``: The ``EMAIL:SETUp:SMTPLOGIn`` command.
        - ``.smtppassword``: The ``EMAIL:SETUp:SMTPPASSWord`` command.
        - ``.smtpport``: The ``EMAIL:SETUp:SMTPPort`` command.
        - ``.smtpserver``: The ``EMAIL:SETUp:SMTPServer`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fromaddress = EmailSetupFromaddress(device, f"{self._cmd_syntax}:FROMADDRess")
        self._hostaliasname = EmailSetupHostaliasname(device, f"{self._cmd_syntax}:HOSTALIASNAMe")
        self._smtplogin = EmailSetupSmtplogin(device, f"{self._cmd_syntax}:SMTPLOGIn")
        self._smtppassword = EmailSetupSmtppassword(device, f"{self._cmd_syntax}:SMTPPASSWord")
        self._smtpport = EmailSetupSmtpport(device, f"{self._cmd_syntax}:SMTPPort")
        self._smtpserver = EmailSetupSmtpserver(device, f"{self._cmd_syntax}:SMTPServer")

    @property
    def fromaddress(self) -> EmailSetupFromaddress:
        """Return the ``EMAIL:SETUp:FROMADDRess`` command.

        Description:
            - Sets (or queries) the sender's email address for the common server setup information
              that is shared between the Act on Event commands and the Hardcopy Email commands.
              Note: to set the email recipient address for Act on Event commands, use
              ``ACTONEVENT:ACTION:EMAIL:SETUP:TOADDRESS``.

        Usage:
            - Using the ``.query()`` method will send the ``EMAIL:SETUp:FROMADDRess?`` query.
            - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:FROMADDRess?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:FROMADDRess value``
              command.

        SCPI Syntax:
            ```
            - EMAIL:SETUp:FROMADDRess <QString>
            - EMAIL:SETUp:FROMADDRess?
            ```
        """
        return self._fromaddress

    @property
    def hostaliasname(self) -> EmailSetupHostaliasname:
        """Return the ``EMAIL:SETUp:HOSTALIASNAMe`` command.

        Description:
            - Sets (or queries) the email host alias name for the common server setup information
              that is shared between the Act on Event commands and the Hardcopy Email commands. If
              this is an empty string, the DNS name of the instrument is used. This string is
              included in the email message.

        Usage:
            - Using the ``.query()`` method will send the ``EMAIL:SETUp:HOSTALIASNAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:HOSTALIASNAMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:HOSTALIASNAMe value``
              command.

        SCPI Syntax:
            ```
            - EMAIL:SETUp:HOSTALIASNAMe <QString>
            - EMAIL:SETUp:HOSTALIASNAMe?
            ```
        """
        return self._hostaliasname

    @property
    def smtplogin(self) -> EmailSetupSmtplogin:
        """Return the ``EMAIL:SETUp:SMTPLOGIn`` command.

        Description:
            - Sets or returns the email SMTP server login ID for the common server setup information
              that is shared between the Act on Event commands and the Hardcopy Email commands.

        Usage:
            - Using the ``.query()`` method will send the ``EMAIL:SETUp:SMTPLOGIn?`` query.
            - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:SMTPLOGIn?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:SMTPLOGIn value``
              command.

        SCPI Syntax:
            ```
            - EMAIL:SETUp:SMTPLOGIn <QString>
            - EMAIL:SETUp:SMTPLOGIn?
            ```
        """
        return self._smtplogin

    @property
    def smtppassword(self) -> EmailSetupSmtppassword:
        """Return the ``EMAIL:SETUp:SMTPPASSWord`` command.

        Description:
            - Sets the email SMTP server login password for the common server setup information that
              is shared between the Act on Event commands and the Hardcopy Email commands. For
              security reasons, no query form is provided.

        Usage:
            - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:SMTPPASSWord value``
              command.

        SCPI Syntax:
            ```
            - EMAIL:SETUp:SMTPPASSWord <QString>
            ```
        """
        return self._smtppassword

    @property
    def smtpport(self) -> EmailSetupSmtpport:
        """Return the ``EMAIL:SETUp:SMTPPort`` command.

        Description:
            - Sets or returns the email SMTP server port number for the common server setup
              information that is shared between the Act on Event commands and the Hardcopy Email
              commands. The default port number is 25.

        Usage:
            - Using the ``.query()`` method will send the ``EMAIL:SETUp:SMTPPort?`` query.
            - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:SMTPPort?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:SMTPPort value``
              command.

        SCPI Syntax:
            ```
            - EMAIL:SETUp:SMTPPort <NR1>
            - EMAIL:SETUp:SMTPPort?
            ```
        """
        return self._smtpport

    @property
    def smtpserver(self) -> EmailSetupSmtpserver:
        """Return the ``EMAIL:SETUp:SMTPServer`` command.

        Description:
            - Sets or returns the email SMTP server DNS name for the common server setup information
              that is shared between the Act on Event commands and the Hardcopy Email commands.

        Usage:
            - Using the ``.query()`` method will send the ``EMAIL:SETUp:SMTPServer?`` query.
            - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp:SMTPServer?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EMAIL:SETUp:SMTPServer value``
              command.

        SCPI Syntax:
            ```
            - EMAIL:SETUp:SMTPServer <QString>
            - EMAIL:SETUp:SMTPServer?
            ```
        """
        return self._smtpserver


class Email(SCPICmdRead):
    """The ``EMAIL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``EMAIL?`` query.
        - Using the ``.verify(value)`` method will send the ``EMAIL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.setup``: The ``EMAIL:SETUp`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "EMAIL") -> None:
        super().__init__(device, cmd_syntax)
        self._setup = EmailSetup(device, f"{self._cmd_syntax}:SETUp")

    @property
    def setup(self) -> EmailSetup:
        """Return the ``EMAIL:SETUp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``EMAIL:SETUp?`` query.
            - Using the ``.verify(value)`` method will send the ``EMAIL:SETUp?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fromaddress``: The ``EMAIL:SETUp:FROMADDRess`` command.
            - ``.hostaliasname``: The ``EMAIL:SETUp:HOSTALIASNAMe`` command.
            - ``.smtplogin``: The ``EMAIL:SETUp:SMTPLOGIn`` command.
            - ``.smtppassword``: The ``EMAIL:SETUp:SMTPPASSWord`` command.
            - ``.smtpport``: The ``EMAIL:SETUp:SMTPPort`` command.
            - ``.smtpserver``: The ``EMAIL:SETUp:SMTPServer`` command.
        """
        return self._setup
