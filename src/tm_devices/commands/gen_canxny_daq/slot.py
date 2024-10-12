# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The slot commands module.

These commands are used in the following models:
DAQ6510

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - slot[slot].amps.endchannel
    - slot[slot].amps.startchannel
    - slot[slot].analogoutput.endchannel
    - slot[slot].analogoutput.startchannel
    - slot[slot].commonsideohms
    - slot[slot].digitalio.endchannel
    - slot[slot].digitalio.startchannel
    - slot[slot].idn
    - slot[slot].isolated.endchannel
    - slot[slot].isolated.startchannel
    - slot[slot].matrix.columns
    - slot[slot].matrix.rows
    - slot[slot].maxvoltage
    - slot[slot].pseudocard
    - slot[slot].tempsensor
    - slot[slot].totalizer.endchannel
    - slot[slot].totalizer.startchannel
    - slot[slot].voltage.endchannel
    - slot[slot].voltage.startchannel
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class SlotItemVoltage(BaseTSPCmd):
    """The ``slot[slot].voltage`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.endchannel``: The ``slot[slot].voltage.endchannel`` attribute.
        - ``.startchannel``: The ``slot[slot].voltage.startchannel`` attribute.
    """

    @property
    def endchannel(self) -> str:
        """Access the ``slot[slot].voltage.endchannel`` attribute.

        Description:
            - This attribute indicates the last channel in the specified slot that supports voltage
              or 2-wire measurements.

        Usage:
            - Accessing this property will send the ``print(slot[slot].voltage.endchannel)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].voltage.endchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".endchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.endchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.endchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def startchannel(self) -> str:
        """Access the ``slot[slot].voltage.startchannel`` attribute.

        Description:
            - This attribute indicates the first channel in the specified slot that supports voltage
              or 2-wire measurements.

        Usage:
            - Accessing this property will send the ``print(slot[slot].voltage.startchannel)``
              query.

        TSP Syntax:
            ```
            - print(slot[slot].voltage.startchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".startchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.startchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.startchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemTotalizer(BaseTSPCmd):
    """The ``slot[slot].totalizer`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.endchannel``: The ``slot[slot].totalizer.endchannel`` attribute.
        - ``.startchannel``: The ``slot[slot].totalizer.startchannel`` attribute.
    """

    @property
    def endchannel(self) -> str:
        """Access the ``slot[slot].totalizer.endchannel`` attribute.

        Description:
            - This attribute indicates the last totalizer channel in the specified slot.

        Usage:
            - Accessing this property will send the ``print(slot[slot].totalizer.endchannel)``
              query.

        TSP Syntax:
            ```
            - print(slot[slot].totalizer.endchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".endchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.endchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.endchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def startchannel(self) -> str:
        """Access the ``slot[slot].totalizer.startchannel`` attribute.

        Description:
            - This attribute indicates the first totalizer channel in the specified slot.

        Usage:
            - Accessing this property will send the ``print(slot[slot].totalizer.startchannel)``
              query.

        TSP Syntax:
            ```
            - print(slot[slot].totalizer.startchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".startchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.startchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.startchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemMatrix(BaseTSPCmd):
    """The ``slot[slot].matrix`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.columns``: The ``slot[slot].matrix.columns`` attribute.
        - ``.rows``: The ``slot[slot].matrix.rows`` attribute.
    """

    @property
    def columns(self) -> str:
        """Access the ``slot[slot].matrix.columns`` attribute.

        Description:
            - This attribute returns the number of columns in the matrix for the card in the
              specified slot.

        Usage:
            - Accessing this property will send the ``print(slot[slot].matrix.columns)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].matrix.columns)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".columns"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.columns)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.columns`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rows(self) -> str:
        """Access the ``slot[slot].matrix.rows`` attribute.

        Description:
            - This attribute returns the number of rows in the matrix on the card in the specified
              slot.

        Usage:
            - Accessing this property will send the ``print(slot[slot].matrix.rows)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].matrix.rows)
            ```

        Info:
            - ``slot``, the slot number (1 or 2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rows"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rows)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rows`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemIsolated(BaseTSPCmd):
    """The ``slot[slot].isolated`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.endchannel``: The ``slot[slot].isolated.endchannel`` attribute.
        - ``.startchannel``: The ``slot[slot].isolated.startchannel`` attribute.
    """

    @property
    def endchannel(self) -> str:
        """Access the ``slot[slot].isolated.endchannel`` attribute.

        Description:
            - This attribute indicates the last channel in the specified slot that has isolated
              channels.

        Usage:
            - Accessing this property will send the ``print(slot[slot].isolated.endchannel)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].isolated.endchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".endchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.endchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.endchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def startchannel(self) -> str:
        """Access the ``slot[slot].isolated.startchannel`` attribute.

        Description:
            - This attribute indicates the first channel in the specified slot that has isolated
              channels.

        Usage:
            - Accessing this property will send the ``print(slot[slot].isolated.startchannel)``
              query.

        TSP Syntax:
            ```
            - print(slot[slot].isolated.startchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".startchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.startchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.startchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemDigitalio(BaseTSPCmd):
    """The ``slot[slot].digitalio`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.endchannel``: The ``slot[slot].digitalio.endchannel`` attribute.
        - ``.startchannel``: The ``slot[slot].digitalio.startchannel`` attribute.
    """

    @property
    def endchannel(self) -> str:
        """Access the ``slot[slot].digitalio.endchannel`` attribute.

        Description:
            - This attribute indicates the last channel in the specified slot that supports digital
              inputs and outputs.

        Usage:
            - Accessing this property will send the ``print(slot[slot].digitalio.endchannel)``
              query.

        TSP Syntax:
            ```
            - print(slot[slot].digitalio.endchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".endchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.endchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.endchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def startchannel(self) -> str:
        """Access the ``slot[slot].digitalio.startchannel`` attribute.

        Description:
            - This attribute indicates the first channel in the specified slot that supports digital
              inputs and outputs.

        Usage:
            - Accessing this property will send the ``print(slot[slot].digitalio.startchannel)``
              query.

        TSP Syntax:
            ```
            - print(slot[slot].digitalio.startchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".startchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.startchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.startchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemAnalogoutput(BaseTSPCmd):
    """The ``slot[slot].analogoutput`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.endchannel``: The ``slot[slot].analogoutput.endchannel`` attribute.
        - ``.startchannel``: The ``slot[slot].analogoutput.startchannel`` attribute.
    """

    @property
    def endchannel(self) -> str:
        """Access the ``slot[slot].analogoutput.endchannel`` attribute.

        Description:
            - This attribute indicates the last channel in the specified slot that supports analog
              outputs.

        Usage:
            - Accessing this property will send the ``print(slot[slot].analogoutput.endchannel)``
              query.

        TSP Syntax:
            ```
            - print(slot[slot].analogoutput.endchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".endchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.endchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.endchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def startchannel(self) -> str:
        """Access the ``slot[slot].analogoutput.startchannel`` attribute.

        Description:
            - This attribute indicates the first channel in the specified slot that supports analog
              outputs.

        Usage:
            - Accessing this property will send the ``print(slot[slot].analogoutput.startchannel)``
              query.

        TSP Syntax:
            ```
            - print(slot[slot].analogoutput.startchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".startchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.startchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.startchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemAmps(BaseTSPCmd):
    """The ``slot[slot].amps`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.endchannel``: The ``slot[slot].amps.endchannel`` attribute.
        - ``.startchannel``: The ``slot[slot].amps.startchannel`` attribute.
    """

    @property
    def endchannel(self) -> str:
        """Access the ``slot[slot].amps.endchannel`` attribute.

        Description:
            - This attribute indicates the last channel in the specified slot that supports amps
              measurements.

        Usage:
            - Accessing this property will send the ``print(slot[slot].amps.endchannel)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].amps.endchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".endchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.endchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.endchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def startchannel(self) -> str:
        """Access the ``slot[slot].amps.startchannel`` attribute.

        Description:
            - This attribute indicates the first channel in the specified slot that supports current
              measurements.

        Usage:
            - Accessing this property will send the ``print(slot[slot].amps.startchannel)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].amps.startchannel)
            ```

        Info:
            - ``slot``, the slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".startchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.startchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.startchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[slot]`` command tree.

    Info:
        - ``slot``, the slot number.

    Properties and methods:
        - ``.amps``: The ``slot[slot].amps`` command tree.
        - ``.analogoutput``: The ``slot[slot].analogoutput`` command tree.
        - ``.commonsideohms``: The ``slot[slot].commonsideohms`` attribute.
        - ``.digitalio``: The ``slot[slot].digitalio`` command tree.
        - ``.idn``: The ``slot[slot].idn`` attribute.
        - ``.isolated``: The ``slot[slot].isolated`` command tree.
        - ``.matrix``: The ``slot[slot].matrix`` command tree.
        - ``.maxvoltage``: The ``slot[slot].maxvoltage`` attribute.
        - ``.pseudocard``: The ``slot[slot].pseudocard`` attribute.
        - ``.tempsensor``: The ``slot[slot].tempsensor`` attribute.
        - ``.totalizer``: The ``slot[slot].totalizer`` command tree.
        - ``.voltage``: The ``slot[slot].voltage`` command tree.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "slot[slot]"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._amps = SlotItemAmps(device, f"{self._cmd_syntax}.amps")
        self._analogoutput = SlotItemAnalogoutput(device, f"{self._cmd_syntax}.analogoutput")
        self._digitalio = SlotItemDigitalio(device, f"{self._cmd_syntax}.digitalio")
        self._isolated = SlotItemIsolated(device, f"{self._cmd_syntax}.isolated")
        self._matrix = SlotItemMatrix(device, f"{self._cmd_syntax}.matrix")
        self._totalizer = SlotItemTotalizer(device, f"{self._cmd_syntax}.totalizer")
        self._voltage = SlotItemVoltage(device, f"{self._cmd_syntax}.voltage")

    @property
    def amps(self) -> SlotItemAmps:
        """Return the ``slot[slot].amps`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.endchannel``: The ``slot[slot].amps.endchannel`` attribute.
            - ``.startchannel``: The ``slot[slot].amps.startchannel`` attribute.
        """
        return self._amps

    @property
    def analogoutput(self) -> SlotItemAnalogoutput:
        """Return the ``slot[slot].analogoutput`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.endchannel``: The ``slot[slot].analogoutput.endchannel`` attribute.
            - ``.startchannel``: The ``slot[slot].analogoutput.startchannel`` attribute.
        """
        return self._analogoutput

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
            - ``slot``, the slot number.

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
    def digitalio(self) -> SlotItemDigitalio:
        """Return the ``slot[slot].digitalio`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.endchannel``: The ``slot[slot].digitalio.endchannel`` attribute.
            - ``.startchannel``: The ``slot[slot].digitalio.startchannel`` attribute.
        """
        return self._digitalio

    @property
    def idn(self) -> str:
        """Access the ``slot[slot].idn`` attribute.

        Description:
            - This attribute returns a string that contains information about the switching module.

        Usage:
            - Accessing this property will send the ``print(slot[slot].idn)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].idn)
            ```

        Info:
            - ``slot``, the slot number (1 or 2).

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
    def isolated(self) -> SlotItemIsolated:
        """Return the ``slot[slot].isolated`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.endchannel``: The ``slot[slot].isolated.endchannel`` attribute.
            - ``.startchannel``: The ``slot[slot].isolated.startchannel`` attribute.
        """
        return self._isolated

    @property
    def matrix(self) -> SlotItemMatrix:
        """Return the ``slot[slot].matrix`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.columns``: The ``slot[slot].matrix.columns`` attribute.
            - ``.rows``: The ``slot[slot].matrix.rows`` attribute.
        """
        return self._matrix

    @property
    def maxvoltage(self) -> str:
        """Access the ``slot[slot].maxvoltage`` attribute.

        Description:
            - This attribute returns the maximum voltage of all channels on a switching module in
              the specified slot.

        Usage:
            - Accessing this property will send the ``print(slot[slot].maxvoltage)`` query.

        TSP Syntax:
            ```
            - print(slot[slot].maxvoltage)
            ```

        Info:
            - ``slot``, the slot number (1 or 2).

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
    def pseudocard(self) -> str:
        """Access the ``slot[slot].pseudocard`` attribute.

        Description:
            - This attribute specifies a pseudocard to implement for the designated slot.

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
            - ``slot``, the slot number (1 or 2).

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
            - This attribute specifies a pseudocard to implement for the designated slot.

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
            - ``slot``, the slot number (1 or 2).

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
            - ``slot``, the slot number.

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
    def totalizer(self) -> SlotItemTotalizer:
        """Return the ``slot[slot].totalizer`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.endchannel``: The ``slot[slot].totalizer.endchannel`` attribute.
            - ``.startchannel``: The ``slot[slot].totalizer.startchannel`` attribute.
        """
        return self._totalizer

    @property
    def voltage(self) -> SlotItemVoltage:
        """Return the ``slot[slot].voltage`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.endchannel``: The ``slot[slot].voltage.endchannel`` attribute.
            - ``.startchannel``: The ``slot[slot].voltage.startchannel`` attribute.
        """
        return self._voltage


# pylint: disable=too-few-public-methods
class Slot(BaseTSPCmd):
    """The ``slot`` command tree.

    Constants:
        - ``.PSEUDO_NONE``: No pseudocard.
    """

    PSEUDO_NONE = "slot.PSEUDO_NONE"
    """str: No pseudocard."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "slot") -> None:
        super().__init__(device, cmd_syntax)
