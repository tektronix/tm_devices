"""The connected commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CONNected:REQUested:STATus <NR1>
    - CONNected:STATus?
    - CONNected:USAGe:TRack:REQUested:STATus <NR1>
    - CONNected:USAGe:TRack:STATus?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ConnectedUsageTrackStatus(SCPICmdRead):
    """The ``CONNected:USAGe:TRack:STATus`` command.

    Description:
        - This query command returns the tracking usage status of the Connected Scope Preference
          feature. On the instrument, the feature is found in Utility > User Preferences > Other >
          Connected Scope Preferences.

    Usage:
        - Using the ``.query()`` method will send the ``CONNected:USAGe:TRack:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNected:USAGe:TRack:STATus?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONNected:USAGe:TRack:STATus?
        ```
    """


class ConnectedUsageTrackRequestedStatus(SCPICmdWrite):
    """The ``CONNected:USAGe:TRack:REQUested:STATus`` command.

    Description:
        - This command sets the tracking usage status of the Connected Scope Preference feature.
          After issuing the status command, the ``CONNected:SAVEPREferences`` command should be set
          immediately to make the feature enabled. On the instrument, the feature is found in
          Utility > User Preferences > Other > Connected Scope Preferences.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``CONNected:USAGe:TRack:REQUested:STATus value`` command.

    SCPI Syntax:
        ```
        - CONNected:USAGe:TRack:REQUested:STATus <NR1>
        ```

    Info:
        - ``<NR1>`` enables or disables the Connected Scope Preference feature. The argument can be
          either 1 or 0. Setting 1 will enable the tracking usage status of the Connected Scope
          Preference feature.
    """


class ConnectedUsageTrackRequested(SCPICmdRead):
    """The ``CONNected:USAGe:TRack:REQUested`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONNected:USAGe:TRack:REQUested?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNected:USAGe:TRack:REQUested?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.status``: The ``CONNected:USAGe:TRack:REQUested:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = ConnectedUsageTrackRequestedStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def status(self) -> ConnectedUsageTrackRequestedStatus:
        """Return the ``CONNected:USAGe:TRack:REQUested:STATus`` command.

        Description:
            - This command sets the tracking usage status of the Connected Scope Preference feature.
              After issuing the status command, the ``CONNected:SAVEPREferences`` command should be
              set immediately to make the feature enabled. On the instrument, the feature is found
              in Utility > User Preferences > Other > Connected Scope Preferences.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``CONNected:USAGe:TRack:REQUested:STATus value`` command.

        SCPI Syntax:
            ```
            - CONNected:USAGe:TRack:REQUested:STATus <NR1>
            ```

        Info:
            - ``<NR1>`` enables or disables the Connected Scope Preference feature. The argument can
              be either 1 or 0. Setting 1 will enable the tracking usage status of the Connected
              Scope Preference feature.
        """
        return self._status


