# type annotations
from typing import Iterable

# internal libs
from .interface import FooInterface

# public interface
__all__ = ['FooManager', ]


class FooManager:
    """A FooManager manages the Foo."""

    source: Iterable[str]
    interface: FooInterface

    def __init__(self, source: Iterable[str], interface: FooInterface = None) -> None:
        """Direct initialization with `interface`."""
        self.source = source
        self.interface = interface or FooInterface.new()
