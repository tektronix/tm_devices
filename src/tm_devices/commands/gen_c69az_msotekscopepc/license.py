"""The license commands module.

These commands are used in the following models:
MSO2, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - LICense:APPID? {<QString>}
    - LICense:COUNt?
    - LICense:ERRor?
    - LICense:GMT?
    - LICense:HID?
    - LICense:INSTall <block_data>
    - LICense:ITEM? <NR1>
    - LICense:LIST?
    - LICense:VALidate? <QString>
    - LICense?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class LicenseValidate(SCPICmdReadWithArguments):
    """The ``LICense:VALidate`` command.

    Description:
        - This query accepts a license nomenclature as an argument and returns True (1) if that
          nomenclature is active and any required hardware is installed, or False (0) if either the
          nomenclature is not active or required hardware is not installed.

    Usage:
        - Using the ``.query(argument)`` method will send the ``LICense:VALidate? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``LICense:VALidate? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LICense:VALidate? <QString>
        ```

    Info:
        - ``<QString>`` is the license nomenclature.
    """


class LicenseList(SCPICmdRead):
    """The ``LICense:LIST`` command.

    Description:
        - This query returns the active license nomenclatures as a comma-separated list of strings.
          Duplicate nomenclatures, that is, the same license but with different expiration dates,
          are included.

    Usage:
        - Using the ``.query()`` method will send the ``LICense:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``LICense:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LICense:LIST?
        ```
    """


class LicenseItem(SCPICmdReadWithArguments):
    """The ``LICense:ITEM`` command.

    Description:
        - This query returns the details pertaining to a specific license. The NR1 argument is
          zero-indexed. If no argument is provided, zero is assumed.

    Usage:
        - Using the ``.query(argument)`` method will send the ``LICense:ITEM? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``LICense:ITEM? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LICense:ITEM? <NR1>
        ```
    """


class LicenseInstall(SCPICmdWrite):
    """The ``LICense:INSTall`` command.

    Description:
        - This command accepts a ``<block_data>`` license and installs it on the instrument.
          Restarting the instrument may be necessary to fully activate the additional capabilities.

    Usage:
        - Using the ``.write(value)`` method will send the ``LICense:INSTall value`` command.

    SCPI Syntax:
        ```
        - LICense:INSTall <block_data>
        ```

    Info:
        - ``<block_data>`` is the license in block data format.
    """


class LicenseHid(SCPICmdRead):
    """The ``LICense:HID`` command.

    Description:
        - This query returns the instrument HostID unique identifier.

    Usage:
        - Using the ``.query()`` method will send the ``LICense:HID?`` query.
        - Using the ``.verify(value)`` method will send the ``LICense:HID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LICense:HID?
        ```
    """


class LicenseGmt(SCPICmdRead):
    """The ``LICense:GMT`` command.

    Description:
        - This query returns the GMT time in ISO 8601 format, the local date, 24 hour time and
          time-zone offset.

    Usage:
        - Using the ``.query()`` method will send the ``LICense:GMT?`` query.
        - Using the ``.verify(value)`` method will send the ``LICense:GMT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LICense:GMT?
        ```
    """


class LicenseError(SCPICmdRead):
    """The ``LICense:ERRor`` command.

    Description:
        - This query-only command prompts the instrument to return all events and their messages
          (delimited by commas), and removes the returned events from the Event Queue. This command
          is an alias for ALLEV?.

    Usage:
        - Using the ``.query()`` method will send the ``LICense:ERRor?`` query.
        - Using the ``.verify(value)`` method will send the ``LICense:ERRor?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LICense:ERRor?
        ```
    """


class LicenseCount(SCPICmdRead):
    """The ``LICense:COUNt`` command.

    Description:
        - This query returns a count of the number of active licenses installed.

    Usage:
        - Using the ``.query()`` method will send the ``LICense:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``LICense:COUNt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LICense:COUNt?
        ```
    """


class LicenseAppid(SCPICmdReadWithArguments):
    """The ``LICense:APPID`` command.

    Description:
        - This query returns a comma-separated list of the active application IDs. If a string
          argument is provided, a '0' or '1' is returned, according to whether the string matches an
          active application ID.

    Usage:
        - Using the ``.query(argument)`` method will send the ``LICense:APPID? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``LICense:APPID? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LICense:APPID? {<QString>}
        ```
    """


#  pylint: disable=too-many-instance-attributes
class License(SCPICmdRead):
    """The ``LICense`` command.

    Description:
        - This query-only command returns all license parameters.

    Usage:
        - Using the ``.query()`` method will send the ``LICense?`` query.
        - Using the ``.verify(value)`` method will send the ``LICense?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - LICense?
        ```

    Properties:
        - ``.appid``: The ``LICense:APPID`` command.
        - ``.count``: The ``LICense:COUNt`` command.
        - ``.error``: The ``LICense:ERRor`` command.
        - ``.gmt``: The ``LICense:GMT`` command.
        - ``.hid``: The ``LICense:HID`` command.
        - ``.install``: The ``LICense:INSTall`` command.
        - ``.item``: The ``LICense:ITEM`` command.
        - ``.list``: The ``LICense:LIST`` command.
        - ``.validate``: The ``LICense:VALidate`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "LICense") -> None:
        super().__init__(device, cmd_syntax)
        self._appid = LicenseAppid(device, f"{self._cmd_syntax}:APPID")
        self._count = LicenseCount(device, f"{self._cmd_syntax}:COUNt")
        self._error = LicenseError(device, f"{self._cmd_syntax}:ERRor")
        self._gmt = LicenseGmt(device, f"{self._cmd_syntax}:GMT")
        self._hid = LicenseHid(device, f"{self._cmd_syntax}:HID")
        self._install = LicenseInstall(device, f"{self._cmd_syntax}:INSTall")
        self._item = LicenseItem(device, f"{self._cmd_syntax}:ITEM")
        self._list = LicenseList(device, f"{self._cmd_syntax}:LIST")
        self._validate = LicenseValidate(device, f"{self._cmd_syntax}:VALidate")

    @property
    def appid(self) -> LicenseAppid:
        """Return the ``LICense:APPID`` command.

        Description:
            - This query returns a comma-separated list of the active application IDs. If a string
              argument is provided, a '0' or '1' is returned, according to whether the string
              matches an active application ID.

        Usage:
            - Using the ``.query(argument)`` method will send the ``LICense:APPID? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``LICense:APPID? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.

        SCPI Syntax:
            ```
            - LICense:APPID? {<QString>}
            ```
        """
        return self._appid

    @property
    def count(self) -> LicenseCount:
        """Return the ``LICense:COUNt`` command.

        Description:
            - This query returns a count of the number of active licenses installed.

        Usage:
            - Using the ``.query()`` method will send the ``LICense:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``LICense:COUNt?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - LICense:COUNt?
            ```
        """
        return self._count

    @property
    def error(self) -> LicenseError:
        """Return the ``LICense:ERRor`` command.

        Description:
            - This query-only command prompts the instrument to return all events and their messages
              (delimited by commas), and removes the returned events from the Event Queue. This
              command is an alias for ALLEV?.

        Usage:
            - Using the ``.query()`` method will send the ``LICense:ERRor?`` query.
            - Using the ``.verify(value)`` method will send the ``LICense:ERRor?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - LICense:ERRor?
            ```
        """
        return self._error

    @property
    def gmt(self) -> LicenseGmt:
        """Return the ``LICense:GMT`` command.

        Description:
            - This query returns the GMT time in ISO 8601 format, the local date, 24 hour time and
              time-zone offset.

        Usage:
            - Using the ``.query()`` method will send the ``LICense:GMT?`` query.
            - Using the ``.verify(value)`` method will send the ``LICense:GMT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - LICense:GMT?
            ```
        """
        return self._gmt

    @property
    def hid(self) -> LicenseHid:
        """Return the ``LICense:HID`` command.

        Description:
            - This query returns the instrument HostID unique identifier.

        Usage:
            - Using the ``.query()`` method will send the ``LICense:HID?`` query.
            - Using the ``.verify(value)`` method will send the ``LICense:HID?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - LICense:HID?
            ```
        """
        return self._hid

    @property
    def install(self) -> LicenseInstall:
        """Return the ``LICense:INSTall`` command.

        Description:
            - This command accepts a ``<block_data>`` license and installs it on the instrument.
              Restarting the instrument may be necessary to fully activate the additional
              capabilities.

        Usage:
            - Using the ``.write(value)`` method will send the ``LICense:INSTall value`` command.

        SCPI Syntax:
            ```
            - LICense:INSTall <block_data>
            ```

        Info:
            - ``<block_data>`` is the license in block data format.
        """
        return self._install

    @property
    def item(self) -> LicenseItem:
        """Return the ``LICense:ITEM`` command.

        Description:
            - This query returns the details pertaining to a specific license. The NR1 argument is
              zero-indexed. If no argument is provided, zero is assumed.

        Usage:
            - Using the ``.query(argument)`` method will send the ``LICense:ITEM? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``LICense:ITEM? argument``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - LICense:ITEM? <NR1>
            ```
        """
        return self._item

    @property
    def list(self) -> LicenseList:
        """Return the ``LICense:LIST`` command.

        Description:
            - This query returns the active license nomenclatures as a comma-separated list of
              strings. Duplicate nomenclatures, that is, the same license but with different
              expiration dates, are included.

        Usage:
            - Using the ``.query()`` method will send the ``LICense:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``LICense:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - LICense:LIST?
            ```
        """
        return self._list

    @property
    def validate(self) -> LicenseValidate:
        """Return the ``LICense:VALidate`` command.

        Description:
            - This query accepts a license nomenclature as an argument and returns True (1) if that
              nomenclature is active and any required hardware is installed, or False (0) if either
              the nomenclature is not active or required hardware is not installed.

        Usage:
            - Using the ``.query(argument)`` method will send the ``LICense:VALidate? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``LICense:VALidate? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.

        SCPI Syntax:
            ```
            - LICense:VALidate? <QString>
            ```

        Info:
            - ``<QString>`` is the license nomenclature.
        """
        return self._validate
