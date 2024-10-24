# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The status commands module.

These commands are used in the following models:
SMU2606B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - status.condition
    - status.measurement.buffer_available.condition
    - status.measurement.buffer_available.enable
    - status.measurement.buffer_available.event
    - status.measurement.buffer_available.ntr
    - status.measurement.buffer_available.ptr
    - status.measurement.condition
    - status.measurement.current_limit.condition
    - status.measurement.current_limit.enable
    - status.measurement.current_limit.event
    - status.measurement.current_limit.ntr
    - status.measurement.current_limit.ptr
    - status.measurement.enable
    - status.measurement.event
    - status.measurement.instrument.condition
    - status.measurement.instrument.enable
    - status.measurement.instrument.event
    - status.measurement.instrument.ntr
    - status.measurement.instrument.ptr
    - status.measurement.instrument.smuX.condition
    - status.measurement.instrument.smuX.enable
    - status.measurement.instrument.smuX.event
    - status.measurement.instrument.smuX.ntr
    - status.measurement.instrument.smuX.ptr
    - status.measurement.ntr
    - status.measurement.ptr
    - status.measurement.reading_overflow.condition
    - status.measurement.reading_overflow.enable
    - status.measurement.reading_overflow.event
    - status.measurement.reading_overflow.ntr
    - status.measurement.reading_overflow.ptr
    - status.measurement.voltage_limit.condition
    - status.measurement.voltage_limit.enable
    - status.measurement.voltage_limit.event
    - status.measurement.voltage_limit.ntr
    - status.measurement.voltage_limit.ptr
    - status.node_enable
    - status.node_event
    - status.operation.calibrating.condition
    - status.operation.calibrating.enable
    - status.operation.calibrating.event
    - status.operation.calibrating.ntr
    - status.operation.calibrating.ptr
    - status.operation.condition
    - status.operation.enable
    - status.operation.event
    - status.operation.instrument.condition
    - status.operation.instrument.digio.condition
    - status.operation.instrument.digio.enable
    - status.operation.instrument.digio.event
    - status.operation.instrument.digio.ntr
    - status.operation.instrument.digio.ptr
    - status.operation.instrument.digio.trigger_overrun.condition
    - status.operation.instrument.digio.trigger_overrun.enable
    - status.operation.instrument.digio.trigger_overrun.event
    - status.operation.instrument.digio.trigger_overrun.ntr
    - status.operation.instrument.digio.trigger_overrun.ptr
    - status.operation.instrument.enable
    - status.operation.instrument.event
    - status.operation.instrument.lan.condition
    - status.operation.instrument.lan.enable
    - status.operation.instrument.lan.event
    - status.operation.instrument.lan.ntr
    - status.operation.instrument.lan.ptr
    - status.operation.instrument.lan.trigger_overrun.condition
    - status.operation.instrument.lan.trigger_overrun.enable
    - status.operation.instrument.lan.trigger_overrun.event
    - status.operation.instrument.lan.trigger_overrun.ntr
    - status.operation.instrument.lan.trigger_overrun.ptr
    - status.operation.instrument.ntr
    - status.operation.instrument.ptr
    - status.operation.instrument.smuX.condition
    - status.operation.instrument.smuX.enable
    - status.operation.instrument.smuX.event
    - status.operation.instrument.smuX.ntr
    - status.operation.instrument.smuX.ptr
    - status.operation.instrument.smuX.trigger_overrrun.condition
    - status.operation.instrument.smuX.trigger_overrrun.enable
    - status.operation.instrument.smuX.trigger_overrrun.event
    - status.operation.instrument.smuX.trigger_overrrun.ntr
    - status.operation.instrument.smuX.trigger_overrrun.ptr
    - status.operation.instrument.trigger_blender.condition
    - status.operation.instrument.trigger_blender.enable
    - status.operation.instrument.trigger_blender.event
    - status.operation.instrument.trigger_blender.ntr
    - status.operation.instrument.trigger_blender.ptr
    - status.operation.instrument.trigger_blender.trigger_overrun.condition
    - status.operation.instrument.trigger_blender.trigger_overrun.enable
    - status.operation.instrument.trigger_blender.trigger_overrun.event
    - status.operation.instrument.trigger_blender.trigger_overrun.ntr
    - status.operation.instrument.trigger_blender.trigger_overrun.ptr
    - status.operation.instrument.trigger_timer.condition
    - status.operation.instrument.trigger_timer.enable
    - status.operation.instrument.trigger_timer.event
    - status.operation.instrument.trigger_timer.ntr
    - status.operation.instrument.trigger_timer.ptr
    - status.operation.instrument.trigger_timer.trigger_overrun.condition
    - status.operation.instrument.trigger_timer.trigger_overrun.enable
    - status.operation.instrument.trigger_timer.trigger_overrun.event
    - status.operation.instrument.trigger_timer.trigger_overrun.ntr
    - status.operation.instrument.trigger_timer.trigger_overrun.ptr
    - status.operation.instrument.tsplink.condition
    - status.operation.instrument.tsplink.enable
    - status.operation.instrument.tsplink.event
    - status.operation.instrument.tsplink.ntr
    - status.operation.instrument.tsplink.ptr
    - status.operation.instrument.tsplink.trigger_overrun.condition
    - status.operation.instrument.tsplink.trigger_overrun.enable
    - status.operation.instrument.tsplink.trigger_overrun.event
    - status.operation.instrument.tsplink.trigger_overrun.ntr
    - status.operation.instrument.tsplink.trigger_overrun.ptr
    - status.operation.measuring.condition
    - status.operation.measuring.enable
    - status.operation.measuring.event
    - status.operation.measuring.ntr
    - status.operation.measuring.ptr
    - status.operation.ntr
    - status.operation.ptr
    - status.operation.remote.condition
    - status.operation.remote.enable
    - status.operation.remote.event
    - status.operation.remote.ntr
    - status.operation.remote.ptr
    - status.operation.sweeping.condition
    - status.operation.sweeping.enable
    - status.operation.sweeping.event
    - status.operation.sweeping.ntr
    - status.operation.sweeping.ptr
    - status.operation.trigger_overrun.condition
    - status.operation.trigger_overrun.enable
    - status.operation.trigger_overrun.event
    - status.operation.trigger_overrun.ntr
    - status.operation.trigger_overrun.ptr
    - status.operation.user.condition
    - status.operation.user.enable
    - status.operation.user.event
    - status.operation.user.ntr
    - status.operation.user.ptr
    - status.questionable.calibration.condition
    - status.questionable.calibration.enable
    - status.questionable.calibration.event
    - status.questionable.calibration.ntr
    - status.questionable.calibration.ptr
    - status.questionable.condition
    - status.questionable.enable
    - status.questionable.event
    - status.questionable.instrument.condition
    - status.questionable.instrument.enable
    - status.questionable.instrument.event
    - status.questionable.instrument.ntr
    - status.questionable.instrument.ptr
    - status.questionable.instrument.smuX.condition
    - status.questionable.instrument.smuX.enable
    - status.questionable.instrument.smuX.event
    - status.questionable.instrument.smuX.ntr
    - status.questionable.instrument.smuX.ptr
    - status.questionable.ntr
    - status.questionable.over_temperature.condition
    - status.questionable.over_temperature.enable
    - status.questionable.over_temperature.event
    - status.questionable.over_temperature.ntr
    - status.questionable.over_temperature.ptr
    - status.questionable.ptr
    - status.questionable.unstable_output.condition
    - status.questionable.unstable_output.enable
    - status.questionable.unstable_output.event
    - status.questionable.unstable_output.ntr
    - status.questionable.unstable_output.ptr
    - status.request_enable
    - status.request_event
    - status.reset()
    - status.standard.condition
    - status.standard.enable
    - status.standard.event
    - status.standard.ntr
    - status.standard.ptr
    - status.system.condition
    - status.system.enable
    - status.system.event
    - status.system.ntr
    - status.system.ptr
    - status.system2.condition
    - status.system2.enable
    - status.system2.event
    - status.system2.ntr
    - status.system2.ptr
    - status.system3.condition
    - status.system3.enable
    - status.system3.event
    - status.system3.ntr
    - status.system3.ptr
    - status.system4.condition
    - status.system4.enable
    - status.system4.event
    - status.system4.ntr
    - status.system4.ptr
    - status.system5.condition
    - status.system5.enable
    - status.system5.event
    - status.system5.ntr
    - status.system5.ptr
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import (
    BaseTSPCmd,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedChannel,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class StatusSystem5(BaseTSPCmd):
    """The ``status.system5`` command tree.

    Constants:
        - ``.NODE57``: B1. This attributes manages the TSP-Link system summary register of the
          status model for node.
        - ``.NODE58``: B2. This attributes manages the TSP-Link system summary register of the
          status model for node.
        - ``.NODE59``: B3. This attributes manages the TSP-Link system summary register of the
          status model for node.
        - ``.NODE60``: B4. This attributes manages the TSP-Link system summary register of the
          status model for node.
        - ``.NODE61``: B5. This attributes manages the TSP-Link system summary register of the
          status model for node.
        - ``.NODE62``: B6. This attributes manages the TSP-Link system summary register of the
          status model for node.
        - ``.NODE63``: B7. This attributes manages the TSP-Link system summary register of the
          status model for node.
        - ``.NODE64``: B8. This attributes manages the TSP-Link system summary register of the
          status model for node.

    Properties and methods:
        - ``.condition``: The ``status.system5.condition`` attribute.
        - ``.enable``: The ``status.system5.enable`` attribute.
        - ``.event``: The ``status.system5.event`` attribute.
        - ``.ntr``: The ``status.system5.ntr`` attribute.
        - ``.ptr``: The ``status.system5.ptr`` attribute.
    """

    NODE57 = "status.system5.NODE57"
    """str: B1. This attributes manages the TSP-Link system summary register of the status model for node."""  # noqa: E501
    NODE58 = "status.system5.NODE58"
    """str: B2. This attributes manages the TSP-Link system summary register of the status model for node."""  # noqa: E501
    NODE59 = "status.system5.NODE59"
    """str: B3. This attributes manages the TSP-Link system summary register of the status model for node."""  # noqa: E501
    NODE60 = "status.system5.NODE60"
    """str: B4. This attributes manages the TSP-Link system summary register of the status model for node."""  # noqa: E501
    NODE61 = "status.system5.NODE61"
    """str: B5. This attributes manages the TSP-Link system summary register of the status model for node."""  # noqa: E501
    NODE62 = "status.system5.NODE62"
    """str: B6. This attributes manages the TSP-Link system summary register of the status model for node."""  # noqa: E501
    NODE63 = "status.system5.NODE63"
    """str: B7. This attributes manages the TSP-Link system summary register of the status model for node."""  # noqa: E501
    NODE64 = "status.system5.NODE64"
    """str: B8. This attributes manages the TSP-Link system summary register of the status model for node."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.system5.condition`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 57 through 64.

        Usage:
            - Accessing this property will send the ``print(status.system5.condition)`` query.

        TSP Syntax:
            ```
            - print(status.system5.condition)
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
        """Access the ``status.system5.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 57 through 64.

        Usage:
            - Accessing this property will send the ``print(status.system5.enable)`` query.
            - Setting this property to a value will send the ``status.system5.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system5.enable = value
            - print(status.system5.enable)
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
        """Access the ``status.system5.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 57 through 64.

        Usage:
            - Accessing this property will send the ``print(status.system5.enable)`` query.
            - Setting this property to a value will send the ``status.system5.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system5.enable = value
            - print(status.system5.enable)
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
        """Access the ``status.system5.event`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 57 through 64.

        Usage:
            - Accessing this property will send the ``print(status.system5.event)`` query.

        TSP Syntax:
            ```
            - print(status.system5.event)
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
        """Access the ``status.system5.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 57 through 64.

        Usage:
            - Accessing this property will send the ``print(status.system5.ntr)`` query.
            - Setting this property to a value will send the ``status.system5.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system5.ntr = value
            - print(status.system5.ntr)
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
        """Access the ``status.system5.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 57 through 64.

        Usage:
            - Accessing this property will send the ``print(status.system5.ntr)`` query.
            - Setting this property to a value will send the ``status.system5.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system5.ntr = value
            - print(status.system5.ntr)
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
        """Access the ``status.system5.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 57 through 64.

        Usage:
            - Accessing this property will send the ``print(status.system5.ptr)`` query.
            - Setting this property to a value will send the ``status.system5.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system5.ptr = value
            - print(status.system5.ptr)
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
        """Access the ``status.system5.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 57 through 64.

        Usage:
            - Accessing this property will send the ``print(status.system5.ptr)`` query.
            - Setting this property to a value will send the ``status.system5.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system5.ptr = value
            - print(status.system5.ptr)
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


class StatusSystem4(BaseTSPCmd):
    """The ``status.system4`` command tree.

    Constants:
        - ``.EXT``: B0. This attributes manages the TSP-Link system summary register of the status
          model for nodes 43 through 56.
        - ``.EXTENSION_BIT``: B0. This attributes manages the TSP-Link system summary register of
          the status model for nodes 43 through 56.
        - ``.NODE43``: B1. This attributes manages the TSP-Link system summary register of the
          status model for node 43.
        - ``.NODE44``: B2. This attributes manages the TSP-Link system summary register of the
          status model for node 44.
        - ``.NODE45``: B3. This attributes manages the TSP-Link system summary register of the
          status model for node 45.
        - ``.NODE46``: B4. This attributes manages the TSP-Link system summary register of the
          status model for node 46.
        - ``.NODE47``: B5. This attributes manages the TSP-Link system summary register of the
          status model for node 47.
        - ``.NODE48``: B6. This attributes manages the TSP-Link system summary register of the
          status model for node 48.
        - ``.NODE49``: B7. This attributes manages the TSP-Link system summary register of the
          status model for node 49.
        - ``.NODE50``: B8. This attributes manages the TSP-Link system summary register of the
          status model for node 50.
        - ``.NODE51``: B9. This attributes manages the TSP-Link system summary register of the
          status model for node 51.
        - ``.NODE52``: B10. This attributes manages the TSP-Link system summary register of the
          status model for node 52.
        - ``.NODE53``: B11. This attributes manages the TSP-Link system summary register of the
          status model for node 53.
        - ``.NODE54``: B12. This attributes manages the TSP-Link system summary register of the
          status model for node 54.
        - ``.NODE55``: B13. This attributes manages the TSP-Link system summary register of the
          status model for node 55.
        - ``.NODE56``: B14. This attributes manages the TSP-Link system summary register of the
          status model for node 56.

    Properties and methods:
        - ``.condition``: The ``status.system4.condition`` attribute.
        - ``.enable``: The ``status.system4.enable`` attribute.
        - ``.event``: The ``status.system4.event`` attribute.
        - ``.ntr``: The ``status.system4.ntr`` attribute.
        - ``.ptr``: The ``status.system4.ptr`` attribute.
    """

    EXT = "status.system4.EXT"
    """str: B0. This attributes manages the TSP-Link system summary register of the status model for nodes 43 through 56."""  # noqa: E501
    EXTENSION_BIT = "status.system4.EXTENSION_BIT"
    """str: B0. This attributes manages the TSP-Link system summary register of the status model for nodes 43 through 56."""  # noqa: E501
    NODE43 = "status.system4.NODE43"
    """str: B1. This attributes manages the TSP-Link system summary register of the status model for node 43."""  # noqa: E501
    NODE44 = "status.system4.NODE44"
    """str: B2. This attributes manages the TSP-Link system summary register of the status model for node 44."""  # noqa: E501
    NODE45 = "status.system4.NODE45"
    """str: B3. This attributes manages the TSP-Link system summary register of the status model for node 45."""  # noqa: E501
    NODE46 = "status.system4.NODE46"
    """str: B4. This attributes manages the TSP-Link system summary register of the status model for node 46."""  # noqa: E501
    NODE47 = "status.system4.NODE47"
    """str: B5. This attributes manages the TSP-Link system summary register of the status model for node 47."""  # noqa: E501
    NODE48 = "status.system4.NODE48"
    """str: B6. This attributes manages the TSP-Link system summary register of the status model for node 48."""  # noqa: E501
    NODE49 = "status.system4.NODE49"
    """str: B7. This attributes manages the TSP-Link system summary register of the status model for node 49."""  # noqa: E501
    NODE50 = "status.system4.NODE50"
    """str: B8. This attributes manages the TSP-Link system summary register of the status model for node 50."""  # noqa: E501
    NODE51 = "status.system4.NODE51"
    """str: B9. This attributes manages the TSP-Link system summary register of the status model for node 51."""  # noqa: E501
    NODE52 = "status.system4.NODE52"
    """str: B10. This attributes manages the TSP-Link system summary register of the status model for node 52."""  # noqa: E501
    NODE53 = "status.system4.NODE53"
    """str: B11. This attributes manages the TSP-Link system summary register of the status model for node 53."""  # noqa: E501
    NODE54 = "status.system4.NODE54"
    """str: B12. This attributes manages the TSP-Link system summary register of the status model for node 54."""  # noqa: E501
    NODE55 = "status.system4.NODE55"
    """str: B13. This attributes manages the TSP-Link system summary register of the status model for node 55."""  # noqa: E501
    NODE56 = "status.system4.NODE56"
    """str: B14. This attributes manages the TSP-Link system summary register of the status model for node 56."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.system4.condition`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 43 through 56.

        Usage:
            - Accessing this property will send the ``print(status.system4.condition)`` query.

        TSP Syntax:
            ```
            - print(status.system4.condition)
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
        """Access the ``status.system4.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 43 through 56.

        Usage:
            - Accessing this property will send the ``print(status.system4.enable)`` query.
            - Setting this property to a value will send the ``status.system4.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system4.enable = value
            - print(status.system4.enable)
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
        """Access the ``status.system4.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 43 through 56.

        Usage:
            - Accessing this property will send the ``print(status.system4.enable)`` query.
            - Setting this property to a value will send the ``status.system4.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system4.enable = value
            - print(status.system4.enable)
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
        """Access the ``status.system4.event`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 43 through 56.

        Usage:
            - Accessing this property will send the ``print(status.system4.event)`` query.

        TSP Syntax:
            ```
            - print(status.system4.event)
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
        """Access the ``status.system4.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 43 through 56.

        Usage:
            - Accessing this property will send the ``print(status.system4.ntr)`` query.
            - Setting this property to a value will send the ``status.system4.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system4.ntr = value
            - print(status.system4.ntr)
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
        """Access the ``status.system4.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 43 through 56.

        Usage:
            - Accessing this property will send the ``print(status.system4.ntr)`` query.
            - Setting this property to a value will send the ``status.system4.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system4.ntr = value
            - print(status.system4.ntr)
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
        """Access the ``status.system4.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 43 through 56.

        Usage:
            - Accessing this property will send the ``print(status.system4.ptr)`` query.
            - Setting this property to a value will send the ``status.system4.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system4.ptr = value
            - print(status.system4.ptr)
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
        """Access the ``status.system4.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 43 through 56.

        Usage:
            - Accessing this property will send the ``print(status.system4.ptr)`` query.
            - Setting this property to a value will send the ``status.system4.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system4.ptr = value
            - print(status.system4.ptr)
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


class StatusSystem3(BaseTSPCmd):
    """The ``status.system3`` command tree.

    Constants:
        - ``.EXT``: B0. This attribute manages the TSP-Link system summary register of the status
          model for nodes 29 through 42.
        - ``.EXTENSION_BIT``: B0. This attribute manages the TSP-Link system summary register of the
          status model for nodes 29 through 42.
        - ``.NODE29``: B1. This attribute manages the TSP-Link system summary register of the status
          model for node 29.
        - ``.NODE30``: B2. This attribute manages the TSP-Link system summary register of the status
          model for node 30.
        - ``.NODE31``: B3. This attribute manages the TSP-Link system summary register of the status
          model for node 31.
        - ``.NODE32``: B4. This attribute manages the TSP-Link system summary register of the status
          model for node 32.
        - ``.NODE33``: B5. This attribute manages the TSP-Link system summary register of the status
          model for node 33.
        - ``.NODE34``: B6. This attribute manages the TSP-Link system summary register of the status
          model for node 34.
        - ``.NODE35``: B7. This attribute manages the TSP-Link system summary register of the status
          model for node 35.
        - ``.NODE36``: B7. This attribute manages the TSP-Link system summary register of the status
          model for node 36.
        - ``.NODE37``: B8. This attribute manages the TSP-Link system summary register of the status
          model for node 37.
        - ``.NODE38``: B9. This attribute manages the TSP-Link system summary register of the status
          model for node 38.
        - ``.NODE39``: B10. This attribute manages the TSP-Link system summary register of the
          status model for node 39.
        - ``.NODE40``: B11. This attribute manages the TSP-Link system summary register of the
          status model for node 40.
        - ``.NODE41``: B12. This attribute manages the TSP-Link system summary register of the
          status model for node 41.
        - ``.NODE42``: B13. This attribute manages the TSP-Link system summary register of the
          status model for node 42.

    Properties and methods:
        - ``.condition``: The ``status.system3.condition`` attribute.
        - ``.enable``: The ``status.system3.enable`` attribute.
        - ``.event``: The ``status.system3.event`` attribute.
        - ``.ntr``: The ``status.system3.ntr`` attribute.
        - ``.ptr``: The ``status.system3.ptr`` attribute.
    """

    EXT = "status.system3.EXT"
    """str: B0. This attribute manages the TSP-Link system summary register of the status model for nodes 29 through 42."""  # noqa: E501
    EXTENSION_BIT = "status.system3.EXTENSION_BIT"
    """str: B0. This attribute manages the TSP-Link system summary register of the status model for nodes 29 through 42."""  # noqa: E501
    NODE29 = "status.system3.NODE29"
    """str: B1. This attribute manages the TSP-Link system summary register of the status model for node 29."""  # noqa: E501
    NODE30 = "status.system3.NODE30"
    """str: B2. This attribute manages the TSP-Link system summary register of the status model for node 30."""  # noqa: E501
    NODE31 = "status.system3.NODE31"
    """str: B3. This attribute manages the TSP-Link system summary register of the status model for node 31."""  # noqa: E501
    NODE32 = "status.system3.NODE32"
    """str: B4. This attribute manages the TSP-Link system summary register of the status model for node 32."""  # noqa: E501
    NODE33 = "status.system3.NODE33"
    """str: B5. This attribute manages the TSP-Link system summary register of the status model for node 33."""  # noqa: E501
    NODE34 = "status.system3.NODE34"
    """str: B6. This attribute manages the TSP-Link system summary register of the status model for node 34."""  # noqa: E501
    NODE35 = "status.system3.NODE35"
    """str: B7. This attribute manages the TSP-Link system summary register of the status model for node 35."""  # noqa: E501
    NODE36 = "status.system3.NODE36"
    """str: B7. This attribute manages the TSP-Link system summary register of the status model for node 36."""  # noqa: E501
    NODE37 = "status.system3.NODE37"
    """str: B8. This attribute manages the TSP-Link system summary register of the status model for node 37."""  # noqa: E501
    NODE38 = "status.system3.NODE38"
    """str: B9. This attribute manages the TSP-Link system summary register of the status model for node 38."""  # noqa: E501
    NODE39 = "status.system3.NODE39"
    """str: B10. This attribute manages the TSP-Link system summary register of the status model for node 39."""  # noqa: E501
    NODE40 = "status.system3.NODE40"
    """str: B11. This attribute manages the TSP-Link system summary register of the status model for node 40."""  # noqa: E501
    NODE41 = "status.system3.NODE41"
    """str: B12. This attribute manages the TSP-Link system summary register of the status model for node 41."""  # noqa: E501
    NODE42 = "status.system3.NODE42"
    """str: B13. This attribute manages the TSP-Link system summary register of the status model for node 42."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.system3.condition`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 29 through 42.

        Usage:
            - Accessing this property will send the ``print(status.system3.condition)`` query.

        TSP Syntax:
            ```
            - print(status.system3.condition)
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
        """Access the ``status.system3.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 29 through 42.

        Usage:
            - Accessing this property will send the ``print(status.system3.enable)`` query.
            - Setting this property to a value will send the ``status.system3.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system3.enable = value
            - print(status.system3.enable)
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
        """Access the ``status.system3.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 29 through 42.

        Usage:
            - Accessing this property will send the ``print(status.system3.enable)`` query.
            - Setting this property to a value will send the ``status.system3.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system3.enable = value
            - print(status.system3.enable)
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
        """Access the ``status.system3.event`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 29 through 42.

        Usage:
            - Accessing this property will send the ``print(status.system3.event)`` query.

        TSP Syntax:
            ```
            - print(status.system3.event)
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
        """Access the ``status.system3.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 29 through 42.

        Usage:
            - Accessing this property will send the ``print(status.system3.ntr)`` query.
            - Setting this property to a value will send the ``status.system3.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system3.ntr = value
            - print(status.system3.ntr)
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
        """Access the ``status.system3.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 29 through 42.

        Usage:
            - Accessing this property will send the ``print(status.system3.ntr)`` query.
            - Setting this property to a value will send the ``status.system3.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system3.ntr = value
            - print(status.system3.ntr)
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
        """Access the ``status.system3.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 29 through 42.

        Usage:
            - Accessing this property will send the ``print(status.system3.ptr)`` query.
            - Setting this property to a value will send the ``status.system3.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system3.ptr = value
            - print(status.system3.ptr)
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
        """Access the ``status.system3.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 29 through 42.

        Usage:
            - Accessing this property will send the ``print(status.system3.ptr)`` query.
            - Setting this property to a value will send the ``status.system3.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system3.ptr = value
            - print(status.system3.ptr)
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


class StatusSystem2(BaseTSPCmd):
    """The ``status.system2`` command tree.

    Constants:
        - ``.EXT``: B0. Manages the TSP-Link system summary register of the status model for nodes
          15 through 28.
        - ``.EXTENSION_BIT``: B0. Manages the TSP-Link system summary register of the status model
          for nodes 15 through 28.
        - ``.NODE15``: B1. Manages the TSP-Link system summary register of the status model for node
          15.
        - ``.NODE16``: B2. Manages the TSP-Link system summary register of the status model for node
          16.
        - ``.NODE17``: B3. Manages the TSP-Link system summary register of the status model for node
          17.
        - ``.NODE18``: B4. Manages the TSP-Link system summary register of the status model for node
          18.
        - ``.NODE19``: B5. Manages the TSP-Link system summary register of the status model for node
          19.
        - ``.NODE20``: B6. Manages the TSP-Link system summary register of the status model for node
          20.
        - ``.NODE21``: B7. Manages the TSP-Link system summary register of the status model for node
          21.
        - ``.NODE22``: B8. Manages the TSP-Link system summary register of the status model for node
          22.
        - ``.NODE23``: B9. Manages the TSP-Link system summary register of the status model for node
          23.
        - ``.NODE24``: B10. Manages the TSP-Link system summary register of the status model for
          node 24.
        - ``.NODE25``: B11. Manages the TSP-Link system summary register of the status model for
          node 25.
        - ``.NODE26``: B12. Manages the TSP-Link system summary register of the status model for
          node 26.
        - ``.NODE27``: B13. Manages the TSP-Link system summary register of the status model for
          node 27.
        - ``.NODE28``: B14. Manages the TSP-Link system summary register of the status model for
          node 28.

    Properties and methods:
        - ``.condition``: The ``status.system2.condition`` attribute.
        - ``.enable``: The ``status.system2.enable`` attribute.
        - ``.event``: The ``status.system2.event`` attribute.
        - ``.ntr``: The ``status.system2.ntr`` attribute.
        - ``.ptr``: The ``status.system2.ptr`` attribute.
    """

    EXT = "status.system2.EXT"
    """str: B0. Manages the TSP-Link system summary register of the status model for nodes 15 through 28."""  # noqa: E501
    EXTENSION_BIT = "status.system2.EXTENSION_BIT"
    """str: B0. Manages the TSP-Link system summary register of the status model for nodes 15 through 28."""  # noqa: E501
    NODE15 = "status.system2.NODE15"
    """str: B1. Manages the TSP-Link system summary register of the status model for node 15."""
    NODE16 = "status.system2.NODE16"
    """str: B2. Manages the TSP-Link system summary register of the status model for node 16."""
    NODE17 = "status.system2.NODE17"
    """str: B3. Manages the TSP-Link system summary register of the status model for node 17."""
    NODE18 = "status.system2.NODE18"
    """str: B4. Manages the TSP-Link system summary register of the status model for node 18."""
    NODE19 = "status.system2.NODE19"
    """str: B5. Manages the TSP-Link system summary register of the status model for node 19."""
    NODE20 = "status.system2.NODE20"
    """str: B6. Manages the TSP-Link system summary register of the status model for node 20."""
    NODE21 = "status.system2.NODE21"
    """str: B7. Manages the TSP-Link system summary register of the status model for node 21."""
    NODE22 = "status.system2.NODE22"
    """str: B8. Manages the TSP-Link system summary register of the status model for node 22."""
    NODE23 = "status.system2.NODE23"
    """str: B9. Manages the TSP-Link system summary register of the status model for node 23."""
    NODE24 = "status.system2.NODE24"
    """str: B10. Manages the TSP-Link system summary register of the status model for node 24."""
    NODE25 = "status.system2.NODE25"
    """str: B11. Manages the TSP-Link system summary register of the status model for node 25."""
    NODE26 = "status.system2.NODE26"
    """str: B12. Manages the TSP-Link system summary register of the status model for node 26."""
    NODE27 = "status.system2.NODE27"
    """str: B13. Manages the TSP-Link system summary register of the status model for node 27."""
    NODE28 = "status.system2.NODE28"
    """str: B14. Manages the TSP-Link system summary register of the status model for node 28."""

    @property
    def condition(self) -> str:
        """Access the ``status.system2.condition`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 15 through 28.

        Usage:
            - Accessing this property will send the ``print(status.system2.condition)`` query.

        TSP Syntax:
            ```
            - print(status.system2.condition)
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
        """Access the ``status.system2.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 15 through 28.

        Usage:
            - Accessing this property will send the ``print(status.system2.enable)`` query.
            - Setting this property to a value will send the ``status.system2.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system2.enable = value
            - print(status.system2.enable)
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
        """Access the ``status.system2.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 15 through 28.

        Usage:
            - Accessing this property will send the ``print(status.system2.enable)`` query.
            - Setting this property to a value will send the ``status.system2.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system2.enable = value
            - print(status.system2.enable)
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
        """Access the ``status.system2.event`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 15 through 28.

        Usage:
            - Accessing this property will send the ``print(status.system2.event)`` query.

        TSP Syntax:
            ```
            - print(status.system2.event)
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
        """Access the ``status.system2.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 15 through 28.

        Usage:
            - Accessing this property will send the ``print(status.system2.ntr)`` query.
            - Setting this property to a value will send the ``status.system2.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system2.ntr = value
            - print(status.system2.ntr)
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
        """Access the ``status.system2.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 15 through 28.

        Usage:
            - Accessing this property will send the ``print(status.system2.ntr)`` query.
            - Setting this property to a value will send the ``status.system2.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system2.ntr = value
            - print(status.system2.ntr)
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
        """Access the ``status.system2.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 15 through 28.

        Usage:
            - Accessing this property will send the ``print(status.system2.ptr)`` query.
            - Setting this property to a value will send the ``status.system2.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system2.ptr = value
            - print(status.system2.ptr)
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
        """Access the ``status.system2.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 15 through 28.

        Usage:
            - Accessing this property will send the ``print(status.system2.ptr)`` query.
            - Setting this property to a value will send the ``status.system2.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system2.ptr = value
            - print(status.system2.ptr)
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


class StatusSystem(BaseTSPCmd):
    """The ``status.system`` command tree.

    Constants:
        - ``.EXT``: B0. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.EXTENSION_BIT``: B0. In an expanded system (TSP-Link), this is used to read or write to
          the system summary register.
        - ``.NODE1``: B1. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE10``: B10. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE11``: B11. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE12``: B12. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE13``: B13. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE14``: B14. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE2``: B2. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE3``: B3. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE4``: B4. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE5``: B5. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE6``: B6. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE7``: B7. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE8``: B8. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.
        - ``.NODE9``: B9. In an expanded system (TSP-Link), this is used to read or write to the
          system summary register.

    Properties and methods:
        - ``.condition``: The ``status.system.condition`` attribute.
        - ``.enable``: The ``status.system.enable`` attribute.
        - ``.event``: The ``status.system.event`` attribute.
        - ``.ntr``: The ``status.system.ntr`` attribute.
        - ``.ptr``: The ``status.system.ptr`` attribute.
    """

    EXT = "status.system.EXT"
    """str: B0. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    EXTENSION_BIT = "status.system.EXTENSION_BIT"
    """str: B0. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE1 = "status.system.NODE1"
    """str: B1. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE10 = "status.system.NODE10"
    """str: B10. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE11 = "status.system.NODE11"
    """str: B11. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE12 = "status.system.NODE12"
    """str: B12. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE13 = "status.system.NODE13"
    """str: B13. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE14 = "status.system.NODE14"
    """str: B14. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE2 = "status.system.NODE2"
    """str: B2. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE3 = "status.system.NODE3"
    """str: B3. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE4 = "status.system.NODE4"
    """str: B4. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE5 = "status.system.NODE5"
    """str: B5. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE6 = "status.system.NODE6"
    """str: B6. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE7 = "status.system.NODE7"
    """str: B7. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE8 = "status.system.NODE8"
    """str: B8. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501
    NODE9 = "status.system.NODE9"
    """str: B9. In an expanded system (TSP-Link), this is used to read or write to the system summary register."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.system.condition`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 1 through 14.

        Usage:
            - Accessing this property will send the ``print(status.system.condition)`` query.

        TSP Syntax:
            ```
            - print(status.system.condition)
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
        """Access the ``status.system.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 1 through 14.

        Usage:
            - Accessing this property will send the ``print(status.system.enable)`` query.
            - Setting this property to a value will send the ``status.system.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system.enable = value
            - print(status.system.enable)
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
        """Access the ``status.system.enable`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 1 through 14.

        Usage:
            - Accessing this property will send the ``print(status.system.enable)`` query.
            - Setting this property to a value will send the ``status.system.enable = value``
              command.

        TSP Syntax:
            ```
            - status.system.enable = value
            - print(status.system.enable)
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
        """Access the ``status.system.event`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 1 through 14.

        Usage:
            - Accessing this property will send the ``print(status.system.event)`` query.

        TSP Syntax:
            ```
            - print(status.system.event)
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
        """Access the ``status.system.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 1 through 14.

        Usage:
            - Accessing this property will send the ``print(status.system.ntr)`` query.
            - Setting this property to a value will send the ``status.system.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system.ntr = value
            - print(status.system.ntr)
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
        """Access the ``status.system.ntr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 1 through 14.

        Usage:
            - Accessing this property will send the ``print(status.system.ntr)`` query.
            - Setting this property to a value will send the ``status.system.ntr = value`` command.

        TSP Syntax:
            ```
            - status.system.ntr = value
            - print(status.system.ntr)
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
        """Access the ``status.system.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 1 through 14.

        Usage:
            - Accessing this property will send the ``print(status.system.ptr)`` query.
            - Setting this property to a value will send the ``status.system.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system.ptr = value
            - print(status.system.ptr)
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
        """Access the ``status.system.ptr`` attribute.

        Description:
            - These attributes manage the TSP-Link&reg; system summary register of the status model
              for nodes 1 through 14.

        Usage:
            - Accessing this property will send the ``print(status.system.ptr)`` query.
            - Setting this property to a value will send the ``status.system.ptr = value`` command.

        TSP Syntax:
            ```
            - status.system.ptr = value
            - print(status.system.ptr)
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


class StatusStandard(BaseTSPCmd):
    r"""The ``status.standard`` command tree.

    Constants:
        - ``.CME``: B5. Set bit indicates that a command error has occurred. Command errors include.
        - ``.COMMAND_ERROR``: B5. Set bit indicates that a command error has occurred. Command
          errors include.
        - ``.DDE``: B3. Set bit indicates that an instrument operation did not execute properly due
          to some internal condition.
        - ``.DEVICE_DEPENDENT_ERROR``: B3. Set bit indicates that an instrument operation did not
          execute properly due to some internal condition.
        - ``.EXE``: B4. Set bit indicates that the instrument detected an error while trying to
          execute a command.
        - ``.EXECUTION_ERROR``: B4. Set bit indicates that the instrument detected an error while
          trying to execute a command.
        - ``.OPC``: B0. Set bit indicates that all pending selected instrument operations are
          completed and the instrument is ready to accept new commands. The bit is set in response
          to an \*OPC command. The opc() function can be used in place of the \*OPC command.
        - ``.OPERATION_COMPLETE``: B0. Set bit indicates that all pending selected instrument
          operations are completed and the instrument is ready to accept new commands. The bit is
          set in response to an \*OPC command. The opc() function can be used in place of the \*OPC
          command.
        - ``.PON``: B7. Set bit indicates that the instrument has been turned off and turned back on
          since the last time this register has been read.
        - ``.POWER_ON``: B7. Set bit indicates that the instrument has been turned off and turned
          back on since the last time this register has been read.
        - ``.QUERY_ERROR``: B2. Set bit indicates that you attempted to read data from an empty
          Output Queue.
        - ``.QYE``: B2. Set bit indicates that you attempted to read data from an empty Output
          Queue.
        - ``.URQ``: B6. Set bit indicates that the LOCAL key on the instrument front panel was
          pressed.
        - ``.USER_REQUEST``: B6. Set bit indicates that the LOCAL key on the instrument front panel
          was pressed.

    Properties and methods:
        - ``.condition``: The ``status.standard.condition`` attribute.
        - ``.enable``: The ``status.standard.enable`` attribute.
        - ``.event``: The ``status.standard.event`` attribute.
        - ``.ntr``: The ``status.standard.ntr`` attribute.
        - ``.ptr``: The ``status.standard.ptr`` attribute.
    """

    CME = "status.standard.CME"
    """str: B5. Set bit indicates that a command error has occurred. Command errors include."""
    COMMAND_ERROR = "status.standard.COMMAND_ERROR"
    """str: B5. Set bit indicates that a command error has occurred. Command errors include."""
    DDE = "status.standard.DDE"
    """str: B3. Set bit indicates that an instrument operation did not execute properly due to some internal condition."""  # noqa: E501
    DEVICE_DEPENDENT_ERROR = "status.standard.DEVICE_DEPENDENT_ERROR"
    """str: B3. Set bit indicates that an instrument operation did not execute properly due to some internal condition."""  # noqa: E501
    EXE = "status.standard.EXE"
    """str: B4. Set bit indicates that the instrument detected an error while trying to execute a command."""  # noqa: E501
    EXECUTION_ERROR = "status.standard.EXECUTION_ERROR"
    """str: B4. Set bit indicates that the instrument detected an error while trying to execute a command."""  # noqa: E501
    OPC = "status.standard.OPC"
    r"""str: B0. Set bit indicates that all pending selected instrument operations are completed and the instrument is ready to accept new commands. The bit is set in response to an \*OPC command. The opc() function can be used in place of the \*OPC command."""  # noqa: E501
    OPERATION_COMPLETE = "status.standard.OPERATION_COMPLETE"
    r"""str: B0. Set bit indicates that all pending selected instrument operations are completed and the instrument is ready to accept new commands. The bit is set in response to an \*OPC command. The opc() function can be used in place of the \*OPC command."""  # noqa: E501
    PON = "status.standard.PON"
    """str: B7. Set bit indicates that the instrument has been turned off and turned back on since the last time this register has been read."""  # noqa: E501
    POWER_ON = "status.standard.POWER_ON"
    """str: B7. Set bit indicates that the instrument has been turned off and turned back on since the last time this register has been read."""  # noqa: E501
    QUERY_ERROR = "status.standard.QUERY_ERROR"
    """str: B2. Set bit indicates that you attempted to read data from an empty Output Queue."""
    QYE = "status.standard.QYE"
    """str: B2. Set bit indicates that you attempted to read data from an empty Output Queue."""
    URQ = "status.standard.URQ"
    """str: B6. Set bit indicates that the LOCAL key on the instrument front panel was pressed."""
    USER_REQUEST = "status.standard.USER_REQUEST"
    """str: B6. Set bit indicates that the LOCAL key on the instrument front panel was pressed."""

    @property
    def condition(self) -> str:
        """Access the ``status.standard.condition`` attribute.

        Description:
            - These attributes manage the standard event status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.standard.condition)`` query.

        TSP Syntax:
            ```
            - print(status.standard.condition)
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
        """Access the ``status.standard.enable`` attribute.

        Description:
            - These attributes manage the standard event status register set of the status model.

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
            - These attributes manage the standard event status register set of the status model.

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
            - These attributes manage the standard event status register set of the status model.

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

    @property
    def ntr(self) -> str:
        """Access the ``status.standard.ntr`` attribute.

        Description:
            - These attributes manage the standard event status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.standard.ntr)`` query.
            - Setting this property to a value will send the ``status.standard.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.standard.ntr = value
            - print(status.standard.ntr)
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
        """Access the ``status.standard.ntr`` attribute.

        Description:
            - These attributes manage the standard event status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.standard.ntr)`` query.
            - Setting this property to a value will send the ``status.standard.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.standard.ntr = value
            - print(status.standard.ntr)
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
        """Access the ``status.standard.ptr`` attribute.

        Description:
            - These attributes manage the standard event status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.standard.ptr)`` query.
            - Setting this property to a value will send the ``status.standard.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.standard.ptr = value
            - print(status.standard.ptr)
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
        """Access the ``status.standard.ptr`` attribute.

        Description:
            - These attributes manage the standard event status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.standard.ptr)`` query.
            - Setting this property to a value will send the ``status.standard.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.standard.ptr = value
            - print(status.standard.ptr)
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


class StatusQuestionableUnstableOutput(BaseTSPCmd):
    """The ``status.questionable.unstable_output`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates that an unstable output
          condition was detected on SMU A.
        - ``.SMUB``: B2. Set bit indicates that an unstable output condition was detected on SMU B.

    Properties and methods:
        - ``.condition``: The ``status.questionable.unstable_output.condition`` attribute.
        - ``.enable``: The ``status.questionable.unstable_output.enable`` attribute.
        - ``.event``: The ``status.questionable.unstable_output.event`` attribute.
        - ``.ntr``: The ``status.questionable.unstable_output.ntr`` attribute.
        - ``.ptr``: The ``status.questionable.unstable_output.ptr`` attribute.
    """

    SMUA = "status.questionable.unstable_output.SMUA"
    """str: B1. Set bit indicates that an unstable output
condition was detected on SMU A."""
    SMUB = "status.questionable.unstable_output.SMUB"
    """str: B2. Set bit indicates that an unstable output condition was detected on SMU B."""

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.unstable_output.condition`` attribute.

        Description:
            - This attribute contains the questionable status unstable output summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.unstable_output.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.unstable_output.condition)
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
        """Access the ``status.questionable.unstable_output.enable`` attribute.

        Description:
            - This attribute contains the questionable status unstable output summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.unstable_output.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.unstable_output.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.unstable_output.enable = value
            - print(status.questionable.unstable_output.enable)
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
        """Access the ``status.questionable.unstable_output.enable`` attribute.

        Description:
            - This attribute contains the questionable status unstable output summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.unstable_output.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.unstable_output.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.unstable_output.enable = value
            - print(status.questionable.unstable_output.enable)
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
        """Access the ``status.questionable.unstable_output.event`` attribute.

        Description:
            - This attribute contains the questionable status unstable output summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.unstable_output.event)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.unstable_output.event)
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
        """Access the ``status.questionable.unstable_output.ntr`` attribute.

        Description:
            - This attribute contains the questionable status unstable output summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.unstable_output.ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.unstable_output.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.unstable_output.ntr = value
            - print(status.questionable.unstable_output.ntr)
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
        """Access the ``status.questionable.unstable_output.ntr`` attribute.

        Description:
            - This attribute contains the questionable status unstable output summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.unstable_output.ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.unstable_output.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.unstable_output.ntr = value
            - print(status.questionable.unstable_output.ntr)
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
        """Access the ``status.questionable.unstable_output.ptr`` attribute.

        Description:
            - This attribute contains the questionable status unstable output summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.unstable_output.ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.unstable_output.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.unstable_output.ptr = value
            - print(status.questionable.unstable_output.ptr)
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
        """Access the ``status.questionable.unstable_output.ptr`` attribute.

        Description:
            - This attribute contains the questionable status unstable output summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.unstable_output.ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.unstable_output.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.unstable_output.ptr = value
            - print(status.questionable.unstable_output.ptr)
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


class StatusQuestionableOverTemperature(BaseTSPCmd):
    """The ``status.questionable.over_temperature`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates that an overtemperature condition was detected on SMU A.
        - ``.SMUB``: B2. Set bit indicates that an overtemperature condition was detected on SMU B.

    Properties and methods:
        - ``.condition``: The ``status.questionable.over_temperature.condition`` attribute.
        - ``.enable``: The ``status.questionable.over_temperature.enable`` attribute.
        - ``.event``: The ``status.questionable.over_temperature.event`` attribute.
        - ``.ntr``: The ``status.questionable.over_temperature.ntr`` attribute.
        - ``.ptr``: The ``status.questionable.over_temperature.ptr`` attribute.
    """

    SMUA = "status.questionable.over_temperature.SMUA"
    """str: B1. Set bit indicates that an overtemperature condition was detected on SMU A."""
    SMUB = "status.questionable.over_temperature.SMUB"
    """str: B2. Set bit indicates that an overtemperature condition was detected on SMU B."""

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.over_temperature.condition`` attribute.

        Description:
            - This attribute contains the questionable status over temperature summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.over_temperature.condition)
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
        """Access the ``status.questionable.over_temperature.enable`` attribute.

        Description:
            - This attribute contains the questionable status over temperature summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.enable = value
            - print(status.questionable.over_temperature.enable)
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
        """Access the ``status.questionable.over_temperature.enable`` attribute.

        Description:
            - This attribute contains the questionable status over temperature summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.enable = value
            - print(status.questionable.over_temperature.enable)
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
        """Access the ``status.questionable.over_temperature.event`` attribute.

        Description:
            - This attribute contains the questionable status over temperature summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.event)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.over_temperature.event)
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
        """Access the ``status.questionable.over_temperature.ntr`` attribute.

        Description:
            - This attribute contains the questionable status over temperature summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.ntr = value
            - print(status.questionable.over_temperature.ntr)
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
        """Access the ``status.questionable.over_temperature.ntr`` attribute.

        Description:
            - This attribute contains the questionable status over temperature summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.ntr = value
            - print(status.questionable.over_temperature.ntr)
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
        """Access the ``status.questionable.over_temperature.ptr`` attribute.

        Description:
            - This attribute contains the questionable status over temperature summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.ptr = value
            - print(status.questionable.over_temperature.ptr)
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
        """Access the ``status.questionable.over_temperature.ptr`` attribute.

        Description:
            - This attribute contains the questionable status over temperature summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.ptr = value
            - print(status.questionable.over_temperature.ptr)
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


