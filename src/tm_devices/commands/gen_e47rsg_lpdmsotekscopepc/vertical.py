"""The vertical commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - VERTical:DESKew:FROM:CUSTOMPROPAgation <NR3>
    - VERTical:DESKew:FROM:CUSTOMPROPAgation?
    - VERTical:DESKew:FROM:SOUrce CH<x>
    - VERTical:DESKew:FROM:SOUrce?
    - VERTical:DESKew:STATIC EXECute
    - VERTical:DESKew:TO:CUSTOMPROPAgation <NR3>
    - VERTical:DESKew:TO:SOUrce CH<x>
    - VERTical:DESKew:TO:SOUrce?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class VerticalDeskewToSource(SCPICmdWrite, SCPICmdRead):
    """The ``VERTical:DESKew:TO:SOUrce`` command.

    Description:
        - This command sets or queries the target channel for performing channel-to-channel deskew
          adjustment. Target sources can be any of the live analog channels.

    Usage:
        - Using the ``.query()`` method will send the ``VERTical:DESKew:TO:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``VERTical:DESKew:TO:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VERTical:DESKew:TO:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - VERTical:DESKew:TO:SOUrce CH<x>
        - VERTical:DESKew:TO:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source.
    """


class VerticalDeskewToCustompropagation(SCPICmdWrite):
    """The ``VERTical:DESKew:TO:CUSTOMPROPAgation`` command.

    Description:
        - This command sets or queries a target (TO) delay that can be specified by the user when
          the propagation delay of the target (TO) probe used for deskew cannot be detected
          automatically.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``VERTical:DESKew:TO:CUSTOMPROPAgation value`` command.

    SCPI Syntax:
        ```
        - VERTical:DESKew:TO:CUSTOMPROPAgation <NR3>
        ```

    Info:
        - ``<NR3>`` is a target (TO) delay that can be specified by the user when the propagation
          delay of the target (TO) probe used for deskew cannot be detected automatically.
    """


class VerticalDeskewTo(SCPICmdRead):
    """The ``VERTical:DESKew:TO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VERTical:DESKew:TO?`` query.
        - Using the ``.verify(value)`` method will send the ``VERTical:DESKew:TO?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.custompropagation``: The ``VERTical:DESKew:TO:CUSTOMPROPAgation`` command.
        - ``.source``: The ``VERTical:DESKew:TO:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custompropagation = VerticalDeskewToCustompropagation(
            device, f"{self._cmd_syntax}:CUSTOMPROPAgation"
        )
        self._source = VerticalDeskewToSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def custompropagation(self) -> VerticalDeskewToCustompropagation:
        """Return the ``VERTical:DESKew:TO:CUSTOMPROPAgation`` command.

        Description:
            - This command sets or queries a target (TO) delay that can be specified by the user
              when the propagation delay of the target (TO) probe used for deskew cannot be detected
              automatically.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``VERTical:DESKew:TO:CUSTOMPROPAgation value`` command.

        SCPI Syntax:
            ```
            - VERTical:DESKew:TO:CUSTOMPROPAgation <NR3>
            ```

        Info:
            - ``<NR3>`` is a target (TO) delay that can be specified by the user when the
              propagation delay of the target (TO) probe used for deskew cannot be detected
              automatically.
        """
        return self._custompropagation

    @property
    def source(self) -> VerticalDeskewToSource:
        """Return the ``VERTical:DESKew:TO:SOUrce`` command.

        Description:
            - This command sets or queries the target channel for performing channel-to-channel
              deskew adjustment. Target sources can be any of the live analog channels.

        Usage:
            - Using the ``.query()`` method will send the ``VERTical:DESKew:TO:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``VERTical:DESKew:TO:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VERTical:DESKew:TO:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - VERTical:DESKew:TO:SOUrce CH<x>
            - VERTical:DESKew:TO:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source.
        """
        return self._source


class VerticalDeskewStatic(SCPICmdWrite):
    """The ``VERTical:DESKew:STATIC`` command.

    Description:
        - This command executes static deskew using the deskew settings.

    Usage:
        - Using the ``.write(value)`` method will send the ``VERTical:DESKew:STATIC value`` command.

    SCPI Syntax:
        ```
        - VERTical:DESKew:STATIC EXECute
        ```

    Info:
        - ``EXECute`` will execute static deskew using the deskew settings.
    """


class VerticalDeskewFromSource(SCPICmdWrite, SCPICmdRead):
    """The ``VERTical:DESKew:FROM:SOUrce`` command.

    Description:
        - This command sets or queries the source channel for performing channel-to-channel deskew
          adjustment. Sources can be any of the analog channels.

    Usage:
        - Using the ``.query()`` method will send the ``VERTical:DESKew:FROM:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``VERTical:DESKew:FROM:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VERTical:DESKew:FROM:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - VERTical:DESKew:FROM:SOUrce CH<x>
        - VERTical:DESKew:FROM:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source.
    """


class VerticalDeskewFromCustompropagation(SCPICmdWrite, SCPICmdRead):
    """The ``VERTical:DESKew:FROM:CUSTOMPROPAgation`` command.

    Description:
        - This command sets or queries a target (FROM) delay that you can specify when the
          propagation delay of the target (FROM) probe used for deskew cannot be detected
          automatically.

    Usage:
        - Using the ``.query()`` method will send the ``VERTical:DESKew:FROM:CUSTOMPROPAgation?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``VERTical:DESKew:FROM:CUSTOMPROPAgation?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``VERTical:DESKew:FROM:CUSTOMPROPAgation value`` command.

    SCPI Syntax:
        ```
        - VERTical:DESKew:FROM:CUSTOMPROPAgation <NR3>
        - VERTical:DESKew:FROM:CUSTOMPROPAgation?
        ```

    Info:
        - ``<NR3>`` is a target (FROM) delay that you can specify when the propagation delay of the
          target (FROM) probe used for deskew cannot be detected automatically.
    """


