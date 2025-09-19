"""The hardcopy commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HARDCopy {STARt}
    - HARDCopy:ACTIVeprinter {<NR1>|<name>}
    - HARDCopy:ACTIVeprinter?
    - HARDCopy:INKSaver?
    - HARDCopy:LAYout {PORTRait|LANdscape}
    - HARDCopy:LAYout?
    - HARDCopy:PREVIEW {ON|OFF|<NR1>}
    - HARDCopy:PRINTer:ADD <name>,<server>,<address>|<emailaddress>
    - HARDCopy:PRINTer:DELete <name>
    - HARDCopy:PRINTer:LIST?
    - HARDCopy:PRINTer:REName <name>,<new_name>,<new_server>,<new_address>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HardcopyPrinterRename(SCPICmdWrite):
    """The ``HARDCopy:PRINTer:REName`` command.

    Description:
        - Renames a network or email printer on the list of available printers, replacing the
          currently stored settings with the settings specified in the command. The first argument
          can be either the printer name, or the index from querying ``HARDCOPY:PRINTER:LIST``

    Usage:
        - Using the ``.write(value)`` method will send the ``HARDCopy:PRINTer:REName value``
          command.

    SCPI Syntax:
        ```
        - HARDCopy:PRINTer:REName <name>,<new_name>,<new_server>,<new_address>
        ```

    Info:
        - ``Network printer:``
        - ``<index>`` is the name of the printer to be renamed (deleted).
        - ``<name>`` is the name of the printer to be renamed (deleted).
        - ``<new_printer_name>`` is the new name for this printer.
        - ``<new_server_name>`` is the new print server for this printer.
        - ``<new_server_address>`` is the new IP address for the server.
        - ``Email printer:``
        - ``<index>`` is the index or name of the printer to be renamed.
        - ``<name>`` is the index or name of the printer to be renamed.
        - ``<new printer email address`` > is the new email address for this printer.
    """


class HardcopyPrinterList(SCPICmdRead):
    """The ``HARDCopy:PRINTer:LIST`` command.

    Description:
        - Displays the list of currently defined printers. The fields for each entry represent the
          printer number, whether the printer is currently active (Y=active, N=inactive), the
          printer name, the printer type (USB, Net or Email), print server name or IP address.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:PRINTer:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:PRINTer:LIST?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HARDCopy:PRINTer:LIST?
        ```
    """


class HardcopyPrinterDelete(SCPICmdWrite):
    """The ``HARDCopy:PRINTer:DELete`` command.

    Description:
        - Removes a network printer from the list of available printers. The printer name is case
          sensitive.

    Usage:
        - Using the ``.write(value)`` method will send the ``HARDCopy:PRINTer:DELete value``
          command.

    SCPI Syntax:
        ```
        - HARDCopy:PRINTer:DELete <name>
        ```

    Info:
        - ``<name>`` is the name of the printer to be deleted.
    """


class HardcopyPrinterAdd(SCPICmdWrite):
    """The ``HARDCopy:PRINTer:ADD`` command.

    Description:
        - This command is used to add a network or email printer to the list of available printers.
          Adding a network printer requires 3 arguments, but only one of server name or server IP
          address should be specified. An empty string can be used for blank arguments. Adding an
          email printer requires only one argument.

    Usage:
        - Using the ``.write(value)`` method will send the ``HARDCopy:PRINTer:ADD value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:PRINTer:ADD <name>,<server>,<address>|<emailaddress>
        ```

    Info:
        - ``Network printers:``
        - ``<name>`` is the name of the network printer queue.
        - ``<server>`` is the host name of the print (LPR) server.
        - ``<address>`` is the IP address of the print server.
        - ``Email printers:``
        - ``<emailaddress>`` is the internet email address of the printer. Must contain an @
          character.
    """


class HardcopyPrinter(SCPICmdRead):
    """The ``HARDCopy:PRINTer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:PRINTer?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:PRINTer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.add``: The ``HARDCopy:PRINTer:ADD`` command.
        - ``.delete``: The ``HARDCopy:PRINTer:DELete`` command.
        - ``.list``: The ``HARDCopy:PRINTer:LIST`` command.
        - ``.rename``: The ``HARDCopy:PRINTer:REName`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._add = HardcopyPrinterAdd(device, f"{self._cmd_syntax}:ADD")
        self._delete = HardcopyPrinterDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = HardcopyPrinterList(device, f"{self._cmd_syntax}:LIST")
        self._rename = HardcopyPrinterRename(device, f"{self._cmd_syntax}:REName")

    @property
    def add(self) -> HardcopyPrinterAdd:
        """Return the ``HARDCopy:PRINTer:ADD`` command.

        Description:
            - This command is used to add a network or email printer to the list of available
              printers. Adding a network printer requires 3 arguments, but only one of server name
              or server IP address should be specified. An empty string can be used for blank
              arguments. Adding an email printer requires only one argument.

        Usage:
            - Using the ``.write(value)`` method will send the ``HARDCopy:PRINTer:ADD value``
              command.

        SCPI Syntax:
            ```
            - HARDCopy:PRINTer:ADD <name>,<server>,<address>|<emailaddress>
            ```

        Info:
            - ``Network printers:``
            - ``<name>`` is the name of the network printer queue.
            - ``<server>`` is the host name of the print (LPR) server.
            - ``<address>`` is the IP address of the print server.
            - ``Email printers:``
            - ``<emailaddress>`` is the internet email address of the printer. Must contain an @
              character.
        """
        return self._add

    @property
    def delete(self) -> HardcopyPrinterDelete:
        """Return the ``HARDCopy:PRINTer:DELete`` command.

        Description:
            - Removes a network printer from the list of available printers. The printer name is
              case sensitive.

        Usage:
            - Using the ``.write(value)`` method will send the ``HARDCopy:PRINTer:DELete value``
              command.

        SCPI Syntax:
            ```
            - HARDCopy:PRINTer:DELete <name>
            ```

        Info:
            - ``<name>`` is the name of the printer to be deleted.
        """
        return self._delete

    @property
    def list(self) -> HardcopyPrinterList:
        """Return the ``HARDCopy:PRINTer:LIST`` command.

        Description:
            - Displays the list of currently defined printers. The fields for each entry represent
              the printer number, whether the printer is currently active (Y=active, N=inactive),
              the printer name, the printer type (USB, Net or Email), print server name or IP
              address.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:PRINTer:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:PRINTer:LIST?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HARDCopy:PRINTer:LIST?
            ```
        """
        return self._list

    @property
    def rename(self) -> HardcopyPrinterRename:
        """Return the ``HARDCopy:PRINTer:REName`` command.

        Description:
            - Renames a network or email printer on the list of available printers, replacing the
              currently stored settings with the settings specified in the command. The first
              argument can be either the printer name, or the index from querying
              ``HARDCOPY:PRINTER:LIST``

        Usage:
            - Using the ``.write(value)`` method will send the ``HARDCopy:PRINTer:REName value``
              command.

        SCPI Syntax:
            ```
            - HARDCopy:PRINTer:REName <name>,<new_name>,<new_server>,<new_address>
            ```

        Info:
            - ``Network printer:``
            - ``<index>`` is the name of the printer to be renamed (deleted).
            - ``<name>`` is the name of the printer to be renamed (deleted).
            - ``<new_printer_name>`` is the new name for this printer.
            - ``<new_server_name>`` is the new print server for this printer.
            - ``<new_server_address>`` is the new IP address for the server.
            - ``Email printer:``
            - ``<index>`` is the index or name of the printer to be renamed.
            - ``<name>`` is the index or name of the printer to be renamed.
            - ``<new printer email address`` > is the new email address for this printer.
        """
        return self._rename


class HardcopyPreview(SCPICmdWrite):
    """The ``HARDCopy:PREVIEW`` command.

    Description:
        - Displays a preview of the current screen contents with the InkSaver Palette if
          ``HARDCopy:INKSAVER`` is 1 or the Normal Palette if ``HARDCopy:INKSAVER`` is 0.

    Usage:
        - Using the ``.write(value)`` method will send the ``HARDCopy:PREVIEW value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:PREVIEW {ON|OFF|<NR1>}
        ```

    Info:
        - ``ON`` or <NR1> ≠ 0 turns preview mode on.
        - ``OFF`` or <NR1> = 0 turns preview mode off.
    """


class HardcopyLayout(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy:LAYout`` command.

    Description:
        - This command specifies the page orientation for hard copy. If you set the layout to
          LANdscape, the printer will print hard copies in landscape mode where the long edge of the
          screen will print to the long edge of the sheet of paper. If you set the layout to
          PORTRait, the printer will print hard copies in portrait mode. This command is not
          applicable for PictBridge hardcopies.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:LAYout?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:LAYout?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HARDCopy:LAYout value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:LAYout {PORTRait|LANdscape}
        - HARDCopy:LAYout?
        ```

    Info:
        - ``PORTRait`` orients the screen image vertically on the printed page.
        - ``LANdscape`` orients the screen image horizontally on the printed page.
    """


class HardcopyInksaver(SCPICmdRead):
    """The ``HARDCopy:INKSaver`` command.

    Description:
        - Changes hard copy output to print traces and graticule on a white background while
          retaining waveform color information (except for channel 1, which prints as dark blue
          because yellow does not show up well and is difficult to see on a white background). This
          option can significantly reduce print time and quantities of ink required compared with
          WYSIWYG dark background images.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:INKSaver?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:INKSaver?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HARDCopy:INKSaver?
        ```

    Info:
        - ``ON`` or <NR1> ≠ 0 sets the ink saver mode on.
        - ``OFF`` or <NR1> = 0 sets the ink saver mode off.
    """


class HardcopyActiveprinter(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy:ACTIVeprinter`` command.

    Description:
        - This command specifies the currently active printer. When a hard copy operation is
          performed, the output will be sent to this printer. One of two methods of specifying the
          printer can be used: specifying an index value obtained from looking at the list of
          attached printers or by specifying the printer name.

    Usage:
        - Using the ``.query()`` method will send the ``HARDCopy:ACTIVeprinter?`` query.
        - Using the ``.verify(value)`` method will send the ``HARDCopy:ACTIVeprinter?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HARDCopy:ACTIVeprinter value`` command.

    SCPI Syntax:
        ```
        - HARDCopy:ACTIVeprinter {<NR1>|<name>}
        - HARDCopy:ACTIVeprinter?
        ```

    Info:
        - ``<NR1>`` is the index of the desired printer as returned from ``HARDCOPY:PRINTER:LIST``.
        - ``<name>`` is the name of the printer as specified in the printer list. This name is case
          sensitive and must be entered exactly as shown in the list.
    """


class Hardcopy(SCPICmdWrite, SCPICmdRead):
    """The ``HARDCopy`` command.

    Description:
        - Sends a hard copy of the screen display to the currently active printer using the current
          palette and layout settings.

    Usage:
        - Using the ``.write(value)`` method will send the ``HARDCopy value`` command.

    SCPI Syntax:
        ```
        - HARDCopy {STARt}
        ```

    Info:
        - ``STARt`` sends a block of data representing the current screen image to the requested
          port. The data sent is in the image format specified by the ``SAVE:IMAGE:FILEFORMAT``
          command and the compression level is controlled by the selected format (BMP and TIFF are
          uncompressed whereas PNG is compressed). The ``HARDCOPY:INKSAVER`` determines whether the
          data sent is in InkSaver mode.

    Properties:
        - ``.activeprinter``: The ``HARDCopy:ACTIVeprinter`` command.
        - ``.inksaver``: The ``HARDCopy:INKSaver`` command.
        - ``.layout``: The ``HARDCopy:LAYout`` command.
        - ``.preview``: The ``HARDCopy:PREVIEW`` command.
        - ``.printer``: The ``HARDCopy:PRINTer`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "HARDCopy") -> None:
        super().__init__(device, cmd_syntax)
        self._activeprinter = HardcopyActiveprinter(device, f"{self._cmd_syntax}:ACTIVeprinter")
        self._inksaver = HardcopyInksaver(device, f"{self._cmd_syntax}:INKSaver")
        self._layout = HardcopyLayout(device, f"{self._cmd_syntax}:LAYout")
        self._preview = HardcopyPreview(device, f"{self._cmd_syntax}:PREVIEW")
        self._printer = HardcopyPrinter(device, f"{self._cmd_syntax}:PRINTer")

    @property
    def activeprinter(self) -> HardcopyActiveprinter:
        """Return the ``HARDCopy:ACTIVeprinter`` command.

        Description:
            - This command specifies the currently active printer. When a hard copy operation is
              performed, the output will be sent to this printer. One of two methods of specifying
              the printer can be used: specifying an index value obtained from looking at the list
              of attached printers or by specifying the printer name.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:ACTIVeprinter?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:ACTIVeprinter?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy:ACTIVeprinter value``
              command.

        SCPI Syntax:
            ```
            - HARDCopy:ACTIVeprinter {<NR1>|<name>}
            - HARDCopy:ACTIVeprinter?
            ```

        Info:
            - ``<NR1>`` is the index of the desired printer as returned from
              ``HARDCOPY:PRINTER:LIST``.
            - ``<name>`` is the name of the printer as specified in the printer list. This name is
              case sensitive and must be entered exactly as shown in the list.
        """
        return self._activeprinter

    @property
    def inksaver(self) -> HardcopyInksaver:
        """Return the ``HARDCopy:INKSaver`` command.

        Description:
            - Changes hard copy output to print traces and graticule on a white background while
              retaining waveform color information (except for channel 1, which prints as dark blue
              because yellow does not show up well and is difficult to see on a white background).
              This option can significantly reduce print time and quantities of ink required
              compared with WYSIWYG dark background images.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:INKSaver?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:INKSaver?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HARDCopy:INKSaver?
            ```

        Info:
            - ``ON`` or <NR1> ≠ 0 sets the ink saver mode on.
            - ``OFF`` or <NR1> = 0 sets the ink saver mode off.
        """
        return self._inksaver

    @property
    def layout(self) -> HardcopyLayout:
        """Return the ``HARDCopy:LAYout`` command.

        Description:
            - This command specifies the page orientation for hard copy. If you set the layout to
              LANdscape, the printer will print hard copies in landscape mode where the long edge of
              the screen will print to the long edge of the sheet of paper. If you set the layout to
              PORTRait, the printer will print hard copies in portrait mode. This command is not
              applicable for PictBridge hardcopies.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:LAYout?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:LAYout?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy:LAYout value`` command.

        SCPI Syntax:
            ```
            - HARDCopy:LAYout {PORTRait|LANdscape}
            - HARDCopy:LAYout?
            ```

        Info:
            - ``PORTRait`` orients the screen image vertically on the printed page.
            - ``LANdscape`` orients the screen image horizontally on the printed page.
        """
        return self._layout

    @property
    def preview(self) -> HardcopyPreview:
        """Return the ``HARDCopy:PREVIEW`` command.

        Description:
            - Displays a preview of the current screen contents with the InkSaver Palette if
              ``HARDCopy:INKSAVER`` is 1 or the Normal Palette if ``HARDCopy:INKSAVER`` is 0.

        Usage:
            - Using the ``.write(value)`` method will send the ``HARDCopy:PREVIEW value`` command.

        SCPI Syntax:
            ```
            - HARDCopy:PREVIEW {ON|OFF|<NR1>}
            ```

        Info:
            - ``ON`` or <NR1> ≠ 0 turns preview mode on.
            - ``OFF`` or <NR1> = 0 turns preview mode off.
        """
        return self._preview

    @property
    def printer(self) -> HardcopyPrinter:
        """Return the ``HARDCopy:PRINTer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy:PRINTer?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy:PRINTer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.add``: The ``HARDCopy:PRINTer:ADD`` command.
            - ``.delete``: The ``HARDCopy:PRINTer:DELete`` command.
            - ``.list``: The ``HARDCopy:PRINTer:LIST`` command.
            - ``.rename``: The ``HARDCopy:PRINTer:REName`` command.
        """
        return self._printer
