# ruff: noqa: PLR0913
# pyright: reportConstantRedefinition=none
"""The slot commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - slot[Z].firmware.update()
    - slot[Z].firmware.verify()
    - slot[Z].license
    - slot[Z].manufacturer
    - slot[Z].model
    - slot[Z].psu[X].abort()
    - slot[Z].psu[X].configlist.create()
    - slot[Z].psu[X].configlist.delete()
    - slot[Z].psu[X].configlist.query()
    - slot[Z].psu[X].configlist.recall()
    - slot[Z].psu[X].configlist.size()
    - slot[Z].psu[X].configlist.store()
    - slot[Z].psu[X].configlist.table()
    - slot[Z].psu[X].defbuffer1
    - slot[Z].psu[X].defbuffer2
    - slot[Z].psu[X].makebuffer()
    - slot[Z].psu[X].measure.Y()
    - slot[Z].psu[X].measure.aperture
    - slot[Z].psu[X].measure.count
    - slot[Z].psu[X].measure.nplc
    - slot[Z].psu[X].measure.overlappedY()
    - slot[Z].psu[X].measure.rangei
    - slot[Z].psu[X].measure.rangev
    - slot[Z].psu[X].measure.rate
    - slot[Z].psu[X].measure.rel.enablei
    - slot[Z].psu[X].measure.rel.enablep
    - slot[Z].psu[X].measure.rel.enabler
    - slot[Z].psu[X].measure.rel.enablev
    - slot[Z].psu[X].measure.rel.leveli
    - slot[Z].psu[X].measure.rel.levelp
    - slot[Z].psu[X].measure.rel.levelr
    - slot[Z].psu[X].measure.rel.levelv
    - slot[Z].psu[X].measure.tempcomp
    - slot[Z].psu[X].overlapped
    - slot[Z].psu[X].reset()
    - slot[Z].psu[X].source.constantcurrent
    - slot[Z].psu[X].source.levelv
    - slot[Z].psu[X].source.limiti
    - slot[Z].psu[X].source.offmode
    - slot[Z].psu[X].source.output
    - slot[Z].psu[X].source.protect.enablei
    - slot[Z].psu[X].source.protect.enablev
    - slot[Z].psu[X].source.protect.leveli
    - slot[Z].psu[X].source.protect.levelv
    - slot[Z].psu[X].source.protect.trippedi
    - slot[Z].psu[X].source.protect.trippedv
    - slot[Z].psu[X].source.rangev
    - slot[Z].psu[X].source.slewratev
    - slot[Z].psu[X].trigger.measure.Y()
    - slot[Z].psu[X].trigger.source.linearY()
    - slot[Z].psu[X].trigger.source.listY()
    - slot[Z].psu[X].trigger.source.logY()
    - slot[Z].psu[X].waitcomplete()
    - slot[Z].serialno
    - slot[Z].smu[X].abort()
    - slot[Z].smu[X].configlist.create()
    - slot[Z].smu[X].configlist.delete()
    - slot[Z].smu[X].configlist.query()
    - slot[Z].smu[X].configlist.recall()
    - slot[Z].smu[X].configlist.size()
    - slot[Z].smu[X].configlist.store()
    - slot[Z].smu[X].configlist.table()
    - slot[Z].smu[X].contact.calibratehi()
    - slot[Z].smu[X].contact.calibratelo()
    - slot[Z].smu[X].contact.check()
    - slot[Z].smu[X].contact.getcalhi()
    - slot[Z].smu[X].contact.r()
    - slot[Z].smu[X].contact.speed
    - slot[Z].smu[X].contact.threshold
    - slot[Z].smu[X].defbuffer1
    - slot[Z].smu[X].defbuffer2
    - slot[Z].smu[X].guard.v()
    - slot[Z].smu[X].makebuffer()
    - slot[Z].smu[X].measure.Y()
    - slot[Z].smu[X].measure.aperture
    - slot[Z].smu[X].measure.autodelay
    - slot[Z].smu[X].measure.autorangei
    - slot[Z].smu[X].measure.autorangev
    - slot[Z].smu[X].measure.count
    - slot[Z].smu[X].measure.delay
    - slot[Z].smu[X].measure.interval
    - slot[Z].smu[X].measure.lowrangei
    - slot[Z].smu[X].measure.lowrangev
    - slot[Z].smu[X].measure.nplc
    - slot[Z].smu[X].measure.overlappedY()
    - slot[Z].smu[X].measure.rangei
    - slot[Z].smu[X].measure.rangev
    - slot[Z].smu[X].measure.rel.enablei
    - slot[Z].smu[X].measure.rel.enablep
    - slot[Z].smu[X].measure.rel.enabler
    - slot[Z].smu[X].measure.rel.enablev
    - slot[Z].smu[X].measure.rel.leveli
    - slot[Z].smu[X].measure.rel.levelp
    - slot[Z].smu[X].measure.rel.levelr
    - slot[Z].smu[X].measure.rel.levelv
    - slot[Z].smu[X].measure.tempcomp
    - slot[Z].smu[X].overlapped
    - slot[Z].smu[X].reset()
    - slot[Z].smu[X].sense
    - slot[Z].smu[X].source.autodelay
    - slot[Z].smu[X].source.autorangei
    - slot[Z].smu[X].source.autorangev
    - slot[Z].smu[X].source.constantcurrent
    - slot[Z].smu[X].source.delay
    - slot[Z].smu[X].source.func
    - slot[Z].smu[X].source.leveli
    - slot[Z].smu[X].source.levelv
    - slot[Z].smu[X].source.limiti
    - slot[Z].smu[X].source.limitni
    - slot[Z].smu[X].source.limitnv
    - slot[Z].smu[X].source.limitpi
    - slot[Z].smu[X].source.limitpv
    - slot[Z].smu[X].source.limitv
    - slot[Z].smu[X].source.lowrangei
    - slot[Z].smu[X].source.lowrangev
    - slot[Z].smu[X].source.offfunc
    - slot[Z].smu[X].source.offlimiti
    - slot[Z].smu[X].source.offlimitni
    - slot[Z].smu[X].source.offlimitnv
    - slot[Z].smu[X].source.offlimitpi
    - slot[Z].smu[X].source.offlimitpv
    - slot[Z].smu[X].source.offlimitv
    - slot[Z].smu[X].source.offmode
    - slot[Z].smu[X].source.output
    - slot[Z].smu[X].source.rangei
    - slot[Z].smu[X].source.rangev
    - slot[Z].smu[X].trigger.measure.Y()
    - slot[Z].smu[X].trigger.source.linearY()
    - slot[Z].smu[X].trigger.source.listY()
    - slot[Z].smu[X].trigger.source.logY()
    - slot[Z].smu[X].waitcomplete()
    - slot[Z].status.measurement.condition
    - slot[Z].status.measurement.current_limit.condition
    - slot[Z].status.measurement.current_limit.enable
    - slot[Z].status.measurement.current_limit.event
    - slot[Z].status.measurement.current_limit.ntr
    - slot[Z].status.measurement.current_limit.ptr
    - slot[Z].status.measurement.enable
    - slot[Z].status.measurement.event
    - slot[Z].status.measurement.instrument.condition
    - slot[Z].status.measurement.instrument.enable
    - slot[Z].status.measurement.instrument.event
    - slot[Z].status.measurement.instrument.ntr
    - slot[Z].status.measurement.instrument.psu[X].condition
    - slot[Z].status.measurement.instrument.psu[X].enable
    - slot[Z].status.measurement.instrument.psu[X].event
    - slot[Z].status.measurement.instrument.psu[X].ntr
    - slot[Z].status.measurement.instrument.psu[X].ptr
    - slot[Z].status.measurement.instrument.ptr
    - slot[Z].status.measurement.instrument.smu[X].condition
    - slot[Z].status.measurement.instrument.smu[X].enable
    - slot[Z].status.measurement.instrument.smu[X].event
    - slot[Z].status.measurement.instrument.smu[X].ntr
    - slot[Z].status.measurement.instrument.smu[X].ptr
    - slot[Z].status.measurement.ntr
    - slot[Z].status.measurement.protection.condition
    - slot[Z].status.measurement.protection.enable
    - slot[Z].status.measurement.protection.event
    - slot[Z].status.measurement.protection.ntr
    - slot[Z].status.measurement.protection.ptr
    - slot[Z].status.measurement.ptr
    - slot[Z].status.measurement.reading_overflow.condition
    - slot[Z].status.measurement.reading_overflow.enable
    - slot[Z].status.measurement.reading_overflow.event
    - slot[Z].status.measurement.reading_overflow.ntr
    - slot[Z].status.measurement.reading_overflow.ptr
    - slot[Z].status.measurement.voltage_limit.condition
    - slot[Z].status.measurement.voltage_limit.enable
    - slot[Z].status.measurement.voltage_limit.event
    - slot[Z].status.measurement.voltage_limit.ntr
    - slot[Z].status.measurement.voltage_limit.ptr
    - slot[Z].status.operation.calibrating.condition
    - slot[Z].status.operation.calibrating.enable
    - slot[Z].status.operation.calibrating.event
    - slot[Z].status.operation.calibrating.ntr
    - slot[Z].status.operation.calibrating.ptr
    - slot[Z].status.operation.condition
    - slot[Z].status.operation.enable
    - slot[Z].status.operation.event
    - slot[Z].status.operation.instrument.condition
    - slot[Z].status.operation.instrument.enable
    - slot[Z].status.operation.instrument.event
    - slot[Z].status.operation.instrument.ntr
    - slot[Z].status.operation.instrument.psu[X].condition
    - slot[Z].status.operation.instrument.psu[X].enable
    - slot[Z].status.operation.instrument.psu[X].event
    - slot[Z].status.operation.instrument.psu[X].ntr
    - slot[Z].status.operation.instrument.psu[X].ptr
    - slot[Z].status.operation.instrument.ptr
    - slot[Z].status.operation.instrument.smu[X].condition
    - slot[Z].status.operation.instrument.smu[X].enable
    - slot[Z].status.operation.instrument.smu[X].event
    - slot[Z].status.operation.instrument.smu[X].ntr
    - slot[Z].status.operation.instrument.smu[X].ptr
    - slot[Z].status.operation.measuring.condition
    - slot[Z].status.operation.measuring.enable
    - slot[Z].status.operation.measuring.event
    - slot[Z].status.operation.measuring.ntr
    - slot[Z].status.operation.measuring.ptr
    - slot[Z].status.operation.ntr
    - slot[Z].status.operation.ptr
    - slot[Z].status.operation.sweeping.condition
    - slot[Z].status.operation.sweeping.enable
    - slot[Z].status.operation.sweeping.event
    - slot[Z].status.operation.sweeping.ntr
    - slot[Z].status.operation.sweeping.ptr
    - slot[Z].status.questionable.calibration.condition
    - slot[Z].status.questionable.calibration.enable
    - slot[Z].status.questionable.calibration.event
    - slot[Z].status.questionable.calibration.ntr
    - slot[Z].status.questionable.calibration.ptr
    - slot[Z].status.questionable.condition
    - slot[Z].status.questionable.enable
    - slot[Z].status.questionable.event
    - slot[Z].status.questionable.instrument.condition
    - slot[Z].status.questionable.instrument.enable
    - slot[Z].status.questionable.instrument.event
    - slot[Z].status.questionable.instrument.ntr
    - slot[Z].status.questionable.instrument.psu[X].condition
    - slot[Z].status.questionable.instrument.psu[X].enable
    - slot[Z].status.questionable.instrument.psu[X].event
    - slot[Z].status.questionable.instrument.psu[X].ntr
    - slot[Z].status.questionable.instrument.psu[X].ptr
    - slot[Z].status.questionable.instrument.ptr
    - slot[Z].status.questionable.instrument.smu[X].condition
    - slot[Z].status.questionable.instrument.smu[X].enable
    - slot[Z].status.questionable.instrument.smu[X].event
    - slot[Z].status.questionable.instrument.smu[X].ntr
    - slot[Z].status.questionable.instrument.smu[X].ptr
    - slot[Z].status.questionable.ntr
    - slot[Z].status.questionable.over_temperature.condition
    - slot[Z].status.questionable.over_temperature.enable
    - slot[Z].status.questionable.over_temperature.event
    - slot[Z].status.questionable.over_temperature.ntr
    - slot[Z].status.questionable.over_temperature.ptr
    - slot[Z].status.questionable.ptr
    - slot[Z].status.reset()
    - slot[Z].trigger.model.abort()
    - slot[Z].trigger.model.addblock.branch.always()
    - slot[Z].trigger.model.addblock.branch.counter()
    - slot[Z].trigger.model.addblock.branch.once()
    - slot[Z].trigger.model.addblock.branch.onceexcluded()
    - slot[Z].trigger.model.addblock.configlist.next()
    - slot[Z].trigger.model.addblock.configlist.prev()
    - slot[Z].trigger.model.addblock.configlist.recall()
    - slot[Z].trigger.model.addblock.delay.constant()
    - slot[Z].trigger.model.addblock.logevent()
    - slot[Z].trigger.model.addblock.measure()
    - slot[Z].trigger.model.addblock.measureoverlapped()
    - slot[Z].trigger.model.addblock.nop()
    - slot[Z].trigger.model.addblock.reset.branch.counter()
    - slot[Z].trigger.model.addblock.source.action.bias()
    - slot[Z].trigger.model.addblock.source.action.skip()
    - slot[Z].trigger.model.addblock.source.action.step()
    - slot[Z].trigger.model.addblock.source.output()
    - slot[Z].trigger.model.addblock.wait()
    - slot[Z].trigger.model.create()
    - slot[Z].trigger.model.delete()
    - slot[Z].trigger.model.initiate()
    - slot[Z].trigger.model.removeblock()
    - slot[Z].trigger.model.state()
    - slot[Z].version
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from ..gen_4dh8ja_mpmpsumsmu.buffervar import Buffervar
from ..helpers import (
    BaseTSPCmd,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class SlotItemTriggerModelAddblockSourceAction(BaseTSPCmd):
    """The ``slot[Z].trigger.model.addblock.source.action`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.bias()``: The ``slot[Z].trigger.model.addblock.source.action.bias()`` function.
        - ``.skip()``: The ``slot[Z].trigger.model.addblock.source.action.skip()`` function.
        - ``.step()``: The ``slot[Z].trigger.model.addblock.source.action.step()`` function.
    """

    def bias(self, trigger_model_name: str, block_name: str, channel: str) -> None:
        """Run the ``slot[Z].trigger.model.addblock.source.action.bias()`` function.

        Description:
            - This function creates a block that sets the source output level to the bias level.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.source.action.bias()
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
        """Run the ``slot[Z].trigger.model.addblock.source.action.skip()`` function.

        Description:
            - This function defines a trigger model block that skips a step in the sweep operation
              on the specified channel.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.source.action.skip()
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
        """Run the ``slot[Z].trigger.model.addblock.source.action.step()`` function.

        Description:
            - This function defines a trigger model block that advances the source output to the
              next point of the sweep for the specified channel.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.source.action.step()
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


class SlotItemTriggerModelAddblockSource(BaseTSPCmd):
    """The ``slot[Z].trigger.model.addblock.source`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.action``: The ``slot[Z].trigger.model.addblock.source.action`` command tree.
        - ``.output()``: The ``slot[Z].trigger.model.addblock.source.output()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._action = SlotItemTriggerModelAddblockSourceAction(
            device, f"{self._cmd_syntax}.action"
        )

    @property
    def action(self) -> SlotItemTriggerModelAddblockSourceAction:
        """Return the ``slot[Z].trigger.model.addblock.source.action`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.bias()``: The ``slot[Z].trigger.model.addblock.source.action.bias()`` function.
            - ``.skip()``: The ``slot[Z].trigger.model.addblock.source.action.skip()`` function.
            - ``.step()``: The ``slot[Z].trigger.model.addblock.source.action.step()`` function.
        """
        return self._action

    def output(self, trigger_model_name: str, block_name: str, channel: str, state: str) -> None:
        """Run the ``slot[Z].trigger.model.addblock.source.output()`` function.

        Description:
            - This function defines a trigger model block that turns the output source on or off.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.source.output()
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


class SlotItemTriggerModelAddblockResetBranch(BaseTSPCmd):
    """The ``slot[Z].trigger.model.addblock.reset.branch`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.counter()``: The ``slot[Z].trigger.model.addblock.reset.branch.counter()`` function.
    """

    def counter(
        self, trigger_model_name: str, block_name: str, reset_branch_count_block_name: str
    ) -> None:
        """Run the ``slot[Z].trigger.model.addblock.reset.branch.counter()`` function.

        Description:
            - This function defines a trigger model block that resets the count for a branch counter
              block.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.reset.branch.counter()
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


class SlotItemTriggerModelAddblockReset(BaseTSPCmd):
    """The ``slot[Z].trigger.model.addblock.reset`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.branch``: The ``slot[Z].trigger.model.addblock.reset.branch`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._branch = SlotItemTriggerModelAddblockResetBranch(device, f"{self._cmd_syntax}.branch")

    @property
    def branch(self) -> SlotItemTriggerModelAddblockResetBranch:
        """Return the ``slot[Z].trigger.model.addblock.reset.branch`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.counter()``: The ``slot[Z].trigger.model.addblock.reset.branch.counter()``
              function.
        """
        return self._branch


class SlotItemTriggerModelAddblockDelay(BaseTSPCmd):
    """The ``slot[Z].trigger.model.addblock.delay`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.constant()``: The ``slot[Z].trigger.model.addblock.delay.constant()`` function.
    """

    def constant(
        self,
        trigger_model_name: str,
        block_name: str,
        delay_time: Optional[str] = None,
        reference_block_name: Optional[str] = None,
    ) -> None:
        """Run the ``slot[Z].trigger.model.addblock.delay.constant()`` function.

        Description:
            - This function adds a constant delay to the execution of a trigger model.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.delay.constant()
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


class SlotItemTriggerModelAddblockConfiglist(BaseTSPCmd):
    """The ``slot[Z].trigger.model.addblock.configlist`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.next()``: The ``slot[Z].trigger.model.addblock.configlist.next()`` function.
        - ``.prev()``: The ``slot[Z].trigger.model.addblock.configlist.prev()`` function.
        - ``.recall()``: The ``slot[Z].trigger.model.addblock.configlist.recall()`` function.
    """

    def next(
        self, trigger_model_name: str, block_name: str, channel: str, configlist_name: str
    ) -> None:
        """Run the ``slot[Z].trigger.model.addblock.configlist.next()`` function.

        Description:
            - This function recalls the settings at the next index of a configuration list.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.configlist.next()
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
        """Run the ``slot[Z].trigger.model.addblock.configlist.prev()`` function.

        Description:
            - This function defines a trigger model block that recalls the settings stored at the
              previous index in a configuration list.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.configlist.prev()
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
        """Run the ``slot[Z].trigger.model.addblock.configlist.recall()`` function.

        Description:
            - This function recalls the system settings that are stored in a configuration list.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.configlist.recall()
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


class SlotItemTriggerModelAddblockBranch(BaseTSPCmd):
    """The ``slot[Z].trigger.model.addblock.branch`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.always()``: The ``slot[Z].trigger.model.addblock.branch.always()`` function.
        - ``.counter()``: The ``slot[Z].trigger.model.addblock.branch.counter()`` function.
        - ``.once()``: The ``slot[Z].trigger.model.addblock.branch.once()`` function.
        - ``.onceexcluded()``: The ``slot[Z].trigger.model.addblock.branch.onceexcluded()``
          function.
    """

    def always(self, trigger_model_name: str, block_name: str, branch_to_block_name: str) -> None:
        """Run the ``slot[Z].trigger.model.addblock.branch.always()`` function.

        Description:
            - This function defines a trigger model block that always branches to a specific block.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.branch.always()
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
        """Run the ``slot[Z].trigger.model.addblock.branch.counter()`` function.

        Description:
            - This function defines a trigger model block that branches to a block a specified
              number of times.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.branch.counter()
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
        """Run the ``slot[Z].trigger.model.addblock.branch.once()`` function.

        Description:
            - This function causes the trigger model to branch to a specified trigger model block
              the first time it is encountered in the trigger model.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.branch.once()
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
        """Run the ``slot[Z].trigger.model.addblock.branch.onceexcluded()`` function.

        Description:
            - This function causes the trigger model to branch to a specified trigger model block
              every time it is encountered in the trigger model except for the first time.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.branch.onceexcluded()
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


