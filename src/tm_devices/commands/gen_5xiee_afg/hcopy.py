"""The hcopy commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HCOPy:SDUMp:IMMediate
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HcopySdumpImmediate(SCPICmdWriteNoArguments):
    """The ``HCOPy:SDUMp:IMMediate`` command.

    Description:
        - This command copies a screen image and saves the image file to a USB memory. The default
          file name is TEK00nnn.BMP, where nnn is a consecutive number from 000 through 999. The
          image files are saved in a folder named 'TEK' in the USB memory.

    Usage:
        - Using the ``.write()`` method will send the ``HCOPy:SDUMp:IMMediate`` command.

    SCPI Syntax:
        ```
        - HCOPy:SDUMp:IMMediate
        ```
    """


class HcopySdump(SCPICmdRead):
    """The ``HCOPy:SDUMp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HCOPy:SDUMp?`` query.
        - Using the ``.verify(value)`` method will send the ``HCOPy:SDUMp?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``HCOPy:SDUMp:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = HcopySdumpImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> HcopySdumpImmediate:
        """Return the ``HCOPy:SDUMp:IMMediate`` command.

        Description:
            - This command copies a screen image and saves the image file to a USB memory. The
              default file name is TEK00nnn.BMP, where nnn is a consecutive number from 000 through
              999. The image files are saved in a folder named 'TEK' in the USB memory.

        Usage:
            - Using the ``.write()`` method will send the ``HCOPy:SDUMp:IMMediate`` command.

        SCPI Syntax:
            ```
            - HCOPy:SDUMp:IMMediate
            ```
        """
        return self._immediate


class Hcopy(SCPICmdRead):
    """The ``HCOPy`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HCOPy?`` query.
        - Using the ``.verify(value)`` method will send the ``HCOPy?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sdump``: The ``HCOPy:SDUMp`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "HCOPy") -> None:
        super().__init__(device, cmd_syntax)
        self._sdump = HcopySdump(device, f"{self._cmd_syntax}:SDUMp")

    @property
    def sdump(self) -> HcopySdump:
        """Return the ``HCOPy:SDUMp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HCOPy:SDUMp?`` query.
            - Using the ``.verify(value)`` method will send the ``HCOPy:SDUMp?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``HCOPy:SDUMp:IMMediate`` command.
        """
        return self._sdump