class StatusQuestionableInstrumentSmuxItem(ValidatedChannel, BaseTSPCmd):
    """The ``status.questionable.instrument.smuX`` command tree.

    Constants:
        - ``.CAL``: B8. Set bit indicates that the calibration constants stored in nonvolatile
          memory were corrupted and could not be loaded when the instrument powered up.
        - ``.CALIBRATION``: B8. Set bit indicates that the calibration constants stored in
          nonvolatile memory were corrupted and could not be loaded when the instrument powered up.
        - ``.OTEMP``: B12. Set bit indicates that an overtemperature condition was detected.
        - ``.OVER_TEMPERATURE``: B12. Set bit indicates that an overtemperature condition was
          detected.
        - ``.UNSTABLE_OUTPUT``: B9. Set bit indicates that an
          unstable output condition
          was detected.
        - ``.UO``: B9. Set bit indicates that an
          unstable output condition
          was detected.

    Properties and methods:
        - ``.condition``: The ``status.questionable.instrument.smuX.condition`` attribute.
        - ``.enable``: The ``status.questionable.instrument.smuX.enable`` attribute.
        - ``.event``: The ``status.questionable.instrument.smuX.event`` attribute.
        - ``.ntr``: The ``status.questionable.instrument.smuX.ntr`` attribute.
        - ``.ptr``: The ``status.questionable.instrument.smuX.ptr`` attribute.
    """

    CAL = "status.questionable.instrument.smuX.CAL"
    """str: B8. Set bit indicates that the calibration constants stored in nonvolatile memory were corrupted and could not be loaded when the instrument powered up."""  # noqa: E501
    CALIBRATION = "status.questionable.instrument.smuX.CALIBRATION"
    """str: B8. Set bit indicates that the calibration constants stored in nonvolatile memory were corrupted and could not be loaded when the instrument powered up."""  # noqa: E501
    OTEMP = "status.questionable.instrument.smuX.OTEMP"
    """str: B12. Set bit indicates that an overtemperature condition was detected."""
    OVER_TEMPERATURE = "status.questionable.instrument.smuX.OVER_TEMPERATURE"
    """str: B12. Set bit indicates that an overtemperature condition was detected."""
    UNSTABLE_OUTPUT = "status.questionable.instrument.smuX.UNSTABLE_OUTPUT"
    """str: B9. Set bit indicates that an
unstable output condition
was detected."""
    UO = "status.questionable.instrument.smuX.UO"
    """str: B9. Set bit indicates that an
unstable output condition
was detected."""

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.CAL = self.CAL.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CALIBRATION = self.CALIBRATION.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OTEMP = self.OTEMP.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OVER_TEMPERATURE = self.OVER_TEMPERATURE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.UNSTABLE_OUTPUT = self.UNSTABLE_OUTPUT.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.UO = self.UO.replace("smuX", f"smu{self._cmd_syntax[3]}")

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.instrument.smuX.condition`` attribute.

        Description:
            - This attribute contains the questionable status SMU A summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.smuX.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.instrument.smuX.condition)
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
        """Access the ``status.questionable.instrument.smuX.enable`` attribute.

        Description:
            - This attribute contains the questionable status SMU A summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.smuX.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.smuX.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.smuX.enable = value
            - print(status.questionable.instrument.smuX.enable)
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
        """Access the ``status.questionable.instrument.smuX.enable`` attribute.

        Description:
            - This attribute contains the questionable status SMU A summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.smuX.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.smuX.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.smuX.enable = value
            - print(status.questionable.instrument.smuX.enable)
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
        """Access the ``status.questionable.instrument.smuX.event`` attribute.

        Description:
            - This attribute contains the questionable status SMU A summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.smuX.event)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.instrument.smuX.event)
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
        """Access the ``status.questionable.instrument.smuX.ntr`` attribute.

        Description:
            - This attribute contains the questionable status SMU A summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.smuX.ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.smuX.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.smuX.ntr = value
            - print(status.questionable.instrument.smuX.ntr)
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
        """Access the ``status.questionable.instrument.smuX.ntr`` attribute.

        Description:
            - This attribute contains the questionable status SMU A summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.smuX.ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.smuX.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.smuX.ntr = value
            - print(status.questionable.instrument.smuX.ntr)
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
        """Access the ``status.questionable.instrument.smuX.ptr`` attribute.

        Description:
            - This attribute contains the questionable status SMU A summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.smuX.ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.smuX.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.smuX.ptr = value
            - print(status.questionable.instrument.smuX.ptr)
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
        """Access the ``status.questionable.instrument.smuX.ptr`` attribute.

        Description:
            - This attribute contains the questionable status SMU A summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.smuX.ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.smuX.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.smuX.ptr = value
            - print(status.questionable.instrument.smuX.ptr)
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


class StatusQuestionableInstrument(BaseTSPCmd):
    """The ``status.questionable.instrument`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates one or more enabled bits for the SMU A questionable
          register are set.
        - ``.SMUB``: B2. Set bit indicates one or more enabled bits for the SMU B questionable
          register are set.

    Properties and methods:
        - ``.condition``: The ``status.questionable.instrument.condition`` attribute.
        - ``.enable``: The ``status.questionable.instrument.enable`` attribute.
        - ``.event``: The ``status.questionable.instrument.event`` attribute.
        - ``.ntr``: The ``status.questionable.instrument.ntr`` attribute.
        - ``.ptr``: The ``status.questionable.instrument.ptr`` attribute.
        - ``.smu``: The ``status.questionable.instrument.smuX`` command tree.
    """

    SMUA = "status.questionable.instrument.SMUA"
    """str: B1. Set bit indicates one or more enabled bits for the SMU A questionable register are set."""  # noqa: E501
    SMUB = "status.questionable.instrument.SMUB"
    """str: B2. Set bit indicates one or more enabled bits for the SMU B questionable register are set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._smu: Dict[str, StatusQuestionableInstrumentSmuxItem] = DefaultDictPassKeyToFactory(
            lambda x: StatusQuestionableInstrumentSmuxItem(device, f"{self._cmd_syntax}.smu{x}")
        )

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.instrument.condition`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.instrument.condition)
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
        """Access the ``status.questionable.instrument.enable`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.enable = value
            - print(status.questionable.instrument.enable)
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
        """Access the ``status.questionable.instrument.enable`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.enable = value
            - print(status.questionable.instrument.enable)
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
        """Access the ``status.questionable.instrument.event`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.event)``
              query.

        TSP Syntax:
            ```
            - print(status.questionable.instrument.event)
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
        """Access the ``status.questionable.instrument.ntr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.ntr = value
            - print(status.questionable.instrument.ntr)
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
        """Access the ``status.questionable.instrument.ntr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.ntr = value
            - print(status.questionable.instrument.ntr)
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
        """Access the ``status.questionable.instrument.ptr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.ptr = value
            - print(status.questionable.instrument.ptr)
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
        """Access the ``status.questionable.instrument.ptr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.ptr = value
            - print(status.questionable.instrument.ptr)
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
    def smu(self) -> Dict[str, StatusQuestionableInstrumentSmuxItem]:
        """Return the ``status.questionable.instrument.smuX`` command tree.

        Constants:
            - ``.CAL``: B8. Set bit indicates that the calibration constants stored in nonvolatile
              memory were corrupted and could not be loaded when the instrument powered up.
            - ``.CALIBRATION``: B8. Set bit indicates that the calibration constants stored in
              nonvolatile memory were corrupted and could not be loaded when the instrument powered
              up.
            - ``.OTEMP``: B12. Set bit indicates that an overtemperature condition was detected.
            - ``.OVER_TEMPERATURE``: B12. Set bit indicates that an overtemperature condition was
              detected.
            - ``.UNSTABLE_OUTPUT``: B9. Set bit indicates that an
              unstable output condition
              was detected.
            - ``.UO``: B9. Set bit indicates that an
              unstable output condition
              was detected.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.instrument.smuX.condition`` attribute.
            - ``.enable``: The ``status.questionable.instrument.smuX.enable`` attribute.
            - ``.event``: The ``status.questionable.instrument.smuX.event`` attribute.
            - ``.ntr``: The ``status.questionable.instrument.smuX.ntr`` attribute.
            - ``.ptr``: The ``status.questionable.instrument.smuX.ptr`` attribute.
        """
        return self._smu


class StatusQuestionableCalibration(BaseTSPCmd):
    """The ``status.questionable.calibration`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates that the SMU A calibration constants stored in
          nonvolatile memory were corrupted and could not be loaded when the instrument powered up.
        - ``.SMUB``: B2. Set bit indicates that the SMU B calibration constants stored in
          nonvolatile memory were corrupted and could not be loaded when the instrument powered up.

    Properties and methods:
        - ``.condition``: The ``status.questionable.calibration.condition`` attribute.
        - ``.enable``: The ``status.questionable.calibration.enable`` attribute.
        - ``.event``: The ``status.questionable.calibration.event`` attribute.
        - ``.ntr``: The ``status.questionable.calibration.ntr`` attribute.
        - ``.ptr``: The ``status.questionable.calibration.ptr`` attribute.
    """

    SMUA = "status.questionable.calibration.SMUA"
    """str: B1. Set bit indicates that the SMU A calibration constants stored in nonvolatile memory were corrupted and could not be loaded when the instrument powered up."""  # noqa: E501
    SMUB = "status.questionable.calibration.SMUB"
    """str: B2. Set bit indicates that the SMU B calibration constants stored in nonvolatile memory were corrupted and could not be loaded when the instrument powered up."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.calibration.condition`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.calibration.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.calibration.condition)
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
        """Access the ``status.questionable.calibration.enable`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.calibration.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.enable = value
            - print(status.questionable.calibration.enable)
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
        """Access the ``status.questionable.calibration.enable`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.calibration.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.enable = value
            - print(status.questionable.calibration.enable)
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
        """Access the ``status.questionable.calibration.event`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.event)``
              query.

        TSP Syntax:
            ```
            - print(status.questionable.calibration.event)
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
        """Access the ``status.questionable.calibration.ntr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.ntr = value
            - print(status.questionable.calibration.ntr)
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
        """Access the ``status.questionable.calibration.ntr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.ntr = value
            - print(status.questionable.calibration.ntr)
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
        """Access the ``status.questionable.calibration.ptr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.ptr = value
            - print(status.questionable.calibration.ptr)
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
        """Access the ``status.questionable.calibration.ptr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.ptr = value
            - print(status.questionable.calibration.ptr)
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


class StatusQuestionable(BaseTSPCmd):
    """The ``status.questionable`` command tree.

    Constants:
        - ``.CAL``: B8. An enabled bit in the questionable status calibration summary event register
          is set.
        - ``.CALIBRATION``: B8. An enabled bit in the questionable status calibration summary event
          register is set.
        - ``.INST``: B13. An enabled bit in the questionable status instrument summary event
          register is set.
        - ``.INSTRUMENT_SUMMARY``: B13. An enabled bit in the questionable status instrument summary
          event register is set.
        - ``.OTEMP``: B12. An enabled bit in the questionable status over temperature summary event
          register is set.
        - ``.OVER_TEMPERATURE``: B12. An enabled bit in the questionable status over temperature
          summary event register is set.
        - ``.UNSTABLE_OUTPUT``: B9. An enabled bit in the questionable status unstable output
          summary event register is set.
        - ``.UO``: B9. An enabled bit in the questionable status unstable output summary event
          register is set.

    Properties and methods:
        - ``.calibration``: The ``status.questionable.calibration`` command tree.
        - ``.condition``: The ``status.questionable.condition`` attribute.
        - ``.enable``: The ``status.questionable.enable`` attribute.
        - ``.event``: The ``status.questionable.event`` attribute.
        - ``.instrument``: The ``status.questionable.instrument`` command tree.
        - ``.ntr``: The ``status.questionable.ntr`` attribute.
        - ``.over_temperature``: The ``status.questionable.over_temperature`` command tree.
        - ``.ptr``: The ``status.questionable.ptr`` attribute.
        - ``.unstable_output``: The ``status.questionable.unstable_output`` command tree.
    """

    CAL = "status.questionable.CAL"
    """str: B8. An enabled bit in the questionable status calibration summary event register is set."""  # noqa: E501
    CALIBRATION = "status.questionable.CALIBRATION"
    """str: B8. An enabled bit in the questionable status calibration summary event register is set."""  # noqa: E501
    INST = "status.questionable.INST"
    """str: B13. An enabled bit in the questionable status instrument summary event register is set."""  # noqa: E501
    INSTRUMENT_SUMMARY = "status.questionable.INSTRUMENT_SUMMARY"
    """str: B13. An enabled bit in the questionable status instrument summary event register is set."""  # noqa: E501
    OTEMP = "status.questionable.OTEMP"
    """str: B12. An enabled bit in the questionable status over temperature summary event register is set."""  # noqa: E501
    OVER_TEMPERATURE = "status.questionable.OVER_TEMPERATURE"
    """str: B12. An enabled bit in the questionable status over temperature summary event register is set."""  # noqa: E501
    UNSTABLE_OUTPUT = "status.questionable.UNSTABLE_OUTPUT"
    """str: B9. An enabled bit in the questionable status unstable output summary event register is set."""  # noqa: E501
    UO = "status.questionable.UO"
    """str: B9. An enabled bit in the questionable status unstable output summary event register is set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calibration = StatusQuestionableCalibration(device, f"{self._cmd_syntax}.calibration")
        self._instrument = StatusQuestionableInstrument(device, f"{self._cmd_syntax}.instrument")
        self._over_temperature = StatusQuestionableOverTemperature(
            device, f"{self._cmd_syntax}.over_temperature"
        )
        self._unstable_output = StatusQuestionableUnstableOutput(
            device, f"{self._cmd_syntax}.unstable_output"
        )

    @property
    def calibration(self) -> StatusQuestionableCalibration:
        """Return the ``status.questionable.calibration`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates that the SMU A calibration constants stored in
              nonvolatile memory were corrupted and could not be loaded when the instrument powered
              up.
            - ``.SMUB``: B2. Set bit indicates that the SMU B calibration constants stored in
              nonvolatile memory were corrupted and could not be loaded when the instrument powered
              up.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.calibration.condition`` attribute.
            - ``.enable``: The ``status.questionable.calibration.enable`` attribute.
            - ``.event``: The ``status.questionable.calibration.event`` attribute.
            - ``.ntr``: The ``status.questionable.calibration.ntr`` attribute.
            - ``.ptr``: The ``status.questionable.calibration.ptr`` attribute.
        """
        return self._calibration

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.condition`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

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
            - These attributes manage the questionable status register set of the status model.

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
            - These attributes manage the questionable status register set of the status model.

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
            - These attributes manage the questionable status register set of the status model.

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

    @property
    def instrument(self) -> StatusQuestionableInstrument:
        """Return the ``status.questionable.instrument`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates one or more enabled bits for the SMU A questionable
              register are set.
            - ``.SMUB``: B2. Set bit indicates one or more enabled bits for the SMU B questionable
              register are set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.instrument.condition`` attribute.
            - ``.enable``: The ``status.questionable.instrument.enable`` attribute.
            - ``.event``: The ``status.questionable.instrument.event`` attribute.
            - ``.ntr``: The ``status.questionable.instrument.ntr`` attribute.
            - ``.ptr``: The ``status.questionable.instrument.ptr`` attribute.
            - ``.smu``: The ``status.questionable.instrument.smuX`` command tree.
        """
        return self._instrument

    @property
    def ntr(self) -> str:
        """Access the ``status.questionable.ntr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.ntr)`` query.
            - Setting this property to a value will send the ``status.questionable.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.ntr = value
            - print(status.questionable.ntr)
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
        """Access the ``status.questionable.ntr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.ntr)`` query.
            - Setting this property to a value will send the ``status.questionable.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.ntr = value
            - print(status.questionable.ntr)
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
    def over_temperature(self) -> StatusQuestionableOverTemperature:
        """Return the ``status.questionable.over_temperature`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates that an overtemperature condition was detected on SMU
              A.
            - ``.SMUB``: B2. Set bit indicates that an overtemperature condition was detected on SMU
              B.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.over_temperature.condition`` attribute.
            - ``.enable``: The ``status.questionable.over_temperature.enable`` attribute.
            - ``.event``: The ``status.questionable.over_temperature.event`` attribute.
            - ``.ntr``: The ``status.questionable.over_temperature.ntr`` attribute.
            - ``.ptr``: The ``status.questionable.over_temperature.ptr`` attribute.
        """
        return self._over_temperature

    @property
    def ptr(self) -> str:
        """Access the ``status.questionable.ptr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.ptr)`` query.
            - Setting this property to a value will send the ``status.questionable.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.ptr = value
            - print(status.questionable.ptr)
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
        """Access the ``status.questionable.ptr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.ptr)`` query.
            - Setting this property to a value will send the ``status.questionable.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.ptr = value
            - print(status.questionable.ptr)
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
    def unstable_output(self) -> StatusQuestionableUnstableOutput:
        """Return the ``status.questionable.unstable_output`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates that an unstable output
              condition was detected on SMU A.
            - ``.SMUB``: B2. Set bit indicates that an unstable output condition was detected on SMU
              B.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.unstable_output.condition`` attribute.
            - ``.enable``: The ``status.questionable.unstable_output.enable`` attribute.
            - ``.event``: The ``status.questionable.unstable_output.event`` attribute.
            - ``.ntr``: The ``status.questionable.unstable_output.ntr`` attribute.
            - ``.ptr``: The ``status.questionable.unstable_output.ptr`` attribute.
        """
        return self._unstable_output


class StatusOperationUser(BaseTSPCmd):
    """The ``status.operation.user`` command tree.

    Constants:
        - ``.BIT0``: B0. Read or write bit 0 of the operation status user register.
        - ``.BIT1``: B1. Read or write bit 1 of the operation status user register.
        - ``.BIT10``: B10. Read or write bit 10 of the operation status user register.
        - ``.BIT11``: B11. Read or write bit 11 of the operation status user register.
        - ``.BIT12``: B12. Read or write bit 12 of the operation status user register.
        - ``.BIT13``: B13. Read or write bit 13 of the operation status user register.
        - ``.BIT14``: B14. Read or write bit 14 of the operation status user register.
        - ``.BIT2``: B2. Read or write bit 2 of the operation status user register.
        - ``.BIT3``: B3. Read or write bit 3 of the operation status user register.
        - ``.BIT4``: B4. Read or write bit 4 of the operation status user register.
        - ``.BIT5``: B5. Read or write bit 5 of the operation status user register.
        - ``.BIT6``: B6. Read or write bit 6 of the operation status user register.
        - ``.BIT7``: B7. Read or write bit 7 of the operation status user register.
        - ``.BIT8``: B8. Read or write bit 8 of the operation status user register.
        - ``.BIT9``: B9. Read or write bit 9 of the operation status user register.

    Properties and methods:
        - ``.condition``: The ``status.operation.user.condition`` attribute.
        - ``.enable``: The ``status.operation.user.enable`` attribute.
        - ``.event``: The ``status.operation.user.event`` attribute.
        - ``.ntr``: The ``status.operation.user.ntr`` attribute.
        - ``.ptr``: The ``status.operation.user.ptr`` attribute.
    """

    BIT0 = "status.operation.user.BIT0"
    """str: B0. Read or write bit 0 of the operation status user register."""
    BIT1 = "status.operation.user.BIT1"
    """str: B1. Read or write bit 1 of the operation status user register."""
    BIT10 = "status.operation.user.BIT10"
    """str: B10. Read or write bit 10 of the operation status user register."""
    BIT11 = "status.operation.user.BIT11"
    """str: B11. Read or write bit 11 of the operation status user register."""
    BIT12 = "status.operation.user.BIT12"
    """str: B12. Read or write bit 12 of the operation status user register."""
    BIT13 = "status.operation.user.BIT13"
    """str: B13. Read or write bit 13 of the operation status user register."""
    BIT14 = "status.operation.user.BIT14"
    """str: B14. Read or write bit 14 of the operation status user register."""
    BIT2 = "status.operation.user.BIT2"
    """str: B2. Read or write bit 2 of the operation status user register."""
    BIT3 = "status.operation.user.BIT3"
    """str: B3. Read or write bit 3 of the operation status user register."""
    BIT4 = "status.operation.user.BIT4"
    """str: B4. Read or write bit 4 of the operation status user register."""
    BIT5 = "status.operation.user.BIT5"
    """str: B5. Read or write bit 5 of the operation status user register."""
    BIT6 = "status.operation.user.BIT6"
    """str: B6. Read or write bit 6 of the operation status user register."""
    BIT7 = "status.operation.user.BIT7"
    """str: B7. Read or write bit 7 of the operation status user register."""
    BIT8 = "status.operation.user.BIT8"
    """str: B8. Read or write bit 8 of the operation status user register."""
    BIT9 = "status.operation.user.BIT9"
    """str: B9. Read or write bit 9 of the operation status user register."""

    @property
    def condition(self) -> str:
        """Access the ``status.operation.user.condition`` attribute.

        Description:
            - These attributes manage the operation status user register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.user.condition)``
              query.
            - Setting this property to a value will send the
              ``status.operation.user.condition = value`` command.

        TSP Syntax:
            ```
            - status.operation.user.condition = value
            - print(status.operation.user.condition)
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

    @condition.setter
    def condition(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.user.condition`` attribute.

        Description:
            - These attributes manage the operation status user register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.user.condition)``
              query.
            - Setting this property to a value will send the
              ``status.operation.user.condition = value`` command.

        TSP Syntax:
            ```
            - status.operation.user.condition = value
            - print(status.operation.user.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".condition", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.condition = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.operation.user.enable`` attribute.

        Description:
            - These attributes manage the operation status user register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.user.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.user.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.user.enable = value
            - print(status.operation.user.enable)
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
        """Access the ``status.operation.user.enable`` attribute.

        Description:
            - These attributes manage the operation status user register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.user.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.user.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.user.enable = value
            - print(status.operation.user.enable)
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
        """Access the ``status.operation.user.event`` attribute.

        Description:
            - These attributes manage the operation status user register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.user.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.user.event)
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
        """Access the ``status.operation.user.ntr`` attribute.

        Description:
            - These attributes manage the operation status user register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.user.ntr)`` query.
            - Setting this property to a value will send the ``status.operation.user.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.user.ntr = value
            - print(status.operation.user.ntr)
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
        """Access the ``status.operation.user.ntr`` attribute.

        Description:
            - These attributes manage the operation status user register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.user.ntr)`` query.
            - Setting this property to a value will send the ``status.operation.user.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.user.ntr = value
            - print(status.operation.user.ntr)
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
        """Access the ``status.operation.user.ptr`` attribute.

        Description:
            - These attributes manage the operation status user register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.user.ptr)`` query.
            - Setting this property to a value will send the ``status.operation.user.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.user.ptr = value
            - print(status.operation.user.ptr)
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
        """Access the ``status.operation.user.ptr`` attribute.

        Description:
            - These attributes manage the operation status user register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.user.ptr)`` query.
            - Setting this property to a value will send the ``status.operation.user.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.user.ptr = value
            - print(status.operation.user.ptr)
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


class StatusOperationTriggerOverrun(BaseTSPCmd):
    """The ``status.operation.trigger_overrun`` command tree.

    Constants:
        - ``.DIGIO``: B12. Set bit indicates one of the enabled bits in the operation status digital
          I/O overrun event register is set.
        - ``.DIGITAL_IO``: B12. Set bit indicates one of the enabled bits in the operation status
          digital I/O overrun event register is set.
        - ``.LAN``: B14. Set bit indicates one of the enabled bits in the operation status LAN
          trigger overrun event register is set.
        - ``.SMUA``: B1. Set bit indicates one of the enabled bits in the operation status SMU A
          trigger overrun event register is set.
        - ``.SMUB``: B2. Set bit indicates one of the enabled bits in the operation status SMU B
          trigger overrun event register is set.
        - ``.TRGBLND``: B10. Set bit indicates one of the enabled bits in the operation status
          trigger blender overrun event register is set.
        - ``.TRGTMR``: B11. Set bit indicates one of the enabled bits in the operation status
          trigger timer overrun event register is set.
        - ``.TRIGGER_BLENDER``: B10. Set bit indicates one of the enabled bits in the operation
          status trigger blender overrun event register is set.
        - ``.TRIGGER_TIMER``: B11. Set bit indicates one of the enabled bits in the operation status
          trigger timer overrun event register is set.
        - ``.TSPLINK``: B13. Set bit indicates one of the enabled bits in the operation status
          TSP-Link overrun event register is set.

    Properties and methods:
        - ``.condition``: The ``status.operation.trigger_overrun.condition`` attribute.
        - ``.enable``: The ``status.operation.trigger_overrun.enable`` attribute.
        - ``.event``: The ``status.operation.trigger_overrun.event`` attribute.
        - ``.ntr``: The ``status.operation.trigger_overrun.ntr`` attribute.
        - ``.ptr``: The ``status.operation.trigger_overrun.ptr`` attribute.
    """

    DIGIO = "status.operation.trigger_overrun.DIGIO"
    """str: B12. Set bit indicates one of the enabled bits in the operation status digital I/O overrun event register is set."""  # noqa: E501
    DIGITAL_IO = "status.operation.trigger_overrun.DIGITAL_IO"
    """str: B12. Set bit indicates one of the enabled bits in the operation status digital I/O overrun event register is set."""  # noqa: E501
    LAN = "status.operation.trigger_overrun.LAN"
    """str: B14. Set bit indicates one of the enabled bits in the operation status LAN trigger overrun event register is set."""  # noqa: E501
    SMUA = "status.operation.trigger_overrun.SMUA"
    """str: B1. Set bit indicates one of the enabled bits in the operation status SMU A trigger overrun event register is set."""  # noqa: E501
    SMUB = "status.operation.trigger_overrun.SMUB"
    """str: B2. Set bit indicates one of the enabled bits in the operation status SMU B trigger overrun event register is set."""  # noqa: E501
    TRGBLND = "status.operation.trigger_overrun.TRGBLND"
    """str: B10. Set bit indicates one of the enabled bits in the operation status trigger blender overrun event register is set."""  # noqa: E501
    TRGTMR = "status.operation.trigger_overrun.TRGTMR"
    """str: B11. Set bit indicates one of the enabled bits in the operation status trigger timer overrun event register is set."""  # noqa: E501
    TRIGGER_BLENDER = "status.operation.trigger_overrun.TRIGGER_BLENDER"
    """str: B10. Set bit indicates one of the enabled bits in the operation status trigger blender overrun event register is set."""  # noqa: E501
    TRIGGER_TIMER = "status.operation.trigger_overrun.TRIGGER_TIMER"
    """str: B11. Set bit indicates one of the enabled bits in the operation status trigger timer overrun event register is set."""  # noqa: E501
    TSPLINK = "status.operation.trigger_overrun.TSPLINK"
    """str: B13. Set bit indicates one of the enabled bits in the operation status TSP-Link overrun event register is set."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.operation.trigger_overrun.condition`` attribute.

        Description:
            - This attribute contains the operation status trigger overrun summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.trigger_overrun.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.trigger_overrun.condition)
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
        """Access the ``status.operation.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger overrun summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.trigger_overrun.enable = value
            - print(status.operation.trigger_overrun.enable)
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
        """Access the ``status.operation.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger overrun summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.trigger_overrun.enable = value
            - print(status.operation.trigger_overrun.enable)
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
        """Access the ``status.operation.trigger_overrun.event`` attribute.

        Description:
            - This attribute contains the operation status trigger overrun summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.trigger_overrun.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.trigger_overrun.event)
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
        """Access the ``status.operation.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger overrun summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.trigger_overrun.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.trigger_overrun.ntr = value
            - print(status.operation.trigger_overrun.ntr)
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
        """Access the ``status.operation.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger overrun summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.trigger_overrun.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.trigger_overrun.ntr = value
            - print(status.operation.trigger_overrun.ntr)
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
        """Access the ``status.operation.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger overrun summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.trigger_overrun.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.trigger_overrun.ptr = value
            - print(status.operation.trigger_overrun.ptr)
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
        """Access the ``status.operation.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger overrun summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.trigger_overrun.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.trigger_overrun.ptr = value
            - print(status.operation.trigger_overrun.ptr)
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


class StatusOperationSweeping(BaseTSPCmd):
    """The ``status.operation.sweeping`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates that SMU A is sweeping.
        - ``.SMUB``: B2. Set bit indicates SMU B is sweeping.

    Properties and methods:
        - ``.condition``: The ``status.operation.sweeping.condition`` attribute.
        - ``.enable``: The ``status.operation.sweeping.enable`` attribute.
        - ``.event``: The ``status.operation.sweeping.event`` attribute.
        - ``.ntr``: The ``status.operation.sweeping.ntr`` attribute.
        - ``.ptr``: The ``status.operation.sweeping.ptr`` attribute.
    """

    SMUA = "status.operation.sweeping.SMUA"
    """str: B1. Set bit indicates that SMU A is sweeping."""
    SMUB = "status.operation.sweeping.SMUB"
    """str: B2. Set bit indicates SMU B is sweeping."""

    @property
    def condition(self) -> str:
        """Access the ``status.operation.sweeping.condition`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.condition)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.sweeping.condition)
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
        """Access the ``status.operation.sweeping.enable`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.enable = value
            - print(status.operation.sweeping.enable)
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
        """Access the ``status.operation.sweeping.enable`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.enable = value
            - print(status.operation.sweeping.enable)
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
        """Access the ``status.operation.sweeping.event`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.sweeping.event)
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
        """Access the ``status.operation.sweeping.ntr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.ntr = value
            - print(status.operation.sweeping.ntr)
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
        """Access the ``status.operation.sweeping.ntr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.ntr = value
            - print(status.operation.sweeping.ntr)
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
        """Access the ``status.operation.sweeping.ptr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.ptr = value
            - print(status.operation.sweeping.ptr)
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
        """Access the ``status.operation.sweeping.ptr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.ptr = value
            - print(status.operation.sweeping.ptr)
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


class StatusOperationRemote(BaseTSPCmd):
    """The ``status.operation.remote`` command tree.

    Constants:
        - ``.CAV``: B1. Set bit indicates there is a command available in the execution queue.
        - ``.COMMAND_AVAILABLE``: B1. Set bit indicates there is a command available in the
          execution queue.
        - ``.PRMPT``: B11. Set bit indicates command prompts are enabled.
        - ``.PROMPTS_ENABLED``: B11. Set bit indicates command prompts are enabled.

    Properties and methods:
        - ``.condition``: The ``status.operation.remote.condition`` attribute.
        - ``.enable``: The ``status.operation.remote.enable`` attribute.
        - ``.event``: The ``status.operation.remote.event`` attribute.
        - ``.ntr``: The ``status.operation.remote.ntr`` attribute.
        - ``.ptr``: The ``status.operation.remote.ptr`` attribute.
    """

    CAV = "status.operation.remote.CAV"
    """str: B1. Set bit indicates there is a command available in the execution queue."""
    COMMAND_AVAILABLE = "status.operation.remote.COMMAND_AVAILABLE"
    """str: B1. Set bit indicates there is a command available in the execution queue."""
    PRMPT = "status.operation.remote.PRMPT"
    """str: B11. Set bit indicates command prompts are enabled."""
    PROMPTS_ENABLED = "status.operation.remote.PROMPTS_ENABLED"
    """str: B11. Set bit indicates command prompts are enabled."""

    @property
    def condition(self) -> str:
        """Access the ``status.operation.remote.condition`` attribute.

        Description:
            - This attribute contains the operation status remote summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.remote.condition)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.remote.condition)
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
        """Access the ``status.operation.remote.enable`` attribute.

        Description:
            - This attribute contains the operation status remote summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.remote.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.remote.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.remote.enable = value
            - print(status.operation.remote.enable)
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
        """Access the ``status.operation.remote.enable`` attribute.

        Description:
            - This attribute contains the operation status remote summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.remote.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.remote.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.remote.enable = value
            - print(status.operation.remote.enable)
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
        """Access the ``status.operation.remote.event`` attribute.

        Description:
            - This attribute contains the operation status remote summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.remote.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.remote.event)
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
        """Access the ``status.operation.remote.ntr`` attribute.

        Description:
            - This attribute contains the operation status remote summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.remote.ntr)`` query.
            - Setting this property to a value will send the ``status.operation.remote.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.remote.ntr = value
            - print(status.operation.remote.ntr)
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
        """Access the ``status.operation.remote.ntr`` attribute.

        Description:
            - This attribute contains the operation status remote summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.remote.ntr)`` query.
            - Setting this property to a value will send the ``status.operation.remote.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.remote.ntr = value
            - print(status.operation.remote.ntr)
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
        """Access the ``status.operation.remote.ptr`` attribute.

        Description:
            - This attribute contains the operation status remote summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.remote.ptr)`` query.
            - Setting this property to a value will send the ``status.operation.remote.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.remote.ptr = value
            - print(status.operation.remote.ptr)
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
        """Access the ``status.operation.remote.ptr`` attribute.

        Description:
            - This attribute contains the operation status remote summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.remote.ptr)`` query.
            - Setting this property to a value will send the ``status.operation.remote.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.remote.ptr = value
            - print(status.operation.remote.ptr)
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


class StatusOperationMeasuring(BaseTSPCmd):
    """The ``status.operation.measuring`` command tree.

    Constants:
        - ``.SMUA``: B1. Bit is set when SMU A is making an overlapped measurement, but it is not
          set when making a normal synchronous measurement.
        - ``.SMUB``: B2. This bit is set when SMU B is making an overlapped measurement, but it is
          not set when making a normal synchronous measurement.

    Properties and methods:
        - ``.condition``: The ``status.operation.measuring.condition`` attribute.
        - ``.enable``: The ``status.operation.measuring.enable`` attribute.
        - ``.event``: The ``status.operation.measuring.event`` attribute.
        - ``.ntr``: The ``status.operation.measuring.ntr`` attribute.
        - ``.ptr``: The ``status.operation.measuring.ptr`` attribute.
    """

    SMUA = "status.operation.measuring.SMUA"
    """str: B1. Bit is set when SMU A is making an overlapped measurement, but it is not set when making a normal synchronous measurement."""  # noqa: E501
    SMUB = "status.operation.measuring.SMUB"
    """str: B2. This bit is set when SMU B is making an overlapped measurement, but it is not set when making a normal synchronous measurement."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.operation.measuring.condition`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.condition)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.measuring.condition)
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
        """Access the ``status.operation.measuring.enable`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.measuring.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.enable = value
            - print(status.operation.measuring.enable)
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
        """Access the ``status.operation.measuring.enable`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.measuring.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.enable = value
            - print(status.operation.measuring.enable)
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
        """Access the ``status.operation.measuring.event`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.measuring.event)
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
        """Access the ``status.operation.measuring.ntr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.measuring.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.ntr = value
            - print(status.operation.measuring.ntr)
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
        """Access the ``status.operation.measuring.ntr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.measuring.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.ntr = value
            - print(status.operation.measuring.ntr)
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
        """Access the ``status.operation.measuring.ptr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.measuring.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.ptr = value
            - print(status.operation.measuring.ptr)
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
        """Access the ``status.operation.measuring.ptr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.measuring.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.ptr = value
            - print(status.operation.measuring.ptr)
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


