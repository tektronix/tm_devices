"""The connectivity commands module.

These commands are used in the following models:
AWG5200, AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CONNectivity:ACTive <generator_name>
    - CONNectivity:ACTive?
    - CONNectivity:CONNect <hostname>[,<generator_name>]
    - CONNectivity:DISConnect <generator_name>
    - CONNectivity:GANG:CREAte <gang_name>,<member1>,<member2>[,<member3>[,<member4>]]
    - CONNectivity:REMove <generator_name>
    - CONNectivity:STATus? <generator_name>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ConnectivityStatus(SCPICmdReadWithArguments):
    """The ``CONNectivity:STATus`` command.

    Description:
        - This command returns the connection status of the named generator.

    Usage:
        - Using the ``.query(argument)`` method will send the ``CONNectivity:STATus? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CONNectivity:STATus? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - CONNectivity:STATus? <generator_name>
        ```
    """


class ConnectivityRemove(SCPICmdWrite):
    """The ``CONNectivity:REMove`` command.

    Description:
        - This command removes the named generator from SourceXpress. If the named generator is the
          active generator, it is disconnected and removed without warning. If the generator is in a
          gang, the gang and all its members are removed.

    Usage:
        - Using the ``.write(value)`` method will send the ``CONNectivity:REMove value`` command.

    SCPI Syntax:
        ```
        - CONNectivity:REMove <generator_name>
        ```
    """


class ConnectivityGangCreate(SCPICmdWrite):
    """The ``CONNectivity:GANG:CREAte`` command.

    Description:
        - This command creates a gang generator consisting of the specified instruments (members). A
          gang generator can consist of 2 to 4 generators. The gang is placed in the Generator List.

    Usage:
        - Using the ``.write(value)`` method will send the ``CONNectivity:GANG:CREAte value``
          command.

    SCPI Syntax:
        ```
        - CONNectivity:GANG:CREAte <gang_name>,<member1>,<member2>[,<member3>[,<member4>]]
        ```
    """


class ConnectivityGang(SCPICmdRead):
    """The ``CONNectivity:GANG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONNectivity:GANG?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNectivity:GANG?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.create``: The ``CONNectivity:GANG:CREAte`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._create = ConnectivityGangCreate(device, f"{self._cmd_syntax}:CREAte")

    @property
    def create(self) -> ConnectivityGangCreate:
        """Return the ``CONNectivity:GANG:CREAte`` command.

        Description:
            - This command creates a gang generator consisting of the specified instruments
              (members). A gang generator can consist of 2 to 4 generators. The gang is placed in
              the Generator List.

        Usage:
            - Using the ``.write(value)`` method will send the ``CONNectivity:GANG:CREAte value``
              command.

        SCPI Syntax:
            ```
            - CONNectivity:GANG:CREAte <gang_name>,<member1>,<member2>[,<member3>[,<member4>]]
            ```
        """
        return self._create


class ConnectivityDisconnect(SCPICmdWrite):
    """The ``CONNectivity:DISConnect`` command.

    Description:
        - This command disconnects the named generator from SourceXpress.

    Usage:
        - Using the ``.write(value)`` method will send the ``CONNectivity:DISConnect value``
          command.

    SCPI Syntax:
        ```
        - CONNectivity:DISConnect <generator_name>
        ```
    """


class ConnectivityConnect(SCPICmdWrite):
    """The ``CONNectivity:CONNect`` command.

    Description:
        - This command connects SourceXpress to a remote generator using the generator's hostname,
          making the remote generator available for use by SourceXpress. You can also assign a
          unique generator name of the connected generator. If a name is not specified, then the
          hostname is used as the name for the connected generator. The generator name is the name
          that appears in the Generator List.

    Usage:
        - Using the ``.write(value)`` method will send the ``CONNectivity:CONNect value`` command.

    SCPI Syntax:
        ```
        - CONNectivity:CONNect <hostname>[,<generator_name>]
        ```
    """


class ConnectivityActive(SCPICmdWrite, SCPICmdRead):
    """The ``CONNectivity:ACTive`` command.

    Description:
        - This command sets or returns the active generator using the connected generator name. The
          active generator is the target of instrument operations. Only a single generator can be
          active at once. The set version of this command must use the actual generator name as
          listed in the Generator List (in the SourceXpress application).

    Usage:
        - Using the ``.query()`` method will send the ``CONNectivity:ACTive?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNectivity:ACTive?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CONNectivity:ACTive value`` command.

    SCPI Syntax:
        ```
        - CONNectivity:ACTive <generator_name>
        - CONNectivity:ACTive?
        ```
    """


