# type annotations
from __future__ import annotations
from typing import Dict, Any

# standard libs
from dataclasses import dataclass

# public interface
__all__ = ['FooInterface', 'DEFAULT_CONFIG', ]


DEFAULT_CONFIG: Dict[str, Any] = {
    'a': 1,
    'b': False,
}


@dataclass
class FooInterface:
    """Interface for Foo."""

    config: Dict[str, Any]

    @classmethod
    def new(cls) -> FooInterface:
        """Default interface."""
        return cls(DEFAULT_CONFIG)
