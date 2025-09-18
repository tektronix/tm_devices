# pyright: reportConstantRedefinition=none
"""The status commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - status.condition
    - status.node_enable
    - status.node_event
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
    - status.operation.instrument.digio.trigger_overrun[2].condition
    - status.operation.instrument.digio.trigger_overrun[2].enable
    - status.operation.instrument.digio.trigger_overrun[2].event
    - status.operation.instrument.digio.trigger_overrun[2].ntr
    - status.operation.instrument.digio.trigger_overrun[2].ptr
    - status.operation.instrument.enable
    - status.operation.instrument.event
    - status.operation.instrument.lan.condition
    - status.operation.instrument.lan.enable
    - status.operation.instrument.lan.event
    - status.operation.instrument.lan.ntr
    - status.operation.instrument.lan.ptr
    - status.operation.instrument.ntr
    - status.operation.instrument.ptr
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
    - status.operation.ntr
    - status.operation.program.condition
    - status.operation.program.enable
    - status.operation.program.event
    - status.operation.program.ntr
    - status.operation.program.ptr
    - status.operation.ptr
    - status.operation.remote.condition
    - status.operation.remote.enable
    - status.operation.remote.event
    - status.operation.remote.ntr
    - status.operation.remote.ptr
    - status.operation.slot.presence.condition
    - status.operation.slot.presence.enable
    - status.operation.slot.presence.event
    - status.operation.slot.presence.ntr
    - status.operation.slot.presence.ptr
    - status.operation.slot.status.condition
    - status.operation.slot.status.enable
    - status.operation.slot.status.event
    - status.operation.slot.status.ntr
    - status.operation.slot.status.ptr
    - status.operation.slot.summary.condition
    - status.operation.slot.summary.enable
    - status.operation.slot.summary.event
    - status.operation.slot.summary.ntr
    - status.operation.slot.summary.ptr
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
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class StatusSystem5(BaseTSPCmd):
    """The ``status.system5`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.system5.condition`` attribute.
        - ``.enable``: The ``status.system5.enable`` attribute.
        - ``.event``: The ``status.system5.event`` attribute.
        - ``.ntr``: The ``status.system5.ntr`` attribute.
        - ``.ptr``: The ``status.system5.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.system5.condition`` attribute.

        Description:
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 57 through 64.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 57 through 64.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 57 through 64.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 57 through 64.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 57 through 64.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 57 through 64.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 57 through 64.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 57 through 64.

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

    Properties and methods:
        - ``.condition``: The ``status.system4.condition`` attribute.
        - ``.enable``: The ``status.system4.enable`` attribute.
        - ``.event``: The ``status.system4.event`` attribute.
        - ``.ntr``: The ``status.system4.ntr`` attribute.
        - ``.ptr``: The ``status.system4.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.system4.condition`` attribute.

        Description:
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 43 through 56.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 43 through 56.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 43 through 56.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 43 through 56.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 43 through 56.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 43 through 56.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 43 through 56.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 43 through 56.

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

    Properties and methods:
        - ``.condition``: The ``status.system3.condition`` attribute.
        - ``.enable``: The ``status.system3.enable`` attribute.
        - ``.event``: The ``status.system3.event`` attribute.
        - ``.ntr``: The ``status.system3.ntr`` attribute.
        - ``.ptr``: The ``status.system3.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.system3.condition`` attribute.

        Description:
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 29 through 42.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 29 through 42.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 29 through 42.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 29 through 42.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 29 through 42.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 29 through 42.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 29 through 42.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 29 through 42.

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

    Properties and methods:
        - ``.condition``: The ``status.system2.condition`` attribute.
        - ``.enable``: The ``status.system2.enable`` attribute.
        - ``.event``: The ``status.system2.event`` attribute.
        - ``.ntr``: The ``status.system2.ntr`` attribute.
        - ``.ptr``: The ``status.system2.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.system2.condition`` attribute.

        Description:
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 15 through 28.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 15 through 28.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 15 through 28.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 15 through 28.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 15 through 28.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 15 through 28.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 15 through 28.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 15 through 28.

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

    Properties and methods:
        - ``.condition``: The ``status.system.condition`` attribute.
        - ``.enable``: The ``status.system.enable`` attribute.
        - ``.event``: The ``status.system.event`` attribute.
        - ``.ntr``: The ``status.system.ntr`` attribute.
        - ``.ptr``: The ``status.system.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.system.condition`` attribute.

        Description:
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 1 through 14.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 1 through 14.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 1 through 14.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 1 through 14.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 1 through 14.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 1 through 14.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 1 through 14.

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
            - These attributes manage the TSP-LinkTM system summary register of the status model for
              nodes 1 through 14.

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
    """The ``status.standard`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.standard.condition`` attribute.
        - ``.enable``: The ``status.standard.enable`` attribute.
        - ``.event``: The ``status.standard.event`` attribute.
        - ``.ntr``: The ``status.standard.ntr`` attribute.
        - ``.ptr``: The ``status.standard.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.standard.condition`` attribute.

        Description:
            - These attributes manage the Standard Event Status register set of the status model.

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
            - These attributes manage the Standard Event Status register set of the status model.

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
            - These attributes manage the Standard Event Status register set of the status model.

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
            - These attributes manage the Standard Event Status register set of the status model.

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
            - These attributes manage the Standard Event Status register set of the status model.

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
            - These attributes manage the Standard Event Status register set of the status model.

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
            - These attributes manage the Standard Event Status register set of the status model.

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
            - These attributes manage the Standard Event Status register set of the status model.

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


