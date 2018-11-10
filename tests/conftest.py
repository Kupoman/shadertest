import pytest

from shadertest.shader_parser import (
    Argument,
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


@pytest.fixture
def one_arg_function():
    return Function(
        'function',
        'float',
        [
            Argument('float', 'a')
        ],
        'float function (float a) { return a * 2.0; }'
    )