class StatusOperationInstrumentTsplinkTriggerOverrun(BaseTSPCmd):
    """The ``status.operation.instrument.tsplink.trigger_overrun`` command tree.

    Constants:
        - ``.LINE1``: B1. A set bit indicates that line 1 generated an action overrun when triggered
          to generate an output trigger.
        - ``.LINE2``: B2. A set bit indicates that line 2 generated an action overrun when triggered
          to generate an output trigger.
        - ``.LINE3``: B3. A set bit indicates that line 3 generated an action overrun when triggered
          to generate an output trigger.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.tsplink.trigger_overrun.condition``
          attribute.
        - ``.enable``: The ``status.operation.instrument.tsplink.trigger_overrun.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.tsplink.trigger_overrun.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.tsplink.trigger_overrun.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.tsplink.trigger_overrun.ptr`` attribute.
    """

    LINE1 = "status.operation.instrument.tsplink.trigger_overrun.LINE1"
    """str: B1. A set bit indicates that line 1 generated an action overrun when triggered to generate an output trigger."""  # noqa: E501
    LINE2 = "status.operation.instrument.tsplink.trigger_overrun.LINE2"
    """str: B2. A set bit indicates that line 2 generated an action overrun when triggered to generate an output trigger."""  # noqa: E501
    LINE3 = "status.operation.instrument.tsplink.trigger_overrun.LINE3"
    """str: B3. A set bit indicates that line 3 generated an action overrun when triggered to generate an output trigger."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.tsplink.trigger_overrun.condition`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.trigger_overrun.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.tsplink.trigger_overrun.condition)
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
        """Access the ``status.operation.instrument.tsplink.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.trigger_overrun.enable = value
            - print(status.operation.instrument.tsplink.trigger_overrun.enable)
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
        """Access the ``status.operation.instrument.tsplink.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.trigger_overrun.enable = value
            - print(status.operation.instrument.tsplink.trigger_overrun.enable)
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
        """Access the ``status.operation.instrument.tsplink.trigger_overrun.event`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.trigger_overrun.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.tsplink.trigger_overrun.event)
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
        """Access the ``status.operation.instrument.tsplink.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.trigger_overrun.ntr = value
            - print(status.operation.instrument.tsplink.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.tsplink.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.trigger_overrun.ntr = value
            - print(status.operation.instrument.tsplink.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.tsplink.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.trigger_overrun.ptr = value
            - print(status.operation.instrument.tsplink.trigger_overrun.ptr)
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
        """Access the ``status.operation.instrument.tsplink.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.trigger_overrun.ptr = value
            - print(status.operation.instrument.tsplink.trigger_overrun.ptr)
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


class StatusOperationInstrumentTsplink(BaseTSPCmd):
    """The ``status.operation.instrument.tsplink`` command tree.

    Constants:
        - ``.TRGOVR``: B10. Set bit indicates one or more enabled bits for the operation status
          TSP-Link overrun register is set.
        - ``.TRIGGER_OVERRUN``: B10. Set bit indicates one or more enabled bits for the operation
          status TSP-Link overrun register is set.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.tsplink.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.tsplink.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.tsplink.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.tsplink.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.tsplink.ptr`` attribute.
        - ``.trigger_overrun``: The ``status.operation.instrument.tsplink.trigger_overrun`` command
          tree.
    """

    TRGOVR = "status.operation.instrument.tsplink.TRGOVR"
    """str: B10. Set bit indicates one or more enabled bits for the operation status TSP-Link overrun register is set."""  # noqa: E501
    TRIGGER_OVERRUN = "status.operation.instrument.tsplink.TRIGGER_OVERRUN"
    """str: B10. Set bit indicates one or more enabled bits for the operation status TSP-Link overrun register is set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._trigger_overrun = StatusOperationInstrumentTsplinkTriggerOverrun(
            device, f"{self._cmd_syntax}.trigger_overrun"
        )

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.tsplink.condition`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.tsplink.condition)
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
        """Access the ``status.operation.instrument.tsplink.enable`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.enable = value
            - print(status.operation.instrument.tsplink.enable)
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
        """Access the ``status.operation.instrument.tsplink.enable`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.enable = value
            - print(status.operation.instrument.tsplink.enable)
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
        """Access the ``status.operation.instrument.tsplink.event`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.tsplink.event)
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
        """Access the ``status.operation.instrument.tsplink.ntr`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.ntr = value
            - print(status.operation.instrument.tsplink.ntr)
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
        """Access the ``status.operation.instrument.tsplink.ntr`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.ntr = value
            - print(status.operation.instrument.tsplink.ntr)
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
        """Access the ``status.operation.instrument.tsplink.ptr`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.ptr = value
            - print(status.operation.instrument.tsplink.ptr)
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
        """Access the ``status.operation.instrument.tsplink.ptr`` attribute.

        Description:
            - This attribute contains the operation status TSP-Link summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.tsplink.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.tsplink.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.tsplink.ptr = value
            - print(status.operation.instrument.tsplink.ptr)
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
    def trigger_overrun(self) -> StatusOperationInstrumentTsplinkTriggerOverrun:
        """Return the ``status.operation.instrument.tsplink.trigger_overrun`` command tree.

        Constants:
            - ``.LINE1``: B1. A set bit indicates that line 1 generated an action overrun when
              triggered to generate an output trigger.
            - ``.LINE2``: B2. A set bit indicates that line 2 generated an action overrun when
              triggered to generate an output trigger.
            - ``.LINE3``: B3. A set bit indicates that line 3 generated an action overrun when
              triggered to generate an output trigger.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.tsplink.trigger_overrun.condition``
              attribute.
            - ``.enable``: The ``status.operation.instrument.tsplink.trigger_overrun.enable``
              attribute.
            - ``.event``: The ``status.operation.instrument.tsplink.trigger_overrun.event``
              attribute.
            - ``.ntr``: The ``status.operation.instrument.tsplink.trigger_overrun.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.tsplink.trigger_overrun.ptr`` attribute.
        """
        return self._trigger_overrun


class StatusOperationInstrumentTriggerTimerTriggerOverrun(BaseTSPCmd):
    """The ``status.operation.instrument.trigger_timer.trigger_overrun`` command tree.

    Constants:
        - ``.TMR1``: B1. A set bit indicates that timer 1 generated an action overrun because it was
          still processing a delay from a previous trigger when a new trigger was received.
        - ``.TMR2``: B2. A set bit indicates that timer 2 generated an action overrun because it was
          still processing a delay from a previous trigger when a new trigger was received.
        - ``.TMR3``: B3. A set bit indicates that timer 3 generated an action overrun because it was
          still processing a delay from a previous trigger when a new trigger was received.
        - ``.TMR4``: B4. A set bit indicates that timer 4 generated an action overrun because it was
          still processing a delay from a previous trigger when a new trigger was received.
        - ``.TMR5``: B5. A set bit indicates that timer 5 generated an action overrun because it was
          still processing a delay from a previous trigger when a new trigger was received.
        - ``.TMR6``: B6. A set bit indicates that timer 6 generated an action overrun because it was
          still processing a delay from a previous trigger when a new trigger was received.
        - ``.TMR7``: B7. A set bit indicates that timer 7 generated an action overrun because it was
          still processing a delay from a previous trigger when a new trigger was received.
        - ``.TMR8``: B8. A set bit indicates that timer 8 generated an action overrun because it was
          still processing a delay from a previous trigger when a new trigger was received.

    Properties and methods:
        - ``.condition``: The
          ``status.operation.instrument.trigger_timer.trigger_overrun.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.trigger_timer.trigger_overrun.enable``
          attribute.
        - ``.event``: The ``status.operation.instrument.trigger_timer.trigger_overrun.event``
          attribute.
        - ``.ntr``: The ``status.operation.instrument.trigger_timer.trigger_overrun.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.trigger_timer.trigger_overrun.ptr`` attribute.
    """

    TMR1 = "status.operation.instrument.trigger_timer.trigger_overrun.TMR1"
    """str: B1. A set bit indicates that timer 1 generated an action overrun because it was still processing a delay from a previous trigger when a new trigger was received."""  # noqa: E501
    TMR2 = "status.operation.instrument.trigger_timer.trigger_overrun.TMR2"
    """str: B2. A set bit indicates that timer 2 generated an action overrun because it was still processing a delay from a previous trigger when a new trigger was received."""  # noqa: E501
    TMR3 = "status.operation.instrument.trigger_timer.trigger_overrun.TMR3"
    """str: B3. A set bit indicates that timer 3 generated an action overrun because it was still processing a delay from a previous trigger when a new trigger was received."""  # noqa: E501
    TMR4 = "status.operation.instrument.trigger_timer.trigger_overrun.TMR4"
    """str: B4. A set bit indicates that timer 4 generated an action overrun because it was still processing a delay from a previous trigger when a new trigger was received."""  # noqa: E501
    TMR5 = "status.operation.instrument.trigger_timer.trigger_overrun.TMR5"
    """str: B5. A set bit indicates that timer 5 generated an action overrun because it was still processing a delay from a previous trigger when a new trigger was received."""  # noqa: E501
    TMR6 = "status.operation.instrument.trigger_timer.trigger_overrun.TMR6"
    """str: B6. A set bit indicates that timer 6 generated an action overrun because it was still processing a delay from a previous trigger when a new trigger was received."""  # noqa: E501
    TMR7 = "status.operation.instrument.trigger_timer.trigger_overrun.TMR7"
    """str: B7. A set bit indicates that timer 7 generated an action overrun because it was still processing a delay from a previous trigger when a new trigger was received."""  # noqa: E501
    TMR8 = "status.operation.instrument.trigger_timer.trigger_overrun.TMR8"
    """str: B8. A set bit indicates that timer 8 generated an action overrun because it was still processing a delay from a previous trigger when a new trigger was received."""  # noqa: E501

    @property
    def condition(self) -> str:
        """``status.operation.instrument.trigger_timer.trigger_overrun.condition`` attribute.

        Description:
            - This attribute contains the operation status trigger timer overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.trigger_overrun.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.trigger_timer.trigger_overrun.condition)
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
        """``status.operation.instrument.trigger_timer.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger timer overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.trigger_overrun.enable = value
            - print(status.operation.instrument.trigger_timer.trigger_overrun.enable)
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
        """``status.operation.instrument.trigger_timer.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger timer overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.trigger_overrun.enable = value
            - print(status.operation.instrument.trigger_timer.trigger_overrun.enable)
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
        """Access the ``status.operation.instrument.trigger_timer.trigger_overrun.event`` attribute.

        Description:
            - This attribute contains the operation status trigger timer overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.trigger_overrun.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.trigger_timer.trigger_overrun.event)
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
        """Access the ``status.operation.instrument.trigger_timer.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger timer overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.trigger_overrun.ntr = value
            - print(status.operation.instrument.trigger_timer.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.trigger_timer.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger timer overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.trigger_overrun.ntr = value
            - print(status.operation.instrument.trigger_timer.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.trigger_timer.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger timer overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.trigger_overrun.ptr = value
            - print(status.operation.instrument.trigger_timer.trigger_overrun.ptr)
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
        """Access the ``status.operation.instrument.trigger_timer.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger timer overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.trigger_overrun.ptr = value
            - print(status.operation.instrument.trigger_timer.trigger_overrun.ptr)
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


class StatusOperationInstrumentTriggerTimer(BaseTSPCmd):
    """The ``status.operation.instrument.trigger_timer`` command tree.

    Constants:
        - ``.TRGOVR``: B10. Set bit indicates one or more enabled bits for the operation status
          trigger timer overrun register is set.
        - ``.TRIGGER_OVERRUN``: B10. Set bit indicates one or more enabled bits for the operation
          status trigger timer overrun register is set.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.trigger_timer.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.trigger_timer.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.trigger_timer.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.trigger_timer.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.trigger_timer.ptr`` attribute.
        - ``.trigger_overrun``: The ``status.operation.instrument.trigger_timer.trigger_overrun``
          command tree.
    """

    TRGOVR = "status.operation.instrument.trigger_timer.TRGOVR"
    """str: B10. Set bit indicates one or more enabled bits for the operation status trigger timer overrun register is set."""  # noqa: E501
    TRIGGER_OVERRUN = "status.operation.instrument.trigger_timer.TRIGGER_OVERRUN"
    """str: B10. Set bit indicates one or more enabled bits for the operation status trigger timer overrun register is set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._trigger_overrun = StatusOperationInstrumentTriggerTimerTriggerOverrun(
            device, f"{self._cmd_syntax}.trigger_overrun"
        )

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.trigger_timer.condition`` attribute.

        Description:
            - This attribute contains the operation status trigger timer summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.trigger_timer.condition)
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
        """Access the ``status.operation.instrument.trigger_timer.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger timer summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.enable = value
            - print(status.operation.instrument.trigger_timer.enable)
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
        """Access the ``status.operation.instrument.trigger_timer.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger timer summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.enable = value
            - print(status.operation.instrument.trigger_timer.enable)
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
        """Access the ``status.operation.instrument.trigger_timer.event`` attribute.

        Description:
            - This attribute contains the operation status trigger timer summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.trigger_timer.event)
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
        """Access the ``status.operation.instrument.trigger_timer.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger timer summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.ntr = value
            - print(status.operation.instrument.trigger_timer.ntr)
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
        """Access the ``status.operation.instrument.trigger_timer.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger timer summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.ntr = value
            - print(status.operation.instrument.trigger_timer.ntr)
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
        """Access the ``status.operation.instrument.trigger_timer.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger timer summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.ptr = value
            - print(status.operation.instrument.trigger_timer.ptr)
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
        """Access the ``status.operation.instrument.trigger_timer.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger timer summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_timer.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_timer.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_timer.ptr = value
            - print(status.operation.instrument.trigger_timer.ptr)
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
    def trigger_overrun(self) -> StatusOperationInstrumentTriggerTimerTriggerOverrun:
        """Return the ``status.operation.instrument.trigger_timer.trigger_overrun`` command tree.

        Constants:
            - ``.TMR1``: B1. A set bit indicates that timer 1 generated an action overrun because it
              was still processing a delay from a previous trigger when a new trigger was received.
            - ``.TMR2``: B2. A set bit indicates that timer 2 generated an action overrun because it
              was still processing a delay from a previous trigger when a new trigger was received.
            - ``.TMR3``: B3. A set bit indicates that timer 3 generated an action overrun because it
              was still processing a delay from a previous trigger when a new trigger was received.
            - ``.TMR4``: B4. A set bit indicates that timer 4 generated an action overrun because it
              was still processing a delay from a previous trigger when a new trigger was received.
            - ``.TMR5``: B5. A set bit indicates that timer 5 generated an action overrun because it
              was still processing a delay from a previous trigger when a new trigger was received.
            - ``.TMR6``: B6. A set bit indicates that timer 6 generated an action overrun because it
              was still processing a delay from a previous trigger when a new trigger was received.
            - ``.TMR7``: B7. A set bit indicates that timer 7 generated an action overrun because it
              was still processing a delay from a previous trigger when a new trigger was received.
            - ``.TMR8``: B8. A set bit indicates that timer 8 generated an action overrun because it
              was still processing a delay from a previous trigger when a new trigger was received.

        Sub-properties and sub-methods:
            - ``.condition``: The
              ``status.operation.instrument.trigger_timer.trigger_overrun.condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.trigger_timer.trigger_overrun.enable``
              attribute.
            - ``.event``: The ``status.operation.instrument.trigger_timer.trigger_overrun.event``
              attribute.
            - ``.ntr``: The ``status.operation.instrument.trigger_timer.trigger_overrun.ntr``
              attribute.
            - ``.ptr``: The ``status.operation.instrument.trigger_timer.trigger_overrun.ptr``
              attribute.
        """
        return self._trigger_overrun


class StatusOperationInstrumentTriggerBlenderTriggerOverrun(BaseTSPCmd):
    """The ``status.operation.instrument.trigger_blender.trigger_overrun`` command tree.

    Constants:
        - ``.BLND1``: B1. A set bit value indicates that trigger blender 1 generated an action
          overrun.
        - ``.BLND2``: B2. A set bit value indicates that trigger blender 2 generated an action
          overrun.
        - ``.BLND3``: B3. A set bit value indicates that trigger blender 3 generated an action
          overrun.
        - ``.BLND4``: B4. A set bit value indicates that trigger blender 4 generated an action
          overrun.
        - ``.BLND5``: B5. A set bit value indicates that trigger blender 5 generated an action
          overrun.
        - ``.BLND6``: B6. A set bit value indicates that trigger blender 6 generated an action
          overrun.

    Properties and methods:
        - ``.condition``: The
          ``status.operation.instrument.trigger_blender.trigger_overrun.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.trigger_blender.trigger_overrun.enable``
          attribute.
        - ``.event``: The ``status.operation.instrument.trigger_blender.trigger_overrun.event``
          attribute.
        - ``.ntr``: The ``status.operation.instrument.trigger_blender.trigger_overrun.ntr``
          attribute.
        - ``.ptr``: The ``status.operation.instrument.trigger_blender.trigger_overrun.ptr``
          attribute.
    """

    BLND1 = "status.operation.instrument.trigger_blender.trigger_overrun.BLND1"
    """str: B1. A set bit value indicates that trigger blender 1 generated an action overrun."""
    BLND2 = "status.operation.instrument.trigger_blender.trigger_overrun.BLND2"
    """str: B2. A set bit value indicates that trigger blender 2 generated an action overrun."""
    BLND3 = "status.operation.instrument.trigger_blender.trigger_overrun.BLND3"
    """str: B3. A set bit value indicates that trigger blender 3 generated an action overrun."""
    BLND4 = "status.operation.instrument.trigger_blender.trigger_overrun.BLND4"
    """str: B4. A set bit value indicates that trigger blender 4 generated an action overrun."""
    BLND5 = "status.operation.instrument.trigger_blender.trigger_overrun.BLND5"
    """str: B5. A set bit value indicates that trigger blender 5 generated an action overrun."""
    BLND6 = "status.operation.instrument.trigger_blender.trigger_overrun.BLND6"
    """str: B6. A set bit value indicates that trigger blender 6 generated an action overrun."""

    @property
    def condition(self) -> str:
        """``status.operation.instrument.trigger_blender.trigger_overrun.condition`` attribute.

        Description:
            - This attribute contains the operation status trigger blender overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.trigger_overrun.condition)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.trigger_blender.trigger_overrun.condition)
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
        """``status.operation.instrument.trigger_blender.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger blender overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.trigger_overrun.enable = value``
              command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.trigger_overrun.enable = value
            - print(status.operation.instrument.trigger_blender.trigger_overrun.enable)
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
        """``status.operation.instrument.trigger_blender.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger blender overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.trigger_overrun.enable = value``
              command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.trigger_overrun.enable = value
            - print(status.operation.instrument.trigger_blender.trigger_overrun.enable)
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
        """``status.operation.instrument.trigger_blender.trigger_overrun.event`` attribute.

        Description:
            - This attribute contains the operation status trigger blender overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.trigger_overrun.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.trigger_blender.trigger_overrun.event)
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
        """Access the ``status.operation.instrument.trigger_blender.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger blender overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.trigger_overrun.ntr = value
            - print(status.operation.instrument.trigger_blender.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.trigger_blender.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger blender overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.trigger_overrun.ntr = value
            - print(status.operation.instrument.trigger_blender.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.trigger_blender.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger blender overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.trigger_overrun.ptr = value
            - print(status.operation.instrument.trigger_blender.trigger_overrun.ptr)
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
        """Access the ``status.operation.instrument.trigger_blender.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger blender overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.trigger_overrun.ptr = value
            - print(status.operation.instrument.trigger_blender.trigger_overrun.ptr)
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


class StatusOperationInstrumentTriggerBlender(BaseTSPCmd):
    """The ``status.operation.instrument.trigger_blender`` command tree.

    Constants:
        - ``.TRGOVR``: B10. Set bit indicates one or more enabled bits for operation status trigger
          blender overrun register is set.
        - ``.TRIGGER_OVERRUN``: B10. Set bit indicates one or more enabled bits for operation status
          trigger blender overrun register is set.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.trigger_blender.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.trigger_blender.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.trigger_blender.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.trigger_blender.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.trigger_blender.ptr`` attribute.
        - ``.trigger_overrun``: The ``status.operation.instrument.trigger_blender.trigger_overrun``
          command tree.
    """

    TRGOVR = "status.operation.instrument.trigger_blender.TRGOVR"
    """str: B10. Set bit indicates one or more enabled bits for operation status trigger blender overrun register is set."""  # noqa: E501
    TRIGGER_OVERRUN = "status.operation.instrument.trigger_blender.TRIGGER_OVERRUN"
    """str: B10. Set bit indicates one or more enabled bits for operation status trigger blender overrun register is set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._trigger_overrun = StatusOperationInstrumentTriggerBlenderTriggerOverrun(
            device, f"{self._cmd_syntax}.trigger_overrun"
        )

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.trigger_blender.condition`` attribute.

        Description:
            - This attribute contains the operation status trigger blender summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.trigger_blender.condition)
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
        """Access the ``status.operation.instrument.trigger_blender.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger blender summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.enable = value
            - print(status.operation.instrument.trigger_blender.enable)
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
        """Access the ``status.operation.instrument.trigger_blender.enable`` attribute.

        Description:
            - This attribute contains the operation status trigger blender summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.enable = value
            - print(status.operation.instrument.trigger_blender.enable)
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
        """Access the ``status.operation.instrument.trigger_blender.event`` attribute.

        Description:
            - This attribute contains the operation status trigger blender summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.trigger_blender.event)
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
        """Access the ``status.operation.instrument.trigger_blender.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger blender summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.ntr = value
            - print(status.operation.instrument.trigger_blender.ntr)
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
        """Access the ``status.operation.instrument.trigger_blender.ntr`` attribute.

        Description:
            - This attribute contains the operation status trigger blender summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.ntr = value
            - print(status.operation.instrument.trigger_blender.ntr)
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
        """Access the ``status.operation.instrument.trigger_blender.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger blender summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.ptr = value
            - print(status.operation.instrument.trigger_blender.ptr)
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
        """Access the ``status.operation.instrument.trigger_blender.ptr`` attribute.

        Description:
            - This attribute contains the operation status trigger blender summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.trigger_blender.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.trigger_blender.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.trigger_blender.ptr = value
            - print(status.operation.instrument.trigger_blender.ptr)
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
    def trigger_overrun(self) -> StatusOperationInstrumentTriggerBlenderTriggerOverrun:
        """Return the ``status.operation.instrument.trigger_blender.trigger_overrun`` command tree.

        Constants:
            - ``.BLND1``: B1. A set bit value indicates that trigger blender 1 generated an action
              overrun.
            - ``.BLND2``: B2. A set bit value indicates that trigger blender 2 generated an action
              overrun.
            - ``.BLND3``: B3. A set bit value indicates that trigger blender 3 generated an action
              overrun.
            - ``.BLND4``: B4. A set bit value indicates that trigger blender 4 generated an action
              overrun.
            - ``.BLND5``: B5. A set bit value indicates that trigger blender 5 generated an action
              overrun.
            - ``.BLND6``: B6. A set bit value indicates that trigger blender 6 generated an action
              overrun.

        Sub-properties and sub-methods:
            - ``.condition``: The
              ``status.operation.instrument.trigger_blender.trigger_overrun.condition`` attribute.
            - ``.enable``: The
              ``status.operation.instrument.trigger_blender.trigger_overrun.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.trigger_blender.trigger_overrun.event``
              attribute.
            - ``.ntr``: The ``status.operation.instrument.trigger_blender.trigger_overrun.ntr``
              attribute.
            - ``.ptr``: The ``status.operation.instrument.trigger_blender.trigger_overrun.ptr``
              attribute.
        """
        return self._trigger_overrun


# pylint: disable=too-few-public-methods
class StatusOperationInstrumentSmuxItemTriggerOverrun(BaseTSPCmd):
    """The ``status.operation.instrument.smuX.trigger_overrun`` command tree.

    Constants:
        - ``.ARM``: B1. Set bit indicates that the arm event detector of the SMU was already in the
          detected state when a trigger was received.
        - ``.ENDP``: B4. Set bit indicates that the end pulse event detector of the SMU was already
          in the detected state when a trigger was received.
        - ``.MEAS``: B3. Set bit indicates that the measurement event detector of the SMU was
          already in the detected state when a trigger was received.
        - ``.SRC``: B2. Set bit indicates that the source event detector of the SMU was already in
          the detected state when a trigger was received.
    """

    ARM = "status.operation.instrument.smuX.trigger_overrun.ARM"
    """str: B1. Set bit indicates that the arm event detector of the SMU was already in the detected state when a trigger was received."""  # noqa: E501
    ENDP = "status.operation.instrument.smuX.trigger_overrun.ENDP"
    """str: B4. Set bit indicates that the end pulse event detector of the SMU was already in the detected state when a trigger was received."""  # noqa: E501
    MEAS = "status.operation.instrument.smuX.trigger_overrun.MEAS"
    """str: B3. Set bit indicates that the measurement event detector of the SMU was already in the detected state when a trigger was received."""  # noqa: E501
    SRC = "status.operation.instrument.smuX.trigger_overrun.SRC"
    """str: B2. Set bit indicates that the source event detector of the SMU was already in the detected state when a trigger was received."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.ARM = self.ARM.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.ENDP = self.ENDP.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.MEAS = self.MEAS.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SRC = self.SRC.replace("smuX", f"smu{self._cmd_syntax[3]}")


class StatusOperationInstrumentSmuxItemTriggerOverrrun(BaseTSPCmd):
    """The ``status.operation.instrument.smuX.trigger_overrrun`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.smuX.trigger_overrrun.condition``
          attribute.
        - ``.enable``: The ``status.operation.instrument.smuX.trigger_overrrun.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.smuX.trigger_overrrun.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.smuX.trigger_overrrun.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.smuX.trigger_overrrun.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.smuX.trigger_overrrun.condition`` attribute.

        Description:
            - This attribute contains the operation status SMU X trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.trigger_overrrun.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.smuX.trigger_overrrun.condition)
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
        """Access the ``status.operation.instrument.smuX.trigger_overrrun.enable`` attribute.

        Description:
            - This attribute contains the operation status SMU X trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.trigger_overrrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.trigger_overrrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.trigger_overrrun.enable = value
            - print(status.operation.instrument.smuX.trigger_overrrun.enable)
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
        """Access the ``status.operation.instrument.smuX.trigger_overrrun.enable`` attribute.

        Description:
            - This attribute contains the operation status SMU X trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.trigger_overrrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.trigger_overrrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.trigger_overrrun.enable = value
            - print(status.operation.instrument.smuX.trigger_overrrun.enable)
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
        """Access the ``status.operation.instrument.smuX.trigger_overrrun.event`` attribute.

        Description:
            - This attribute contains the operation status SMU X trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.trigger_overrrun.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.smuX.trigger_overrrun.event)
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
        """Access the ``status.operation.instrument.smuX.trigger_overrrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status SMU X trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.trigger_overrrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.trigger_overrrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.trigger_overrrun.ntr = value
            - print(status.operation.instrument.smuX.trigger_overrrun.ntr)
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
        """Access the ``status.operation.instrument.smuX.trigger_overrrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status SMU X trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.trigger_overrrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.trigger_overrrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.trigger_overrrun.ntr = value
            - print(status.operation.instrument.smuX.trigger_overrrun.ntr)
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
        """Access the ``status.operation.instrument.smuX.trigger_overrrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status SMU X trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.trigger_overrrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.trigger_overrrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.trigger_overrrun.ptr = value
            - print(status.operation.instrument.smuX.trigger_overrrun.ptr)
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
        """Access the ``status.operation.instrument.smuX.trigger_overrrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status SMU X trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.trigger_overrrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.trigger_overrrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.trigger_overrrun.ptr = value
            - print(status.operation.instrument.smuX.trigger_overrrun.ptr)
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


