# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The status commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - status.condition
    - status.measurement.condition
    - status.measurement.enable
    - status.measurement.event
    - status.measurement.ntr
    - status.measurement.ptr
    - status.node_enable
    - status.node_event
    - status.operation.condition
    - status.operation.enable
    - status.operation.event
    - status.operation.ntr
    - status.operation.ptr
    - status.operation.user.condition
    - status.operation.user.enable
    - status.operation.user.event
    - status.operation.user.ntr
    - status.operation.user.ptr
    - status.questionable.condition
    - status.questionable.enable
    - status.questionable.event
    - status.questionable.ntr
    - status.questionable.ptr
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

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

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


class StatusQuestionable(BaseTSPCmd):
    """The ``status.questionable`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.questionable.condition`` attribute.
        - ``.enable``: The ``status.questionable.enable`` attribute.
        - ``.event``: The ``status.questionable.event`` attribute.
        - ``.ntr``: The ``status.questionable.ntr`` attribute.
        - ``.ptr``: The ``status.questionable.ptr`` attribute.
    """

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


class StatusOperation(BaseTSPCmd):
    """The ``status.operation`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.condition`` attribute.
        - ``.enable``: The ``status.operation.enable`` attribute.
        - ``.event``: The ``status.operation.event`` attribute.
        - ``.ntr``: The ``status.operation.ntr`` attribute.
        - ``.ptr``: The ``status.operation.ptr`` attribute.
        - ``.user``: The ``status.operation.user`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._user = StatusOperationUser(device, f"{self._cmd_syntax}.user")

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


class StatusMeasurement(BaseTSPCmd):
    """The ``status.measurement`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.measurement.condition`` attribute.
        - ``.enable``: The ``status.measurement.enable`` attribute.
        - ``.event``: The ``status.measurement.event`` attribute.
        - ``.ntr``: The ``status.measurement.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.condition`` attribute.

        Description:
            - These attributes contain the measurement event register set.

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
    def enable(self) -> str:
        """Access the ``status.measurement.enable`` attribute.

        Description:
            - These attributes contain the measurement event register set.

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
            - These attributes contain the measurement event register set.

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
            - These attributes contain the measurement event register set.

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
    def ntr(self) -> str:
        """Access the ``status.measurement.ntr`` attribute.

        Description:
            - These attributes contain the measurement event register set.

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
            - These attributes contain the measurement event register set.

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
            - These attributes contain the measurement event register set.

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
            - These attributes contain the measurement event register set.

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


#  pylint: disable=too-many-instance-attributes
class Status(BaseTSPCmd):
    """The ``status`` command tree.

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

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.condition`` attribute.
            - ``.enable``: The ``status.measurement.enable`` attribute.
            - ``.event``: The ``status.measurement.event`` attribute.
            - ``.ntr``: The ``status.measurement.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.ptr`` attribute.
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

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.condition`` attribute.
            - ``.enable``: The ``status.operation.enable`` attribute.
            - ``.event``: The ``status.operation.event`` attribute.
            - ``.ntr``: The ``status.operation.ntr`` attribute.
            - ``.ptr``: The ``status.operation.ptr`` attribute.
            - ``.user``: The ``status.operation.user`` command tree.
        """
        return self._operation

    @property
    def questionable(self) -> StatusQuestionable:
        """Return the ``status.questionable`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.condition`` attribute.
            - ``.enable``: The ``status.questionable.enable`` attribute.
            - ``.event``: The ``status.questionable.event`` attribute.
            - ``.ntr``: The ``status.questionable.ntr`` attribute.
            - ``.ptr``: The ``status.questionable.ptr`` attribute.
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
