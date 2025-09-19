# ruff: noqa: PLR0913
# pyright: reportConstantRedefinition=none
"""The trigger commands module.

These commands are used in the following models:
MPSU50_2ST

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - trigger.model.abort()
    - trigger.model.addblock.branch.always()
    - trigger.model.addblock.branch.counter()
    - trigger.model.addblock.branch.once()
    - trigger.model.addblock.branch.onceexcluded()
    - trigger.model.addblock.configlist.next()
    - trigger.model.addblock.configlist.prev()
    - trigger.model.addblock.configlist.recall()
    - trigger.model.addblock.delay.constant()
    - trigger.model.addblock.logevent()
    - trigger.model.addblock.measure()
    - trigger.model.addblock.measureoverlapped()
    - trigger.model.addblock.nop()
    - trigger.model.addblock.reset.branch.counter()
    - trigger.model.addblock.source.action.bias()
    - trigger.model.addblock.source.action.skip()
    - trigger.model.addblock.source.action.step()
    - trigger.model.addblock.source.output()
    - trigger.model.addblock.wait()
    - trigger.model.create()
    - trigger.model.delete()
    - trigger.model.initiate()
    - trigger.model.removeblock()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class TriggerModelAddblockSourceAction(BaseTSPCmd):
    """The ``trigger.model.addblock.source.action`` command tree.

    Properties and methods:
        - ``.bias()``: The ``trigger.model.addblock.source.action.bias()`` function.
        - ``.skip()``: The ``trigger.model.addblock.source.action.skip()`` function.
        - ``.step()``: The ``trigger.model.addblock.source.action.step()`` function.
    """

    def bias(self, trigger_model_name: str, block_name: str, channel: str) -> None:
        """Run the ``trigger.model.addblock.source.action.bias()`` function.

        Description:
            - This function creates a block that sets the source output level to the bias level.

        TSP Syntax:
            ```
            - trigger.model.addblock.source.action.bias()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which this block is added.
            block_name: Name of the trigger block.
            channel: Channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.bias("{trigger_model_name}", "{block_name}", {channel})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.bias()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def skip(self, trigger_model_name: str, block_name: str, channel: str) -> None:
        """Run the ``trigger.model.addblock.source.action.skip()`` function.

        Description:
            - This function defines a trigger model block that skips a step in the sweep operation
              on the specified channel.

        TSP Syntax:
            ```
            - trigger.model.addblock.source.action.skip()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block is added.
            block_name: Name of the trigger block defining where to branch.
            channel: Channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.skip("{trigger_model_name}", "{block_name}", {channel})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.skip()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def step(self, trigger_model_name: str, block_name: str, channel: str) -> None:
        """Run the ``trigger.model.addblock.source.action.step()`` function.

        Description:
            - This function defines a trigger model block that advances the source output to the
              next point of the sweep for the specified channel.

        TSP Syntax:
            ```
            - trigger.model.addblock.source.action.step()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block is added.
            block_name: Name of the trigger block defining where to branch.
            channel: Channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.step("{trigger_model_name}", "{block_name}", {channel})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.step()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class TriggerModelAddblockSource(BaseTSPCmd):
    """The ``trigger.model.addblock.source`` command tree.

    Properties and methods:
        - ``.action``: The ``trigger.model.addblock.source.action`` command tree.
        - ``.output()``: The ``trigger.model.addblock.source.output()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._action = TriggerModelAddblockSourceAction(device, f"{self._cmd_syntax}.action")

    @property
    def action(self) -> TriggerModelAddblockSourceAction:
        """Return the ``trigger.model.addblock.source.action`` command tree.

        Sub-properties and sub-methods:
            - ``.bias()``: The ``trigger.model.addblock.source.action.bias()`` function.
            - ``.skip()``: The ``trigger.model.addblock.source.action.skip()`` function.
            - ``.step()``: The ``trigger.model.addblock.source.action.step()`` function.
        """
        return self._action

    def output(self, trigger_model_name: str, block_name: str, channel: str, state: str) -> None:
        """Run the ``trigger.model.addblock.source.output()`` function.

        Description:
            - This function defines a trigger model block that turns the output source on or off.

        TSP Syntax:
            ```
            - trigger.model.addblock.source.output()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the trigger block to be added.
            channel: Module channel number.
            state: Turn the source off.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.output("{trigger_model_name}", '
                f'"{block_name}", '
                f"{channel}, "
                f"{state})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.output()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class TriggerModelAddblockResetBranch(BaseTSPCmd):
    """The ``trigger.model.addblock.reset.branch`` command tree.

    Properties and methods:
        - ``.counter()``: The ``trigger.model.addblock.reset.branch.counter()`` function.
    """

    def counter(
        self, trigger_model_name: str, block_name: str, reset_branch_count_block_name: str
    ) -> None:
        """Run the ``trigger.model.addblock.reset.branch.counter()`` function.

        Description:
            - This function defines a trigger model block that resets the count for a branch counter
              block.

        TSP Syntax:
            ```
            - trigger.model.addblock.reset.branch.counter()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the block to be added.
            reset_branch_count_block_name: Name of the branch counter block to reset the count value
                to 0.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.counter("{trigger_model_name}", '
                f'"{block_name}", '
                f'"{reset_branch_count_block_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.counter()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class TriggerModelAddblockReset(BaseTSPCmd):
    """The ``trigger.model.addblock.reset`` command tree.

    Properties and methods:
        - ``.branch``: The ``trigger.model.addblock.reset.branch`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._branch = TriggerModelAddblockResetBranch(device, f"{self._cmd_syntax}.branch")

    @property
    def branch(self) -> TriggerModelAddblockResetBranch:
        """Return the ``trigger.model.addblock.reset.branch`` command tree.

        Sub-properties and sub-methods:
            - ``.counter()``: The ``trigger.model.addblock.reset.branch.counter()`` function.
        """
        return self._branch