#  pylint: disable=too-many-instance-attributes
class StatusOperationInstrumentSmuxItem(ValidatedChannel, BaseTSPCmd):
    """The ``status.operation.instrument.smuX`` command tree.

    Constants:
        - ``.CAL``: Set bit B0 indicates that smuX is unlocked for calibration.
        - ``.CALIBRATING``: Set bit B0 indicates that smuX is unlocked for calibration.
        - ``.MEAS``: Bit B4 is set when making an overlapped measurement, but it is not set when
          making a normal synchronous measurement.
        - ``.MEASURING``: Bit B4 is set when making an overlapped measurement, but it is not set
          when making a normal synchronous measurement.
        - ``.SWE``: Set bit B3 indicates that smuX is sweeping.
        - ``.SWEEPING``: Set bit B3 indicates that smuX is sweeping.
        - ``.TRGOVR``: Set bit B10 indicates an enabled bit has been set in the operation status
          smuX trigger overrun event register.
        - ``.TRIGGER_OVERRUN``: Set bit B10 indicates an enabled bit has been set in the operation
          status smuX trigger overrun event register.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.smuX.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.smuX.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.smuX.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.smuX.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.smuX.ptr`` attribute.
        - ``.trigger_overrrun``: The ``status.operation.instrument.smuX.trigger_overrrun`` command
          tree.
        - ``.trigger_overrun``: The ``status.operation.instrument.smuX.trigger_overrun`` command
          tree.
    """

    CAL = "status.operation.instrument.smuX.CAL"
    """str: Set bit B0 indicates that smuX is unlocked for calibration."""
    CALIBRATING = "status.operation.instrument.smuX.CALIBRATING"
    """str: Set bit B0 indicates that smuX is unlocked for calibration."""
    MEAS = "status.operation.instrument.smuX.MEAS"
    """str: Bit B4 is set when making an overlapped measurement, but it is not set when making a normal synchronous measurement."""  # noqa: E501
    MEASURING = "status.operation.instrument.smuX.MEASURING"
    """str: Bit B4 is set when making an overlapped measurement, but it is not set when making a normal synchronous measurement."""  # noqa: E501
    SWE = "status.operation.instrument.smuX.SWE"
    """str: Set bit B3 indicates that smuX is sweeping."""
    SWEEPING = "status.operation.instrument.smuX.SWEEPING"
    """str: Set bit B3 indicates that smuX is sweeping."""
    TRGOVR = "status.operation.instrument.smuX.TRGOVR"
    """str: Set bit B10 indicates an enabled bit has been set in the operation status smuX trigger overrun event register."""  # noqa: E501
    TRIGGER_OVERRUN = "status.operation.instrument.smuX.TRIGGER_OVERRUN"
    """str: Set bit B10 indicates an enabled bit has been set in the operation status smuX trigger overrun event register."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.CAL = self.CAL.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CALIBRATING = self.CALIBRATING.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.MEAS = self.MEAS.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.MEASURING = self.MEASURING.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SWE = self.SWE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SWEEPING = self.SWEEPING.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.TRGOVR = self.TRGOVR.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.TRIGGER_OVERRUN = self.TRIGGER_OVERRUN.replace("smuX", f"smu{self._cmd_syntax[3]}")
        self._trigger_overrrun = StatusOperationInstrumentSmuxItemTriggerOverrrun(
            device, f"{self._cmd_syntax}.trigger_overrrun"
        )
        self._trigger_overrun = StatusOperationInstrumentSmuxItemTriggerOverrun(
            device, f"{self._cmd_syntax}.trigger_overrun"
        )

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.smuX.condition`` attribute.

        Description:
            - This attribute contains the operation status SMU X summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.smuX.condition)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example
              status.operation.instrument.smua.enable applies to SMU channel A).

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
        """Access the ``status.operation.instrument.smuX.enable`` attribute.

        Description:
            - This attribute contains the operation status SMU X summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.enable = value
            - print(status.operation.instrument.smuX.enable)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example
              status.operation.instrument.smua.enable applies to SMU channel A).

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
        """Access the ``status.operation.instrument.smuX.enable`` attribute.

        Description:
            - This attribute contains the operation status SMU X summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.enable = value
            - print(status.operation.instrument.smuX.enable)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example
              status.operation.instrument.smua.enable applies to SMU channel A).

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
        """Access the ``status.operation.instrument.smuX.event`` attribute.

        Description:
            - This attribute contains the operation status SMU X summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.smuX.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.smuX.event)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example
              status.operation.instrument.smua.enable applies to SMU channel A).

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
        """Access the ``status.operation.instrument.smuX.ntr`` attribute.

        Description:
            - This attribute contains the operation status SMU X summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.smuX.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.ntr = value
            - print(status.operation.instrument.smuX.ntr)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example
              status.operation.instrument.smua.enable applies to SMU channel A).

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
        """Access the ``status.operation.instrument.smuX.ntr`` attribute.

        Description:
            - This attribute contains the operation status SMU X summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.smuX.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.ntr = value
            - print(status.operation.instrument.smuX.ntr)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example
              status.operation.instrument.smua.enable applies to SMU channel A).

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
        """Access the ``status.operation.instrument.smuX.ptr`` attribute.

        Description:
            - This attribute contains the operation status SMU X summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.smuX.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.ptr = value
            - print(status.operation.instrument.smuX.ptr)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example
              status.operation.instrument.smua.enable applies to SMU channel A).

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
        """Access the ``status.operation.instrument.smuX.ptr`` attribute.

        Description:
            - This attribute contains the operation status SMU X summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.smuX.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.smuX.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.smuX.ptr = value
            - print(status.operation.instrument.smuX.ptr)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example
              status.operation.instrument.smua.enable applies to SMU channel A).

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
    def trigger_overrrun(self) -> StatusOperationInstrumentSmuxItemTriggerOverrrun:
        """Return the ``status.operation.instrument.smuX.trigger_overrrun`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.smuX.trigger_overrrun.condition``
              attribute.
            - ``.enable``: The ``status.operation.instrument.smuX.trigger_overrrun.enable``
              attribute.
            - ``.event``: The ``status.operation.instrument.smuX.trigger_overrrun.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.smuX.trigger_overrrun.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.smuX.trigger_overrrun.ptr`` attribute.
        """
        return self._trigger_overrrun

    @property
    def trigger_overrun(self) -> StatusOperationInstrumentSmuxItemTriggerOverrun:
        """Return the ``status.operation.instrument.smuX.trigger_overrun`` command tree.

        Constants:
            - ``.ARM``: B1. Set bit indicates that the arm event detector of the SMU was already in
              the detected state when a trigger was received.
            - ``.ENDP``: B4. Set bit indicates that the end pulse event detector of the SMU was
              already in the detected state when a trigger was received.
            - ``.MEAS``: B3. Set bit indicates that the measurement event detector of the SMU was
              already in the detected state when a trigger was received.
            - ``.SRC``: B2. Set bit indicates that the source event detector of the SMU was already
              in the detected state when a trigger was received.
        """
        return self._trigger_overrun


