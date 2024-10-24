# Adding new methods to drivers

This guide will walk through the steps needed to add a new methods to existing
device drivers.

## Device Type Abstraction

Because of the inheritance structure of the device drivers (see the
[architecture diagrams](../advanced/architecture.md#device-types)), new
methods should be added to the highest applicable class in the tree. All methods
for each family of device (TekScope, SMU26xx, PSU2200, etc.) need to be defined in that
device family's abstract class, or higher up the tree, to enable accurate type
hinting for each different device family tree. Unless the implementation is the
same for all subclasses of that device family, the abstract class's implementation
should be decorated as an `@abstractmethod`.

## New method addition example

```python
from abc import abstractmethod


# scope.py
# Abstract class
class Scope(...):
    @abstractmethod
    def new_method(self):
        """Abstract class raises an error."""


# tekscope.py
# Specific model class
class TekScope(Scope):
    def new_method(self):
        # Model-specific implementation goes here.
        print("This is a new method for the TekScope class!")
```
