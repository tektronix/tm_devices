# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The status commands module.

These commands are used in the following models:
DMM6500, DMM7510

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - status.clear()
    - status.condition
    - status.operation.condition
    - status.operation.enable
    - status.operation.event
    - status.operation.getmap()
    - status.operation.setmap()
    - status.preset()
    - status.questionable.condition
    - status.questionable.enable
    - status.questionable.event
    - status.questionable.getmap()
    - status.questionable.setmap()
    - status.request_enable
    - status.standard.enable
    - status.standard.event
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class StatusStandard(BaseTSPCmd):
    """The ``status.standard`` command tree.

    Properties and methods:
        - ``.enable``: The ``status.standard.enable`` attribute.
        - ``.event``: The ``status.standard.event`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``status.standard.enable`` attribute.

        Description:
            - This attribute reads or sets the bits in the Status Enable register of the Standard
              Event Register.

        Usage:
            - Accessing this property will send the ``print(status.standard.enable)`` query.
            - Setting this property to a value will send the ``status.standard.enable = value``
              command.

        TSP Syntax:
            ```
            - status.standard.enable = value
            - print(status.standard.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``status.standard.enable`` attribute.

        Description:
            - This attribute reads or sets the bits in the Status Enable register of the Standard
              Event Register.

        Usage:
            - Accessing this property will send the ``print(status.standard.enable)`` query.
            - Setting this property to a value will send the ``status.standard.enable = value``
              command.

        TSP Syntax:
            ```
            - status.standard.enable = value
            - print(status.standard.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def event(self) -> str:
        """Access the ``status.standard.event`` attribute.

        Description:
            - This attribute returns the contents of the Standard Event Status Register set of the
              status model.

        Usage:
            - Accessing this property will send the ``print(status.standard.event)`` query.

        TSP Syntax:
            ```
            - print(status.standard.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusQuestionable(BaseTSPCmd):
    """The ``status.questionable`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.questionable.condition`` attribute.
        - ``.enable``: The ``status.questionable.enable`` attribute.
        - ``.event``: The ``status.questionable.event`` attribute.
        - ``.getmap()``: The ``status.questionable.getmap()`` function.
        - ``.setmap()``: The ``status.questionable.setmap()`` function.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.condition`` attribute.

        Description:
            - This attribute reads the Questionable Condition Register of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.questionable.enable`` attribute.

        Description:
            - This attribute sets or reads the contents of the questionable event enable register of
              the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.enable)`` query.
            - Setting this property to a value will send the ``status.questionable.enable = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.enable = value
            - print(status.questionable.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.enable`` attribute.

        Description:
            - This attribute sets or reads the contents of the questionable event enable register of
              the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.enable)`` query.
            - Setting this property to a value will send the ``status.questionable.enable = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.enable = value
            - print(status.questionable.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def event(self) -> str:
        """Access the ``status.questionable.event`` attribute.

        Description:
            - This attribute reads the Questionable Event Register.

        Usage:
            - Accessing this property will send the ``print(status.questionable.event)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getmap(self, bit_number: int) -> str:
        """Run the ``status.questionable.getmap()`` function.

        Description:
            - This function requests the mapped set event and mapped clear event status for a bit in
              the Questionable Event Registers.

        TSP Syntax:
            ```
            - status.questionable.getmap()
            ```

        Args:
            bit_number: The bit number to check (0 to 14).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getmap({bit_number}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getmap()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setmap(self, bit_number: int, set_event: int, clear_event: Optional[int] = None) -> None:
        """Run the ``status.questionable.setmap()`` function.

        Description:
            - This function maps events to bits in the questionable event registers.

        TSP Syntax:
            ```
            - status.questionable.setmap()
            ```

        Args:
            bit_number: The bit number that is mapped to an event (0 to 14).
            set_event: The number of the event that sets the bits in the condition and event
                registers; 0 if no mapping.
            clear_event (optional): The number of the event that clears the bit in the condition
                register; 0 if no mapping.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    bit_number,
                    set_event,
                    clear_event,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setmap({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setmap()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusOperation(BaseTSPCmd):
    """The ``status.operation`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.condition`` attribute.
        - ``.enable``: The ``status.operation.enable`` attribute.
        - ``.event``: The ``status.operation.event`` attribute.
        - ``.getmap()``: The ``status.operation.getmap()`` function.
        - ``.setmap()``: The ``status.operation.setmap()`` function.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.condition`` attribute.

        Description:
            - This attribute reads the Operation Event Register of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.operation.enable`` attribute.

        Description:
            - This attribute sets or reads the contents of the Operation Event Enable Register of
              the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.enable)`` query.
            - Setting this property to a value will send the ``status.operation.enable = value``
              command.

        TSP Syntax:
            ```
            - status.operation.enable = value
            - print(status.operation.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.enable`` attribute.

        Description:
            - This attribute sets or reads the contents of the Operation Event Enable Register of
              the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.enable)`` query.
            - Setting this property to a value will send the ``status.operation.enable = value``
              command.

        TSP Syntax:
            ```
            - status.operation.enable = value
            - print(status.operation.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def event(self) -> str:
        """Access the ``status.operation.event`` attribute.

        Description:
            - This attribute reads the Operation Event Register of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getmap(self, bit_number: int) -> str:
        """Run the ``status.operation.getmap()`` function.

        Description:
            - This function requests the mapped set event and mapped clear event status for a bit in
              the Operation Event Registers.

        TSP Syntax:
            ```
            - status.operation.getmap()
            ```

        Args:
            bit_number: The bit number to check.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getmap({bit_number}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getmap()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setmap(self, bit_number: int, set_event: int, clear_event: Optional[int] = None) -> None:
        """Run the ``status.operation.setmap()`` function.

        Description:
            - This function allows you to map events to bits in the Operation Event Register.

        TSP Syntax:
            ```
            - status.operation.setmap()
            ```

        Args:
            bit_number: The bit number that is mapped to an event (0 to 14).
            set_event: The number of the event that sets the bits in the condition and event
                registers; 0 if no mapping.
            clear_event (optional): The number of the event that clears the bit in the condition
                register; 0 if no mapping.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    bit_number,
                    set_event,
                    clear_event,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setmap({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setmap()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Status(BaseTSPCmd):
    """The ``status`` command tree.

    Properties and methods:
        - ``.clear()``: The ``status.clear()`` function.
        - ``.condition``: The ``status.condition`` attribute.
        - ``.operation``: The ``status.operation`` command tree.
        - ``.preset()``: The ``status.preset()`` function.
        - ``.questionable``: The ``status.questionable`` command tree.
        - ``.request_enable``: The ``status.request_enable`` attribute.
        - ``.standard``: The ``status.standard`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "status") -> None:
        super().__init__(device, cmd_syntax)
        self._operation = StatusOperation(device, f"{self._cmd_syntax}.operation")
        self._questionable = StatusQuestionable(device, f"{self._cmd_syntax}.questionable")
        self._standard = StatusStandard(device, f"{self._cmd_syntax}.standard")

    @property
    def condition(self) -> str:
        """Access the ``status.condition`` attribute.

        Description:
            - This attribute stores the status byte condition register.

        Usage:
            - Accessing this property will send the ``print(status.condition)`` query.

        TSP Syntax:
            ```
            - print(status.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def operation(self) -> StatusOperation:
        """Return the ``status.operation`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.condition`` attribute.
            - ``.enable``: The ``status.operation.enable`` attribute.
            - ``.event``: The ``status.operation.event`` attribute.
            - ``.getmap()``: The ``status.operation.getmap()`` function.
            - ``.setmap()``: The ``status.operation.setmap()`` function.
        """
        return self._operation

    @property
    def questionable(self) -> StatusQuestionable:
        """Return the ``status.questionable`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.condition`` attribute.
            - ``.enable``: The ``status.questionable.enable`` attribute.
            - ``.event``: The ``status.questionable.event`` attribute.
            - ``.getmap()``: The ``status.questionable.getmap()`` function.
            - ``.setmap()``: The ``status.questionable.setmap()`` function.
        """
        return self._questionable

    @property
    def request_enable(self) -> str:
        """Access the ``status.request_enable`` attribute.

        Description:
            - This attribute stores the settings of the Service Request (SRQ) Enable Register.

        Usage:
            - Accessing this property will send the ``print(status.request_enable)`` query.
            - Setting this property to a value will send the ``status.request_enable = value``
              command.

        TSP Syntax:
            ```
            - status.request_enable = value
            - print(status.request_enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".request_enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.request_enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.request_enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @request_enable.setter
    def request_enable(self, value: Union[str, float]) -> None:
        """Access the ``status.request_enable`` attribute.

        Description:
            - This attribute stores the settings of the Service Request (SRQ) Enable Register.

        Usage:
            - Accessing this property will send the ``print(status.request_enable)`` query.
            - Setting this property to a value will send the ``status.request_enable = value``
              command.

        TSP Syntax:
            ```
            - status.request_enable = value
            - print(status.request_enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".request_enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.request_enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.request_enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def standard(self) -> StatusStandard:
        """Return the ``status.standard`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``status.standard.enable`` attribute.
            - ``.event``: The ``status.standard.event`` attribute.
        """
        return self._standard

    def clear(self) -> None:
        """Run the ``status.clear()`` function.

        Description:
            - This function clears event registers.

        TSP Syntax:
            ```
            - status.clear()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clear()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.clear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def preset(self) -> None:
        """Run the ``status.preset()`` function.

        Description:
            - This function resets all bits in the status model.

        TSP Syntax:
            ```
            - status.preset()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.preset()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.preset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