class StatusOperationInstrumentLanTriggerOverrun(BaseTSPCmd):
    """The ``status.operation.instrument.lan.trigger_overrun`` command tree.

    Constants:
        - ``.LAN1``: B1. A set bit indicates that LAN trigger 1 generated an action overrun when
          triggered to generate a trigger packet.
        - ``.LAN2``: B2. A set bit indicates that LAN trigger 2 generated an action overrun when
          triggered to generate a trigger packet.
        - ``.LAN3``: B3. A set bit indicates that LAN trigger 3 generated an action overrun when
          triggered to generate a trigger packet.
        - ``.LAN4``: B4. A set bit indicates that LAN trigger 4 generated an action overrun when
          triggered to generate a trigger packet.
        - ``.LAN5``: B5. A set bit indicates that LAN trigger 5 generated an action overrun when
          triggered to generate a trigger packet.
        - ``.LAN6``: B6. A set bit indicates that LAN trigger 6 generated an action overrun when
          triggered to generate a trigger packet.
        - ``.LAN7``: B7. A set bit indicates that LAN trigger 7 generated an action overrun when
          triggered to generate a trigger packet.
        - ``.LAN8``: B8. A set bit indicates that LAN trigger 8 generated an action overrun when
          triggered to generate a trigger packet.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.lan.trigger_overrun.condition``
          attribute.
        - ``.enable``: The ``status.operation.instrument.lan.trigger_overrun.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.lan.trigger_overrun.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.lan.trigger_overrun.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.lan.trigger_overrun.ptr`` attribute.
    """

    LAN1 = "status.operation.instrument.lan.trigger_overrun.LAN1"
    """str: B1. A set bit indicates that LAN trigger 1 generated an action overrun when triggered to generate a trigger packet."""  # noqa: E501
    LAN2 = "status.operation.instrument.lan.trigger_overrun.LAN2"
    """str: B2. A set bit indicates that LAN trigger 2 generated an action overrun when triggered to generate a trigger packet."""  # noqa: E501
    LAN3 = "status.operation.instrument.lan.trigger_overrun.LAN3"
    """str: B3. A set bit indicates that LAN trigger 3 generated an action overrun when triggered to generate a trigger packet."""  # noqa: E501
    LAN4 = "status.operation.instrument.lan.trigger_overrun.LAN4"
    """str: B4. A set bit indicates that LAN trigger 4 generated an action overrun when triggered to generate a trigger packet."""  # noqa: E501
    LAN5 = "status.operation.instrument.lan.trigger_overrun.LAN5"
    """str: B5. A set bit indicates that LAN trigger 5 generated an action overrun when triggered to generate a trigger packet."""  # noqa: E501
    LAN6 = "status.operation.instrument.lan.trigger_overrun.LAN6"
    """str: B6. A set bit indicates that LAN trigger 6 generated an action overrun when triggered to generate a trigger packet."""  # noqa: E501
    LAN7 = "status.operation.instrument.lan.trigger_overrun.LAN7"
    """str: B7. A set bit indicates that LAN trigger 7 generated an action overrun when triggered to generate a trigger packet."""  # noqa: E501
    LAN8 = "status.operation.instrument.lan.trigger_overrun.LAN8"
    """str: B8. A set bit indicates that LAN trigger 8 generated an action overrun when triggered to generate a trigger packet."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.lan.trigger_overrun.condition`` attribute.

        Description:
            - This attribute contains the operation status LAN trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.trigger_overrun.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.lan.trigger_overrun.condition)
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
        """Access the ``status.operation.instrument.lan.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status LAN trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.trigger_overrun.enable = value
            - print(status.operation.instrument.lan.trigger_overrun.enable)
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
        """Access the ``status.operation.instrument.lan.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status LAN trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.trigger_overrun.enable = value
            - print(status.operation.instrument.lan.trigger_overrun.enable)
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
        """Access the ``status.operation.instrument.lan.trigger_overrun.event`` attribute.

        Description:
            - This attribute contains the operation status LAN trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.trigger_overrun.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.lan.trigger_overrun.event)
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
        """Access the ``status.operation.instrument.lan.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status LAN trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.trigger_overrun.ntr = value
            - print(status.operation.instrument.lan.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.lan.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status LAN trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.trigger_overrun.ntr = value
            - print(status.operation.instrument.lan.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.lan.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status LAN trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.trigger_overrun.ptr = value
            - print(status.operation.instrument.lan.trigger_overrun.ptr)
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
        """Access the ``status.operation.instrument.lan.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status LAN trigger overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.trigger_overrun.ptr = value
            - print(status.operation.instrument.lan.trigger_overrun.ptr)
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


class StatusOperationInstrumentLan(BaseTSPCmd):
    """The ``status.operation.instrument.lan`` command tree.

    Constants:
        - ``.CON``: B0. Set bit indicates that the LAN cable is connected and a link has been
          detected.
        - ``.CONF``: B1. Set bit indicates the LAN is performing its configuration sequence.
        - ``.CONFIGURING``: B1. Set bit indicates the LAN is performing its configuration sequence.
        - ``.CONNECTION``: B0. Set bit indicates that the LAN cable is connected and a link has been
          detected.
        - ``.TRGOVR``: B10. Set bit indicates one or more enabled bits for the operation status LAN
          trigger overrun register is set.
        - ``.TRIGGER_OVERRUN``: B10. Set bit indicates one or more enabled bits for the operation
          status LAN trigger overrun register is set.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.lan.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.lan.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.lan.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.lan.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.lan.ptr`` attribute.
        - ``.trigger_overrun``: The ``status.operation.instrument.lan.trigger_overrun`` command
          tree.
    """

    CON = "status.operation.instrument.lan.CON"
    """str: B0. Set bit indicates that the LAN cable is connected and a link has been detected."""
    CONF = "status.operation.instrument.lan.CONF"
    """str: B1. Set bit indicates the LAN is performing its configuration sequence."""
    CONFIGURING = "status.operation.instrument.lan.CONFIGURING"
    """str: B1. Set bit indicates the LAN is performing its configuration sequence."""
    CONNECTION = "status.operation.instrument.lan.CONNECTION"
    """str: B0. Set bit indicates that the LAN cable is connected and a link has been detected."""
    TRGOVR = "status.operation.instrument.lan.TRGOVR"
    """str: B10. Set bit indicates one or more enabled bits for the operation status LAN trigger overrun register is set."""  # noqa: E501
    TRIGGER_OVERRUN = "status.operation.instrument.lan.TRIGGER_OVERRUN"
    """str: B10. Set bit indicates one or more enabled bits for the operation status LAN trigger overrun register is set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._trigger_overrun = StatusOperationInstrumentLanTriggerOverrun(
            device, f"{self._cmd_syntax}.trigger_overrun"
        )

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.lan.condition`` attribute.

        Description:
            - This attribute contains the operation status LAN summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.lan.condition)
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
        """Access the ``status.operation.instrument.lan.enable`` attribute.

        Description:
            - This attribute contains the operation status LAN summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.enable = value
            - print(status.operation.instrument.lan.enable)
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
        """Access the ``status.operation.instrument.lan.enable`` attribute.

        Description:
            - This attribute contains the operation status LAN summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.lan.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.enable = value
            - print(status.operation.instrument.lan.enable)
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
        """Access the ``status.operation.instrument.lan.event`` attribute.

        Description:
            - This attribute contains the operation status LAN summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.lan.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.lan.event)
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
        """Access the ``status.operation.instrument.lan.ntr`` attribute.

        Description:
            - This attribute contains the operation status LAN summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.lan.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.ntr = value
            - print(status.operation.instrument.lan.ntr)
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
        """Access the ``status.operation.instrument.lan.ntr`` attribute.

        Description:
            - This attribute contains the operation status LAN summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.lan.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.ntr = value
            - print(status.operation.instrument.lan.ntr)
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
        """Access the ``status.operation.instrument.lan.ptr`` attribute.

        Description:
            - This attribute contains the operation status LAN summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.lan.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.ptr = value
            - print(status.operation.instrument.lan.ptr)
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
        """Access the ``status.operation.instrument.lan.ptr`` attribute.

        Description:
            - This attribute contains the operation status LAN summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.lan.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.lan.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.lan.ptr = value
            - print(status.operation.instrument.lan.ptr)
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
    def trigger_overrun(self) -> StatusOperationInstrumentLanTriggerOverrun:
        """Return the ``status.operation.instrument.lan.trigger_overrun`` command tree.

        Constants:
            - ``.LAN1``: B1. A set bit indicates that LAN trigger 1 generated an action overrun when
              triggered to generate a trigger packet.
            - ``.LAN2``: B2. A set bit indicates that LAN trigger 2 generated an action overrun when
              triggered to generate a trigger packet.
            - ``.LAN3``: B3. A set bit indicates that LAN trigger 3 generated an action overrun when
              triggered to generate a trigger packet.
            - ``.LAN4``: B4. A set bit indicates that LAN trigger 4 generated an action overrun when
              triggered to generate a trigger packet.
            - ``.LAN5``: B5. A set bit indicates that LAN trigger 5 generated an action overrun when
              triggered to generate a trigger packet.
            - ``.LAN6``: B6. A set bit indicates that LAN trigger 6 generated an action overrun when
              triggered to generate a trigger packet.
            - ``.LAN7``: B7. A set bit indicates that LAN trigger 7 generated an action overrun when
              triggered to generate a trigger packet.
            - ``.LAN8``: B8. A set bit indicates that LAN trigger 8 generated an action overrun when
              triggered to generate a trigger packet.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.lan.trigger_overrun.condition``
              attribute.
            - ``.enable``: The ``status.operation.instrument.lan.trigger_overrun.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.lan.trigger_overrun.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.lan.trigger_overrun.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.lan.trigger_overrun.ptr`` attribute.
        """
        return self._trigger_overrun