class Connectivity(SCPICmdRead):
    """The ``CONNectivity`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONNectivity?`` query.
        - Using the ``.verify(value)`` method will send the ``CONNectivity?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.active``: The ``CONNectivity:ACTive`` command.
        - ``.connect``: The ``CONNectivity:CONNect`` command.
        - ``.disconnect``: The ``CONNectivity:DISConnect`` command.
        - ``.gang``: The ``CONNectivity:GANG`` command tree.
        - ``.remove``: The ``CONNectivity:REMove`` command.
        - ``.status``: The ``CONNectivity:STATus`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "CONNectivity"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._active = ConnectivityActive(device, f"{self._cmd_syntax}:ACTive")
        self._connect = ConnectivityConnect(device, f"{self._cmd_syntax}:CONNect")
        self._disconnect = ConnectivityDisconnect(device, f"{self._cmd_syntax}:DISConnect")
        self._gang = ConnectivityGang(device, f"{self._cmd_syntax}:GANG")
        self._remove = ConnectivityRemove(device, f"{self._cmd_syntax}:REMove")
        self._status = ConnectivityStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def active(self) -> ConnectivityActive:
        """Return the ``CONNectivity:ACTive`` command.

        Description:
            - This command sets or returns the active generator using the connected generator name.
              The active generator is the target of instrument operations. Only a single generator
              can be active at once. The set version of this command must use the actual generator
              name as listed in the Generator List (in the SourceXpress application).

        Usage:
            - Using the ``.query()`` method will send the ``CONNectivity:ACTive?`` query.
            - Using the ``.verify(value)`` method will send the ``CONNectivity:ACTive?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CONNectivity:ACTive value``
              command.

        SCPI Syntax:
            ```
            - CONNectivity:ACTive <generator_name>
            - CONNectivity:ACTive?
            ```
        """
        return self._active

    @property
    def connect(self) -> ConnectivityConnect:
        """Return the ``CONNectivity:CONNect`` command.

        Description:
            - This command connects SourceXpress to a remote generator using the generator's
              hostname, making the remote generator available for use by SourceXpress. You can also
              assign a unique generator name of the connected generator. If a name is not specified,
              then the hostname is used as the name for the connected generator. The generator name
              is the name that appears in the Generator List.

        Usage:
            - Using the ``.write(value)`` method will send the ``CONNectivity:CONNect value``
              command.

        SCPI Syntax:
            ```
            - CONNectivity:CONNect <hostname>[,<generator_name>]
            ```
        """
        return self._connect

    @property
    def disconnect(self) -> ConnectivityDisconnect:
        """Return the ``CONNectivity:DISConnect`` command.

        Description:
            - This command disconnects the named generator from SourceXpress.

        Usage:
            - Using the ``.write(value)`` method will send the ``CONNectivity:DISConnect value``
              command.

        SCPI Syntax:
            ```
            - CONNectivity:DISConnect <generator_name>
            ```
        """
        return self._disconnect

    @property
    def gang(self) -> ConnectivityGang:
        """Return the ``CONNectivity:GANG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONNectivity:GANG?`` query.
            - Using the ``.verify(value)`` method will send the ``CONNectivity:GANG?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.create``: The ``CONNectivity:GANG:CREAte`` command.
        """
        return self._gang

    @property
    def remove(self) -> ConnectivityRemove:
        """Return the ``CONNectivity:REMove`` command.

        Description:
            - This command removes the named generator from SourceXpress. If the named generator is
              the active generator, it is disconnected and removed without warning. If the generator
              is in a gang, the gang and all its members are removed.

        Usage:
            - Using the ``.write(value)`` method will send the ``CONNectivity:REMove value``
              command.

        SCPI Syntax:
            ```
            - CONNectivity:REMove <generator_name>
            ```
        """
        return self._remove

    @property
    def status(self) -> ConnectivityStatus:
        """Return the ``CONNectivity:STATus`` command.

        Description:
            - This command returns the connection status of the named generator.

        Usage:
            - Using the ``.query(argument)`` method will send the ``CONNectivity:STATus? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CONNectivity:STATus? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - CONNectivity:STATus? <generator_name>
            ```
        """
        return self._status
