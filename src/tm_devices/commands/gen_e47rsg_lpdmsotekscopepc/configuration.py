"""The configuration commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CONFIGuration:ANALOg:BANDWidth?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ConfigurationAnalogBandwidth(SCPICmdRead):
    """The ``CONFIGuration:ANALOg:BANDWidth`` command.

    Description:
        - This command queries the maximum licensed bandwidth of the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:BANDWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:BANDWidth?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ANALOg:BANDWidth?
        ```
    """


class ConfigurationAnalog(SCPICmdRead):
    """The ``CONFIGuration:ANALOg`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bandwidth``: The ``CONFIGuration:ANALOg:BANDWidth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = ConfigurationAnalogBandwidth(device, f"{self._cmd_syntax}:BANDWidth")

    @property
    def bandwidth(self) -> ConfigurationAnalogBandwidth:
        """Return the ``CONFIGuration:ANALOg:BANDWidth`` command.

        Description:
            - This command queries the maximum licensed bandwidth of the instrument.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:BANDWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:BANDWidth?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ANALOg:BANDWidth?
            ```
        """
        return self._bandwidth


class Configuration(SCPICmdRead):
    """The ``CONFIGuration`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.analog``: The ``CONFIGuration:ANALOg`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "CONFIGuration"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._analog = ConfigurationAnalog(device, f"{self._cmd_syntax}:ANALOg")

    @property
    def analog(self) -> ConfigurationAnalog:
        """Return the ``CONFIGuration:ANALOg`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bandwidth``: The ``CONFIGuration:ANALOg:BANDWidth`` command.
        """
        return self._analog
