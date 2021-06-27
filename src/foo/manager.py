# internal libs
from .interface import FooInterface

# public interface
__all__ = ['FooManager', ]


class FooManager:
    """A FooManager manages the Foo."""

    interface: FooInterface

    def __init__(self, interface: FooInterface = None) -> None:
        """Direct initialization with `interface`."""
        self.interface = interface or FooInterface.new()
