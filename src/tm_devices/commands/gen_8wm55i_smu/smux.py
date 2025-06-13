# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The smux commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - smuX.abort()
    - smuX.buffer.getstats()
    - smuX.buffer.recalculatestats()
    - smuX.cal.adjustdate
    - smuX.cal.date
    - smuX.cal.due
    - smuX.cal.lock()
    - smuX.cal.password
    - smuX.cal.polarity
    - smuX.cal.restore()
    - smuX.cal.save()
    - smuX.cal.state
    - smuX.cal.unlock()
    - smuX.contact.calibratehi()
    - smuX.contact.calibratelo()
    - smuX.contact.check()
    - smuX.contact.r()
    - smuX.contact.speed
    - smuX.contact.threshold
    - smuX.makebuffer()
    - smuX.measure.Y()
    - smuX.measure.analogfilter
    - smuX.measure.autorangei
    - smuX.measure.autorangev
    - smuX.measure.autozero
    - smuX.measure.calibrateY()
    - smuX.measure.count
    - smuX.measure.delay
    - smuX.measure.delayfactor
    - smuX.measure.filter.count
    - smuX.measure.filter.enable
    - smuX.measure.filter.type
    - smuX.measure.highcrangedelayfactor
    - smuX.measure.interval
    - smuX.measure.lowrangei
    - smuX.measure.lowrangev
    - smuX.measure.nplc
    - smuX.measure.overlappedY()
    - smuX.measure.rangei
    - smuX.measure.rangev
    - smuX.measure.rel.enablei
    - smuX.measure.rel.enablep
    - smuX.measure.rel.enabler
    - smuX.measure.rel.enablev
    - smuX.measure.rel.leveli
    - smuX.measure.rel.levelp
    - smuX.measure.rel.levelr
    - smuX.measure.rel.levelv
    - smuX.measureYandstep()
    - smuX.nvbuffer1
    - smuX.nvbuffer2
    - smuX.reset()
    - smuX.savebuffer()
    - smuX.sense
    - smuX.source.autorangei
    - smuX.source.autorangev
    - smuX.source.calibrateY()
    - smuX.source.compliance
    - smuX.source.delay
    - smuX.source.func
    - smuX.source.highc
    - smuX.source.leveli
    - smuX.source.levelv
    - smuX.source.limiti
    - smuX.source.limitp
    - smuX.source.limitv
    - smuX.source.lowrangei
    - smuX.source.lowrangev
    - smuX.source.offfunc
    - smuX.source.offlimiti
    - smuX.source.offlimitv
    - smuX.source.offmode
    - smuX.source.output
    - smuX.source.outputenableaction
    - smuX.source.rangei
    - smuX.source.rangev
    - smuX.source.settling
    - smuX.source.sink
    - smuX.trigger.arm.count
    - smuX.trigger.arm.set()
    - smuX.trigger.arm.stimulus
    - smuX.trigger.autoclear
    - smuX.trigger.count
    - smuX.trigger.endpulse.action
    - smuX.trigger.endpulse.set()
    - smuX.trigger.endpulse.stimulus
    - smuX.trigger.endsweep.action
    - smuX.trigger.initiate()
    - smuX.trigger.measure.Y()
    - smuX.trigger.measure.action
    - smuX.trigger.measure.set()
    - smuX.trigger.measure.stimulus
    - smuX.trigger.source.action
    - smuX.trigger.source.limiti
    - smuX.trigger.source.limitv
    - smuX.trigger.source.linearY()
    - smuX.trigger.source.listY()
    - smuX.trigger.source.logY()
    - smuX.trigger.source.set()
    - smuX.trigger.source.stimulus
    ```
"""

from typing import Any, Dict, Optional, Sequence, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError, ValidatedChannel

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class SmuxItemTriggerSource(BaseTSPCmd):
    """The ``smuX.trigger.source`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.source.action
          applies to SMU channel A).

    Properties and methods:
        - ``.action``: The ``smuX.trigger.source.action`` attribute.
        - ``.limiti``: The ``smuX.trigger.source.limiti`` attribute.
        - ``.limitv``: The ``smuX.trigger.source.limitv`` attribute.
        - ``.lineari()``: The ``smuX.trigger.source.lineari()`` function.
        - ``.linearv()``: The ``smuX.trigger.source.linearv()`` function.
        - ``.listi()``: The ``smuX.trigger.source.listi()`` function.
        - ``.listv()``: The ``smuX.trigger.source.listv()`` function.
        - ``.logi()``: The ``smuX.trigger.source.logi()`` function.
        - ``.logv()``: The ``smuX.trigger.source.logv()`` function.
        - ``.set()``: The ``smuX.trigger.source.set()`` function.
        - ``.stimulus``: The ``smuX.trigger.source.stimulus`` attribute.
    """

    @property
    def action(self) -> str:
        """Access the ``smuX.trigger.source.action`` attribute.

        Description:
            - This attribute enables or disables sweeping the source (on or off).

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.source.action)`` query.
            - Setting this property to a value will send the ``smuX.trigger.source.action = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.source.action = value
            - print(smuX.trigger.source.action)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.source.action
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".action"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.action)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.action`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @action.setter
    def action(self, value: Union[str, float]) -> None:
        """Access the ``smuX.trigger.source.action`` attribute.

        Description:
            - This attribute enables or disables sweeping the source (on or off).

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.source.action)`` query.
            - Setting this property to a value will send the ``smuX.trigger.source.action = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.source.action = value
            - print(smuX.trigger.source.action)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.source.action
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".action", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.action = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.action`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limiti(self) -> str:
        """Access the ``smuX.trigger.source.limiti`` attribute.

        Description:
            - This attribute sets the sweep source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.source.limiti)`` query.
            - Setting this property to a value will send the ``smuX.trigger.source.limiti = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.source.limiti = value
            - print(smuX.trigger.source.limiti)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.source.limitv
              applies to SMU channel A).

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
        """Access the ``smuX.trigger.source.limiti`` attribute.

        Description:
            - This attribute sets the sweep source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.source.limiti)`` query.
            - Setting this property to a value will send the ``smuX.trigger.source.limiti = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.source.limiti = value
            - print(smuX.trigger.source.limiti)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.source.limitv
              applies to SMU channel A).

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
        """Access the ``smuX.trigger.source.limitv`` attribute.

        Description:
            - This attribute sets the sweep source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.source.limitv)`` query.
            - Setting this property to a value will send the ``smuX.trigger.source.limitv = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.source.limitv = value
            - print(smuX.trigger.source.limitv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.source.limitv
              applies to SMU channel A).

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
        """Access the ``smuX.trigger.source.limitv`` attribute.

        Description:
            - This attribute sets the sweep source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.source.limitv)`` query.
            - Setting this property to a value will send the ``smuX.trigger.source.limitv = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.source.limitv = value
            - print(smuX.trigger.source.limitv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.source.limitv
              applies to SMU channel A).

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
    def stimulus(self) -> str:
        """Access the ``smuX.trigger.source.stimulus`` attribute.

        Description:
            - This attribute defines which event causes the source event detector to enter the
              detected state.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.source.stimulus)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.source.stimulus = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.source.stimulus = value
            - print(smuX.trigger.source.stimulus)
            ```

        Info:
            - ``X``, the source-measure (SMU) channel (for example, smua.trigger.source.stimulus
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``smuX.trigger.source.stimulus`` attribute.

        Description:
            - This attribute defines which event causes the source event detector to enter the
              detected state.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.source.stimulus)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.source.stimulus = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.source.stimulus = value
            - print(smuX.trigger.source.stimulus)
            ```

        Info:
            - ``X``, the source-measure (SMU) channel (for example, smua.trigger.source.stimulus
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def lineari(self, start_value: float, end_value: float, points: int) -> None:
        """Run the ``smuX.trigger.source.lineari()`` function.

        Description:
            - This function configures a linear source sweep. (i = current in amperes)

        TSP Syntax:
            ```
            - smuX.trigger.source.lineari()
            ```

        Args:
            start_value: Source value of the first point.
            end_value: Source value of the last point.
            points: The number of points used to calculate the step size.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.lineari({start_value}, {end_value}, {points})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.lineari()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def linearv(self, start_value: float, end_value: float, points: int) -> None:
        """Run the ``smuX.trigger.source.linearv()`` function.

        Description:
            - This function configures a linear source sweep. (v = voltage in volts)

        TSP Syntax:
            ```
            - smuX.trigger.source.linearv()
            ```

        Args:
            start_value: Source value of the first point.
            end_value: Source value of the last point.
            points: The number of points used to calculate the step size.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.linearv({start_value}, {end_value}, {points})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.linearv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def listi(self, sweep_list: Sequence[Union[str, float]]) -> None:
        """Run the ``smuX.trigger.source.listi()`` function.

        Description:
            - This function configures an array-based source sweep. (i = current in amperes)

        TSP Syntax:
            ```
            - smuX.trigger.source.listi()
            ```

        Args:
            sweep_list: An array of source values.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.listi({{{', '.join([str(x) for x in sweep_list])}}})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.listi()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def listv(self, sweep_list: Sequence[Union[str, float]]) -> None:
        """Run the ``smuX.trigger.source.listv()`` function.

        Description:
            - This function configures an array-based source sweep. (v = voltage in volts)

        TSP Syntax:
            ```
            - smuX.trigger.source.listv()
            ```

        Args:
            sweep_list: An array of source values.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.listv({{{', '.join([str(x) for x in sweep_list])}}})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.listv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def logi(self, start_value: float, end_value: float, points: int, asymptote: str) -> None:
        """Run the ``smuX.trigger.source.logi()`` function.

        Description:
            - This function configures an exponential (geometric) source sweep. (i = current in
              amperes)

        TSP Syntax:
            ```
            - smuX.trigger.source.logi()
            ```

        Args:
            start_value: Source value of the first point.
            end_value: Source value of the last point.
            points: The number of points used to calculate the step size.
            asymptote: The asymptotic offset value.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.logi({start_value}, {end_value}, {points}, {asymptote})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.logi()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def logv(self, start_value: float, end_value: float, points: int, asymptote: str) -> None:
        """Run the ``smuX.trigger.source.logv()`` function.

        Description:
            - This function configures an exponential (geometric) source sweep. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - smuX.trigger.source.logv()
            ```

        Args:
            start_value: Source value of the first point.
            end_value: Source value of the last point.
            points: The number of points used to calculate the step size.
            asymptote: The asymptotic offset value.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.logv({start_value}, {end_value}, {points}, {asymptote})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.logv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def set_(self) -> None:
        """Run the ``smuX.trigger.source.set()`` function.

        Description:
            - This function sets the source event detector to the detected state.

        TSP Syntax:
            ```
            - smuX.trigger.source.set()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.source.set()
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.set()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuxItemTriggerMeasure(BaseTSPCmd):
    """The ``smuX.trigger.measure`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.measure.v()
          applies to SMU channel A).

    Properties and methods:
        - ``.i()``: The ``smuX.trigger.measure.i()`` function.
        - ``.iv()``: The ``smuX.trigger.measure.iv()`` function.
        - ``.p()``: The ``smuX.trigger.measure.p()`` function.
        - ``.r()``: The ``smuX.trigger.measure.r()`` function.
        - ``.v()``: The ``smuX.trigger.measure.v()`` function.
        - ``.action``: The ``smuX.trigger.measure.action`` attribute.
        - ``.set()``: The ``smuX.trigger.measure.set()`` function.
        - ``.stimulus``: The ``smuX.trigger.measure.stimulus`` attribute.
    """

    @property
    def action(self) -> str:
        """Access the ``smuX.trigger.measure.action`` attribute.

        Description:
            - This attribute controls measurement actions during a sweep.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.measure.action)`` query.
            - Setting this property to a value will send the ``smuX.trigger.measure.action = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.measure.action = value
            - print(smuX.trigger.measure.action)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.measure.action
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".action"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.action)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.action`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @action.setter
    def action(self, value: Union[str, float]) -> None:
        """Access the ``smuX.trigger.measure.action`` attribute.

        Description:
            - This attribute controls measurement actions during a sweep.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.measure.action)`` query.
            - Setting this property to a value will send the ``smuX.trigger.measure.action = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.measure.action = value
            - print(smuX.trigger.measure.action)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.measure.action
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".action", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.action = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.action`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``smuX.trigger.measure.stimulus`` attribute.

        Description:
            - This attribute selects the event that causes the measure event detector to enter the
              detected state.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.measure.stimulus)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.measure.stimulus = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.measure.stimulus = value
            - print(smuX.trigger.measure.stimulus)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.measure.stimulus applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``smuX.trigger.measure.stimulus`` attribute.

        Description:
            - This attribute selects the event that causes the measure event detector to enter the
              detected state.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.measure.stimulus)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.measure.stimulus = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.measure.stimulus = value
            - print(smuX.trigger.measure.stimulus)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.measure.stimulus applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def i(self, rbuffer: str) -> None:
        """Run the ``smuX.trigger.measure.i()`` function.

        Description:
            - This function configures the measurements that are to be made in a subsequent sweep.
              (i = current in amperes)

        TSP Syntax:
            ```
            - smuX.trigger.measure.i()
            ```

        Args:
            rbuffer: A reading buffer object where the readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.i({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.i()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def iv(self, ibuffer: str, vbuffer: str) -> None:
        """Run the ``smuX.trigger.measure.iv()`` function.

        Description:
            - This function configures the measurements that are to be made in a subsequent sweep.
              (i = current in amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - smuX.trigger.measure.iv()
            ```

        Args:
            ibuffer: A reading buffer object where current readings are stored.
            vbuffer: A reading buffer object where voltage readings are stored.

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

    def p(self, rbuffer: str) -> None:
        """Run the ``smuX.trigger.measure.p()`` function.

        Description:
            - This function configures the measurements that are to be made in a subsequent sweep.
              (p = power in watts)

        TSP Syntax:
            ```
            - smuX.trigger.measure.p()
            ```

        Args:
            rbuffer: A reading buffer object where the readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.p({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.p()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def r(self, rbuffer: str) -> None:
        """Run the ``smuX.trigger.measure.r()`` function.

        Description:
            - This function configures the measurements that are to be made in a subsequent sweep.
              (r = resistance in ohms)

        TSP Syntax:
            ```
            - smuX.trigger.measure.r()
            ```

        Args:
            rbuffer: A reading buffer object where the readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.r({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.r()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def v(self, rbuffer: str) -> None:
        """Run the ``smuX.trigger.measure.v()`` function.

        Description:
            - This function configures the measurements that are to be made in a subsequent sweep.
              (v = voltage in volts)

        TSP Syntax:
            ```
            - smuX.trigger.measure.v()
            ```

        Args:
            rbuffer: A reading buffer object where the readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.v({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.v()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def set_(self) -> None:
        """Run the ``smuX.trigger.measure.set()`` function.

        Description:
            - This function sets the measurement event detector to the detected state.

        TSP Syntax:
            ```
            - smuX.trigger.measure.set()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.measure.set()
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.set()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuxItemTriggerEndsweep(BaseTSPCmd):
    """The ``smuX.trigger.endsweep`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.endsweep.action
          applies to SMU channel A).

    Properties and methods:
        - ``.action``: The ``smuX.trigger.endsweep.action`` attribute.
    """

    @property
    def action(self) -> str:
        """Access the ``smuX.trigger.endsweep.action`` attribute.

        Description:
            - This attribute sets the action of the source at the end of a sweep.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.endsweep.action)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.endsweep.action = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.endsweep.action = value
            - print(smuX.trigger.endsweep.action)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.endsweep.action applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".action"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.action)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.action`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @action.setter
    def action(self, value: Union[str, float]) -> None:
        """Access the ``smuX.trigger.endsweep.action`` attribute.

        Description:
            - This attribute sets the action of the source at the end of a sweep.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.endsweep.action)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.endsweep.action = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.endsweep.action = value
            - print(smuX.trigger.endsweep.action)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.endsweep.action applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".action", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.action = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.action`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuxItemTriggerEndpulse(BaseTSPCmd):
    """The ``smuX.trigger.endpulse`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.endpulse.action
          applies to SMU channel A).

    Properties and methods:
        - ``.action``: The ``smuX.trigger.endpulse.action`` attribute.
        - ``.set()``: The ``smuX.trigger.endpulse.set()`` function.
        - ``.stimulus``: The ``smuX.trigger.endpulse.stimulus`` attribute.
    """

    @property
    def action(self) -> str:
        """Access the ``smuX.trigger.endpulse.action`` attribute.

        Description:
            - This attribute enables or disables pulse mode sweeps.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.endpulse.action)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.endpulse.action = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.endpulse.action = value
            - print(smuX.trigger.endpulse.action)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.endpulse.action applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".action"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.action)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.action`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @action.setter
    def action(self, value: Union[str, float]) -> None:
        """Access the ``smuX.trigger.endpulse.action`` attribute.

        Description:
            - This attribute enables or disables pulse mode sweeps.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.endpulse.action)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.endpulse.action = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.endpulse.action = value
            - print(smuX.trigger.endpulse.action)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.endpulse.action applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".action", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.action = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.action`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``smuX.trigger.endpulse.stimulus`` attribute.

        Description:
            - This attribute defines which event causes the end pulse event detector to enter the
              detected state.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.endpulse.stimulus)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.endpulse.stimulus = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.endpulse.stimulus = value
            - print(smuX.trigger.endpulse.stimulus)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.endpulse.stimulus applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``smuX.trigger.endpulse.stimulus`` attribute.

        Description:
            - This attribute defines which event causes the end pulse event detector to enter the
              detected state.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.endpulse.stimulus)`` query.
            - Setting this property to a value will send the
              ``smuX.trigger.endpulse.stimulus = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.endpulse.stimulus = value
            - print(smuX.trigger.endpulse.stimulus)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.endpulse.stimulus applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def set_(self) -> None:
        """Run the ``smuX.trigger.endpulse.set()`` function.

        Description:
            - This function sets the end pulse event detector to the detected state.

        TSP Syntax:
            ```
            - smuX.trigger.endpulse.set()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.endpulse.set()
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.set()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuxItemTriggerArm(BaseTSPCmd):
    """The ``smuX.trigger.arm`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.arm.count applies
          to SMU channel A).

    Properties and methods:
        - ``.count``: The ``smuX.trigger.arm.count`` attribute.
        - ``.set()``: The ``smuX.trigger.arm.set()`` function.
        - ``.stimulus``: The ``smuX.trigger.arm.stimulus`` attribute.
    """

    @property
    def count(self) -> str:
        """Access the ``smuX.trigger.arm.count`` attribute.

        Description:
            - This attribute sets the arm count in the trigger model.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.arm.count)`` query.
            - Setting this property to a value will send the ``smuX.trigger.arm.count = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.arm.count = value
            - print(smuX.trigger.arm.count)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.arm.count
              applies to SMU channel A).

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
        """Access the ``smuX.trigger.arm.count`` attribute.

        Description:
            - This attribute sets the arm count in the trigger model.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.arm.count)`` query.
            - Setting this property to a value will send the ``smuX.trigger.arm.count = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.arm.count = value
            - print(smuX.trigger.arm.count)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.arm.count
              applies to SMU channel A).

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
    def stimulus(self) -> str:
        """Access the ``smuX.trigger.arm.stimulus`` attribute.

        Description:
            - This attribute selects the event that causes the arm event detector to enter the
              detected state.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.arm.stimulus)`` query.
            - Setting this property to a value will send the ``smuX.trigger.arm.stimulus = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.arm.stimulus = value
            - print(smuX.trigger.arm.stimulus)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.arm.stimulus
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``smuX.trigger.arm.stimulus`` attribute.

        Description:
            - This attribute selects the event that causes the arm event detector to enter the
              detected state.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.arm.stimulus)`` query.
            - Setting this property to a value will send the ``smuX.trigger.arm.stimulus = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.arm.stimulus = value
            - print(smuX.trigger.arm.stimulus)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.arm.stimulus
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def set_(self) -> None:
        """Run the ``smuX.trigger.arm.set()`` function.

        Description:
            - This function sets the arm event detector to the detected state.

        TSP Syntax:
            ```
            - smuX.trigger.arm.set()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.arm.set()
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.set()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