class StatusOperationUser(BaseTSPCmd):
    """The ``status.operation.user`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.user.condition`` attribute.
        - ``.enable``: The ``status.operation.user.enable`` attribute.
        - ``.event``: The ``status.operation.user.event`` attribute.
        - ``.ntr``: The ``status.operation.user.ntr`` attribute.
        - ``.ptr``: The ``status.operation.user.ptr`` attribute.
    """

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

    Properties and methods:
        - ``.condition``: The ``status.operation.trigger_overrun.condition`` attribute.
        - ``.enable``: The ``status.operation.trigger_overrun.enable`` attribute.
        - ``.event``: The ``status.operation.trigger_overrun.event`` attribute.
        - ``.ntr``: The ``status.operation.trigger_overrun.ntr`` attribute.
        - ``.ptr``: The ``status.operation.trigger_overrun.ptr`` attribute.
    """

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


class StatusOperationSlotSummary(BaseTSPCmd):
    """The ``status.operation.slot.summary`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.slot.summary.condition`` attribute.
        - ``.enable``: The ``status.operation.slot.summary.enable`` attribute.
        - ``.event``: The ``status.operation.slot.summary.event`` attribute.
        - ``.ntr``: The ``status.operation.slot.summary.ntr`` attribute.
        - ``.ptr``: The ``status.operation.slot.summary.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.slot.summary.condition`` attribute.

        Description:
            - This attribute contains the Slot Summary Register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.slot.summary.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.slot.summary.condition)
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
        """Access the ``status.operation.slot.summary.enable`` attribute.

        Description:
            - This attribute contains the Slot Summary Register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.summary.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.summary.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.summary.enable = value
            - print(status.operation.slot.summary.enable)
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
        """Access the ``status.operation.slot.summary.enable`` attribute.

        Description:
            - This attribute contains the Slot Summary Register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.summary.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.summary.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.summary.enable = value
            - print(status.operation.slot.summary.enable)
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
        """Access the ``status.operation.slot.summary.event`` attribute.

        Description:
            - This attribute contains the Slot Summary Register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.summary.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.slot.summary.event)
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
        """Access the ``status.operation.slot.summary.ntr`` attribute.

        Description:
            - This attribute contains the Slot Summary Register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.summary.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.summary.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.summary.ntr = value
            - print(status.operation.slot.summary.ntr)
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
        """Access the ``status.operation.slot.summary.ntr`` attribute.

        Description:
            - This attribute contains the Slot Summary Register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.summary.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.summary.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.summary.ntr = value
            - print(status.operation.slot.summary.ntr)
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
        """Access the ``status.operation.slot.summary.ptr`` attribute.

        Description:
            - This attribute contains the Slot Summary Register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.summary.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.summary.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.summary.ptr = value
            - print(status.operation.slot.summary.ptr)
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
        """Access the ``status.operation.slot.summary.ptr`` attribute.

        Description:
            - This attribute contains the Slot Summary Register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.summary.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.summary.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.summary.ptr = value
            - print(status.operation.slot.summary.ptr)
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


class StatusOperationSlotStatus(BaseTSPCmd):
    """The ``status.operation.slot.status`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.slot.status.condition`` attribute.
        - ``.enable``: The ``status.operation.slot.status.enable`` attribute.
        - ``.event``: The ``status.operation.slot.status.event`` attribute.
        - ``.ntr``: The ``status.operation.slot.status.ntr`` attribute.
        - ``.ptr``: The ``status.operation.slot.status.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.slot.status.condition`` attribute.

        Description:
            - This attribute contains the operation Slot Status register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.slot.status.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.slot.status.condition)
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
        """Access the ``status.operation.slot.status.enable`` attribute.

        Description:
            - This attribute contains the operation Slot Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.status.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.status.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.status.enable = value
            - print(status.operation.slot.status.enable)
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
        """Access the ``status.operation.slot.status.enable`` attribute.

        Description:
            - This attribute contains the operation Slot Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.status.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.status.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.status.enable = value
            - print(status.operation.slot.status.enable)
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
        """Access the ``status.operation.slot.status.event`` attribute.

        Description:
            - This attribute contains the operation Slot Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.status.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.slot.status.event)
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
        """Access the ``status.operation.slot.status.ntr`` attribute.

        Description:
            - This attribute contains the operation Slot Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.status.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.status.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.status.ntr = value
            - print(status.operation.slot.status.ntr)
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
        """Access the ``status.operation.slot.status.ntr`` attribute.

        Description:
            - This attribute contains the operation Slot Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.status.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.status.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.status.ntr = value
            - print(status.operation.slot.status.ntr)
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
        """Access the ``status.operation.slot.status.ptr`` attribute.

        Description:
            - This attribute contains the operation Slot Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.status.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.status.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.status.ptr = value
            - print(status.operation.slot.status.ptr)
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
        """Access the ``status.operation.slot.status.ptr`` attribute.

        Description:
            - This attribute contains the operation Slot Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.status.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.status.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.status.ptr = value
            - print(status.operation.slot.status.ptr)
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


class StatusOperationSlotPresence(BaseTSPCmd):
    """The ``status.operation.slot.presence`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.slot.presence.condition`` attribute.
        - ``.enable``: The ``status.operation.slot.presence.enable`` attribute.
        - ``.event``: The ``status.operation.slot.presence.event`` attribute.
        - ``.ntr``: The ``status.operation.slot.presence.ntr`` attribute.
        - ``.ptr``: The ``status.operation.slot.presence.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.slot.presence.condition`` attribute.

        Description:
            - This attribute contains the operation status hardware presence register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.slot.presence.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.slot.presence.condition)
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
        """Access the ``status.operation.slot.presence.enable`` attribute.

        Description:
            - This attribute contains the operation status hardware presence register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.presence.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.presence.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.presence.enable = value
            - print(status.operation.slot.presence.enable)
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
        """Access the ``status.operation.slot.presence.enable`` attribute.

        Description:
            - This attribute contains the operation status hardware presence register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.presence.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.presence.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.presence.enable = value
            - print(status.operation.slot.presence.enable)
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
        """Access the ``status.operation.slot.presence.event`` attribute.

        Description:
            - This attribute contains the operation status hardware presence register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.presence.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.slot.presence.event)
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
        """Access the ``status.operation.slot.presence.ntr`` attribute.

        Description:
            - This attribute contains the operation status hardware presence register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.presence.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.presence.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.presence.ntr = value
            - print(status.operation.slot.presence.ntr)
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
        """Access the ``status.operation.slot.presence.ntr`` attribute.

        Description:
            - This attribute contains the operation status hardware presence register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.presence.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.presence.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.presence.ntr = value
            - print(status.operation.slot.presence.ntr)
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
        """Access the ``status.operation.slot.presence.ptr`` attribute.

        Description:
            - This attribute contains the operation status hardware presence register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.presence.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.presence.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.presence.ptr = value
            - print(status.operation.slot.presence.ptr)
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
        """Access the ``status.operation.slot.presence.ptr`` attribute.

        Description:
            - This attribute contains the operation status hardware presence register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.slot.presence.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.slot.presence.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.slot.presence.ptr = value
            - print(status.operation.slot.presence.ptr)
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


class StatusOperationSlot(BaseTSPCmd):
    """The ``status.operation.slot`` command tree.

    Properties and methods:
        - ``.presence``: The ``status.operation.slot.presence`` command tree.
        - ``.status``: The ``status.operation.slot.status`` command tree.
        - ``.summary``: The ``status.operation.slot.summary`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._presence = StatusOperationSlotPresence(device, f"{self._cmd_syntax}.presence")
        self._status = StatusOperationSlotStatus(device, f"{self._cmd_syntax}.status")
        self._summary = StatusOperationSlotSummary(device, f"{self._cmd_syntax}.summary")

    @property
    def presence(self) -> StatusOperationSlotPresence:
        """Return the ``status.operation.slot.presence`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.slot.presence.condition`` attribute.
            - ``.enable``: The ``status.operation.slot.presence.enable`` attribute.
            - ``.event``: The ``status.operation.slot.presence.event`` attribute.
            - ``.ntr``: The ``status.operation.slot.presence.ntr`` attribute.
            - ``.ptr``: The ``status.operation.slot.presence.ptr`` attribute.
        """
        return self._presence

    @property
    def status(self) -> StatusOperationSlotStatus:
        """Return the ``status.operation.slot.status`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.slot.status.condition`` attribute.
            - ``.enable``: The ``status.operation.slot.status.enable`` attribute.
            - ``.event``: The ``status.operation.slot.status.event`` attribute.
            - ``.ntr``: The ``status.operation.slot.status.ntr`` attribute.
            - ``.ptr``: The ``status.operation.slot.status.ptr`` attribute.
        """
        return self._status

    @property
    def summary(self) -> StatusOperationSlotSummary:
        """Return the ``status.operation.slot.summary`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.slot.summary.condition`` attribute.
            - ``.enable``: The ``status.operation.slot.summary.enable`` attribute.
            - ``.event``: The ``status.operation.slot.summary.event`` attribute.
            - ``.ntr``: The ``status.operation.slot.summary.ntr`` attribute.
            - ``.ptr``: The ``status.operation.slot.summary.ptr`` attribute.
        """
        return self._summary


