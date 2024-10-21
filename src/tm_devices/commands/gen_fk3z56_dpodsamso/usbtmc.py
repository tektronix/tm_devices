"""The usbtmc commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - USBTMC:PRODUCTID:DECimal?
    - USBTMC:PRODUCTID:HEXadecimal?
    - USBTMC:SERIALnumber?
    - USBTMC:VENDORID:DECimal?
    - USBTMC:VENDORID:HEXadecimal?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class UsbtmcVendoridHexadecimal(SCPICmdRead):
    """The ``USBTMC:VENDORID:HEXadecimal`` command.

    Description:
        - This query returns the vendor ID number as a hexadecimal value. The hexadecimal vendor ID
          for Tektronix instruments is 0x699. USBTMC stands for USB Test & Measurement Class, a
          protocol that allows GPIB-like communication with USB devices.

    Usage:
        - Using the ``.query()`` method will send the ``USBTMC:VENDORID:HEXadecimal?`` query.
        - Using the ``.verify(value)`` method will send the ``USBTMC:VENDORID:HEXadecimal?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - USBTMC:VENDORID:HEXadecimal?
        ```
    """


class UsbtmcVendoridDecimal(SCPICmdRead):
    """The ``USBTMC:VENDORID:DECimal`` command.

    Description:
        - This query returns the vendor ID number as a decimal. The decimal vendor ID for Tektronix
          instruments is 1689. USBTMC stands for USB Test & Measurement Class, a protocol that
          allows GPIB-like communication with USB devices.

    Usage:
        - Using the ``.query()`` method will send the ``USBTMC:VENDORID:DECimal?`` query.
        - Using the ``.verify(value)`` method will send the ``USBTMC:VENDORID:DECimal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - USBTMC:VENDORID:DECimal?
        ```
    """


class UsbtmcVendorid(SCPICmdRead):
    """The ``USBTMC:VENDORID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``USBTMC:VENDORID?`` query.
        - Using the ``.verify(value)`` method will send the ``USBTMC:VENDORID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.decimal``: The ``USBTMC:VENDORID:DECimal`` command.
        - ``.hexadecimal``: The ``USBTMC:VENDORID:HEXadecimal`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._decimal = UsbtmcVendoridDecimal(device, f"{self._cmd_syntax}:DECimal")
        self._hexadecimal = UsbtmcVendoridHexadecimal(device, f"{self._cmd_syntax}:HEXadecimal")

    @property
    def decimal(self) -> UsbtmcVendoridDecimal:
        """Return the ``USBTMC:VENDORID:DECimal`` command.

        Description:
            - This query returns the vendor ID number as a decimal. The decimal vendor ID for
              Tektronix instruments is 1689. USBTMC stands for USB Test & Measurement Class, a
              protocol that allows GPIB-like communication with USB devices.

        Usage:
            - Using the ``.query()`` method will send the ``USBTMC:VENDORID:DECimal?`` query.
            - Using the ``.verify(value)`` method will send the ``USBTMC:VENDORID:DECimal?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - USBTMC:VENDORID:DECimal?
            ```
        """
        return self._decimal

    @property
    def hexadecimal(self) -> UsbtmcVendoridHexadecimal:
        """Return the ``USBTMC:VENDORID:HEXadecimal`` command.

        Description:
            - This query returns the vendor ID number as a hexadecimal value. The hexadecimal vendor
              ID for Tektronix instruments is 0x699. USBTMC stands for USB Test & Measurement Class,
              a protocol that allows GPIB-like communication with USB devices.

        Usage:
            - Using the ``.query()`` method will send the ``USBTMC:VENDORID:HEXadecimal?`` query.
            - Using the ``.verify(value)`` method will send the ``USBTMC:VENDORID:HEXadecimal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - USBTMC:VENDORID:HEXadecimal?
            ```
        """
        return self._hexadecimal


class UsbtmcSerialnumber(SCPICmdRead):
    """The ``USBTMC:SERIALnumber`` command.

    Description:
        - This query returns the serial number of the oscilloscope. USBTMC stands for USB Test &
          Measurement Class, a protocol that allows GPIB-like communication with USB devices.

    Usage:
        - Using the ``.query()`` method will send the ``USBTMC:SERIALnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``USBTMC:SERIALnumber?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - USBTMC:SERIALnumber?
        ```
    """


class UsbtmcProductidHexadecimal(SCPICmdRead):
    """The ``USBTMC:PRODUCTID:HEXadecimal`` command.

    Description:
        - This query returns the product ID number as a hexadecimal value. The product ID numbers
          vary for each instrument family and model. USBTMC stands for USB Test & Measurement Class,
          a protocol that allows GPIB-like communication with USB devices. For product ID numbers,
          see the following table.

    Usage:
        - Using the ``.query()`` method will send the ``USBTMC:PRODUCTID:HEXadecimal?`` query.
        - Using the ``.verify(value)`` method will send the ``USBTMC:PRODUCTID:HEXadecimal?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - USBTMC:PRODUCTID:HEXadecimal?
        ```
    """


class UsbtmcProductidDecimal(SCPICmdRead):
    """The ``USBTMC:PRODUCTID:DECimal`` command.

    Description:
        - This query returns the product ID number as a decimal. The product ID numbers vary for
          each instrument family and model. USBTMC stands for USB Test & Measurement Class, a
          protocol that allows GPIB-like communication with USB devices. For product ID numbers, see
          the following table.

    Usage:
        - Using the ``.query()`` method will send the ``USBTMC:PRODUCTID:DECimal?`` query.
        - Using the ``.verify(value)`` method will send the ``USBTMC:PRODUCTID:DECimal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - USBTMC:PRODUCTID:DECimal?
        ```
    """


class UsbtmcProductid(SCPICmdRead):
    """The ``USBTMC:PRODUCTID`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``USBTMC:PRODUCTID?`` query.
        - Using the ``.verify(value)`` method will send the ``USBTMC:PRODUCTID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.decimal``: The ``USBTMC:PRODUCTID:DECimal`` command.
        - ``.hexadecimal``: The ``USBTMC:PRODUCTID:HEXadecimal`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._decimal = UsbtmcProductidDecimal(device, f"{self._cmd_syntax}:DECimal")
        self._hexadecimal = UsbtmcProductidHexadecimal(device, f"{self._cmd_syntax}:HEXadecimal")

    @property
    def decimal(self) -> UsbtmcProductidDecimal:
        """Return the ``USBTMC:PRODUCTID:DECimal`` command.

        Description:
            - This query returns the product ID number as a decimal. The product ID numbers vary for
              each instrument family and model. USBTMC stands for USB Test & Measurement Class, a
              protocol that allows GPIB-like communication with USB devices. For product ID numbers,
              see the following table.

        Usage:
            - Using the ``.query()`` method will send the ``USBTMC:PRODUCTID:DECimal?`` query.
            - Using the ``.verify(value)`` method will send the ``USBTMC:PRODUCTID:DECimal?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - USBTMC:PRODUCTID:DECimal?
            ```
        """
        return self._decimal

    @property
    def hexadecimal(self) -> UsbtmcProductidHexadecimal:
        """Return the ``USBTMC:PRODUCTID:HEXadecimal`` command.

        Description:
            - This query returns the product ID number as a hexadecimal value. The product ID
              numbers vary for each instrument family and model. USBTMC stands for USB Test &
              Measurement Class, a protocol that allows GPIB-like communication with USB devices.
              For product ID numbers, see the following table.

        Usage:
            - Using the ``.query()`` method will send the ``USBTMC:PRODUCTID:HEXadecimal?`` query.
            - Using the ``.verify(value)`` method will send the ``USBTMC:PRODUCTID:HEXadecimal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - USBTMC:PRODUCTID:HEXadecimal?
            ```
        """
        return self._hexadecimal


