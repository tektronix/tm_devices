# pylint: disable=line-too-long
"""The language commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - LANGuage {ENGLish|FRENch|GERMan|ITALian|SPANish|PORTUguese|JAPAnese|KOREan|RUSSian|SIMPlifiedchinese|TRADitionalchinese}
    - LANGuage?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Language(SCPICmdWrite, SCPICmdRead):
    """The ``LANGuage`` command.

    Description:
        - This command specifies the user interface display language. This command only affects the
          oscilloscope displayed language. Remote commands and their responses are always in
          English.

    Usage:
        - Using the ``.query()`` method will send the ``LANGuage?`` query.
        - Using the ``.verify(value)`` method will send the ``LANGuage?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LANGuage value`` command.

    SCPI Syntax:
        ```
        - LANGuage {ENGLish|FRENch|GERMan|ITALian|SPANish|PORTUguese|JAPAnese|KOREan|RUSSian|SIMPlifiedchinese|TRADitionalchinese}
        - LANGuage?
        ```
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "LANGuage") -> None:
        super().__init__(device, cmd_syntax)