class StatusOperationRemote(BaseTSPCmd):
    """The ``status.operation.remote`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.remote.condition`` attribute.
        - ``.enable``: The ``status.operation.remote.enable`` attribute.
        - ``.event``: The ``status.operation.remote.event`` attribute.
        - ``.ntr``: The ``status.operation.remote.ntr`` attribute.
        - ``.ptr``: The ``status.operation.remote.ptr`` attribute.
    """

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


class StatusOperationProgram(BaseTSPCmd):
    """The ``status.operation.program`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.program.condition`` attribute.
        - ``.enable``: The ``status.operation.program.enable`` attribute.
        - ``.event``: The ``status.operation.program.event`` attribute.
        - ``.ntr``: The ``status.operation.program.ntr`` attribute.
        - ``.ptr``: The ``status.operation.program.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.program.condition`` attribute.

        Description:
            - This attribute contains the Operation Status Program Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.program.condition)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.program.condition)
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
        """Access the ``status.operation.program.enable`` attribute.

        Description:
            - This attribute contains the Operation Status Program Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.program.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.program.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.program.enable = value
            - print(status.operation.program.enable)
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
        """Access the ``status.operation.program.enable`` attribute.

        Description:
            - This attribute contains the Operation Status Program Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.program.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.program.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.program.enable = value
            - print(status.operation.program.enable)
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
        """Access the ``status.operation.program.event`` attribute.

        Description:
            - This attribute contains the Operation Status Program Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.program.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.program.event)
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
        """Access the ``status.operation.program.ntr`` attribute.

        Description:
            - This attribute contains the Operation Status Program Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.program.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.program.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.program.ntr = value
            - print(status.operation.program.ntr)
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
        """Access the ``status.operation.program.ntr`` attribute.

        Description:
            - This attribute contains the Operation Status Program Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.program.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.program.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.program.ntr = value
            - print(status.operation.program.ntr)
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
        """Access the ``status.operation.program.ptr`` attribute.

        Description:
            - This attribute contains the Operation Status Program Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.program.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.program.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.program.ptr = value
            - print(status.operation.program.ptr)
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
        """Access the ``status.operation.program.ptr`` attribute.

        Description:
            - This attribute contains the Operation Status Program Status register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.program.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.program.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.program.ptr = value
            - print(status.operation.program.ptr)
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

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.tsplink.trigger_overrun.condition``
          attribute.
        - ``.enable``: The ``status.operation.instrument.tsplink.trigger_overrun.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.tsplink.trigger_overrun.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.tsplink.trigger_overrun.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.tsplink.trigger_overrun.ptr`` attribute.
    """

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

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.tsplink.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.tsplink.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.tsplink.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.tsplink.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.tsplink.ptr`` attribute.
        - ``.trigger_overrun``: The ``status.operation.instrument.tsplink.trigger_overrun`` command
          tree.
    """

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

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.trigger_timer.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.trigger_timer.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.trigger_timer.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.trigger_timer.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.trigger_timer.ptr`` attribute.
        - ``.trigger_overrun``: The ``status.operation.instrument.trigger_timer.trigger_overrun``
          command tree.
    """

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


class StatusOperationInstrumentLan(BaseTSPCmd):
    """The ``status.operation.instrument.lan`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.lan.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.lan.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.lan.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.lan.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.lan.ptr`` attribute.
    """

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


class StatusOperationInstrumentDigioTriggerOverrunItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``status.operation.instrument.digio.trigger_overrun[2]`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.digio.trigger_overrun[2].condition``
          attribute.
        - ``.enable``: The ``status.operation.instrument.digio.trigger_overrun[2].enable``
          attribute.
        - ``.event``: The ``status.operation.instrument.digio.trigger_overrun[2].event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.digio.trigger_overrun[2].ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.digio.trigger_overrun[2].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.digio.trigger_overrun[2].condition`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set for
              lines 15 through 18.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun[2].condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.digio.trigger_overrun[2].condition)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun[2].enable`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set for
              lines 15 through 18.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun[2].enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun[2].enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun[2].enable = value
            - print(status.operation.instrument.digio.trigger_overrun[2].enable)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun[2].enable`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set for
              lines 15 through 18.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun[2].enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun[2].enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun[2].enable = value
            - print(status.operation.instrument.digio.trigger_overrun[2].enable)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun[2].event`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set for
              lines 15 through 18.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun[2].event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.digio.trigger_overrun[2].event)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun[2].ntr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set for
              lines 15 through 18.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun[2].ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun[2].ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun[2].ntr = value
            - print(status.operation.instrument.digio.trigger_overrun[2].ntr)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun[2].ntr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set for
              lines 15 through 18.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun[2].ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun[2].ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun[2].ntr = value
            - print(status.operation.instrument.digio.trigger_overrun[2].ntr)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun[2].ptr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set for
              lines 15 through 18.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun[2].ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun[2].ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun[2].ptr = value
            - print(status.operation.instrument.digio.trigger_overrun[2].ptr)
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
        """Access the ``status.operation.instrument.digio.trigger_overrun[2].ptr`` attribute.

        Description:
            - This attribute contains the operation status digital I/O overrun register set for
              lines 15 through 18.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.digio.trigger_overrun[2].ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.digio.trigger_overrun[2].ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.digio.trigger_overrun[2].ptr = value
            - print(status.operation.instrument.digio.trigger_overrun[2].ptr)
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


class StatusOperationInstrumentDigioTriggerOverrun(BaseTSPCmd):
    """The ``status.operation.instrument.digio.trigger_overrun`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.digio.trigger_overrun.condition``
          attribute.
        - ``.enable``: The ``status.operation.instrument.digio.trigger_overrun.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.digio.trigger_overrun.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.digio.trigger_overrun.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.digio.trigger_overrun.ptr`` attribute.
    """

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

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.digio.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.digio.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.digio.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.digio.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.digio.ptr`` attribute.
        - ``.trigger_overrun``: The ``status.operation.instrument.digio.trigger_overrun`` command
          tree.
        - ``.trigger_overrunx``: The ``status.operation.instrument.digio.trigger_overrun[2]``
          command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._trigger_overrun = StatusOperationInstrumentDigioTriggerOverrun(
            device, f"{self._cmd_syntax}.trigger_overrun"
        )
        self._trigger_overrunx: Dict[int, StatusOperationInstrumentDigioTriggerOverrunItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: StatusOperationInstrumentDigioTriggerOverrunItem(
                    device, f"{self._cmd_syntax}.trigger_overrun[{x}]"
                )
            )
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

    @property
    def trigger_overrunx(self) -> Dict[int, StatusOperationInstrumentDigioTriggerOverrunItem]:
        """Return the ``status.operation.instrument.digio.trigger_overrun[2]`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.digio.trigger_overrun[2].condition``
              attribute.
            - ``.enable``: The ``status.operation.instrument.digio.trigger_overrun[2].enable``
              attribute.
            - ``.event``: The ``status.operation.instrument.digio.trigger_overrun[2].event``
              attribute.
            - ``.ntr``: The ``status.operation.instrument.digio.trigger_overrun[2].ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.digio.trigger_overrun[2].ptr`` attribute.
        """
        return self._trigger_overrunx


class StatusOperationInstrument(BaseTSPCmd):
    """The ``status.operation.instrument`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.condition`` attribute.
        - ``.digio``: The ``status.operation.instrument.digio`` command tree.
        - ``.enable``: The ``status.operation.instrument.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.event`` attribute.
        - ``.lan``: The ``status.operation.instrument.lan`` command tree.
        - ``.ntr``: The ``status.operation.instrument.ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.ptr`` attribute.
        - ``.trigger_timer``: The ``status.operation.instrument.trigger_timer`` command tree.
        - ``.tsplink``: The ``status.operation.instrument.tsplink`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._digio = StatusOperationInstrumentDigio(device, f"{self._cmd_syntax}.digio")
        self._lan = StatusOperationInstrumentLan(device, f"{self._cmd_syntax}.lan")
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

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.digio.condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.digio.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.digio.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.digio.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.digio.ptr`` attribute.
            - ``.trigger_overrun``: The ``status.operation.instrument.digio.trigger_overrun``
              command tree.
            - ``.trigger_overrunx``: The ``status.operation.instrument.digio.trigger_overrun[2]``
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

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.lan.condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.lan.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.lan.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.lan.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.lan.ptr`` attribute.
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
    def trigger_timer(self) -> StatusOperationInstrumentTriggerTimer:
        """Return the ``status.operation.instrument.trigger_timer`` command tree.

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


class StatusOperation(BaseTSPCmd):
    """The ``status.operation`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.condition`` attribute.
        - ``.enable``: The ``status.operation.enable`` attribute.
        - ``.event``: The ``status.operation.event`` attribute.
        - ``.instrument``: The ``status.operation.instrument`` command tree.
        - ``.ntr``: The ``status.operation.ntr`` attribute.
        - ``.program``: The ``status.operation.program`` command tree.
        - ``.ptr``: The ``status.operation.ptr`` attribute.
        - ``.remote``: The ``status.operation.remote`` command tree.
        - ``.slot``: The ``status.operation.slot`` command tree.
        - ``.trigger_overrun``: The ``status.operation.trigger_overrun`` command tree.
        - ``.user``: The ``status.operation.user`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._instrument = StatusOperationInstrument(device, f"{self._cmd_syntax}.instrument")
        self._program = StatusOperationProgram(device, f"{self._cmd_syntax}.program")
        self._remote = StatusOperationRemote(device, f"{self._cmd_syntax}.remote")
        self._slot = StatusOperationSlot(device, f"{self._cmd_syntax}.slot")
        self._trigger_overrun = StatusOperationTriggerOverrun(
            device, f"{self._cmd_syntax}.trigger_overrun"
        )
        self._user = StatusOperationUser(device, f"{self._cmd_syntax}.user")

    @property
    def condition(self) -> str:
        """Access the ``status.operation.condition`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

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
            - These attributes manage the Operation Status Register set of the status model.

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
            - These attributes manage the Operation Status Register set of the status model.

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
            - These attributes manage the Operation Status Register set of the status model.

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

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.condition`` attribute.
            - ``.digio``: The ``status.operation.instrument.digio`` command tree.
            - ``.enable``: The ``status.operation.instrument.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.event`` attribute.
            - ``.lan``: The ``status.operation.instrument.lan`` command tree.
            - ``.ntr``: The ``status.operation.instrument.ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.ptr`` attribute.
            - ``.trigger_timer``: The ``status.operation.instrument.trigger_timer`` command tree.
            - ``.tsplink``: The ``status.operation.instrument.tsplink`` command tree.
        """
        return self._instrument

    @property
    def ntr(self) -> str:
        """Access the ``status.operation.ntr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

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
            - These attributes manage the Operation Status Register set of the status model.

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
    def program(self) -> StatusOperationProgram:
        """Return the ``status.operation.program`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.program.condition`` attribute.
            - ``.enable``: The ``status.operation.program.enable`` attribute.
            - ``.event``: The ``status.operation.program.event`` attribute.
            - ``.ntr``: The ``status.operation.program.ntr`` attribute.
            - ``.ptr``: The ``status.operation.program.ptr`` attribute.
        """
        return self._program

    @property
    def ptr(self) -> str:
        """Access the ``status.operation.ptr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

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
            - These attributes manage the Operation Status Register set of the status model.

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

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.remote.condition`` attribute.
            - ``.enable``: The ``status.operation.remote.enable`` attribute.
            - ``.event``: The ``status.operation.remote.event`` attribute.
            - ``.ntr``: The ``status.operation.remote.ntr`` attribute.
            - ``.ptr``: The ``status.operation.remote.ptr`` attribute.
        """
        return self._remote

    @property
    def slot(self) -> StatusOperationSlot:
        """Return the ``status.operation.slot`` command tree.

        Sub-properties and sub-methods:
            - ``.presence``: The ``status.operation.slot.presence`` command tree.
            - ``.status``: The ``status.operation.slot.status`` command tree.
            - ``.summary``: The ``status.operation.slot.summary`` command tree.
        """
        return self._slot

    @property
    def trigger_overrun(self) -> StatusOperationTriggerOverrun:
        """Return the ``status.operation.trigger_overrun`` command tree.

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

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.user.condition`` attribute.
            - ``.enable``: The ``status.operation.user.enable`` attribute.
            - ``.event``: The ``status.operation.user.event`` attribute.
            - ``.ntr``: The ``status.operation.user.ntr`` attribute.
            - ``.ptr``: The ``status.operation.user.ptr`` attribute.
        """
        return self._user


class Status(BaseTSPCmd):
    """The ``status`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.condition`` attribute.
        - ``.node_enable``: The ``status.node_enable`` attribute.
        - ``.node_event``: The ``status.node_event`` attribute.
        - ``.operation``: The ``status.operation`` command tree.
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

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "status") -> None:
        super().__init__(device, cmd_syntax)
        self._operation = StatusOperation(device, f"{self._cmd_syntax}.operation")
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
            - This attribute stores the condition of the status byte register.

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

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.condition`` attribute.
            - ``.enable``: The ``status.operation.enable`` attribute.
            - ``.event``: The ``status.operation.event`` attribute.
            - ``.instrument``: The ``status.operation.instrument`` command tree.
            - ``.ntr``: The ``status.operation.ntr`` attribute.
            - ``.program``: The ``status.operation.program`` command tree.
            - ``.ptr``: The ``status.operation.ptr`` attribute.
            - ``.remote``: The ``status.operation.remote`` command tree.
            - ``.slot``: The ``status.operation.slot`` command tree.
            - ``.trigger_overrun``: The ``status.operation.trigger_overrun`` command tree.
            - ``.user``: The ``status.operation.user`` command tree.
        """
        return self._operation

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
        """Return the ``status.standard`` command tree.

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
            - This function resets all bits in the mainframe status model.

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