class ConnectedUsageTrack(SCPICmdRead):
    """The ``CONNected:USAGe:TRack`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONNected:USAGe:TRack?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNected:USAGe:TRack?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.requested``: The ``CONNected:USAGe:TRack:REQUested`` command tree.
        - ``.status``: The ``CONNected:USAGe:TRack:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._requested = ConnectedUsageTrackRequested(device, f"{self._cmd_syntax}:REQUested")
        self._status = ConnectedUsageTrackStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def requested(self) -> ConnectedUsageTrackRequested:
        """Return the ``CONNected:USAGe:TRack:REQUested`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONNected:USAGe:TRack:REQUested?``
              query.
            - Using the ``.verify(value)`` method will send the ``CONNected:USAGe:TRack:REQUested?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.status``: The ``CONNected:USAGe:TRack:REQUested:STATus`` command.
        """
        return self._requested

    @property
    def status(self) -> ConnectedUsageTrackStatus:
        """Return the ``CONNected:USAGe:TRack:STATus`` command.

        Description:
            - This query command returns the tracking usage status of the Connected Scope Preference
              feature. On the instrument, the feature is found in Utility > User Preferences > Other
              > Connected Scope Preferences.

        Usage:
            - Using the ``.query()`` method will send the ``CONNected:USAGe:TRack:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``CONNected:USAGe:TRack:STATus?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONNected:USAGe:TRack:STATus?
            ```
        """
        return self._status


class ConnectedUsage(SCPICmdRead):
    """The ``CONNected:USAGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONNected:USAGe?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNected:USAGe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.track``: The ``CONNected:USAGe:TRack`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._track = ConnectedUsageTrack(device, f"{self._cmd_syntax}:TRack")

    @property
    def track(self) -> ConnectedUsageTrack:
        """Return the ``CONNected:USAGe:TRack`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONNected:USAGe:TRack?`` query.
            - Using the ``.verify(value)`` method will send the ``CONNected:USAGe:TRack?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.requested``: The ``CONNected:USAGe:TRack:REQUested`` command tree.
            - ``.status``: The ``CONNected:USAGe:TRack:STATus`` command.
        """
        return self._track


class ConnectedStatus(SCPICmdRead):
    """The ``CONNected:STATus`` command.

    Description:
        - This query command returns the status of the Connected Scope Preference feature. On the
          instrument, the feature is found in Utility > User Preferences > Other > Connected Scope
          Preferences.

    Usage:
        - Using the ``.query()`` method will send the ``CONNected:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNected:STATus?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONNected:STATus?
        ```
    """


class ConnectedRequestedStatus(SCPICmdWrite):
    """The ``CONNected:REQUested:STATus`` command.

    Description:
        - This command sets the status of the Connected Scope Preference feature. After issuing the
          status command, the ``CONNected:SAVEPREferences`` command should be set immediately to
          make the feature enabled. On the instrument, the feature is found in Utility > User
          Preferences > Other > Connected Scope Preferences.

    Usage:
        - Using the ``.write(value)`` method will send the ``CONNected:REQUested:STATus value``
          command.

    SCPI Syntax:
        ```
        - CONNected:REQUested:STATus <NR1>
        ```

    Info:
        - ``<NR1>`` enables or disables the Connected Scope Preference feature. The argument can be
          either 1 or 0. Setting 1 will enable the feature.
    """


class ConnectedRequested(SCPICmdRead):
    """The ``CONNected:REQUested`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONNected:REQUested?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNected:REQUested?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.status``: The ``CONNected:REQUested:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = ConnectedRequestedStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def status(self) -> ConnectedRequestedStatus:
        """Return the ``CONNected:REQUested:STATus`` command.

        Description:
            - This command sets the status of the Connected Scope Preference feature. After issuing
              the status command, the ``CONNected:SAVEPREferences`` command should be set
              immediately to make the feature enabled. On the instrument, the feature is found in
              Utility > User Preferences > Other > Connected Scope Preferences.

        Usage:
            - Using the ``.write(value)`` method will send the ``CONNected:REQUested:STATus value``
              command.

        SCPI Syntax:
            ```
            - CONNected:REQUested:STATus <NR1>
            ```

        Info:
            - ``<NR1>`` enables or disables the Connected Scope Preference feature. The argument can
              be either 1 or 0. Setting 1 will enable the feature.
        """
        return self._status


class Connected(SCPICmdRead):
    """The ``CONNected`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONNected?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNected?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.requested``: The ``CONNected:REQUested`` command tree.
        - ``.status``: The ``CONNected:STATus`` command.
        - ``.usage``: The ``CONNected:USAGe`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CONNected") -> None:
        super().__init__(device, cmd_syntax)
        self._requested = ConnectedRequested(device, f"{self._cmd_syntax}:REQUested")
        self._status = ConnectedStatus(device, f"{self._cmd_syntax}:STATus")
        self._usage = ConnectedUsage(device, f"{self._cmd_syntax}:USAGe")

    @property
    def requested(self) -> ConnectedRequested:
        """Return the ``CONNected:REQUested`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONNected:REQUested?`` query.
            - Using the ``.verify(value)`` method will send the ``CONNected:REQUested?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.status``: The ``CONNected:REQUested:STATus`` command.
        """
        return self._requested

    @property
    def status(self) -> ConnectedStatus:
        """Return the ``CONNected:STATus`` command.

        Description:
            - This query command returns the status of the Connected Scope Preference feature. On
              the instrument, the feature is found in Utility > User Preferences > Other > Connected
              Scope Preferences.

        Usage:
            - Using the ``.query()`` method will send the ``CONNected:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``CONNected:STATus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONNected:STATus?
            ```
        """
        return self._status

    @property
    def usage(self) -> ConnectedUsage:
        """Return the ``CONNected:USAGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONNected:USAGe?`` query.
            - Using the ``.verify(value)`` method will send the ``CONNected:USAGe?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.track``: The ``CONNected:USAGe:TRack`` command tree.
        """
        return self._usage
