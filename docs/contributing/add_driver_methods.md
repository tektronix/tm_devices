# Adding new methods to drivers

This guide will walk through the steps needed to add a new methods to existing
device drivers.

## Device Type Abstraction

Because of the inheritance structure of the device drivers (see the
[architecture diagrams](../advanced/architecture.md#main-device-types)), new
methods should be added to the highest applicable class in the tree. All methods
for each type of device (Scope, AFG, SMU, etc.) need to be defined in that
device type's abstract class, or higher up the tree, to enable accurate type
hinting for each different device type tree. Unless the implementation is the
same for all subclasses of that device type, the abstract class's implementation
should simply `raise NotImplementedError`.

## New method addition example

```python
# scope.py
# Abstract class
class Scope(...):
    def new_method(self):
        # Abstract class raises an error.
        raise NotImplementedError


# tekscope.py
# Specific model class
class TekScope(Scope):
    def new_method(self):
        # Model-specific implementation goes here.
        print("This is a new method for the TekScope class!")
```
