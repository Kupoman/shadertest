import pytest

from shadertest.shader_parser import (
    Function,
)


@pytest.fixture
def no_arg_function():
    return Function(
        'function',
        'float',
        [],
        'float function () { return 1.0; }'
    )