class VerticalDeskewFrom(SCPICmdRead):
    """The ``VERTical:DESKew:FROM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VERTical:DESKew:FROM?`` query.
        - Using the ``.verify(value)`` method will send the ``VERTical:DESKew:FROM?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.custompropagation``: The ``VERTical:DESKew:FROM:CUSTOMPROPAgation`` command.
        - ``.source``: The ``VERTical:DESKew:FROM:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custompropagation = VerticalDeskewFromCustompropagation(
            device, f"{self._cmd_syntax}:CUSTOMPROPAgation"
        )
        self._source = VerticalDeskewFromSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def custompropagation(self) -> VerticalDeskewFromCustompropagation:
        """Return the ``VERTical:DESKew:FROM:CUSTOMPROPAgation`` command.

        Description:
            - This command sets or queries a target (FROM) delay that you can specify when the
              propagation delay of the target (FROM) probe used for deskew cannot be detected
              automatically.

        Usage:
            - Using the ``.query()`` method will send the
              ``VERTical:DESKew:FROM:CUSTOMPROPAgation?`` query.
            - Using the ``.verify(value)`` method will send the
              ``VERTical:DESKew:FROM:CUSTOMPROPAgation?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``VERTical:DESKew:FROM:CUSTOMPROPAgation value`` command.

        SCPI Syntax:
            ```
            - VERTical:DESKew:FROM:CUSTOMPROPAgation <NR3>
            - VERTical:DESKew:FROM:CUSTOMPROPAgation?
            ```

        Info:
            - ``<NR3>`` is a target (FROM) delay that you can specify when the propagation delay of
              the target (FROM) probe used for deskew cannot be detected automatically.
        """
        return self._custompropagation

    @property
    def source(self) -> VerticalDeskewFromSource:
        """Return the ``VERTical:DESKew:FROM:SOUrce`` command.

        Description:
            - This command sets or queries the source channel for performing channel-to-channel
              deskew adjustment. Sources can be any of the analog channels.

        Usage:
            - Using the ``.query()`` method will send the ``VERTical:DESKew:FROM:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``VERTical:DESKew:FROM:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VERTical:DESKew:FROM:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - VERTical:DESKew:FROM:SOUrce CH<x>
            - VERTical:DESKew:FROM:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source.
        """
        return self._source


class VerticalDeskew(SCPICmdRead):
    """The ``VERTical:DESKew`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VERTical:DESKew?`` query.
        - Using the ``.verify(value)`` method will send the ``VERTical:DESKew?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.from``: The ``VERTical:DESKew:FROM`` command tree.
        - ``.static``: The ``VERTical:DESKew:STATIC`` command.
        - ``.to``: The ``VERTical:DESKew:TO`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._from = VerticalDeskewFrom(device, f"{self._cmd_syntax}:FROM")
        self._static = VerticalDeskewStatic(device, f"{self._cmd_syntax}:STATIC")
        self._to = VerticalDeskewTo(device, f"{self._cmd_syntax}:TO")

    @property
    def from_(self) -> VerticalDeskewFrom:
        """Return the ``VERTical:DESKew:FROM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VERTical:DESKew:FROM?`` query.
            - Using the ``.verify(value)`` method will send the ``VERTical:DESKew:FROM?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.custompropagation``: The ``VERTical:DESKew:FROM:CUSTOMPROPAgation`` command.
            - ``.source``: The ``VERTical:DESKew:FROM:SOUrce`` command.
        """
        return self._from

    @property
    def static(self) -> VerticalDeskewStatic:
        """Return the ``VERTical:DESKew:STATIC`` command.

        Description:
            - This command executes static deskew using the deskew settings.

        Usage:
            - Using the ``.write(value)`` method will send the ``VERTical:DESKew:STATIC value``
              command.

        SCPI Syntax:
            ```
            - VERTical:DESKew:STATIC EXECute
            ```

        Info:
            - ``EXECute`` will execute static deskew using the deskew settings.
        """
        return self._static

    @property
    def to(self) -> VerticalDeskewTo:
        """Return the ``VERTical:DESKew:TO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VERTical:DESKew:TO?`` query.
            - Using the ``.verify(value)`` method will send the ``VERTical:DESKew:TO?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.custompropagation``: The ``VERTical:DESKew:TO:CUSTOMPROPAgation`` command.
            - ``.source``: The ``VERTical:DESKew:TO:SOUrce`` command.
        """
        return self._to


class Vertical(SCPICmdRead):
    """The ``VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``VERTical?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.deskew``: The ``VERTical:DESKew`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "VERTical") -> None:
        super().__init__(device, cmd_syntax)
        self._deskew = VerticalDeskew(device, f"{self._cmd_syntax}:DESKew")

    @property
    def deskew(self) -> VerticalDeskew:
        """Return the ``VERTical:DESKew`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VERTical:DESKew?`` query.
            - Using the ``.verify(value)`` method will send the ``VERTical:DESKew?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.from``: The ``VERTical:DESKew:FROM`` command tree.
            - ``.static``: The ``VERTical:DESKew:STATIC`` command.
            - ``.to``: The ``VERTical:DESKew:TO`` command tree.
        """
        return self._deskew