class TriggerModelAddblockDelay(BaseTSPCmd):
    """The ``trigger.model.addblock.delay`` command tree.

    Properties and methods:
        - ``.constant()``: The ``trigger.model.addblock.delay.constant()`` function.
    """

    def constant(
        self,
        trigger_model_name: str,
        block_name: str,
        delay_time: Optional[str] = None,
        reference_block_name: Optional[str] = None,
    ) -> None:
        """Run the ``trigger.model.addblock.delay.constant()`` function.

        Description:
            - This function adds a constant delay to the execution of a trigger model.

        TSP Syntax:
            ```
            - trigger.model.addblock.delay.constant()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the trigger block where execution will proceed when the evaluation
                result is true.
            delay_time (optional): Time delay as a positive value.
            reference_block_name (optional): Trigger model block to use for the start time of the
                delay; see Details.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{trigger_model_name}"',
                    f'"{block_name}"',
                    delay_time,
                    f'"{reference_block_name}"' if reference_block_name is not None else None,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.constant({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.constant()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class TriggerModelAddblockConfiglist(BaseTSPCmd):
    """The ``trigger.model.addblock.configlist`` command tree.

    Properties and methods:
        - ``.next()``: The ``trigger.model.addblock.configlist.next()`` function.
        - ``.prev()``: The ``trigger.model.addblock.configlist.prev()`` function.
        - ``.recall()``: The ``trigger.model.addblock.configlist.recall()`` function.
    """

    def next(
        self, trigger_model_name: str, block_name: str, channel: str, configlist_name: str
    ) -> None:
        """Run the ``trigger.model.addblock.configlist.next()`` function.

        Description:
            - This function recalls the settings at the next index of a configuration list.

        TSP Syntax:
            ```
            - trigger.model.addblock.configlist.next()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the block to be added.
            channel: Module channel number.
            configlist_name: A string that defines the configuration list to recall.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.next("{trigger_model_name}", '
                f'"{block_name}", '
                f"{channel}, "
                f'"{configlist_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.next()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def prev(
        self, trigger_model_name: str, block_name: str, channel: str, configlist_name: str
    ) -> None:
        """Run the ``trigger.model.addblock.configlist.prev()`` function.

        Description:
            - This function defines a trigger model block that recalls the settings stored at the
              previous index in a configuration list.

        TSP Syntax:
            ```
            - trigger.model.addblock.configlist.prev()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the block to be added.
            channel: Module channel number.
            configlist_name: A string that defines the configuration list to recall.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.prev("{trigger_model_name}", '
                f'"{block_name}", '
                f"{channel}, "
                f'"{configlist_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.prev()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def recall(
        self,
        trigger_model_name: str,
        block_name: str,
        channel: str,
        configlist_name: str,
        index: int,
    ) -> None:
        """Run the ``trigger.model.addblock.configlist.recall()`` function.

        Description:
            - This function recalls the system settings that are stored in a configuration list.

        TSP Syntax:
            ```
            - trigger.model.addblock.configlist.recall()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the block to be added.
            channel: Module channel number.
            configlist_name: A string that defines the configuration list to recall.
            index: The index in the configuration list to recall; default is 1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.recall("{trigger_model_name}", '
                f'"{block_name}", '
                f"{channel}, "
                f'"{configlist_name}", '
                f"{index})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recall()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class TriggerModelAddblockBranch(BaseTSPCmd):
    """The ``trigger.model.addblock.branch`` command tree.

    Properties and methods:
        - ``.always()``: The ``trigger.model.addblock.branch.always()`` function.
        - ``.counter()``: The ``trigger.model.addblock.branch.counter()`` function.
        - ``.once()``: The ``trigger.model.addblock.branch.once()`` function.
        - ``.onceexcluded()``: The ``trigger.model.addblock.branch.onceexcluded()`` function.
    """

    def always(self, trigger_model_name: str, block_name: str, branch_to_block_name: str) -> None:
        """Run the ``trigger.model.addblock.branch.always()`` function.

        Description:
            - This function defines a trigger model block that always branches to a specific block.

        TSP Syntax:
            ```
            - trigger.model.addblock.branch.always()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the block to be added.
            branch_to_block_name: Name of the next trigger block to run.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.always("{trigger_model_name}", '
                f'"{block_name}", '
                f'"{branch_to_block_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.always()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def counter(
        self, trigger_model_name: str, block_name: str, branch_to_block_name: str, target_count: str
    ) -> None:
        """Run the ``trigger.model.addblock.branch.counter()`` function.

        Description:
            - This function defines a trigger model block that branches to a block a specified
              number of times.

        TSP Syntax:
            ```
            - trigger.model.addblock.branch.counter()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the block to be added.
            branch_to_block_name: Name of the next block to run.
            target_count: Number of times to repeat the branch.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.counter("{trigger_model_name}", '
                f'"{block_name}", '
                f'"{branch_to_block_name}", '
                f"{target_count})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.counter()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def once(self, trigger_model_name: str, block_name: str, branch_to_block_name: str) -> None:
        """Run the ``trigger.model.addblock.branch.once()`` function.

        Description:
            - This function causes the trigger model to branch to a specified trigger model block
              the first time it is encountered in the trigger model.

        TSP Syntax:
            ```
            - trigger.model.addblock.branch.once()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block is added.
            block_name: Name of the trigger block.
            branch_to_block_name: Name of the block to branch to on the first pass through this
                block.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.once("{trigger_model_name}", '
                f'"{block_name}", '
                f'"{branch_to_block_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.once()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def onceexcluded(
        self, trigger_model_name: str, block_name: str, branch_to_block_name: str
    ) -> None:
        """Run the ``trigger.model.addblock.branch.onceexcluded()`` function.

        Description:
            - This function causes the trigger model to branch to a specified trigger model block
              every time it is encountered in the trigger model except for the first time.

        TSP Syntax:
            ```
            - trigger.model.addblock.branch.onceexcluded()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block is added.
            block_name: Name of the trigger block.
            branch_to_block_name: Name of the block to branch to on the first pass through this
                block.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.onceexcluded("{trigger_model_name}", '
                f'"{block_name}", '
                f'"{branch_to_block_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.onceexcluded()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class TriggerModelAddblock(BaseTSPCmd):
    """The ``trigger.model.addblock`` command tree.

    Properties and methods:
        - ``.branch``: The ``trigger.model.addblock.branch`` command tree.
        - ``.configlist``: The ``trigger.model.addblock.configlist`` command tree.
        - ``.delay``: The ``trigger.model.addblock.delay`` command tree.
        - ``.logevent()``: The ``trigger.model.addblock.logevent()`` function.
        - ``.measure()``: The ``trigger.model.addblock.measure()`` function.
        - ``.measureoverlapped()``: The ``trigger.model.addblock.measureoverlapped()`` function.
        - ``.nop()``: The ``trigger.model.addblock.nop()`` function.
        - ``.reset``: The ``trigger.model.addblock.reset`` command tree.
        - ``.source``: The ``trigger.model.addblock.source`` command tree.
        - ``.wait()``: The ``trigger.model.addblock.wait()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._branch = TriggerModelAddblockBranch(device, f"{self._cmd_syntax}.branch")
        self._configlist = TriggerModelAddblockConfiglist(device, f"{self._cmd_syntax}.configlist")
        self._delay = TriggerModelAddblockDelay(device, f"{self._cmd_syntax}.delay")
        self._reset = TriggerModelAddblockReset(device, f"{self._cmd_syntax}.reset")
        self._source = TriggerModelAddblockSource(device, f"{self._cmd_syntax}.source")

    @property
    def branch(self) -> TriggerModelAddblockBranch:
        """Return the ``trigger.model.addblock.branch`` command tree.

        Sub-properties and sub-methods:
            - ``.always()``: The ``trigger.model.addblock.branch.always()`` function.
            - ``.counter()``: The ``trigger.model.addblock.branch.counter()`` function.
            - ``.once()``: The ``trigger.model.addblock.branch.once()`` function.
            - ``.onceexcluded()``: The ``trigger.model.addblock.branch.onceexcluded()`` function.
        """
        return self._branch

    @property
    def configlist(self) -> TriggerModelAddblockConfiglist:
        """Return the ``trigger.model.addblock.configlist`` command tree.

        Sub-properties and sub-methods:
            - ``.next()``: The ``trigger.model.addblock.configlist.next()`` function.
            - ``.prev()``: The ``trigger.model.addblock.configlist.prev()`` function.
            - ``.recall()``: The ``trigger.model.addblock.configlist.recall()`` function.
        """
        return self._configlist

    @property
    def delay(self) -> TriggerModelAddblockDelay:
        """Return the ``trigger.model.addblock.delay`` command tree.

        Sub-properties and sub-methods:
            - ``.constant()``: The ``trigger.model.addblock.delay.constant()`` function.
        """
        return self._delay

    @property
    def reset(self) -> TriggerModelAddblockReset:
        """Return the ``trigger.model.addblock.reset`` command tree.

        Sub-properties and sub-methods:
            - ``.branch``: The ``trigger.model.addblock.reset.branch`` command tree.
        """
        return self._reset

    @property
    def source(self) -> TriggerModelAddblockSource:
        """Return the ``trigger.model.addblock.source`` command tree.

        Sub-properties and sub-methods:
            - ``.action``: The ``trigger.model.addblock.source.action`` command tree.
            - ``.output()``: The ``trigger.model.addblock.source.output()`` function.
        """
        return self._source

    def logevent(
        self, trigger_model_name: str, block_name: str, event_number: int, message: str
    ) -> None:
        """Run the ``trigger.model.addblock.logevent()`` function.

        Description:
            - This function allows you to log an event in the event log when the trigger model is
              running.

        TSP Syntax:
            ```
            - trigger.model.addblock.logevent()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the block to be added.
            event_number: The event number.
            message: A string up to 31 characters.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.logevent("{trigger_model_name}", '
                f'"{block_name}", '
                f"{event_number}, "
                f'"{message}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.logevent()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measure(
        self, trigger_model_name: str, block_name: str, channel: str, count: Optional[str] = None
    ) -> None:
        """Run the ``trigger.model.addblock.measure()`` function.

        Description:
            - This function defines a trigger block that makes a measurement.

        TSP Syntax:
            ```
            - trigger.model.addblock.measure()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the trigger block.
            channel: Channel list, specified in a table; for example.
            count (optional): Number of measurements to make when this block is executed.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{trigger_model_name}"',
                    f'"{block_name}"',
                    channel,
                    count,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.measure({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measure()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measureoverlapped(
        self, trigger_model_name: str, block_name: str, channel: str, count: Optional[str] = None
    ) -> None:
        """Run the ``trigger.model.addblock.measureoverlapped()`` function.

        Description:
            - This function defines a trigger-model block that makes a measurement in an overlapped
              mode which allows you to measure the response of the device under test while the
              source is being stepped.

        TSP Syntax:
            ```
            - trigger.model.addblock.measureoverlapped()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the trigger block.
            channel: Module channel number to measure.
            count (optional): Number of measurements to make when this block starts.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{trigger_model_name}"',
                    f'"{block_name}"',
                    channel,
                    count,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.measureoverlapped({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measureoverlapped()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def nop(self, trigger_model_name: str, block_name: str) -> None:
        """Run the ``trigger.model.addblock.nop()`` function.

        Description:
            - This function creates a placeholder block that performs no action in the trigger
              model.

        TSP Syntax:
            ```
            - trigger.model.addblock.nop()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the trigger block.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.nop("{trigger_model_name}", "{block_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.nop()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments
    def wait(
        self,
        trigger_model_name: str,
        block_name: str,
        event: str,
        clear: Optional[str] = None,
        logic: Optional[str] = None,
        event_2: Optional[str] = None,
        event_3: Optional[str] = None,
        event_4: Optional[str] = None,
    ) -> None:
        """Run the ``trigger.model.addblock.wait()`` function.

        Description:
            - This function defines a trigger model block that waits for an event before allowing
              the trigger model to continue.

        TSP Syntax:
            ```
            - trigger.model.addblock.wait()
            ```

        Args:
            trigger_model_name: Name of the trigger model to which the block will be added.
            block_name: Name of the trigger block being added by this command.
            event: The event that must occur before the trigger block allows trigger execution to
                continue (see Details).
            clear (optional): To clear previously detected trigger events when entering the wait
                block.
            logic (optional): If each event must occur before the trigger model continues.
            event_2 (optional): The event that must occur before the trigger block allows trigger
                execution to continue (see Details).
            event_3 (optional): The event that must occur before the trigger block allows trigger
                execution to continue (see Details).
            event_4 (optional): The event that must occur before the trigger block allows trigger
                execution to continue (see Details).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{trigger_model_name}"',
                    f'"{block_name}"',
                    event,
                    clear,
                    logic,
                    event_2,
                    event_3,
                    event_4,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.wait({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.wait()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class TriggerModel(BaseTSPCmd):
    """The ``trigger.model`` command tree.

    Properties and methods:
        - ``.abort()``: The ``trigger.model.abort()`` function.
        - ``.addblock``: The ``trigger.model.addblock`` command tree.
        - ``.create()``: The ``trigger.model.create()`` function.
        - ``.delete()``: The ``trigger.model.delete()`` function.
        - ``.initiate()``: The ``trigger.model.initiate()`` function.
        - ``.removeblock()``: The ``trigger.model.removeblock()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._addblock = TriggerModelAddblock(device, f"{self._cmd_syntax}.addblock")

    @property
    def addblock(self) -> TriggerModelAddblock:
        """Return the ``trigger.model.addblock`` command tree.

        Sub-properties and sub-methods:
            - ``.branch``: The ``trigger.model.addblock.branch`` command tree.
            - ``.configlist``: The ``trigger.model.addblock.configlist`` command tree.
            - ``.delay``: The ``trigger.model.addblock.delay`` command tree.
            - ``.logevent()``: The ``trigger.model.addblock.logevent()`` function.
            - ``.measure()``: The ``trigger.model.addblock.measure()`` function.
            - ``.measureoverlapped()``: The ``trigger.model.addblock.measureoverlapped()`` function.
            - ``.nop()``: The ``trigger.model.addblock.nop()`` function.
            - ``.reset``: The ``trigger.model.addblock.reset`` command tree.
            - ``.source``: The ``trigger.model.addblock.source`` command tree.
            - ``.wait()``: The ``trigger.model.addblock.wait()`` function.
        """
        return self._addblock

    def abort(self, trigger_model_name: str) -> None:
        """Run the ``trigger.model.abort()`` function.

        Description:
            - This function stops trigger model execution on the specified module.

        TSP Syntax:
            ```
            - trigger.model.abort()
            ```

        Args:
            trigger_model_name: Name of the trigger model to abort.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.abort("{trigger_model_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.abort()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def create(self, trigger_model_name: str) -> None:
        """Run the ``trigger.model.create()`` function.

        Description:
            - This function creates a trigger model.

        TSP Syntax:
            ```
            - trigger.model.create()
            ```

        Args:
            trigger_model_name: Name of the trigger model to create.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.create("{trigger_model_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.create()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, trigger_model_name: str) -> None:
        """Run the ``trigger.model.delete()`` function.

        Description:
            - This function deletes a trigger model.

        TSP Syntax:
            ```
            - trigger.model.delete()
            ```

        Args:
            trigger_model_name: Name of the trigger model to delete.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.delete("{trigger_model_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def initiate(self, trigger_model_name: str) -> None:
        """Run the ``trigger.model.initiate()`` function.

        Description:
            - This function starts a specified trigger model on a module.

        TSP Syntax:
            ```
            - trigger.model.initiate()
            ```

        Args:
            trigger_model_name: Name of the trigger model to start.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.initiate("{trigger_model_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.initiate()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def removeblock(self, trigger_model_name: str, trigger_block_name: str) -> None:
        """Run the ``trigger.model.removeblock()`` function.

        Description:
            - This function removes the trigger block from the trigger model.

        TSP Syntax:
            ```
            - trigger.model.removeblock()
            ```

        Args:
            trigger_model_name: Name of the trigger model from which this trigger block will be
                removed.
            trigger_block_name: Unique name of the trigger block to remove; this string cannot be
                empty.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.removeblock("{trigger_model_name}", "{trigger_block_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.removeblock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Trigger(BaseTSPCmd):
    """The ``trigger`` command tree.

    Properties and methods:
        - ``.model``: The ``trigger.model`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "trigger") -> None:
        super().__init__(device, cmd_syntax)
        self._model = TriggerModel(device, f"{self._cmd_syntax}.model")

    @property
    def model(self) -> TriggerModel:
        """Return the ``trigger.model`` command tree.

        Sub-properties and sub-methods:
            - ``.abort()``: The ``trigger.model.abort()`` function.
            - ``.addblock``: The ``trigger.model.addblock`` command tree.
            - ``.create()``: The ``trigger.model.create()`` function.
            - ``.delete()``: The ``trigger.model.delete()`` function.
            - ``.initiate()``: The ``trigger.model.initiate()`` function.
            - ``.removeblock()``: The ``trigger.model.removeblock()`` function.
        """
        return self._model