class Usbtmc(SCPICmdRead):
    """The ``USBTMC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``USBTMC?`` query.
        - Using the ``.verify(value)`` method will send the ``USBTMC?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.productid``: The ``USBTMC:PRODUCTID`` command tree.
        - ``.serialnumber``: The ``USBTMC:SERIALnumber`` command.
        - ``.vendorid``: The ``USBTMC:VENDORID`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "USBTMC") -> None:
        super().__init__(device, cmd_syntax)
        self._productid = UsbtmcProductid(device, f"{self._cmd_syntax}:PRODUCTID")
        self._serialnumber = UsbtmcSerialnumber(device, f"{self._cmd_syntax}:SERIALnumber")
        self._vendorid = UsbtmcVendorid(device, f"{self._cmd_syntax}:VENDORID")

    @property
    def productid(self) -> UsbtmcProductid:
        """Return the ``USBTMC:PRODUCTID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``USBTMC:PRODUCTID?`` query.
            - Using the ``.verify(value)`` method will send the ``USBTMC:PRODUCTID?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.decimal``: The ``USBTMC:PRODUCTID:DECimal`` command.
            - ``.hexadecimal``: The ``USBTMC:PRODUCTID:HEXadecimal`` command.
        """
        return self._productid

    @property
    def serialnumber(self) -> UsbtmcSerialnumber:
        """Return the ``USBTMC:SERIALnumber`` command.

        Description:
            - This query returns the serial number of the oscilloscope. USBTMC stands for USB Test &
              Measurement Class, a protocol that allows GPIB-like communication with USB devices.

        Usage:
            - Using the ``.query()`` method will send the ``USBTMC:SERIALnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``USBTMC:SERIALnumber?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - USBTMC:SERIALnumber?
            ```
        """
        return self._serialnumber

    @property
    def vendorid(self) -> UsbtmcVendorid:
        """Return the ``USBTMC:VENDORID`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``USBTMC:VENDORID?`` query.
            - Using the ``.verify(value)`` method will send the ``USBTMC:VENDORID?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.decimal``: The ``USBTMC:VENDORID:DECimal`` command.
            - ``.hexadecimal``: The ``USBTMC:VENDORID:HEXadecimal`` command.
        """
        return self._vendorid