class SlotItemTriggerModelAddblock(BaseTSPCmd):
    """The ``slot[Z].trigger.model.addblock`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.branch``: The ``slot[Z].trigger.model.addblock.branch`` command tree.
        - ``.configlist``: The ``slot[Z].trigger.model.addblock.configlist`` command tree.
        - ``.delay``: The ``slot[Z].trigger.model.addblock.delay`` command tree.
        - ``.logevent()``: The ``slot[Z].trigger.model.addblock.logevent()`` function.
        - ``.measure()``: The ``slot[Z].trigger.model.addblock.measure()`` function.
        - ``.measureoverlapped()``: The ``slot[Z].trigger.model.addblock.measureoverlapped()``
          function.
        - ``.nop()``: The ``slot[Z].trigger.model.addblock.nop()`` function.
        - ``.reset``: The ``slot[Z].trigger.model.addblock.reset`` command tree.
        - ``.source``: The ``slot[Z].trigger.model.addblock.source`` command tree.
        - ``.wait()``: The ``slot[Z].trigger.model.addblock.wait()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._branch = SlotItemTriggerModelAddblockBranch(device, f"{self._cmd_syntax}.branch")
        self._configlist = SlotItemTriggerModelAddblockConfiglist(
            device, f"{self._cmd_syntax}.configlist"
        )
        self._delay = SlotItemTriggerModelAddblockDelay(device, f"{self._cmd_syntax}.delay")
        self._reset = SlotItemTriggerModelAddblockReset(device, f"{self._cmd_syntax}.reset")
        self._source = SlotItemTriggerModelAddblockSource(device, f"{self._cmd_syntax}.source")

    @property
    def branch(self) -> SlotItemTriggerModelAddblockBranch:
        """Return the ``slot[Z].trigger.model.addblock.branch`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.always()``: The ``slot[Z].trigger.model.addblock.branch.always()`` function.
            - ``.counter()``: The ``slot[Z].trigger.model.addblock.branch.counter()`` function.
            - ``.once()``: The ``slot[Z].trigger.model.addblock.branch.once()`` function.
            - ``.onceexcluded()``: The ``slot[Z].trigger.model.addblock.branch.onceexcluded()``
              function.
        """
        return self._branch

    @property
    def configlist(self) -> SlotItemTriggerModelAddblockConfiglist:
        """Return the ``slot[Z].trigger.model.addblock.configlist`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.next()``: The ``slot[Z].trigger.model.addblock.configlist.next()`` function.
            - ``.prev()``: The ``slot[Z].trigger.model.addblock.configlist.prev()`` function.
            - ``.recall()``: The ``slot[Z].trigger.model.addblock.configlist.recall()`` function.
        """
        return self._configlist

    @property
    def delay(self) -> SlotItemTriggerModelAddblockDelay:
        """Return the ``slot[Z].trigger.model.addblock.delay`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.constant()``: The ``slot[Z].trigger.model.addblock.delay.constant()`` function.
        """
        return self._delay

    @property
    def reset(self) -> SlotItemTriggerModelAddblockReset:
        """Return the ``slot[Z].trigger.model.addblock.reset`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.branch``: The ``slot[Z].trigger.model.addblock.reset.branch`` command tree.
        """
        return self._reset

    @property
    def source(self) -> SlotItemTriggerModelAddblockSource:
        """Return the ``slot[Z].trigger.model.addblock.source`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.action``: The ``slot[Z].trigger.model.addblock.source.action`` command tree.
            - ``.output()``: The ``slot[Z].trigger.model.addblock.source.output()`` function.
        """
        return self._source

    def logevent(
        self, trigger_model_name: str, block_name: str, event_number: int, message: str
    ) -> None:
        """Run the ``slot[Z].trigger.model.addblock.logevent()`` function.

        Description:
            - This function allows you to log an event in the event log when the trigger model is
              running.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.logevent()
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
        """Run the ``slot[Z].trigger.model.addblock.measure()`` function.

        Description:
            - This function defines a trigger block that makes a measurement.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.measure()
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
        """Run the ``slot[Z].trigger.model.addblock.measureoverlapped()`` function.

        Description:
            - This function defines a trigger-model block that makes a measurement in an overlapped
              mode which allows you to measure the response of the device under test while the
              source is being stepped.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.measureoverlapped()
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
        """Run the ``slot[Z].trigger.model.addblock.nop()`` function.

        Description:
            - This function creates a placeholder block that performs no action in the trigger
              model.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.nop()
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
        """Run the ``slot[Z].trigger.model.addblock.wait()`` function.

        Description:
            - This function defines a trigger model block that waits for an event before allowing
              the trigger model to continue.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.addblock.wait()
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


class SlotItemTriggerModel(BaseTSPCmd):
    """The ``slot[Z].trigger.model`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.abort()``: The ``slot[Z].trigger.model.abort()`` function.
        - ``.addblock``: The ``slot[Z].trigger.model.addblock`` command tree.
        - ``.create()``: The ``slot[Z].trigger.model.create()`` function.
        - ``.delete()``: The ``slot[Z].trigger.model.delete()`` function.
        - ``.initiate()``: The ``slot[Z].trigger.model.initiate()`` function.
        - ``.removeblock()``: The ``slot[Z].trigger.model.removeblock()`` function.
        - ``.state()``: The ``slot[Z].trigger.model.state()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._addblock = SlotItemTriggerModelAddblock(device, f"{self._cmd_syntax}.addblock")

    @property
    def addblock(self) -> SlotItemTriggerModelAddblock:
        """Return the ``slot[Z].trigger.model.addblock`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.branch``: The ``slot[Z].trigger.model.addblock.branch`` command tree.
            - ``.configlist``: The ``slot[Z].trigger.model.addblock.configlist`` command tree.
            - ``.delay``: The ``slot[Z].trigger.model.addblock.delay`` command tree.
            - ``.logevent()``: The ``slot[Z].trigger.model.addblock.logevent()`` function.
            - ``.measure()``: The ``slot[Z].trigger.model.addblock.measure()`` function.
            - ``.measureoverlapped()``: The ``slot[Z].trigger.model.addblock.measureoverlapped()``
              function.
            - ``.nop()``: The ``slot[Z].trigger.model.addblock.nop()`` function.
            - ``.reset``: The ``slot[Z].trigger.model.addblock.reset`` command tree.
            - ``.source``: The ``slot[Z].trigger.model.addblock.source`` command tree.
            - ``.wait()``: The ``slot[Z].trigger.model.addblock.wait()`` function.
        """
        return self._addblock

    def abort(self, trigger_model_name: str) -> None:
        """Run the ``slot[Z].trigger.model.abort()`` function.

        Description:
            - This function stops trigger model execution on the specified module.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.abort()
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
        """Run the ``slot[Z].trigger.model.create()`` function.

        Description:
            - This function creates a trigger model.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.create()
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
        """Run the ``slot[Z].trigger.model.delete()`` function.

        Description:
            - This function deletes a trigger model.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.delete()
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
        """Run the ``slot[Z].trigger.model.initiate()`` function.

        Description:
            - This function starts a specified trigger model on a module.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.initiate()
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
        """Run the ``slot[Z].trigger.model.removeblock()`` function.

        Description:
            - This function removes the trigger block from the trigger model.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.removeblock()
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

    def state(self, trigger_model_name: str) -> str:
        """Run the ``slot[Z].trigger.model.state()`` function.

        Description:
            - This function returns the present state of the trigger model.

        TSP Syntax:
            ```
            - slot[Z].trigger.model.state()
            ```

        Args:
            trigger_model_name: Name of the trigger model.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.state("{trigger_model_name}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.state()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemTrigger(BaseTSPCmd):
    """The ``slot[Z].trigger`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.model``: The ``slot[Z].trigger.model`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._model = SlotItemTriggerModel(device, f"{self._cmd_syntax}.model")

    @property
    def model(self) -> SlotItemTriggerModel:
        """Return the ``slot[Z].trigger.model`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.abort()``: The ``slot[Z].trigger.model.abort()`` function.
            - ``.addblock``: The ``slot[Z].trigger.model.addblock`` command tree.
            - ``.create()``: The ``slot[Z].trigger.model.create()`` function.
            - ``.delete()``: The ``slot[Z].trigger.model.delete()`` function.
            - ``.initiate()``: The ``slot[Z].trigger.model.initiate()`` function.
            - ``.removeblock()``: The ``slot[Z].trigger.model.removeblock()`` function.
            - ``.state()``: The ``slot[Z].trigger.model.state()`` function.
        """
        return self._model


class SlotItemStatusQuestionableOverTemperature(BaseTSPCmd):
    """The ``slot[Z].status.questionable.over_temperature`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.questionable.over_temperature.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.questionable.over_temperature.enable`` attribute.
        - ``.event``: The ``slot[Z].status.questionable.over_temperature.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.questionable.over_temperature.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.questionable.over_temperature.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.questionable.over_temperature.condition`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.over_temperature.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.over_temperature.condition)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.over_temperature.enable`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.over_temperature.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.over_temperature.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.over_temperature.enable = value
            - print(slot[Z].status.questionable.over_temperature.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.over_temperature.enable`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.over_temperature.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.over_temperature.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.over_temperature.enable = value
            - print(slot[Z].status.questionable.over_temperature.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.over_temperature.event`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.over_temperature.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.over_temperature.event)
            ```

        Info:
            - ``Z``, the module slot number.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.questionable.over_temperature.ntr`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.over_temperature.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.over_temperature.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.over_temperature.ntr = value
            - print(slot[Z].status.questionable.over_temperature.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.over_temperature.ntr`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.over_temperature.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.over_temperature.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.over_temperature.ntr = value
            - print(slot[Z].status.questionable.over_temperature.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.questionable.over_temperature.ptr`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.over_temperature.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.over_temperature.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.over_temperature.ptr = value
            - print(slot[Z].status.questionable.over_temperature.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.over_temperature.ptr`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.over_temperature.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.over_temperature.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.over_temperature.ptr = value
            - print(slot[Z].status.questionable.over_temperature.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusQuestionableInstrumentSmuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[Z].status.questionable.instrument.smu[X]`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the channel of the SMU: 1 or 2.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.questionable.instrument.smu[X].condition`` attribute.
        - ``.enable``: The ``slot[Z].status.questionable.instrument.smu[X].enable`` attribute.
        - ``.event``: The ``slot[Z].status.questionable.instrument.smu[X].event`` attribute.
        - ``.ntr``: The ``slot[Z].status.questionable.instrument.smu[X].ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.questionable.instrument.smu[X].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.questionable.instrument.smu[X].condition`` attribute.

        Description:
            - This attribute contains the questionable status SMU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.smu[X].condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.instrument.smu[X].condition)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

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
        """Access the ``slot[Z].status.questionable.instrument.smu[X].enable`` attribute.

        Description:
            - This attribute contains the questionable status SMU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.smu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.smu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.smu[X].enable = value
            - print(slot[Z].status.questionable.instrument.smu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

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
        """Access the ``slot[Z].status.questionable.instrument.smu[X].enable`` attribute.

        Description:
            - This attribute contains the questionable status SMU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.smu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.smu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.smu[X].enable = value
            - print(slot[Z].status.questionable.instrument.smu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

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
        """Access the ``slot[Z].status.questionable.instrument.smu[X].event`` attribute.

        Description:
            - This attribute contains the questionable status SMU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.smu[X].event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.instrument.smu[X].event)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.questionable.instrument.smu[X].ntr`` attribute.

        Description:
            - This attribute contains the questionable status SMU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.smu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.smu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.smu[X].ntr = value
            - print(slot[Z].status.questionable.instrument.smu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.instrument.smu[X].ntr`` attribute.

        Description:
            - This attribute contains the questionable status SMU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.smu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.smu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.smu[X].ntr = value
            - print(slot[Z].status.questionable.instrument.smu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.questionable.instrument.smu[X].ptr`` attribute.

        Description:
            - This attribute contains the questionable status SMU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.smu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.smu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.smu[X].ptr = value
            - print(slot[Z].status.questionable.instrument.smu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.instrument.smu[X].ptr`` attribute.

        Description:
            - This attribute contains the questionable status SMU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.smu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.smu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.smu[X].ptr = value
            - print(slot[Z].status.questionable.instrument.smu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusQuestionableInstrumentPsuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[Z].status.questionable.instrument.psu[X]`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the channel of the PSU: 1 or 2.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.questionable.instrument.psu[X].condition`` attribute.
        - ``.enable``: The ``slot[Z].status.questionable.instrument.psu[X].enable`` attribute.
        - ``.event``: The ``slot[Z].status.questionable.instrument.psu[X].event`` attribute.
        - ``.ntr``: The ``slot[Z].status.questionable.instrument.psu[X].ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.questionable.instrument.psu[X].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.questionable.instrument.psu[X].condition`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.psu[X].condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.instrument.psu[X].condition)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

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
        """Access the ``slot[Z].status.questionable.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.psu[X].enable = value
            - print(slot[Z].status.questionable.instrument.psu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

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
        """Access the ``slot[Z].status.questionable.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.psu[X].enable = value
            - print(slot[Z].status.questionable.instrument.psu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

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
        """Access the ``slot[Z].status.questionable.instrument.psu[X].event`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.psu[X].event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.instrument.psu[X].event)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.questionable.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.psu[X].ntr = value
            - print(slot[Z].status.questionable.instrument.psu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.psu[X].ntr = value
            - print(slot[Z].status.questionable.instrument.psu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.questionable.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.psu[X].ptr = value
            - print(slot[Z].status.questionable.instrument.psu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.psu[X].ptr = value
            - print(slot[Z].status.questionable.instrument.psu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusQuestionableInstrument(BaseTSPCmd):
    """The ``slot[Z].status.questionable.instrument`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.questionable.instrument.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.questionable.instrument.enable`` attribute.
        - ``.event``: The ``slot[Z].status.questionable.instrument.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.questionable.instrument.ntr`` attribute.
        - ``.psu``: The ``slot[Z].status.questionable.instrument.psu[X]`` command tree.
        - ``.ptr``: The ``slot[Z].status.questionable.instrument.ptr`` attribute.
        - ``.smu``: The ``slot[Z].status.questionable.instrument.smu[X]`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._psu: Dict[int, SlotItemStatusQuestionableInstrumentPsuItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SlotItemStatusQuestionableInstrumentPsuItem(
                    device, f"{self._cmd_syntax}.psu[{x}]"
                )
            )
        )
        self._smu: Dict[int, SlotItemStatusQuestionableInstrumentSmuItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SlotItemStatusQuestionableInstrumentSmuItem(
                    device, f"{self._cmd_syntax}.smu[{x}]"
                )
            )
        )

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.questionable.instrument.condition`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.instrument.condition)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.instrument.enable`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.enable = value
            - print(slot[Z].status.questionable.instrument.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.instrument.enable`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.enable = value
            - print(slot[Z].status.questionable.instrument.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.instrument.event`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.instrument.event)
            ```

        Info:
            - ``Z``, the module slot number.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.questionable.instrument.ntr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.ntr = value
            - print(slot[Z].status.questionable.instrument.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.instrument.ntr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.ntr = value
            - print(slot[Z].status.questionable.instrument.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def psu(self) -> Dict[int, SlotItemStatusQuestionableInstrumentPsuItem]:
        """Return the ``slot[Z].status.questionable.instrument.psu[X]`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.questionable.instrument.psu[X].condition``
              attribute.
            - ``.enable``: The ``slot[Z].status.questionable.instrument.psu[X].enable`` attribute.
            - ``.event``: The ``slot[Z].status.questionable.instrument.psu[X].event`` attribute.
            - ``.ntr``: The ``slot[Z].status.questionable.instrument.psu[X].ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.questionable.instrument.psu[X].ptr`` attribute.
        """
        return self._psu

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.questionable.instrument.ptr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.ptr = value
            - print(slot[Z].status.questionable.instrument.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.instrument.ptr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.instrument.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.instrument.ptr = value
            - print(slot[Z].status.questionable.instrument.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def smu(self) -> Dict[int, SlotItemStatusQuestionableInstrumentSmuItem]:
        """Return the ``slot[Z].status.questionable.instrument.smu[X]`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.questionable.instrument.smu[X].condition``
              attribute.
            - ``.enable``: The ``slot[Z].status.questionable.instrument.smu[X].enable`` attribute.
            - ``.event``: The ``slot[Z].status.questionable.instrument.smu[X].event`` attribute.
            - ``.ntr``: The ``slot[Z].status.questionable.instrument.smu[X].ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.questionable.instrument.smu[X].ptr`` attribute.
        """
        return self._smu


class SlotItemStatusQuestionableCalibration(BaseTSPCmd):
    """The ``slot[Z].status.questionable.calibration`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.questionable.calibration.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.questionable.calibration.enable`` attribute.
        - ``.event``: The ``slot[Z].status.questionable.calibration.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.questionable.calibration.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.questionable.calibration.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.questionable.calibration.condition`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.calibration.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.calibration.condition)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.calibration.enable`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.calibration.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.calibration.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.calibration.enable = value
            - print(slot[Z].status.questionable.calibration.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.calibration.enable`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.calibration.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.calibration.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.calibration.enable = value
            - print(slot[Z].status.questionable.calibration.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.calibration.event`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.calibration.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.calibration.event)
            ```

        Info:
            - ``Z``, the module slot number.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.questionable.calibration.ntr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.calibration.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.calibration.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.calibration.ntr = value
            - print(slot[Z].status.questionable.calibration.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.calibration.ntr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.calibration.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.calibration.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.calibration.ntr = value
            - print(slot[Z].status.questionable.calibration.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.questionable.calibration.ptr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.calibration.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.calibration.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.calibration.ptr = value
            - print(slot[Z].status.questionable.calibration.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.calibration.ptr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.questionable.calibration.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.calibration.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.calibration.ptr = value
            - print(slot[Z].status.questionable.calibration.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusQuestionable(BaseTSPCmd):
    """The ``slot[Z].status.questionable`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.calibration``: The ``slot[Z].status.questionable.calibration`` command tree.
        - ``.condition``: The ``slot[Z].status.questionable.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.questionable.enable`` attribute.
        - ``.event``: The ``slot[Z].status.questionable.event`` attribute.
        - ``.instrument``: The ``slot[Z].status.questionable.instrument`` command tree.
        - ``.ntr``: The ``slot[Z].status.questionable.ntr`` attribute.
        - ``.over_temperature``: The ``slot[Z].status.questionable.over_temperature`` command tree.
        - ``.ptr``: The ``slot[Z].status.questionable.ptr`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calibration = SlotItemStatusQuestionableCalibration(
            device, f"{self._cmd_syntax}.calibration"
        )
        self._instrument = SlotItemStatusQuestionableInstrument(
            device, f"{self._cmd_syntax}.instrument"
        )
        self._over_temperature = SlotItemStatusQuestionableOverTemperature(
            device, f"{self._cmd_syntax}.over_temperature"
        )

    @property
    def calibration(self) -> SlotItemStatusQuestionableCalibration:
        """Return the ``slot[Z].status.questionable.calibration`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.questionable.calibration.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.questionable.calibration.enable`` attribute.
            - ``.event``: The ``slot[Z].status.questionable.calibration.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.questionable.calibration.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.questionable.calibration.ptr`` attribute.
        """
        return self._calibration

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.questionable.condition`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.questionable.condition)``
              query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.condition)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.enable`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.questionable.enable)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.enable = value
            - print(slot[Z].status.questionable.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.enable`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.questionable.enable)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.enable = value
            - print(slot[Z].status.questionable.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.questionable.event`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.questionable.event)``
              query.

        TSP Syntax:
            ```
            - print(slot[Z].status.questionable.event)
            ```

        Info:
            - ``Z``, the module slot number.

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

    @property
    def instrument(self) -> SlotItemStatusQuestionableInstrument:
        """Return the ``slot[Z].status.questionable.instrument`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.questionable.instrument.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.questionable.instrument.enable`` attribute.
            - ``.event``: The ``slot[Z].status.questionable.instrument.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.questionable.instrument.ntr`` attribute.
            - ``.psu``: The ``slot[Z].status.questionable.instrument.psu[X]`` command tree.
            - ``.ptr``: The ``slot[Z].status.questionable.instrument.ptr`` attribute.
            - ``.smu``: The ``slot[Z].status.questionable.instrument.smu[X]`` command tree.
        """
        return self._instrument

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.questionable.ntr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.questionable.ntr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.ntr = value
            - print(slot[Z].status.questionable.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.ntr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.questionable.ntr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.ntr = value
            - print(slot[Z].status.questionable.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def over_temperature(self) -> SlotItemStatusQuestionableOverTemperature:
        """Return the ``slot[Z].status.questionable.over_temperature`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.questionable.over_temperature.condition``
              attribute.
            - ``.enable``: The ``slot[Z].status.questionable.over_temperature.enable`` attribute.
            - ``.event``: The ``slot[Z].status.questionable.over_temperature.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.questionable.over_temperature.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.questionable.over_temperature.ptr`` attribute.
        """
        return self._over_temperature

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.questionable.ptr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.questionable.ptr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.ptr = value
            - print(slot[Z].status.questionable.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.questionable.ptr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.questionable.ptr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.questionable.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.questionable.ptr = value
            - print(slot[Z].status.questionable.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusOperationSweeping(BaseTSPCmd):
    """The ``slot[Z].status.operation.sweeping`` command tree.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.operation.sweeping.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.operation.sweeping.enable`` attribute.
        - ``.event``: The ``slot[Z].status.operation.sweeping.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.operation.sweeping.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.operation.sweeping.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.operation.sweeping.condition`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.sweeping.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.sweeping.condition)
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
        """Access the ``slot[Z].status.operation.sweeping.enable`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.sweeping.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.sweeping.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.sweeping.enable = value
            - print(slot[Z].status.operation.sweeping.enable)
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
        """Access the ``slot[Z].status.operation.sweeping.enable`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.sweeping.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.sweeping.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.sweeping.enable = value
            - print(slot[Z].status.operation.sweeping.enable)
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
        """Access the ``slot[Z].status.operation.sweeping.event`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.sweeping.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.sweeping.event)
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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.operation.sweeping.ntr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.sweeping.ntr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.sweeping.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.sweeping.ntr = value
            - print(slot[Z].status.operation.sweeping.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.sweeping.ntr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.sweeping.ntr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.sweeping.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.sweeping.ntr = value
            - print(slot[Z].status.operation.sweeping.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.operation.sweeping.ptr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.sweeping.ptr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.sweeping.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.sweeping.ptr = value
            - print(slot[Z].status.operation.sweeping.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.sweeping.ptr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.sweeping.ptr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.sweeping.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.sweeping.ptr = value
            - print(slot[Z].status.operation.sweeping.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusOperationMeasuring(BaseTSPCmd):
    """The ``slot[Z].status.operation.measuring`` command tree.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.operation.measuring.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.operation.measuring.enable`` attribute.
        - ``.event``: The ``slot[Z].status.operation.measuring.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.operation.measuring.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.operation.measuring.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.operation.measuring.condition`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.measuring.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.measuring.condition)
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
        """Access the ``slot[Z].status.operation.measuring.enable`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.measuring.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.measuring.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.measuring.enable = value
            - print(slot[Z].status.operation.measuring.enable)
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
        """Access the ``slot[Z].status.operation.measuring.enable`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.measuring.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.measuring.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.measuring.enable = value
            - print(slot[Z].status.operation.measuring.enable)
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
        """Access the ``slot[Z].status.operation.measuring.event`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.measuring.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.measuring.event)
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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.operation.measuring.ntr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.measuring.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.measuring.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.measuring.ntr = value
            - print(slot[Z].status.operation.measuring.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.measuring.ntr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.measuring.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.measuring.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.measuring.ntr = value
            - print(slot[Z].status.operation.measuring.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.operation.measuring.ptr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.measuring.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.measuring.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.measuring.ptr = value
            - print(slot[Z].status.operation.measuring.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.measuring.ptr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.measuring.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.measuring.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.measuring.ptr = value
            - print(slot[Z].status.operation.measuring.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusOperationInstrumentSmuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[Z].status.operation.instrument.smu[X]`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the source-measure unit (SMU) channel (for example,
          slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot 2).

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.operation.instrument.smu[X].condition`` attribute.
        - ``.enable``: The ``slot[Z].status.operation.instrument.smu[X].enable`` attribute.
        - ``.event``: The ``slot[Z].status.operation.instrument.smu[X].event`` attribute.
        - ``.ntr``: The ``slot[Z].status.operation.instrument.smu[X].ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.operation.instrument.smu[X].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.operation.instrument.smu[X].condition`` attribute.

        Description:
            - This attribute contains the Operation Status SMU[X] Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.smu[X].condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.instrument.smu[X].condition)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the source-measure unit (SMU) channel (for example,
              slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot
              2).

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
        """Access the ``slot[Z].status.operation.instrument.smu[X].enable`` attribute.

        Description:
            - This attribute contains the Operation Status SMU[X] Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.smu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.smu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.smu[X].enable = value
            - print(slot[Z].status.operation.instrument.smu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the source-measure unit (SMU) channel (for example,
              slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot
              2).

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
        """Access the ``slot[Z].status.operation.instrument.smu[X].enable`` attribute.

        Description:
            - This attribute contains the Operation Status SMU[X] Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.smu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.smu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.smu[X].enable = value
            - print(slot[Z].status.operation.instrument.smu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the source-measure unit (SMU) channel (for example,
              slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot
              2).

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
        """Access the ``slot[Z].status.operation.instrument.smu[X].event`` attribute.

        Description:
            - This attribute contains the Operation Status SMU[X] Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.smu[X].event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.instrument.smu[X].event)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the source-measure unit (SMU) channel (for example,
              slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot
              2).

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.operation.instrument.smu[X].ntr`` attribute.

        Description:
            - This attribute contains the Operation Status SMU[X] Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.smu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.smu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.smu[X].ntr = value
            - print(slot[Z].status.operation.instrument.smu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the source-measure unit (SMU) channel (for example,
              slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot
              2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.instrument.smu[X].ntr`` attribute.

        Description:
            - This attribute contains the Operation Status SMU[X] Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.smu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.smu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.smu[X].ntr = value
            - print(slot[Z].status.operation.instrument.smu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the source-measure unit (SMU) channel (for example,
              slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot
              2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.operation.instrument.smu[X].ptr`` attribute.

        Description:
            - This attribute contains the Operation Status SMU[X] Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.smu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.smu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.smu[X].ptr = value
            - print(slot[Z].status.operation.instrument.smu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the source-measure unit (SMU) channel (for example,
              slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot
              2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.instrument.smu[X].ptr`` attribute.

        Description:
            - This attribute contains the Operation Status SMU[X] Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.smu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.smu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.smu[X].ptr = value
            - print(slot[Z].status.operation.instrument.smu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the source-measure unit (SMU) channel (for example,
              slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot
              2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusOperationInstrumentPsuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[Z].status.operation.instrument.psu[X]`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the power supply unit (PSU) channel (for example
          slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.operation.instrument.psu[X].condition`` attribute.
        - ``.enable``: The ``slot[Z].status.operation.instrument.psu[X].enable`` attribute.
        - ``.event``: The ``slot[Z].status.operation.instrument.psu[X].event`` attribute.
        - ``.ntr``: The ``slot[Z].status.operation.instrument.psu[X].ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.operation.instrument.psu[X].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.operation.instrument.psu[X].condition`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.psu[X].condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.instrument.psu[X].condition)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

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
        """Access the ``slot[Z].status.operation.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.psu[X].enable = value
            - print(slot[Z].status.operation.instrument.psu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

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
        """Access the ``slot[Z].status.operation.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.psu[X].enable = value
            - print(slot[Z].status.operation.instrument.psu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

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
        """Access the ``slot[Z].status.operation.instrument.psu[X].event`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.psu[X].event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.instrument.psu[X].event)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.operation.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.psu[X].ntr = value
            - print(slot[Z].status.operation.instrument.psu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.psu[X].ntr = value
            - print(slot[Z].status.operation.instrument.psu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.operation.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.psu[X].ptr = value
            - print(slot[Z].status.operation.instrument.psu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.psu[X].ptr = value
            - print(slot[Z].status.operation.instrument.psu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusOperationInstrument(BaseTSPCmd):
    """The ``slot[Z].status.operation.instrument`` command tree.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.operation.instrument.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.operation.instrument.enable`` attribute.
        - ``.event``: The ``slot[Z].status.operation.instrument.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.operation.instrument.ntr`` attribute.
        - ``.psu``: The ``slot[Z].status.operation.instrument.psu[X]`` command tree.
        - ``.ptr``: The ``slot[Z].status.operation.instrument.ptr`` attribute.
        - ``.smu``: The ``slot[Z].status.operation.instrument.smu[X]`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._psu: Dict[int, SlotItemStatusOperationInstrumentPsuItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SlotItemStatusOperationInstrumentPsuItem(
                    device, f"{self._cmd_syntax}.psu[{x}]"
                )
            )
        )
        self._smu: Dict[int, SlotItemStatusOperationInstrumentSmuItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SlotItemStatusOperationInstrumentSmuItem(
                    device, f"{self._cmd_syntax}.smu[{x}]"
                )
            )
        )

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.operation.instrument.condition`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.instrument.condition)
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
        """Access the ``slot[Z].status.operation.instrument.enable`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.enable = value
            - print(slot[Z].status.operation.instrument.enable)
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
        """Access the ``slot[Z].status.operation.instrument.enable`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.enable = value
            - print(slot[Z].status.operation.instrument.enable)
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
        """Access the ``slot[Z].status.operation.instrument.event`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.instrument.event)
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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.operation.instrument.ntr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.ntr = value
            - print(slot[Z].status.operation.instrument.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.instrument.ntr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.ntr = value
            - print(slot[Z].status.operation.instrument.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def psu(self) -> Dict[int, SlotItemStatusOperationInstrumentPsuItem]:
        """Return the ``slot[Z].status.operation.instrument.psu[X]`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.operation.instrument.psu[X].condition``
              attribute.
            - ``.enable``: The ``slot[Z].status.operation.instrument.psu[X].enable`` attribute.
            - ``.event``: The ``slot[Z].status.operation.instrument.psu[X].event`` attribute.
            - ``.ntr``: The ``slot[Z].status.operation.instrument.psu[X].ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.operation.instrument.psu[X].ptr`` attribute.
        """
        return self._psu

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.operation.instrument.ptr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.ptr = value
            - print(slot[Z].status.operation.instrument.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.instrument.ptr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.instrument.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.instrument.ptr = value
            - print(slot[Z].status.operation.instrument.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def smu(self) -> Dict[int, SlotItemStatusOperationInstrumentSmuItem]:
        """Return the ``slot[Z].status.operation.instrument.smu[X]`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the source-measure unit (SMU) channel (for example,
              slot[2]status.operation.instrument.smu[1].enable applies to the SMU channel 1 in slot
              2).

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.operation.instrument.smu[X].condition``
              attribute.
            - ``.enable``: The ``slot[Z].status.operation.instrument.smu[X].enable`` attribute.
            - ``.event``: The ``slot[Z].status.operation.instrument.smu[X].event`` attribute.
            - ``.ntr``: The ``slot[Z].status.operation.instrument.smu[X].ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.operation.instrument.smu[X].ptr`` attribute.
        """
        return self._smu


class SlotItemStatusOperationCalibrating(BaseTSPCmd):
    """The ``slot[Z].status.operation.calibrating`` command tree.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.operation.calibrating.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.operation.calibrating.enable`` attribute.
        - ``.event``: The ``slot[Z].status.operation.calibrating.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.operation.calibrating.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.operation.calibrating.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.operation.calibrating.condition`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.calibrating.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.calibrating.condition)
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
        """Access the ``slot[Z].status.operation.calibrating.enable`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.calibrating.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.calibrating.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.calibrating.enable = value
            - print(slot[Z].status.operation.calibrating.enable)
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
        """Access the ``slot[Z].status.operation.calibrating.enable`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.calibrating.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.calibrating.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.calibrating.enable = value
            - print(slot[Z].status.operation.calibrating.enable)
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
        """Access the ``slot[Z].status.operation.calibrating.event`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.calibrating.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.calibrating.event)
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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.operation.calibrating.ntr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.calibrating.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.calibrating.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.calibrating.ntr = value
            - print(slot[Z].status.operation.calibrating.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.calibrating.ntr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.calibrating.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.calibrating.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.calibrating.ntr = value
            - print(slot[Z].status.operation.calibrating.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.operation.calibrating.ptr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.calibrating.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.calibrating.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.calibrating.ptr = value
            - print(slot[Z].status.operation.calibrating.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.calibrating.ptr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.operation.calibrating.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.calibrating.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.calibrating.ptr = value
            - print(slot[Z].status.operation.calibrating.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusOperation(BaseTSPCmd):
    """The ``slot[Z].status.operation`` command tree.

    Properties and methods:
        - ``.calibrating``: The ``slot[Z].status.operation.calibrating`` command tree.
        - ``.condition``: The ``slot[Z].status.operation.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.operation.enable`` attribute.
        - ``.event``: The ``slot[Z].status.operation.event`` attribute.
        - ``.instrument``: The ``slot[Z].status.operation.instrument`` command tree.
        - ``.measuring``: The ``slot[Z].status.operation.measuring`` command tree.
        - ``.ntr``: The ``slot[Z].status.operation.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.operation.ptr`` attribute.
        - ``.sweeping``: The ``slot[Z].status.operation.sweeping`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calibrating = SlotItemStatusOperationCalibrating(
            device, f"{self._cmd_syntax}.calibrating"
        )
        self._instrument = SlotItemStatusOperationInstrument(
            device, f"{self._cmd_syntax}.instrument"
        )
        self._measuring = SlotItemStatusOperationMeasuring(device, f"{self._cmd_syntax}.measuring")
        self._sweeping = SlotItemStatusOperationSweeping(device, f"{self._cmd_syntax}.sweeping")

    @property
    def calibrating(self) -> SlotItemStatusOperationCalibrating:
        """Return the ``slot[Z].status.operation.calibrating`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.operation.calibrating.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.operation.calibrating.enable`` attribute.
            - ``.event``: The ``slot[Z].status.operation.calibrating.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.operation.calibrating.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.operation.calibrating.ptr`` attribute.
        """
        return self._calibrating

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.operation.condition`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.condition)``
              query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.condition)
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
        """Access the ``slot[Z].status.operation.enable`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.enable)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.enable = value
            - print(slot[Z].status.operation.enable)
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
        """Access the ``slot[Z].status.operation.enable`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.enable)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.enable = value
            - print(slot[Z].status.operation.enable)
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
        """Access the ``slot[Z].status.operation.event`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.operation.event)
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

    @property
    def instrument(self) -> SlotItemStatusOperationInstrument:
        """Return the ``slot[Z].status.operation.instrument`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.operation.instrument.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.operation.instrument.enable`` attribute.
            - ``.event``: The ``slot[Z].status.operation.instrument.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.operation.instrument.ntr`` attribute.
            - ``.psu``: The ``slot[Z].status.operation.instrument.psu[X]`` command tree.
            - ``.ptr``: The ``slot[Z].status.operation.instrument.ptr`` attribute.
            - ``.smu``: The ``slot[Z].status.operation.instrument.smu[X]`` command tree.
        """
        return self._instrument

    @property
    def measuring(self) -> SlotItemStatusOperationMeasuring:
        """Return the ``slot[Z].status.operation.measuring`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.operation.measuring.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.operation.measuring.enable`` attribute.
            - ``.event``: The ``slot[Z].status.operation.measuring.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.operation.measuring.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.operation.measuring.ptr`` attribute.
        """
        return self._measuring

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.operation.ntr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.ntr = value
            - print(slot[Z].status.operation.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.ntr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.ntr = value
            - print(slot[Z].status.operation.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.operation.ptr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.ptr = value
            - print(slot[Z].status.operation.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.operation.ptr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.operation.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.operation.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.operation.ptr = value
            - print(slot[Z].status.operation.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def sweeping(self) -> SlotItemStatusOperationSweeping:
        """Return the ``slot[Z].status.operation.sweeping`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.operation.sweeping.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.operation.sweeping.enable`` attribute.
            - ``.event``: The ``slot[Z].status.operation.sweeping.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.operation.sweeping.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.operation.sweeping.ptr`` attribute.
        """
        return self._sweeping


class SlotItemStatusMeasurementVoltageLimit(BaseTSPCmd):
    """The ``slot[Z].status.measurement.voltage_limit`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.measurement.voltage_limit.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.measurement.voltage_limit.enable`` attribute.
        - ``.event``: The ``slot[Z].status.measurement.voltage_limit.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.measurement.voltage_limit.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.measurement.voltage_limit.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.measurement.voltage_limit.condition`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.voltage_limit.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.voltage_limit.condition)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.voltage_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.voltage_limit.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.voltage_limit.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.voltage_limit.enable = value
            - print(slot[Z].status.measurement.voltage_limit.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.voltage_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.voltage_limit.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.voltage_limit.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.voltage_limit.enable = value
            - print(slot[Z].status.measurement.voltage_limit.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.voltage_limit.event`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.voltage_limit.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.voltage_limit.event)
            ```

        Info:
            - ``Z``, the module slot number.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.measurement.voltage_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.voltage_limit.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.voltage_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.voltage_limit.ntr = value
            - print(slot[Z].status.measurement.voltage_limit.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.voltage_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.voltage_limit.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.voltage_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.voltage_limit.ntr = value
            - print(slot[Z].status.measurement.voltage_limit.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.measurement.voltage_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.voltage_limit.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.voltage_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.voltage_limit.ptr = value
            - print(slot[Z].status.measurement.voltage_limit.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.voltage_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.voltage_limit.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.voltage_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.voltage_limit.ptr = value
            - print(slot[Z].status.measurement.voltage_limit.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusMeasurementReadingOverflow(BaseTSPCmd):
    """The ``slot[Z].status.measurement.reading_overflow`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.measurement.reading_overflow.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.measurement.reading_overflow.enable`` attribute.
        - ``.event``: The ``slot[Z].status.measurement.reading_overflow.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.measurement.reading_overflow.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.measurement.reading_overflow.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.measurement.reading_overflow.condition`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.reading_overflow.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.reading_overflow.condition)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.reading_overflow.enable`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.reading_overflow.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.reading_overflow.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.reading_overflow.enable = value
            - print(slot[Z].status.measurement.reading_overflow.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.reading_overflow.enable`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.reading_overflow.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.reading_overflow.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.reading_overflow.enable = value
            - print(slot[Z].status.measurement.reading_overflow.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.reading_overflow.event`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.reading_overflow.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.reading_overflow.event)
            ```

        Info:
            - ``Z``, the module slot number.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.measurement.reading_overflow.ntr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.reading_overflow.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.reading_overflow.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.reading_overflow.ntr = value
            - print(slot[Z].status.measurement.reading_overflow.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.reading_overflow.ntr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.reading_overflow.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.reading_overflow.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.reading_overflow.ntr = value
            - print(slot[Z].status.measurement.reading_overflow.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.measurement.reading_overflow.ptr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.reading_overflow.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.reading_overflow.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.reading_overflow.ptr = value
            - print(slot[Z].status.measurement.reading_overflow.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.reading_overflow.ptr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.reading_overflow.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.reading_overflow.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.reading_overflow.ptr = value
            - print(slot[Z].status.measurement.reading_overflow.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusMeasurementProtection(BaseTSPCmd):
    """The ``slot[Z].status.measurement.protection`` command tree.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.measurement.protection.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.measurement.protection.enable`` attribute.
        - ``.event``: The ``slot[Z].status.measurement.protection.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.measurement.protection.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.measurement.protection.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.measurement.protection.condition`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.protection.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.protection.condition)
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
        """Access the ``slot[Z].status.measurement.protection.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.protection.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.protection.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.protection.enable = value
            - print(slot[Z].status.measurement.protection.enable)
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
        """Access the ``slot[Z].status.measurement.protection.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.protection.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.protection.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.protection.enable = value
            - print(slot[Z].status.measurement.protection.enable)
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
        """Access the ``slot[Z].status.measurement.protection.event`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.protection.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.protection.event)
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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.measurement.protection.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.protection.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.protection.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.protection.ntr = value
            - print(slot[Z].status.measurement.protection.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.protection.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.protection.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.protection.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.protection.ntr = value
            - print(slot[Z].status.measurement.protection.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.measurement.protection.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.protection.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.protection.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.protection.ptr = value
            - print(slot[Z].status.measurement.protection.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.protection.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.protection.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.protection.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.protection.ptr = value
            - print(slot[Z].status.measurement.protection.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusMeasurementInstrumentSmuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[Z].status.measurement.instrument.smu[X]`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the channel of the SMU: 1 or 2.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.measurement.instrument.smu[X].condition`` attribute.
        - ``.enable``: The ``slot[Z].status.measurement.instrument.smu[X].enable`` attribute.
        - ``.event``: The ``slot[Z].status.measurement.instrument.smu[X].event`` attribute.
        - ``.ntr``: The ``slot[Z].status.measurement.instrument.smu[X].ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.measurement.instrument.smu[X].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.measurement.instrument.smu[X].condition`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.smu[X].condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.instrument.smu[X].condition)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

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
        """Access the ``slot[Z].status.measurement.instrument.smu[X].enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.smu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.smu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.smu[X].enable = value
            - print(slot[Z].status.measurement.instrument.smu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

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
        """Access the ``slot[Z].status.measurement.instrument.smu[X].enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.smu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.smu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.smu[X].enable = value
            - print(slot[Z].status.measurement.instrument.smu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

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
        """Access the ``slot[Z].status.measurement.instrument.smu[X].event`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.smu[X].event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.instrument.smu[X].event)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.measurement.instrument.smu[X].ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.smu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.smu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.smu[X].ntr = value
            - print(slot[Z].status.measurement.instrument.smu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.instrument.smu[X].ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.smu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.smu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.smu[X].ntr = value
            - print(slot[Z].status.measurement.instrument.smu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.measurement.instrument.smu[X].ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.smu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.smu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.smu[X].ptr = value
            - print(slot[Z].status.measurement.instrument.smu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.instrument.smu[X].ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.smu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.smu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.smu[X].ptr = value
            - print(slot[Z].status.measurement.instrument.smu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusMeasurementInstrumentPsuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[Z].status.measurement.instrument.psu[X]`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the channel of the PSU: 1 or 2.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.measurement.instrument.psu[X].condition`` attribute.
        - ``.enable``: The ``slot[Z].status.measurement.instrument.psu[X].enable`` attribute.
        - ``.event``: The ``slot[Z].status.measurement.instrument.psu[X].event`` attribute.
        - ``.ntr``: The ``slot[Z].status.measurement.instrument.psu[X].ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.measurement.instrument.psu[X].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.measurement.instrument.psu[X].condition`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.psu[X].condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.instrument.psu[X].condition)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

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
        """Access the ``slot[Z].status.measurement.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.psu[X].enable = value
            - print(slot[Z].status.measurement.instrument.psu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

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
        """Access the ``slot[Z].status.measurement.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.psu[X].enable = value
            - print(slot[Z].status.measurement.instrument.psu[X].enable)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

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
        """Access the ``slot[Z].status.measurement.instrument.psu[X].event`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.psu[X].event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.instrument.psu[X].event)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.measurement.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.psu[X].ntr = value
            - print(slot[Z].status.measurement.instrument.psu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.psu[X].ntr = value
            - print(slot[Z].status.measurement.instrument.psu[X].ntr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.measurement.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.psu[X].ptr = value
            - print(slot[Z].status.measurement.instrument.psu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.psu[X].ptr = value
            - print(slot[Z].status.measurement.instrument.psu[X].ptr)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusMeasurementInstrument(BaseTSPCmd):
    """The ``slot[Z].status.measurement.instrument`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.measurement.instrument.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.measurement.instrument.enable`` attribute.
        - ``.event``: The ``slot[Z].status.measurement.instrument.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.measurement.instrument.ntr`` attribute.
        - ``.psu``: The ``slot[Z].status.measurement.instrument.psu[X]`` command tree.
        - ``.ptr``: The ``slot[Z].status.measurement.instrument.ptr`` attribute.
        - ``.smu``: The ``slot[Z].status.measurement.instrument.smu[X]`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._psu: Dict[int, SlotItemStatusMeasurementInstrumentPsuItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SlotItemStatusMeasurementInstrumentPsuItem(
                    device, f"{self._cmd_syntax}.psu[{x}]"
                )
            )
        )
        self._smu: Dict[int, SlotItemStatusMeasurementInstrumentSmuItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SlotItemStatusMeasurementInstrumentSmuItem(
                    device, f"{self._cmd_syntax}.smu[{x}]"
                )
            )
        )

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.measurement.instrument.condition`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.instrument.condition)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.instrument.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.enable = value
            - print(slot[Z].status.measurement.instrument.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.instrument.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.enable = value
            - print(slot[Z].status.measurement.instrument.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.instrument.event`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.instrument.event)
            ```

        Info:
            - ``Z``, the module slot number.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.measurement.instrument.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.ntr = value
            - print(slot[Z].status.measurement.instrument.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.instrument.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.ntr = value
            - print(slot[Z].status.measurement.instrument.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def psu(self) -> Dict[int, SlotItemStatusMeasurementInstrumentPsuItem]:
        """Return the ``slot[Z].status.measurement.instrument.psu[X]`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the PSU: 1 or 2.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.measurement.instrument.psu[X].condition``
              attribute.
            - ``.enable``: The ``slot[Z].status.measurement.instrument.psu[X].enable`` attribute.
            - ``.event``: The ``slot[Z].status.measurement.instrument.psu[X].event`` attribute.
            - ``.ntr``: The ``slot[Z].status.measurement.instrument.psu[X].ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.measurement.instrument.psu[X].ptr`` attribute.
        """
        return self._psu

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.measurement.instrument.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.ptr = value
            - print(slot[Z].status.measurement.instrument.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.instrument.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.instrument.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.instrument.ptr = value
            - print(slot[Z].status.measurement.instrument.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def smu(self) -> Dict[int, SlotItemStatusMeasurementInstrumentSmuItem]:
        """Return the ``slot[Z].status.measurement.instrument.smu[X]`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel of the SMU: 1 or 2.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.measurement.instrument.smu[X].condition``
              attribute.
            - ``.enable``: The ``slot[Z].status.measurement.instrument.smu[X].enable`` attribute.
            - ``.event``: The ``slot[Z].status.measurement.instrument.smu[X].event`` attribute.
            - ``.ntr``: The ``slot[Z].status.measurement.instrument.smu[X].ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.measurement.instrument.smu[X].ptr`` attribute.
        """
        return self._smu


class SlotItemStatusMeasurementCurrentLimit(BaseTSPCmd):
    """The ``slot[Z].status.measurement.current_limit`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.measurement.current_limit.condition`` attribute.
        - ``.enable``: The ``slot[Z].status.measurement.current_limit.enable`` attribute.
        - ``.event``: The ``slot[Z].status.measurement.current_limit.event`` attribute.
        - ``.ntr``: The ``slot[Z].status.measurement.current_limit.ntr`` attribute.
        - ``.ptr``: The ``slot[Z].status.measurement.current_limit.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.measurement.current_limit.condition`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.current_limit.condition)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.current_limit.condition)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.current_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.current_limit.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.current_limit.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.current_limit.enable = value
            - print(slot[Z].status.measurement.current_limit.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.current_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.current_limit.enable)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.current_limit.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.current_limit.enable = value
            - print(slot[Z].status.measurement.current_limit.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.current_limit.event`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.current_limit.event)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.current_limit.event)
            ```

        Info:
            - ``Z``, the module slot number.

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

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.measurement.current_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.current_limit.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.current_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.current_limit.ntr = value
            - print(slot[Z].status.measurement.current_limit.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.current_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.current_limit.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.current_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.current_limit.ntr = value
            - print(slot[Z].status.measurement.current_limit.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.measurement.current_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.current_limit.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.current_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.current_limit.ptr = value
            - print(slot[Z].status.measurement.current_limit.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.current_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].status.measurement.current_limit.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.current_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.current_limit.ptr = value
            - print(slot[Z].status.measurement.current_limit.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemStatusMeasurement(BaseTSPCmd):
    """The ``slot[Z].status.measurement`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.condition``: The ``slot[Z].status.measurement.condition`` attribute.
        - ``.current_limit``: The ``slot[Z].status.measurement.current_limit`` command tree.
        - ``.enable``: The ``slot[Z].status.measurement.enable`` attribute.
        - ``.event``: The ``slot[Z].status.measurement.event`` attribute.
        - ``.instrument``: The ``slot[Z].status.measurement.instrument`` command tree.
        - ``.ntr``: The ``slot[Z].status.measurement.ntr`` attribute.
        - ``.protection``: The ``slot[Z].status.measurement.protection`` command tree.
        - ``.ptr``: The ``slot[Z].status.measurement.ptr`` attribute.
        - ``.reading_overflow``: The ``slot[Z].status.measurement.reading_overflow`` command tree.
        - ``.voltage_limit``: The ``slot[Z].status.measurement.voltage_limit`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._current_limit = SlotItemStatusMeasurementCurrentLimit(
            device, f"{self._cmd_syntax}.current_limit"
        )
        self._instrument = SlotItemStatusMeasurementInstrument(
            device, f"{self._cmd_syntax}.instrument"
        )
        self._protection = SlotItemStatusMeasurementProtection(
            device, f"{self._cmd_syntax}.protection"
        )
        self._reading_overflow = SlotItemStatusMeasurementReadingOverflow(
            device, f"{self._cmd_syntax}.reading_overflow"
        )
        self._voltage_limit = SlotItemStatusMeasurementVoltageLimit(
            device, f"{self._cmd_syntax}.voltage_limit"
        )

    @property
    def condition(self) -> str:
        """Access the ``slot[Z].status.measurement.condition`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.measurement.condition)``
              query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.condition)
            ```

        Info:
            - ``Z``, the module slot number.

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
    def current_limit(self) -> SlotItemStatusMeasurementCurrentLimit:
        """Return the ``slot[Z].status.measurement.current_limit`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.measurement.current_limit.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.measurement.current_limit.enable`` attribute.
            - ``.event``: The ``slot[Z].status.measurement.current_limit.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.measurement.current_limit.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.measurement.current_limit.ptr`` attribute.
        """
        return self._current_limit

    @property
    def enable(self) -> str:
        """Access the ``slot[Z].status.measurement.enable`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.measurement.enable)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.enable = value
            - print(slot[Z].status.measurement.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.enable`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.measurement.enable)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.enable = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.enable = value
            - print(slot[Z].status.measurement.enable)
            ```

        Info:
            - ``Z``, the module slot number.

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
        """Access the ``slot[Z].status.measurement.event`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.measurement.event)``
              query.

        TSP Syntax:
            ```
            - print(slot[Z].status.measurement.event)
            ```

        Info:
            - ``Z``, the module slot number.

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

    @property
    def instrument(self) -> SlotItemStatusMeasurementInstrument:
        """Return the ``slot[Z].status.measurement.instrument`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.measurement.instrument.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.measurement.instrument.enable`` attribute.
            - ``.event``: The ``slot[Z].status.measurement.instrument.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.measurement.instrument.ntr`` attribute.
            - ``.psu``: The ``slot[Z].status.measurement.instrument.psu[X]`` command tree.
            - ``.ptr``: The ``slot[Z].status.measurement.instrument.ptr`` attribute.
            - ``.smu``: The ``slot[Z].status.measurement.instrument.smu[X]`` command tree.
        """
        return self._instrument

    @property
    def ntr(self) -> str:
        """Access the ``slot[Z].status.measurement.ntr`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.measurement.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.ntr = value
            - print(slot[Z].status.measurement.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.ntr`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.measurement.ntr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.ntr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.ntr = value
            - print(slot[Z].status.measurement.ntr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def protection(self) -> SlotItemStatusMeasurementProtection:
        """Return the ``slot[Z].status.measurement.protection`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.measurement.protection.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.measurement.protection.enable`` attribute.
            - ``.event``: The ``slot[Z].status.measurement.protection.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.measurement.protection.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.measurement.protection.ptr`` attribute.
        """
        return self._protection

    @property
    def ptr(self) -> str:
        """Access the ``slot[Z].status.measurement.ptr`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.measurement.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.ptr = value
            - print(slot[Z].status.measurement.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].status.measurement.ptr`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(slot[Z].status.measurement.ptr)`` query.
            - Setting this property to a value will send the
              ``slot[Z].status.measurement.ptr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].status.measurement.ptr = value
            - print(slot[Z].status.measurement.ptr)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def reading_overflow(self) -> SlotItemStatusMeasurementReadingOverflow:
        """Return the ``slot[Z].status.measurement.reading_overflow`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.measurement.reading_overflow.condition``
              attribute.
            - ``.enable``: The ``slot[Z].status.measurement.reading_overflow.enable`` attribute.
            - ``.event``: The ``slot[Z].status.measurement.reading_overflow.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.measurement.reading_overflow.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.measurement.reading_overflow.ptr`` attribute.
        """
        return self._reading_overflow

    @property
    def voltage_limit(self) -> SlotItemStatusMeasurementVoltageLimit:
        """Return the ``slot[Z].status.measurement.voltage_limit`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.measurement.voltage_limit.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.measurement.voltage_limit.enable`` attribute.
            - ``.event``: The ``slot[Z].status.measurement.voltage_limit.event`` attribute.
            - ``.ntr``: The ``slot[Z].status.measurement.voltage_limit.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.measurement.voltage_limit.ptr`` attribute.
        """
        return self._voltage_limit


class SlotItemStatus(BaseTSPCmd):
    """The ``slot[Z].status`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.measurement``: The ``slot[Z].status.measurement`` command tree.
        - ``.operation``: The ``slot[Z].status.operation`` command tree.
        - ``.questionable``: The ``slot[Z].status.questionable`` command tree.
        - ``.reset()``: The ``slot[Z].status.reset()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._measurement = SlotItemStatusMeasurement(device, f"{self._cmd_syntax}.measurement")
        self._operation = SlotItemStatusOperation(device, f"{self._cmd_syntax}.operation")
        self._questionable = SlotItemStatusQuestionable(device, f"{self._cmd_syntax}.questionable")

    @property
    def measurement(self) -> SlotItemStatusMeasurement:
        """Return the ``slot[Z].status.measurement`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.condition``: The ``slot[Z].status.measurement.condition`` attribute.
            - ``.current_limit``: The ``slot[Z].status.measurement.current_limit`` command tree.
            - ``.enable``: The ``slot[Z].status.measurement.enable`` attribute.
            - ``.event``: The ``slot[Z].status.measurement.event`` attribute.
            - ``.instrument``: The ``slot[Z].status.measurement.instrument`` command tree.
            - ``.ntr``: The ``slot[Z].status.measurement.ntr`` attribute.
            - ``.protection``: The ``slot[Z].status.measurement.protection`` command tree.
            - ``.ptr``: The ``slot[Z].status.measurement.ptr`` attribute.
            - ``.reading_overflow``: The ``slot[Z].status.measurement.reading_overflow`` command
              tree.
            - ``.voltage_limit``: The ``slot[Z].status.measurement.voltage_limit`` command tree.
        """
        return self._measurement

    @property
    def operation(self) -> SlotItemStatusOperation:
        """Return the ``slot[Z].status.operation`` command tree.

        Sub-properties and sub-methods:
            - ``.calibrating``: The ``slot[Z].status.operation.calibrating`` command tree.
            - ``.condition``: The ``slot[Z].status.operation.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.operation.enable`` attribute.
            - ``.event``: The ``slot[Z].status.operation.event`` attribute.
            - ``.instrument``: The ``slot[Z].status.operation.instrument`` command tree.
            - ``.measuring``: The ``slot[Z].status.operation.measuring`` command tree.
            - ``.ntr``: The ``slot[Z].status.operation.ntr`` attribute.
            - ``.ptr``: The ``slot[Z].status.operation.ptr`` attribute.
            - ``.sweeping``: The ``slot[Z].status.operation.sweeping`` command tree.
        """
        return self._operation

    @property
    def questionable(self) -> SlotItemStatusQuestionable:
        """Return the ``slot[Z].status.questionable`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.calibration``: The ``slot[Z].status.questionable.calibration`` command tree.
            - ``.condition``: The ``slot[Z].status.questionable.condition`` attribute.
            - ``.enable``: The ``slot[Z].status.questionable.enable`` attribute.
            - ``.event``: The ``slot[Z].status.questionable.event`` attribute.
            - ``.instrument``: The ``slot[Z].status.questionable.instrument`` command tree.
            - ``.ntr``: The ``slot[Z].status.questionable.ntr`` attribute.
            - ``.over_temperature``: The ``slot[Z].status.questionable.over_temperature`` command
              tree.
            - ``.ptr``: The ``slot[Z].status.questionable.ptr`` attribute.
        """
        return self._questionable

    def reset(self) -> None:
        """Run the ``slot[Z].status.reset()`` function.

        Description:
            - This function resets all bits in the status model for the defined slot to default
              values.

        TSP Syntax:
            ```
            - slot[Z].status.reset()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemSmuItemTriggerSource(BaseTSPCmd):
    """The ``slot[Z].smu[X].trigger.source`` command tree.

    Properties and methods:
        - ``.lineari()``: The ``slot[Z].smu[X].trigger.source.lineari()`` function.
        - ``.linearv()``: The ``slot[Z].smu[X].trigger.source.linearv()`` function.
        - ``.listi()``: The ``slot[Z].smu[X].trigger.source.listi()`` function.
        - ``.listv()``: The ``slot[Z].smu[X].trigger.source.listv()`` function.
        - ``.logi()``: The ``slot[Z].smu[X].trigger.source.logi()`` function.
        - ``.logv()``: The ``slot[Z].smu[X].trigger.source.logv()`` function.
    """

    def lineari(self, start: str, end: str, points: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.source.lineari()`` function.

        Description:
            - This function configures the linear sweep for the trigger model. (i = current in
              amperes)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.source.lineari()
            ```

        Args:
            start: Start source level.
            end: End source level.
            points: Number of points used to calculate the step size.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.lineari({start}, {end}, {points})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.lineari()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def linearv(self, start: str, end: str, points: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.source.linearv()`` function.

        Description:
            - This function configures the linear sweep for the trigger model. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.source.linearv()
            ```

        Args:
            start: Start source level.
            end: End source level.
            points: Number of points used to calculate the step size.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.linearv({start}, {end}, {points})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.linearv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def listi(self, source_levels: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.source.listi()`` function.

        Description:
            - This function configures the list sweep for the trigger model. (i = current in
              amperes)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.source.listi()
            ```

        Args:
            source_levels: List of source levels; see Details.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.listi({source_levels})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.listi()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def listv(self, source_levels: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.source.listv()`` function.

        Description:
            - This function configures the list sweep for the trigger model. (v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.source.listv()
            ```

        Args:
            source_levels: List of source levels; see Details.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.listv({source_levels})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.listv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def logi(self, start: str, end: str, points: str, asymptote: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.source.logi()`` function.

        Description:
            - This function configures a logarithmic sweep for the trigger model. (i = current in
              amperes)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.source.logi()
            ```

        Args:
            start: Start source level.
            end: End source level.
            points: Number of points used to calculate the step size.
            asymptote: The asymptotic offset value (optional).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.logi({start}, {end}, {points}, {asymptote})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.logi()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def logv(self, start: str, end: str, points: str, asymptote: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.source.logv()`` function.

        Description:
            - This function configures a logarithmic sweep for the trigger model. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.source.logv()
            ```

        Args:
            start: Start source level.
            end: End source level.
            points: Number of points used to calculate the step size.
            asymptote: The asymptotic offset value (optional).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.logv({start}, {end}, {points}, {asymptote})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.logv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemSmuItemTriggerMeasure(BaseTSPCmd):
    """The ``slot[Z].smu[X].trigger.measure`` command tree.

    Properties and methods:
        - ``.i()``: The ``slot[Z].smu[X].trigger.measure.i()`` function.
        - ``.iv()``: The ``slot[Z].smu[X].trigger.measure.iv()`` function.
        - ``.p()``: The ``slot[Z].smu[X].trigger.measure.p()`` function.
        - ``.r()``: The ``slot[Z].smu[X].trigger.measure.r()`` function.
        - ``.v()``: The ``slot[Z].smu[X].trigger.measure.v()`` function.
    """

    def i(self, reading_buffer: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.measure.i()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (i
              = current in amperes)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.measure.i()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.i({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.i()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def iv(self, ibuffer: str, vbuffer: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.measure.iv()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (i
              = current in amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.measure.iv()
            ```

        Args:
            ibuffer: Buffer to store current readings.
            vbuffer: Buffer to store voltage readings.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.iv({ibuffer}, {vbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.iv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def p(self, reading_buffer: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.measure.p()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (p
              = power in watts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.measure.p()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.p({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.p()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def r(self, reading_buffer: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.measure.r()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (r
              = resistance in ohms)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.measure.r()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.r({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.r()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def v(self, reading_buffer: str) -> None:
        """Run the ``slot[Z].smu[X].trigger.measure.v()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (v
              = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].trigger.measure.v()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.v({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.v()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemSmuItemTrigger(BaseTSPCmd):
    """The ``slot[Z].smu[X].trigger`` command tree.

    Properties and methods:
        - ``.measure``: The ``slot[Z].smu[X].trigger.measure`` command tree.
        - ``.source``: The ``slot[Z].smu[X].trigger.source`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._measure = SlotItemSmuItemTriggerMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = SlotItemSmuItemTriggerSource(device, f"{self._cmd_syntax}.source")

    @property
    def measure(self) -> SlotItemSmuItemTriggerMeasure:
        """Return the ``slot[Z].smu[X].trigger.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.i()``: The ``slot[Z].smu[X].trigger.measure.i()`` function.
            - ``.iv()``: The ``slot[Z].smu[X].trigger.measure.iv()`` function.
            - ``.p()``: The ``slot[Z].smu[X].trigger.measure.p()`` function.
            - ``.r()``: The ``slot[Z].smu[X].trigger.measure.r()`` function.
            - ``.v()``: The ``slot[Z].smu[X].trigger.measure.v()`` function.
        """
        return self._measure

    @property
    def source(self) -> SlotItemSmuItemTriggerSource:
        """Return the ``slot[Z].smu[X].trigger.source`` command tree.

        Sub-properties and sub-methods:
            - ``.lineari()``: The ``slot[Z].smu[X].trigger.source.lineari()`` function.
            - ``.linearv()``: The ``slot[Z].smu[X].trigger.source.linearv()`` function.
            - ``.listi()``: The ``slot[Z].smu[X].trigger.source.listi()`` function.
            - ``.listv()``: The ``slot[Z].smu[X].trigger.source.listv()`` function.
            - ``.logi()``: The ``slot[Z].smu[X].trigger.source.logi()`` function.
            - ``.logv()``: The ``slot[Z].smu[X].trigger.source.logv()`` function.
        """
        return self._source


#  pylint: disable=too-many-public-methods
class SlotItemSmuItemSource(BaseTSPCmd):
    """The ``slot[Z].smu[X].source`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the module channel number.

    Properties and methods:
        - ``.autodelay``: The ``slot[Z].smu[X].source.autodelay`` attribute.
        - ``.autorangei``: The ``slot[Z].smu[X].source.autorangei`` attribute.
        - ``.autorangev``: The ``slot[Z].smu[X].source.autorangev`` attribute.
        - ``.constantcurrent``: The ``slot[Z].smu[X].source.constantcurrent`` attribute.
        - ``.delay``: The ``slot[Z].smu[X].source.delay`` attribute.
        - ``.func``: The ``slot[Z].smu[X].source.func`` attribute.
        - ``.leveli``: The ``slot[Z].smu[X].source.leveli`` attribute.
        - ``.levelv``: The ``slot[Z].smu[X].source.levelv`` attribute.
        - ``.limiti``: The ``slot[Z].smu[X].source.limiti`` attribute.
        - ``.limitv``: The ``slot[Z].smu[X].source.limitv`` attribute.
        - ``.limitni``: The ``slot[Z].smu[X].source.limitni`` attribute.
        - ``.limitnv``: The ``slot[Z].smu[X].source.limitnv`` attribute.
        - ``.limitpi``: The ``slot[Z].smu[X].source.limitpi`` attribute.
        - ``.limitpv``: The ``slot[Z].smu[X].source.limitpv`` attribute.
        - ``.lowrangei``: The ``slot[Z].smu[X].source.lowrangei`` attribute.
        - ``.lowrangev``: The ``slot[Z].smu[X].source.lowrangev`` attribute.
        - ``.offfunc``: The ``slot[Z].smu[X].source.offfunc`` attribute.
        - ``.offlimiti``: The ``slot[Z].smu[X].source.offlimiti`` attribute.
        - ``.offlimitv``: The ``slot[Z].smu[X].source.offlimitv`` attribute.
        - ``.offlimitni``: The ``slot[Z].smu[X].source.offlimitni`` attribute.
        - ``.offlimitnv``: The ``slot[Z].smu[X].source.offlimitnv`` attribute.
        - ``.offlimitpi``: The ``slot[Z].smu[X].source.offlimitpi`` attribute.
        - ``.offlimitpv``: The ``slot[Z].smu[X].source.offlimitpv`` attribute.
        - ``.offmode``: The ``slot[Z].smu[X].source.offmode`` attribute.
        - ``.output``: The ``slot[Z].smu[X].source.output`` attribute.
        - ``.rangei``: The ``slot[Z].smu[X].source.rangei`` attribute.
        - ``.rangev``: The ``slot[Z].smu[X].source.rangev`` attribute.
    """

    @property
    def autodelay(self) -> str:
        """Access the ``slot[Z].smu[X].source.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic delay that occurs when the source is
              changed.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.autodelay)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.autodelay = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.autodelay = value
            - print(slot[Z].smu[X].source.autodelay)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autodelay"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autodelay)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autodelay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autodelay.setter
    def autodelay(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic delay that occurs when the source is
              changed.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.autodelay)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.autodelay = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.autodelay = value
            - print(slot[Z].smu[X].source.autodelay)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autodelay", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autodelay = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autodelay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autorangei(self) -> str:
        """Access the ``slot[Z].smu[X].source.autorangei`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on or off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.autorangei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.autorangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.autorangei = value
            - print(slot[Z].smu[X].source.autorangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorangei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorangei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorangei.setter
    def autorangei(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.autorangei`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on or off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.autorangei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.autorangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.autorangei = value
            - print(slot[Z].smu[X].source.autorangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorangei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorangei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autorangev(self) -> str:
        """Access the ``slot[Z].smu[X].source.autorangev`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on or off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.autorangev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.autorangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.autorangev = value
            - print(slot[Z].smu[X].source.autorangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorangev.setter
    def autorangev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.autorangev`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on or off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.autorangev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.autorangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.autorangev = value
            - print(slot[Z].smu[X].source.autorangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorangev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorangev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def constantcurrent(self) -> str:
        """Access the ``slot[Z].smu[X].source.constantcurrent`` attribute.

        Description:
            - This attribute indicates when the source is within the current limit.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.constantcurrent)``
              query.

        TSP Syntax:
            ```
            - print(slot[Z].smu[X].source.constantcurrent)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".constantcurrent"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.constantcurrent)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.constantcurrent`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def delay(self) -> str:
        """Access the ``slot[Z].smu[X].source.delay`` attribute.

        Description:
            - This attribute contains the delay that occurs when the source is changed.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.delay)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].source.delay = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.delay = value
            - print(slot[Z].smu[X].source.delay)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".delay"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.delay)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @delay.setter
    def delay(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.delay`` attribute.

        Description:
            - This attribute contains the delay that occurs when the source is changed.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.delay)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].source.delay = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.delay = value
            - print(slot[Z].smu[X].source.delay)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".delay", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.delay = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def func(self) -> str:
        """Access the ``slot[Z].smu[X].source.func`` attribute.

        Description:
            - This attribute configures the source function as either voltage source or current
              source.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.func)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].source.func = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.func = value
            - print(slot[Z].smu[X].source.func)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".func"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.func)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @func.setter
    def func(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.func`` attribute.

        Description:
            - This attribute configures the source function as either voltage source or current
              source.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.func)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].source.func = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.func = value
            - print(slot[Z].smu[X].source.func)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".func", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.func = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def leveli(self) -> str:
        """Access the ``slot[Z].smu[X].source.leveli`` attribute.

        Description:
            - This attribute configures the source level setting. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.leveli)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.leveli = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.leveli = value
            - print(slot[Z].smu[X].source.leveli)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".leveli"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.leveli)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @leveli.setter
    def leveli(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.leveli`` attribute.

        Description:
            - This attribute configures the source level setting. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.leveli)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.leveli = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.leveli = value
            - print(slot[Z].smu[X].source.leveli)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".leveli", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.leveli = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelv(self) -> str:
        """Access the ``slot[Z].smu[X].source.levelv`` attribute.

        Description:
            - This attribute configures the source level setting. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.levelv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.levelv = value
            - print(slot[Z].smu[X].source.levelv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelv.setter
    def levelv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.levelv`` attribute.

        Description:
            - This attribute configures the source level setting. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.levelv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.levelv = value
            - print(slot[Z].smu[X].source.levelv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limiti(self) -> str:
        """Access the ``slot[Z].smu[X].source.limiti`` attribute.

        Description:
            - This attribute symmetrically configures both the positive and the negative source
              limit settings. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limiti)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limiti = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limiti = value
            - print(slot[Z].smu[X].source.limiti)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".limiti"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.limiti)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limiti`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @limiti.setter
    def limiti(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.limiti`` attribute.

        Description:
            - This attribute symmetrically configures both the positive and the negative source
              limit settings. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limiti)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limiti = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limiti = value
            - print(slot[Z].smu[X].source.limiti)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".limiti", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.limiti = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limiti`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limitv(self) -> str:
        """Access the ``slot[Z].smu[X].source.limitv`` attribute.

        Description:
            - This attribute symmetrically configures both the positive and the negative source
              limit settings. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitv = value
            - print(slot[Z].smu[X].source.limitv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".limitv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.limitv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @limitv.setter
    def limitv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.limitv`` attribute.

        Description:
            - This attribute symmetrically configures both the positive and the negative source
              limit settings. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitv = value
            - print(slot[Z].smu[X].source.limitv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".limitv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.limitv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limitni(self) -> str:
        """Access the ``slot[Z].smu[X].source.limitni`` attribute.

        Description:
            - This attribute configures the negative source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitni)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitni = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitni = value
            - print(slot[Z].smu[X].source.limitni)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".limitni"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.limitni)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitni`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @limitni.setter
    def limitni(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.limitni`` attribute.

        Description:
            - This attribute configures the negative source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitni)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitni = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitni = value
            - print(slot[Z].smu[X].source.limitni)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".limitni", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.limitni = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitni`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limitnv(self) -> str:
        """Access the ``slot[Z].smu[X].source.limitnv`` attribute.

        Description:
            - This attribute configures the negative source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitnv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitnv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitnv = value
            - print(slot[Z].smu[X].source.limitnv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".limitnv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.limitnv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitnv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @limitnv.setter
    def limitnv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.limitnv`` attribute.

        Description:
            - This attribute configures the negative source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitnv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitnv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitnv = value
            - print(slot[Z].smu[X].source.limitnv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".limitnv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.limitnv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitnv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limitpi(self) -> str:
        """Access the ``slot[Z].smu[X].source.limitpi`` attribute.

        Description:
            - This attribute configures the positive source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitpi)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitpi = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitpi = value
            - print(slot[Z].smu[X].source.limitpi)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".limitpi"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.limitpi)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitpi`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @limitpi.setter
    def limitpi(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.limitpi`` attribute.

        Description:
            - This attribute configures the positive source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitpi)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitpi = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitpi = value
            - print(slot[Z].smu[X].source.limitpi)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".limitpi", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.limitpi = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitpi`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limitpv(self) -> str:
        """Access the ``slot[Z].smu[X].source.limitpv`` attribute.

        Description:
            - This attribute configures the positive source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitpv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitpv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitpv = value
            - print(slot[Z].smu[X].source.limitpv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".limitpv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.limitpv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitpv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @limitpv.setter
    def limitpv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.limitpv`` attribute.

        Description:
            - This attribute configures the positive source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.limitpv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.limitpv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.limitpv = value
            - print(slot[Z].smu[X].source.limitpv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".limitpv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.limitpv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitpv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def lowrangei(self) -> str:
        """Access the ``slot[Z].smu[X].source.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest source range that will be used during autoranging. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.lowrangei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.lowrangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.lowrangei = value
            - print(slot[Z].smu[X].source.lowrangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".lowrangei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.lowrangei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lowrangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @lowrangei.setter
    def lowrangei(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest source range that will be used during autoranging. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.lowrangei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.lowrangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.lowrangei = value
            - print(slot[Z].smu[X].source.lowrangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".lowrangei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.lowrangei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lowrangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def lowrangev(self) -> str:
        """Access the ``slot[Z].smu[X].source.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest source range that will be used during autoranging. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.lowrangev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.lowrangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.lowrangev = value
            - print(slot[Z].smu[X].source.lowrangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".lowrangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.lowrangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lowrangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @lowrangev.setter
    def lowrangev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest source range that will be used during autoranging. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.lowrangev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.lowrangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.lowrangev = value
            - print(slot[Z].smu[X].source.lowrangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".lowrangev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.lowrangev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lowrangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offfunc(self) -> str:
        """Access the ``slot[Z].smu[X].source.offfunc`` attribute.

        Description:
            - This attribute sets the source function used (source 0 A or 0 V) when the output is
              turned off and the source-measure-unit (SMU) is in normal output-off mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offfunc)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offfunc = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offfunc = value
            - print(slot[Z].smu[X].source.offfunc)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offfunc"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offfunc)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offfunc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offfunc.setter
    def offfunc(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.offfunc`` attribute.

        Description:
            - This attribute sets the source function used (source 0 A or 0 V) when the output is
              turned off and the source-measure-unit (SMU) is in normal output-off mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offfunc)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offfunc = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offfunc = value
            - print(slot[Z].smu[X].source.offfunc)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offfunc", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offfunc = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offfunc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offlimiti(self) -> str:
        """Access the ``slot[Z].smu[X].source.offlimiti`` attribute.

        Description:
            - This attribute configures both the positive and negative source off limit settings
              symmetrically. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimiti)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimiti = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimiti = value
            - print(slot[Z].smu[X].source.offlimiti)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offlimiti"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offlimiti)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimiti`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offlimiti.setter
    def offlimiti(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.offlimiti`` attribute.

        Description:
            - This attribute configures both the positive and negative source off limit settings
              symmetrically. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimiti)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimiti = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimiti = value
            - print(slot[Z].smu[X].source.offlimiti)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offlimiti", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offlimiti = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimiti`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offlimitv(self) -> str:
        """Access the ``slot[Z].smu[X].source.offlimitv`` attribute.

        Description:
            - This attribute configures both the positive and negative source off limit settings
              symmetrically. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitv = value
            - print(slot[Z].smu[X].source.offlimitv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offlimitv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offlimitv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offlimitv.setter
    def offlimitv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.offlimitv`` attribute.

        Description:
            - This attribute configures both the positive and negative source off limit settings
              symmetrically. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitv = value
            - print(slot[Z].smu[X].source.offlimitv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offlimitv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offlimitv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offlimitni(self) -> str:
        """Access the ``slot[Z].smu[X].source.offlimitni`` attribute.

        Description:
            - This attribute configures the negative source off limit setting. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitni)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitni = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitni = value
            - print(slot[Z].smu[X].source.offlimitni)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offlimitni"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offlimitni)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitni`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offlimitni.setter
    def offlimitni(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.offlimitni`` attribute.

        Description:
            - This attribute configures the negative source off limit setting. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitni)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitni = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitni = value
            - print(slot[Z].smu[X].source.offlimitni)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offlimitni", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offlimitni = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitni`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offlimitnv(self) -> str:
        """Access the ``slot[Z].smu[X].source.offlimitnv`` attribute.

        Description:
            - This attribute configures the negative source off limit setting. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitnv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitnv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitnv = value
            - print(slot[Z].smu[X].source.offlimitnv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offlimitnv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offlimitnv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitnv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offlimitnv.setter
    def offlimitnv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.offlimitnv`` attribute.

        Description:
            - This attribute configures the negative source off limit setting. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitnv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitnv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitnv = value
            - print(slot[Z].smu[X].source.offlimitnv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offlimitnv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offlimitnv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitnv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offlimitpi(self) -> str:
        """Access the ``slot[Z].smu[X].source.offlimitpi`` attribute.

        Description:
            - This attribute configures the positive source off limit setting. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitpi)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitpi = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitpi = value
            - print(slot[Z].smu[X].source.offlimitpi)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offlimitpi"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offlimitpi)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitpi`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offlimitpi.setter
    def offlimitpi(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.offlimitpi`` attribute.

        Description:
            - This attribute configures the positive source off limit setting. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitpi)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitpi = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitpi = value
            - print(slot[Z].smu[X].source.offlimitpi)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offlimitpi", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offlimitpi = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitpi`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offlimitpv(self) -> str:
        """Access the ``slot[Z].smu[X].source.offlimitpv`` attribute.

        Description:
            - This attribute configures the positive source off limit setting. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitpv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitpv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitpv = value
            - print(slot[Z].smu[X].source.offlimitpv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offlimitpv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offlimitpv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitpv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offlimitpv.setter
    def offlimitpv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.offlimitpv`` attribute.

        Description:
            - This attribute configures the positive source off limit setting. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offlimitpv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offlimitpv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offlimitpv = value
            - print(slot[Z].smu[X].source.offlimitpv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offlimitpv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offlimitpv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offlimitpv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offmode(self) -> str:
        """Access the ``slot[Z].smu[X].source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offmode)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offmode = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offmode = value
            - print(slot[Z].smu[X].source.offmode)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offmode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offmode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offmode.setter
    def offmode(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.offmode)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.offmode = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.offmode = value
            - print(slot[Z].smu[X].source.offmode)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offmode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offmode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def output(self) -> str:
        """Access the ``slot[Z].smu[X].source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.output)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.output = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.output = value
            - print(slot[Z].smu[X].source.output)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".output"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.output)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.output`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @output.setter
    def output(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.output)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.output = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.output = value
            - print(slot[Z].smu[X].source.output)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".output", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.output = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.output`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rangei(self) -> str:
        """Access the ``slot[Z].smu[X].source.rangei`` attribute.

        Description:
            - This attribute configures the source range setting to be fixed for function Y. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.rangei)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.rangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.rangei = value
            - print(slot[Z].smu[X].source.rangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rangei.setter
    def rangei(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.rangei`` attribute.

        Description:
            - This attribute configures the source range setting to be fixed for function Y. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.rangei)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.rangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.rangei = value
            - print(slot[Z].smu[X].source.rangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rangei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rangei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rangev(self) -> str:
        """Access the ``slot[Z].smu[X].source.rangev`` attribute.

        Description:
            - This attribute configures the source range setting to be fixed for function Y. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.rangev)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.rangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.rangev = value
            - print(slot[Z].smu[X].source.rangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rangev.setter
    def rangev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].source.rangev`` attribute.

        Description:
            - This attribute configures the source range setting to be fixed for function Y. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].source.rangev)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].source.rangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].source.rangev = value
            - print(slot[Z].smu[X].source.rangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rangev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rangev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemSmuItemMeasureRel(BaseTSPCmd):
    """The ``slot[Z].smu[X].measure.rel`` command tree.

    Properties and methods:
        - ``.enablei``: The ``slot[Z].smu[X].measure.rel.enablei`` attribute.
        - ``.enablep``: The ``slot[Z].smu[X].measure.rel.enablep`` attribute.
        - ``.enabler``: The ``slot[Z].smu[X].measure.rel.enabler`` attribute.
        - ``.enablev``: The ``slot[Z].smu[X].measure.rel.enablev`` attribute.
        - ``.leveli``: The ``slot[Z].smu[X].measure.rel.leveli`` attribute.
        - ``.levelp``: The ``slot[Z].smu[X].measure.rel.levelp`` attribute.
        - ``.levelr``: The ``slot[Z].smu[X].measure.rel.levelr`` attribute.
        - ``.levelv``: The ``slot[Z].smu[X].measure.rel.levelv`` attribute.
    """

    @property
    def enablei(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.enablei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.enablei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.enablei = value
            - print(slot[Z].smu[X].measure.rel.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablei.setter
    def enablei(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.enablei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.enablei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.enablei = value
            - print(slot[Z].smu[X].measure.rel.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enablep(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.enablep)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.enablep = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.enablep = value
            - print(slot[Z].smu[X].measure.rel.enablep)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablep"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablep)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablep`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablep.setter
    def enablep(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.enablep)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.enablep = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.enablep = value
            - print(slot[Z].smu[X].measure.rel.enablep)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablep", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablep = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablep`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enabler(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.enabler)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.enabler = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.enabler = value
            - print(slot[Z].smu[X].measure.rel.enabler)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enabler"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enabler)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enabler`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enabler.setter
    def enabler(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.enabler)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.enabler = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.enabler = value
            - print(slot[Z].smu[X].measure.rel.enabler)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enabler", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enabler = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enabler`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enablev(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.enablev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.enablev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.enablev = value
            - print(slot[Z].smu[X].measure.rel.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablev.setter
    def enablev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.enablev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.enablev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.enablev = value
            - print(slot[Z].smu[X].measure.rel.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def leveli(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rel.leveli`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.leveli)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.leveli = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.leveli = value
            - print(slot[Z].smu[X].measure.rel.leveli)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".leveli"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.leveli)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @leveli.setter
    def leveli(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.rel.leveli`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.leveli)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.leveli = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.leveli = value
            - print(slot[Z].smu[X].measure.rel.leveli)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".leveli", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.leveli = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelp(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rel.levelp`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (p = power in
              watts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.levelp)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.levelp = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.levelp = value
            - print(slot[Z].smu[X].measure.rel.levelp)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelp"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelp)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelp.setter
    def levelp(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.rel.levelp`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (p = power in
              watts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.levelp)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.levelp = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.levelp = value
            - print(slot[Z].smu[X].measure.rel.levelp)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelp", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelp = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelr(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rel.levelr`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (r = resistance
              in ohms)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.levelr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.levelr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.levelr = value
            - print(slot[Z].smu[X].measure.rel.levelr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelr.setter
    def levelr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.rel.levelr`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (r = resistance
              in ohms)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.levelr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.levelr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.levelr = value
            - print(slot[Z].smu[X].measure.rel.levelr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelv(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rel.levelv`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.levelv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.levelv = value
            - print(slot[Z].smu[X].measure.rel.levelv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelv.setter
    def levelv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.rel.levelv`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rel.levelv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.rel.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.rel.levelv = value
            - print(slot[Z].smu[X].measure.rel.levelv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


#  pylint: disable=too-many-public-methods
class SlotItemSmuItemMeasure(BaseTSPCmd):
    """The ``slot[Z].smu[X].measure`` command tree.

    Properties and methods:
        - ``.i()``: The ``slot[Z].smu[X].measure.i()`` function.
        - ``.p()``: The ``slot[Z].smu[X].measure.p()`` function.
        - ``.r()``: The ``slot[Z].smu[X].measure.r()`` function.
        - ``.v()``: The ``slot[Z].smu[X].measure.v()`` function.
        - ``.aperture``: The ``slot[Z].smu[X].measure.aperture`` attribute.
        - ``.autodelay``: The ``slot[Z].smu[X].measure.autodelay`` attribute.
        - ``.autorangei``: The ``slot[Z].smu[X].measure.autorangei`` attribute.
        - ``.autorangev``: The ``slot[Z].smu[X].measure.autorangev`` attribute.
        - ``.count``: The ``slot[Z].smu[X].measure.count`` attribute.
        - ``.delay``: The ``slot[Z].smu[X].measure.delay`` attribute.
        - ``.interval``: The ``slot[Z].smu[X].measure.interval`` attribute.
        - ``.lowrangei``: The ``slot[Z].smu[X].measure.lowrangei`` attribute.
        - ``.lowrangev``: The ``slot[Z].smu[X].measure.lowrangev`` attribute.
        - ``.nplc``: The ``slot[Z].smu[X].measure.nplc`` attribute.
        - ``.overlappedi()``: The ``slot[Z].smu[X].measure.overlappedi()`` function.
        - ``.overlappediv()``: The ``slot[Z].smu[X].measure.overlappediv()`` function.
        - ``.overlappedp()``: The ``slot[Z].smu[X].measure.overlappedp()`` function.
        - ``.overlappedr()``: The ``slot[Z].smu[X].measure.overlappedr()`` function.
        - ``.overlappedv()``: The ``slot[Z].smu[X].measure.overlappedv()`` function.
        - ``.rangei``: The ``slot[Z].smu[X].measure.rangei`` attribute.
        - ``.rangev``: The ``slot[Z].smu[X].measure.rangev`` attribute.
        - ``.rel``: The ``slot[Z].smu[X].measure.rel`` command tree.
        - ``.tempcomp``: The ``slot[Z].smu[X].measure.tempcomp`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rel = SlotItemSmuItemMeasureRel(device, f"{self._cmd_syntax}.rel")

    @property
    def aperture(self) -> str:
        """Access the ``slot[Z].smu[X].measure.aperture`` attribute.

        Description:
            - This attribute configures the measurement aperture for a channel in seconds.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.aperture)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.aperture = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.aperture = value
            - print(slot[Z].smu[X].measure.aperture)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".aperture"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.aperture)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.aperture`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @aperture.setter
    def aperture(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.aperture`` attribute.

        Description:
            - This attribute configures the measurement aperture for a channel in seconds.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.aperture)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.aperture = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.aperture = value
            - print(slot[Z].smu[X].measure.aperture)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".aperture", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.aperture = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.aperture`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autodelay(self) -> str:
        """Access the ``slot[Z].smu[X].measure.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic measurement delay.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.autodelay)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.autodelay = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.autodelay = value
            - print(slot[Z].smu[X].measure.autodelay)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autodelay"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autodelay)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autodelay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autodelay.setter
    def autodelay(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic measurement delay.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.autodelay)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.autodelay = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.autodelay = value
            - print(slot[Z].smu[X].measure.autodelay)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autodelay", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autodelay = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autodelay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autorangei(self) -> str:
        """Access the ``slot[Z].smu[X].measure.autorangei`` attribute.

        Description:
            - This attribute contains the state of the measure autorange control (on or off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.autorangei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.autorangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.autorangei = value
            - print(slot[Z].smu[X].measure.autorangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorangei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorangei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorangei.setter
    def autorangei(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.autorangei`` attribute.

        Description:
            - This attribute contains the state of the measure autorange control (on or off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.autorangei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.autorangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.autorangei = value
            - print(slot[Z].smu[X].measure.autorangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorangei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorangei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autorangev(self) -> str:
        """Access the ``slot[Z].smu[X].measure.autorangev`` attribute.

        Description:
            - This attribute contains the state of the measure autorange control (on or off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.autorangev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.autorangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.autorangev = value
            - print(slot[Z].smu[X].measure.autorangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorangev.setter
    def autorangev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.autorangev`` attribute.

        Description:
            - This attribute contains the state of the measure autorange control (on or off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.autorangev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.autorangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.autorangev = value
            - print(slot[Z].smu[X].measure.autorangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorangev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorangev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def count(self) -> str:
        """Access the ``slot[Z].smu[X].measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements performed when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.count)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.count = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.count = value
            - print(slot[Z].smu[X].measure.count)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".count"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.count)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @count.setter
    def count(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements performed when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.count)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.count = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.count = value
            - print(slot[Z].smu[X].measure.count)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".count", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.count = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def delay(self) -> str:
        """Access the ``slot[Z].smu[X].measure.delay`` attribute.

        Description:
            - This attribute controls the measurement delay.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.delay)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.delay = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.delay = value
            - print(slot[Z].smu[X].measure.delay)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".delay"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.delay)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @delay.setter
    def delay(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.delay`` attribute.

        Description:
            - This attribute controls the measurement delay.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.delay)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.delay = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.delay = value
            - print(slot[Z].smu[X].measure.delay)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".delay", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.delay = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def interval(self) -> str:
        """Access the ``slot[Z].smu[X].measure.interval`` attribute.

        Description:
            - This attribute sets the interval between multiple measurements.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.interval)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.interval = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.interval = value
            - print(slot[Z].smu[X].measure.interval)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".interval"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.interval)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.interval`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @interval.setter
    def interval(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.interval`` attribute.

        Description:
            - This attribute sets the interval between multiple measurements.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.interval)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.interval = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.interval = value
            - print(slot[Z].smu[X].measure.interval)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".interval", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.interval = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.interval`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def lowrangei(self) -> str:
        """Access the ``slot[Z].smu[X].measure.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest measurement range to be used when the instrument is
              autoranging. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.lowrangei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.lowrangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.lowrangei = value
            - print(slot[Z].smu[X].measure.lowrangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".lowrangei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.lowrangei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lowrangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @lowrangei.setter
    def lowrangei(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest measurement range to be used when the instrument is
              autoranging. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.lowrangei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.lowrangei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.lowrangei = value
            - print(slot[Z].smu[X].measure.lowrangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".lowrangei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.lowrangei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lowrangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def lowrangev(self) -> str:
        """Access the ``slot[Z].smu[X].measure.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest measurement range to be used when the instrument is
              autoranging. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.lowrangev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.lowrangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.lowrangev = value
            - print(slot[Z].smu[X].measure.lowrangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".lowrangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.lowrangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lowrangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @lowrangev.setter
    def lowrangev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest measurement range to be used when the instrument is
              autoranging. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.lowrangev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.lowrangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.lowrangev = value
            - print(slot[Z].smu[X].measure.lowrangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".lowrangev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.lowrangev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lowrangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def nplc(self) -> str:
        """Access the ``slot[Z].smu[X].measure.nplc`` attribute.

        Description:
            - This command sets the time that the input signal is measured in number of power line
              cycles.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.nplc)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].measure.nplc = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.nplc = value
            - print(slot[Z].smu[X].measure.nplc)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".nplc"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.nplc)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.nplc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @nplc.setter
    def nplc(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.nplc`` attribute.

        Description:
            - This command sets the time that the input signal is measured in number of power line
              cycles.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.nplc)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].measure.nplc = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.nplc = value
            - print(slot[Z].smu[X].measure.nplc)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".nplc", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.nplc = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.nplc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rangei(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rangei`` attribute.

        Description:
            - This attribute contains the positive, full scale value of the measurement range for
              voltage or current. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rangei)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].smu[X].measure.rangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rangev(self) -> str:
        """Access the ``slot[Z].smu[X].measure.rangev`` attribute.

        Description:
            - This attribute contains the positive, full scale value of the measurement range for
              voltage or current. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.rangev)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].smu[X].measure.rangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rel(self) -> SlotItemSmuItemMeasureRel:
        """Return the ``slot[Z].smu[X].measure.rel`` command tree.

        Sub-properties and sub-methods:
            - ``.enablei``: The ``slot[Z].smu[X].measure.rel.enablei`` attribute.
            - ``.enablep``: The ``slot[Z].smu[X].measure.rel.enablep`` attribute.
            - ``.enabler``: The ``slot[Z].smu[X].measure.rel.enabler`` attribute.
            - ``.enablev``: The ``slot[Z].smu[X].measure.rel.enablev`` attribute.
            - ``.leveli``: The ``slot[Z].smu[X].measure.rel.leveli`` attribute.
            - ``.levelp``: The ``slot[Z].smu[X].measure.rel.levelp`` attribute.
            - ``.levelr``: The ``slot[Z].smu[X].measure.rel.levelr`` attribute.
            - ``.levelv``: The ``slot[Z].smu[X].measure.rel.levelv`` attribute.
        """
        return self._rel

    @property
    def tempcomp(self) -> str:
        """Access the ``slot[Z].smu[X].measure.tempcomp`` attribute.

        Description:
            - This attribute turns temperature compensation on or off for the current measurements.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.tempcomp)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.tempcomp = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.tempcomp = value
            - print(slot[Z].smu[X].measure.tempcomp)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".tempcomp"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.tempcomp)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tempcomp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @tempcomp.setter
    def tempcomp(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].measure.tempcomp`` attribute.

        Description:
            - This attribute turns temperature compensation on or off for the current measurements.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].measure.tempcomp)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].measure.tempcomp = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.tempcomp = value
            - print(slot[Z].smu[X].measure.tempcomp)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".tempcomp", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.tempcomp = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tempcomp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def i(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``slot[Z].smu[X].measure.i()`` function.

        Description:
            - This function makes one or more measurements. (i = current in amperes)

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.i()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.i({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.i()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def p(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``slot[Z].smu[X].measure.p()`` function.

        Description:
            - This function makes one or more measurements. (p = power in watts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.p()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.p({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.p()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def r(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``slot[Z].smu[X].measure.r()`` function.

        Description:
            - This function makes one or more measurements. (r = resistance in ohms)

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.r()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.r({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.r()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def v(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``slot[Z].smu[X].measure.v()`` function.

        Description:
            - This function makes one or more measurements. (v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.v()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.v({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.v()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedi(self, rbuffer: str) -> None:
        """Run the ``slot[Z].smu[X].measure.overlappedi()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes)

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.overlappedi()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedi({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedi()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappediv(self, ibuffer: str, vbuffer: str) -> None:
        """Run the ``slot[Z].smu[X].measure.overlappediv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.overlappediv()
            ```

        Args:
            ibuffer: A reading buffer object where current readings are stored.
            vbuffer: A reading buffer object where voltage readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappediv({ibuffer}, {vbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappediv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedp(self, rbuffer: str) -> None:
        """Run the ``slot[Z].smu[X].measure.overlappedp()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (p = power in watts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.overlappedp()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedp({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedp()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedr(self, rbuffer: str) -> None:
        """Run the ``slot[Z].smu[X].measure.overlappedr()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (r = resistance in
              ohms)

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.overlappedr()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedr({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedr()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedv(self, rbuffer: str) -> None:
        """Run the ``slot[Z].smu[X].measure.overlappedv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].smu[X].measure.overlappedv()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedv({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemSmuItemGuard(BaseTSPCmd):
    """The ``slot[Z].smu[X].guard`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the module channel number.

    Properties and methods:
        - ``.v()``: The ``slot[Z].smu[X].guard.v()`` function.
    """

    def v(self) -> str:
        """Run the ``slot[Z].smu[X].guard.v()`` function.

        Description:
            - This function makes a guard voltage measurement.

        TSP Syntax:
            ```
            - slot[Z].smu[X].guard.v()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.v())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.v()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemSmuItemContact(BaseTSPCmd):
    """The ``slot[Z].smu[X].contact`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the channel (1 or 2).

    Properties and methods:
        - ``.calibratehi()``: The ``slot[Z].smu[X].contact.calibratehi()`` function.
        - ``.calibratelo()``: The ``slot[Z].smu[X].contact.calibratelo()`` function.
        - ``.check()``: The ``slot[Z].smu[X].contact.check()`` function.
        - ``.getcalhi()``: The ``slot[Z].smu[X].contact.getcalhi()`` function.
        - ``.r()``: The ``slot[Z].smu[X].contact.r()`` function.
        - ``.speed``: The ``slot[Z].smu[X].contact.speed`` attribute.
        - ``.threshold``: The ``slot[Z].smu[X].contact.threshold`` attribute.
    """

    @property
    def speed(self) -> str:
        """Access the ``slot[Z].smu[X].contact.speed`` attribute.

        Description:
            - This attribute sets the contact check measurement speed.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].contact.speed)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].contact.speed = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].contact.speed = value
            - print(slot[Z].smu[X].contact.speed)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".speed"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.speed)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.speed`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @speed.setter
    def speed(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].contact.speed`` attribute.

        Description:
            - This attribute sets the contact check measurement speed.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].contact.speed)`` query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].contact.speed = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].contact.speed = value
            - print(slot[Z].smu[X].contact.speed)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".speed", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.speed = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.speed`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def threshold(self) -> str:
        """Access the ``slot[Z].smu[X].contact.threshold`` attribute.

        Description:
            - This attribute sets the contact check pass or fail threshold.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].contact.threshold)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].contact.threshold = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].contact.threshold = value
            - print(slot[Z].smu[X].contact.threshold)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".threshold"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.threshold)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.threshold`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @threshold.setter
    def threshold(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].contact.threshold`` attribute.

        Description:
            - This attribute sets the contact check pass or fail threshold.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].contact.threshold)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].smu[X].contact.threshold = value`` command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].contact.threshold = value
            - print(slot[Z].smu[X].contact.threshold)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".threshold", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.threshold = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.threshold`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def calibratehi(
        self, cp1_measured: str, cp1_reference: str, cp2_measured: str, cp2_reference: str
    ) -> None:
        """Run the ``slot[Z].smu[X].contact.calibratehi()`` function.

        Description:
            - This function adjusts the high/sense high contact check measurement.

        TSP Syntax:
            ```
            - slot[Z].smu[X].contact.calibratehi()
            ```

        Args:
            cp1_measured: The value measured for point 1.
            cp1_reference: The reference measurement for point 1 as measured externally.
            cp2_measured: The value measured for point 2.
            cp2_reference: The reference measurement for point 2 as measured externally.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.calibratehi({cp1_measured}, "
                f"{cp1_reference}, "
                f"{cp2_measured}, "
                f"{cp2_reference})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.calibratehi()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def calibratelo(
        self, cp1_measured: str, cp1_reference: str, cp2_measured: str, cp2_reference: str
    ) -> None:
        """Run the ``slot[Z].smu[X].contact.calibratelo()`` function.

        Description:
            - This function adjusts the low/sense low contact check measurement.

        TSP Syntax:
            ```
            - slot[Z].smu[X].contact.calibratelo()
            ```

        Args:
            cp1_measured: The value measured for point 1.
            cp1_reference: The reference measurement for point 1 as measured externally.
            cp2_measured: The value measured for point 2.
            cp2_reference: The reference measurement for point 2 as measured externally.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.calibratelo({cp1_measured}, "
                f"{cp1_reference}, "
                f"{cp2_measured}, "
                f"{cp2_reference})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.calibratelo()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def check(self) -> str:
        """Run the ``slot[Z].smu[X].contact.check()`` function.

        Description:
            - This function performs a contact check measurement and compares the result to the
              user-specified contact check threshold setting.

        TSP Syntax:
            ```
            - slot[Z].smu[X].contact.check()
            ```

        Info:
            - ``X``, the module channel number.
            - ``Z``, the module slot number.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.check())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.check()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getcalhi(self, range_: str) -> str:
        """Run the ``slot[Z].smu[X].contact.getcalhi()`` function.

        Description:
            - This function returns the calibration constants used during the contact check hi
              measurement calculation.

        TSP Syntax:
            ```
            - slot[Z].smu[X].contact.getcalhi()
            ```

        Args:
            range_: Specifies the range to retrieve.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getcalhi({range_}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getcalhi()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def r(self) -> str:
        """Run the ``slot[Z].smu[X].contact.r()`` function.

        Description:
            - This function performs a contact check measurement and returns the measured contact
              resistances.

        TSP Syntax:
            ```
            - slot[Z].smu[X].contact.r()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.r())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.r()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemSmuItemConfiglist(BaseTSPCmd):
    """The ``slot[Z].smu[X].configlist`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the module channel number.

    Properties and methods:
        - ``.create()``: The ``slot[Z].smu[X].configlist.create()`` function.
        - ``.delete()``: The ``slot[Z].smu[X].configlist.delete()`` function.
        - ``.query()``: The ``slot[Z].smu[X].configlist.query()`` function.
        - ``.recall()``: The ``slot[Z].smu[X].configlist.recall()`` function.
        - ``.size()``: The ``slot[Z].smu[X].configlist.size()`` function.
        - ``.store()``: The ``slot[Z].smu[X].configlist.store()`` function.
        - ``.table()``: The ``slot[Z].smu[X].configlist.table()`` function.
    """

    def create(self, config_list_name: str) -> None:
        """Run the ``slot[Z].smu[X].configlist.create()`` function.

        Description:
            - This function creates an empty configuration list.

        TSP Syntax:
            ```
            - slot[Z].smu[X].configlist.create()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.create("{config_list_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.create()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, config_list_name: str, index: Optional[int] = None) -> None:
        """Run the ``slot[Z].smu[X].configlist.delete()`` function.

        Description:
            - This function deletes a configuration list.

        TSP Syntax:
            ```
            - slot[Z].smu[X].configlist.delete()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.
            index (optional): A number starting from 1 that defines a specific configuration index
                in the configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.delete({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def query(
        self, config_list_name: str, index: int, field_separator: Optional[str] = None
    ) -> str:
        """Run the ``slot[Z].smu[X].configlist.query()`` function.

        Description:
            - This function returns a list of TSP commands and parameter settings that are stored in
              the specified configuration index.

        TSP Syntax:
            ```
            - slot[Z].smu[X].configlist.query()
            ```

        Args:
            config_list_name: A string that represents the name of a measure configuration list.
            index: A number starting from 1 that defines a specific configuration index in the
                configuration list.
            field_separator (optional): String that represents the separator for the data; use one
                of the following.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    index,
                    f'"{field_separator}"' if field_separator is not None else None,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.query({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.query()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def recall(self, config_list_name: str, index: int) -> None:
        """Run the ``slot[Z].smu[X].configlist.recall()`` function.

        Description:
            - This function recalls a configuration index in a configuration list.

        TSP Syntax:
            ```
            - slot[Z].smu[X].configlist.recall()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.
            index: A number starting from 1 that defines a specific configuration index in the
                measure configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.recall("{config_list_name}", {index})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recall()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def size(self, config_list_name: str) -> str:
        """Run the ``slot[Z].smu[X].configlist.size()`` function.

        Description:
            - This function returns the size (number of configuration indexes) of a configuration
              list.

        TSP Syntax:
            ```
            - slot[Z].smu[X].configlist.size()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.size("{config_list_name}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.size()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def store(self, config_list_name: str, index: Optional[int] = None) -> None:
        """Run the ``slot[Z].smu[X].configlist.store()`` function.

        Description:
            - This function stores the active settings into the named configuration list.

        TSP Syntax:
            ```
            - slot[Z].smu[X].configlist.store()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.
            index (optional): A number starting from 1 that defines a specific configuration index
                in the configuration list. This parameter is optional.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.store({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.store()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def table(self) -> str:
        """Run the ``slot[Z].smu[X].configlist.table()`` function.

        Description:
            - This function returns the name of one measure configuration lists that is stored on
              the instrument.

        TSP Syntax:
            ```
            - slot[Z].smu[X].configlist.table()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.table())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.table()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemSmuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[Z].smu[X]`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the module channel number.

    Properties and methods:
        - ``.abort()``: The ``slot[Z].smu[X].abort()`` function.
        - ``.configlist``: The ``slot[Z].smu[X].configlist`` command tree.
        - ``.contact``: The ``slot[Z].smu[X].contact`` command tree.
        - ``.defbuffer1``: The ``slot[Z].smu[X].defbuffer1`` attribute.
        - ``.defbuffer2``: The ``slot[Z].smu[X].defbuffer2`` attribute.
        - ``.guard``: The ``slot[Z].smu[X].guard`` command tree.
        - ``.makebuffer()``: The ``slot[Z].smu[X].makebuffer()`` function.
        - ``.measure``: The ``slot[Z].smu[X].measure`` command tree.
        - ``.overlapped``: The ``slot[Z].smu[X].overlapped`` attribute.
        - ``.reset()``: The ``slot[Z].smu[X].reset()`` function.
        - ``.sense``: The ``slot[Z].smu[X].sense`` attribute.
        - ``.source``: The ``slot[Z].smu[X].source`` command tree.
        - ``.trigger``: The ``slot[Z].smu[X].trigger`` command tree.
        - ``.waitcomplete()``: The ``slot[Z].smu[X].waitcomplete()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._buffer_count = 1
        self._configlist = SlotItemSmuItemConfiglist(device, f"{self._cmd_syntax}.configlist")
        self._contact = SlotItemSmuItemContact(device, f"{self._cmd_syntax}.contact")
        self._guard = SlotItemSmuItemGuard(device, f"{self._cmd_syntax}.guard")
        self._measure = SlotItemSmuItemMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = SlotItemSmuItemSource(device, f"{self._cmd_syntax}.source")
        self._trigger = SlotItemSmuItemTrigger(device, f"{self._cmd_syntax}.trigger")

    @property
    def configlist(self) -> SlotItemSmuItemConfiglist:
        """Return the ``slot[Z].smu[X].configlist`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.create()``: The ``slot[Z].smu[X].configlist.create()`` function.
            - ``.delete()``: The ``slot[Z].smu[X].configlist.delete()`` function.
            - ``.query()``: The ``slot[Z].smu[X].configlist.query()`` function.
            - ``.recall()``: The ``slot[Z].smu[X].configlist.recall()`` function.
            - ``.size()``: The ``slot[Z].smu[X].configlist.size()`` function.
            - ``.store()``: The ``slot[Z].smu[X].configlist.store()`` function.
            - ``.table()``: The ``slot[Z].smu[X].configlist.table()`` function.
        """
        return self._configlist

    @property
    def contact(self) -> SlotItemSmuItemContact:
        """Return the ``slot[Z].smu[X].contact`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the channel (1 or 2).

        Sub-properties and sub-methods:
            - ``.calibratehi()``: The ``slot[Z].smu[X].contact.calibratehi()`` function.
            - ``.calibratelo()``: The ``slot[Z].smu[X].contact.calibratelo()`` function.
            - ``.check()``: The ``slot[Z].smu[X].contact.check()`` function.
            - ``.getcalhi()``: The ``slot[Z].smu[X].contact.getcalhi()`` function.
            - ``.r()``: The ``slot[Z].smu[X].contact.r()`` function.
            - ``.speed``: The ``slot[Z].smu[X].contact.speed`` attribute.
            - ``.threshold``: The ``slot[Z].smu[X].contact.threshold`` attribute.
        """
        return self._contact

    @cached_property
    def defbuffer1(self) -> Buffervar:
        """Access the ``slot[Z].smu[X].defbuffer1`` attribute.

        Description:
            - This attribute contains the default dedicated reading buffers. (1 = default buffer1)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].defbuffer1)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].smu[X].defbuffer1)
            ```

        Returns:
            The default buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return Buffervar(self._device, f"{self._cmd_syntax}.defbuffer1")

    @cached_property
    def defbuffer2(self) -> Buffervar:
        """Access the ``slot[Z].smu[X].defbuffer2`` attribute.

        Description:
            - This attribute contains the default dedicated reading buffers. (2 = default buffer2)

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].defbuffer2)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].smu[X].defbuffer2)
            ```

        Returns:
            The default buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return Buffervar(self._device, f"{self._cmd_syntax}.defbuffer2")

    @property
    def guard(self) -> SlotItemSmuItemGuard:
        """Return the ``slot[Z].smu[X].guard`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.v()``: The ``slot[Z].smu[X].guard.v()`` function.
        """
        return self._guard

    @property
    def measure(self) -> SlotItemSmuItemMeasure:
        """Return the ``slot[Z].smu[X].measure`` command tree.

        Sub-properties and sub-methods:
            - ``.i()``: The ``slot[Z].smu[X].measure.i()`` function.
            - ``.p()``: The ``slot[Z].smu[X].measure.p()`` function.
            - ``.r()``: The ``slot[Z].smu[X].measure.r()`` function.
            - ``.v()``: The ``slot[Z].smu[X].measure.v()`` function.
            - ``.aperture``: The ``slot[Z].smu[X].measure.aperture`` attribute.
            - ``.autodelay``: The ``slot[Z].smu[X].measure.autodelay`` attribute.
            - ``.autorangei``: The ``slot[Z].smu[X].measure.autorangei`` attribute.
            - ``.autorangev``: The ``slot[Z].smu[X].measure.autorangev`` attribute.
            - ``.count``: The ``slot[Z].smu[X].measure.count`` attribute.
            - ``.delay``: The ``slot[Z].smu[X].measure.delay`` attribute.
            - ``.interval``: The ``slot[Z].smu[X].measure.interval`` attribute.
            - ``.lowrangei``: The ``slot[Z].smu[X].measure.lowrangei`` attribute.
            - ``.lowrangev``: The ``slot[Z].smu[X].measure.lowrangev`` attribute.
            - ``.nplc``: The ``slot[Z].smu[X].measure.nplc`` attribute.
            - ``.overlappedi()``: The ``slot[Z].smu[X].measure.overlappedi()`` function.
            - ``.overlappediv()``: The ``slot[Z].smu[X].measure.overlappediv()`` function.
            - ``.overlappedp()``: The ``slot[Z].smu[X].measure.overlappedp()`` function.
            - ``.overlappedr()``: The ``slot[Z].smu[X].measure.overlappedr()`` function.
            - ``.overlappedv()``: The ``slot[Z].smu[X].measure.overlappedv()`` function.
            - ``.rangei``: The ``slot[Z].smu[X].measure.rangei`` attribute.
            - ``.rangev``: The ``slot[Z].smu[X].measure.rangev`` attribute.
            - ``.rel``: The ``slot[Z].smu[X].measure.rel`` command tree.
            - ``.tempcomp``: The ``slot[Z].smu[X].measure.tempcomp`` attribute.
        """
        return self._measure

    @property
    def overlapped(self) -> str:
        """Access the ``slot[Z].smu[X].overlapped`` attribute.

        Description:
            - This attribute contains the state of the overlapped mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].overlapped)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].overlapped = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].overlapped = value
            - print(slot[Z].smu[X].overlapped)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".overlapped"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.overlapped)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overlapped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @overlapped.setter
    def overlapped(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].overlapped`` attribute.

        Description:
            - This attribute contains the state of the overlapped mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].overlapped)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].overlapped = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].overlapped = value
            - print(slot[Z].smu[X].overlapped)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".overlapped", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.overlapped = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overlapped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def sense(self) -> str:
        """Access the ``slot[Z].smu[X].sense`` attribute.

        Description:
            - This attribute contains the state of the sense mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].sense)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].sense = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].sense = value
            - print(slot[Z].smu[X].sense)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".sense"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.sense)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.sense`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @sense.setter
    def sense(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].smu[X].sense`` attribute.

        Description:
            - This attribute contains the state of the sense mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].smu[X].sense)`` query.
            - Setting this property to a value will send the ``slot[Z].smu[X].sense = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].smu[X].sense = value
            - print(slot[Z].smu[X].sense)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".sense", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.sense = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.sense`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def source(self) -> SlotItemSmuItemSource:
        """Return the ``slot[Z].smu[X].source`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.autodelay``: The ``slot[Z].smu[X].source.autodelay`` attribute.
            - ``.autorangei``: The ``slot[Z].smu[X].source.autorangei`` attribute.
            - ``.autorangev``: The ``slot[Z].smu[X].source.autorangev`` attribute.
            - ``.constantcurrent``: The ``slot[Z].smu[X].source.constantcurrent`` attribute.
            - ``.delay``: The ``slot[Z].smu[X].source.delay`` attribute.
            - ``.func``: The ``slot[Z].smu[X].source.func`` attribute.
            - ``.leveli``: The ``slot[Z].smu[X].source.leveli`` attribute.
            - ``.levelv``: The ``slot[Z].smu[X].source.levelv`` attribute.
            - ``.limiti``: The ``slot[Z].smu[X].source.limiti`` attribute.
            - ``.limitv``: The ``slot[Z].smu[X].source.limitv`` attribute.
            - ``.limitni``: The ``slot[Z].smu[X].source.limitni`` attribute.
            - ``.limitnv``: The ``slot[Z].smu[X].source.limitnv`` attribute.
            - ``.limitpi``: The ``slot[Z].smu[X].source.limitpi`` attribute.
            - ``.limitpv``: The ``slot[Z].smu[X].source.limitpv`` attribute.
            - ``.lowrangei``: The ``slot[Z].smu[X].source.lowrangei`` attribute.
            - ``.lowrangev``: The ``slot[Z].smu[X].source.lowrangev`` attribute.
            - ``.offfunc``: The ``slot[Z].smu[X].source.offfunc`` attribute.
            - ``.offlimiti``: The ``slot[Z].smu[X].source.offlimiti`` attribute.
            - ``.offlimitv``: The ``slot[Z].smu[X].source.offlimitv`` attribute.
            - ``.offlimitni``: The ``slot[Z].smu[X].source.offlimitni`` attribute.
            - ``.offlimitnv``: The ``slot[Z].smu[X].source.offlimitnv`` attribute.
            - ``.offlimitpi``: The ``slot[Z].smu[X].source.offlimitpi`` attribute.
            - ``.offlimitpv``: The ``slot[Z].smu[X].source.offlimitpv`` attribute.
            - ``.offmode``: The ``slot[Z].smu[X].source.offmode`` attribute.
            - ``.output``: The ``slot[Z].smu[X].source.output`` attribute.
            - ``.rangei``: The ``slot[Z].smu[X].source.rangei`` attribute.
            - ``.rangev``: The ``slot[Z].smu[X].source.rangev`` attribute.
        """
        return self._source

    @property
    def trigger(self) -> SlotItemSmuItemTrigger:
        """Return the ``slot[Z].smu[X].trigger`` command tree.

        Sub-properties and sub-methods:
            - ``.measure``: The ``slot[Z].smu[X].trigger.measure`` command tree.
            - ``.source``: The ``slot[Z].smu[X].trigger.source`` command tree.
        """
        return self._trigger

    def abort(self) -> None:
        """Run the ``slot[Z].smu[X].abort()`` function.

        Description:
            - This function terminates all overlapped operations on the specified channel.

        TSP Syntax:
            ```
            - slot[Z].smu[X].abort()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.abort()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.abort()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def makebuffer(self, buffer_size: str, *, buffer_name: Optional[str] = None) -> Buffervar:
        """Run the ``slot[Z].smu[X].makebuffer()`` function.

        Description:
            - This function creates a reading buffer.

        TSP Syntax:
            ```
            - slot[Z].smu[X].makebuffer()
            ```

        Args:
            buffer_size: The size of the reading buffer.
            buffer_name (optional): The name of the buffer variable to create. If not provided, an
                auto-generated variable will be used.

        Returns:
            The created buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        if buffer_name is None:
            buffer_name = f"private_custom_smu_buffer_{self._buffer_count}"
            self._buffer_count += 1
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{buffer_name} = {self._cmd_syntax}.makebuffer({buffer_size})"
            )
            self._device._user_created_custom_buffers.append(buffer_name)  # pyright: ignore[reportOptionalMemberAccess,reportPrivateUsage]  # noqa: SLF001
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.makebuffer()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
        return Buffervar(self._device, buffer_name)

    def reset(self) -> None:
        """Run the ``slot[Z].smu[X].reset()`` function.

        Description:
            - This function turns off the output and resets the commands that begin with smu [X]. to
              their default settings.

        TSP Syntax:
            ```
            - slot[Z].smu[X].reset()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def waitcomplete(self) -> None:
        """Run the ``slot[Z].smu[X].waitcomplete()`` function.

        Description:
            - This function waits for all previously started overlapped commands to complete on the
              specified channel of a module.

        TSP Syntax:
            ```
            - slot[Z].smu[X].waitcomplete()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.waitcomplete()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.waitcomplete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemPsuItemTriggerSource(BaseTSPCmd):
    """The ``slot[Z].psu[X].trigger.source`` command tree.

    Properties and methods:
        - ``.linearv()``: The ``slot[Z].psu[X].trigger.source.linearv()`` function.
        - ``.listv()``: The ``slot[Z].psu[X].trigger.source.listv()`` function.
        - ``.logv()``: The ``slot[Z].psu[X].trigger.source.logv()`` function.
    """

    def linearv(self, start: str, end: str, points: str) -> None:
        """Run the ``slot[Z].psu[X].trigger.source.linearv()`` function.

        Description:
            - This function configures the linear sweep for the trigger model. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].trigger.source.linearv()
            ```

        Args:
            start: Start source level.
            end: End source level.
            points: Number of points used to calculate the step size.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.linearv({start}, {end}, {points})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.linearv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def listv(self, source_levels: str) -> None:
        """Run the ``slot[Z].psu[X].trigger.source.listv()`` function.

        Description:
            - This function configures the list sweep for the trigger model. (v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].trigger.source.listv()
            ```

        Args:
            source_levels: List of source levels. Each time a source block is reached, the index
                increases by 1. When it reaches the end, it cycles back to the beginning.

        For example, ({1, 2, 3}).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.listv({source_levels})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.listv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def logv(self, start: str, end: str, points: str) -> None:
        """Run the ``slot[Z].psu[X].trigger.source.logv()`` function.

        Description:
            - This function configures a logarithmic sweep for the trigger model. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].trigger.source.logv()
            ```

        Args:
            start: Start source level.
            end: End source level.
            points: Number of points used to calculate the step size.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.logv({start}, {end}, {points})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.logv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemPsuItemTriggerMeasure(BaseTSPCmd):
    """The ``slot[Z].psu[X].trigger.measure`` command tree.

    Properties and methods:
        - ``.i()``: The ``slot[Z].psu[X].trigger.measure.i()`` function.
        - ``.iv()``: The ``slot[Z].psu[X].trigger.measure.iv()`` function.
        - ``.p()``: The ``slot[Z].psu[X].trigger.measure.p()`` function.
        - ``.r()``: The ``slot[Z].psu[X].trigger.measure.r()`` function.
        - ``.v()``: The ``slot[Z].psu[X].trigger.measure.v()`` function.
    """

    def i(self, reading_buffer: str) -> None:
        """Run the ``slot[Z].psu[X].trigger.measure.i()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (i
              = current in amperes)

        TSP Syntax:
            ```
            - slot[Z].psu[X].trigger.measure.i()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.i({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.i()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def iv(self, ibuffer: str, vbuffer: str) -> None:
        """Run the ``slot[Z].psu[X].trigger.measure.iv()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (i
              = current in amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].trigger.measure.iv()
            ```

        Args:
            ibuffer: Buffer to store current readings.
            vbuffer: Buffer to store voltage readings.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.iv({ibuffer}, {vbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.iv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def p(self, reading_buffer: str) -> None:
        """Run the ``slot[Z].psu[X].trigger.measure.p()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (p
              = power in watts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].trigger.measure.p()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.p({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.p()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def r(self, reading_buffer: str) -> None:
        """Run the ``slot[Z].psu[X].trigger.measure.r()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (r
              = resistance in ohms)

        TSP Syntax:
            ```
            - slot[Z].psu[X].trigger.measure.r()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.r({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.r()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def v(self, reading_buffer: str) -> None:
        """Run the ``slot[Z].psu[X].trigger.measure.v()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (v
              = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].trigger.measure.v()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.v({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.v()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemPsuItemTrigger(BaseTSPCmd):
    """The ``slot[Z].psu[X].trigger`` command tree.

    Properties and methods:
        - ``.measure``: The ``slot[Z].psu[X].trigger.measure`` command tree.
        - ``.source``: The ``slot[Z].psu[X].trigger.source`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._measure = SlotItemPsuItemTriggerMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = SlotItemPsuItemTriggerSource(device, f"{self._cmd_syntax}.source")

    @property
    def measure(self) -> SlotItemPsuItemTriggerMeasure:
        """Return the ``slot[Z].psu[X].trigger.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.i()``: The ``slot[Z].psu[X].trigger.measure.i()`` function.
            - ``.iv()``: The ``slot[Z].psu[X].trigger.measure.iv()`` function.
            - ``.p()``: The ``slot[Z].psu[X].trigger.measure.p()`` function.
            - ``.r()``: The ``slot[Z].psu[X].trigger.measure.r()`` function.
            - ``.v()``: The ``slot[Z].psu[X].trigger.measure.v()`` function.
        """
        return self._measure

    @property
    def source(self) -> SlotItemPsuItemTriggerSource:
        """Return the ``slot[Z].psu[X].trigger.source`` command tree.

        Sub-properties and sub-methods:
            - ``.linearv()``: The ``slot[Z].psu[X].trigger.source.linearv()`` function.
            - ``.listv()``: The ``slot[Z].psu[X].trigger.source.listv()`` function.
            - ``.logv()``: The ``slot[Z].psu[X].trigger.source.logv()`` function.
        """
        return self._source


class SlotItemPsuItemSourceProtect(BaseTSPCmd):
    """The ``slot[Z].psu[X].source.protect`` command tree.

    Properties and methods:
        - ``.enablei``: The ``slot[Z].psu[X].source.protect.enablei`` attribute.
        - ``.enablev``: The ``slot[Z].psu[X].source.protect.enablev`` attribute.
        - ``.leveli``: The ``slot[Z].psu[X].source.protect.leveli`` attribute.
        - ``.levelv``: The ``slot[Z].psu[X].source.protect.levelv`` attribute.
        - ``.trippedi``: The ``slot[Z].psu[X].source.protect.trippedi`` attribute.
        - ``.trippedv``: The ``slot[Z].psu[X].source.protect.trippedv`` attribute.
    """

    @property
    def enablei(self) -> str:
        """Access the ``slot[Z].psu[X].source.protect.enablei`` attribute.

        Description:
            - This attribute enables or disables the overcurrent protection function.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.protect.enablei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.protect.enablei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.protect.enablei = value
            - print(slot[Z].psu[X].source.protect.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablei.setter
    def enablei(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.protect.enablei`` attribute.

        Description:
            - This attribute enables or disables the overcurrent protection function.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.protect.enablei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.protect.enablei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.protect.enablei = value
            - print(slot[Z].psu[X].source.protect.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enablev(self) -> str:
        """Access the ``slot[Z].psu[X].source.protect.enablev`` attribute.

        Description:
            - This attribute enables or disables the overvoltage protection function.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.protect.enablev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.protect.enablev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.protect.enablev = value
            - print(slot[Z].psu[X].source.protect.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablev.setter
    def enablev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.protect.enablev`` attribute.

        Description:
            - This attribute enables or disables the overvoltage protection function.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.protect.enablev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.protect.enablev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.protect.enablev = value
            - print(slot[Z].psu[X].source.protect.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def leveli(self) -> str:
        """Access the ``slot[Z].psu[X].source.protect.leveli`` attribute.

        Description:
            - This attribute configures the overcurrent protection level.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.protect.leveli)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.protect.leveli = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.protect.leveli = value
            - print(slot[Z].psu[X].source.protect.leveli)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".leveli"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.leveli)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @leveli.setter
    def leveli(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.protect.leveli`` attribute.

        Description:
            - This attribute configures the overcurrent protection level.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.protect.leveli)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.protect.leveli = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.protect.leveli = value
            - print(slot[Z].psu[X].source.protect.leveli)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".leveli", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.leveli = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelv(self) -> str:
        """Access the ``slot[Z].psu[X].source.protect.levelv`` attribute.

        Description:
            - This attribute configures the overvoltage protection level.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.protect.levelv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.protect.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.protect.levelv = value
            - print(slot[Z].psu[X].source.protect.levelv)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelv.setter
    def levelv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.protect.levelv`` attribute.

        Description:
            - This attribute configures the overvoltage protection level.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.protect.levelv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.protect.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.protect.levelv = value
            - print(slot[Z].psu[X].source.protect.levelv)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def trippedi(self) -> str:
        """Access the ``slot[Z].psu[X].source.protect.trippedi`` attribute.

        Description:
            - This attribute indicates if the overcurrent protection circuit was tripped.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].psu[X].source.protect.trippedi)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].psu[X].source.protect.trippedi)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".trippedi"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.trippedi)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.trippedi`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def trippedv(self) -> str:
        """Access the ``slot[Z].psu[X].source.protect.trippedv`` attribute.

        Description:
            - This attribute indicates if the overvoltage protection circuit was tripped.

        Usage:
            - Accessing this property will send the
              ``print(slot[Z].psu[X].source.protect.trippedv)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].psu[X].source.protect.trippedv)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".trippedv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.trippedv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.trippedv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemPsuItemSource(BaseTSPCmd):
    """The ``slot[Z].psu[X].source`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the module channel number.

    Properties and methods:
        - ``.constantcurrent``: The ``slot[Z].psu[X].source.constantcurrent`` attribute.
        - ``.levelv``: The ``slot[Z].psu[X].source.levelv`` attribute.
        - ``.limiti``: The ``slot[Z].psu[X].source.limiti`` attribute.
        - ``.offmode``: The ``slot[Z].psu[X].source.offmode`` attribute.
        - ``.output``: The ``slot[Z].psu[X].source.output`` attribute.
        - ``.protect``: The ``slot[Z].psu[X].source.protect`` command tree.
        - ``.rangev``: The ``slot[Z].psu[X].source.rangev`` attribute.
        - ``.slewratev``: The ``slot[Z].psu[X].source.slewratev`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._protect = SlotItemPsuItemSourceProtect(device, f"{self._cmd_syntax}.protect")

    @property
    def constantcurrent(self) -> str:
        """Access the ``slot[Z].psu[X].source.constantcurrent`` attribute.

        Description:
            - This attribute indicates when the source is within the current limit.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.constantcurrent)``
              query.

        TSP Syntax:
            ```
            - print(slot[Z].psu[X].source.constantcurrent)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".constantcurrent"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.constantcurrent)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.constantcurrent`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelv(self) -> str:
        """Access the ``slot[Z].psu[X].source.levelv`` attribute.

        Description:
            - This attribute configures the voltage source level.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.levelv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.levelv = value
            - print(slot[Z].psu[X].source.levelv)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelv.setter
    def levelv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.levelv`` attribute.

        Description:
            - This attribute configures the voltage source level.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.levelv)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.levelv = value
            - print(slot[Z].psu[X].source.levelv)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limiti(self) -> str:
        """Access the ``slot[Z].psu[X].source.limiti`` attribute.

        Description:
            - This attribute configures the source current limit.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.limiti)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.limiti = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.limiti = value
            - print(slot[Z].psu[X].source.limiti)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".limiti"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.limiti)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limiti`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @limiti.setter
    def limiti(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.limiti`` attribute.

        Description:
            - This attribute configures the source current limit.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.limiti)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.limiti = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.limiti = value
            - print(slot[Z].psu[X].source.limiti)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".limiti", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.limiti = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limiti`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offmode(self) -> str:
        """Access the ``slot[Z].psu[X].source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.offmode)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.offmode = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.offmode = value
            - print(slot[Z].psu[X].source.offmode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offmode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offmode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offmode.setter
    def offmode(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.offmode)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.offmode = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.offmode = value
            - print(slot[Z].psu[X].source.offmode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offmode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offmode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def output(self) -> str:
        """Access the ``slot[Z].psu[X].source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.output)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.output = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.output = value
            - print(slot[Z].psu[X].source.output)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".output"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.output)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.output`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @output.setter
    def output(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.output)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.output = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.output = value
            - print(slot[Z].psu[X].source.output)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".output", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.output = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.output`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def protect(self) -> SlotItemPsuItemSourceProtect:
        """Return the ``slot[Z].psu[X].source.protect`` command tree.

        Sub-properties and sub-methods:
            - ``.enablei``: The ``slot[Z].psu[X].source.protect.enablei`` attribute.
            - ``.enablev``: The ``slot[Z].psu[X].source.protect.enablev`` attribute.
            - ``.leveli``: The ``slot[Z].psu[X].source.protect.leveli`` attribute.
            - ``.levelv``: The ``slot[Z].psu[X].source.protect.levelv`` attribute.
            - ``.trippedi``: The ``slot[Z].psu[X].source.protect.trippedi`` attribute.
            - ``.trippedv``: The ``slot[Z].psu[X].source.protect.trippedv`` attribute.
        """
        return self._protect

    @property
    def rangev(self) -> str:
        """Access the ``slot[Z].psu[X].source.rangev`` attribute.

        Description:
            - This attribute contains the value of the source range for voltage.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.rangev)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.rangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.rangev = value
            - print(slot[Z].psu[X].source.rangev)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rangev.setter
    def rangev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.rangev`` attribute.

        Description:
            - This attribute contains the value of the source range for voltage.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.rangev)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.rangev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.rangev = value
            - print(slot[Z].psu[X].source.rangev)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rangev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rangev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def slewratev(self) -> str:
        """Access the ``slot[Z].psu[X].source.slewratev`` attribute.

        Description:
            - This attribute configures the voltage source slew rate.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.slewratev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.slewratev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.slewratev = value
            - print(slot[Z].psu[X].source.slewratev)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".slewratev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.slewratev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slewratev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @slewratev.setter
    def slewratev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].source.slewratev`` attribute.

        Description:
            - This attribute configures the voltage source slew rate.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].source.slewratev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].source.slewratev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].source.slewratev = value
            - print(slot[Z].psu[X].source.slewratev)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".slewratev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.slewratev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slewratev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemPsuItemMeasureRel(BaseTSPCmd):
    """The ``slot[Z].psu[X].measure.rel`` command tree.

    Properties and methods:
        - ``.enablei``: The ``slot[Z].psu[X].measure.rel.enablei`` attribute.
        - ``.enablep``: The ``slot[Z].psu[X].measure.rel.enablep`` attribute.
        - ``.enabler``: The ``slot[Z].psu[X].measure.rel.enabler`` attribute.
        - ``.enablev``: The ``slot[Z].psu[X].measure.rel.enablev`` attribute.
        - ``.leveli``: The ``slot[Z].psu[X].measure.rel.leveli`` attribute.
        - ``.levelp``: The ``slot[Z].psu[X].measure.rel.levelp`` attribute.
        - ``.levelr``: The ``slot[Z].psu[X].measure.rel.levelr`` attribute.
        - ``.levelv``: The ``slot[Z].psu[X].measure.rel.levelv`` attribute.
    """

    @property
    def enablei(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.enablei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.enablei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.enablei = value
            - print(slot[Z].psu[X].measure.rel.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablei.setter
    def enablei(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.enablei)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.enablei = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.enablei = value
            - print(slot[Z].psu[X].measure.rel.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enablep(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.enablep)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.enablep = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.enablep = value
            - print(slot[Z].psu[X].measure.rel.enablep)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablep"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablep)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablep`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablep.setter
    def enablep(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.enablep)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.enablep = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.enablep = value
            - print(slot[Z].psu[X].measure.rel.enablep)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablep", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablep = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablep`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enabler(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.enabler)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.enabler = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.enabler = value
            - print(slot[Z].psu[X].measure.rel.enabler)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enabler"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enabler)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enabler`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enabler.setter
    def enabler(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.enabler)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.enabler = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.enabler = value
            - print(slot[Z].psu[X].measure.rel.enabler)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enabler", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enabler = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enabler`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enablev(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.enablev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.enablev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.enablev = value
            - print(slot[Z].psu[X].measure.rel.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablev.setter
    def enablev(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.enablev)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.enablev = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.enablev = value
            - print(slot[Z].psu[X].measure.rel.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def leveli(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rel.leveli`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.leveli)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.leveli = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.leveli = value
            - print(slot[Z].psu[X].measure.rel.leveli)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".leveli"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.leveli)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @leveli.setter
    def leveli(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.rel.leveli`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.leveli)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.leveli = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.leveli = value
            - print(slot[Z].psu[X].measure.rel.leveli)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".leveli", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.leveli = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelp(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rel.levelp`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (p = power in
              watts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.levelp)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.levelp = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.levelp = value
            - print(slot[Z].psu[X].measure.rel.levelp)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelp"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelp)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelp.setter
    def levelp(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.rel.levelp`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (p = power in
              watts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.levelp)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.levelp = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.levelp = value
            - print(slot[Z].psu[X].measure.rel.levelp)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelp", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelp = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelr(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rel.levelr`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (r = resistance
              in ohms)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.levelr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.levelr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.levelr = value
            - print(slot[Z].psu[X].measure.rel.levelr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelr.setter
    def levelr(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.rel.levelr`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (r = resistance
              in ohms)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.levelr)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.levelr = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.levelr = value
            - print(slot[Z].psu[X].measure.rel.levelr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelv(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rel.levelv`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.levelv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.levelv = value
            - print(slot[Z].psu[X].measure.rel.levelv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelv.setter
    def levelv(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.rel.levelv`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rel.levelv)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.rel.levelv = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rel.levelv = value
            - print(slot[Z].psu[X].measure.rel.levelv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemPsuItemMeasure(BaseTSPCmd):
    """The ``slot[Z].psu[X].measure`` command tree.

    Properties and methods:
        - ``.i()``: The ``slot[Z].psu[X].measure.i()`` function.
        - ``.p()``: The ``slot[Z].psu[X].measure.p()`` function.
        - ``.r()``: The ``slot[Z].psu[X].measure.r()`` function.
        - ``.v()``: The ``slot[Z].psu[X].measure.v()`` function.
        - ``.aperture``: The ``slot[Z].psu[X].measure.aperture`` attribute.
        - ``.count``: The ``slot[Z].psu[X].measure.count`` attribute.
        - ``.nplc``: The ``slot[Z].psu[X].measure.nplc`` attribute.
        - ``.overlappedi()``: The ``slot[Z].psu[X].measure.overlappedi()`` function.
        - ``.overlappediv()``: The ``slot[Z].psu[X].measure.overlappediv()`` function.
        - ``.overlappedp()``: The ``slot[Z].psu[X].measure.overlappedp()`` function.
        - ``.overlappedr()``: The ``slot[Z].psu[X].measure.overlappedr()`` function.
        - ``.overlappedv()``: The ``slot[Z].psu[X].measure.overlappedv()`` function.
        - ``.rangei``: The ``slot[Z].psu[X].measure.rangei`` attribute.
        - ``.rangev``: The ``slot[Z].psu[X].measure.rangev`` attribute.
        - ``.rate``: The ``slot[Z].psu[X].measure.rate`` attribute.
        - ``.rel``: The ``slot[Z].psu[X].measure.rel`` command tree.
        - ``.tempcomp``: The ``slot[Z].psu[X].measure.tempcomp`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rel = SlotItemPsuItemMeasureRel(device, f"{self._cmd_syntax}.rel")

    @property
    def aperture(self) -> str:
        """Access the ``slot[Z].psu[X].measure.aperture`` attribute.

        Description:
            - This attribute configures the measurement aperture for a channel in seconds.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.aperture)``
              query.

        TSP Syntax:
            ```
            - print(slot[Z].psu[X].measure.aperture)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".aperture"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.aperture)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.aperture`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def count(self) -> str:
        """Access the ``slot[Z].psu[X].measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements performed when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.count)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.count = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.count = value
            - print(slot[Z].psu[X].measure.count)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".count"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.count)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @count.setter
    def count(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements performed when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.count)`` query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.count = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.count = value
            - print(slot[Z].psu[X].measure.count)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".count", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.count = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def nplc(self) -> str:
        """Access the ``slot[Z].psu[X].measure.nplc`` attribute.

        Description:
            - This attribute configures the measurement aperture in number of power line cycles.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.nplc)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].psu[X].measure.nplc)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".nplc"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.nplc)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.nplc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rangei(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rangei`` attribute.

        Description:
            - This attribute contains the positive, full scale value of the measurement range for
              voltage or current. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rangei)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].psu[X].measure.rangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rangev(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rangev`` attribute.

        Description:
            - This attribute contains the positive, full scale value of the measurement range for
              voltage or current. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rangev)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].psu[X].measure.rangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rate(self) -> str:
        """Access the ``slot[Z].psu[X].measure.rate`` attribute.

        Description:
            - This attribute configures the measure rate for a PSU channel.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rate)`` query.
            - Setting this property to a value will send the ``slot[Z].psu[X].measure.rate = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rate = value
            - print(slot[Z].psu[X].measure.rate)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rate"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rate)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rate.setter
    def rate(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.rate`` attribute.

        Description:
            - This attribute configures the measure rate for a PSU channel.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.rate)`` query.
            - Setting this property to a value will send the ``slot[Z].psu[X].measure.rate = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.rate = value
            - print(slot[Z].psu[X].measure.rate)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rate", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rate = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rel(self) -> SlotItemPsuItemMeasureRel:
        """Return the ``slot[Z].psu[X].measure.rel`` command tree.

        Sub-properties and sub-methods:
            - ``.enablei``: The ``slot[Z].psu[X].measure.rel.enablei`` attribute.
            - ``.enablep``: The ``slot[Z].psu[X].measure.rel.enablep`` attribute.
            - ``.enabler``: The ``slot[Z].psu[X].measure.rel.enabler`` attribute.
            - ``.enablev``: The ``slot[Z].psu[X].measure.rel.enablev`` attribute.
            - ``.leveli``: The ``slot[Z].psu[X].measure.rel.leveli`` attribute.
            - ``.levelp``: The ``slot[Z].psu[X].measure.rel.levelp`` attribute.
            - ``.levelr``: The ``slot[Z].psu[X].measure.rel.levelr`` attribute.
            - ``.levelv``: The ``slot[Z].psu[X].measure.rel.levelv`` attribute.
        """
        return self._rel

    @property
    def tempcomp(self) -> str:
        """Access the ``slot[Z].psu[X].measure.tempcomp`` attribute.

        Description:
            - This attribute turns temperature compensation on or off for the current measurements.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.tempcomp)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.tempcomp = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.tempcomp = value
            - print(slot[Z].psu[X].measure.tempcomp)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".tempcomp"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.tempcomp)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tempcomp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @tempcomp.setter
    def tempcomp(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].measure.tempcomp`` attribute.

        Description:
            - This attribute turns temperature compensation on or off for the current measurements.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].measure.tempcomp)``
              query.
            - Setting this property to a value will send the
              ``slot[Z].psu[X].measure.tempcomp = value`` command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.tempcomp = value
            - print(slot[Z].psu[X].measure.tempcomp)
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".tempcomp", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.tempcomp = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tempcomp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def i(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``slot[Z].psu[X].measure.i()`` function.

        Description:
            - This function makes one or more measurements. (i = current in amperes)

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.i()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.i({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.i()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def p(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``slot[Z].psu[X].measure.p()`` function.

        Description:
            - This function makes one or more measurements. (p = power in watts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.p()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.p({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.p()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def r(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``slot[Z].psu[X].measure.r()`` function.

        Description:
            - This function makes one or more measurements. (r = resistance in ohms)

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.r()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.r({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.r()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def v(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``slot[Z].psu[X].measure.v()`` function.

        Description:
            - This function makes one or more measurements. (v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.v()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.v({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.v()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedi(self, rbuffer: str) -> None:
        """Run the ``slot[Z].psu[X].measure.overlappedi()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes)

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.overlappedi()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedi({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedi()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappediv(self, ibuffer: str, vbuffer: str) -> None:
        """Run the ``slot[Z].psu[X].measure.overlappediv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.overlappediv()
            ```

        Args:
            ibuffer: A reading buffer object where current readings are stored.
            vbuffer: A reading buffer object where voltage readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappediv({ibuffer}, {vbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappediv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedp(self, rbuffer: str) -> None:
        """Run the ``slot[Z].psu[X].measure.overlappedp()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (p = power in watts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.overlappedp()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedp({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedp()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedr(self, rbuffer: str) -> None:
        """Run the ``slot[Z].psu[X].measure.overlappedr()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (r = resistance in
              ohms)

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.overlappedr()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedr({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedr()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedv(self, rbuffer: str) -> None:
        """Run the ``slot[Z].psu[X].measure.overlappedv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (v = voltage in volts)

        TSP Syntax:
            ```
            - slot[Z].psu[X].measure.overlappedv()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedv({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemPsuItemConfiglist(BaseTSPCmd):
    """The ``slot[Z].psu[X].configlist`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the module channel number.

    Properties and methods:
        - ``.create()``: The ``slot[Z].psu[X].configlist.create()`` function.
        - ``.delete()``: The ``slot[Z].psu[X].configlist.delete()`` function.
        - ``.query()``: The ``slot[Z].psu[X].configlist.query()`` function.
        - ``.recall()``: The ``slot[Z].psu[X].configlist.recall()`` function.
        - ``.size()``: The ``slot[Z].psu[X].configlist.size()`` function.
        - ``.store()``: The ``slot[Z].psu[X].configlist.store()`` function.
        - ``.table()``: The ``slot[Z].psu[X].configlist.table()`` function.
    """

    def create(self, config_list_name: str) -> None:
        """Run the ``slot[Z].psu[X].configlist.create()`` function.

        Description:
            - This function creates an empty configuration list.

        TSP Syntax:
            ```
            - slot[Z].psu[X].configlist.create()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.create("{config_list_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.create()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, config_list_name: str, index: Optional[int] = None) -> None:
        """Run the ``slot[Z].psu[X].configlist.delete()`` function.

        Description:
            - This function deletes a configuration list.

        TSP Syntax:
            ```
            - slot[Z].psu[X].configlist.delete()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.
            index (optional): A number starting from 1 that defines a specific configuration index
                in the configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.delete({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def query(
        self, config_list_name: str, index: int, field_separator: Optional[str] = None
    ) -> str:
        """Run the ``slot[Z].psu[X].configlist.query()`` function.

        Description:
            - This function returns a list of TSP commands and parameter settings that are stored in
              the specified configuration index.

        TSP Syntax:
            ```
            - slot[Z].psu[X].configlist.query()
            ```

        Args:
            config_list_name: A string that represents the name of a measure configuration list.
            index: A number starting from 1 that defines a specific configuration index in the
                configuration list.
            field_separator (optional): String that represents the separator for the data; use one
                of the following.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    index,
                    f'"{field_separator}"' if field_separator is not None else None,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.query({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.query()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def recall(self, config_list_name: str, index: int) -> None:
        """Run the ``slot[Z].psu[X].configlist.recall()`` function.

        Description:
            - This function recalls a configuration index in a configuration list.

        TSP Syntax:
            ```
            - slot[Z].psu[X].configlist.recall()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.
            index: A number starting from 1 that defines a specific configuration index in the
                measure configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.recall("{config_list_name}", {index})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recall()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def size(self, config_list_name: str) -> str:
        """Run the ``slot[Z].psu[X].configlist.size()`` function.

        Description:
            - This function returns the size (number of configuration indexes) of a configuration
              list.

        TSP Syntax:
            ```
            - slot[Z].psu[X].configlist.size()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.size("{config_list_name}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.size()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def store(self, config_list_name: str, index: Optional[int] = None) -> None:
        """Run the ``slot[Z].psu[X].configlist.store()`` function.

        Description:
            - This function stores the active settings into the named configuration list.

        TSP Syntax:
            ```
            - slot[Z].psu[X].configlist.store()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.
            index (optional): A number starting from 1 that defines a specific configuration index
                in the configuration list. This parameter is optional.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.store({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.store()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def table(self) -> str:
        """Run the ``slot[Z].psu[X].configlist.table()`` function.

        Description:
            - This function returns the name of one measure configuration lists that is stored on
              the instrument.

        TSP Syntax:
            ```
            - slot[Z].psu[X].configlist.table()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.table())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.table()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemPsuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[Z].psu[X]`` command tree.

    Info:
        - ``Z``, the module slot number.
        - ``X``, the module channel number.

    Properties and methods:
        - ``.abort()``: The ``slot[Z].psu[X].abort()`` function.
        - ``.configlist``: The ``slot[Z].psu[X].configlist`` command tree.
        - ``.defbuffer1``: The ``slot[Z].psu[X].defbuffer1`` attribute.
        - ``.defbuffer2``: The ``slot[Z].psu[X].defbuffer2`` attribute.
        - ``.makebuffer()``: The ``slot[Z].psu[X].makebuffer()`` function.
        - ``.measure``: The ``slot[Z].psu[X].measure`` command tree.
        - ``.overlapped``: The ``slot[Z].psu[X].overlapped`` attribute.
        - ``.reset()``: The ``slot[Z].psu[X].reset()`` function.
        - ``.source``: The ``slot[Z].psu[X].source`` command tree.
        - ``.trigger``: The ``slot[Z].psu[X].trigger`` command tree.
        - ``.waitcomplete()``: The ``slot[Z].psu[X].waitcomplete()`` function.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._buffer_count = 1
        self._configlist = SlotItemPsuItemConfiglist(device, f"{self._cmd_syntax}.configlist")
        self._measure = SlotItemPsuItemMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = SlotItemPsuItemSource(device, f"{self._cmd_syntax}.source")
        self._trigger = SlotItemPsuItemTrigger(device, f"{self._cmd_syntax}.trigger")

    @property
    def configlist(self) -> SlotItemPsuItemConfiglist:
        """Return the ``slot[Z].psu[X].configlist`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.create()``: The ``slot[Z].psu[X].configlist.create()`` function.
            - ``.delete()``: The ``slot[Z].psu[X].configlist.delete()`` function.
            - ``.query()``: The ``slot[Z].psu[X].configlist.query()`` function.
            - ``.recall()``: The ``slot[Z].psu[X].configlist.recall()`` function.
            - ``.size()``: The ``slot[Z].psu[X].configlist.size()`` function.
            - ``.store()``: The ``slot[Z].psu[X].configlist.store()`` function.
            - ``.table()``: The ``slot[Z].psu[X].configlist.table()`` function.
        """
        return self._configlist

    @cached_property
    def defbuffer1(self) -> Buffervar:
        """Access the ``slot[Z].psu[X].defbuffer1`` attribute.

        Description:
            - This attribute contains the default dedicated reading buffers. (1 = default buffer1)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].defbuffer1)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].psu[X].defbuffer1)
            ```

        Returns:
            The default buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return Buffervar(self._device, f"{self._cmd_syntax}.defbuffer1")

    @cached_property
    def defbuffer2(self) -> Buffervar:
        """Access the ``slot[Z].psu[X].defbuffer2`` attribute.

        Description:
            - This attribute contains the default dedicated reading buffers. (2 = default buffer2)

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].defbuffer2)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].psu[X].defbuffer2)
            ```

        Returns:
            The default buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return Buffervar(self._device, f"{self._cmd_syntax}.defbuffer2")

    @property
    def measure(self) -> SlotItemPsuItemMeasure:
        """Return the ``slot[Z].psu[X].measure`` command tree.

        Sub-properties and sub-methods:
            - ``.i()``: The ``slot[Z].psu[X].measure.i()`` function.
            - ``.p()``: The ``slot[Z].psu[X].measure.p()`` function.
            - ``.r()``: The ``slot[Z].psu[X].measure.r()`` function.
            - ``.v()``: The ``slot[Z].psu[X].measure.v()`` function.
            - ``.aperture``: The ``slot[Z].psu[X].measure.aperture`` attribute.
            - ``.count``: The ``slot[Z].psu[X].measure.count`` attribute.
            - ``.nplc``: The ``slot[Z].psu[X].measure.nplc`` attribute.
            - ``.overlappedi()``: The ``slot[Z].psu[X].measure.overlappedi()`` function.
            - ``.overlappediv()``: The ``slot[Z].psu[X].measure.overlappediv()`` function.
            - ``.overlappedp()``: The ``slot[Z].psu[X].measure.overlappedp()`` function.
            - ``.overlappedr()``: The ``slot[Z].psu[X].measure.overlappedr()`` function.
            - ``.overlappedv()``: The ``slot[Z].psu[X].measure.overlappedv()`` function.
            - ``.rangei``: The ``slot[Z].psu[X].measure.rangei`` attribute.
            - ``.rangev``: The ``slot[Z].psu[X].measure.rangev`` attribute.
            - ``.rate``: The ``slot[Z].psu[X].measure.rate`` attribute.
            - ``.rel``: The ``slot[Z].psu[X].measure.rel`` command tree.
            - ``.tempcomp``: The ``slot[Z].psu[X].measure.tempcomp`` attribute.
        """
        return self._measure

    @property
    def overlapped(self) -> str:
        """Access the ``slot[Z].psu[X].overlapped`` attribute.

        Description:
            - This attribute contains the state of the overlapped mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].overlapped)`` query.
            - Setting this property to a value will send the ``slot[Z].psu[X].overlapped = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].overlapped = value
            - print(slot[Z].psu[X].overlapped)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".overlapped"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.overlapped)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overlapped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @overlapped.setter
    def overlapped(self, value: Union[str, float]) -> None:
        """Access the ``slot[Z].psu[X].overlapped`` attribute.

        Description:
            - This attribute contains the state of the overlapped mode.

        Usage:
            - Accessing this property will send the ``print(slot[Z].psu[X].overlapped)`` query.
            - Setting this property to a value will send the ``slot[Z].psu[X].overlapped = value``
              command.

        TSP Syntax:
            ```
            - slot[Z].psu[X].overlapped = value
            - print(slot[Z].psu[X].overlapped)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".overlapped", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.overlapped = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overlapped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def source(self) -> SlotItemPsuItemSource:
        """Return the ``slot[Z].psu[X].source`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.constantcurrent``: The ``slot[Z].psu[X].source.constantcurrent`` attribute.
            - ``.levelv``: The ``slot[Z].psu[X].source.levelv`` attribute.
            - ``.limiti``: The ``slot[Z].psu[X].source.limiti`` attribute.
            - ``.offmode``: The ``slot[Z].psu[X].source.offmode`` attribute.
            - ``.output``: The ``slot[Z].psu[X].source.output`` attribute.
            - ``.protect``: The ``slot[Z].psu[X].source.protect`` command tree.
            - ``.rangev``: The ``slot[Z].psu[X].source.rangev`` attribute.
            - ``.slewratev``: The ``slot[Z].psu[X].source.slewratev`` attribute.
        """
        return self._source

    @property
    def trigger(self) -> SlotItemPsuItemTrigger:
        """Return the ``slot[Z].psu[X].trigger`` command tree.

        Sub-properties and sub-methods:
            - ``.measure``: The ``slot[Z].psu[X].trigger.measure`` command tree.
            - ``.source``: The ``slot[Z].psu[X].trigger.source`` command tree.
        """
        return self._trigger

    def abort(self) -> None:
        """Run the ``slot[Z].psu[X].abort()`` function.

        Description:
            - This function terminates all overlapped operations on the specified channel.

        TSP Syntax:
            ```
            - slot[Z].psu[X].abort()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.abort()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.abort()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def makebuffer(self, buffer_size: str, *, buffer_name: Optional[str] = None) -> Buffervar:
        """Run the ``slot[Z].psu[X].makebuffer()`` function.

        Description:
            - This function creates a reading buffer.

        TSP Syntax:
            ```
            - slot[Z].psu[X].makebuffer()
            ```

        Args:
            buffer_size: The size of the reading buffer.
            buffer_name (optional): The name of the buffer variable to create. If not provided, an
                auto-generated variable will be used.

        Returns:
            The created buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        if buffer_name is None:
            buffer_name = f"private_custom_psu_buffer_{self._buffer_count}"
            self._buffer_count += 1
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{buffer_name} = {self._cmd_syntax}.makebuffer({buffer_size})"
            )
            self._device._user_created_custom_buffers.append(buffer_name)  # pyright: ignore[reportOptionalMemberAccess,reportPrivateUsage]  # noqa: SLF001
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.makebuffer()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
        return Buffervar(self._device, buffer_name)

    def reset(self) -> None:
        """Run the ``slot[Z].psu[X].reset()`` function.

        Description:
            - This function turns off the output and resets the commands that begin with psu[X]. to
              their default settings.

        TSP Syntax:
            ```
            - slot[Z].psu[X].reset()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def waitcomplete(self) -> None:
        """Run the ``slot[Z].psu[X].waitcomplete()`` function.

        Description:
            - This function waits for all previously started overlapped commands to complete on the
              specified channel of a module.

        TSP Syntax:
            ```
            - slot[Z].psu[X].waitcomplete()
            ```

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.waitcomplete()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.waitcomplete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItemFirmware(BaseTSPCmd):
    """The ``slot[Z].firmware`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.update()``: The ``slot[Z].firmware.update()`` function.
        - ``.verify()``: The ``slot[Z].firmware.verify()`` function.
    """

    def update(self) -> None:
        """Run the ``slot[Z].firmware.update()`` function.

        Description:
            - This function flashes a firmware image of a module installed in a slot after the image
              has been downloaded to the mainframe.

        TSP Syntax:
            ```
            - slot[Z].firmware.update()
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.update()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.update()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def verify(self) -> str:
        """Run the ``slot[Z].firmware.verify()`` function.

        Description:
            - This function verifys that an image downloaded to the mainframe is the exact firmware
              flashed onto a module.

        TSP Syntax:
            ```
            - slot[Z].firmware.verify()
            ```

        Info:
            - ``Z``, the module slot number.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.verify())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.verify()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[Z]`` command tree.

    Info:
        - ``Z``, the module slot number.

    Properties and methods:
        - ``.firmware``: The ``slot[Z].firmware`` command tree.
        - ``.license``: The ``slot[Z].license`` attribute.
        - ``.manufacturer``: The ``slot[Z].manufacturer`` attribute.
        - ``.model``: The ``slot[Z].model`` attribute.
        - ``.psu``: The ``slot[Z].psu[X]`` command tree.
        - ``.serialno``: The ``slot[Z].serialno`` attribute.
        - ``.smu``: The ``slot[Z].smu[X]`` command tree.
        - ``.status``: The ``slot[Z].status`` command tree.
        - ``.trigger``: The ``slot[Z].trigger`` command tree.
        - ``.version``: The ``slot[Z].version`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "slot[Z]") -> None:
        super().__init__(device, cmd_syntax)
        self._firmware = SlotItemFirmware(device, f"{self._cmd_syntax}.firmware")
        self._psu: Dict[int, SlotItemPsuItem] = DefaultDictPassKeyToFactory(
            lambda x: SlotItemPsuItem(device, f"{self._cmd_syntax}.psu[{x}]")
        )
        self._smu: Dict[int, SlotItemSmuItem] = DefaultDictPassKeyToFactory(
            lambda x: SlotItemSmuItem(device, f"{self._cmd_syntax}.smu[{x}]")
        )
        self._status = SlotItemStatus(device, f"{self._cmd_syntax}.status")
        self._trigger = SlotItemTrigger(device, f"{self._cmd_syntax}.trigger")

    @property
    def firmware(self) -> SlotItemFirmware:
        """Return the ``slot[Z].firmware`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.update()``: The ``slot[Z].firmware.update()`` function.
            - ``.verify()``: The ``slot[Z].firmware.verify()`` function.
        """
        return self._firmware

    @property
    def license(self) -> str:
        """Access the ``slot[Z].license`` attribute.

        Description:
            - This attribute stores the license of the module installed in the specified mainframe
              slot.

        Usage:
            - Accessing this property will send the ``print(slot[Z].license)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].license)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".license"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.license)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.license`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def manufacturer(self) -> str:
        """Access the ``slot[Z].manufacturer`` attribute.

        Description:
            - This attribute stores the manufacturer of the module in the specified mainframe slot.

        Usage:
            - Accessing this property will send the ``print(slot[Z].manufacturer)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].manufacturer)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".manufacturer"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.manufacturer)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.manufacturer`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def model(self) -> str:
        """Access the ``slot[Z].model`` attribute.

        Description:
            - This attribute stores the model number of the module in the specified mainframe slot.

        Usage:
            - Accessing this property will send the ``print(slot[Z].model)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].model)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".model"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.model)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.model`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def psu(self) -> Dict[int, SlotItemPsuItem]:
        """Return the ``slot[Z].psu[X]`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.abort()``: The ``slot[Z].psu[X].abort()`` function.
            - ``.configlist``: The ``slot[Z].psu[X].configlist`` command tree.
            - ``.defbuffer1``: The ``slot[Z].psu[X].defbuffer1`` attribute.
            - ``.defbuffer2``: The ``slot[Z].psu[X].defbuffer2`` attribute.
            - ``.makebuffer()``: The ``slot[Z].psu[X].makebuffer()`` function.
            - ``.measure``: The ``slot[Z].psu[X].measure`` command tree.
            - ``.overlapped``: The ``slot[Z].psu[X].overlapped`` attribute.
            - ``.reset()``: The ``slot[Z].psu[X].reset()`` function.
            - ``.source``: The ``slot[Z].psu[X].source`` command tree.
            - ``.trigger``: The ``slot[Z].psu[X].trigger`` command tree.
            - ``.waitcomplete()``: The ``slot[Z].psu[X].waitcomplete()`` function.
        """
        return self._psu

    @property
    def serialno(self) -> str:
        """Access the ``slot[Z].serialno`` attribute.

        Description:
            - This attribute stores the serial number of the module in the specified mainframe slot.

        Usage:
            - Accessing this property will send the ``print(slot[Z].serialno)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].serialno)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".serialno"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.serialno)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.serialno`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def smu(self) -> Dict[int, SlotItemSmuItem]:
        """Return the ``slot[Z].smu[X]`` command tree.

        Info:
            - ``Z``, the module slot number.
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.abort()``: The ``slot[Z].smu[X].abort()`` function.
            - ``.configlist``: The ``slot[Z].smu[X].configlist`` command tree.
            - ``.contact``: The ``slot[Z].smu[X].contact`` command tree.
            - ``.defbuffer1``: The ``slot[Z].smu[X].defbuffer1`` attribute.
            - ``.defbuffer2``: The ``slot[Z].smu[X].defbuffer2`` attribute.
            - ``.guard``: The ``slot[Z].smu[X].guard`` command tree.
            - ``.makebuffer()``: The ``slot[Z].smu[X].makebuffer()`` function.
            - ``.measure``: The ``slot[Z].smu[X].measure`` command tree.
            - ``.overlapped``: The ``slot[Z].smu[X].overlapped`` attribute.
            - ``.reset()``: The ``slot[Z].smu[X].reset()`` function.
            - ``.sense``: The ``slot[Z].smu[X].sense`` attribute.
            - ``.source``: The ``slot[Z].smu[X].source`` command tree.
            - ``.trigger``: The ``slot[Z].smu[X].trigger`` command tree.
            - ``.waitcomplete()``: The ``slot[Z].smu[X].waitcomplete()`` function.
        """
        return self._smu

    @property
    def status(self) -> SlotItemStatus:
        """Return the ``slot[Z].status`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.measurement``: The ``slot[Z].status.measurement`` command tree.
            - ``.operation``: The ``slot[Z].status.operation`` command tree.
            - ``.questionable``: The ``slot[Z].status.questionable`` command tree.
            - ``.reset()``: The ``slot[Z].status.reset()`` function.
        """
        return self._status

    @property
    def trigger(self) -> SlotItemTrigger:
        """Return the ``slot[Z].trigger`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.model``: The ``slot[Z].trigger.model`` command tree.
        """
        return self._trigger

    @property
    def version(self) -> str:
        """Access the ``slot[Z].version`` attribute.

        Description:
            - This attribute stores the firmware version number of the module in the specified slot
              of the mainframe.

        Usage:
            - Accessing this property will send the ``print(slot[Z].version)`` query.

        TSP Syntax:
            ```
            - print(slot[Z].version)
            ```

        Info:
            - ``Z``, the module slot number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".version"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.version)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.version`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
