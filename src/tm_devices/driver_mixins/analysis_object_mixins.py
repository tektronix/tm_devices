"""All mixin classes providing common methods and attributes for analysis objects.

Examples include MATH, SEARCH, BUS, PLOT,...etc.
"""

from abc import ABC, abstractmethod
from typing import Optional, Union


class BusMixin(ABC):
    """A mixin class which adds methods and properties for handling bus objetcs."""

    @abstractmethod
    def add_bus(self, bus_num: int) -> None:
        """Add a new bus.

        Args:
            bus_num: The number of the bus to add.
        """

    @abstractmethod
    def add_new_bus(self, bus_name: str, bus_type: str) -> None:
        """Add a new bus with the given name, and type.

        Args:
            bus_name: The name of the new bus.
            bus_type: The type of the new bus.
        """

    @abstractmethod
    def delete_bus(self, bus_num: int) -> None:
        """Delete a bus.

        Args:
            bus_num: The number of the bus to delete.
        """


class HistogramMixin(ABC):
    """A mixin class which adds methods and properties for handling histrogram objects."""

    @abstractmethod
    def add_histogram(self, hist_num: int) -> None:
        """Add a new histogram.

        Args:
            hist_num: The number of the histogram to add.
        """

    @abstractmethod
    def delete_histogram(self, hist_num: int) -> None:
        """Delete a histogram.

        Args:
            hist_num: The number of the histogram to delete.
        """


class MathMixin(ABC):
    """A mixin class which adds methods and properties for handling math objects."""

    @abstractmethod
    def add_math(self, math_num: int) -> None:
        """Add a new math.

        Args:
            math_num: The number of the math to add.
        """

    @abstractmethod
    def add_new_math(self, math_name: str, math_expression: str) -> None:
        """Add a new math with the given expression.

        Args:
            math_name: The name of the math.
            math_expression: The math expression.
        """

    @abstractmethod
    def delete_math(self, math_num: int) -> None:
        """Delete a math.

        Args:
            math_num: The number of the math to delete.
        """


class MeasurementsMixin(ABC):
    """A mixin class which adds methods and properties for handling measurement objects."""

    @abstractmethod
    def add_new_measurement(
        self, meas_name: str, meas_type: str, meas_source: Optional[str] = None
    ) -> None:
        """Add a new measurement with the given name, type, and source.

        Args:
            meas_name: The name of the new measurement.
            meas_type: The type of the new measurement.
            meas_source: The source of the new measurement.
                If None, the currently selected waveform (or first available valid source)
                will be used as the source.
        """

    @abstractmethod
    def add_measurement(self, measurement_num: int) -> None:
        """Add a new measurement.

        Args:
            measurement_num: The number of the measurement to add.
        """

    @abstractmethod
    def add_measurement_table(self, meas_table_num: int) -> None:
        """Add a new measurement table.

        Args:
            meas_table_num: The number of the measurement table to add.
        """

    @abstractmethod
    def delete_measurement(self, measurement_num: int) -> None:
        """Delete a measurement.

        Args:
            measurement_num: The number of the measurement to delete.
        """

    @abstractmethod
    def delete_measurement_table(self, measurement_table_num: int) -> None:
        """Delete a measurement table.

        Args:
            measurement_table_num: The number of the measurement table to delete.
        """


class PlotMixin(ABC):
    """A mixin class which adds methods and properties for handling plot objects."""

    @abstractmethod
    def add_new_plot(self, plot_name: str, plot_type: str) -> None:
        """Add a new plot with the given name, and type.

        Args:
            plot_name: The name of the new plot.
            plot_type: The type of the new plot.
        """

    @abstractmethod
    def add_plot(self, plot_num: int) -> None:
        """Add a new plot.

        Args:
            plot_num: The number of the plot to add.
        """

    @abstractmethod
    def delete_plot(self, plot_num: int) -> None:
        """Delete a plot.

        Args:
            plot_num: The number of the plot to delete.
        """


class PowerMixin(ABC):
    """A mixin class which adds methods and properties for handling power objects."""

    @abstractmethod
    def add_power(self, power_meas_num: int) -> None:
        """Add a new power measurement.

        Args:
            power_meas_num: The number of the power measurement to add.
        """

    @abstractmethod
    def delete_power(self, power_num: int) -> None:
        """Delete a power.

        Args:
            power_num: The number of the power to delete.
        """


class ReferenceMixin(ABC):
    """A mixin class which adds methods and properties for handling reference objects."""

    @abstractmethod
    def add_ref(self, ref_num: int) -> None:
        """Add a new ref.

        Args:
            ref_num: The number of the ref to add.
        """

    @abstractmethod
    def delete_ref(self, ref_num: int) -> None:
        """Delete a ref.

        Args:
            ref_num: The number of the ref to delete.
        """

    @abstractmethod
    def recall_reference(self, reference_path: str, ref_number: Union[int, str]) -> None:
        """Recall a reference waveform file.

        Args:
            reference_path: The path to the reference waveform file.
            ref_number: The REF number to recall the waveform to.
        """

    @abstractmethod
    def save_waveform_to_reference(self, waveform: str, reference: str) -> None:
        """Save the specified waveform to a reference.

        Args:
            waveform: The name of the waveform to save, e.g. CH1, MATH1, etc.
            reference: The name of the target reference, e.g. REF1.
        """


class SearchMixin(ABC):
    """A mixin class which adds methods and properties for handling search objects."""

    @abstractmethod
    def add_search(self, search_num: int) -> None:
        """Add a new search.

        Args:
            search_num: The number of the search to add.
        """

    @abstractmethod
    def delete_search(self, search_num: int) -> None:
        """Delete a search.

        Args:
            search_num: The number of the search to delete.
        """