class StatusOperationInstrumentDigioTriggerOverrun(BaseTSPCmd):
    """The ``status.operation.instrument.digio.trigger_overrun`` command tree.

    Constants:
        - ``.LINE1``: B1. A set bit indicates that digital I/O line 1 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE10``: B10. A set bit indicates that digital I/O line 10 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE11``: B11. A set bit indicates that digital I/O line 11 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE12``: B12. A set bit indicates that digital I/O line 12 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE13``: B13. A set bit indicates that digital I/O line 13 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE14``: B14. A set bit indicates that digital I/O line 14 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE2``: B2. A set bit indicates that digital I/O line 2 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE3``: B3. A set bit indicates that digital I/O line 3 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE4``: B4. A set bit indicates that digital I/O line 4 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE5``: B5. A set bit indicates that digital I/O line 5 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE6``: B6. A set bit indicates that digital I/O line 6 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE7``: B7. A set bit indicates that digital I/O line 7 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE8``: B8. A set bit indicates that digital I/O line 7 generated an action overrun
          when it was triggered to generate an output trigger.
        - ``.LINE9``: B9. A set bit indicates that digital I/O line 9 generated an action overrun
          when it was triggered to generate an output trigger.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.digio.trigger_overrun.condition``
          attribute.
        - ``.enable``: The ``status.operation.instrument.digio.trigger_overrun.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.digio.trigger_overrun.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.digio.trigger_overrun.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.digio.trigger_overrun.ptr`` attribute.
    """

    LINE1 = "status.operation.instrument.digio.trigger_overrun.LINE1"
    """str: B1. A set bit indicates that digital I/O line 1 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE10 = "status.operation.instrument.digio.trigger_overrun.LINE10"
    """str: B10. A set bit indicates that digital I/O line 10 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE11 = "status.operation.instrument.digio.trigger_overrun.LINE11"
    """str: B11. A set bit indicates that digital I/O line 11 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE12 = "status.operation.instrument.digio.trigger_overrun.LINE12"
    """str: B12. A set bit indicates that digital I/O line 12 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE13 = "status.operation.instrument.digio.trigger_overrun.LINE13"
    """str: B13. A set bit indicates that digital I/O line 13 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE14 = "status.operation.instrument.digio.trigger_overrun.LINE14"
    """str: B14. A set bit indicates that digital I/O line 14 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE2 = "status.operation.instrument.digio.trigger_overrun.LINE2"
    """str: B2. A set bit indicates that digital I/O line 2 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE3 = "status.operation.instrument.digio.trigger_overrun.LINE3"
    """str: B3. A set bit indicates that digital I/O line 3 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE4 = "status.operation.instrument.digio.trigger_overrun.LINE4"
    """str: B4. A set bit indicates that digital I/O line 4 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE5 = "status.operation.instrument.digio.trigger_overrun.LINE5"
    """str: B5. A set bit indicates that digital I/O line 5 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE6 = "status.operation.instrument.digio.trigger_overrun.LINE6"
    """str: B6. A set bit indicates that digital I/O line 6 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE7 = "status.operation.instrument.digio.trigger_overrun.LINE7"
    """str: B7. A set bit indicates that digital I/O line 7 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE8 = "status.operation.instrument.digio.trigger_overrun.LINE8"
    """str: B8. A set bit indicates that digital I/O line 7 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501
    LINE9 = "status.operation.instrument.digio.trigger_overrun.LINE9"
    """str: B9. A set bit indicates that digital I/O line 9 generated an action overrun when it was triggered to generate an output trigger."""  # noqa: E501

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.digio.trigger_overrun.condition`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.digio.trigger_overrun.condition)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun.enable = value
            - print(status.operation.instrument.digio.trigger_overrun.enable)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun.enable`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun.enable = value
            - print(status.operation.instrument.digio.trigger_overrun.enable)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun.event`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.digio.trigger_overrun.event)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun.ntr = value
            - print(status.operation.instrument.digio.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun.ntr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun.ntr = value
            - print(status.operation.instrument.digio.trigger_overrun.ntr)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun.ptr = value
            - print(status.operation.instrument.digio.trigger_overrun.ptr)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun.ptr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun.ptr = value
            - print(status.operation.instrument.digio.trigger_overrun.ptr)
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


class StatusOperationInstrumentDigio(BaseTSPCmd):
    """The ``status.operation.instrument.digio`` command tree.

    Constants:
        - ``.TRGOVR``: B10. Set bit indicates an enabled bit in the Operation Status Digital I/O
          Overrun Register is set.
        - ``.TRIGGER_OVERRUN``: B10. Set bit indicates an enabled bit in the Operation Status
          Digital I/O Overrun Register is set.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.digio.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.digio.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.digio.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.digio.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.digio.ptr`` attribute.
        - ``.trigger_overrun``: The ``status.operation.instrument.digio.trigger_overrun`` command
          tree.
    """

    TRGOVR = "status.operation.instrument.digio.TRGOVR"
    """str: B10. Set bit indicates an enabled bit in the Operation Status Digital I/O Overrun Register is set."""  # noqa: E501
    TRIGGER_OVERRUN = "status.operation.instrument.digio.TRIGGER_OVERRUN"
    """str: B10. Set bit indicates an enabled bit in the Operation Status Digital I/O Overrun Register is set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._trigger_overrun = StatusOperationInstrumentDigioTriggerOverrun(
            device, f"{self._cmd_syntax}.trigger_overrun"
        )

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.digio.condition`` attribute.

        Description:
            - This attribute contains the operation status digital I/O summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.digio.condition)
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
        """Access the ``status.operation.instrument.digio.enable`` attribute.

        Description:
            - This attribute contains the operation status digital I/O summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.enable = value
            - print(status.operation.instrument.digio.enable)
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
        """Access the ``status.operation.instrument.digio.enable`` attribute.

        Description:
            - This attribute contains the operation status digital I/O summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.enable = value
            - print(status.operation.instrument.digio.enable)
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
        """Access the ``status.operation.instrument.digio.event`` attribute.

        Description:
            - This attribute contains the operation status digital I/O summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.digio.event)
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
        """Access the ``status.operation.instrument.digio.ntr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.digio.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.ntr = value
            - print(status.operation.instrument.digio.ntr)
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
        """Access the ``status.operation.instrument.digio.ntr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.digio.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.ntr = value
            - print(status.operation.instrument.digio.ntr)
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
        """Access the ``status.operation.instrument.digio.ptr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.digio.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.ptr = value
            - print(status.operation.instrument.digio.ptr)
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
        """Access the ``status.operation.instrument.digio.ptr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.digio.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.ptr = value
            - print(status.operation.instrument.digio.ptr)
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
    def trigger_overrun(self) -> StatusOperationInstrumentDigioTriggerOverrun:
        """Return the ``status.operation.instrument.digio.trigger_overrun`` command tree.

        Constants:
            - ``.LINE1``: B1. A set bit indicates that digital I/O line 1 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE10``: B10. A set bit indicates that digital I/O line 10 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE11``: B11. A set bit indicates that digital I/O line 11 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE12``: B12. A set bit indicates that digital I/O line 12 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE13``: B13. A set bit indicates that digital I/O line 13 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE14``: B14. A set bit indicates that digital I/O line 14 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE2``: B2. A set bit indicates that digital I/O line 2 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE3``: B3. A set bit indicates that digital I/O line 3 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE4``: B4. A set bit indicates that digital I/O line 4 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE5``: B5. A set bit indicates that digital I/O line 5 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE6``: B6. A set bit indicates that digital I/O line 6 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE7``: B7. A set bit indicates that digital I/O line 7 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE8``: B8. A set bit indicates that digital I/O line 7 generated an action
              overrun when it was triggered to generate an output trigger.
            - ``.LINE9``: B9. A set bit indicates that digital I/O line 9 generated an action
              overrun when it was triggered to generate an output trigger.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.digio.trigger_overrun.condition``
              attribute.
            - ``.enable``: The ``status.operation.instrument.digio.trigger_overrun.enable``
              attribute.
            - ``.event``: The ``status.operation.instrument.digio.trigger_overrun.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.digio.trigger_overrun.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.digio.trigger_overrun.ptr`` attribute.
        """
        return self._trigger_overrun


class StatusOperationInstrument(BaseTSPCmd):
    """The ``status.operation.instrument`` command tree.

    Constants:
        - ``.DIGIO``: B12. Set bit indicates one or more enabled bits for the operation status
          digital I/O summary register is set.
        - ``.DIGITAL_IO``: B12. Set bit indicates one or more enabled bits for the operation status
          digital I/O summary register is set.
        - ``.LAN``: B14. Set bit indicates one or more enabled bits for the operation status LAN
          summary register is set.
        - ``.SMUA``: B1. Set bit indicates one or more enabled bits for the operation status SMU A
          summary register is set.
        - ``.SMUB``: B2. Set bit indicates one or more enabled bits for the operation status SMU B
          summary register is set.
        - ``.TRGBLND``: B10. Set bit indicates one or more enabled bits for the operation status
          trigger blender summary register is set.
        - ``.TRGTMR``: B11. Set bit indicates one or more enabled bits for the operation status
          trigger timer summary register is set.
        - ``.TRIGGER_BLENDER``: B10. Set bit indicates one or more enabled bits for the operation
          status trigger blender summary register is set.
        - ``.TRIGGER_TIMER``: B11. Set bit indicates one or more enabled bits for the operation
          status trigger timer summary register is set.
        - ``.TSPLINK``: B13. Set bit indicates one or more enabled bits for the operation status
          TSP-Link summary register is set.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.condition`` attribute.
        - ``.digio``: The ``status.operation.instrument.digio`` command tree.
        - ``.enable``: The ``status.operation.instrument.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.event`` attribute.
        - ``.lan``: The ``status.operation.instrument.lan`` command tree.
        - ``.ntr``: The ``status.operation.instrument.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.ptr`` attribute.
        - ``.smu``: The ``status.operation.instrument.smuX`` command tree.
        - ``.trigger_blender``: The ``status.operation.instrument.trigger_blender`` command tree.
        - ``.trigger_timer``: The ``status.operation.instrument.trigger_timer`` command tree.
        - ``.tsplink``: The ``status.operation.instrument.tsplink`` command tree.
    """

    DIGIO = "status.operation.instrument.DIGIO"
    """str: B12. Set bit indicates one or more enabled bits for the operation status digital I/O summary register is set."""  # noqa: E501
    DIGITAL_IO = "status.operation.instrument.DIGITAL_IO"
    """str: B12. Set bit indicates one or more enabled bits for the operation status digital I/O summary register is set."""  # noqa: E501
    LAN = "status.operation.instrument.LAN"
    """str: B14. Set bit indicates one or more enabled bits for the operation status LAN summary register is set."""  # noqa: E501
    SMUA = "status.operation.instrument.SMUA"
    """str: B1. Set bit indicates one or more enabled bits for the operation status SMU A summary register is set."""  # noqa: E501
    SMUB = "status.operation.instrument.SMUB"
    """str: B2. Set bit indicates one or more enabled bits for the operation status SMU B summary register is set."""  # noqa: E501
    TRGBLND = "status.operation.instrument.TRGBLND"
    """str: B10. Set bit indicates one or more enabled bits for the operation status trigger blender summary register is set."""  # noqa: E501
    TRGTMR = "status.operation.instrument.TRGTMR"
    """str: B11. Set bit indicates one or more enabled bits for the operation status trigger timer summary register is set."""  # noqa: E501
    TRIGGER_BLENDER = "status.operation.instrument.TRIGGER_BLENDER"
    """str: B10. Set bit indicates one or more enabled bits for the operation status trigger blender summary register is set."""  # noqa: E501
    TRIGGER_TIMER = "status.operation.instrument.TRIGGER_TIMER"
    """str: B11. Set bit indicates one or more enabled bits for the operation status trigger timer summary register is set."""  # noqa: E501
    TSPLINK = "status.operation.instrument.TSPLINK"
    """str: B13. Set bit indicates one or more enabled bits for the operation status TSP-Link summary register is set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._digio = StatusOperationInstrumentDigio(device, f"{self._cmd_syntax}.digio")
        self._lan = StatusOperationInstrumentLan(device, f"{self._cmd_syntax}.lan")
        self._smu: Dict[str, StatusOperationInstrumentSmuxItem] = DefaultDictPassKeyToFactory(
            lambda x: StatusOperationInstrumentSmuxItem(device, f"{self._cmd_syntax}.smu{x}")
        )
        self._trigger_blender = StatusOperationInstrumentTriggerBlender(
            device, f"{self._cmd_syntax}.trigger_blender"
        )
        self._trigger_timer = StatusOperationInstrumentTriggerTimer(
            device, f"{self._cmd_syntax}.trigger_timer"
        )
        self._tsplink = StatusOperationInstrumentTsplink(device, f"{self._cmd_syntax}.tsplink")

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.condition`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.condition)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.condition)
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
    def digio(self) -> StatusOperationInstrumentDigio:
        """Return the ``status.operation.instrument.digio`` command tree.

        Constants:
            - ``.TRGOVR``: B10. Set bit indicates an enabled bit in the Operation Status Digital I/O
              Overrun Register is set.
            - ``.TRIGGER_OVERRUN``: B10. Set bit indicates an enabled bit in the Operation Status
              Digital I/O Overrun Register is set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.digio.condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.digio.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.digio.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.digio.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.digio.ptr`` attribute.
            - ``.trigger_overrun``: The ``status.operation.instrument.digio.trigger_overrun``
              command tree.
        """
        return self._digio

    @property
    def enable(self) -> str:
        """Access the ``status.operation.instrument.enable`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.enable = value
            - print(status.operation.instrument.enable)
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
        """Access the ``status.operation.instrument.enable`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.enable = value
            - print(status.operation.instrument.enable)
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
        """Access the ``status.operation.instrument.event`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.event)
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
    def lan(self) -> StatusOperationInstrumentLan:
        """Return the ``status.operation.instrument.lan`` command tree.

        Constants:
            - ``.CON``: B0. Set bit indicates that the LAN cable is connected and a link has been
              detected.
            - ``.CONF``: B1. Set bit indicates the LAN is performing its configuration sequence.
            - ``.CONFIGURING``: B1. Set bit indicates the LAN is performing its configuration
              sequence.
            - ``.CONNECTION``: B0. Set bit indicates that the LAN cable is connected and a link has
              been detected.
            - ``.TRGOVR``: B10. Set bit indicates one or more enabled bits for the operation status
              LAN trigger overrun register is set.
            - ``.TRIGGER_OVERRUN``: B10. Set bit indicates one or more enabled bits for the
              operation status LAN trigger overrun register is set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.lan.condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.lan.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.lan.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.lan.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.lan.ptr`` attribute.
            - ``.trigger_overrun``: The ``status.operation.instrument.lan.trigger_overrun`` command
              tree.
        """
        return self._lan

    @property
    def ntr(self) -> str:
        """Access the ``status.operation.instrument.ntr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.ntr = value
            - print(status.operation.instrument.ntr)
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
        """Access the ``status.operation.instrument.ntr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.ntr = value
            - print(status.operation.instrument.ntr)
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
        """Access the ``status.operation.instrument.ptr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.ptr = value
            - print(status.operation.instrument.ptr)
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
        """Access the ``status.operation.instrument.ptr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.ptr = value
            - print(status.operation.instrument.ptr)
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
    def smu(self) -> Dict[str, StatusOperationInstrumentSmuxItem]:
        """Return the ``status.operation.instrument.smuX`` command tree.

        Constants:
            - ``.CAL``: Set bit B0 indicates that smuX is unlocked for calibration.
            - ``.CALIBRATING``: Set bit B0 indicates that smuX is unlocked for calibration.
            - ``.MEAS``: Bit B4 is set when making an overlapped measurement, but it is not set when
              making a normal synchronous measurement.
            - ``.MEASURING``: Bit B4 is set when making an overlapped measurement, but it is not set
              when making a normal synchronous measurement.
            - ``.SWE``: Set bit B3 indicates that smuX is sweeping.
            - ``.SWEEPING``: Set bit B3 indicates that smuX is sweeping.
            - ``.TRGOVR``: Set bit B10 indicates an enabled bit has been set in the operation status
              smuX trigger overrun event register.
            - ``.TRIGGER_OVERRUN``: Set bit B10 indicates an enabled bit has been set in the
              operation status smuX trigger overrun event register.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.smuX.condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.smuX.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.smuX.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.smuX.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.smuX.ptr`` attribute.
            - ``.trigger_overrrun``: The ``status.operation.instrument.smuX.trigger_overrrun``
              command tree.
            - ``.trigger_overrun``: The ``status.operation.instrument.smuX.trigger_overrun`` command
              tree.
        """
        return self._smu

    @property
    def trigger_blender(self) -> StatusOperationInstrumentTriggerBlender:
        """Return the ``status.operation.instrument.trigger_blender`` command tree.

        Constants:
            - ``.TRGOVR``: B10. Set bit indicates one or more enabled bits for operation status
              trigger blender overrun register is set.
            - ``.TRIGGER_OVERRUN``: B10. Set bit indicates one or more enabled bits for operation
              status trigger blender overrun register is set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.trigger_blender.condition``
              attribute.
            - ``.enable``: The ``status.operation.instrument.trigger_blender.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.trigger_blender.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.trigger_blender.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.trigger_blender.ptr`` attribute.
            - ``.trigger_overrun``: The
              ``status.operation.instrument.trigger_blender.trigger_overrun`` command tree.
        """
        return self._trigger_blender

    @property
    def trigger_timer(self) -> StatusOperationInstrumentTriggerTimer:
        """Return the ``status.operation.instrument.trigger_timer`` command tree.

        Constants:
            - ``.TRGOVR``: B10. Set bit indicates one or more enabled bits for the operation status
              trigger timer overrun register is set.
            - ``.TRIGGER_OVERRUN``: B10. Set bit indicates one or more enabled bits for the
              operation status trigger timer overrun register is set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.trigger_timer.condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.trigger_timer.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.trigger_timer.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.trigger_timer.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.trigger_timer.ptr`` attribute.
            - ``.trigger_overrun``: The
              ``status.operation.instrument.trigger_timer.trigger_overrun`` command tree.
        """
        return self._trigger_timer

    @property
    def tsplink(self) -> StatusOperationInstrumentTsplink:
        """Return the ``status.operation.instrument.tsplink`` command tree.

        Constants:
            - ``.TRGOVR``: B10. Set bit indicates one or more enabled bits for the operation status
              TSP-Link overrun register is set.
            - ``.TRIGGER_OVERRUN``: B10. Set bit indicates one or more enabled bits for the
              operation status TSP-Link overrun register is set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.tsplink.condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.tsplink.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.tsplink.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.tsplink.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.tsplink.ptr`` attribute.
            - ``.trigger_overrun``: The ``status.operation.instrument.tsplink.trigger_overrun``
              command tree.
        """
        return self._tsplink


class StatusOperationCalibrating(BaseTSPCmd):
    """The ``status.operation.calibrating`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates that SMU A is unlocked for calibration.
        - ``.SMUB``: B2. Set bit indicates that SMU B is unlocked for calibration.

    Properties and methods:
        - ``.condition``: The ``status.operation.calibrating.condition`` attribute.
        - ``.enable``: The ``status.operation.calibrating.enable`` attribute.
        - ``.event``: The ``status.operation.calibrating.event`` attribute.
        - ``.ntr``: The ``status.operation.calibrating.ntr`` attribute.
        - ``.ptr``: The ``status.operation.calibrating.ptr`` attribute.
    """

    SMUA = "status.operation.calibrating.SMUA"
    """str: B1. Set bit indicates that SMU A is unlocked for calibration."""
    SMUB = "status.operation.calibrating.SMUB"
    """str: B2. Set bit indicates that SMU B is unlocked for calibration."""

    @property
    def condition(self) -> str:
        """Access the ``status.operation.calibrating.condition`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.calibrating.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.calibrating.condition)
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
        """Access the ``status.operation.calibrating.enable`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.enable = value
            - print(status.operation.calibrating.enable)
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
        """Access the ``status.operation.calibrating.enable`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.enable = value
            - print(status.operation.calibrating.enable)
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
        """Access the ``status.operation.calibrating.event`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.calibrating.event)
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
        """Access the ``status.operation.calibrating.ntr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.ntr = value
            - print(status.operation.calibrating.ntr)
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
        """Access the ``status.operation.calibrating.ntr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.ntr = value
            - print(status.operation.calibrating.ntr)
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
        """Access the ``status.operation.calibrating.ptr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.ptr = value
            - print(status.operation.calibrating.ptr)
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
        """Access the ``status.operation.calibrating.ptr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.ptr = value
            - print(status.operation.calibrating.ptr)
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


class StatusOperation(BaseTSPCmd):
    """The ``status.operation`` command tree.

    Constants:
        - ``.CAL``: B0. Set bit indicates that the summary bit of the status.operation.calibrating
          register has been set.
        - ``.CALIBRATING``: B0. Set bit indicates that the summary bit of the
          status.operation.calibrating register has been set.
        - ``.INST``: B13. Set bit indicates that the summary bit from the
          status.operation.instrument register is set.
        - ``.INSTRUMENT_SUMMARY``: B13. Set bit indicates that the summary bit from the
          status.operation.instrument register is set.
        - ``.MEAS``: B4. Set bit indicates that the summary bit of the status.operation.measuring
          register is set.
        - ``.MEASURING``: B4. Set bit indicates that the summary bit of the
          status.operation.measuring register is set.
        - ``.PROG``: B14. Set bit indicates that a command or program is running.
        - ``.PROGRAM_RUNNING``: B14. Set bit indicates that a command or program is running.
        - ``.REM``: B11. Set bit indicates that the summary bit of the status.operation.remote
          register is set.
        - ``.REMOTE_SUMMARY``: B11. Set bit indicates that the summary bit of the
          status.operation.remote register is set.
        - ``.SWE``: B3. Set bit indicates that the summary bit from the status.operation.sweeping
          register is set.
        - ``.SWEEPING``: B3. Set bit indicates that the summary bit from the
          status.operation.sweeping register is set.
        - ``.TRGOVR``: B10. Set bit indicates that the summary bit from the
          status.operation.trigger_overrun register is set.
        - ``.TRIGGER_OVERRUN``: B10. Set bit indicates that the summary bit from the
          status.operation.trigger_overrun register is set.
        - ``.USER``: B12. Set bit indicates that the summary bit from the status.operation.user
          register is set.

    Properties and methods:
        - ``.calibrating``: The ``status.operation.calibrating`` command tree.
        - ``.condition``: The ``status.operation.condition`` attribute.
        - ``.enable``: The ``status.operation.enable`` attribute.
        - ``.event``: The ``status.operation.event`` attribute.
        - ``.instrument``: The ``status.operation.instrument`` command tree.
        - ``.measuring``: The ``status.operation.measuring`` command tree.
        - ``.ntr``: The ``status.operation.ntr`` attribute.
        - ``.ptr``: The ``status.operation.ptr`` attribute.
        - ``.remote``: The ``status.operation.remote`` command tree.
        - ``.sweeping``: The ``status.operation.sweeping`` command tree.
        - ``.trigger_overrun``: The ``status.operation.trigger_overrun`` command tree.
        - ``.user``: The ``status.operation.user`` command tree.
    """

    CAL = "status.operation.CAL"
    """str: B0. Set bit indicates that the summary bit of the status.operation.calibrating register has been set."""  # noqa: E501
    CALIBRATING = "status.operation.CALIBRATING"
    """str: B0. Set bit indicates that the summary bit of the status.operation.calibrating register has been set."""  # noqa: E501
    INST = "status.operation.INST"
    """str: B13. Set bit indicates that the summary bit from the status.operation.instrument register is set."""  # noqa: E501
    INSTRUMENT_SUMMARY = "status.operation.INSTRUMENT_SUMMARY"
    """str: B13. Set bit indicates that the summary bit from the status.operation.instrument register is set."""  # noqa: E501
    MEAS = "status.operation.MEAS"
    """str: B4. Set bit indicates that the summary bit of the status.operation.measuring register is set."""  # noqa: E501
    MEASURING = "status.operation.MEASURING"
    """str: B4. Set bit indicates that the summary bit of the status.operation.measuring register is set."""  # noqa: E501
    PROG = "status.operation.PROG"
    """str: B14. Set bit indicates that a command or program is running."""
    PROGRAM_RUNNING = "status.operation.PROGRAM_RUNNING"
    """str: B14. Set bit indicates that a command or program is running."""
    REM = "status.operation.REM"
    """str: B11. Set bit indicates that the summary bit of the status.operation.remote register is set."""  # noqa: E501
    REMOTE_SUMMARY = "status.operation.REMOTE_SUMMARY"
    """str: B11. Set bit indicates that the summary bit of the status.operation.remote register is set."""  # noqa: E501
    SWE = "status.operation.SWE"
    """str: B3. Set bit indicates that the summary bit from the status.operation.sweeping register is set."""  # noqa: E501
    SWEEPING = "status.operation.SWEEPING"
    """str: B3. Set bit indicates that the summary bit from the status.operation.sweeping register is set."""  # noqa: E501
    TRGOVR = "status.operation.TRGOVR"
    """str: B10. Set bit indicates that the summary bit from the status.operation.trigger_overrun register is set."""  # noqa: E501
    TRIGGER_OVERRUN = "status.operation.TRIGGER_OVERRUN"
    """str: B10. Set bit indicates that the summary bit from the status.operation.trigger_overrun register is set."""  # noqa: E501
    USER = "status.operation.USER"
    """str: B12. Set bit indicates that the summary bit from the status.operation.user register is set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calibrating = StatusOperationCalibrating(device, f"{self._cmd_syntax}.calibrating")
        self._instrument = StatusOperationInstrument(device, f"{self._cmd_syntax}.instrument")
        self._measuring = StatusOperationMeasuring(device, f"{self._cmd_syntax}.measuring")
        self._remote = StatusOperationRemote(device, f"{self._cmd_syntax}.remote")
        self._sweeping = StatusOperationSweeping(device, f"{self._cmd_syntax}.sweeping")
        self._trigger_overrun = StatusOperationTriggerOverrun(
            device, f"{self._cmd_syntax}.trigger_overrun"
        )
        self._user = StatusOperationUser(device, f"{self._cmd_syntax}.user")

    @property
    def calibrating(self) -> StatusOperationCalibrating:
        """Return the ``status.operation.calibrating`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates that SMU A is unlocked for calibration.
            - ``.SMUB``: B2. Set bit indicates that SMU B is unlocked for calibration.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.calibrating.condition`` attribute.
            - ``.enable``: The ``status.operation.calibrating.enable`` attribute.
            - ``.event``: The ``status.operation.calibrating.event`` attribute.
            - ``.ntr``: The ``status.operation.calibrating.ntr`` attribute.
            - ``.ptr``: The ``status.operation.calibrating.ptr`` attribute.
        """
        return self._calibrating

    @property
    def condition(self) -> str:
        """Access the ``status.operation.condition`` attribute.

        Description:
            - These attributes manage the operation status register set of the status model.

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
            - These attributes manage the operation status register set of the status model.

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
            - These attributes manage the operation status register set of the status model.

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
            - These attributes manage the operation status register set of the status model.

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

    @property
    def instrument(self) -> StatusOperationInstrument:
        """Return the ``status.operation.instrument`` command tree.

        Constants:
            - ``.DIGIO``: B12. Set bit indicates one or more enabled bits for the operation status
              digital I/O summary register is set.
            - ``.DIGITAL_IO``: B12. Set bit indicates one or more enabled bits for the operation
              status digital I/O summary register is set.
            - ``.LAN``: B14. Set bit indicates one or more enabled bits for the operation status LAN
              summary register is set.
            - ``.SMUA``: B1. Set bit indicates one or more enabled bits for the operation status SMU
              A summary register is set.
            - ``.SMUB``: B2. Set bit indicates one or more enabled bits for the operation status SMU
              B summary register is set.
            - ``.TRGBLND``: B10. Set bit indicates one or more enabled bits for the operation status
              trigger blender summary register is set.
            - ``.TRGTMR``: B11. Set bit indicates one or more enabled bits for the operation status
              trigger timer summary register is set.
            - ``.TRIGGER_BLENDER``: B10. Set bit indicates one or more enabled bits for the
              operation status trigger blender summary register is set.
            - ``.TRIGGER_TIMER``: B11. Set bit indicates one or more enabled bits for the operation
              status trigger timer summary register is set.
            - ``.TSPLINK``: B13. Set bit indicates one or more enabled bits for the operation status
              TSP-Link summary register is set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.condition`` attribute.
            - ``.digio``: The ``status.operation.instrument.digio`` command tree.
            - ``.enable``: The ``status.operation.instrument.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.event`` attribute.
            - ``.lan``: The ``status.operation.instrument.lan`` command tree.
            - ``.ntr``: The ``status.operation.instrument.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.ptr`` attribute.
            - ``.smu``: The ``status.operation.instrument.smuX`` command tree.
            - ``.trigger_blender``: The ``status.operation.instrument.trigger_blender`` command
              tree.
            - ``.trigger_timer``: The ``status.operation.instrument.trigger_timer`` command tree.
            - ``.tsplink``: The ``status.operation.instrument.tsplink`` command tree.
        """
        return self._instrument

    @property
    def measuring(self) -> StatusOperationMeasuring:
        """Return the ``status.operation.measuring`` command tree.

        Constants:
            - ``.SMUA``: B1. Bit is set when SMU A is making an overlapped measurement, but it is
              not set when making a normal synchronous measurement.
            - ``.SMUB``: B2. This bit is set when SMU B is making an overlapped measurement, but it
              is not set when making a normal synchronous measurement.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.measuring.condition`` attribute.
            - ``.enable``: The ``status.operation.measuring.enable`` attribute.
            - ``.event``: The ``status.operation.measuring.event`` attribute.
            - ``.ntr``: The ``status.operation.measuring.ntr`` attribute.
            - ``.ptr``: The ``status.operation.measuring.ptr`` attribute.
        """
        return self._measuring

    @property
    def ntr(self) -> str:
        """Access the ``status.operation.ntr`` attribute.

        Description:
            - These attributes manage the operation status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.ntr)`` query.
            - Setting this property to a value will send the ``status.operation.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.ntr = value
            - print(status.operation.ntr)
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
        """Access the ``status.operation.ntr`` attribute.

        Description:
            - These attributes manage the operation status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.ntr)`` query.
            - Setting this property to a value will send the ``status.operation.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.ntr = value
            - print(status.operation.ntr)
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
        """Access the ``status.operation.ptr`` attribute.

        Description:
            - These attributes manage the operation status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.ptr)`` query.
            - Setting this property to a value will send the ``status.operation.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.ptr = value
            - print(status.operation.ptr)
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
        """Access the ``status.operation.ptr`` attribute.

        Description:
            - These attributes manage the operation status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.ptr)`` query.
            - Setting this property to a value will send the ``status.operation.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.ptr = value
            - print(status.operation.ptr)
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
    def remote(self) -> StatusOperationRemote:
        """Return the ``status.operation.remote`` command tree.

        Constants:
            - ``.CAV``: B1. Set bit indicates there is a command available in the execution queue.
            - ``.COMMAND_AVAILABLE``: B1. Set bit indicates there is a command available in the
              execution queue.
            - ``.PRMPT``: B11. Set bit indicates command prompts are enabled.
            - ``.PROMPTS_ENABLED``: B11. Set bit indicates command prompts are enabled.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.remote.condition`` attribute.
            - ``.enable``: The ``status.operation.remote.enable`` attribute.
            - ``.event``: The ``status.operation.remote.event`` attribute.
            - ``.ntr``: The ``status.operation.remote.ntr`` attribute.
            - ``.ptr``: The ``status.operation.remote.ptr`` attribute.
        """
        return self._remote

    @property
    def sweeping(self) -> StatusOperationSweeping:
        """Return the ``status.operation.sweeping`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates that SMU A is sweeping.
            - ``.SMUB``: B2. Set bit indicates SMU B is sweeping.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.sweeping.condition`` attribute.
            - ``.enable``: The ``status.operation.sweeping.enable`` attribute.
            - ``.event``: The ``status.operation.sweeping.event`` attribute.
            - ``.ntr``: The ``status.operation.sweeping.ntr`` attribute.
            - ``.ptr``: The ``status.operation.sweeping.ptr`` attribute.
        """
        return self._sweeping

    @property
    def trigger_overrun(self) -> StatusOperationTriggerOverrun:
        """Return the ``status.operation.trigger_overrun`` command tree.

        Constants:
            - ``.DIGIO``: B12. Set bit indicates one of the enabled bits in the operation status
              digital I/O overrun event register is set.
            - ``.DIGITAL_IO``: B12. Set bit indicates one of the enabled bits in the operation
              status digital I/O overrun event register is set.
            - ``.LAN``: B14. Set bit indicates one of the enabled bits in the operation status LAN
              trigger overrun event register is set.
            - ``.SMUA``: B1. Set bit indicates one of the enabled bits in the operation status SMU A
              trigger overrun event register is set.
            - ``.SMUB``: B2. Set bit indicates one of the enabled bits in the operation status SMU B
              trigger overrun event register is set.
            - ``.TRGBLND``: B10. Set bit indicates one of the enabled bits in the operation status
              trigger blender overrun event register is set.
            - ``.TRGTMR``: B11. Set bit indicates one of the enabled bits in the operation status
              trigger timer overrun event register is set.
            - ``.TRIGGER_BLENDER``: B10. Set bit indicates one of the enabled bits in the operation
              status trigger blender overrun event register is set.
            - ``.TRIGGER_TIMER``: B11. Set bit indicates one of the enabled bits in the operation
              status trigger timer overrun event register is set.
            - ``.TSPLINK``: B13. Set bit indicates one of the enabled bits in the operation status
              TSP-Link overrun event register is set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.trigger_overrun.condition`` attribute.
            - ``.enable``: The ``status.operation.trigger_overrun.enable`` attribute.
            - ``.event``: The ``status.operation.trigger_overrun.event`` attribute.
            - ``.ntr``: The ``status.operation.trigger_overrun.ntr`` attribute.
            - ``.ptr``: The ``status.operation.trigger_overrun.ptr`` attribute.
        """
        return self._trigger_overrun

    @property
    def user(self) -> StatusOperationUser:
        """Return the ``status.operation.user`` command tree.

        Constants:
            - ``.BIT0``: B0. Read or write bit 0 of the operation status user register.
            - ``.BIT1``: B1. Read or write bit 1 of the operation status user register.
            - ``.BIT10``: B10. Read or write bit 10 of the operation status user register.
            - ``.BIT11``: B11. Read or write bit 11 of the operation status user register.
            - ``.BIT12``: B12. Read or write bit 12 of the operation status user register.
            - ``.BIT13``: B13. Read or write bit 13 of the operation status user register.
            - ``.BIT14``: B14. Read or write bit 14 of the operation status user register.
            - ``.BIT2``: B2. Read or write bit 2 of the operation status user register.
            - ``.BIT3``: B3. Read or write bit 3 of the operation status user register.
            - ``.BIT4``: B4. Read or write bit 4 of the operation status user register.
            - ``.BIT5``: B5. Read or write bit 5 of the operation status user register.
            - ``.BIT6``: B6. Read or write bit 6 of the operation status user register.
            - ``.BIT7``: B7. Read or write bit 7 of the operation status user register.
            - ``.BIT8``: B8. Read or write bit 8 of the operation status user register.
            - ``.BIT9``: B9. Read or write bit 9 of the operation status user register.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.user.condition`` attribute.
            - ``.enable``: The ``status.operation.user.enable`` attribute.
            - ``.event``: The ``status.operation.user.event`` attribute.
            - ``.ntr``: The ``status.operation.user.ntr`` attribute.
            - ``.ptr``: The ``status.operation.user.ptr`` attribute.
        """
        return self._user


