# package attributes
__version__ = '0.1.0'

# internal libs
from .manager import FooManager
from .interface import FooInterface

# public interface
__all__ = ['FooManager', 'FooInterface', ]
