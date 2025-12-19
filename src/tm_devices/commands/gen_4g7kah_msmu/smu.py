# pyright: reportConstantRedefinition=none
"""The smu commands module.

These commands are used in the following models:
MSMU60_2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - smu[X].abort()
    - smu[X].configlist.create()
    - smu[X].configlist.delete()
    - smu[X].configlist.query()
    - smu[X].configlist.recall()
    - smu[X].configlist.size()
    - smu[X].configlist.store()
    - smu[X].configlist.table()
    - smu[X].contact.calibratehi()
    - smu[X].contact.calibratelo()
    - smu[X].contact.check()
    - smu[X].contact.getcalhi()
    - smu[X].contact.r()
    - smu[X].contact.speed
    - smu[X].contact.threshold
    - smu[X].defbuffer1
    - smu[X].defbuffer2
    - smu[X].guard.v()
    - smu[X].makebuffer()
    - smu[X].measure.aperture
    - smu[X].measure.autodelay
    - smu[X].measure.autorangei
    - smu[X].measure.autorangev
    - smu[X].measure.count
    - smu[X].measure.delay
    - smu[X].measure.i()
    - smu[X].measure.interval
    - smu[X].measure.lowrangei
    - smu[X].measure.lowrangev
    - smu[X].measure.nplc
    - smu[X].measure.overlappedi()
    - smu[X].measure.overlappediv()
    - smu[X].measure.overlappedp()
    - smu[X].measure.overlappedr()
    - smu[X].measure.overlappedv()
    - smu[X].measure.p()
    - smu[X].measure.r()
    - smu[X].measure.rangei
    - smu[X].measure.rangev
    - smu[X].measure.rel.enablei
    - smu[X].measure.rel.enablep
    - smu[X].measure.rel.enabler
    - smu[X].measure.rel.enablev
    - smu[X].measure.rel.leveli
    - smu[X].measure.rel.levelp
    - smu[X].measure.rel.levelr
    - smu[X].measure.rel.levelv
    - smu[X].measure.tempcomp
    - smu[X].measure.v()
    - smu[X].overlapped
    - smu[X].reset()
    - smu[X].sense
    - smu[X].source.autodelay
    - smu[X].source.autorangei
    - smu[X].source.autorangev
    - smu[X].source.constantcurrent
    - smu[X].source.delay
    - smu[X].source.func
    - smu[X].source.leveli
    - smu[X].source.levelv
    - smu[X].source.limiti
    - smu[X].source.limitni
    - smu[X].source.limitnv
    - smu[X].source.limitpi
    - smu[X].source.limitpv
    - smu[X].source.limitv
    - smu[X].source.lowrangei
    - smu[X].source.lowrangev
    - smu[X].source.offfunc
    - smu[X].source.offlimiti
    - smu[X].source.offlimitni
    - smu[X].source.offlimitnv
    - smu[X].source.offlimitpi
    - smu[X].source.offlimitpv
    - smu[X].source.offlimitv
    - smu[X].source.offmode
    - smu[X].source.output
    - smu[X].source.rangei
    - smu[X].source.rangev
    - smu[X].trigger.measure.i()
    - smu[X].trigger.measure.iv()
    - smu[X].trigger.measure.p()
    - smu[X].trigger.measure.r()
    - smu[X].trigger.measure.v()
    - smu[X].trigger.source.lineari()
    - smu[X].trigger.source.linearv()
    - smu[X].trigger.source.listi()
    - smu[X].trigger.source.listv()
    - smu[X].trigger.source.logi()
    - smu[X].trigger.source.logv()
    - smu[X].waitcomplete()
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from ..gen_4dh8ja_mpmpsumsmu.buffervar import Buffervar
from ..helpers import BaseTSPCmd, NoDeviceProvidedError, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class SmuItemTriggerSource(BaseTSPCmd):
    """The ``smu[X].trigger.source`` command tree.

    Properties and methods:
        - ``.lineari()``: The ``smu[X].trigger.source.lineari()`` function.
        - ``.linearv()``: The ``smu[X].trigger.source.linearv()`` function.
        - ``.listi()``: The ``smu[X].trigger.source.listi()`` function.
        - ``.listv()``: The ``smu[X].trigger.source.listv()`` function.
        - ``.logi()``: The ``smu[X].trigger.source.logi()`` function.
        - ``.logv()``: The ``smu[X].trigger.source.logv()`` function.
    """

    def lineari(self, start: str, end: str, points: str) -> None:
        """Run the ``smu[X].trigger.source.lineari()`` function.

        Description:
            - This function configures the linear sweep for the trigger model. (i = current in
              amperes)

        TSP Syntax:
            ```
            - smu[X].trigger.source.lineari()
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
        """Run the ``smu[X].trigger.source.linearv()`` function.

        Description:
            - This function configures the linear sweep for the trigger model. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - smu[X].trigger.source.linearv()
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
        """Run the ``smu[X].trigger.source.listi()`` function.

        Description:
            - This function configures the list sweep for the trigger model. (i = current in
              amperes)

        TSP Syntax:
            ```
            - smu[X].trigger.source.listi()
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
        """Run the ``smu[X].trigger.source.listv()`` function.

        Description:
            - This function configures the list sweep for the trigger model. (v = voltage in volts)

        TSP Syntax:
            ```
            - smu[X].trigger.source.listv()
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
        """Run the ``smu[X].trigger.source.logi()`` function.

        Description:
            - This function configures a logarithmic sweep for the trigger model. (i = current in
              amperes)

        TSP Syntax:
            ```
            - smu[X].trigger.source.logi()
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
        """Run the ``smu[X].trigger.source.logv()`` function.

        Description:
            - This function configures a logarithmic sweep for the trigger model. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - smu[X].trigger.source.logv()
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


class SmuItemTriggerMeasure(BaseTSPCmd):
    """The ``smu[X].trigger.measure`` command tree.

    Properties and methods:
        - ``.i()``: The ``smu[X].trigger.measure.i()`` function.
        - ``.iv()``: The ``smu[X].trigger.measure.iv()`` function.
        - ``.p()``: The ``smu[X].trigger.measure.p()`` function.
        - ``.r()``: The ``smu[X].trigger.measure.r()`` function.
        - ``.v()``: The ``smu[X].trigger.measure.v()`` function.
    """

    def i(self, reading_buffer: str) -> None:
        """Run the ``smu[X].trigger.measure.i()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (i
              = current in amperes)

        TSP Syntax:
            ```
            - smu[X].trigger.measure.i()
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
        """Run the ``smu[X].trigger.measure.iv()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (i
              = current in amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - smu[X].trigger.measure.iv()
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
        """Run the ``smu[X].trigger.measure.p()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (p
              = power in watts)

        TSP Syntax:
            ```
            - smu[X].trigger.measure.p()
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
        """Run the ``smu[X].trigger.measure.r()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (r
              = resistance in ohms)

        TSP Syntax:
            ```
            - smu[X].trigger.measure.r()
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
        """Run the ``smu[X].trigger.measure.v()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (v
              = voltage in volts)

        TSP Syntax:
            ```
            - smu[X].trigger.measure.v()
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


class SmuItemTrigger(BaseTSPCmd):
    """The ``smu[X].trigger`` command tree.

    Properties and methods:
        - ``.measure``: The ``smu[X].trigger.measure`` command tree.
        - ``.source``: The ``smu[X].trigger.source`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._measure = SmuItemTriggerMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = SmuItemTriggerSource(device, f"{self._cmd_syntax}.source")

    @property
    def measure(self) -> SmuItemTriggerMeasure:
        """Return the ``smu[X].trigger.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.i()``: The ``smu[X].trigger.measure.i()`` function.
            - ``.iv()``: The ``smu[X].trigger.measure.iv()`` function.
            - ``.p()``: The ``smu[X].trigger.measure.p()`` function.
            - ``.r()``: The ``smu[X].trigger.measure.r()`` function.
            - ``.v()``: The ``smu[X].trigger.measure.v()`` function.
        """
        return self._measure

    @property
    def source(self) -> SmuItemTriggerSource:
        """Return the ``smu[X].trigger.source`` command tree.

        Sub-properties and sub-methods:
            - ``.lineari()``: The ``smu[X].trigger.source.lineari()`` function.
            - ``.linearv()``: The ``smu[X].trigger.source.linearv()`` function.
            - ``.listi()``: The ``smu[X].trigger.source.listi()`` function.
            - ``.listv()``: The ``smu[X].trigger.source.listv()`` function.
            - ``.logi()``: The ``smu[X].trigger.source.logi()`` function.
            - ``.logv()``: The ``smu[X].trigger.source.logv()`` function.
        """
        return self._source


#  pylint: disable=too-many-public-methods
class SmuItemSource(BaseTSPCmd):
    """The ``smu[X].source`` command tree.

    Info:
        - ``X``, the module channel number.

    Properties and methods:
        - ``.autodelay``: The ``smu[X].source.autodelay`` attribute.
        - ``.autorangei``: The ``smu[X].source.autorangei`` attribute.
        - ``.autorangev``: The ``smu[X].source.autorangev`` attribute.
        - ``.constantcurrent``: The ``smu[X].source.constantcurrent`` attribute.
        - ``.delay``: The ``smu[X].source.delay`` attribute.
        - ``.func``: The ``smu[X].source.func`` attribute.
        - ``.leveli``: The ``smu[X].source.leveli`` attribute.
        - ``.levelv``: The ``smu[X].source.levelv`` attribute.
        - ``.limiti``: The ``smu[X].source.limiti`` attribute.
        - ``.limitv``: The ``smu[X].source.limitv`` attribute.
        - ``.limitni``: The ``smu[X].source.limitni`` attribute.
        - ``.limitnv``: The ``smu[X].source.limitnv`` attribute.
        - ``.limitpi``: The ``smu[X].source.limitpi`` attribute.
        - ``.limitpv``: The ``smu[X].source.limitpv`` attribute.
        - ``.lowrangei``: The ``smu[X].source.lowrangei`` attribute.
        - ``.lowrangev``: The ``smu[X].source.lowrangev`` attribute.
        - ``.offfunc``: The ``smu[X].source.offfunc`` attribute.
        - ``.offlimiti``: The ``smu[X].source.offlimiti`` attribute.
        - ``.offlimitv``: The ``smu[X].source.offlimitv`` attribute.
        - ``.offlimitni``: The ``smu[X].source.offlimitni`` attribute.
        - ``.offlimitnv``: The ``smu[X].source.offlimitnv`` attribute.
        - ``.offlimitpi``: The ``smu[X].source.offlimitpi`` attribute.
        - ``.offlimitpv``: The ``smu[X].source.offlimitpv`` attribute.
        - ``.offmode``: The ``smu[X].source.offmode`` attribute.
        - ``.output``: The ``smu[X].source.output`` attribute.
        - ``.rangei``: The ``smu[X].source.rangei`` attribute.
        - ``.rangev``: The ``smu[X].source.rangev`` attribute.
    """

    @property
    def autodelay(self) -> str:
        """Access the ``smu[X].source.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic delay that occurs when the source is
              changed.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.autodelay)`` query.
            - Setting this property to a value will send the ``smu[X].source.autodelay = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.autodelay = value
            - print(smu[X].source.autodelay)
            ```

        Info:
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
        """Access the ``smu[X].source.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic delay that occurs when the source is
              changed.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.autodelay)`` query.
            - Setting this property to a value will send the ``smu[X].source.autodelay = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.autodelay = value
            - print(smu[X].source.autodelay)
            ```

        Info:
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
        """Access the ``smu[X].source.autorangei`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on or off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.autorangei)`` query.
            - Setting this property to a value will send the ``smu[X].source.autorangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.autorangei = value
            - print(smu[X].source.autorangei)
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
        """Access the ``smu[X].source.autorangei`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on or off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.autorangei)`` query.
            - Setting this property to a value will send the ``smu[X].source.autorangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.autorangei = value
            - print(smu[X].source.autorangei)
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
        """Access the ``smu[X].source.autorangev`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on or off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.autorangev)`` query.
            - Setting this property to a value will send the ``smu[X].source.autorangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.autorangev = value
            - print(smu[X].source.autorangev)
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
        """Access the ``smu[X].source.autorangev`` attribute.

        Description:
            - This attribute contains the state of the source autorange control (on or off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.autorangev)`` query.
            - Setting this property to a value will send the ``smu[X].source.autorangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.autorangev = value
            - print(smu[X].source.autorangev)
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
        """Access the ``smu[X].source.constantcurrent`` attribute.

        Description:
            - This attribute indicates when the source is within the current limit.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.constantcurrent)`` query.

        TSP Syntax:
            ```
            - print(smu[X].source.constantcurrent)
            ```

        Info:
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
        """Access the ``smu[X].source.delay`` attribute.

        Description:
            - This attribute contains the delay that occurs when the source is changed.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.delay)`` query.
            - Setting this property to a value will send the ``smu[X].source.delay = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.delay = value
            - print(smu[X].source.delay)
            ```

        Info:
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
        """Access the ``smu[X].source.delay`` attribute.

        Description:
            - This attribute contains the delay that occurs when the source is changed.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.delay)`` query.
            - Setting this property to a value will send the ``smu[X].source.delay = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.delay = value
            - print(smu[X].source.delay)
            ```

        Info:
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
        """Access the ``smu[X].source.func`` attribute.

        Description:
            - This attribute configures the source function as either voltage source or current
              source.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.func)`` query.
            - Setting this property to a value will send the ``smu[X].source.func = value`` command.

        TSP Syntax:
            ```
            - smu[X].source.func = value
            - print(smu[X].source.func)
            ```

        Info:
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
        """Access the ``smu[X].source.func`` attribute.

        Description:
            - This attribute configures the source function as either voltage source or current
              source.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.func)`` query.
            - Setting this property to a value will send the ``smu[X].source.func = value`` command.

        TSP Syntax:
            ```
            - smu[X].source.func = value
            - print(smu[X].source.func)
            ```

        Info:
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
        """Access the ``smu[X].source.leveli`` attribute.

        Description:
            - This attribute configures the source level setting. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.leveli)`` query.
            - Setting this property to a value will send the ``smu[X].source.leveli = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.leveli = value
            - print(smu[X].source.leveli)
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
        """Access the ``smu[X].source.leveli`` attribute.

        Description:
            - This attribute configures the source level setting. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.leveli)`` query.
            - Setting this property to a value will send the ``smu[X].source.leveli = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.leveli = value
            - print(smu[X].source.leveli)
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
        """Access the ``smu[X].source.levelv`` attribute.

        Description:
            - This attribute configures the source level setting. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.levelv)`` query.
            - Setting this property to a value will send the ``smu[X].source.levelv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.levelv = value
            - print(smu[X].source.levelv)
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
        """Access the ``smu[X].source.levelv`` attribute.

        Description:
            - This attribute configures the source level setting. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.levelv)`` query.
            - Setting this property to a value will send the ``smu[X].source.levelv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.levelv = value
            - print(smu[X].source.levelv)
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
        """Access the ``smu[X].source.limiti`` attribute.

        Description:
            - This attribute symmetrically configures both the positive and the negative source
              limit settings. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limiti)`` query.
            - Setting this property to a value will send the ``smu[X].source.limiti = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limiti = value
            - print(smu[X].source.limiti)
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
        """Access the ``smu[X].source.limiti`` attribute.

        Description:
            - This attribute symmetrically configures both the positive and the negative source
              limit settings. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limiti)`` query.
            - Setting this property to a value will send the ``smu[X].source.limiti = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limiti = value
            - print(smu[X].source.limiti)
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
        """Access the ``smu[X].source.limitv`` attribute.

        Description:
            - This attribute symmetrically configures both the positive and the negative source
              limit settings. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitv)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitv = value
            - print(smu[X].source.limitv)
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
        """Access the ``smu[X].source.limitv`` attribute.

        Description:
            - This attribute symmetrically configures both the positive and the negative source
              limit settings. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitv)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitv = value
            - print(smu[X].source.limitv)
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
        """Access the ``smu[X].source.limitni`` attribute.

        Description:
            - This attribute configures the negative source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitni)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitni = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitni = value
            - print(smu[X].source.limitni)
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
        """Access the ``smu[X].source.limitni`` attribute.

        Description:
            - This attribute configures the negative source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitni)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitni = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitni = value
            - print(smu[X].source.limitni)
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
        """Access the ``smu[X].source.limitnv`` attribute.

        Description:
            - This attribute configures the negative source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitnv)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitnv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitnv = value
            - print(smu[X].source.limitnv)
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
        """Access the ``smu[X].source.limitnv`` attribute.

        Description:
            - This attribute configures the negative source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitnv)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitnv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitnv = value
            - print(smu[X].source.limitnv)
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
        """Access the ``smu[X].source.limitpi`` attribute.

        Description:
            - This attribute configures the positive source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitpi)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitpi = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitpi = value
            - print(smu[X].source.limitpi)
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
        """Access the ``smu[X].source.limitpi`` attribute.

        Description:
            - This attribute configures the positive source limit. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitpi)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitpi = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitpi = value
            - print(smu[X].source.limitpi)
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
        """Access the ``smu[X].source.limitpv`` attribute.

        Description:
            - This attribute configures the positive source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitpv)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitpv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitpv = value
            - print(smu[X].source.limitpv)
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
        """Access the ``smu[X].source.limitpv`` attribute.

        Description:
            - This attribute configures the positive source limit. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.limitpv)`` query.
            - Setting this property to a value will send the ``smu[X].source.limitpv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.limitpv = value
            - print(smu[X].source.limitpv)
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
        """Access the ``smu[X].source.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest source range that will be used during autoranging. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.lowrangei)`` query.
            - Setting this property to a value will send the ``smu[X].source.lowrangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.lowrangei = value
            - print(smu[X].source.lowrangei)
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
        """Access the ``smu[X].source.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest source range that will be used during autoranging. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.lowrangei)`` query.
            - Setting this property to a value will send the ``smu[X].source.lowrangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.lowrangei = value
            - print(smu[X].source.lowrangei)
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
        """Access the ``smu[X].source.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest source range that will be used during autoranging. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.lowrangev)`` query.
            - Setting this property to a value will send the ``smu[X].source.lowrangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.lowrangev = value
            - print(smu[X].source.lowrangev)
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
        """Access the ``smu[X].source.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest source range that will be used during autoranging. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.lowrangev)`` query.
            - Setting this property to a value will send the ``smu[X].source.lowrangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.lowrangev = value
            - print(smu[X].source.lowrangev)
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
        """Access the ``smu[X].source.offfunc`` attribute.

        Description:
            - This attribute sets the source function used (source 0 A or 0 V) when the output is
              turned off and the source-measure-unit (SMU) is in normal output-off mode.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offfunc)`` query.
            - Setting this property to a value will send the ``smu[X].source.offfunc = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offfunc = value
            - print(smu[X].source.offfunc)
            ```

        Info:
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
        """Access the ``smu[X].source.offfunc`` attribute.

        Description:
            - This attribute sets the source function used (source 0 A or 0 V) when the output is
              turned off and the source-measure-unit (SMU) is in normal output-off mode.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offfunc)`` query.
            - Setting this property to a value will send the ``smu[X].source.offfunc = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offfunc = value
            - print(smu[X].source.offfunc)
            ```

        Info:
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
        """Access the ``smu[X].source.offlimiti`` attribute.

        Description:
            - This attribute configures both the positive and negative source off limit settings
              symmetrically. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimiti)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimiti = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimiti = value
            - print(smu[X].source.offlimiti)
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
        """Access the ``smu[X].source.offlimiti`` attribute.

        Description:
            - This attribute configures both the positive and negative source off limit settings
              symmetrically. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimiti)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimiti = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimiti = value
            - print(smu[X].source.offlimiti)
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
        """Access the ``smu[X].source.offlimitv`` attribute.

        Description:
            - This attribute configures both the positive and negative source off limit settings
              symmetrically. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitv)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitv = value
            - print(smu[X].source.offlimitv)
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
        """Access the ``smu[X].source.offlimitv`` attribute.

        Description:
            - This attribute configures both the positive and negative source off limit settings
              symmetrically. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitv)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitv = value
            - print(smu[X].source.offlimitv)
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
        """Access the ``smu[X].source.offlimitni`` attribute.

        Description:
            - This attribute configures the negative source off limit setting. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitni)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitni = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitni = value
            - print(smu[X].source.offlimitni)
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
        """Access the ``smu[X].source.offlimitni`` attribute.

        Description:
            - This attribute configures the negative source off limit setting. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitni)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitni = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitni = value
            - print(smu[X].source.offlimitni)
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
        """Access the ``smu[X].source.offlimitnv`` attribute.

        Description:
            - This attribute configures the negative source off limit setting. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitnv)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitnv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitnv = value
            - print(smu[X].source.offlimitnv)
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
        """Access the ``smu[X].source.offlimitnv`` attribute.

        Description:
            - This attribute configures the negative source off limit setting. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitnv)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitnv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitnv = value
            - print(smu[X].source.offlimitnv)
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
        """Access the ``smu[X].source.offlimitpi`` attribute.

        Description:
            - This attribute configures the positive source off limit setting. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitpi)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitpi = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitpi = value
            - print(smu[X].source.offlimitpi)
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
        """Access the ``smu[X].source.offlimitpi`` attribute.

        Description:
            - This attribute configures the positive source off limit setting. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitpi)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitpi = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitpi = value
            - print(smu[X].source.offlimitpi)
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
        """Access the ``smu[X].source.offlimitpv`` attribute.

        Description:
            - This attribute configures the positive source off limit setting. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitpv)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitpv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitpv = value
            - print(smu[X].source.offlimitpv)
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
        """Access the ``smu[X].source.offlimitpv`` attribute.

        Description:
            - This attribute configures the positive source off limit setting. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offlimitpv)`` query.
            - Setting this property to a value will send the ``smu[X].source.offlimitpv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offlimitpv = value
            - print(smu[X].source.offlimitpv)
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
        """Access the ``smu[X].source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offmode)`` query.
            - Setting this property to a value will send the ``smu[X].source.offmode = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offmode = value
            - print(smu[X].source.offmode)
            ```

        Info:
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
        """Access the ``smu[X].source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.offmode)`` query.
            - Setting this property to a value will send the ``smu[X].source.offmode = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.offmode = value
            - print(smu[X].source.offmode)
            ```

        Info:
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
        """Access the ``smu[X].source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.output)`` query.
            - Setting this property to a value will send the ``smu[X].source.output = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.output = value
            - print(smu[X].source.output)
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
        """Access the ``smu[X].source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(smu[X].source.output)`` query.
            - Setting this property to a value will send the ``smu[X].source.output = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.output = value
            - print(smu[X].source.output)
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
        """Access the ``smu[X].source.rangei`` attribute.

        Description:
            - This attribute configures the source range setting to be fixed for function Y. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.rangei)`` query.
            - Setting this property to a value will send the ``smu[X].source.rangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.rangei = value
            - print(smu[X].source.rangei)
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
        """Access the ``smu[X].source.rangei`` attribute.

        Description:
            - This attribute configures the source range setting to be fixed for function Y. (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.rangei)`` query.
            - Setting this property to a value will send the ``smu[X].source.rangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.rangei = value
            - print(smu[X].source.rangei)
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
        """Access the ``smu[X].source.rangev`` attribute.

        Description:
            - This attribute configures the source range setting to be fixed for function Y. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.rangev)`` query.
            - Setting this property to a value will send the ``smu[X].source.rangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.rangev = value
            - print(smu[X].source.rangev)
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
        """Access the ``smu[X].source.rangev`` attribute.

        Description:
            - This attribute configures the source range setting to be fixed for function Y. (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].source.rangev)`` query.
            - Setting this property to a value will send the ``smu[X].source.rangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].source.rangev = value
            - print(smu[X].source.rangev)
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


class SmuItemMeasureRel(BaseTSPCmd):
    """The ``smu[X].measure.rel`` command tree.

    Properties and methods:
        - ``.enablei``: The ``smu[X].measure.rel.enablei`` attribute.
        - ``.enablep``: The ``smu[X].measure.rel.enablep`` attribute.
        - ``.enabler``: The ``smu[X].measure.rel.enabler`` attribute.
        - ``.enablev``: The ``smu[X].measure.rel.enablev`` attribute.
        - ``.leveli``: The ``smu[X].measure.rel.leveli`` attribute.
        - ``.levelp``: The ``smu[X].measure.rel.levelp`` attribute.
        - ``.levelr``: The ``smu[X].measure.rel.levelr`` attribute.
        - ``.levelv``: The ``smu[X].measure.rel.levelv`` attribute.
    """

    @property
    def enablei(self) -> str:
        """Access the ``smu[X].measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.enablei)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.enablei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.enablei = value
            - print(smu[X].measure.rel.enablei)
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
        """Access the ``smu[X].measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.enablei)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.enablei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.enablei = value
            - print(smu[X].measure.rel.enablei)
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
        """Access the ``smu[X].measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.enablep)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.enablep = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.enablep = value
            - print(smu[X].measure.rel.enablep)
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
        """Access the ``smu[X].measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.enablep)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.enablep = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.enablep = value
            - print(smu[X].measure.rel.enablep)
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
        """Access the ``smu[X].measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.enabler)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.enabler = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.enabler = value
            - print(smu[X].measure.rel.enabler)
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
        """Access the ``smu[X].measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.enabler)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.enabler = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.enabler = value
            - print(smu[X].measure.rel.enabler)
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
        """Access the ``smu[X].measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.enablev)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.enablev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.enablev = value
            - print(smu[X].measure.rel.enablev)
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
        """Access the ``smu[X].measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.enablev)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.enablev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.enablev = value
            - print(smu[X].measure.rel.enablev)
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
        """Access the ``smu[X].measure.rel.leveli`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.leveli)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.leveli = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.leveli = value
            - print(smu[X].measure.rel.leveli)
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
        """Access the ``smu[X].measure.rel.leveli`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.leveli)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.leveli = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.leveli = value
            - print(smu[X].measure.rel.leveli)
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
        """Access the ``smu[X].measure.rel.levelp`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (p = power in
              watts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.levelp)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.levelp = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.levelp = value
            - print(smu[X].measure.rel.levelp)
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
        """Access the ``smu[X].measure.rel.levelp`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (p = power in
              watts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.levelp)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.levelp = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.levelp = value
            - print(smu[X].measure.rel.levelp)
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
        """Access the ``smu[X].measure.rel.levelr`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (r = resistance
              in ohms)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.levelr)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.levelr = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.levelr = value
            - print(smu[X].measure.rel.levelr)
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
        """Access the ``smu[X].measure.rel.levelr`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (r = resistance
              in ohms)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.levelr)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.levelr = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.levelr = value
            - print(smu[X].measure.rel.levelr)
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
        """Access the ``smu[X].measure.rel.levelv`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.levelv)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.levelv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.levelv = value
            - print(smu[X].measure.rel.levelv)
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
        """Access the ``smu[X].measure.rel.levelv`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rel.levelv)`` query.
            - Setting this property to a value will send the ``smu[X].measure.rel.levelv = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.rel.levelv = value
            - print(smu[X].measure.rel.levelv)
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
class SmuItemMeasure(BaseTSPCmd):
    """The ``smu[X].measure`` command tree.

    Properties and methods:
        - ``.i()``: The ``smu[X].measure.i()`` function.
        - ``.p()``: The ``smu[X].measure.p()`` function.
        - ``.r()``: The ``smu[X].measure.r()`` function.
        - ``.v()``: The ``smu[X].measure.v()`` function.
        - ``.aperture``: The ``smu[X].measure.aperture`` attribute.
        - ``.autodelay``: The ``smu[X].measure.autodelay`` attribute.
        - ``.autorangei``: The ``smu[X].measure.autorangei`` attribute.
        - ``.autorangev``: The ``smu[X].measure.autorangev`` attribute.
        - ``.count``: The ``smu[X].measure.count`` attribute.
        - ``.delay``: The ``smu[X].measure.delay`` attribute.
        - ``.interval``: The ``smu[X].measure.interval`` attribute.
        - ``.lowrangei``: The ``smu[X].measure.lowrangei`` attribute.
        - ``.lowrangev``: The ``smu[X].measure.lowrangev`` attribute.
        - ``.nplc``: The ``smu[X].measure.nplc`` attribute.
        - ``.overlappedi()``: The ``smu[X].measure.overlappedi()`` function.
        - ``.overlappediv()``: The ``smu[X].measure.overlappediv()`` function.
        - ``.overlappedp()``: The ``smu[X].measure.overlappedp()`` function.
        - ``.overlappedr()``: The ``smu[X].measure.overlappedr()`` function.
        - ``.overlappedv()``: The ``smu[X].measure.overlappedv()`` function.
        - ``.rangei``: The ``smu[X].measure.rangei`` attribute.
        - ``.rangev``: The ``smu[X].measure.rangev`` attribute.
        - ``.rel``: The ``smu[X].measure.rel`` command tree.
        - ``.tempcomp``: The ``smu[X].measure.tempcomp`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rel = SmuItemMeasureRel(device, f"{self._cmd_syntax}.rel")

    @property
    def aperture(self) -> str:
        """Access the ``smu[X].measure.aperture`` attribute.

        Description:
            - This attribute configures the measurement aperture for a channel in seconds.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.aperture)`` query.
            - Setting this property to a value will send the ``smu[X].measure.aperture = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.aperture = value
            - print(smu[X].measure.aperture)
            ```

        Info:
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
        """Access the ``smu[X].measure.aperture`` attribute.

        Description:
            - This attribute configures the measurement aperture for a channel in seconds.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.aperture)`` query.
            - Setting this property to a value will send the ``smu[X].measure.aperture = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.aperture = value
            - print(smu[X].measure.aperture)
            ```

        Info:
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
        """Access the ``smu[X].measure.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic measurement delay.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.autodelay)`` query.
            - Setting this property to a value will send the ``smu[X].measure.autodelay = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.autodelay = value
            - print(smu[X].measure.autodelay)
            ```

        Info:
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
        """Access the ``smu[X].measure.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic measurement delay.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.autodelay)`` query.
            - Setting this property to a value will send the ``smu[X].measure.autodelay = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.autodelay = value
            - print(smu[X].measure.autodelay)
            ```

        Info:
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
        """Access the ``smu[X].measure.autorangei`` attribute.

        Description:
            - This attribute contains the state of the measure autorange control (on or off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.autorangei)`` query.
            - Setting this property to a value will send the ``smu[X].measure.autorangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.autorangei = value
            - print(smu[X].measure.autorangei)
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
        """Access the ``smu[X].measure.autorangei`` attribute.

        Description:
            - This attribute contains the state of the measure autorange control (on or off). (i =
              current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.autorangei)`` query.
            - Setting this property to a value will send the ``smu[X].measure.autorangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.autorangei = value
            - print(smu[X].measure.autorangei)
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
        """Access the ``smu[X].measure.autorangev`` attribute.

        Description:
            - This attribute contains the state of the measure autorange control (on or off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.autorangev)`` query.
            - Setting this property to a value will send the ``smu[X].measure.autorangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.autorangev = value
            - print(smu[X].measure.autorangev)
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
        """Access the ``smu[X].measure.autorangev`` attribute.

        Description:
            - This attribute contains the state of the measure autorange control (on or off). (v =
              voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.autorangev)`` query.
            - Setting this property to a value will send the ``smu[X].measure.autorangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.autorangev = value
            - print(smu[X].measure.autorangev)
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
        """Access the ``smu[X].measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements performed when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.count)`` query.
            - Setting this property to a value will send the ``smu[X].measure.count = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.count = value
            - print(smu[X].measure.count)
            ```

        Info:
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
        """Access the ``smu[X].measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements performed when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.count)`` query.
            - Setting this property to a value will send the ``smu[X].measure.count = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.count = value
            - print(smu[X].measure.count)
            ```

        Info:
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
        """Access the ``smu[X].measure.delay`` attribute.

        Description:
            - This attribute controls the measurement delay.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.delay)`` query.
            - Setting this property to a value will send the ``smu[X].measure.delay = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.delay = value
            - print(smu[X].measure.delay)
            ```

        Info:
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
        """Access the ``smu[X].measure.delay`` attribute.

        Description:
            - This attribute controls the measurement delay.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.delay)`` query.
            - Setting this property to a value will send the ``smu[X].measure.delay = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.delay = value
            - print(smu[X].measure.delay)
            ```

        Info:
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
        """Access the ``smu[X].measure.interval`` attribute.

        Description:
            - This attribute sets the interval between multiple measurements.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.interval)`` query.
            - Setting this property to a value will send the ``smu[X].measure.interval = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.interval = value
            - print(smu[X].measure.interval)
            ```

        Info:
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
        """Access the ``smu[X].measure.interval`` attribute.

        Description:
            - This attribute sets the interval between multiple measurements.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.interval)`` query.
            - Setting this property to a value will send the ``smu[X].measure.interval = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.interval = value
            - print(smu[X].measure.interval)
            ```

        Info:
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
        """Access the ``smu[X].measure.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest measurement range to be used when the instrument is
              autoranging. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.lowrangei)`` query.
            - Setting this property to a value will send the ``smu[X].measure.lowrangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.lowrangei = value
            - print(smu[X].measure.lowrangei)
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
        """Access the ``smu[X].measure.lowrangei`` attribute.

        Description:
            - This attribute sets the lowest measurement range to be used when the instrument is
              autoranging. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.lowrangei)`` query.
            - Setting this property to a value will send the ``smu[X].measure.lowrangei = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.lowrangei = value
            - print(smu[X].measure.lowrangei)
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
        """Access the ``smu[X].measure.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest measurement range to be used when the instrument is
              autoranging. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.lowrangev)`` query.
            - Setting this property to a value will send the ``smu[X].measure.lowrangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.lowrangev = value
            - print(smu[X].measure.lowrangev)
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
        """Access the ``smu[X].measure.lowrangev`` attribute.

        Description:
            - This attribute sets the lowest measurement range to be used when the instrument is
              autoranging. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.lowrangev)`` query.
            - Setting this property to a value will send the ``smu[X].measure.lowrangev = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.lowrangev = value
            - print(smu[X].measure.lowrangev)
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
        """Access the ``smu[X].measure.nplc`` attribute.

        Description:
            - This command sets the time that the input signal is measured in number of power line
              cycles.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.nplc)`` query.
            - Setting this property to a value will send the ``smu[X].measure.nplc = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.nplc = value
            - print(smu[X].measure.nplc)
            ```

        Info:
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
        """Access the ``smu[X].measure.nplc`` attribute.

        Description:
            - This command sets the time that the input signal is measured in number of power line
              cycles.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.nplc)`` query.
            - Setting this property to a value will send the ``smu[X].measure.nplc = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.nplc = value
            - print(smu[X].measure.nplc)
            ```

        Info:
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
        """Access the ``smu[X].measure.rangei`` attribute.

        Description:
            - This attribute contains the positive, full scale value of the measurement range for
              voltage or current. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rangei)`` query.

        TSP Syntax:
            ```
            - print(smu[X].measure.rangei)
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
        """Access the ``smu[X].measure.rangev`` attribute.

        Description:
            - This attribute contains the positive, full scale value of the measurement range for
              voltage or current. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.rangev)`` query.

        TSP Syntax:
            ```
            - print(smu[X].measure.rangev)
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
    def rel(self) -> SmuItemMeasureRel:
        """Return the ``smu[X].measure.rel`` command tree.

        Sub-properties and sub-methods:
            - ``.enablei``: The ``smu[X].measure.rel.enablei`` attribute.
            - ``.enablep``: The ``smu[X].measure.rel.enablep`` attribute.
            - ``.enabler``: The ``smu[X].measure.rel.enabler`` attribute.
            - ``.enablev``: The ``smu[X].measure.rel.enablev`` attribute.
            - ``.leveli``: The ``smu[X].measure.rel.leveli`` attribute.
            - ``.levelp``: The ``smu[X].measure.rel.levelp`` attribute.
            - ``.levelr``: The ``smu[X].measure.rel.levelr`` attribute.
            - ``.levelv``: The ``smu[X].measure.rel.levelv`` attribute.
        """
        return self._rel

    @property
    def tempcomp(self) -> str:
        """Access the ``smu[X].measure.tempcomp`` attribute.

        Description:
            - This attribute turns temperature compensation on or off for the current measurements.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.tempcomp)`` query.
            - Setting this property to a value will send the ``smu[X].measure.tempcomp = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.tempcomp = value
            - print(smu[X].measure.tempcomp)
            ```

        Info:
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
        """Access the ``smu[X].measure.tempcomp`` attribute.

        Description:
            - This attribute turns temperature compensation on or off for the current measurements.

        Usage:
            - Accessing this property will send the ``print(smu[X].measure.tempcomp)`` query.
            - Setting this property to a value will send the ``smu[X].measure.tempcomp = value``
              command.

        TSP Syntax:
            ```
            - smu[X].measure.tempcomp = value
            - print(smu[X].measure.tempcomp)
            ```

        Info:
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
        """Run the ``smu[X].measure.i()`` function.

        Description:
            - This function makes one or more measurements. (i = current in amperes)

        TSP Syntax:
            ```
            - smu[X].measure.i()
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
        """Run the ``smu[X].measure.p()`` function.

        Description:
            - This function makes one or more measurements. (p = power in watts)

        TSP Syntax:
            ```
            - smu[X].measure.p()
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
        """Run the ``smu[X].measure.r()`` function.

        Description:
            - This function makes one or more measurements. (r = resistance in ohms)

        TSP Syntax:
            ```
            - smu[X].measure.r()
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
        """Run the ``smu[X].measure.v()`` function.

        Description:
            - This function makes one or more measurements. (v = voltage in volts)

        TSP Syntax:
            ```
            - smu[X].measure.v()
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
        """Run the ``smu[X].measure.overlappedi()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes)

        TSP Syntax:
            ```
            - smu[X].measure.overlappedi()
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
        """Run the ``smu[X].measure.overlappediv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - smu[X].measure.overlappediv()
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
        """Run the ``smu[X].measure.overlappedp()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (p = power in watts)

        TSP Syntax:
            ```
            - smu[X].measure.overlappedp()
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
        """Run the ``smu[X].measure.overlappedr()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (r = resistance in
              ohms)

        TSP Syntax:
            ```
            - smu[X].measure.overlappedr()
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
        """Run the ``smu[X].measure.overlappedv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (v = voltage in volts)

        TSP Syntax:
            ```
            - smu[X].measure.overlappedv()
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


class SmuItemGuard(BaseTSPCmd):
    """The ``smu[X].guard`` command tree.

    Info:
        - ``X``, the module channel number.

    Properties and methods:
        - ``.v()``: The ``smu[X].guard.v()`` function.
    """

    def v(self) -> str:
        """Run the ``smu[X].guard.v()`` function.

        Description:
            - This function makes a guard voltage measurement.

        TSP Syntax:
            ```
            - smu[X].guard.v()
            ```

        Info:
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


class SmuItemContact(BaseTSPCmd):
    """The ``smu[X].contact`` command tree.

    Info:
        - ``X``, the channel (1 or 2).

    Properties and methods:
        - ``.calibratehi()``: The ``smu[X].contact.calibratehi()`` function.
        - ``.calibratelo()``: The ``smu[X].contact.calibratelo()`` function.
        - ``.check()``: The ``smu[X].contact.check()`` function.
        - ``.getcalhi()``: The ``smu[X].contact.getcalhi()`` function.
        - ``.r()``: The ``smu[X].contact.r()`` function.
        - ``.speed``: The ``smu[X].contact.speed`` attribute.
        - ``.threshold``: The ``smu[X].contact.threshold`` attribute.
    """

    @property
    def speed(self) -> str:
        """Access the ``smu[X].contact.speed`` attribute.

        Description:
            - This attribute sets the contact check measurement speed.

        Usage:
            - Accessing this property will send the ``print(smu[X].contact.speed)`` query.
            - Setting this property to a value will send the ``smu[X].contact.speed = value``
              command.

        TSP Syntax:
            ```
            - smu[X].contact.speed = value
            - print(smu[X].contact.speed)
            ```

        Info:
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
        """Access the ``smu[X].contact.speed`` attribute.

        Description:
            - This attribute sets the contact check measurement speed.

        Usage:
            - Accessing this property will send the ``print(smu[X].contact.speed)`` query.
            - Setting this property to a value will send the ``smu[X].contact.speed = value``
              command.

        TSP Syntax:
            ```
            - smu[X].contact.speed = value
            - print(smu[X].contact.speed)
            ```

        Info:
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
        """Access the ``smu[X].contact.threshold`` attribute.

        Description:
            - This attribute sets the contact check pass or fail threshold.

        Usage:
            - Accessing this property will send the ``print(smu[X].contact.threshold)`` query.
            - Setting this property to a value will send the ``smu[X].contact.threshold = value``
              command.

        TSP Syntax:
            ```
            - smu[X].contact.threshold = value
            - print(smu[X].contact.threshold)
            ```

        Info:
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
        """Access the ``smu[X].contact.threshold`` attribute.

        Description:
            - This attribute sets the contact check pass or fail threshold.

        Usage:
            - Accessing this property will send the ``print(smu[X].contact.threshold)`` query.
            - Setting this property to a value will send the ``smu[X].contact.threshold = value``
              command.

        TSP Syntax:
            ```
            - smu[X].contact.threshold = value
            - print(smu[X].contact.threshold)
            ```

        Info:
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
        """Run the ``smu[X].contact.calibratehi()`` function.

        Description:
            - This function adjusts the high/sense high contact check measurement.

        TSP Syntax:
            ```
            - smu[X].contact.calibratehi()
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
        """Run the ``smu[X].contact.calibratelo()`` function.

        Description:
            - This function adjusts the low/sense low contact check measurement.

        TSP Syntax:
            ```
            - smu[X].contact.calibratelo()
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
        """Run the ``smu[X].contact.check()`` function.

        Description:
            - This function performs a contact check measurement and compares the result to the
              user-specified contact check threshold setting.

        TSP Syntax:
            ```
            - smu[X].contact.check()
            ```

        Info:
            - ``X``, the module channel number.

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
        """Run the ``smu[X].contact.getcalhi()`` function.

        Description:
            - This function returns the calibration constants used during the contact check hi
              measurement calculation.

        TSP Syntax:
            ```
            - smu[X].contact.getcalhi()
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
        """Run the ``smu[X].contact.r()`` function.

        Description:
            - This function performs a contact check measurement and returns the measured contact
              resistances.

        TSP Syntax:
            ```
            - smu[X].contact.r()
            ```

        Info:
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


