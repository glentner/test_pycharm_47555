# external libs
import pytest

# internal libs
from foo.interface import FooInterface, DEFAULT_CONFIG


@pytest.mark.unit
class TestFooInterface:
    """Unit tests for FooInterface."""

    def test_build(self) -> None:
        """Create an instance of FooInterface."""
        interface = FooInterface({})
        assert isinstance(interface, FooInterface)

    def test_attributes(self) -> None:
        """FooInterface.config is same as passed to constructor."""
        config = {'a': 1, 'b': True, 'c': None}
        interface = FooInterface(config)
        assert interface.config == config

    def test_new(self) -> None:
        """FooInterface.new() returns default configuration."""
        interface = FooInterface.new()
        assert isinstance(interface, FooInterface)
        assert interface.config == DEFAULT_CONFIG