#  pylint: disable=too-many-instance-attributes
class SmuxItemTrigger(BaseTSPCmd):
    """The ``smuX.trigger`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.ARMED_EVENT_ID
          applies to SMU channel A).

    Constants:
        - ``.ARMED_EVENT_ID``: The number of the armed event.
        - ``.IDLE_EVENT_ID``: The idle event number.
        - ``.MEASURE_COMPLETE_EVENT_ID``: The measurement complete event number.
        - ``.PULSE_COMPLETE_EVENT_ID``: The pulse complete event number.
        - ``.SOURCE_COMPLETE_EVENT_ID``: The source complete event number.
        - ``.SWEEPING_EVENT_ID``: The sweeping event number.
        - ``.SWEEP_COMPLETE_EVENT_ID``: The sweep complete event number.

    Properties and methods:
        - ``.arm``: The ``smuX.trigger.arm`` command tree.
        - ``.autoclear``: The ``smuX.trigger.autoclear`` attribute.
        - ``.count``: The ``smuX.trigger.count`` attribute.
        - ``.endpulse``: The ``smuX.trigger.endpulse`` command tree.
        - ``.endsweep``: The ``smuX.trigger.endsweep`` command tree.
        - ``.initiate()``: The ``smuX.trigger.initiate()`` function.
        - ``.measure``: The ``smuX.trigger.measure`` command tree.
        - ``.source``: The ``smuX.trigger.source`` command tree.
    """

    ARMED_EVENT_ID = "smuX.trigger.ARMED_EVENT_ID"
    """str: The number of the armed event."""
    IDLE_EVENT_ID = "smuX.trigger.IDLE_EVENT_ID"
    """str: The idle event number."""
    MEASURE_COMPLETE_EVENT_ID = "smuX.trigger.MEASURE_COMPLETE_EVENT_ID"
    """str: The measurement complete event number."""
    PULSE_COMPLETE_EVENT_ID = "smuX.trigger.PULSE_COMPLETE_EVENT_ID"
    """str: The pulse complete event number."""
    SOURCE_COMPLETE_EVENT_ID = "smuX.trigger.SOURCE_COMPLETE_EVENT_ID"
    """str: The source complete event number."""
    SWEEPING_EVENT_ID = "smuX.trigger.SWEEPING_EVENT_ID"
    """str: The sweeping event number."""
    SWEEP_COMPLETE_EVENT_ID = "smuX.trigger.SWEEP_COMPLETE_EVENT_ID"
    """str: The sweep complete event number."""

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.ARMED_EVENT_ID = self.ARMED_EVENT_ID.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.IDLE_EVENT_ID = self.IDLE_EVENT_ID.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.MEASURE_COMPLETE_EVENT_ID = self.MEASURE_COMPLETE_EVENT_ID.replace(
            "smuX", f"smu{self._cmd_syntax[3]}"
        )
        # pylint: disable=invalid-name
        self.PULSE_COMPLETE_EVENT_ID = self.PULSE_COMPLETE_EVENT_ID.replace(
            "smuX", f"smu{self._cmd_syntax[3]}"
        )
        # pylint: disable=invalid-name
        self.SOURCE_COMPLETE_EVENT_ID = self.SOURCE_COMPLETE_EVENT_ID.replace(
            "smuX", f"smu{self._cmd_syntax[3]}"
        )
        # pylint: disable=invalid-name
        self.SWEEPING_EVENT_ID = self.SWEEPING_EVENT_ID.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SWEEP_COMPLETE_EVENT_ID = self.SWEEP_COMPLETE_EVENT_ID.replace(
            "smuX", f"smu{self._cmd_syntax[3]}"
        )
        self._arm = SmuxItemTriggerArm(device, f"{self._cmd_syntax}.arm")
        self._endpulse = SmuxItemTriggerEndpulse(device, f"{self._cmd_syntax}.endpulse")
        self._endsweep = SmuxItemTriggerEndsweep(device, f"{self._cmd_syntax}.endsweep")
        self._measure = SmuxItemTriggerMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = SmuxItemTriggerSource(device, f"{self._cmd_syntax}.source")

    @property
    def arm(self) -> SmuxItemTriggerArm:
        """Return the ``smuX.trigger.arm`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.arm.count
              applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.count``: The ``smuX.trigger.arm.count`` attribute.
            - ``.set()``: The ``smuX.trigger.arm.set()`` function.
            - ``.stimulus``: The ``smuX.trigger.arm.stimulus`` attribute.
        """
        return self._arm

    @property
    def autoclear(self) -> str:
        """Access the ``smuX.trigger.autoclear`` attribute.

        Description:
            - This attribute turns automatic clearing of the event detectors on or off.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.autoclear)`` query.
            - Setting this property to a value will send the ``smuX.trigger.autoclear = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.autoclear = value
            - print(smuX.trigger.autoclear)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.autoclear
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autoclear"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autoclear)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autoclear`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autoclear.setter
    def autoclear(self, value: Union[str, float]) -> None:
        """Access the ``smuX.trigger.autoclear`` attribute.

        Description:
            - This attribute turns automatic clearing of the event detectors on or off.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.autoclear)`` query.
            - Setting this property to a value will send the ``smuX.trigger.autoclear = value``
              command.

        TSP Syntax:
            ```
            - smuX.trigger.autoclear = value
            - print(smuX.trigger.autoclear)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.autoclear
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autoclear", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autoclear = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autoclear`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def count(self) -> str:
        """Access the ``smuX.trigger.count`` attribute.

        Description:
            - This attribute sets the trigger count in the trigger model.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.count)`` query.
            - Setting this property to a value will send the ``smuX.trigger.count = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.count = value
            - print(smuX.trigger.count)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.trigger.count applies to SMU channel A).

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
        """Access the ``smuX.trigger.count`` attribute.

        Description:
            - This attribute sets the trigger count in the trigger model.

        Usage:
            - Accessing this property will send the ``print(smuX.trigger.count)`` query.
            - Setting this property to a value will send the ``smuX.trigger.count = value`` command.

        TSP Syntax:
            ```
            - smuX.trigger.count = value
            - print(smuX.trigger.count)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.trigger.count applies to SMU channel A).

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
    def endpulse(self) -> SmuxItemTriggerEndpulse:
        """Return the ``smuX.trigger.endpulse`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.endpulse.action applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.action``: The ``smuX.trigger.endpulse.action`` attribute.
            - ``.set()``: The ``smuX.trigger.endpulse.set()`` function.
            - ``.stimulus``: The ``smuX.trigger.endpulse.stimulus`` attribute.
        """
        return self._endpulse

    @property
    def endsweep(self) -> SmuxItemTriggerEndsweep:
        """Return the ``smuX.trigger.endsweep`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.trigger.endsweep.action applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.action``: The ``smuX.trigger.endsweep.action`` attribute.
        """
        return self._endsweep

    @property
    def measure(self) -> SmuxItemTriggerMeasure:
        """Return the ``smuX.trigger.measure`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.measure.v()
              applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.i()``: The ``smuX.trigger.measure.i()`` function.
            - ``.iv()``: The ``smuX.trigger.measure.iv()`` function.
            - ``.p()``: The ``smuX.trigger.measure.p()`` function.
            - ``.r()``: The ``smuX.trigger.measure.r()`` function.
            - ``.v()``: The ``smuX.trigger.measure.v()`` function.
            - ``.action``: The ``smuX.trigger.measure.action`` attribute.
            - ``.set()``: The ``smuX.trigger.measure.set()`` function.
            - ``.stimulus``: The ``smuX.trigger.measure.stimulus`` attribute.
        """
        return self._measure

    @property
    def source(self) -> SmuxItemTriggerSource:
        """Return the ``smuX.trigger.source`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.source.action
              applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.action``: The ``smuX.trigger.source.action`` attribute.
            - ``.limiti``: The ``smuX.trigger.source.limiti`` attribute.
            - ``.limitv``: The ``smuX.trigger.source.limitv`` attribute.
            - ``.lineari()``: The ``smuX.trigger.source.lineari()`` function.
            - ``.linearv()``: The ``smuX.trigger.source.linearv()`` function.
            - ``.listi()``: The ``smuX.trigger.source.listi()`` function.
            - ``.listv()``: The ``smuX.trigger.source.listv()`` function.
            - ``.logi()``: The ``smuX.trigger.source.logi()`` function.
            - ``.logv()``: The ``smuX.trigger.source.logv()`` function.
            - ``.set()``: The ``smuX.trigger.source.set()`` function.
            - ``.stimulus``: The ``smuX.trigger.source.stimulus`` attribute.
        """
        return self._source

    def initiate(self) -> None:
        """Run the ``smuX.trigger.initiate()`` function.

        Description:
            - This function initiates a sweep operation.

        TSP Syntax:
            ```
            - smuX.trigger.initiate()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.initiate()
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.initiate()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.initiate()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