class SmuItemConfiglist(BaseTSPCmd):
    """The ``smu[X].configlist`` command tree.

    Info:
        - ``X``, the module channel number.

    Properties and methods:
        - ``.create()``: The ``smu[X].configlist.create()`` function.
        - ``.delete()``: The ``smu[X].configlist.delete()`` function.
        - ``.query()``: The ``smu[X].configlist.query()`` function.
        - ``.recall()``: The ``smu[X].configlist.recall()`` function.
        - ``.size()``: The ``smu[X].configlist.size()`` function.
        - ``.store()``: The ``smu[X].configlist.store()`` function.
        - ``.table()``: The ``smu[X].configlist.table()`` function.
    """

    def create(self, config_list_name: str) -> None:
        """Run the ``smu[X].configlist.create()`` function.

        Description:
            - This function creates an empty configuration list.

        TSP Syntax:
            ```
            - smu[X].configlist.create()
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
        """Run the ``smu[X].configlist.delete()`` function.

        Description:
            - This function deletes a configuration list.

        TSP Syntax:
            ```
            - smu[X].configlist.delete()
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
        """Run the ``smu[X].configlist.query()`` function.

        Description:
            - This function returns a list of TSP commands and parameter settings that are stored in
              the specified configuration index.

        TSP Syntax:
            ```
            - smu[X].configlist.query()
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
        """Run the ``smu[X].configlist.recall()`` function.

        Description:
            - This function recalls a configuration index in a configuration list.

        TSP Syntax:
            ```
            - smu[X].configlist.recall()
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
        """Run the ``smu[X].configlist.size()`` function.

        Description:
            - This function returns the size (number of configuration indexes) of a configuration
              list.

        TSP Syntax:
            ```
            - smu[X].configlist.size()
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
        """Run the ``smu[X].configlist.store()`` function.

        Description:
            - This function stores the active settings into the named configuration list.

        TSP Syntax:
            ```
            - smu[X].configlist.store()
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
        """Run the ``smu[X].configlist.table()`` function.

        Description:
            - This function returns the name of one measure configuration lists that is stored on
              the instrument.

        TSP Syntax:
            ```
            - smu[X].configlist.table()
            ```

        Info:
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


class SmuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``smu[X]`` command tree.

    Info:
        - ``X``, the module channel number.

    Properties and methods:
        - ``.abort()``: The ``smu[X].abort()`` function.
        - ``.configlist``: The ``smu[X].configlist`` command tree.
        - ``.contact``: The ``smu[X].contact`` command tree.
        - ``.defbuffer1``: The ``smu[X].defbuffer1`` attribute.
        - ``.defbuffer2``: The ``smu[X].defbuffer2`` attribute.
        - ``.guard``: The ``smu[X].guard`` command tree.
        - ``.makebuffer()``: The ``smu[X].makebuffer()`` function.
        - ``.measure``: The ``smu[X].measure`` command tree.
        - ``.overlapped``: The ``smu[X].overlapped`` attribute.
        - ``.reset()``: The ``smu[X].reset()`` function.
        - ``.sense``: The ``smu[X].sense`` attribute.
        - ``.source``: The ``smu[X].source`` command tree.
        - ``.trigger``: The ``smu[X].trigger`` command tree.
        - ``.waitcomplete()``: The ``smu[X].waitcomplete()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "smu[X]") -> None:
        super().__init__(device, cmd_syntax)
        self._buffer_count = 1
        self._configlist = SmuItemConfiglist(device, f"{self._cmd_syntax}.configlist")
        self._contact = SmuItemContact(device, f"{self._cmd_syntax}.contact")
        self._guard = SmuItemGuard(device, f"{self._cmd_syntax}.guard")
        self._measure = SmuItemMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = SmuItemSource(device, f"{self._cmd_syntax}.source")
        self._trigger = SmuItemTrigger(device, f"{self._cmd_syntax}.trigger")

    @property
    def configlist(self) -> SmuItemConfiglist:
        """Return the ``smu[X].configlist`` command tree.

        Info:
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.create()``: The ``smu[X].configlist.create()`` function.
            - ``.delete()``: The ``smu[X].configlist.delete()`` function.
            - ``.query()``: The ``smu[X].configlist.query()`` function.
            - ``.recall()``: The ``smu[X].configlist.recall()`` function.
            - ``.size()``: The ``smu[X].configlist.size()`` function.
            - ``.store()``: The ``smu[X].configlist.store()`` function.
            - ``.table()``: The ``smu[X].configlist.table()`` function.
        """
        return self._configlist

    @property
    def contact(self) -> SmuItemContact:
        """Return the ``smu[X].contact`` command tree.

        Info:
            - ``X``, the channel (1 or 2).

        Sub-properties and sub-methods:
            - ``.calibratehi()``: The ``smu[X].contact.calibratehi()`` function.
            - ``.calibratelo()``: The ``smu[X].contact.calibratelo()`` function.
            - ``.check()``: The ``smu[X].contact.check()`` function.
            - ``.getcalhi()``: The ``smu[X].contact.getcalhi()`` function.
            - ``.r()``: The ``smu[X].contact.r()`` function.
            - ``.speed``: The ``smu[X].contact.speed`` attribute.
            - ``.threshold``: The ``smu[X].contact.threshold`` attribute.
        """
        return self._contact

    @cached_property
    def defbuffer1(self) -> Buffervar:
        """Access the ``smu[X].defbuffer1`` attribute.

        Description:
            - This attribute contains the default dedicated reading buffers. (1 = default buffer1)

        Usage:
            - Accessing this property will send the ``print(smu[X].defbuffer1)`` query.

        TSP Syntax:
            ```
            - print(smu[X].defbuffer1)
            ```

        Returns:
            The default buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return Buffervar(self._device, f"{self._cmd_syntax}.defbuffer1")

    @cached_property
    def defbuffer2(self) -> Buffervar:
        """Access the ``smu[X].defbuffer2`` attribute.

        Description:
            - This attribute contains the default dedicated reading buffers. (2 = default buffer2)

        Usage:
            - Accessing this property will send the ``print(smu[X].defbuffer2)`` query.

        TSP Syntax:
            ```
            - print(smu[X].defbuffer2)
            ```

        Returns:
            The default buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return Buffervar(self._device, f"{self._cmd_syntax}.defbuffer2")

    @property
    def guard(self) -> SmuItemGuard:
        """Return the ``smu[X].guard`` command tree.

        Info:
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.v()``: The ``smu[X].guard.v()`` function.
        """
        return self._guard

    @property
    def measure(self) -> SmuItemMeasure:
        """Return the ``smu[X].measure`` command tree.

        Sub-properties and sub-methods:
            - ``.i()``: The ``smu[X].measure.i()`` function.
            - ``.p()``: The ``smu[X].measure.p()`` function.
            - ``.r()``: The ``smu[X].measure.r()`` function.
            - ``.v()``: The ``smu[X].measure.v()`` function.
            - ``.aperture``: The ``smu[X].measure.aperture`` attribute.
            - ``.autodelay``: The ``smu[X].measure.autodelay`` attribute.
            - ``.autorangei``: The ``smu[X].measure.autorangei`` attribute.
            - ``.autorangev``: The ``smu[X].measure.autorangev`` attribute.
            - ``.count``: The ``smu[X].measure.count`` attribute.
            - ``.delay``: The ``smu[X].measure.delay`` attribute.
            - ``.interval``: The ``smu[X].measure.interval`` attribute.
            - ``.lowrangei``: The ``smu[X].measure.lowrangei`` attribute.
            - ``.lowrangev``: The ``smu[X].measure.lowrangev`` attribute.
            - ``.nplc``: The ``smu[X].measure.nplc`` attribute.
            - ``.overlappedi()``: The ``smu[X].measure.overlappedi()`` function.
            - ``.overlappediv()``: The ``smu[X].measure.overlappediv()`` function.
            - ``.overlappedp()``: The ``smu[X].measure.overlappedp()`` function.
            - ``.overlappedr()``: The ``smu[X].measure.overlappedr()`` function.
            - ``.overlappedv()``: The ``smu[X].measure.overlappedv()`` function.
            - ``.rangei``: The ``smu[X].measure.rangei`` attribute.
            - ``.rangev``: The ``smu[X].measure.rangev`` attribute.
            - ``.rel``: The ``smu[X].measure.rel`` command tree.
            - ``.tempcomp``: The ``smu[X].measure.tempcomp`` attribute.
        """
        return self._measure

    @property
    def overlapped(self) -> str:
        """Access the ``smu[X].overlapped`` attribute.

        Description:
            - This attribute contains the state of the overlapped mode.

        Usage:
            - Accessing this property will send the ``print(smu[X].overlapped)`` query.
            - Setting this property to a value will send the ``smu[X].overlapped = value`` command.

        TSP Syntax:
            ```
            - smu[X].overlapped = value
            - print(smu[X].overlapped)
            ```

        Info:
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
        """Access the ``smu[X].overlapped`` attribute.

        Description:
            - This attribute contains the state of the overlapped mode.

        Usage:
            - Accessing this property will send the ``print(smu[X].overlapped)`` query.
            - Setting this property to a value will send the ``smu[X].overlapped = value`` command.

        TSP Syntax:
            ```
            - smu[X].overlapped = value
            - print(smu[X].overlapped)
            ```

        Info:
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
        """Access the ``smu[X].sense`` attribute.

        Description:
            - This attribute contains the state of the sense mode.

        Usage:
            - Accessing this property will send the ``print(smu[X].sense)`` query.
            - Setting this property to a value will send the ``smu[X].sense = value`` command.

        TSP Syntax:
            ```
            - smu[X].sense = value
            - print(smu[X].sense)
            ```

        Info:
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
        """Access the ``smu[X].sense`` attribute.

        Description:
            - This attribute contains the state of the sense mode.

        Usage:
            - Accessing this property will send the ``print(smu[X].sense)`` query.
            - Setting this property to a value will send the ``smu[X].sense = value`` command.

        TSP Syntax:
            ```
            - smu[X].sense = value
            - print(smu[X].sense)
            ```

        Info:
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
    def source(self) -> SmuItemSource:
        """Return the ``smu[X].source`` command tree.

        Info:
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.autodelay``: The ``smu[X].source.autodelay`` attribute.
            - ``.autorangei``: The ``smu[X].source.autorangei`` attribute.
            - ``.autorangev``: The ``smu[X].source.autorangev`` attribute.
            - ``.constantcurrent``: The ``smu[X].source.constantcurrent`` attribute.
            - ``.delay``: The ``smu[X].source.delay`` attribute.
            - ``.func``: The ``smu[X].source.func`` attribute.
            - ``.leveli``: The ``smu[X].source.leveli`` attribute.
            - ``.levelv``: The ``smu[X].source.levelv`` attribute.
            - ``.limiti``: The ``smu[X].source.limiti`` attribute.
            - ``.limitv``: The ``smu[X].source.limitv`` attribute.
            - ``.limitni``: The ``smu[X].source.limitni`` attribute.
            - ``.limitnv``: The ``smu[X].source.limitnv`` attribute.
            - ``.limitpi``: The ``smu[X].source.limitpi`` attribute.
            - ``.limitpv``: The ``smu[X].source.limitpv`` attribute.
            - ``.lowrangei``: The ``smu[X].source.lowrangei`` attribute.
            - ``.lowrangev``: The ``smu[X].source.lowrangev`` attribute.
            - ``.offfunc``: The ``smu[X].source.offfunc`` attribute.
            - ``.offlimiti``: The ``smu[X].source.offlimiti`` attribute.
            - ``.offlimitv``: The ``smu[X].source.offlimitv`` attribute.
            - ``.offlimitni``: The ``smu[X].source.offlimitni`` attribute.
            - ``.offlimitnv``: The ``smu[X].source.offlimitnv`` attribute.
            - ``.offlimitpi``: The ``smu[X].source.offlimitpi`` attribute.
            - ``.offlimitpv``: The ``smu[X].source.offlimitpv`` attribute.
            - ``.offmode``: The ``smu[X].source.offmode`` attribute.
            - ``.output``: The ``smu[X].source.output`` attribute.
            - ``.rangei``: The ``smu[X].source.rangei`` attribute.
            - ``.rangev``: The ``smu[X].source.rangev`` attribute.
        """
        return self._source

    @property
    def trigger(self) -> SmuItemTrigger:
        """Return the ``smu[X].trigger`` command tree.

        Sub-properties and sub-methods:
            - ``.measure``: The ``smu[X].trigger.measure`` command tree.
            - ``.source``: The ``smu[X].trigger.source`` command tree.
        """
        return self._trigger

    def abort(self) -> None:
        """Run the ``smu[X].abort()`` function.

        Description:
            - This function terminates all overlapped operations on the specified channel.

        TSP Syntax:
            ```
            - smu[X].abort()
            ```

        Info:
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
        """Run the ``smu[X].makebuffer()`` function.

        Description:
            - This function creates a reading buffer.

        TSP Syntax:
            ```
            - smu[X].makebuffer()
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
        """Run the ``smu[X].reset()`` function.

        Description:
            - This function turns off the output and resets the commands that begin with smu [X]. to
              their default settings.

        TSP Syntax:
            ```
            - smu[X].reset()
            ```

        Info:
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
        """Run the ``smu[X].waitcomplete()`` function.

        Description:
            - This function waits for all previously started overlapped commands to complete on the
              specified channel of a module.

        TSP Syntax:
            ```
            - smu[X].waitcomplete()
            ```

        Info:
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