class StatusMeasurementVoltageLimit(BaseTSPCmd):
    """The ``status.measurement.voltage_limit`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates the enabled VLMT bit for the SMU A measurement register
          is set.
        - ``.SMUB``: B2. Set bit indicates the enabled VLMT bit for the SMU B measurement register
          is set.

    Properties and methods:
        - ``.condition``: The ``status.measurement.voltage_limit.condition`` attribute.
        - ``.enable``: The ``status.measurement.voltage_limit.enable`` attribute.
        - ``.event``: The ``status.measurement.voltage_limit.event`` attribute.
        - ``.ntr``: The ``status.measurement.voltage_limit.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.voltage_limit.ptr`` attribute.
    """

    SMUA = "status.measurement.voltage_limit.SMUA"
    """str: B1. Set bit indicates the enabled VLMT bit for the SMU A measurement register is set."""
    SMUB = "status.measurement.voltage_limit.SMUB"
    """str: B2. Set bit indicates the enabled VLMT bit for the SMU B measurement register is set."""

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.voltage_limit.condition`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.voltage_limit.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.voltage_limit.condition)
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
        """Access the ``status.measurement.voltage_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.voltage_limit.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.voltage_limit.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.voltage_limit.enable = value
            - print(status.measurement.voltage_limit.enable)
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
        """Access the ``status.measurement.voltage_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.voltage_limit.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.voltage_limit.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.voltage_limit.enable = value
            - print(status.measurement.voltage_limit.enable)
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
        """Access the ``status.measurement.voltage_limit.event`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.voltage_limit.event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.voltage_limit.event)
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
        """Access the ``status.measurement.voltage_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.voltage_limit.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.voltage_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.voltage_limit.ntr = value
            - print(status.measurement.voltage_limit.ntr)
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
        """Access the ``status.measurement.voltage_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.voltage_limit.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.voltage_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.voltage_limit.ntr = value
            - print(status.measurement.voltage_limit.ntr)
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
        """Access the ``status.measurement.voltage_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.voltage_limit.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.voltage_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.voltage_limit.ptr = value
            - print(status.measurement.voltage_limit.ptr)
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
        """Access the ``status.measurement.voltage_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event voltage limit summary register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.voltage_limit.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.voltage_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.voltage_limit.ptr = value
            - print(status.measurement.voltage_limit.ptr)
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


class StatusMeasurementReadingOverflow(BaseTSPCmd):
    """The ``status.measurement.reading_overflow`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates that an overflow reading has been detected for SMU A.
        - ``.SMUB``: B2. Set bit indicates that an overflow reading has been detected for SMU B.

    Properties and methods:
        - ``.condition``: The ``status.measurement.reading_overflow.condition`` attribute.
        - ``.enable``: The ``status.measurement.reading_overflow.enable`` attribute.
        - ``.event``: The ``status.measurement.reading_overflow.event`` attribute.
        - ``.ntr``: The ``status.measurement.reading_overflow.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.reading_overflow.ptr`` attribute.
    """

    SMUA = "status.measurement.reading_overflow.SMUA"
    """str: B1. Set bit indicates that an overflow reading has been detected for SMU A."""
    SMUB = "status.measurement.reading_overflow.SMUB"
    """str: B2. Set bit indicates that an overflow reading has been detected for SMU B."""

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.reading_overflow.condition`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.reading_overflow.condition)
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
        """Access the ``status.measurement.reading_overflow.enable`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.enable = value
            - print(status.measurement.reading_overflow.enable)
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
        """Access the ``status.measurement.reading_overflow.enable`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.enable = value
            - print(status.measurement.reading_overflow.enable)
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
        """Access the ``status.measurement.reading_overflow.event`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.reading_overflow.event)
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
        """Access the ``status.measurement.reading_overflow.ntr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.ntr = value
            - print(status.measurement.reading_overflow.ntr)
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
        """Access the ``status.measurement.reading_overflow.ntr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.ntr = value
            - print(status.measurement.reading_overflow.ntr)
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
        """Access the ``status.measurement.reading_overflow.ptr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.ptr = value
            - print(status.measurement.reading_overflow.ptr)
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
        """Access the ``status.measurement.reading_overflow.ptr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.ptr = value
            - print(status.measurement.reading_overflow.ptr)
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


#  pylint: disable=too-many-instance-attributes
class StatusMeasurementInstrumentSmuxItem(ValidatedChannel, BaseTSPCmd):
    """The ``status.measurement.instrument.smuX`` command tree.

    Constants:
        - ``.BAV``: B8. Set bit indicates that there is at least one reading stored in either or
          both dedicated reading buffers.
        - ``.BUFFER_AVAILABLE``: B8. Set bit indicates that there is at least one reading stored in
          either or both dedicated reading buffers.
        - ``.CURRENT_LIMIT``: B1. Set bit indicates that the current limit was exceeded. This bit is
          updated only when a measurement is made or smuX.source.compliance is invoked.
        - ``.ILMT``: B1. Set bit indicates that the current limit was exceeded. This bit is updated
          only when a measurement is made or smuX.source.compliance is invoked.
        - ``.READING_OVERFLOW``: B7. Set bit indicates that an overflow reading has been detected.
        - ``.ROF``: B7. Set bit indicates that an overflow reading has been detected.
        - ``.VLMT``: B0. Set bit indicates that the voltage limit was exceeded. This bit is updated
          only when a measurement is made or smuX.source.compliance is invoked.
        - ``.VOLTAGE_LIMIT``: B0. Set bit indicates that the voltage limit was exceeded. This bit is
          updated only when a measurement is made or smuX.source.compliance is invoked.

    Properties and methods:
        - ``.condition``: The ``status.measurement.instrument.smuX.condition`` attribute.
        - ``.enable``: The ``status.measurement.instrument.smuX.enable`` attribute.
        - ``.event``: The ``status.measurement.instrument.smuX.event`` attribute.
        - ``.ntr``: The ``status.measurement.instrument.smuX.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.instrument.smuX.ptr`` attribute.
    """

    BAV = "status.measurement.instrument.smuX.BAV"
    """str: B8. Set bit indicates that there is at least one reading stored in either or both dedicated reading buffers."""  # noqa: E501
    BUFFER_AVAILABLE = "status.measurement.instrument.smuX.BUFFER_AVAILABLE"
    """str: B8. Set bit indicates that there is at least one reading stored in either or both dedicated reading buffers."""  # noqa: E501
    CURRENT_LIMIT = "status.measurement.instrument.smuX.CURRENT_LIMIT"
    """str: B1. Set bit indicates that the current limit was exceeded. This bit is updated only when a measurement is made or smuX.source.compliance is invoked."""  # noqa: E501
    ILMT = "status.measurement.instrument.smuX.ILMT"
    """str: B1. Set bit indicates that the current limit was exceeded. This bit is updated only when a measurement is made or smuX.source.compliance is invoked."""  # noqa: E501
    READING_OVERFLOW = "status.measurement.instrument.smuX.READING_OVERFLOW"
    """str: B7. Set bit indicates that an overflow reading has been detected."""
    ROF = "status.measurement.instrument.smuX.ROF"
    """str: B7. Set bit indicates that an overflow reading has been detected."""
    VLMT = "status.measurement.instrument.smuX.VLMT"
    """str: B0. Set bit indicates that the voltage limit was exceeded. This bit is updated only when a measurement is made or smuX.source.compliance is invoked."""  # noqa: E501
    VOLTAGE_LIMIT = "status.measurement.instrument.smuX.VOLTAGE_LIMIT"
    """str: B0. Set bit indicates that the voltage limit was exceeded. This bit is updated only when a measurement is made or smuX.source.compliance is invoked."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.BAV = self.BAV.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.BUFFER_AVAILABLE = self.BUFFER_AVAILABLE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CURRENT_LIMIT = self.CURRENT_LIMIT.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.ILMT = self.ILMT.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.READING_OVERFLOW = self.READING_OVERFLOW.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.ROF = self.ROF.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.VLMT = self.VLMT.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.VOLTAGE_LIMIT = self.VOLTAGE_LIMIT.replace("smuX", f"smu{self._cmd_syntax[3]}")

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.instrument.smuX.condition`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU X summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.smuX.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.instrument.smuX.condition)
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
        """Access the ``status.measurement.instrument.smuX.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU X summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.smuX.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.smuX.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.smuX.enable = value
            - print(status.measurement.instrument.smuX.enable)
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
        """Access the ``status.measurement.instrument.smuX.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU X summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.smuX.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.smuX.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.smuX.enable = value
            - print(status.measurement.instrument.smuX.enable)
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
        """Access the ``status.measurement.instrument.smuX.event`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU X summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.smuX.event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.instrument.smuX.event)
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
        """Access the ``status.measurement.instrument.smuX.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU X summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.smuX.ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.smuX.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.smuX.ntr = value
            - print(status.measurement.instrument.smuX.ntr)
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
        """Access the ``status.measurement.instrument.smuX.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU X summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.smuX.ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.smuX.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.smuX.ntr = value
            - print(status.measurement.instrument.smuX.ntr)
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
        """Access the ``status.measurement.instrument.smuX.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU X summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.smuX.ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.smuX.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.smuX.ptr = value
            - print(status.measurement.instrument.smuX.ptr)
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
        """Access the ``status.measurement.instrument.smuX.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event SMU X summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.smuX.ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.smuX.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.smuX.ptr = value
            - print(status.measurement.instrument.smuX.ptr)
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


class StatusMeasurementInstrument(BaseTSPCmd):
    """The ``status.measurement.instrument`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates one or more enabled bits of the measurement event SMU A
          summary register is set.
        - ``.SMUB``: B2. Set bit indicates one or more enabled bits of the measurement event SMU B
          summary register is set.

    Properties and methods:
        - ``.condition``: The ``status.measurement.instrument.condition`` attribute.
        - ``.enable``: The ``status.measurement.instrument.enable`` attribute.
        - ``.event``: The ``status.measurement.instrument.event`` attribute.
        - ``.ntr``: The ``status.measurement.instrument.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.instrument.ptr`` attribute.
        - ``.smu``: The ``status.measurement.instrument.smuX`` command tree.
    """

    SMUA = "status.measurement.instrument.SMUA"
    """str: B1. Set bit indicates one or more enabled bits of the measurement event SMU A summary register is set."""  # noqa: E501
    SMUB = "status.measurement.instrument.SMUB"
    """str: B2. Set bit indicates one or more enabled bits of the measurement event SMU B summary register is set."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._smu: Dict[str, StatusMeasurementInstrumentSmuxItem] = DefaultDictPassKeyToFactory(
            lambda x: StatusMeasurementInstrumentSmuxItem(device, f"{self._cmd_syntax}.smu{x}")
        )

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.instrument.condition`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.instrument.condition)
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
        """Access the ``status.measurement.instrument.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.enable = value
            - print(status.measurement.instrument.enable)
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
        """Access the ``status.measurement.instrument.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.enable = value
            - print(status.measurement.instrument.enable)
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
        """Access the ``status.measurement.instrument.event`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.event)``
              query.

        TSP Syntax:
            ```
            - print(status.measurement.instrument.event)
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
        """Access the ``status.measurement.instrument.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.ntr = value
            - print(status.measurement.instrument.ntr)
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
        """Access the ``status.measurement.instrument.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.ntr = value
            - print(status.measurement.instrument.ntr)
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
        """Access the ``status.measurement.instrument.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.ptr = value
            - print(status.measurement.instrument.ptr)
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
        """Access the ``status.measurement.instrument.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.ptr = value
            - print(status.measurement.instrument.ptr)
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
    def smu(self) -> Dict[str, StatusMeasurementInstrumentSmuxItem]:
        """Return the ``status.measurement.instrument.smuX`` command tree.

        Constants:
            - ``.BAV``: B8. Set bit indicates that there is at least one reading stored in either or
              both dedicated reading buffers.
            - ``.BUFFER_AVAILABLE``: B8. Set bit indicates that there is at least one reading stored
              in either or both dedicated reading buffers.
            - ``.CURRENT_LIMIT``: B1. Set bit indicates that the current limit was exceeded. This
              bit is updated only when a measurement is made or smuX.source.compliance is invoked.
            - ``.ILMT``: B1. Set bit indicates that the current limit was exceeded. This bit is
              updated only when a measurement is made or smuX.source.compliance is invoked.
            - ``.READING_OVERFLOW``: B7. Set bit indicates that an overflow reading has been
              detected.
            - ``.ROF``: B7. Set bit indicates that an overflow reading has been detected.
            - ``.VLMT``: B0. Set bit indicates that the voltage limit was exceeded. This bit is
              updated only when a measurement is made or smuX.source.compliance is invoked.
            - ``.VOLTAGE_LIMIT``: B0. Set bit indicates that the voltage limit was exceeded. This
              bit is updated only when a measurement is made or smuX.source.compliance is invoked.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.instrument.smuX.condition`` attribute.
            - ``.enable``: The ``status.measurement.instrument.smuX.enable`` attribute.
            - ``.event``: The ``status.measurement.instrument.smuX.event`` attribute.
            - ``.ntr``: The ``status.measurement.instrument.smuX.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.instrument.smuX.ptr`` attribute.
        """
        return self._smu


class StatusMeasurementCurrentLimit(BaseTSPCmd):
    """The ``status.measurement.current_limit`` command tree.

    Constants:
        - ``.SMUA``: B1.
        - ``.SMUB``: B2. Set bit indicates that the SMU B current limit was exceeded.

    Properties and methods:
        - ``.condition``: The ``status.measurement.current_limit.condition`` attribute.
        - ``.enable``: The ``status.measurement.current_limit.enable`` attribute.
        - ``.event``: The ``status.measurement.current_limit.event`` attribute.
        - ``.ntr``: The ``status.measurement.current_limit.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.current_limit.ptr`` attribute.
    """

    SMUA = "status.measurement.current_limit.SMUA"
    """str: B1."""
    SMUB = "status.measurement.current_limit.SMUB"
    """str: B2. Set bit indicates that the SMU B current limit was exceeded."""

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.current_limit.condition`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.current_limit.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.current_limit.condition)
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
        """Access the ``status.measurement.current_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.current_limit.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.enable = value
            - print(status.measurement.current_limit.enable)
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
        """Access the ``status.measurement.current_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.current_limit.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.enable = value
            - print(status.measurement.current_limit.enable)
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
        """Access the ``status.measurement.current_limit.event`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.current_limit.event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.current_limit.event)
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
        """Access the ``status.measurement.current_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the ``print(status.measurement.current_limit.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.ntr = value
            - print(status.measurement.current_limit.ntr)
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
        """Access the ``status.measurement.current_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the ``print(status.measurement.current_limit.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.ntr = value
            - print(status.measurement.current_limit.ntr)
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
        """Access the ``status.measurement.current_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the ``print(status.measurement.current_limit.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.ptr = value
            - print(status.measurement.current_limit.ptr)
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
        """Access the ``status.measurement.current_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the ``print(status.measurement.current_limit.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.ptr = value
            - print(status.measurement.current_limit.ptr)
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


class StatusMeasurementBufferAvailable(BaseTSPCmd):
    """The ``status.measurement.buffer_available`` command tree.

    Constants:
        - ``.SMUA``: B1. Set bit indicates that there is at least
          one reading stored in either or both of
          the dedicated reading buffers.
        - ``.SMUB``: B2. Set bit indicates that there is at least
          one reading stored in either or both of
          the dedicated reading buffers.

    Properties and methods:
        - ``.condition``: The ``status.measurement.buffer_available.condition`` attribute.
        - ``.enable``: The ``status.measurement.buffer_available.enable`` attribute.
        - ``.event``: The ``status.measurement.buffer_available.event`` attribute.
        - ``.ntr``: The ``status.measurement.buffer_available.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.buffer_available.ptr`` attribute.
    """

    SMUA = "status.measurement.buffer_available.SMUA"
    """str: B1. Set bit indicates that there is at least
one reading stored in either or both of
the dedicated reading buffers."""
    SMUB = "status.measurement.buffer_available.SMUB"
    """str: B2. Set bit indicates that there is at least
one reading stored in either or both of
the dedicated reading buffers."""

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.buffer_available.condition`` attribute.

        Description:
            - This attribute contains the measurement event buffer available summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.buffer_available.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.buffer_available.condition)
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
        """Access the ``status.measurement.buffer_available.enable`` attribute.

        Description:
            - This attribute contains the measurement event buffer available summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.buffer_available.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.buffer_available.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.buffer_available.enable = value
            - print(status.measurement.buffer_available.enable)
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
        """Access the ``status.measurement.buffer_available.enable`` attribute.

        Description:
            - This attribute contains the measurement event buffer available summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.buffer_available.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.buffer_available.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.buffer_available.enable = value
            - print(status.measurement.buffer_available.enable)
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
        """Access the ``status.measurement.buffer_available.event`` attribute.

        Description:
            - This attribute contains the measurement event buffer available summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.buffer_available.event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.buffer_available.event)
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
        """Access the ``status.measurement.buffer_available.ntr`` attribute.

        Description:
            - This attribute contains the measurement event buffer available summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.buffer_available.ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.buffer_available.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.buffer_available.ntr = value
            - print(status.measurement.buffer_available.ntr)
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
        """Access the ``status.measurement.buffer_available.ntr`` attribute.

        Description:
            - This attribute contains the measurement event buffer available summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.buffer_available.ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.buffer_available.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.buffer_available.ntr = value
            - print(status.measurement.buffer_available.ntr)
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
        """Access the ``status.measurement.buffer_available.ptr`` attribute.

        Description:
            - This attribute contains the measurement event buffer available summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.buffer_available.ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.buffer_available.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.buffer_available.ptr = value
            - print(status.measurement.buffer_available.ptr)
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
        """Access the ``status.measurement.buffer_available.ptr`` attribute.

        Description:
            - This attribute contains the measurement event buffer available summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.buffer_available.ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.buffer_available.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.buffer_available.ptr = value
            - print(status.measurement.buffer_available.ptr)
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


class StatusMeasurement(BaseTSPCmd):
    """The ``status.measurement`` command tree.

    Constants:
        - ``.BAV``: B8. Set bit is a summary of the status.measurement.buffer_available register.
        - ``.BUFFER_AVAILABLE``: B8. Set bit is a summary of the status.measurement.buffer_available
          register.
        - ``.CURRENT_LIMIT``: B1. Set bit is a summary of the
          status.measurement.current_limit
          register.
        - ``.ILMT``: B1. Set bit is a summary of the
          status.measurement.current_limit
          register.
        - ``.INST``: B13. Set bit indicates that a bit in the measurement instrument summary
          register is set.
        - ``.INSTRUMENT_SUMMARY``: B13. Set bit indicates that a bit in the measurement instrument
          summary register is set.
        - ``.OE``: B11.
        - ``.OUTPUT_ENABLE``: B11.
        - ``.READING_OVERFLOW``: B7. Set bit is a summary of the status.measurement.reading_overflow
          register.
        - ``.ROF``: B7. Set bit is a summary of the status.measurement.reading_overflow register.
        - ``.VLMT``: B0. Set bit is a summary of the status.measurement.voltage_limit register.
        - ``.VOLTAGE_LIMIT``: B0. Set bit is a summary of the status.measurement.voltage_limit
          register.

    Properties and methods:
        - ``.buffer_available``: The ``status.measurement.buffer_available`` command tree.
        - ``.condition``: The ``status.measurement.condition`` attribute.
        - ``.current_limit``: The ``status.measurement.current_limit`` command tree.
        - ``.enable``: The ``status.measurement.enable`` attribute.
        - ``.event``: The ``status.measurement.event`` attribute.
        - ``.instrument``: The ``status.measurement.instrument`` command tree.
        - ``.ntr``: The ``status.measurement.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.ptr`` attribute.
        - ``.reading_overflow``: The ``status.measurement.reading_overflow`` command tree.
        - ``.voltage_limit``: The ``status.measurement.voltage_limit`` command tree.
    """

    BAV = "status.measurement.BAV"
    """str: B8. Set bit is a summary of the status.measurement.buffer_available register."""
    BUFFER_AVAILABLE = "status.measurement.BUFFER_AVAILABLE"
    """str: B8. Set bit is a summary of the status.measurement.buffer_available register."""
    CURRENT_LIMIT = "status.measurement.CURRENT_LIMIT"
    """str: B1. Set bit is a summary of the
status.measurement.current_limit
register."""
    ILMT = "status.measurement.ILMT"
    """str: B1. Set bit is a summary of the
status.measurement.current_limit
register."""
    INST = "status.measurement.INST"
    """str: B13. Set bit indicates that a bit in the measurement instrument summary register is set."""  # noqa: E501
    INSTRUMENT_SUMMARY = "status.measurement.INSTRUMENT_SUMMARY"
    """str: B13. Set bit indicates that a bit in the measurement instrument summary register is set."""  # noqa: E501
    OE = "status.measurement.OE"
    """str: B11."""
    OUTPUT_ENABLE = "status.measurement.OUTPUT_ENABLE"
    """str: B11."""
    READING_OVERFLOW = "status.measurement.READING_OVERFLOW"
    """str: B7. Set bit is a summary of the status.measurement.reading_overflow register."""
    ROF = "status.measurement.ROF"
    """str: B7. Set bit is a summary of the status.measurement.reading_overflow register."""
    VLMT = "status.measurement.VLMT"
    """str: B0. Set bit is a summary of the status.measurement.voltage_limit register."""
    VOLTAGE_LIMIT = "status.measurement.VOLTAGE_LIMIT"
    """str: B0. Set bit is a summary of the status.measurement.voltage_limit register."""

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._buffer_available = StatusMeasurementBufferAvailable(
            device, f"{self._cmd_syntax}.buffer_available"
        )
        self._current_limit = StatusMeasurementCurrentLimit(
            device, f"{self._cmd_syntax}.current_limit"
        )
        self._instrument = StatusMeasurementInstrument(device, f"{self._cmd_syntax}.instrument")
        self._reading_overflow = StatusMeasurementReadingOverflow(
            device, f"{self._cmd_syntax}.reading_overflow"
        )
        self._voltage_limit = StatusMeasurementVoltageLimit(
            device, f"{self._cmd_syntax}.voltage_limit"
        )

    @property
    def buffer_available(self) -> StatusMeasurementBufferAvailable:
        """Return the ``status.measurement.buffer_available`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates that there is at least
              one reading stored in either or both of
              the dedicated reading buffers.
            - ``.SMUB``: B2. Set bit indicates that there is at least
              one reading stored in either or both of
              the dedicated reading buffers.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.buffer_available.condition`` attribute.
            - ``.enable``: The ``status.measurement.buffer_available.enable`` attribute.
            - ``.event``: The ``status.measurement.buffer_available.event`` attribute.
            - ``.ntr``: The ``status.measurement.buffer_available.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.buffer_available.ptr`` attribute.
        """
        return self._buffer_available

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.condition`` attribute.

        Description:
            - This attribute contains the measurement event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.condition)
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
    def current_limit(self) -> StatusMeasurementCurrentLimit:
        """Return the ``status.measurement.current_limit`` command tree.

        Constants:
            - ``.SMUA``: B1.
            - ``.SMUB``: B2. Set bit indicates that the SMU B current limit was exceeded.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.current_limit.condition`` attribute.
            - ``.enable``: The ``status.measurement.current_limit.enable`` attribute.
            - ``.event``: The ``status.measurement.current_limit.event`` attribute.
            - ``.ntr``: The ``status.measurement.current_limit.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.current_limit.ptr`` attribute.
        """
        return self._current_limit

    @property
    def enable(self) -> str:
        """Access the ``status.measurement.enable`` attribute.

        Description:
            - This attribute contains the measurement event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.enable)`` query.
            - Setting this property to a value will send the ``status.measurement.enable = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.enable = value
            - print(status.measurement.enable)
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
        """Access the ``status.measurement.enable`` attribute.

        Description:
            - This attribute contains the measurement event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.enable)`` query.
            - Setting this property to a value will send the ``status.measurement.enable = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.enable = value
            - print(status.measurement.enable)
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
        """Access the ``status.measurement.event`` attribute.

        Description:
            - This attribute contains the measurement event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.event)
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
    def instrument(self) -> StatusMeasurementInstrument:
        """Return the ``status.measurement.instrument`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates one or more enabled bits of the measurement event SMU
              A summary register is set.
            - ``.SMUB``: B2. Set bit indicates one or more enabled bits of the measurement event SMU
              B summary register is set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.instrument.condition`` attribute.
            - ``.enable``: The ``status.measurement.instrument.enable`` attribute.
            - ``.event``: The ``status.measurement.instrument.event`` attribute.
            - ``.ntr``: The ``status.measurement.instrument.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.instrument.ptr`` attribute.
            - ``.smu``: The ``status.measurement.instrument.smuX`` command tree.
        """
        return self._instrument

    @property
    def ntr(self) -> str:
        """Access the ``status.measurement.ntr`` attribute.

        Description:
            - This attribute contains the measurement event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.ntr)`` query.
            - Setting this property to a value will send the ``status.measurement.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.ntr = value
            - print(status.measurement.ntr)
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
        """Access the ``status.measurement.ntr`` attribute.

        Description:
            - This attribute contains the measurement event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.ntr)`` query.
            - Setting this property to a value will send the ``status.measurement.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.ntr = value
            - print(status.measurement.ntr)
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
        """Access the ``status.measurement.ptr`` attribute.

        Description:
            - This attribute contains the measurement event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.ptr)`` query.
            - Setting this property to a value will send the ``status.measurement.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.ptr = value
            - print(status.measurement.ptr)
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
        """Access the ``status.measurement.ptr`` attribute.

        Description:
            - This attribute contains the measurement event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.ptr)`` query.
            - Setting this property to a value will send the ``status.measurement.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.ptr = value
            - print(status.measurement.ptr)
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
    def reading_overflow(self) -> StatusMeasurementReadingOverflow:
        """Return the ``status.measurement.reading_overflow`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates that an overflow reading has been detected for SMU A.
            - ``.SMUB``: B2. Set bit indicates that an overflow reading has been detected for SMU B.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.reading_overflow.condition`` attribute.
            - ``.enable``: The ``status.measurement.reading_overflow.enable`` attribute.
            - ``.event``: The ``status.measurement.reading_overflow.event`` attribute.
            - ``.ntr``: The ``status.measurement.reading_overflow.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.reading_overflow.ptr`` attribute.
        """
        return self._reading_overflow

    @property
    def voltage_limit(self) -> StatusMeasurementVoltageLimit:
        """Return the ``status.measurement.voltage_limit`` command tree.

        Constants:
            - ``.SMUA``: B1. Set bit indicates the enabled VLMT bit for the SMU A measurement
              register is set.
            - ``.SMUB``: B2. Set bit indicates the enabled VLMT bit for the SMU B measurement
              register is set.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.voltage_limit.condition`` attribute.
            - ``.enable``: The ``status.measurement.voltage_limit.enable`` attribute.
            - ``.event``: The ``status.measurement.voltage_limit.event`` attribute.
            - ``.ntr``: The ``status.measurement.voltage_limit.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.voltage_limit.ptr`` attribute.
        """
        return self._voltage_limit