#  pylint: disable=too-many-public-methods
class SmuxItemSource(BaseTSPCmd):
    """The ``smuX.source`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.source.autorangev applies
          to SMU channel A).

    Properties and methods:
        - ``.autorangei``: The ``smuX.source.autorangei`` attribute.
        - ``.autorangev``: The ``smuX.source.autorangev`` attribute.
        - ``.calibratei()``: The ``smuX.source.calibratei()`` function.
        - ``.calibratev()``: The ``smuX.source.calibratev()`` function.
        - ``.compliance``: The ``smuX.source.compliance`` attribute.
        - ``.delay``: The ``smuX.source.delay`` attribute.
        - ``.func``: The ``smuX.source.func`` attribute.
        - ``.highc``: The ``smuX.source.highc`` attribute.
        - ``.leveli``: The ``smuX.source.leveli`` attribute.
        - ``.levelv``: The ``smuX.source.levelv`` attribute.
        - ``.limiti``: The ``smuX.source.limiti`` attribute.
        - ``.limitp``: The ``smuX.source.limitp`` attribute.
        - ``.limitv``: The ``smuX.source.limitv`` attribute.
        - ``.lowrangei``: The ``smuX.source.lowrangei`` attribute.
        - ``.lowrangev``: The ``smuX.source.lowrangev`` attribute.
        - ``.offfunc``: The ``smuX.source.offfunc`` attribute.
        - ``.offlimiti``: The ``smuX.source.offlimiti`` attribute.
        - ``.offlimitv``: The ``smuX.source.offlimitv`` attribute.
        - ``.offmode``: The ``smuX.source.offmode`` attribute.
        - ``.output``: The ``smuX.source.output`` attribute.
        - ``.outputenableaction``: The ``smuX.source.outputenableaction`` attribute.
        - ``.rangei``: The ``smuX.source.rangei`` attribute.
        - ``.rangev``: The ``smuX.source.rangev`` attribute.
        - ``.settling``: The ``smuX.source.settling`` attribute.
        - ``.sink``: The ``smuX.source.sink`` attribute.
    """

    @property
    def autorangei(self) -> str:
        """Access the ``smuX.source.autorangei`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on/off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.autorangei)`` query.
            - Setting this property to a value will send the ``smuX.source.autorangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.autorangei = value
            - print(smuX.source.autorangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.autorangev
              applies to SMU channel A).

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
        """Access the ``smuX.source.autorangei`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on/off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.autorangei)`` query.
            - Setting this property to a value will send the ``smuX.source.autorangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.autorangei = value
            - print(smuX.source.autorangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.autorangev
              applies to SMU channel A).

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
        """Access the ``smuX.source.autorangev`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on/off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.autorangev)`` query.
            - Setting this property to a value will send the ``smuX.source.autorangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.autorangev = value
            - print(smuX.source.autorangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.autorangev
              applies to SMU channel A).

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
        """Access the ``smuX.source.autorangev`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on/off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.autorangev)`` query.
            - Setting this property to a value will send the ``smuX.source.autorangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.autorangev = value
            - print(smuX.source.autorangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.autorangev
              applies to SMU channel A).

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
    def compliance(self) -> str:
        """Access the ``smuX.source.compliance`` attribute.

        Description:
            - This attribute contains the state of source compliance.

        Usage:
            - Accessing this property will send the ``print(smuX.source.compliance)`` query.

        TSP Syntax:
            ```
            - print(smuX.source.compliance)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.compliance
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".compliance"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.compliance)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.compliance`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def delay(self) -> str:
        """Access the ``smuX.source.delay`` attribute.

        Description:
            - This attribute contains the source delay.

        Usage:
            - Accessing this property will send the ``print(smuX.source.delay)`` query.
            - Setting this property to a value will send the ``smuX.source.delay = value`` command.

        TSP Syntax:
            ```
            - smuX.source.delay = value
            - print(smuX.source.delay)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.delay applies
              to SMU channel A).

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
        """Access the ``smuX.source.delay`` attribute.

        Description:
            - This attribute contains the source delay.

        Usage:
            - Accessing this property will send the ``print(smuX.source.delay)`` query.
            - Setting this property to a value will send the ``smuX.source.delay = value`` command.

        TSP Syntax:
            ```
            - smuX.source.delay = value
            - print(smuX.source.delay)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.delay applies
              to SMU channel A).

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
        """Access the ``smuX.source.func`` attribute.

        Description:
            - This attribute contains the source function, which can be voltage or current.

        Usage:
            - Accessing this property will send the ``print(smuX.source.func)`` query.
            - Setting this property to a value will send the ``smuX.source.func = value`` command.

        TSP Syntax:
            ```
            - smuX.source.func = value
            - print(smuX.source.func)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.func applies to
              SMU channel A).

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
        """Access the ``smuX.source.func`` attribute.

        Description:
            - This attribute contains the source function, which can be voltage or current.

        Usage:
            - Accessing this property will send the ``print(smuX.source.func)`` query.
            - Setting this property to a value will send the ``smuX.source.func = value`` command.

        TSP Syntax:
            ```
            - smuX.source.func = value
            - print(smuX.source.func)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.func applies to
              SMU channel A).

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
    def highc(self) -> str:
        """Access the ``smuX.source.highc`` attribute.

        Description:
            - This attribute enables or disables high-capacitance mode.

        Usage:
            - Accessing this property will send the ``print(smuX.source.highc)`` query.
            - Setting this property to a value will send the ``smuX.source.highc = value`` command.

        TSP Syntax:
            ```
            - smuX.source.highc = value
            - print(smuX.source.highc)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.highc applies
              to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".highc"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.highc)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.highc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @highc.setter
    def highc(self, value: Union[str, float]) -> None:
        """Access the ``smuX.source.highc`` attribute.

        Description:
            - This attribute enables or disables high-capacitance mode.

        Usage:
            - Accessing this property will send the ``print(smuX.source.highc)`` query.
            - Setting this property to a value will send the ``smuX.source.highc = value`` command.

        TSP Syntax:
            ```
            - smuX.source.highc = value
            - print(smuX.source.highc)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.highc applies
              to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".highc", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.highc = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.highc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def leveli(self) -> str:
        """Access the ``smuX.source.leveli`` attribute.

        Description:
            - This attribute sets the source level. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.leveli)`` query.
            - Setting this property to a value will send the ``smuX.source.leveli = value`` command.

        TSP Syntax:
            ```
            - smuX.source.leveli = value
            - print(smuX.source.leveli)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.levelv applies
              to SMU channel A).

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
        """Access the ``smuX.source.leveli`` attribute.

        Description:
            - This attribute sets the source level. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.leveli)`` query.
            - Setting this property to a value will send the ``smuX.source.leveli = value`` command.

        TSP Syntax:
            ```
            - smuX.source.leveli = value
            - print(smuX.source.leveli)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.levelv applies
              to SMU channel A).

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
        """Access the ``smuX.source.levelv`` attribute.

        Description:
            - This attribute sets the source level. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.levelv)`` query.
            - Setting this property to a value will send the ``smuX.source.levelv = value`` command.

        TSP Syntax:
            ```
            - smuX.source.levelv = value
            - print(smuX.source.levelv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.levelv applies
              to SMU channel A).

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
        """Access the ``smuX.source.levelv`` attribute.

        Description:
            - This attribute sets the source level. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.levelv)`` query.
            - Setting this property to a value will send the ``smuX.source.levelv = value`` command.

        TSP Syntax:
            ```
            - smuX.source.levelv = value
            - print(smuX.source.levelv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.levelv applies
              to SMU channel A).

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
        """Access the ``smuX.source.limiti`` attribute.

        Description:
            - This attribute sets compliance limits. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.limiti)`` query.
            - Setting this property to a value will send the ``smuX.source.limiti = value`` command.

        TSP Syntax:
            ```
            - smuX.source.limiti = value
            - print(smuX.source.limiti)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.limitv applies
              to SMU channel A).

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
        """Access the ``smuX.source.limiti`` attribute.

        Description:
            - This attribute sets compliance limits. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.limiti)`` query.
            - Setting this property to a value will send the ``smuX.source.limiti = value`` command.

        TSP Syntax:
            ```
            - smuX.source.limiti = value
            - print(smuX.source.limiti)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.limitv applies
              to SMU channel A).

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
    def limitp(self) -> str:
        """Access the ``smuX.source.limitp`` attribute.

        Description:
            - This attribute sets compliance limits. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.limitp)`` query.
            - Setting this property to a value will send the ``smuX.source.limitp = value`` command.

        TSP Syntax:
            ```
            - smuX.source.limitp = value
            - print(smuX.source.limitp)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.limitv applies
              to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".limitp"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.limitp)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @limitp.setter
    def limitp(self, value: Union[str, float]) -> None:
        """Access the ``smuX.source.limitp`` attribute.

        Description:
            - This attribute sets compliance limits. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.limitp)`` query.
            - Setting this property to a value will send the ``smuX.source.limitp = value`` command.

        TSP Syntax:
            ```
            - smuX.source.limitp = value
            - print(smuX.source.limitp)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.limitv applies
              to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".limitp", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.limitp = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limitp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limitv(self) -> str:
        """Access the ``smuX.source.limitv`` attribute.

        Description:
            - This attribute sets compliance limits. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.limitv)`` query.
            - Setting this property to a value will send the ``smuX.source.limitv = value`` command.

        TSP Syntax:
            ```
            - smuX.source.limitv = value
            - print(smuX.source.limitv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.limitv applies
              to SMU channel A).

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
        """Access the ``smuX.source.limitv`` attribute.

        Description:
            - This attribute sets compliance limits. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.limitv)`` query.
            - Setting this property to a value will send the ``smuX.source.limitv = value`` command.

        TSP Syntax:
            ```
            - smuX.source.limitv = value
            - print(smuX.source.limitv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.limitv applies
              to SMU channel A).

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
    def lowrangei(self) -> str:
        """Access the ``smuX.source.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest source range that is used during autoranging. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.lowrangei)`` query.
            - Setting this property to a value will send the ``smuX.source.lowrangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.lowrangei = value
            - print(smuX.source.lowrangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.lowrangev
              applies to SMU channel A).

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
        """Access the ``smuX.source.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest source range that is used during autoranging. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.lowrangei)`` query.
            - Setting this property to a value will send the ``smuX.source.lowrangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.lowrangei = value
            - print(smuX.source.lowrangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.lowrangev
              applies to SMU channel A).

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
        """Access the ``smuX.source.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest source range that is used during autoranging. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.lowrangev)`` query.
            - Setting this property to a value will send the ``smuX.source.lowrangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.lowrangev = value
            - print(smuX.source.lowrangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.lowrangev
              applies to SMU channel A).

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
        """Access the ``smuX.source.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest source range that is used during autoranging. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.lowrangev)`` query.
            - Setting this property to a value will send the ``smuX.source.lowrangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.lowrangev = value
            - print(smuX.source.lowrangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.lowrangev
              applies to SMU channel A).

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
        """Access the ``smuX.source.offfunc`` attribute.

        Description:
            - This attribute sets the source function that is used (source 0 A or 0 V) when the
              output is turned off and the source-measure unit (SMU) is in normal output-off mode.

        Usage:
            - Accessing this property will send the ``print(smuX.source.offfunc)`` query.
            - Setting this property to a value will send the ``smuX.source.offfunc = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.offfunc = value
            - print(smuX.source.offfunc)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.source.offfunc applies to SMU channel A).

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
        """Access the ``smuX.source.offfunc`` attribute.

        Description:
            - This attribute sets the source function that is used (source 0 A or 0 V) when the
              output is turned off and the source-measure unit (SMU) is in normal output-off mode.

        Usage:
            - Accessing this property will send the ``print(smuX.source.offfunc)`` query.
            - Setting this property to a value will send the ``smuX.source.offfunc = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.offfunc = value
            - print(smuX.source.offfunc)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.source.offfunc applies to SMU channel A).

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
        """Access the ``smuX.source.offlimiti`` attribute.

        Description:
            - This attribute sets the limit (current or voltage) used when the source-measure unit
              (SMU) is in normal output-off mode. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.offlimiti)`` query.
            - Setting this property to a value will send the ``smuX.source.offlimiti = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.offlimiti = value
            - print(smuX.source.offlimiti)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.offlimiti
              applies to SMU channel A).

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
        """Access the ``smuX.source.offlimiti`` attribute.

        Description:
            - This attribute sets the limit (current or voltage) used when the source-measure unit
              (SMU) is in normal output-off mode. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.offlimiti)`` query.
            - Setting this property to a value will send the ``smuX.source.offlimiti = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.offlimiti = value
            - print(smuX.source.offlimiti)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.offlimiti
              applies to SMU channel A).

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
        """Access the ``smuX.source.offlimitv`` attribute.

        Description:
            - This attribute sets the limit (current or voltage) used when the source-measure unit
              (SMU) is in normal output-off mode. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.offlimitv)`` query.
            - Setting this property to a value will send the ``smuX.source.offlimitv = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.offlimitv = value
            - print(smuX.source.offlimitv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.offlimiti
              applies to SMU channel A).

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
        """Access the ``smuX.source.offlimitv`` attribute.

        Description:
            - This attribute sets the limit (current or voltage) used when the source-measure unit
              (SMU) is in normal output-off mode. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.offlimitv)`` query.
            - Setting this property to a value will send the ``smuX.source.offlimitv = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.offlimitv = value
            - print(smuX.source.offlimitv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.offlimiti
              applies to SMU channel A).

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
    def offmode(self) -> str:
        """Access the ``smuX.source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(smuX.source.offmode)`` query.
            - Setting this property to a value will send the ``smuX.source.offmode = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.offmode = value
            - print(smuX.source.offmode)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.offmode applies
              to SMU channel A).

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
        """Access the ``smuX.source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(smuX.source.offmode)`` query.
            - Setting this property to a value will send the ``smuX.source.offmode = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.offmode = value
            - print(smuX.source.offmode)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.offmode applies
              to SMU channel A).

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
        """Access the ``smuX.source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(smuX.source.output)`` query.
            - Setting this property to a value will send the ``smuX.source.output = value`` command.

        TSP Syntax:
            ```
            - smuX.source.output = value
            - print(smuX.source.output)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.output applies
              to SMU channel A).

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
        """Access the ``smuX.source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(smuX.source.output)`` query.
            - Setting this property to a value will send the ``smuX.source.output = value`` command.

        TSP Syntax:
            ```
            - smuX.source.output = value
            - print(smuX.source.output)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.output applies
              to SMU channel A).

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
    def outputenableaction(self) -> str:
        """Access the ``smuX.source.outputenableaction`` attribute.

        Description:
            - This attribute controls output enable action of the source.

        Usage:
            - Accessing this property will send the ``print(smuX.source.outputenableaction)`` query.
            - Setting this property to a value will send the
              ``smuX.source.outputenableaction = value`` command.

        TSP Syntax:
            ```
            - smuX.source.outputenableaction = value
            - print(smuX.source.outputenableaction)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.source.outputenableaction applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".outputenableaction"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.outputenableaction)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.outputenableaction`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @outputenableaction.setter
    def outputenableaction(self, value: Union[str, float]) -> None:
        """Access the ``smuX.source.outputenableaction`` attribute.

        Description:
            - This attribute controls output enable action of the source.

        Usage:
            - Accessing this property will send the ``print(smuX.source.outputenableaction)`` query.
            - Setting this property to a value will send the
              ``smuX.source.outputenableaction = value`` command.

        TSP Syntax:
            ```
            - smuX.source.outputenableaction = value
            - print(smuX.source.outputenableaction)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example,
              smua.source.outputenableaction applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".outputenableaction", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.outputenableaction = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.outputenableaction`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rangei(self) -> str:
        """Access the ``smuX.source.rangei`` attribute.

        Description:
            - This attribute contains the source range. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.rangei)`` query.
            - Setting this property to a value will send the ``smuX.source.rangei = value`` command.

        TSP Syntax:
            ```
            - smuX.source.rangei = value
            - print(smuX.source.rangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rangev applies
              to SMU channel A).

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
        """Access the ``smuX.source.rangei`` attribute.

        Description:
            - This attribute contains the source range. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.source.rangei)`` query.
            - Setting this property to a value will send the ``smuX.source.rangei = value`` command.

        TSP Syntax:
            ```
            - smuX.source.rangei = value
            - print(smuX.source.rangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rangev applies
              to SMU channel A).

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
        """Access the ``smuX.source.rangev`` attribute.

        Description:
            - This attribute contains the source range. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.rangev)`` query.
            - Setting this property to a value will send the ``smuX.source.rangev = value`` command.

        TSP Syntax:
            ```
            - smuX.source.rangev = value
            - print(smuX.source.rangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rangev applies
              to SMU channel A).

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
        """Access the ``smuX.source.rangev`` attribute.

        Description:
            - This attribute contains the source range. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.source.rangev)`` query.
            - Setting this property to a value will send the ``smuX.source.rangev = value`` command.

        TSP Syntax:
            ```
            - smuX.source.rangev = value
            - print(smuX.source.rangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rangev applies
              to SMU channel A).

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
    def settling(self) -> str:
        """Access the ``smuX.source.settling`` attribute.

        Description:
            - This attribute contains the source settling mode.

        Usage:
            - Accessing this property will send the ``print(smuX.source.settling)`` query.
            - Setting this property to a value will send the ``smuX.source.settling = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.settling = value
            - print(smuX.source.settling)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.source.settling applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".settling"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.settling)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.settling`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @settling.setter
    def settling(self, value: Union[str, float]) -> None:
        """Access the ``smuX.source.settling`` attribute.

        Description:
            - This attribute contains the source settling mode.

        Usage:
            - Accessing this property will send the ``print(smuX.source.settling)`` query.
            - Setting this property to a value will send the ``smuX.source.settling = value``
              command.

        TSP Syntax:
            ```
            - smuX.source.settling = value
            - print(smuX.source.settling)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.source.settling applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".settling", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.settling = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.settling`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def sink(self) -> str:
        """Access the ``smuX.source.sink`` attribute.

        Description:
            - This attribute turns sink mode on or off.

        Usage:
            - Accessing this property will send the ``print(smuX.source.sink)`` query.
            - Setting this property to a value will send the ``smuX.source.sink = value`` command.

        TSP Syntax:
            ```
            - smuX.source.sink = value
            - print(smuX.source.sink)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.sink applies to
              SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".sink"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.sink)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.sink`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @sink.setter
    def sink(self, value: Union[str, float]) -> None:
        """Access the ``smuX.source.sink`` attribute.

        Description:
            - This attribute turns sink mode on or off.

        Usage:
            - Accessing this property will send the ``print(smuX.source.sink)`` query.
            - Setting this property to a value will send the ``smuX.source.sink = value`` command.

        TSP Syntax:
            ```
            - smuX.source.sink = value
            - print(smuX.source.sink)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.sink applies to
              SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".sink", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.sink = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.sink`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def calibratei(
        self,
        range_: str,
        cp1_expected: str,
        cp1_reference: str,
        cp2_expected: str,
        cp2_reference: str,
    ) -> None:
        """Run the ``smuX.source.calibratei()`` function.

        Description:
            - This function generates and activates new source calibration constants. (i = current
              in amperes)

        TSP Syntax:
            ```
            - smuX.source.calibratei()
            ```

        Args:
            range_: The measurement range to adjust.
            cp1_expected: The source value set for point 1.
            cp1_reference: The reference measurement for point 1 as measured externally.
            cp2_expected: The source value set for point 2.
            cp2_reference: The reference measurement for point 2 as measured externally.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.calibratei({range_}, "
                f"{cp1_expected}, "
                f"{cp1_reference}, "
                f"{cp2_expected}, "
                f"{cp2_reference})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.calibratei()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def calibratev(
        self,
        range_: str,
        cp1_expected: str,
        cp1_reference: str,
        cp2_expected: str,
        cp2_reference: str,
    ) -> None:
        """Run the ``smuX.source.calibratev()`` function.

        Description:
            - This function generates and activates new source calibration constants. (v = voltage
              in volts)

        TSP Syntax:
            ```
            - smuX.source.calibratev()
            ```

        Args:
            range_: The measurement range to adjust.
            cp1_expected: The source value set for point 1.
            cp1_reference: The reference measurement for point 1 as measured externally.
            cp2_expected: The source value set for point 2.
            cp2_reference: The reference measurement for point 2 as measured externally.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.calibratev({range_}, "
                f"{cp1_expected}, "
                f"{cp1_reference}, "
                f"{cp2_expected}, "
                f"{cp2_reference})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.calibratev()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuxItemMeasureRel(BaseTSPCmd):
    """The ``smuX.measure.rel`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
          applies to SMU channel A).

    Properties and methods:
        - ``.enablei``: The ``smuX.measure.rel.enablei`` attribute.
        - ``.enablep``: The ``smuX.measure.rel.enablep`` attribute.
        - ``.enabler``: The ``smuX.measure.rel.enabler`` attribute.
        - ``.enablev``: The ``smuX.measure.rel.enablev`` attribute.
        - ``.leveli``: The ``smuX.measure.rel.leveli`` attribute.
        - ``.levelp``: The ``smuX.measure.rel.levelp`` attribute.
        - ``.levelr``: The ``smuX.measure.rel.levelr`` attribute.
        - ``.levelv``: The ``smuX.measure.rel.levelv`` attribute.
    """

    @property
    def enablei(self) -> str:
        """Access the ``smuX.measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.enablei)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.enablei = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.enablei = value
            - print(smuX.measure.rel.enablei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.enablei)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.enablei = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.enablei = value
            - print(smuX.measure.rel.enablei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.enablep)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.enablep = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.enablep = value
            - print(smuX.measure.rel.enablep)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.enablep)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.enablep = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.enablep = value
            - print(smuX.measure.rel.enablep)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.enabler)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.enabler = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.enabler = value
            - print(smuX.measure.rel.enabler)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.enabler)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.enabler = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.enabler = value
            - print(smuX.measure.rel.enabler)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.enablev)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.enablev = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.enablev = value
            - print(smuX.measure.rel.enablev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.enablev)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.enablev = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.enablev = value
            - print(smuX.measure.rel.enablev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.leveli`` attribute.

        Description:
            - This attribute sets the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.leveli)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.leveli = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.leveli = value
            - print(smuX.measure.rel.leveli)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.levelv
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.leveli`` attribute.

        Description:
            - This attribute sets the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.leveli)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.leveli = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.leveli = value
            - print(smuX.measure.rel.leveli)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.levelv
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.levelp`` attribute.

        Description:
            - This attribute sets the offset value for relative measurements. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.levelp)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.levelp = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.levelp = value
            - print(smuX.measure.rel.levelp)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.levelv
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.levelp`` attribute.

        Description:
            - This attribute sets the offset value for relative measurements. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.levelp)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.levelp = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.levelp = value
            - print(smuX.measure.rel.levelp)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.levelv
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.levelr`` attribute.

        Description:
            - This attribute sets the offset value for relative measurements. (r = resistance in
              ohms)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.levelr)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.levelr = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.levelr = value
            - print(smuX.measure.rel.levelr)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.levelv
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.levelr`` attribute.

        Description:
            - This attribute sets the offset value for relative measurements. (r = resistance in
              ohms)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.levelr)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.levelr = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.levelr = value
            - print(smuX.measure.rel.levelr)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.levelv
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.levelv`` attribute.

        Description:
            - This attribute sets the offset value for relative measurements. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.levelv)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.levelv = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.levelv = value
            - print(smuX.measure.rel.levelv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.levelv
              applies to SMU channel A).

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
        """Access the ``smuX.measure.rel.levelv`` attribute.

        Description:
            - This attribute sets the offset value for relative measurements. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rel.levelv)`` query.
            - Setting this property to a value will send the ``smuX.measure.rel.levelv = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rel.levelv = value
            - print(smuX.measure.rel.levelv)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.levelv
              applies to SMU channel A).

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


class SmuxItemMeasureFilter(BaseTSPCmd):
    """The ``smuX.measure.filter`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.filter.count
          applies to SMU channel A).

    Properties and methods:
        - ``.count``: The ``smuX.measure.filter.count`` attribute.
        - ``.enable``: The ``smuX.measure.filter.enable`` attribute.
        - ``.type``: The ``smuX.measure.filter.type`` attribute.
    """

    @property
    def count(self) -> str:
        """Access the ``smuX.measure.filter.count`` attribute.

        Description:
            - This command sets the number of measured readings that are required to yield one
              filtered measurement.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.filter.count)`` query.
            - Setting this property to a value will send the ``smuX.measure.filter.count = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.filter.count = value
            - print(smuX.measure.filter.count)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.filter.count
              applies to SMU channel A).

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
        """Access the ``smuX.measure.filter.count`` attribute.

        Description:
            - This command sets the number of measured readings that are required to yield one
              filtered measurement.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.filter.count)`` query.
            - Setting this property to a value will send the ``smuX.measure.filter.count = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.filter.count = value
            - print(smuX.measure.filter.count)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.filter.count
              applies to SMU channel A).

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
    def enable(self) -> str:
        """Access the ``smuX.measure.filter.enable`` attribute.

        Description:
            - This command enables or disables filtered measurements.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.filter.enable)`` query.
            - Setting this property to a value will send the ``smuX.measure.filter.enable = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.filter.enable = value
            - print(smuX.measure.filter.enable)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.measure.filter.enable applies to SMU channel
              A).

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
        """Access the ``smuX.measure.filter.enable`` attribute.

        Description:
            - This command enables or disables filtered measurements.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.filter.enable)`` query.
            - Setting this property to a value will send the ``smuX.measure.filter.enable = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.filter.enable = value
            - print(smuX.measure.filter.enable)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.measure.filter.enable applies to SMU channel
              A).

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
    def type(self) -> str:
        """Access the ``smuX.measure.filter.type`` attribute.

        Description:
            - This command sets the type of filter used for measurements when the measurement filter
              is enabled.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.filter.type)`` query.
            - Setting this property to a value will send the ``smuX.measure.filter.type = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.filter.type = value
            - print(smuX.measure.filter.type)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.measure.filter.type applies to SMU Channel
              A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".type"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.type)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.type`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @type.setter
    def type(self, value: Union[str, float]) -> None:
        """Access the ``smuX.measure.filter.type`` attribute.

        Description:
            - This command sets the type of filter used for measurements when the measurement filter
              is enabled.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.filter.type)`` query.
            - Setting this property to a value will send the ``smuX.measure.filter.type = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.filter.type = value
            - print(smuX.measure.filter.type)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.measure.filter.type applies to SMU Channel
              A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".type", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.type = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.type`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


#  pylint: disable=too-many-public-methods
class SmuxItemMeasure(BaseTSPCmd):
    """The ``smuX.measure`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.v() applies to SMU
          channel A).

    Properties and methods:
        - ``.i()``: The ``smuX.measure.i()`` function.
        - ``.iv()``: The ``smuX.measure.iv()`` function.
        - ``.p()``: The ``smuX.measure.p()`` function.
        - ``.r()``: The ``smuX.measure.r()`` function.
        - ``.v()``: The ``smuX.measure.v()`` function.
        - ``.analogfilter``: The ``smuX.measure.analogfilter`` attribute.
        - ``.autorangei``: The ``smuX.measure.autorangei`` attribute.
        - ``.autorangev``: The ``smuX.measure.autorangev`` attribute.
        - ``.autozero``: The ``smuX.measure.autozero`` attribute.
        - ``.calibratei()``: The ``smuX.measure.calibratei()`` function.
        - ``.calibratev()``: The ``smuX.measure.calibratev()`` function.
        - ``.count``: The ``smuX.measure.count`` attribute.
        - ``.delay``: The ``smuX.measure.delay`` attribute.
        - ``.delayfactor``: The ``smuX.measure.delayfactor`` attribute.
        - ``.filter``: The ``smuX.measure.filter`` command tree.
        - ``.highcrangedelayfactor``: The ``smuX.measure.highcrangedelayfactor`` attribute.
        - ``.interval``: The ``smuX.measure.interval`` attribute.
        - ``.lowrangei``: The ``smuX.measure.lowrangei`` attribute.
        - ``.lowrangev``: The ``smuX.measure.lowrangev`` attribute.
        - ``.nplc``: The ``smuX.measure.nplc`` attribute.
        - ``.overlappedi()``: The ``smuX.measure.overlappedi()`` function.
        - ``.overlappediv()``: The ``smuX.measure.overlappediv()`` function.
        - ``.overlappedp()``: The ``smuX.measure.overlappedp()`` function.
        - ``.overlappedr()``: The ``smuX.measure.overlappedr()`` function.
        - ``.overlappedv()``: The ``smuX.measure.overlappedv()`` function.
        - ``.rangei``: The ``smuX.measure.rangei`` attribute.
        - ``.rangev``: The ``smuX.measure.rangev`` attribute.
        - ``.rel``: The ``smuX.measure.rel`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._filter = SmuxItemMeasureFilter(device, f"{self._cmd_syntax}.filter")
        self._rel = SmuxItemMeasureRel(device, f"{self._cmd_syntax}.rel")

    @property
    def analogfilter(self) -> str:
        """Access the ``smuX.measure.analogfilter`` attribute.

        Description:
            - This attribute controls the use of an analog filter when measuring on the lowest
              current ranges (2634B, 2635B, and 2636B only).

        Usage:
            - Accessing this property will send the ``print(smuX.measure.analogfilter)`` query.
            - Setting this property to a value will send the ``smuX.measure.analogfilter = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.analogfilter = value
            - print(smuX.measure.analogfilter)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.analogfilter
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".analogfilter"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.analogfilter)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.analogfilter`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @analogfilter.setter
    def analogfilter(self, value: Union[str, float]) -> None:
        """Access the ``smuX.measure.analogfilter`` attribute.

        Description:
            - This attribute controls the use of an analog filter when measuring on the lowest
              current ranges (2634B, 2635B, and 2636B only).

        Usage:
            - Accessing this property will send the ``print(smuX.measure.analogfilter)`` query.
            - Setting this property to a value will send the ``smuX.measure.analogfilter = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.analogfilter = value
            - print(smuX.measure.analogfilter)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.analogfilter
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".analogfilter", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.analogfilter = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.analogfilter`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autorangei(self) -> str:
        """Access the ``smuX.measure.autorangei`` attribute.

        Description:
            - This attribute stores the measurement autorange setting. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.autorangei)`` query.
            - Setting this property to a value will send the ``smuX.measure.autorangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.autorangei = value
            - print(smuX.measure.autorangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.autorangev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.autorangei`` attribute.

        Description:
            - This attribute stores the measurement autorange setting. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.autorangei)`` query.
            - Setting this property to a value will send the ``smuX.measure.autorangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.autorangei = value
            - print(smuX.measure.autorangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.autorangev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.autorangev`` attribute.

        Description:
            - This attribute stores the measurement autorange setting. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.autorangev)`` query.
            - Setting this property to a value will send the ``smuX.measure.autorangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.autorangev = value
            - print(smuX.measure.autorangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.autorangev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.autorangev`` attribute.

        Description:
            - This attribute stores the measurement autorange setting. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.autorangev)`` query.
            - Setting this property to a value will send the ``smuX.measure.autorangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.autorangev = value
            - print(smuX.measure.autorangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.autorangev
              applies to SMU channel A).

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
    def autozero(self) -> str:
        """Access the ``smuX.measure.autozero`` attribute.

        Description:
            - This attribute enables or disables automatic updates to the internal reference
              measurements (autozero) of the instrument.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.autozero)`` query.
            - Setting this property to a value will send the ``smuX.measure.autozero = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.autozero = value
            - print(smuX.measure.autozero)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.autozero
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autozero"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autozero)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autozero`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autozero.setter
    def autozero(self, value: Union[str, float]) -> None:
        """Access the ``smuX.measure.autozero`` attribute.

        Description:
            - This attribute enables or disables automatic updates to the internal reference
              measurements (autozero) of the instrument.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.autozero)`` query.
            - Setting this property to a value will send the ``smuX.measure.autozero = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.autozero = value
            - print(smuX.measure.autozero)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.autozero
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autozero", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autozero = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autozero`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def count(self) -> str:
        """Access the ``smuX.measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements made when a measurement is requested.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.count)`` query.
            - Setting this property to a value will send the ``smuX.measure.count = value`` command.

        TSP Syntax:
            ```
            - smuX.measure.count = value
            - print(smuX.measure.count)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.count applies
              to SMU channel A).

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
        """Access the ``smuX.measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements made when a measurement is requested.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.count)`` query.
            - Setting this property to a value will send the ``smuX.measure.count = value`` command.

        TSP Syntax:
            ```
            - smuX.measure.count = value
            - print(smuX.measure.count)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.count applies
              to SMU channel A).

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
        """Access the ``smuX.measure.delay`` attribute.

        Description:
            - This attribute controls the measurement delay.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.delay)`` query.
            - Setting this property to a value will send the ``smuX.measure.delay = value`` command.

        TSP Syntax:
            ```
            - smuX.measure.delay = value
            - print(smuX.measure.delay)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.delay applies
              to SMU channel A).

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
        """Access the ``smuX.measure.delay`` attribute.

        Description:
            - This attribute controls the measurement delay.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.delay)`` query.
            - Setting this property to a value will send the ``smuX.measure.delay = value`` command.

        TSP Syntax:
            ```
            - smuX.measure.delay = value
            - print(smuX.measure.delay)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.delay applies
              to SMU channel A).

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
    def delayfactor(self) -> str:
        """Access the ``smuX.measure.delayfactor`` attribute.

        Description:
            - This attribute stores a multiplier to the delays that are used when smuX.measure.delay
              is set to smuX.DELAY_AUTO.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.delayfactor)`` query.
            - Setting this property to a value will send the ``smuX.measure.delayfactor = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.delayfactor = value
            - print(smuX.measure.delayfactor)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.delayfactor
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".delayfactor"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.delayfactor)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delayfactor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @delayfactor.setter
    def delayfactor(self, value: Union[str, float]) -> None:
        """Access the ``smuX.measure.delayfactor`` attribute.

        Description:
            - This attribute stores a multiplier to the delays that are used when smuX.measure.delay
              is set to smuX.DELAY_AUTO.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.delayfactor)`` query.
            - Setting this property to a value will send the ``smuX.measure.delayfactor = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.delayfactor = value
            - print(smuX.measure.delayfactor)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.delayfactor
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".delayfactor", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.delayfactor = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delayfactor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def filter(self) -> SmuxItemMeasureFilter:
        """Return the ``smuX.measure.filter`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.filter.count
              applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.count``: The ``smuX.measure.filter.count`` attribute.
            - ``.enable``: The ``smuX.measure.filter.enable`` attribute.
            - ``.type``: The ``smuX.measure.filter.type`` attribute.
        """
        return self._filter

    @property
    def highcrangedelayfactor(self) -> str:
        """Access the ``smuX.measure.highcrangedelayfactor`` attribute.

        Description:
            - This attribute contains a delay multiplier that is only used during range changes when
              the high-capacitance mode is active.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.highcrangedelayfactor)``
              query.
            - Setting this property to a value will send the
              ``smuX.measure.highcrangedelayfactor = value`` command.

        TSP Syntax:
            ```
            - smuX.measure.highcrangedelayfactor = value
            - print(smuX.measure.highcrangedelayfactor)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.measure.highcrangedelayfactor applies to SMU
              Channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".highcrangedelayfactor"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.highcrangedelayfactor)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.highcrangedelayfactor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @highcrangedelayfactor.setter
    def highcrangedelayfactor(self, value: Union[str, float]) -> None:
        """Access the ``smuX.measure.highcrangedelayfactor`` attribute.

        Description:
            - This attribute contains a delay multiplier that is only used during range changes when
              the high-capacitance mode is active.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.highcrangedelayfactor)``
              query.
            - Setting this property to a value will send the
              ``smuX.measure.highcrangedelayfactor = value`` command.

        TSP Syntax:
            ```
            - smuX.measure.highcrangedelayfactor = value
            - print(smuX.measure.highcrangedelayfactor)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.measure.highcrangedelayfactor applies to SMU
              Channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".highcrangedelayfactor", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.highcrangedelayfactor = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.highcrangedelayfactor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def interval(self) -> str:
        """Access the ``smuX.measure.interval`` attribute.

        Description:
            - This attribute sets the interval between multiple measurements.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.interval)`` query.
            - Setting this property to a value will send the ``smuX.measure.interval = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.interval = value
            - print(smuX.measure.interval)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.measure.interval applies to SMU Channel A).

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
        """Access the ``smuX.measure.interval`` attribute.

        Description:
            - This attribute sets the interval between multiple measurements.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.interval)`` query.
            - Setting this property to a value will send the ``smuX.measure.interval = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.interval = value
            - print(smuX.measure.interval)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.measure.interval applies to SMU Channel A).

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
        """Access the ``smuX.measure.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest measurement range that is used when the instrument is
              autoranging. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.lowrangei)`` query.
            - Setting this property to a value will send the ``smuX.measure.lowrangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.lowrangei = value
            - print(smuX.measure.lowrangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.lowrangev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest measurement range that is used when the instrument is
              autoranging. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.lowrangei)`` query.
            - Setting this property to a value will send the ``smuX.measure.lowrangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.lowrangei = value
            - print(smuX.measure.lowrangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.lowrangev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest measurement range that is used when the instrument is
              autoranging. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.lowrangev)`` query.
            - Setting this property to a value will send the ``smuX.measure.lowrangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.lowrangev = value
            - print(smuX.measure.lowrangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.lowrangev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest measurement range that is used when the instrument is
              autoranging. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.lowrangev)`` query.
            - Setting this property to a value will send the ``smuX.measure.lowrangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.lowrangev = value
            - print(smuX.measure.lowrangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.lowrangev
              applies to SMU channel A).

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
        """Access the ``smuX.measure.nplc`` attribute.

        Description:
            - This command sets the integration aperture for measurements.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.nplc)`` query.
            - Setting this property to a value will send the ``smuX.measure.nplc = value`` command.

        TSP Syntax:
            ```
            - smuX.measure.nplc = value
            - print(smuX.measure.nplc)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.nplc applies
              to SMU channel A).

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
        """Access the ``smuX.measure.nplc`` attribute.

        Description:
            - This command sets the integration aperture for measurements.

        Usage:
            - Accessing this property will send the ``print(smuX.measure.nplc)`` query.
            - Setting this property to a value will send the ``smuX.measure.nplc = value`` command.

        TSP Syntax:
            ```
            - smuX.measure.nplc = value
            - print(smuX.measure.nplc)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.nplc applies
              to SMU channel A).

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
        """Access the ``smuX.measure.rangei`` attribute.

        Description:
            - This attribute contains the positive full-scale value of the measurement range for
              voltage or current. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rangei)`` query.
            - Setting this property to a value will send the ``smuX.measure.rangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rangei = value
            - print(smuX.measure.rangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rangev applies
              to SMU channel A).

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
        """Access the ``smuX.measure.rangei`` attribute.

        Description:
            - This attribute contains the positive full-scale value of the measurement range for
              voltage or current. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rangei)`` query.
            - Setting this property to a value will send the ``smuX.measure.rangei = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rangei = value
            - print(smuX.measure.rangei)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rangev applies
              to SMU channel A).

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
        """Access the ``smuX.measure.rangev`` attribute.

        Description:
            - This attribute contains the positive full-scale value of the measurement range for
              voltage or current. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rangev)`` query.
            - Setting this property to a value will send the ``smuX.measure.rangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rangev = value
            - print(smuX.measure.rangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rangev applies
              to SMU channel A).

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
        """Access the ``smuX.measure.rangev`` attribute.

        Description:
            - This attribute contains the positive full-scale value of the measurement range for
              voltage or current. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smuX.measure.rangev)`` query.
            - Setting this property to a value will send the ``smuX.measure.rangev = value``
              command.

        TSP Syntax:
            ```
            - smuX.measure.rangev = value
            - print(smuX.measure.rangev)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rangev applies
              to SMU channel A).

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
    def rel(self) -> SmuxItemMeasureRel:
        """Return the ``smuX.measure.rel`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.rel.enablev
              applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.enablei``: The ``smuX.measure.rel.enablei`` attribute.
            - ``.enablep``: The ``smuX.measure.rel.enablep`` attribute.
            - ``.enabler``: The ``smuX.measure.rel.enabler`` attribute.
            - ``.enablev``: The ``smuX.measure.rel.enablev`` attribute.
            - ``.leveli``: The ``smuX.measure.rel.leveli`` attribute.
            - ``.levelp``: The ``smuX.measure.rel.levelp`` attribute.
            - ``.levelr``: The ``smuX.measure.rel.levelr`` attribute.
            - ``.levelv``: The ``smuX.measure.rel.levelv`` attribute.
        """
        return self._rel

    def i(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``smuX.measure.i()`` function.

        Description:
            - This function makes one or more measurements. (i = current in amperes)

        TSP Syntax:
            ```
            - smuX.measure.i()
            ```

        Args:
            reading_buffer (optional): A reading buffer object where all readings are stored.

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

    def iv(
        self, i_reading_buffer: Optional[str] = None, v_reading_buffer: Optional[str] = None
    ) -> str:
        """Run the ``smuX.measure.iv()`` function.

        Description:
            - This function makes one or more measurements. (i = current in amperes, v = voltage in
              volts)

        TSP Syntax:
            ```
            - smuX.measure.iv()
            ```

        Args:
            i_reading_buffer (optional): A reading buffer object where current readings are stored.
            v_reading_buffer (optional): A reading buffer object where voltage readings are stored.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    i_reading_buffer,
                    v_reading_buffer,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.iv({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.iv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def p(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``smuX.measure.p()`` function.

        Description:
            - This function makes one or more measurements. (p = power in watts)

        TSP Syntax:
            ```
            - smuX.measure.p()
            ```

        Args:
            reading_buffer (optional): A reading buffer object where all readings are stored.

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
        """Run the ``smuX.measure.r()`` function.

        Description:
            - This function makes one or more measurements. (r = resistance in ohms)

        TSP Syntax:
            ```
            - smuX.measure.r()
            ```

        Args:
            reading_buffer (optional): A reading buffer object where all readings are stored.

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
        """Run the ``smuX.measure.v()`` function.

        Description:
            - This function makes one or more measurements. (v = voltage in volts)

        TSP Syntax:
            ```
            - smuX.measure.v()
            ```

        Args:
            reading_buffer (optional): A reading buffer object where all readings are stored.

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

    def calibratei(
        self,
        range_: str,
        cp1_measured: str,
        cp1_reference: str,
        cp2_measured: str,
        cp2_reference: str,
    ) -> None:
        """Run the ``smuX.measure.calibratei()`` function.

        Description:
            - This function generates and activates new measurement calibration constants. (i =
              current in amperes)

        TSP Syntax:
            ```
            - smuX.measure.calibratei()
            ```

        Args:
            range_: The measurement range to adjust.
            cp1_measured: The value measured by this SMU for point 1.
            cp1_reference: The reference measurement for point 1 as measured externally.
            cp2_measured: The value measured by this SMU for point 2.
            cp2_reference: The reference measurement for point 2 as measured externally.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.calibratei({range_}, "
                f"{cp1_measured}, "
                f"{cp1_reference}, "
                f"{cp2_measured}, "
                f"{cp2_reference})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.calibratei()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def calibratev(
        self,
        range_: str,
        cp1_measured: str,
        cp1_reference: str,
        cp2_measured: str,
        cp2_reference: str,
    ) -> None:
        """Run the ``smuX.measure.calibratev()`` function.

        Description:
            - This function generates and activates new measurement calibration constants. (v =
              voltage in volts)

        TSP Syntax:
            ```
            - smuX.measure.calibratev()
            ```

        Args:
            range_: The measurement range to adjust.
            cp1_measured: The value measured by this SMU for point 1.
            cp1_reference: The reference measurement for point 1 as measured externally.
            cp2_measured: The value measured by this SMU for point 2.
            cp2_reference: The reference measurement for point 2 as measured externally.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.calibratev({range_}, "
                f"{cp1_measured}, "
                f"{cp1_reference}, "
                f"{cp2_measured}, "
                f"{cp2_reference})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.calibratev()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedi(self, rbuffer: str) -> None:
        """Run the ``smuX.measure.overlappedi()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes)

        TSP Syntax:
            ```
            - smuX.measure.overlappedi()
            ```

        Args:
            rbuffer: A reading buffer object where the readings are stored.

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
        """Run the ``smuX.measure.overlappediv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - smuX.measure.overlappediv()
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
        """Run the ``smuX.measure.overlappedp()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (p = power in watts)

        TSP Syntax:
            ```
            - smuX.measure.overlappedp()
            ```

        Args:
            rbuffer: A reading buffer object where the readings are stored.

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
        """Run the ``smuX.measure.overlappedr()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (r = resistance in
              ohms)

        TSP Syntax:
            ```
            - smuX.measure.overlappedr()
            ```

        Args:
            rbuffer: A reading buffer object where the readings are stored.

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
        """Run the ``smuX.measure.overlappedv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (v = voltage in volts)

        TSP Syntax:
            ```
            - smuX.measure.overlappedv()
            ```

        Args:
            rbuffer: A reading buffer object where the readings are stored.

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


class SmuxItemContact(BaseTSPCmd):
    """The ``smuX.contact`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.contact.calibratehi()
          applies to SMU channel A).

    Properties and methods:
        - ``.calibratehi()``: The ``smuX.contact.calibratehi()`` function.
        - ``.calibratelo()``: The ``smuX.contact.calibratelo()`` function.
        - ``.check()``: The ``smuX.contact.check()`` function.
        - ``.r()``: The ``smuX.contact.r()`` function.
        - ``.speed``: The ``smuX.contact.speed`` attribute.
        - ``.threshold``: The ``smuX.contact.threshold`` attribute.
    """

    @property
    def speed(self) -> str:
        """Access the ``smuX.contact.speed`` attribute.

        Description:
            - This attribute stores the speed setting for contact check measurements. This command
              is not available on the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(smuX.contact.speed)`` query.
            - Setting this property to a value will send the ``smuX.contact.speed = value`` command.

        TSP Syntax:
            ```
            - smuX.contact.speed = value
            - print(smuX.contact.speed)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.contact.speed applies
              to SMU channel A).

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
        """Access the ``smuX.contact.speed`` attribute.

        Description:
            - This attribute stores the speed setting for contact check measurements. This command
              is not available on the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(smuX.contact.speed)`` query.
            - Setting this property to a value will send the ``smuX.contact.speed = value`` command.

        TSP Syntax:
            ```
            - smuX.contact.speed = value
            - print(smuX.contact.speed)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.contact.speed applies
              to SMU channel A).

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
        """Access the ``smuX.contact.threshold`` attribute.

        Description:
            - This attribute stores the resistance threshold for the smuX.contact.check() function.
              This command is not available on the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(smuX.contact.threshold)`` query.
            - Setting this property to a value will send the ``smuX.contact.threshold = value``
              command.

        TSP Syntax:
            ```
            - smuX.contact.threshold = value
            - print(smuX.contact.threshold)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.contact.threshold
              applies to SMU channel A).

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
        """Access the ``smuX.contact.threshold`` attribute.

        Description:
            - This attribute stores the resistance threshold for the smuX.contact.check() function.
              This command is not available on the 2604B, 2614B, or 2634B.

        Usage:
            - Accessing this property will send the ``print(smuX.contact.threshold)`` query.
            - Setting this property to a value will send the ``smuX.contact.threshold = value``
              command.

        TSP Syntax:
            ```
            - smuX.contact.threshold = value
            - print(smuX.contact.threshold)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.contact.threshold
              applies to SMU channel A).

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
        """Run the ``smuX.contact.calibratehi()`` function.

        Description:
            - This function adjusts the high/sense high contact check measurement. This command is
              not available on the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - smuX.contact.calibratehi()
            ```

        Args:
            cp1_measured: The value measured by this SMU for point 1.
            cp1_reference: The reference measurement for point 1 as measured externally.
            cp2_measured: The value measured by this SMU for point 2.
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
        """Run the ``smuX.contact.calibratelo()`` function.

        Description:
            - This function adjusts the low/sense low contact check measurement. This command is not
              available on the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - smuX.contact.calibratelo()
            ```

        Args:
            cp1_measured: The value measured by this SMU for point 1.
            cp1_reference: The reference measurement for point 1 as measured externally.
            cp2_measured: The value measured by this SMU for point 2.
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

    def check(self) -> None:
        """Run the ``smuX.contact.check()`` function.

        Description:
            - This function determines if contact resistance is lower than the threshold. This
              command is not available on the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - smuX.contact.check()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.contact.check()
              applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.check()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.check()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def r(self) -> str:
        """Run the ``smuX.contact.r()`` function.

        Description:
            - This function measures aggregate contact resistance. This command is not available on
              the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - smuX.contact.r()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.contact.r() applies to
              SMU channel A).

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


class SmuxItemCal(BaseTSPCmd):
    """The ``smuX.cal`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.adjustdate applies to
          SMU channel A).

    Properties and methods:
        - ``.adjustdate``: The ``smuX.cal.adjustdate`` attribute.
        - ``.date``: The ``smuX.cal.date`` attribute.
        - ``.due``: The ``smuX.cal.due`` attribute.
        - ``.lock()``: The ``smuX.cal.lock()`` function.
        - ``.password``: The ``smuX.cal.password`` attribute.
        - ``.polarity``: The ``smuX.cal.polarity`` attribute.
        - ``.restore()``: The ``smuX.cal.restore()`` function.
        - ``.save()``: The ``smuX.cal.save()`` function.
        - ``.state``: The ``smuX.cal.state`` attribute.
        - ``.unlock()``: The ``smuX.cal.unlock()`` function.
    """

    @property
    def adjustdate(self) -> str:
        """Access the ``smuX.cal.adjustdate`` attribute.

        Description:
            - This attribute stores the date of the last calibration adjustment.

        Usage:
            - Accessing this property will send the ``print(smuX.cal.adjustdate)`` query.
            - Setting this property to a value will send the ``smuX.cal.adjustdate = value``
              command.

        TSP Syntax:
            ```
            - smuX.cal.adjustdate = value
            - print(smuX.cal.adjustdate)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.adjustdate applies
              to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".adjustdate"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.adjustdate)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.adjustdate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @adjustdate.setter
    def adjustdate(self, value: Union[str, float]) -> None:
        """Access the ``smuX.cal.adjustdate`` attribute.

        Description:
            - This attribute stores the date of the last calibration adjustment.

        Usage:
            - Accessing this property will send the ``print(smuX.cal.adjustdate)`` query.
            - Setting this property to a value will send the ``smuX.cal.adjustdate = value``
              command.

        TSP Syntax:
            ```
            - smuX.cal.adjustdate = value
            - print(smuX.cal.adjustdate)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.adjustdate applies
              to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".adjustdate", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.adjustdate = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.adjustdate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def date(self) -> str:
        """Access the ``smuX.cal.date`` attribute.

        Description:
            - This attribute stores the calibration date of the active calibration set.

        Usage:
            - Accessing this property will send the ``print(smuX.cal.date)`` query.
            - Setting this property to a value will send the ``smuX.cal.date = value`` command.

        TSP Syntax:
            ```
            - smuX.cal.date = value
            - print(smuX.cal.date)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.date applies to
              SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".date"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.date)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.date`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @date.setter
    def date(self, value: Union[str, float]) -> None:
        """Access the ``smuX.cal.date`` attribute.

        Description:
            - This attribute stores the calibration date of the active calibration set.

        Usage:
            - Accessing this property will send the ``print(smuX.cal.date)`` query.
            - Setting this property to a value will send the ``smuX.cal.date = value`` command.

        TSP Syntax:
            ```
            - smuX.cal.date = value
            - print(smuX.cal.date)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.date applies to
              SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".date", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.date = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.date`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def due(self) -> str:
        """Access the ``smuX.cal.due`` attribute.

        Description:
            - This attribute stores the calibration due date for the next calibration.

        Usage:
            - Accessing this property will send the ``print(smuX.cal.due)`` query.
            - Setting this property to a value will send the ``smuX.cal.due = value`` command.

        TSP Syntax:
            ```
            - smuX.cal.due = value
            - print(smuX.cal.due)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.due applies to SMU
              channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".due"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.due)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.due`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @due.setter
    def due(self, value: Union[str, float]) -> None:
        """Access the ``smuX.cal.due`` attribute.

        Description:
            - This attribute stores the calibration due date for the next calibration.

        Usage:
            - Accessing this property will send the ``print(smuX.cal.due)`` query.
            - Setting this property to a value will send the ``smuX.cal.due = value`` command.

        TSP Syntax:
            ```
            - smuX.cal.due = value
            - print(smuX.cal.due)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.due applies to SMU
              channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".due", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.due = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.due`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def password(self) -> str:
        """Access the ``smuX.cal.password`` attribute.

        Description:
            - This attribute stores the password required to enable calibration.

        Usage:
            - Setting this property to a value will send the ``smuX.cal.password = value`` command.

        TSP Syntax:
            ```
            - smuX.cal.password = value
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.cal.password applies to SMU channel A).

        Raises:
            AttributeError: Indicates that this attribute is write-only.
        """
        if self._device.command_syntax_enabled:  # type: ignore[union-attr]
            return self._cmd_syntax + ".password"
        msg = f"``{self._cmd_syntax}.password`` is a write-only attribute."
        raise AttributeError(msg)

    @password.setter
    def password(self, value: Union[str, float]) -> None:
        """Access the ``smuX.cal.password`` attribute.

        Description:
            - This attribute stores the password required to enable calibration.

        Usage:
            - Setting this property to a value will send the ``smuX.cal.password = value`` command.

        TSP Syntax:
            ```
            - smuX.cal.password = value
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.cal.password applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.password = {value}"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.password`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def polarity(self) -> str:
        """Access the ``smuX.cal.polarity`` attribute.

        Description:
            - This attribute controls which calibration constants are used for all subsequent
              measurements.

        Usage:
            - Accessing this property will send the ``print(smuX.cal.polarity)`` query.
            - Setting this property to a value will send the ``smuX.cal.polarity = value`` command.

        TSP Syntax:
            ```
            - smuX.cal.polarity = value
            - print(smuX.cal.polarity)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.cal.polarity applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".polarity"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.polarity)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.polarity`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @polarity.setter
    def polarity(self, value: Union[str, float]) -> None:
        """Access the ``smuX.cal.polarity`` attribute.

        Description:
            - This attribute controls which calibration constants are used for all subsequent
              measurements.

        Usage:
            - Accessing this property will send the ``print(smuX.cal.polarity)`` query.
            - Setting this property to a value will send the ``smuX.cal.polarity = value`` command.

        TSP Syntax:
            ```
            - smuX.cal.polarity = value
            - print(smuX.cal.polarity)
            ```

        Info:
            - ``X``, the sMU channel (for example, smua.cal.polarity applies to SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".polarity", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.polarity = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.polarity`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def state(self) -> str:
        """Access the ``smuX.cal.state`` attribute.

        Description:
            - This attribute returns the present calibration state.

        Usage:
            - Accessing this property will send the ``print(smuX.cal.state)`` query.

        TSP Syntax:
            ```
            - print(smuX.cal.state)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.state applies to
              SMU channel A).

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

    def lock(self) -> None:
        """Run the ``smuX.cal.lock()`` function.

        Description:
            - This function disables the commands that change calibration settings.

        TSP Syntax:
            ```
            - smuX.cal.lock()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.lock() specifies
              SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.lock()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.lock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def restore(self, calset: Optional[str] = None) -> None:
        """Run the ``smuX.cal.restore()`` function.

        Description:
            - This function loads a stored set of calibration constants.

        TSP Syntax:
            ```
            - smuX.cal.restore()
            ```

        Args:
            calset (optional): The calibration set to be loaded; set calset to one of the following
                values.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (calset,) if x is not None)
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.restore({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.restore()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def save(self) -> None:
        """Run the ``smuX.cal.save()`` function.

        Description:
            - This function stores the active calibration constants to nonvolatile memory.

        TSP Syntax:
            ```
            - smuX.cal.save()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.save() applies to
              SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.save()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.save()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def unlock(self, password: str) -> None:
        """Run the ``smuX.cal.unlock()`` function.

        Description:
            - This function enables the commands that change calibration settings.

        TSP Syntax:
            ```
            - smuX.cal.unlock()
            ```

        Args:
            password: Calibration password.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.unlock({password})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.unlock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuxItemBuffer(BaseTSPCmd):
    """The ``smuX.buffer`` command tree.

    Info:
        - ``X``, the source-measure unit (SMU) channel (for example, smua.buffer.getstats()
          specifies SMU channel A).

    Properties and methods:
        - ``.getstats()``: The ``smuX.buffer.getstats()`` function.
        - ``.recalculatestats()``: The ``smuX.buffer.recalculatestats()`` function.
    """

    def getstats(self, buffer_var: str) -> Dict[Any, Any]:
        """Run the ``smuX.buffer.getstats()`` function.

        Description:
            - This function returns the statistics for a specified reading buffer.

        TSP Syntax:
            ```
            - smuX.buffer.getstats()
            ```

        Args:
            buffer_var: The reading buffer to process.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"tempvar = {self._cmd_syntax}.getstats({buffer_var})"
            )
            retval = self._get_tsp_table_dict("tempvar")
            self._device.write("tempvar = nil")  # type: ignore[union-attr]
            return retval  # noqa: TRY300
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getstats()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def recalculatestats(self, buffer_var: str) -> None:
        """Run the ``smuX.buffer.recalculatestats()`` function.

        Description:
            - This function recalculates the statistics of the specified reading buffer.

        TSP Syntax:
            ```
            - smuX.buffer.recalculatestats()
            ```

        Args:
            buffer_var: The reading buffer to process.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.recalculatestats({buffer_var})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recalculatestats()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


#  pylint: disable=too-many-instance-attributes
class SmuxItem(ValidatedChannel, BaseTSPCmd):
    """The ``smuX`` command tree.

    Constants:
        - ``.ASYNC``: Make measurements during the sweep, but asynchronously with the source area of
          the trigger model.
        - ``.AUTORANGE_FOLLOW_LIMIT``: Set the measure range to the limit range.
        - ``.AUTORANGE_OFF``: Disable autorange.
        - ``.AUTORANGE_ON``: Enable autorange.
        - ``.AUTOZERO_AUTO``: Automatically check reference and zero measurements and perform an
          autozero when needed.
        - ``.AUTOZERO_OFF``: Disable autozero.
        - ``.AUTOZERO_ONCE``: Performs autozero once, then disables autozero.
        - ``.CALSET_DEFAULT``: Load normal calibration constants.
        - ``.CALSET_FACTORY``: Load calibration constants when the instrument left the factory.
        - ``.CALSET_NOMINAL``: Load calibration constants that are uncalibrated, but set to nominal
          values to allow rudimentary functioning of the instrument.
        - ``.CALSET_PREVIOUS``: Load the calibration constants that were used before the last
          default set was overwritten.
        - ``.CALSTATE_CALIBRATING``: Calibration constants or dates have been changed but not yet
          saved to nonvolatile memory.
        - ``.CALSTATE_LOCKED``: Calibration is locked.
        - ``.CALSTATE_UNLOCKED``: Calibration is unlocked but none of the calibration constants or
          dates have changed since the last save/restore.
        - ``.CAL_AUTO``: Use automatic polarity detection for calibration constants.
        - ``.CAL_NEGATIVE``: Measure with negative polarity calibration constants.
        - ``.CAL_POSITIVE``: Measure with positive polarity calibration constants.
        - ``.CONTACT_FAST``: Select the fast speed setting.
        - ``.CONTACT_MEDIUM``: Select the medium speed setting.
        - ``.CONTACT_SLOW``: Select the slow speed setting.
        - ``.DELAY_AUTO``: Use the automatic delay value.
        - ``.DELAY_OFF``: Do not include a delay before measurements.
        - ``.DISABLE``: Use conventional pulsing and full source-measure unit (SMU) functionality.
        - ``.ENABLE``: Allow fast-edge pulsing using the trigger model.
        - ``.FILL_ONCE``: Set the reading buffer fill mode to not overwrite old data.
        - ``.FILL_WINDOW``: Set the reading buffer fill mode to restart new readings at index 1
          after acquiring
          reading at index bufferVar.fillcount.
        - ``.FILTER_MEDIAN``: Selects the median filter when measurement filter is enabled.
        - ``.FILTER_MOVING_AVG``: Selects the moving filter when measurement filter is enabled.
        - ``.FILTER_OFF``: Disable filter measurements.
        - ``.FILTER_ON``: Enable filter measurements.
        - ``.FILTER_REPEAT_AVG``: Selects the repeating filter when measurement filter is enabled.
        - ``.LIMIT_AUTO``: Set the sweep source limit to automatic.
        - ``.OE_NONE``: When output enable is deasserted, take no action.
        - ``.OE_OUTPUT_OFF``: When output enable is deasserted, turn the source output off.
        - ``.OUTPUT_DCAMPS``: Select the current function for the pulse.
        - ``.OUTPUT_DCVOLTS``: Select the voltage function for the pulse.
        - ``.OUTPUT_HIGH_Z``: Opens the output relay when the output is turned off.
        - ``.OUTPUT_NORMAL``: Configures the source function according to smuX.source.offfunc
          attribute.
        - ``.OUTPUT_OFF``: Turns off the source output.
        - ``.OUTPUT_ON``: Turn on the source output.
        - ``.OUTPUT_ZERO``: Configures source to output 0 V as smuX.OUTPUT_NORMAL with different
          compliance handling.
        - ``.REL_OFF``: Disables relative measurements.
        - ``.REL_ON``: Enables relative measurements.
        - ``.SENSE_CALA``: Set the sense mode to calibration.
        - ``.SENSE_LOCAL``: Set the sense mode to local sense (2-wire).
        - ``.SENSE_REMOTE``: Set the sense mode to remote sense (4-wire).
        - ``.SETTLE_DIRECT_IRANGE``: Instructs the SMU to change the current range directly.
        - ``.SETTLE_FAST_ALL``: Enable the smuX.SETTLE_FAST_RANGE and smuX.SETTLE_FASTPOLARITY
          operations.
        - ``.SETTLE_FAST_POLARITY``: Instructs the SMU to change polarity without going to zero.
        - ``.SETTLE_FAST_RANGE``: Instructs the source-measure unit (SMU) to use a faster procedure
          when changing ranges.
        - ``.SETTLE_SMOOTH``: Turn off additional settling operations.
        - ``.SOURCE_HOLD``: Disables pulse mode sweeps, holding the source level for the remainder
          of the step.
        - ``.SOURCE_IDLE``: Sets the source level to the programmed (idle) level at the end of the
          pulse.

    Properties and methods:
        - ``.abort()``: The ``smuX.abort()`` function.
        - ``.buffer``: The ``smuX.buffer`` command tree.
        - ``.cal``: The ``smuX.cal`` command tree.
        - ``.contact``: The ``smuX.contact`` command tree.
        - ``.makebuffer()``: The ``smuX.makebuffer()`` function.
        - ``.measure``: The ``smuX.measure`` command tree.
        - ``.measureiandstep()``: The ``smuX.measureiandstep()`` function.
        - ``.measureivandstep()``: The ``smuX.measureivandstep()`` function.
        - ``.measurepandstep()``: The ``smuX.measurepandstep()`` function.
        - ``.measurerandstep()``: The ``smuX.measurerandstep()`` function.
        - ``.measurevandstep()``: The ``smuX.measurevandstep()`` function.
        - ``.nvbuffer1``: The ``smuX.nvbuffer1`` attribute.
        - ``.nvbuffer2``: The ``smuX.nvbuffer2`` attribute.
        - ``.reset()``: The ``smuX.reset()`` function.
        - ``.savebuffer()``: The ``smuX.savebuffer()`` function.
        - ``.sense``: The ``smuX.sense`` attribute.
        - ``.source``: The ``smuX.source`` command tree.
        - ``.trigger``: The ``smuX.trigger`` command tree.
    """

    ASYNC = "smuX.ASYNC"
    """str: Make measurements during the sweep, but asynchronously with the source area of the trigger model."""  # noqa: E501
    AUTORANGE_FOLLOW_LIMIT = "smuX.AUTORANGE_FOLLOW_LIMIT"
    """str: Set the measure range to the limit range."""
    AUTORANGE_OFF = "smuX.AUTORANGE_OFF"
    """str: Disable autorange."""
    AUTORANGE_ON = "smuX.AUTORANGE_ON"
    """str: Enable autorange."""
    AUTOZERO_AUTO = "smuX.AUTOZERO_AUTO"
    """str: Automatically check reference and zero measurements and perform an autozero when needed."""  # noqa: E501
    AUTOZERO_OFF = "smuX.AUTOZERO_OFF"
    """str: Disable autozero."""
    AUTOZERO_ONCE = "smuX.AUTOZERO_ONCE"
    """str: Performs autozero once, then disables autozero."""
    CALSET_DEFAULT = "smuX.CALSET_DEFAULT"
    """str: Load normal calibration constants."""
    CALSET_FACTORY = "smuX.CALSET_FACTORY"
    """str: Load calibration constants when the instrument left the factory."""
    CALSET_NOMINAL = "smuX.CALSET_NOMINAL"
    """str: Load calibration constants that are uncalibrated, but set to nominal values to allow rudimentary functioning of the instrument."""  # noqa: E501
    CALSET_PREVIOUS = "smuX.CALSET_PREVIOUS"
    """str: Load the calibration constants that were used before the last default set was overwritten."""  # noqa: E501
    CALSTATE_CALIBRATING = "smuX.CALSTATE_CALIBRATING"
    """str: Calibration constants or dates have been changed but not yet saved to nonvolatile memory."""  # noqa: E501
    CALSTATE_LOCKED = "smuX.CALSTATE_LOCKED"
    """str: Calibration is locked."""
    CALSTATE_UNLOCKED = "smuX.CALSTATE_UNLOCKED"
    """str: Calibration is unlocked but none of the calibration constants or dates have changed since the last save/restore."""  # noqa: E501
    CAL_AUTO = "smuX.CAL_AUTO"
    """str: Use automatic polarity detection for calibration constants."""
    CAL_NEGATIVE = "smuX.CAL_NEGATIVE"
    """str: Measure with negative polarity calibration constants."""
    CAL_POSITIVE = "smuX.CAL_POSITIVE"
    """str: Measure with positive polarity calibration constants."""
    CONTACT_FAST = "smuX.CONTACT_FAST"
    """str: Select the fast speed setting."""
    CONTACT_MEDIUM = "smuX.CONTACT_MEDIUM"
    """str: Select the medium speed setting."""
    CONTACT_SLOW = "smuX.CONTACT_SLOW"
    """str: Select the slow speed setting."""
    DELAY_AUTO = "smuX.DELAY_AUTO"
    """str: Use the automatic delay value."""
    DELAY_OFF = "smuX.DELAY_OFF"
    """str: Do not include a delay before measurements."""
    DISABLE = "smuX.DISABLE"
    """str: Use conventional pulsing and full source-measure unit (SMU) functionality."""
    ENABLE = "smuX.ENABLE"
    """str: Allow fast-edge pulsing using the trigger model."""
    FILL_ONCE = "smuX.FILL_ONCE"
    """str: Set the reading buffer fill mode to not overwrite old data."""
    FILL_WINDOW = "smuX.FILL_WINDOW"
    """str: Set the reading buffer fill mode to restart new readings at index 1 after acquiring
reading at index bufferVar.fillcount."""
    FILTER_MEDIAN = "smuX.FILTER_MEDIAN"
    """str: Selects the median filter when measurement filter is enabled."""
    FILTER_MOVING_AVG = "smuX.FILTER_MOVING_AVG"
    """str: Selects the moving filter when measurement filter is enabled."""
    FILTER_OFF = "smuX.FILTER_OFF"
    """str: Disable filter measurements."""
    FILTER_ON = "smuX.FILTER_ON"
    """str: Enable filter measurements."""
    FILTER_REPEAT_AVG = "smuX.FILTER_REPEAT_AVG"
    """str: Selects the repeating filter when measurement filter is enabled."""
    LIMIT_AUTO = "smuX.LIMIT_AUTO"
    """str: Set the sweep source limit to automatic."""
    OE_NONE = "smuX.OE_NONE"
    """str: When output enable is deasserted, take no action."""
    OE_OUTPUT_OFF = "smuX.OE_OUTPUT_OFF"
    """str: When output enable is deasserted, turn the source output off."""
    OUTPUT_DCAMPS = "smuX.OUTPUT_DCAMPS"
    """str: Select the current function for the pulse."""
    OUTPUT_DCVOLTS = "smuX.OUTPUT_DCVOLTS"
    """str: Select the voltage function for the pulse."""
    OUTPUT_HIGH_Z = "smuX.OUTPUT_HIGH_Z"
    """str: Opens the output relay when the output is turned off."""
    OUTPUT_NORMAL = "smuX.OUTPUT_NORMAL"
    """str: Configures the source function according to smuX.source.offfunc attribute."""
    OUTPUT_OFF = "smuX.OUTPUT_OFF"
    """str: Turns off the source output."""
    OUTPUT_ON = "smuX.OUTPUT_ON"
    """str: Turn on the source output."""
    OUTPUT_ZERO = "smuX.OUTPUT_ZERO"
    """str: Configures source to output 0 V as smuX.OUTPUT_NORMAL with different compliance handling."""  # noqa: E501
    REL_OFF = "smuX.REL_OFF"
    """str: Disables relative measurements."""
    REL_ON = "smuX.REL_ON"
    """str: Enables relative measurements."""
    SENSE_CALA = "smuX.SENSE_CALA"
    """str: Set the sense mode to calibration."""
    SENSE_LOCAL = "smuX.SENSE_LOCAL"
    """str: Set the sense mode to local sense (2-wire)."""
    SENSE_REMOTE = "smuX.SENSE_REMOTE"
    """str: Set the sense mode to remote sense (4-wire)."""
    SETTLE_DIRECT_IRANGE = "smuX.SETTLE_DIRECT_IRANGE"
    """str: Instructs the SMU to change the current range directly."""
    SETTLE_FAST_ALL = "smuX.SETTLE_FAST_ALL"
    """str: Enable the smuX.SETTLE_FAST_RANGE and smuX.SETTLE_FASTPOLARITY operations."""
    SETTLE_FAST_POLARITY = "smuX.SETTLE_FAST_POLARITY"
    """str: Instructs the SMU to change polarity without going to zero."""
    SETTLE_FAST_RANGE = "smuX.SETTLE_FAST_RANGE"
    """str: Instructs the source-measure unit (SMU) to use a faster procedure when changing ranges."""  # noqa: E501
    SETTLE_SMOOTH = "smuX.SETTLE_SMOOTH"
    """str: Turn off additional settling operations."""
    SOURCE_HOLD = "smuX.SOURCE_HOLD"
    """str: Disables pulse mode sweeps, holding the source level for the remainder of the step."""
    SOURCE_IDLE = "smuX.SOURCE_IDLE"
    """str: Sets the source level to the programmed (idle) level at the end of the pulse."""

    # pylint: disable=too-many-statements
    def __init__(  # noqa: PLR0915
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "smuX"
    ) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.ASYNC = self.ASYNC.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.AUTORANGE_FOLLOW_LIMIT = self.AUTORANGE_FOLLOW_LIMIT.replace(
            "smuX", f"smu{self._cmd_syntax[3]}"
        )
        # pylint: disable=invalid-name
        self.AUTORANGE_OFF = self.AUTORANGE_OFF.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.AUTORANGE_ON = self.AUTORANGE_ON.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.AUTOZERO_AUTO = self.AUTOZERO_AUTO.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.AUTOZERO_OFF = self.AUTOZERO_OFF.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.AUTOZERO_ONCE = self.AUTOZERO_ONCE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CALSET_DEFAULT = self.CALSET_DEFAULT.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CALSET_FACTORY = self.CALSET_FACTORY.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CALSET_NOMINAL = self.CALSET_NOMINAL.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CALSET_PREVIOUS = self.CALSET_PREVIOUS.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CALSTATE_CALIBRATING = self.CALSTATE_CALIBRATING.replace(
            "smuX", f"smu{self._cmd_syntax[3]}"
        )
        # pylint: disable=invalid-name
        self.CALSTATE_LOCKED = self.CALSTATE_LOCKED.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CALSTATE_UNLOCKED = self.CALSTATE_UNLOCKED.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CAL_AUTO = self.CAL_AUTO.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CAL_NEGATIVE = self.CAL_NEGATIVE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CAL_POSITIVE = self.CAL_POSITIVE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CONTACT_FAST = self.CONTACT_FAST.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CONTACT_MEDIUM = self.CONTACT_MEDIUM.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.CONTACT_SLOW = self.CONTACT_SLOW.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.DELAY_AUTO = self.DELAY_AUTO.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.DELAY_OFF = self.DELAY_OFF.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.DISABLE = self.DISABLE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.ENABLE = self.ENABLE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.FILL_ONCE = self.FILL_ONCE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.FILL_WINDOW = self.FILL_WINDOW.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.FILTER_MEDIAN = self.FILTER_MEDIAN.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.FILTER_MOVING_AVG = self.FILTER_MOVING_AVG.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.FILTER_OFF = self.FILTER_OFF.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.FILTER_ON = self.FILTER_ON.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.FILTER_REPEAT_AVG = self.FILTER_REPEAT_AVG.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.LIMIT_AUTO = self.LIMIT_AUTO.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OE_NONE = self.OE_NONE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OE_OUTPUT_OFF = self.OE_OUTPUT_OFF.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OUTPUT_DCAMPS = self.OUTPUT_DCAMPS.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OUTPUT_DCVOLTS = self.OUTPUT_DCVOLTS.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OUTPUT_HIGH_Z = self.OUTPUT_HIGH_Z.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OUTPUT_NORMAL = self.OUTPUT_NORMAL.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OUTPUT_OFF = self.OUTPUT_OFF.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OUTPUT_ON = self.OUTPUT_ON.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.OUTPUT_ZERO = self.OUTPUT_ZERO.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.REL_OFF = self.REL_OFF.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.REL_ON = self.REL_ON.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SENSE_CALA = self.SENSE_CALA.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SENSE_LOCAL = self.SENSE_LOCAL.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SENSE_REMOTE = self.SENSE_REMOTE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SETTLE_DIRECT_IRANGE = self.SETTLE_DIRECT_IRANGE.replace(
            "smuX", f"smu{self._cmd_syntax[3]}"
        )
        # pylint: disable=invalid-name
        self.SETTLE_FAST_ALL = self.SETTLE_FAST_ALL.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SETTLE_FAST_POLARITY = self.SETTLE_FAST_POLARITY.replace(
            "smuX", f"smu{self._cmd_syntax[3]}"
        )
        # pylint: disable=invalid-name
        self.SETTLE_FAST_RANGE = self.SETTLE_FAST_RANGE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SETTLE_SMOOTH = self.SETTLE_SMOOTH.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SOURCE_HOLD = self.SOURCE_HOLD.replace("smuX", f"smu{self._cmd_syntax[3]}")
        # pylint: disable=invalid-name
        self.SOURCE_IDLE = self.SOURCE_IDLE.replace("smuX", f"smu{self._cmd_syntax[3]}")
        self._buffer = SmuxItemBuffer(device, f"{self._cmd_syntax}.buffer")
        self._cal = SmuxItemCal(device, f"{self._cmd_syntax}.cal")
        self._contact = SmuxItemContact(device, f"{self._cmd_syntax}.contact")
        self._measure = SmuxItemMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = SmuxItemSource(device, f"{self._cmd_syntax}.source")
        self._trigger = SmuxItemTrigger(device, f"{self._cmd_syntax}.trigger")

    @property
    def buffer(self) -> SmuxItemBuffer:
        """Return the ``smuX.buffer`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.buffer.getstats()
              specifies SMU channel A).

        Sub-properties and sub-methods:
            - ``.getstats()``: The ``smuX.buffer.getstats()`` function.
            - ``.recalculatestats()``: The ``smuX.buffer.recalculatestats()`` function.
        """
        return self._buffer

    @property
    def cal(self) -> SmuxItemCal:
        """Return the ``smuX.cal`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.cal.adjustdate applies
              to SMU channel A).

        Sub-properties and sub-methods:
            - ``.adjustdate``: The ``smuX.cal.adjustdate`` attribute.
            - ``.date``: The ``smuX.cal.date`` attribute.
            - ``.due``: The ``smuX.cal.due`` attribute.
            - ``.lock()``: The ``smuX.cal.lock()`` function.
            - ``.password``: The ``smuX.cal.password`` attribute.
            - ``.polarity``: The ``smuX.cal.polarity`` attribute.
            - ``.restore()``: The ``smuX.cal.restore()`` function.
            - ``.save()``: The ``smuX.cal.save()`` function.
            - ``.state``: The ``smuX.cal.state`` attribute.
            - ``.unlock()``: The ``smuX.cal.unlock()`` function.
        """
        return self._cal

    @property
    def contact(self) -> SmuxItemContact:
        """Return the ``smuX.contact`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.contact.calibratehi()
              applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.calibratehi()``: The ``smuX.contact.calibratehi()`` function.
            - ``.calibratelo()``: The ``smuX.contact.calibratelo()`` function.
            - ``.check()``: The ``smuX.contact.check()`` function.
            - ``.r()``: The ``smuX.contact.r()`` function.
            - ``.speed``: The ``smuX.contact.speed`` attribute.
            - ``.threshold``: The ``smuX.contact.threshold`` attribute.
        """
        return self._contact

    @property
    def measure(self) -> SmuxItemMeasure:
        """Return the ``smuX.measure`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.measure.v() applies to
              SMU channel A).

        Sub-properties and sub-methods:
            - ``.i()``: The ``smuX.measure.i()`` function.
            - ``.iv()``: The ``smuX.measure.iv()`` function.
            - ``.p()``: The ``smuX.measure.p()`` function.
            - ``.r()``: The ``smuX.measure.r()`` function.
            - ``.v()``: The ``smuX.measure.v()`` function.
            - ``.analogfilter``: The ``smuX.measure.analogfilter`` attribute.
            - ``.autorangei``: The ``smuX.measure.autorangei`` attribute.
            - ``.autorangev``: The ``smuX.measure.autorangev`` attribute.
            - ``.autozero``: The ``smuX.measure.autozero`` attribute.
            - ``.calibratei()``: The ``smuX.measure.calibratei()`` function.
            - ``.calibratev()``: The ``smuX.measure.calibratev()`` function.
            - ``.count``: The ``smuX.measure.count`` attribute.
            - ``.delay``: The ``smuX.measure.delay`` attribute.
            - ``.delayfactor``: The ``smuX.measure.delayfactor`` attribute.
            - ``.filter``: The ``smuX.measure.filter`` command tree.
            - ``.highcrangedelayfactor``: The ``smuX.measure.highcrangedelayfactor`` attribute.
            - ``.interval``: The ``smuX.measure.interval`` attribute.
            - ``.lowrangei``: The ``smuX.measure.lowrangei`` attribute.
            - ``.lowrangev``: The ``smuX.measure.lowrangev`` attribute.
            - ``.nplc``: The ``smuX.measure.nplc`` attribute.
            - ``.overlappedi()``: The ``smuX.measure.overlappedi()`` function.
            - ``.overlappediv()``: The ``smuX.measure.overlappediv()`` function.
            - ``.overlappedp()``: The ``smuX.measure.overlappedp()`` function.
            - ``.overlappedr()``: The ``smuX.measure.overlappedr()`` function.
            - ``.overlappedv()``: The ``smuX.measure.overlappedv()`` function.
            - ``.rangei``: The ``smuX.measure.rangei`` attribute.
            - ``.rangev``: The ``smuX.measure.rangev`` attribute.
            - ``.rel``: The ``smuX.measure.rel`` command tree.
        """
        return self._measure

    @property
    def nvbuffer1(self) -> str:
        """Access the ``smuX.nvbuffer1`` attribute.

        Description:
            - This attribute contains a dedicated reading buffer. (1 = default buffer1)

        Usage:
            - Accessing this property will send the ``print(smuX.nvbuffer1)`` query.

        TSP Syntax:
            ```
            - print(smuX.nvbuffer1)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.nvbuffer1 applies to
              SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".nvbuffer1"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.nvbuffer1)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.nvbuffer1`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def nvbuffer2(self) -> str:
        """Access the ``smuX.nvbuffer2`` attribute.

        Description:
            - This attribute contains a dedicated reading buffer. (2 = default buffer2)

        Usage:
            - Accessing this property will send the ``print(smuX.nvbuffer2)`` query.

        TSP Syntax:
            ```
            - print(smuX.nvbuffer2)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.nvbuffer1 applies to
              SMU channel A).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".nvbuffer2"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.nvbuffer2)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.nvbuffer2`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def sense(self) -> str:
        """Access the ``smuX.sense`` attribute.

        Description:
            - This attribute contains the state of the sense mode.

        Usage:
            - Accessing this property will send the ``print(smuX.sense)`` query.
            - Setting this property to a value will send the ``smuX.sense = value`` command.

        TSP Syntax:
            ```
            - smuX.sense = value
            - print(smuX.sense)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.sense applies to SMU
              channel A).

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
        """Access the ``smuX.sense`` attribute.

        Description:
            - This attribute contains the state of the sense mode.

        Usage:
            - Accessing this property will send the ``print(smuX.sense)`` query.
            - Setting this property to a value will send the ``smuX.sense = value`` command.

        TSP Syntax:
            ```
            - smuX.sense = value
            - print(smuX.sense)
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.sense applies to SMU
              channel A).

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
    def source(self) -> SmuxItemSource:
        """Return the ``smuX.source`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.source.autorangev
              applies to SMU channel A).

        Sub-properties and sub-methods:
            - ``.autorangei``: The ``smuX.source.autorangei`` attribute.
            - ``.autorangev``: The ``smuX.source.autorangev`` attribute.
            - ``.calibratei()``: The ``smuX.source.calibratei()`` function.
            - ``.calibratev()``: The ``smuX.source.calibratev()`` function.
            - ``.compliance``: The ``smuX.source.compliance`` attribute.
            - ``.delay``: The ``smuX.source.delay`` attribute.
            - ``.func``: The ``smuX.source.func`` attribute.
            - ``.highc``: The ``smuX.source.highc`` attribute.
            - ``.leveli``: The ``smuX.source.leveli`` attribute.
            - ``.levelv``: The ``smuX.source.levelv`` attribute.
            - ``.limiti``: The ``smuX.source.limiti`` attribute.
            - ``.limitp``: The ``smuX.source.limitp`` attribute.
            - ``.limitv``: The ``smuX.source.limitv`` attribute.
            - ``.lowrangei``: The ``smuX.source.lowrangei`` attribute.
            - ``.lowrangev``: The ``smuX.source.lowrangev`` attribute.
            - ``.offfunc``: The ``smuX.source.offfunc`` attribute.
            - ``.offlimiti``: The ``smuX.source.offlimiti`` attribute.
            - ``.offlimitv``: The ``smuX.source.offlimitv`` attribute.
            - ``.offmode``: The ``smuX.source.offmode`` attribute.
            - ``.output``: The ``smuX.source.output`` attribute.
            - ``.outputenableaction``: The ``smuX.source.outputenableaction`` attribute.
            - ``.rangei``: The ``smuX.source.rangei`` attribute.
            - ``.rangev``: The ``smuX.source.rangev`` attribute.
            - ``.settling``: The ``smuX.source.settling`` attribute.
            - ``.sink``: The ``smuX.source.sink`` attribute.
        """
        return self._source

    @property
    def trigger(self) -> SmuxItemTrigger:
        """Return the ``smuX.trigger`` command tree.

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.trigger.ARMED_EVENT_ID
              applies to SMU channel A).

        Constants:
            - ``.ARMED_EVENT_ID``: The number of the armed event.
            - ``.IDLE_EVENT_ID``: The idle event number.
            - ``.MEASURE_COMPLETE_EVENT_ID``: The measurement complete event number.
            - ``.PULSE_COMPLETE_EVENT_ID``: The pulse complete event number.
            - ``.SOURCE_COMPLETE_EVENT_ID``: The source complete event number.
            - ``.SWEEPING_EVENT_ID``: The sweeping event number.
            - ``.SWEEP_COMPLETE_EVENT_ID``: The sweep complete event number.

        Sub-properties and sub-methods:
            - ``.arm``: The ``smuX.trigger.arm`` command tree.
            - ``.autoclear``: The ``smuX.trigger.autoclear`` attribute.
            - ``.count``: The ``smuX.trigger.count`` attribute.
            - ``.endpulse``: The ``smuX.trigger.endpulse`` command tree.
            - ``.endsweep``: The ``smuX.trigger.endsweep`` command tree.
            - ``.initiate()``: The ``smuX.trigger.initiate()`` function.
            - ``.measure``: The ``smuX.trigger.measure`` command tree.
            - ``.source``: The ``smuX.trigger.source`` command tree.
        """
        return self._trigger

    def abort(self) -> None:
        """Run the ``smuX.abort()`` function.

        Description:
            - This function terminates all overlapped operations on the specified source-measure
              unit (SMU).

        TSP Syntax:
            ```
            - smuX.abort()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.abort() applies to SMU
              channel A).

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

    def makebuffer(self, buffer_size: str) -> str:
        """Run the ``smuX.makebuffer()`` function.

        Description:
            - This function creates a reading buffer.

        TSP Syntax:
            ```
            - smuX.makebuffer()
            ```

        Args:
            buffer_size: Maximum number of readings that can be stored.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.makebuffer({buffer_size}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.makebuffer()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measureiandstep(self, source_value: float) -> str:
        """Run the ``smuX.measureiandstep()`` function.

        Description:
            - This function makes one or two measurements and then steps the source. (i = current in
              amperes)

        TSP Syntax:
            ```
            - smuX.measureiandstep()
            ```

        Args:
            source_value: Source value to be set after the measurement is made.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measureiandstep({source_value}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measureiandstep()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measureivandstep(self, source_value: float) -> str:
        """Run the ``smuX.measureivandstep()`` function.

        Description:
            - This function makes one or two measurements and then steps the source. (i = current in
              amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - smuX.measureivandstep()
            ```

        Args:
            source_value: Source value to be set after the measurement is made.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measureivandstep({source_value}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measureivandstep()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measurepandstep(self, source_value: float) -> str:
        """Run the ``smuX.measurepandstep()`` function.

        Description:
            - This function makes one or two measurements and then steps the source. (p = power in
              watts)

        TSP Syntax:
            ```
            - smuX.measurepandstep()
            ```

        Args:
            source_value: Source value to be set after the measurement is made.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measurepandstep({source_value}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measurepandstep()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measurerandstep(self, source_value: float) -> str:
        """Run the ``smuX.measurerandstep()`` function.

        Description:
            - This function makes one or two measurements and then steps the source. (r = resistance
              in ohms)

        TSP Syntax:
            ```
            - smuX.measurerandstep()
            ```

        Args:
            source_value: Source value to be set after the measurement is made.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measurerandstep({source_value}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measurerandstep()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measurevandstep(self, source_value: float) -> str:
        """Run the ``smuX.measurevandstep()`` function.

        Description:
            - This function makes one or two measurements and then steps the source. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - smuX.measurevandstep()
            ```

        Args:
            source_value: Source value to be set after the measurement is made.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measurevandstep({source_value}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measurevandstep()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self) -> None:
        """Run the ``smuX.reset()`` function.

        Description:
            - This function turns off the output and resets the commands that begin with smuX. to
              their default settings.

        TSP Syntax:
            ```
            - smuX.reset()
            ```

        Info:
            - ``X``, the source-measure unit (SMU) channel (for example, smua.reset() applies to SMU
              channel A).

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

    def savebuffer(self, y: str) -> None:
        """Run the ``smuX.savebuffer()`` function.

        Description:
            - This function saves one source-measure unit (SMU) dedicated reading buffer to
              nonvolatile memory (there are two dedicated reading buffers for each SMU).

        TSP Syntax:
            ```
            - smuX.savebuffer()
            ```

        Args:
            y: SMU dedicated reading buffer (1 or 2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.savebuffer({y})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.savebuffer()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
