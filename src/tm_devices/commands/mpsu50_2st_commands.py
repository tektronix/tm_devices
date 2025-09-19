"""The MPSU50_2ST commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Any, Dict

from .gen_3vhopd_mpsu.firmware import Firmware
from .gen_3vhopd_mpsu.psu import PsuItem
from .gen_3vhopd_mpsu.status import Status
from .gen_3vhopd_mpsu.trigger import Trigger
from .gen_4ajvxe_mpmpsu.buffervar import Buffervar


class MPSU50_2STMeta(type):  # noqa: N801
    """A metaclass that prevents instantiation of the class it's applied to."""

    def __call__(cls, *_: Any, **__: Any) -> None:
        """Raises a NotImplementedError when an attempt is made to instantiate the class."""
        instantiation_error_msg = (
            "This provides access to all the commands for the MPSU50_2ST device."
            "It serves only for type-hinting purposes and should not be instantiated."
        )
        raise NotImplementedError(instantiation_error_msg)


class MPSU50_2STCommands(metaclass=MPSU50_2STMeta):  # noqa: N801
    """The MPSU50-2ST commands.

    This provides access to all the commands for the MPSU50-2ST device. See the documentation of
    each property for more usage information.

    Properties and methods:
        - ``.buffer_var``: The ``bufferVar`` command tree.
        - ``.firmware``: The ``firmware`` command tree.
        - ``.license``: The ``license`` attribute.
        - ``.manufacturer``: The ``manufacturer`` attribute.
        - ``.model``: The ``model`` attribute.
        - ``.psu``: The ``psu[X]`` command tree.
        - ``.serialno``: The ``serialno`` attribute.
        - ``.status``: The ``status`` command tree.
        - ``.trigger``: The ``trigger`` command tree.
        - ``.version``: The ``version`` attribute.
    """

    @property
    def buffer_var(self) -> Dict[str, Buffervar]:  # pyright: ignore[reportReturnType]
        """Return the ``bufferVar`` command tree.

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Sub-properties and sub-methods:
            - ``.appendmode``: The ``bufferVar.appendmode`` attribute.
            - ``.cachemode``: The ``bufferVar.cachemode`` attribute.
            - ``.capacity``: The ``bufferVar.capacity`` attribute.
            - ``.clear()``: The ``bufferVar.clear()`` function.
            - ``.clearcache()``: The ``bufferVar.clearcache()`` function.
            - ``.columnname``: The ``bufferVar.columnname`` command tree.
            - ``.fillcount``: The ``bufferVar.fillcount`` attribute.
            - ``.fillmode``: The ``bufferVar.fillmode`` attribute.
            - ``.fractionalseconds``: The ``bufferVar.fractionalseconds[N]`` attribute.
            - ``.measurefunctions``: The ``bufferVar.measurefunctions[N]`` attribute.
            - ``.measureranges``: The ``bufferVar.measureranges[N]`` attribute.
            - ``.n``: The ``bufferVar.n`` attribute.
            - ``.readings``: The ``bufferVar.readings[N]`` attribute.
            - ``.seconds``: The ``bufferVar.seconds[N]`` attribute.
            - ``.sourcefunctions``: The ``bufferVar.sourcefunctions[N]`` attribute.
            - ``.sourceoutputstates``: The ``bufferVar.sourceoutputstates[N]`` attribute.
            - ``.sourceranges``: The ``bufferVar.sourceranges[N]`` attribute.
            - ``.sourcevalues``: The ``bufferVar.sourcevalues[N]`` attribute.
            - ``.statuses``: The ``bufferVar.statuses[N]`` attribute.
            - ``.timestampresolution``: The ``bufferVar.timestampresolution`` attribute.
            - ``.timestamps``: The ``bufferVar.timestamps[N]`` attribute.
        """

    @property
    def firmware(self) -> Firmware:  # pyright: ignore[reportReturnType]
        """Return the ``firmware`` command tree.

        Sub-properties and sub-methods:
            - ``.update()``: The ``firmware.update()`` function.
            - ``.verify()``: The ``firmware.verify()`` function.
        """

    @property
    def license(self) -> str:  # pyright: ignore[reportReturnType]
        """Return the ``license`` attribute.

        Description:
            - This attribute stores the ``license`` of the module installed in the specified
              mainframe slot.

        Usage:
            - Accessing this property will send the ``print(license)`` query.

        TSP Syntax:
            ```
            - print(license)
            ```

        Info:
            - ``license``, the license text of the instrument.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """

    @property
    def manufacturer(self) -> str:  # pyright: ignore[reportReturnType]
        """Return the ``manufacturer`` attribute.

        Description:
            - This attribute stores the ``manufacturer`` of the module in the specified mainframe
              slot.

        Usage:
            - Accessing this property will send the ``print(manufacturer)`` query.

        TSP Syntax:
            ```
            - print(manufacturer)
            ```

        Info:
            - ``manufacturer``, this is always Tektronix.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """

    @property
    def model(self) -> str:  # pyright: ignore[reportReturnType]
        """Return the ``model`` attribute.

        Description:
            - This attribute stores the ``model`` number of the module in the specified mainframe
              slot.

        Usage:
            - Accessing this property will send the ``print(model)`` query.

        TSP Syntax:
            ```
            - print(model)
            ```

        Info:
            - ``model``, the ``model`` number of the module.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """

    @property
    def psu(self) -> Dict[int, PsuItem]:  # pyright: ignore[reportReturnType]
        """Return the ``psu[X]`` command tree.

        Info:
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.abort()``: The ``psu[X].abort()`` function.
            - ``.configlist``: The ``psu[X].configlist`` command tree.
            - ``.defbuffer1``: The ``psu[X].defbuffer1`` attribute.
            - ``.defbuffer2``: The ``psu[X].defbuffer2`` attribute.
            - ``.makebuffer()``: The ``psu[X].makebuffer()`` function.
            - ``.measure``: The ``psu[X].measure`` command tree.
            - ``.overlapped``: The ``psu[X].overlapped`` attribute.
            - ``.reset()``: The ``psu[X].reset()`` function.
            - ``.source``: The ``psu[X].source`` command tree.
            - ``.trigger``: The ``psu[X].trigger`` command tree.
            - ``.waitcomplete()``: The ``psu[X].waitcomplete()`` function.
        """

    @property
    def serialno(self) -> str:  # pyright: ignore[reportReturnType]
        """Return the ``serialno`` attribute.

        Description:
            - This attribute stores the serial number of the module in the specified mainframe slot.

        Usage:
            - Accessing this property will send the ``print(serialno)`` query.

        TSP Syntax:
            ```
            - print(serialno)
            ```

        Info:
            - ``serialno``, the serial number of the module.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """

    @property
    def status(self) -> Status:  # pyright: ignore[reportReturnType]
        """Return the ``status`` command tree.

        Sub-properties and sub-methods:
            - ``.measurement``: The ``status.measurement`` command tree.
            - ``.operation``: The ``status.operation`` command tree.
            - ``.questionable``: The ``status.questionable`` command tree.
            - ``.reset()``: The ``status.reset()`` function.
        """

    @property
    def trigger(self) -> Trigger:  # pyright: ignore[reportReturnType]
        """Return the ``trigger`` command tree.

        Sub-properties and sub-methods:
            - ``.model``: The ``trigger.model`` command tree.
        """

    @property
    def version(self) -> str:  # pyright: ignore[reportReturnType]
        """Return the ``version`` attribute.

        Description:
            - This attribute stores the firmware ``version`` number of the module in the specified
              slot of the mainframe.

        Usage:
            - Accessing this property will send the ``print(version)`` query.

        TSP Syntax:
            ```
            - print(version)
            ```

        Info:
            - ``version``, the module firmware ``version`` number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