#  pylint: disable=too-many-instance-attributes
class Status(BaseTSPCmd):
    """The ``status`` command tree.

    Constants:
        - ``.EAV``: B2. Set summary bit indicates that an error or status message is present in the
          Error Queue.
        - ``.ERROR_AVAILABLE``: B2. Set summary bit indicates that an error or status message is
          present in the Error Queue.
        - ``.ESB``: B5. Set summary bit indicates that an enabled standard event has occurred.
        - ``.EVENT_SUMMARY_BIT``: B5. Set summary bit indicates that an enabled standard event has
          occurred.
        - ``.MASTER_SUMMARY_STATUS``: B6. Request Service (RQS)/Master Summary Status (MSS).
          Depending on how it is used, bit B6 of the status byte register is either the Request for
          Service (RQS) bit or the Master Summary Status (MSS) bit.
        - ``.MAV``: B4. Set summary bit indicates that a response message is present in the Output
          Queue.
        - ``.MEASUREMENT_SUMMARY_BIT``: B0. Set summary bit indicates that an enabled measurement
          event has occurred.
        - ``.MESSAGE_AVAILABLE``: B4. Set summary bit indicates that a response message is present
          in the Output Queue.
        - ``.MSB``: B0. Set summary bit indicates that an enabled measurement event has occurred.
        - ``.MSS``: An enabled summary bit of the status byte register is set.
        - ``.OPERATION_SUMMARY_BIT``: B7. Set summary bit indicates that an enabled operation event
          has occurred.
        - ``.OSB``: B7. Set summary bit indicates that an enabled operation event has occurred.
        - ``.QSB``: B3. Set summary bit indicates that an enabled questionable event has occurred.
        - ``.QUESTIONABLE_SUMMARY_BIT``: B3. Set summary bit indicates that an enabled questionable
          event has occurred.
        - ``.SSB``: B1. Set summary bit indicates that an enabled system event has occurred.
        - ``.SYSTEM_SUMMARY_BIT``: B1. Set summary bit indicates that an enabled system event has
          occurred.

    Properties and methods:
        - ``.condition``: The ``status.condition`` attribute.
        - ``.measurement``: The ``status.measurement`` command tree.
        - ``.node_enable``: The ``status.node_enable`` attribute.
        - ``.node_event``: The ``status.node_event`` attribute.
        - ``.operation``: The ``status.operation`` command tree.
        - ``.questionable``: The ``status.questionable`` command tree.
        - ``.request_enable``: The ``status.request_enable`` attribute.
        - ``.request_event``: The ``status.request_event`` attribute.
        - ``.reset()``: The ``status.reset()`` function.
        - ``.standard``: The ``status.standard`` command tree.
        - ``.system``: The ``status.system`` command tree.
        - ``.system2``: The ``status.system2`` command tree.
        - ``.system3``: The ``status.system3`` command tree.
        - ``.system4``: The ``status.system4`` command tree.
        - ``.system5``: The ``status.system5`` command tree.
    """

    EAV = "status.EAV"
    """str: B2. Set summary bit indicates that an error or status message is present in the Error Queue."""  # noqa: E501
    ERROR_AVAILABLE = "status.ERROR_AVAILABLE"
    """str: B2. Set summary bit indicates that an error or status message is present in the Error Queue."""  # noqa: E501
    ESB = "status.ESB"
    """str: B5. Set summary bit indicates that an enabled standard event has occurred."""
    EVENT_SUMMARY_BIT = "status.EVENT_SUMMARY_BIT"
    """str: B5. Set summary bit indicates that an enabled standard event has occurred."""
    MASTER_SUMMARY_STATUS = "status.MASTER_SUMMARY_STATUS"
    """str: B6. Request Service (RQS)/Master Summary Status (MSS). Depending on how it is used, bit B6 of the status byte register is either the Request for Service (RQS) bit or the Master Summary Status (MSS) bit."""  # noqa: E501
    MAV = "status.MAV"
    """str: B4. Set summary bit indicates that a response message is present in the Output Queue."""
    MEASUREMENT_SUMMARY_BIT = "status.MEASUREMENT_SUMMARY_BIT"
    """str: B0. Set summary bit indicates that an enabled measurement event has occurred."""
    MESSAGE_AVAILABLE = "status.MESSAGE_AVAILABLE"
    """str: B4. Set summary bit indicates that a response message is present in the Output Queue."""
    MSB = "status.MSB"
    """str: B0. Set summary bit indicates that an enabled measurement event has occurred."""
    MSS = "status.MSS"
    """str: An enabled summary bit of the status byte register is set."""
    OPERATION_SUMMARY_BIT = "status.OPERATION_SUMMARY_BIT"
    """str: B7. Set summary bit indicates that an enabled operation event has occurred."""
    OSB = "status.OSB"
    """str: B7. Set summary bit indicates that an enabled operation event has occurred."""
    QSB = "status.QSB"
    """str: B3. Set summary bit indicates that an enabled questionable event has occurred."""
    QUESTIONABLE_SUMMARY_BIT = "status.QUESTIONABLE_SUMMARY_BIT"
    """str: B3. Set summary bit indicates that an enabled questionable event has occurred."""
    SSB = "status.SSB"
    """str: B1. Set summary bit indicates that an enabled system event has occurred."""
    SYSTEM_SUMMARY_BIT = "status.SYSTEM_SUMMARY_BIT"
    """str: B1. Set summary bit indicates that an enabled system event has occurred."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "status") -> None:
        super().__init__(device, cmd_syntax)
        self._measurement = StatusMeasurement(device, f"{self._cmd_syntax}.measurement")
        self._operation = StatusOperation(device, f"{self._cmd_syntax}.operation")
        self._questionable = StatusQuestionable(device, f"{self._cmd_syntax}.questionable")
        self._standard = StatusStandard(device, f"{self._cmd_syntax}.standard")
        self._system = StatusSystem(device, f"{self._cmd_syntax}.system")
        self._system2 = StatusSystem2(device, f"{self._cmd_syntax}.system2")
        self._system3 = StatusSystem3(device, f"{self._cmd_syntax}.system3")
        self._system4 = StatusSystem4(device, f"{self._cmd_syntax}.system4")
        self._system5 = StatusSystem5(device, f"{self._cmd_syntax}.system5")

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
    def measurement(self) -> StatusMeasurement:
        """Return the ``status.measurement`` command tree.

        Constants:
            - ``.BAV``: B8. Set bit is a summary of the status.measurement.buffer_available
              register.
            - ``.BUFFER_AVAILABLE``: B8. Set bit is a summary of the
              status.measurement.buffer_available register.
            - ``.CURRENT_LIMIT``: B1. Set bit is a summary of the
              status.measurement.current_limit
              register.
            - ``.ILMT``: B1. Set bit is a summary of the
              status.measurement.current_limit
              register.
            - ``.INST``: B13. Set bit indicates that a bit in the measurement instrument summary
              register is set.
            - ``.INSTRUMENT_SUMMARY``: B13. Set bit indicates that a bit in the measurement
              instrument summary register is set.
            - ``.OE``: B11.
            - ``.OUTPUT_ENABLE``: B11.
            - ``.READING_OVERFLOW``: B7. Set bit is a summary of the
              status.measurement.reading_overflow register.
            - ``.ROF``: B7. Set bit is a summary of the status.measurement.reading_overflow
              register.
            - ``.VLMT``: B0. Set bit is a summary of the status.measurement.voltage_limit register.
            - ``.VOLTAGE_LIMIT``: B0. Set bit is a summary of the status.measurement.voltage_limit
              register.

        Sub-properties and sub-methods:
            - ``.buffer_available``: The ``status.measurement.buffer_available`` command tree.
            - ``.condition``: The ``status.measurement.condition`` attribute.
            - ``.current_limit``: The ``status.measurement.current_limit`` command tree.
            - ``.enable``: The ``status.measurement.enable`` attribute.
            - ``.event``: The ``status.measurement.event`` attribute.
            - ``.instrument``: The ``status.measurement.instrument`` command tree.
            - ``.ntr``: The ``status.measurement.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.ptr`` attribute.
            - ``.reading_overflow``: The ``status.measurement.reading_overflow`` command tree.
            - ``.voltage_limit``: The ``status.measurement.voltage_limit`` command tree.
        """
        return self._measurement

    @property
    def node_enable(self) -> str:
        """Access the ``status.node_enable`` attribute.

        Description:
            - This attribute stores the system node enable register.

        Usage:
            - Accessing this property will send the ``print(status.node_enable)`` query.
            - Setting this property to a value will send the ``status.node_enable = value`` command.

        TSP Syntax:
            ```
            - status.node_enable = value
            - print(status.node_enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".node_enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.node_enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.node_enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @node_enable.setter
    def node_enable(self, value: Union[str, float]) -> None:
        """Access the ``status.node_enable`` attribute.

        Description:
            - This attribute stores the system node enable register.

        Usage:
            - Accessing this property will send the ``print(status.node_enable)`` query.
            - Setting this property to a value will send the ``status.node_enable = value`` command.

        TSP Syntax:
            ```
            - status.node_enable = value
            - print(status.node_enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".node_enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.node_enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.node_enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def node_event(self) -> str:
        """Access the ``status.node_event`` attribute.

        Description:
            - This attribute stores the status node event register.

        Usage:
            - Accessing this property will send the ``print(status.node_event)`` query.

        TSP Syntax:
            ```
            - print(status.node_event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".node_event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.node_event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.node_event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def operation(self) -> StatusOperation:
        """Return the ``status.operation`` command tree.

        Constants:
            - ``.CAL``: B0. Set bit indicates that the summary bit of the
              status.operation.calibrating register has been set.
            - ``.CALIBRATING``: B0. Set bit indicates that the summary bit of the
              status.operation.calibrating register has been set.
            - ``.INST``: B13. Set bit indicates that the summary bit from the
              status.operation.instrument register is set.
            - ``.INSTRUMENT_SUMMARY``: B13. Set bit indicates that the summary bit from the
              status.operation.instrument register is set.
            - ``.MEAS``: B4. Set bit indicates that the summary bit of the
              status.operation.measuring register is set.
            - ``.MEASURING``: B4. Set bit indicates that the summary bit of the
              status.operation.measuring register is set.
            - ``.PROG``: B14. Set bit indicates that a command or program is running.
            - ``.PROGRAM_RUNNING``: B14. Set bit indicates that a command or program is running.
            - ``.REM``: B11. Set bit indicates that the summary bit of the status.operation.remote
              register is set.
            - ``.REMOTE_SUMMARY``: B11. Set bit indicates that the summary bit of the
              status.operation.remote register is set.
            - ``.SWE``: B3. Set bit indicates that the summary bit from the
              status.operation.sweeping register is set.
            - ``.SWEEPING``: B3. Set bit indicates that the summary bit from the
              status.operation.sweeping register is set.
            - ``.TRGOVR``: B10. Set bit indicates that the summary bit from the
              status.operation.trigger_overrun register is set.
            - ``.TRIGGER_OVERRUN``: B10. Set bit indicates that the summary bit from the
              status.operation.trigger_overrun register is set.
            - ``.USER``: B12. Set bit indicates that the summary bit from the status.operation.user
              register is set.

        Sub-properties and sub-methods:
            - ``.calibrating``: The ``status.operation.calibrating`` command tree.
            - ``.condition``: The ``status.operation.condition`` attribute.
            - ``.enable``: The ``status.operation.enable`` attribute.
            - ``.event``: The ``status.operation.event`` attribute.
            - ``.instrument``: The ``status.operation.instrument`` command tree.
            - ``.measuring``: The ``status.operation.measuring`` command tree.
            - ``.ntr``: The ``status.operation.ntr`` attribute.
            - ``.ptr``: The ``status.operation.ptr`` attribute.
            - ``.remote``: The ``status.operation.remote`` command tree.
            - ``.sweeping``: The ``status.operation.sweeping`` command tree.
            - ``.trigger_overrun``: The ``status.operation.trigger_overrun`` command tree.
            - ``.user``: The ``status.operation.user`` command tree.
        """
        return self._operation

    @property
    def questionable(self) -> StatusQuestionable:
        """Return the ``status.questionable`` command tree.

        Constants:
            - ``.CAL``: B8. An enabled bit in the questionable status calibration summary event
              register is set.
            - ``.CALIBRATION``: B8. An enabled bit in the questionable status calibration summary
              event register is set.
            - ``.INST``: B13. An enabled bit in the questionable status instrument summary event
              register is set.
            - ``.INSTRUMENT_SUMMARY``: B13. An enabled bit in the questionable status instrument
              summary event register is set.
            - ``.OTEMP``: B12. An enabled bit in the questionable status over temperature summary
              event register is set.
            - ``.OVER_TEMPERATURE``: B12. An enabled bit in the questionable status over temperature
              summary event register is set.
            - ``.UNSTABLE_OUTPUT``: B9. An enabled bit in the questionable status unstable output
              summary event register is set.
            - ``.UO``: B9. An enabled bit in the questionable status unstable output summary event
              register is set.

        Sub-properties and sub-methods:
            - ``.calibration``: The ``status.questionable.calibration`` command tree.
            - ``.condition``: The ``status.questionable.condition`` attribute.
            - ``.enable``: The ``status.questionable.enable`` attribute.
            - ``.event``: The ``status.questionable.event`` attribute.
            - ``.instrument``: The ``status.questionable.instrument`` command tree.
            - ``.ntr``: The ``status.questionable.ntr`` attribute.
            - ``.over_temperature``: The ``status.questionable.over_temperature`` command tree.
            - ``.ptr``: The ``status.questionable.ptr`` attribute.
            - ``.unstable_output``: The ``status.questionable.unstable_output`` command tree.
        """
        return self._questionable

    @property
    def request_enable(self) -> str:
        """Access the ``status.request_enable`` attribute.

        Description:
            - This attribute stores the service request (SRQ) enable register.

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
            - This attribute stores the service request (SRQ) enable register.

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
    def request_event(self) -> str:
        """Access the ``status.request_event`` attribute.

        Description:
            - This attribute stores the service request (SRQ) event register.

        Usage:
            - Accessing this property will send the ``print(status.request_event)`` query.

        TSP Syntax:
            ```
            - print(status.request_event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".request_event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.request_event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.request_event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def standard(self) -> StatusStandard:
        r"""Return the ``status.standard`` command tree.

        Constants:
            - ``.CME``: B5. Set bit indicates that a command error has occurred. Command errors
              include.
            - ``.COMMAND_ERROR``: B5. Set bit indicates that a command error has occurred. Command
              errors include.
            - ``.DDE``: B3. Set bit indicates that an instrument operation did not execute properly
              due to some internal condition.
            - ``.DEVICE_DEPENDENT_ERROR``: B3. Set bit indicates that an instrument operation did
              not execute properly due to some internal condition.
            - ``.EXE``: B4. Set bit indicates that the instrument detected an error while trying to
              execute a command.
            - ``.EXECUTION_ERROR``: B4. Set bit indicates that the instrument detected an error
              while trying to execute a command.
            - ``.OPC``: B0. Set bit indicates that all pending selected instrument operations are
              completed and the instrument is ready to accept new commands. The bit is set in
              response to an \*OPC command. The opc() function can be used in place of the \*OPC
              command.
            - ``.OPERATION_COMPLETE``: B0. Set bit indicates that all pending selected instrument
              operations are completed and the instrument is ready to accept new commands. The bit
              is set in response to an \*OPC command. The opc() function can be used in place of the
              \*OPC command.
            - ``.PON``: B7. Set bit indicates that the instrument has been turned off and turned
              back on since the last time this register has been read.
            - ``.POWER_ON``: B7. Set bit indicates that the instrument has been turned off and
              turned back on since the last time this register has been read.
            - ``.QUERY_ERROR``: B2. Set bit indicates that you attempted to read data from an empty
              Output Queue.
            - ``.QYE``: B2. Set bit indicates that you attempted to read data from an empty Output
              Queue.
            - ``.URQ``: B6. Set bit indicates that the LOCAL key on the instrument front panel was
              pressed.
            - ``.USER_REQUEST``: B6. Set bit indicates that the LOCAL key on the instrument front
              panel was pressed.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.standard.condition`` attribute.
            - ``.enable``: The ``status.standard.enable`` attribute.
            - ``.event``: The ``status.standard.event`` attribute.
            - ``.ntr``: The ``status.standard.ntr`` attribute.
            - ``.ptr``: The ``status.standard.ptr`` attribute.
        """
        return self._standard

    @property
    def system(self) -> StatusSystem:
        """Return the ``status.system`` command tree.

        Constants:
            - ``.EXT``: B0. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.
            - ``.EXTENSION_BIT``: B0. In an expanded system (TSP-Link), this is used to read or
              write to the system summary register.
            - ``.NODE1``: B1. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.
            - ``.NODE10``: B10. In an expanded system (TSP-Link), this is used to read or write to
              the system summary register.
            - ``.NODE11``: B11. In an expanded system (TSP-Link), this is used to read or write to
              the system summary register.
            - ``.NODE12``: B12. In an expanded system (TSP-Link), this is used to read or write to
              the system summary register.
            - ``.NODE13``: B13. In an expanded system (TSP-Link), this is used to read or write to
              the system summary register.
            - ``.NODE14``: B14. In an expanded system (TSP-Link), this is used to read or write to
              the system summary register.
            - ``.NODE2``: B2. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.
            - ``.NODE3``: B3. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.
            - ``.NODE4``: B4. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.
            - ``.NODE5``: B5. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.
            - ``.NODE6``: B6. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.
            - ``.NODE7``: B7. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.
            - ``.NODE8``: B8. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.
            - ``.NODE9``: B9. In an expanded system (TSP-Link), this is used to read or write to the
              system summary register.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.system.condition`` attribute.
            - ``.enable``: The ``status.system.enable`` attribute.
            - ``.event``: The ``status.system.event`` attribute.
            - ``.ntr``: The ``status.system.ntr`` attribute.
            - ``.ptr``: The ``status.system.ptr`` attribute.
        """
        return self._system

    @property
    def system2(self) -> StatusSystem2:
        """Return the ``status.system2`` command tree.

        Constants:
            - ``.EXT``: B0. Manages the TSP-Link system summary register of the status model for
              nodes 15 through 28.
            - ``.EXTENSION_BIT``: B0. Manages the TSP-Link system summary register of the status
              model for nodes 15 through 28.
            - ``.NODE15``: B1. Manages the TSP-Link system summary register of the status model for
              node 15.
            - ``.NODE16``: B2. Manages the TSP-Link system summary register of the status model for
              node 16.
            - ``.NODE17``: B3. Manages the TSP-Link system summary register of the status model for
              node 17.
            - ``.NODE18``: B4. Manages the TSP-Link system summary register of the status model for
              node 18.
            - ``.NODE19``: B5. Manages the TSP-Link system summary register of the status model for
              node 19.
            - ``.NODE20``: B6. Manages the TSP-Link system summary register of the status model for
              node 20.
            - ``.NODE21``: B7. Manages the TSP-Link system summary register of the status model for
              node 21.
            - ``.NODE22``: B8. Manages the TSP-Link system summary register of the status model for
              node 22.
            - ``.NODE23``: B9. Manages the TSP-Link system summary register of the status model for
              node 23.
            - ``.NODE24``: B10. Manages the TSP-Link system summary register of the status model for
              node 24.
            - ``.NODE25``: B11. Manages the TSP-Link system summary register of the status model for
              node 25.
            - ``.NODE26``: B12. Manages the TSP-Link system summary register of the status model for
              node 26.
            - ``.NODE27``: B13. Manages the TSP-Link system summary register of the status model for
              node 27.
            - ``.NODE28``: B14. Manages the TSP-Link system summary register of the status model for
              node 28.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.system2.condition`` attribute.
            - ``.enable``: The ``status.system2.enable`` attribute.
            - ``.event``: The ``status.system2.event`` attribute.
            - ``.ntr``: The ``status.system2.ntr`` attribute.
            - ``.ptr``: The ``status.system2.ptr`` attribute.
        """
        return self._system2

    @property
    def system3(self) -> StatusSystem3:
        """Return the ``status.system3`` command tree.

        Constants:
            - ``.EXT``: B0. This attribute manages the TSP-Link system summary register of the
              status model for nodes 29 through 42.
            - ``.EXTENSION_BIT``: B0. This attribute manages the TSP-Link system summary register of
              the status model for nodes 29 through 42.
            - ``.NODE29``: B1. This attribute manages the TSP-Link system summary register of the
              status model for node 29.
            - ``.NODE30``: B2. This attribute manages the TSP-Link system summary register of the
              status model for node 30.
            - ``.NODE31``: B3. This attribute manages the TSP-Link system summary register of the
              status model for node 31.
            - ``.NODE32``: B4. This attribute manages the TSP-Link system summary register of the
              status model for node 32.
            - ``.NODE33``: B5. This attribute manages the TSP-Link system summary register of the
              status model for node 33.
            - ``.NODE34``: B6. This attribute manages the TSP-Link system summary register of the
              status model for node 34.
            - ``.NODE35``: B7. This attribute manages the TSP-Link system summary register of the
              status model for node 35.
            - ``.NODE36``: B7. This attribute manages the TSP-Link system summary register of the
              status model for node 36.
            - ``.NODE37``: B8. This attribute manages the TSP-Link system summary register of the
              status model for node 37.
            - ``.NODE38``: B9. This attribute manages the TSP-Link system summary register of the
              status model for node 38.
            - ``.NODE39``: B10. This attribute manages the TSP-Link system summary register of the
              status model for node 39.
            - ``.NODE40``: B11. This attribute manages the TSP-Link system summary register of the
              status model for node 40.
            - ``.NODE41``: B12. This attribute manages the TSP-Link system summary register of the
              status model for node 41.
            - ``.NODE42``: B13. This attribute manages the TSP-Link system summary register of the
              status model for node 42.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.system3.condition`` attribute.
            - ``.enable``: The ``status.system3.enable`` attribute.
            - ``.event``: The ``status.system3.event`` attribute.
            - ``.ntr``: The ``status.system3.ntr`` attribute.
            - ``.ptr``: The ``status.system3.ptr`` attribute.
        """
        return self._system3

    @property
    def system4(self) -> StatusSystem4:
        """Return the ``status.system4`` command tree.

        Constants:
            - ``.EXT``: B0. This attributes manages the TSP-Link system summary register of the
              status model for nodes 43 through 56.
            - ``.EXTENSION_BIT``: B0. This attributes manages the TSP-Link system summary register
              of the status model for nodes 43 through 56.
            - ``.NODE43``: B1. This attributes manages the TSP-Link system summary register of the
              status model for node 43.
            - ``.NODE44``: B2. This attributes manages the TSP-Link system summary register of the
              status model for node 44.
            - ``.NODE45``: B3. This attributes manages the TSP-Link system summary register of the
              status model for node 45.
            - ``.NODE46``: B4. This attributes manages the TSP-Link system summary register of the
              status model for node 46.
            - ``.NODE47``: B5. This attributes manages the TSP-Link system summary register of the
              status model for node 47.
            - ``.NODE48``: B6. This attributes manages the TSP-Link system summary register of the
              status model for node 48.
            - ``.NODE49``: B7. This attributes manages the TSP-Link system summary register of the
              status model for node 49.
            - ``.NODE50``: B8. This attributes manages the TSP-Link system summary register of the
              status model for node 50.
            - ``.NODE51``: B9. This attributes manages the TSP-Link system summary register of the
              status model for node 51.
            - ``.NODE52``: B10. This attributes manages the TSP-Link system summary register of the
              status model for node 52.
            - ``.NODE53``: B11. This attributes manages the TSP-Link system summary register of the
              status model for node 53.
            - ``.NODE54``: B12. This attributes manages the TSP-Link system summary register of the
              status model for node 54.
            - ``.NODE55``: B13. This attributes manages the TSP-Link system summary register of the
              status model for node 55.
            - ``.NODE56``: B14. This attributes manages the TSP-Link system summary register of the
              status model for node 56.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.system4.condition`` attribute.
            - ``.enable``: The ``status.system4.enable`` attribute.
            - ``.event``: The ``status.system4.event`` attribute.
            - ``.ntr``: The ``status.system4.ntr`` attribute.
            - ``.ptr``: The ``status.system4.ptr`` attribute.
        """
        return self._system4

    @property
    def system5(self) -> StatusSystem5:
        """Return the ``status.system5`` command tree.

        Constants:
            - ``.NODE57``: B1. This attributes manages the TSP-Link system summary register of the
              status model for node.
            - ``.NODE58``: B2. This attributes manages the TSP-Link system summary register of the
              status model for node.
            - ``.NODE59``: B3. This attributes manages the TSP-Link system summary register of the
              status model for node.
            - ``.NODE60``: B4. This attributes manages the TSP-Link system summary register of the
              status model for node.
            - ``.NODE61``: B5. This attributes manages the TSP-Link system summary register of the
              status model for node.
            - ``.NODE62``: B6. This attributes manages the TSP-Link system summary register of the
              status model for node.
            - ``.NODE63``: B7. This attributes manages the TSP-Link system summary register of the
              status model for node.
            - ``.NODE64``: B8. This attributes manages the TSP-Link system summary register of the
              status model for node.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.system5.condition`` attribute.
            - ``.enable``: The ``status.system5.enable`` attribute.
            - ``.event``: The ``status.system5.event`` attribute.
            - ``.ntr``: The ``status.system5.ntr`` attribute.
            - ``.ptr``: The ``status.system5.ptr`` attribute.
        """
        return self._system5

    def reset(self) -> None:
        """Run the ``status.reset()`` function.

        Description:
            - This function resets all bits in the status model.

        TSP Syntax:
            ```
            - status.reset()
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
