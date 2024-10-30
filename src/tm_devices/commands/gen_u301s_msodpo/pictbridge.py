# pylint: disable=line-too-long
"""The pictbridge commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PICTBridge:DATEPrint {DEFLT|OFF|ON}
    - PICTBridge:DEFault
    - PICTBridge:IDPrint {DEFLT|OFF|ON}
    - PICTBridge:IDPrint?
    - PICTBridge:IMAGESize {DEFLT|IN2P5BY3P25|L|IN4BY6|L2|IN8BY10|L4|E|CARD|HAGAKIPC|CM6BY8|CM7BY10|CM9BY13|CM10BY15|CM13BY18|CM15BY21|CM18BY24|A4|LETTER}
    - PICTBridge:PAPERSize {DEFLT|L|L2|HAGAKIPCARD|MM54BY86|MM100BY150|IN4BY6|IN8BY10|LETTER|IN11BY17|A0|A1|A2|A3|A4|A5|A6|A7|A8|A9|B0|B1|B2|B3|B4|B5|B6|B7|B8|B9|ROLL89MM|ROLL127MM|ROLL100MM|ROLL210MM}
    - PICTBridge:PAPERType {DEFLT|PLAIN|PHOTO|FASTPHOTO}
    - PICTBridge:PRINTQual {DEFLT|NRMAL|FINE|DRAFT}
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class PictbridgePrintqual(SCPICmdWrite):
    """The ``PICTBridge:PRINTQual`` command.

    Description:
        - Sets or returns the output print quality.

    Usage:
        - Using the ``.write(value)`` method will send the ``PICTBridge:PRINTQual value`` command.

    SCPI Syntax:
        ```
        - PICTBridge:PRINTQual {DEFLT|NRMAL|FINE|DRAFT}
        ```

    Info:
        - ``DEFLT`` for the default quality print.
        - ``NRMAL`` for a normal quality print.
        - ``FINE`` for a fine quality print.
        - ``DRAFT`` for a draft quality print.
    """


class PictbridgePapertype(SCPICmdWrite):
    """The ``PICTBridge:PAPERType`` command.

    Description:
        - Sets or returns the paper type.

    Usage:
        - Using the ``.write(value)`` method will send the ``PICTBridge:PAPERType value`` command.

    SCPI Syntax:
        ```
        - PICTBridge:PAPERType {DEFLT|PLAIN|PHOTO|FASTPHOTO}
        ```

    Info:
        - ``DEFLT`` for a default print paper type.
        - ``PLAIN`` for a plain print paper type.
        - ``PHOTO`` for a photo print paper type.
        - ``FASTPHOTO`` for a fastphoto print paper type.
    """


class PictbridgePapersize(SCPICmdWrite):
    """The ``PICTBridge:PAPERSize`` command.

    Description:
        - Sets the output print paper size.

    Usage:
        - Using the ``.write(value)`` method will send the ``PICTBridge:PAPERSize value`` command.

    SCPI Syntax:
        ```
        - PICTBridge:PAPERSize {DEFLT|L|L2|HAGAKIPCARD|MM54BY86|MM100BY150|IN4BY6|IN8BY10|LETTER|IN11BY17|A0|A1|A2|A3|A4|A5|A6|A7|A8|A9|B0|B1|B2|B3|B4|B5|B6|B7|B8|B9|ROLL89MM|ROLL127MM|ROLL100MM|ROLL210MM}
        ```

    Info:
        - ``DEFLT`` for a default paper size.
        - ``L`` for a paper size L.
        - ``L2`` for a paper size 2L.
        - ``HAGAKIPCARD`` for a paper size Hagaki.
        - ``MM54BY86`` for a card paper size.
        - ``MM100BY150`` for paper size of 100``*150 MM``.
        - ``IN4BY6`` for a paper size of 4``*6``.
        - ``IN8BY10`` for a paper size of 8``*10``.
        - ``LETTER`` for a letter paper size.
        - ``IN11BY17`` for a paper size of 11``*17``.
        - ``A0`` for a A0 paper size.
        - ``A1`` for a A1 paper size.
        - ``A2`` for a A2 paper size.
        - ``A3`` for a A3 paper size.
        - ``A4`` for a A4 paper size.
        - ``A5`` for a A5 paper size.
        - ``A6`` for a A6 paper size.
        - ``A7`` for a A7 paper size.
        - ``A8`` for a A8 paper size.
        - ``A9`` for a A9 paper size.
        - ``B0`` for a B0 paper size.
        - ``B1`` for a B1 paper size.
        - ``B2`` for a B2 paper size.
        - ``B3`` for a B3 paper size.
        - ``B4`` for a B4 paper size.
        - ``B5`` for a B5 paper size.
        - ``B6`` for a B6 paper size.
        - ``B7`` for a B7 paper size.
        - ``B8`` for a B8 paper size.
        - ``B9`` for a B9 paper size.
        - ``ROLL89MM`` for a 89 MM Roll paper size.
        - ``ROLL127MM`` for a 127 MM Roll paper size.
        - ``ROLL100MM`` for a 100 MM Roll paper size.
        - ``ROLL210MM`` for a 210 MM Roll paper size.
    """  # noqa: E501


class PictbridgeImagesize(SCPICmdWrite):
    """The ``PICTBridge:IMAGESize`` command.

    Description:
        - Sets or returns the image print size.

    Usage:
        - Using the ``.write(value)`` method will send the ``PICTBridge:IMAGESize value`` command.

    SCPI Syntax:
        ```
        - PICTBridge:IMAGESize {DEFLT|IN2P5BY3P25|L|IN4BY6|L2|IN8BY10|L4|E|CARD|HAGAKIPC|CM6BY8|CM7BY10|CM9BY13|CM10BY15|CM13BY18|CM15BY21|CM18BY24|A4|LETTER}
        ```

    Info:
        - ``DEFLT`` for a default image print size.
        - ``IN2P5BY3P25`` for a ``2_5````*3_25`` image print size.
        - ``L`` for a ``3_5````*5`` image print size.
        - ``IN4BY6`` for a 4``*6`` image print size.
        - ``L2`` for a 5``*7`` image print size.
        - ``IN8BY10`` for a 8``*10`` image print size.
        - ``L4`` for a 254 MM``*178 MM`` image print size.
        - ``E`` for a 110 MM``*74 MM`` image print size.
        - ``CARD`` for a 89 MM``*55MM`` image print size.
        - ``HAGAKIPC`` for a 100 MM``*148 MM`` image print size.
        - ``CM6BY8`` for a 6 CM``*8 CM`` image print size.
        - ``CM7BY10`` for a 7 CM``*10 CM`` image print size.
        - ``CM9BY13`` for a 9 CM``*13 CM`` image print size.
        - ``CM10BY15`` for a 10 CM``*15 CM`` image print size.
        - ``CM13BY18`` or a 13 CM``*18 CM`` image print size.
        - ``CM15BY21`` for a 15 CM``*21 CM`` image print size.
        - ``CM18BY24`` for a 18 CM``*24 CM`` image print size.
        - ``A4`` for a A4 image print size.
        - ``LETTER`` for a Letter image print size.
    """  # noqa: E501


class PictbridgeIdprint(SCPICmdWrite, SCPICmdRead):
    """The ``PICTBridge:IDPrint`` command.

    Description:
        - Enables or disables printing the oscilloscope model and serial number on the print output.

    Usage:
        - Using the ``.query()`` method will send the ``PICTBridge:IDPrint?`` query.
        - Using the ``.verify(value)`` method will send the ``PICTBridge:IDPrint?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PICTBridge:IDPrint value`` command.

    SCPI Syntax:
        ```
        - PICTBridge:IDPrint {DEFLT|OFF|ON}
        - PICTBridge:IDPrint?
        ```

    Info:
        - ``DEFLT`` is the default setting of the printer.
        - ``ON`` enables the oscilloscope model and serial number print on the print output.
        - ``OFF`` disables the oscilloscope model and serial number print on the print output.
    """


class PictbridgeDefault(SCPICmdWriteNoArguments):
    """The ``PICTBridge:DEFault`` command.

    Description:
        - Sets the arguments for all PictBridge commands to their default values. The default values
          are same as printer default settings.

    Usage:
        - Using the ``.write()`` method will send the ``PICTBridge:DEFault`` command.

    SCPI Syntax:
        ```
        - PICTBridge:DEFault
        ```
    """


class PictbridgeDateprint(SCPICmdWrite):
    """The ``PICTBridge:DATEPrint`` command.

    Description:
        - Enables or disables printing the date on the print output.

    Usage:
        - Using the ``.write(value)`` method will send the ``PICTBridge:DATEPrint value`` command.

    SCPI Syntax:
        ```
        - PICTBridge:DATEPrint {DEFLT|OFF|ON}
        ```

    Info:
        - ``DEFLT`` is the default setting of the printer.
        - ``ON`` enables the date print on the print output.
        - ``OFF`` disables the date print on the print output.
    """


class Pictbridge(SCPICmdRead):
    """The ``PICTBridge`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PICTBridge?`` query.
        - Using the ``.verify(value)`` method will send the ``PICTBridge?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dateprint``: The ``PICTBridge:DATEPrint`` command.
        - ``.default``: The ``PICTBridge:DEFault`` command.
        - ``.idprint``: The ``PICTBridge:IDPrint`` command.
        - ``.imagesize``: The ``PICTBridge:IMAGESize`` command.
        - ``.papersize``: The ``PICTBridge:PAPERSize`` command.
        - ``.papertype``: The ``PICTBridge:PAPERType`` command.
        - ``.printqual``: The ``PICTBridge:PRINTQual`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "PICTBridge"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._dateprint = PictbridgeDateprint(device, f"{self._cmd_syntax}:DATEPrint")
        self._default = PictbridgeDefault(device, f"{self._cmd_syntax}:DEFault")
        self._idprint = PictbridgeIdprint(device, f"{self._cmd_syntax}:IDPrint")
        self._imagesize = PictbridgeImagesize(device, f"{self._cmd_syntax}:IMAGESize")
        self._papersize = PictbridgePapersize(device, f"{self._cmd_syntax}:PAPERSize")
        self._papertype = PictbridgePapertype(device, f"{self._cmd_syntax}:PAPERType")
        self._printqual = PictbridgePrintqual(device, f"{self._cmd_syntax}:PRINTQual")

    @property
    def dateprint(self) -> PictbridgeDateprint:
        """Return the ``PICTBridge:DATEPrint`` command.

        Description:
            - Enables or disables printing the date on the print output.

        Usage:
            - Using the ``.write(value)`` method will send the ``PICTBridge:DATEPrint value``
              command.

        SCPI Syntax:
            ```
            - PICTBridge:DATEPrint {DEFLT|OFF|ON}
            ```

        Info:
            - ``DEFLT`` is the default setting of the printer.
            - ``ON`` enables the date print on the print output.
            - ``OFF`` disables the date print on the print output.
        """
        return self._dateprint

    @property
    def default(self) -> PictbridgeDefault:
        """Return the ``PICTBridge:DEFault`` command.

        Description:
            - Sets the arguments for all PictBridge commands to their default values. The default
              values are same as printer default settings.

        Usage:
            - Using the ``.write()`` method will send the ``PICTBridge:DEFault`` command.

        SCPI Syntax:
            ```
            - PICTBridge:DEFault
            ```
        """
        return self._default

    @property
    def idprint(self) -> PictbridgeIdprint:
        """Return the ``PICTBridge:IDPrint`` command.

        Description:
            - Enables or disables printing the oscilloscope model and serial number on the print
              output.

        Usage:
            - Using the ``.query()`` method will send the ``PICTBridge:IDPrint?`` query.
            - Using the ``.verify(value)`` method will send the ``PICTBridge:IDPrint?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PICTBridge:IDPrint value`` command.

        SCPI Syntax:
            ```
            - PICTBridge:IDPrint {DEFLT|OFF|ON}
            - PICTBridge:IDPrint?
            ```

        Info:
            - ``DEFLT`` is the default setting of the printer.
            - ``ON`` enables the oscilloscope model and serial number print on the print output.
            - ``OFF`` disables the oscilloscope model and serial number print on the print output.
        """
        return self._idprint

    @property
    def imagesize(self) -> PictbridgeImagesize:
        """Return the ``PICTBridge:IMAGESize`` command.

        Description:
            - Sets or returns the image print size.

        Usage:
            - Using the ``.write(value)`` method will send the ``PICTBridge:IMAGESize value``
              command.

        SCPI Syntax:
            ```
            - PICTBridge:IMAGESize {DEFLT|IN2P5BY3P25|L|IN4BY6|L2|IN8BY10|L4|E|CARD|HAGAKIPC|CM6BY8|CM7BY10|CM9BY13|CM10BY15|CM13BY18|CM15BY21|CM18BY24|A4|LETTER}
            ```

        Info:
            - ``DEFLT`` for a default image print size.
            - ``IN2P5BY3P25`` for a ``2_5````*3_25`` image print size.
            - ``L`` for a ``3_5````*5`` image print size.
            - ``IN4BY6`` for a 4``*6`` image print size.
            - ``L2`` for a 5``*7`` image print size.
            - ``IN8BY10`` for a 8``*10`` image print size.
            - ``L4`` for a 254 MM``*178 MM`` image print size.
            - ``E`` for a 110 MM``*74 MM`` image print size.
            - ``CARD`` for a 89 MM``*55MM`` image print size.
            - ``HAGAKIPC`` for a 100 MM``*148 MM`` image print size.
            - ``CM6BY8`` for a 6 CM``*8 CM`` image print size.
            - ``CM7BY10`` for a 7 CM``*10 CM`` image print size.
            - ``CM9BY13`` for a 9 CM``*13 CM`` image print size.
            - ``CM10BY15`` for a 10 CM``*15 CM`` image print size.
            - ``CM13BY18`` or a 13 CM``*18 CM`` image print size.
            - ``CM15BY21`` for a 15 CM``*21 CM`` image print size.
            - ``CM18BY24`` for a 18 CM``*24 CM`` image print size.
            - ``A4`` for a A4 image print size.
            - ``LETTER`` for a Letter image print size.
        """  # noqa: E501
        return self._imagesize

    @property
    def papersize(self) -> PictbridgePapersize:
        """Return the ``PICTBridge:PAPERSize`` command.

        Description:
            - Sets the output print paper size.

        Usage:
            - Using the ``.write(value)`` method will send the ``PICTBridge:PAPERSize value``
              command.

        SCPI Syntax:
            ```
            - PICTBridge:PAPERSize {DEFLT|L|L2|HAGAKIPCARD|MM54BY86|MM100BY150|IN4BY6|IN8BY10|LETTER|IN11BY17|A0|A1|A2|A3|A4|A5|A6|A7|A8|A9|B0|B1|B2|B3|B4|B5|B6|B7|B8|B9|ROLL89MM|ROLL127MM|ROLL100MM|ROLL210MM}
            ```

        Info:
            - ``DEFLT`` for a default paper size.
            - ``L`` for a paper size L.
            - ``L2`` for a paper size 2L.
            - ``HAGAKIPCARD`` for a paper size Hagaki.
            - ``MM54BY86`` for a card paper size.
            - ``MM100BY150`` for paper size of 100``*150 MM``.
            - ``IN4BY6`` for a paper size of 4``*6``.
            - ``IN8BY10`` for a paper size of 8``*10``.
            - ``LETTER`` for a letter paper size.
            - ``IN11BY17`` for a paper size of 11``*17``.
            - ``A0`` for a A0 paper size.
            - ``A1`` for a A1 paper size.
            - ``A2`` for a A2 paper size.
            - ``A3`` for a A3 paper size.
            - ``A4`` for a A4 paper size.
            - ``A5`` for a A5 paper size.
            - ``A6`` for a A6 paper size.
            - ``A7`` for a A7 paper size.
            - ``A8`` for a A8 paper size.
            - ``A9`` for a A9 paper size.
            - ``B0`` for a B0 paper size.
            - ``B1`` for a B1 paper size.
            - ``B2`` for a B2 paper size.
            - ``B3`` for a B3 paper size.
            - ``B4`` for a B4 paper size.
            - ``B5`` for a B5 paper size.
            - ``B6`` for a B6 paper size.
            - ``B7`` for a B7 paper size.
            - ``B8`` for a B8 paper size.
            - ``B9`` for a B9 paper size.
            - ``ROLL89MM`` for a 89 MM Roll paper size.
            - ``ROLL127MM`` for a 127 MM Roll paper size.
            - ``ROLL100MM`` for a 100 MM Roll paper size.
            - ``ROLL210MM`` for a 210 MM Roll paper size.
        """  # noqa: E501
        return self._papersize

    @property
    def papertype(self) -> PictbridgePapertype:
        """Return the ``PICTBridge:PAPERType`` command.

        Description:
            - Sets or returns the paper type.

        Usage:
            - Using the ``.write(value)`` method will send the ``PICTBridge:PAPERType value``
              command.

        SCPI Syntax:
            ```
            - PICTBridge:PAPERType {DEFLT|PLAIN|PHOTO|FASTPHOTO}
            ```

        Info:
            - ``DEFLT`` for a default print paper type.
            - ``PLAIN`` for a plain print paper type.
            - ``PHOTO`` for a photo print paper type.
            - ``FASTPHOTO`` for a fastphoto print paper type.
        """
        return self._papertype

    @property
    def printqual(self) -> PictbridgePrintqual:
        """Return the ``PICTBridge:PRINTQual`` command.

        Description:
            - Sets or returns the output print quality.

        Usage:
            - Using the ``.write(value)`` method will send the ``PICTBridge:PRINTQual value``
              command.

        SCPI Syntax:
            ```
            - PICTBridge:PRINTQual {DEFLT|NRMAL|FINE|DRAFT}
            ```

        Info:
            - ``DEFLT`` for the default quality print.
            - ``NRMAL`` for a normal quality print.
            - ``FINE`` for a fine quality print.
            - ``DRAFT`` for a draft quality print.
        """
        return self._printqual
