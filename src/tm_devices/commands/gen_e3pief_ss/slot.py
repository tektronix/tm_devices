# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The slot commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - slot[slot].banks.matrix
    - slot[slot].columns.matrix
    - slot[slot].commonsideohms
    - slot[slot].digio
    - slot[slot].idn
    - slot[slot].interlock.override
    - slot[slot].interlock.state
    - slot[slot].isolated
    - slot[slot].matrix
    - slot[slot].maxvoltage
    - slot[slot].multiplexer
    - slot[slot].poles.four
    - slot[slot].poles.one
    - slot[slot].poles.two
    - slot[slot].pseudocard
    - slot[slot].rows.matrix
    - slot[slot].tempsensor
    - slot[slot].thermal.state
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class SlotItemThermal(BaseTSPCmd):
    """The ``slot[slot].thermal`` command tree.

    Info:
        - ``slot``, the slot number (1 to 6).

    Properties and methods:
        - ``.state``: The ``slot[slot].thermal.state`` attribute.
    """

    @property
    def state(self) -> str:
        """Access the ``slot[slot].thermal.state`` attribute.

        Description:
            - This attribute indicates the thermal state of the card in the specified slot.

        Usage:
            - Accessing this property will send the ``print(slot[slot].thermal.state)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].thermal.state)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".state"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.state)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.state`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemRows(BaseTSPCmd):
    """The ``slot[slot].rows`` command tree.

    Info:
        - ``slot``, the slot number (1 to 6).

    Properties and methods:
        - ``.matrix``: The ``slot[slot].rows.matrix`` attribute.
    """

    @property
    def matrix(self) -> str:
        """Access the ``slot[slot].rows.matrix`` attribute.

        Description:
            - This attribute returns the number of rows in the matrix on the card in the specified
              slot.

        Usage:
            - Accessing this property will send the ``print(slot[slot].rows.matrix)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].rows.matrix)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".matrix"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.matrix)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.matrix`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemPoles(BaseTSPCmd):
    """The ``slot[slot].poles`` command tree.

    Info:
        - ``slot``, the slot number (1 to 6).

    Properties and methods:
        - ``.four``: The ``slot[slot].poles.four`` attribute.
        - ``.one``: The ``slot[slot].poles.one`` attribute.
        - ``.two``: The ``slot[slot].poles.two`` attribute.
    """

    @property
    def four(self) -> str:
        """Access the ``slot[slot].poles.four`` attribute.

        Description:
            - This attribute indicates if a four-pole setting is supported for the channels on the
              card.

        Usage:
            - Accessing this property will send the ``print(slot[slot].poles.four)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].poles.four)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".four"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.four)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.four`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def one(self) -> str:
        """Access the ``slot[slot].poles.one`` attribute.

        Description:
            - This attribute indicates if a one-pole setting is supported for the channels on the
              specified card.

        Usage:
            - Accessing this property will send the ``print(slot[slot].poles.one)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].poles.one)
            ```

        Info:
            - ``slot``, the slot number  (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".one"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.one)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.one`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def two(self) -> str:
        """Access the ``slot[slot].poles.two`` attribute.

        Description:
            - This attribute indicates if a two-pole setting is supported for the channels on the
              card.

        Usage:
            - Accessing this property will send the ``print(slot[slot].poles.two)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].poles.two)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".two"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.two)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.two`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemInterlock(BaseTSPCmd):
    """The ``slot[slot].interlock`` command tree.

    Info:
        - ``slot``, the slot (1 to 6) containing the card to which the interlock state is applied.

    Properties and methods:
        - ``.override``: The ``slot[slot].interlock.override`` attribute.
        - ``.state``: The ``slot[slot].interlock.state`` attribute.
    """

    @property
    def override(self) -> str:
        """Access the ``slot[slot].interlock.override`` attribute.

        Description:
            - This attribute suppresses or permits interlock errors to be generated.

        Usage:
            - Accessing this property will send the ``print(slot[slot].interlock.override)`` query.
            - Setting this property to a value will send the
              ``slot[slot].interlock.override = value`` command.

        TSP Syntax:
            ```
            - slot[slot].interlock.override = value
            - print(slot[slot].interlock.override)
            ```

        Info:
            - ``slot``, the slot (1 to 6) containing the card to which the interlock state is
              applied.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".override"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.override)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.override`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @override.setter
    def override(self, value: Union[str, float]) -> None:
        """Access the ``slot[slot].interlock.override`` attribute.

        Description:
            - This attribute suppresses or permits interlock errors to be generated.

        Usage:
            - Accessing this property will send the ``print(slot[slot].interlock.override)`` query.
            - Setting this property to a value will send the
              ``slot[slot].interlock.override = value`` command.

        TSP Syntax:
            ```
            - slot[slot].interlock.override = value
            - print(slot[slot].interlock.override)
            ```

        Info:
            - ``slot``, the slot (1 to 6) containing the card to which the interlock state is
              applied.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".override", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.override = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.override`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def state(self) -> str:
        """Access the ``slot[slot].interlock.state`` attribute.

        Description:
            - This attribute indicates the interlock state of a card.

        Usage:
            - Accessing this property will send the ``print(slot[slot].interlock.state)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].interlock.state)
            ```

        Info:
            - ``slot``, the slot (1 to 6) containing the card to which the interlock state is
              applied.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".state"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.state)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.state`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemColumns(BaseTSPCmd):
    """The ``slot[slot].columns`` command tree.

    Info:
        - ``slot``, the slot number (1 to 6).

    Properties and methods:
        - ``.matrix``: The ``slot[slot].columns.matrix`` attribute.
    """

    @property
    def matrix(self) -> str:
        """Access the ``slot[slot].columns.matrix`` attribute.

        Description:
            - This attribute returns the number of columns in the matrix for the card in the
              specified slot.

        Usage:
            - Accessing this property will send the ``print(slot[slot].columns.matrix)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].columns.matrix)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".matrix"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.matrix)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.matrix`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemBanks(BaseTSPCmd):
    """The ``slot[slot].banks`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.matrix``: The ``slot[slot].banks.matrix`` attribute.
    """

    @property
    def matrix(self) -> str:
        """Access the ``slot[slot].banks.matrix`` attribute.

        Description:
            - This attribute describes the number of banks in the matrix for a card.

        Usage:
            - Accessing this property will send the ``print(slot[slot].banks.matrix)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].banks.matrix)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".matrix"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.matrix)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.matrix`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[slot]`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.banks``: The ``slot[slot].banks`` command tree.
        - ``.columns``: The ``slot[slot].columns`` command tree.
        - ``.commonsideohms``: The ``slot[slot].commonsideohms`` attribute.
        - ``.digio``: The ``slot[slot].digio`` attribute.
        - ``.idn``: The ``slot[slot].idn`` attribute.
        - ``.interlock``: The ``slot[slot].interlock`` command tree.
        - ``.isolated``: The ``slot[slot].isolated`` attribute.
        - ``.matrix``: The ``slot[slot].matrix`` attribute.
        - ``.maxvoltage``: The ``slot[slot].maxvoltage`` attribute.
        - ``.multiplexer``: The ``slot[slot].multiplexer`` attribute.
        - ``.poles``: The ``slot[slot].poles`` command tree.
        - ``.pseudocard``: The ``slot[slot].pseudocard`` attribute.
        - ``.rows``: The ``slot[slot].rows`` command tree.
        - ``.tempsensor``: The ``slot[slot].tempsensor`` attribute.
        - ``.thermal``: The ``slot[slot].thermal`` command tree.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "slot[slot]"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._banks = SlotItemBanks(device, f"{self._cmd_syntax}.banks")
        self._columns = SlotItemColumns(device, f"{self._cmd_syntax}.columns")
        self._interlock = SlotItemInterlock(device, f"{self._cmd_syntax}.interlock")
        self._poles = SlotItemPoles(device, f"{self._cmd_syntax}.poles")
        self._rows = SlotItemRows(device, f"{self._cmd_syntax}.rows")
        self._thermal = SlotItemThermal(device, f"{self._cmd_syntax}.thermal")

    @property
    def banks(self) -> SlotItemBanks:
        """Return the ``slot[slot].banks`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.matrix``: The ``slot[slot].banks.matrix`` attribute.
        """
        return self._banks

    @property
    def columns(self) -> SlotItemColumns:
        """Return the ``slot[slot].columns`` command tree.

        Info:
            - ``slot``, the slot number (1 to 6).

        Sub-properties and sub-methods:
            - ``.matrix``: The ``slot[slot].columns.matrix`` attribute.
        """
        return self._columns

    @property
    def commonsideohms(self) -> str:
        """Access the ``slot[slot].commonsideohms`` attribute.

        Description:
            - This attribute indicates whether a card in the specified slot supports commonside
              channels for 4-wire resistance measurements.

        Usage:
            - Accessing this property will send the ``print(slot[slot].commonsideohms)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].commonsideohms)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".commonsideohms"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.commonsideohms)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.commonsideohms`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def digio(self) -> str:
        """Access the ``slot[slot].digio`` attribute.

        Description:
            - This attribute indicates whether or not a card in the specified slot supports digital
              input and output channels.

        Usage:
            - Accessing this property will send the ``print(slot[slot].digio)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].digio)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".digio"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.digio)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.digio`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def idn(self) -> str:
        """Access the ``slot[slot].idn`` attribute.

        Description:
            - This attribute returns a string that contains information about the plug-in card.

        Usage:
            - Accessing this property will send the ``print(slot[slot].idn)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].idn)
            ```

        Info:
            - ``slot``, the slot number(1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".idn"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.idn)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.idn`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def interlock(self) -> SlotItemInterlock:
        """Return the ``slot[slot].interlock`` command tree.

        Info:
            - ``slot``, the slot (1 to 6) containing the card to which the interlock state is
              applied.

        Sub-properties and sub-methods:
            - ``.override``: The ``slot[slot].interlock.override`` attribute.
            - ``.state``: The ``slot[slot].interlock.state`` attribute.
        """
        return self._interlock

    @property
    def isolated(self) -> str:
        """Access the ``slot[slot].isolated`` attribute.

        Description:
            - This attribute indicates if the card in the specified slot supports isolated channels.

        Usage:
            - Accessing this property will send the ``print(slot[slot].isolated)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].isolated)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".isolated"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.isolated)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.isolated`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def matrix(self) -> str:
        """Access the ``slot[slot].matrix`` attribute.

        Description:
            - This attribute indicates if the card in the specified slot supports matrix channels.

        Usage:
            - Accessing this property will send the ``print(slot[slot].matrix)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].matrix)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".matrix"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.matrix)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.matrix`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def maxvoltage(self) -> str:
        """Access the ``slot[slot].maxvoltage`` attribute.

        Description:
            - This attribute returns the maximum voltage of all channels on a plug-in card in the
              specified slot.

        Usage:
            - Accessing this property will send the ``print(slot[slot].maxvoltage)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].maxvoltage)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".maxvoltage"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.maxvoltage)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.maxvoltage`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def multiplexer(self) -> str:
        """Access the ``slot[slot].multiplexer`` attribute.

        Description:
            - This attribute indicates if the card in the specified slot supports multiplexer
              channels.

        Usage:
            - Accessing this property will send the ``print(slot[slot].multiplexer)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].multiplexer)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".multiplexer"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.multiplexer)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.multiplexer`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def poles(self) -> SlotItemPoles:
        """Return the ``slot[slot].poles`` command tree.

        Info:
            - ``slot``, the slot number (1 to 6).

        Sub-properties and sub-methods:
            - ``.four``: The ``slot[slot].poles.four`` attribute.
            - ``.one``: The ``slot[slot].poles.one`` attribute.
            - ``.two``: The ``slot[slot].poles.two`` attribute.
        """
        return self._poles

    @property
    def pseudocard(self) -> str:
        """Access the ``slot[slot].pseudocard`` attribute.

        Description:
            - This attribute specifies a pseudocard to implement.

        Usage:
            - Accessing this property will send the ``print(slot[slot].pseudocard)`` query.
            - Setting this property to a value will send the ``slot[slot].pseudocard = value``
              command.

        TSP Syntax:
            ```
            - slot[slot].pseudocard = value
            - print(slot[slot].pseudocard)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".pseudocard"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.pseudocard)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.pseudocard`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @pseudocard.setter
    def pseudocard(self, value: Union[str, float]) -> None:
        """Access the ``slot[slot].pseudocard`` attribute.

        Description:
            - This attribute specifies a pseudocard to implement.

        Usage:
            - Accessing this property will send the ``print(slot[slot].pseudocard)`` query.
            - Setting this property to a value will send the ``slot[slot].pseudocard = value``
              command.

        TSP Syntax:
            ```
            - slot[slot].pseudocard = value
            - print(slot[slot].pseudocard)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".pseudocard", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.pseudocard = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.pseudocard`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rows(self) -> SlotItemRows:
        """Return the ``slot[slot].rows`` command tree.

        Info:
            - ``slot``, the slot number (1 to 6).

        Sub-properties and sub-methods:
            - ``.matrix``: The ``slot[slot].rows.matrix`` attribute.
        """
        return self._rows

    @property
    def tempsensor(self) -> str:
        """Access the ``slot[slot].tempsensor`` attribute.

        Description:
            - This attribute indicates if the module in the specified slot supports temperature
              sensor channels.

        Usage:
            - Accessing this property will send the ``print(slot[slot].tempsensor)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].tempsensor)
            ```

        Info:
            - ``slot``, the slot number (1 to 6).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".tempsensor"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.tempsensor)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tempsensor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def thermal(self) -> SlotItemThermal:
        """Return the ``slot[slot].thermal`` command tree.

        Info:
            - ``slot``, the slot number (1 to 6).

        Sub-properties and sub-methods:
            - ``.state``: The ``slot[slot].thermal.state`` attribute.
        """
        return self._thermal
