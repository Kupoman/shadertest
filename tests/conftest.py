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
            Argument('float', 'a'),
        ],
        'float function (float a) { return a * 2.0; }'
    )


@pytest.fixture
def two_arg_function():
    return Function(
        'function',
        'float',
        [
            Argument('float', 'a'),
            Argument('float', 'b'),
        ],
        'float function (float a, float b) { return a + b; }'
    )


@pytest.fixture
def int_arg_function():
    return Function(
        'function',
        'float',
        [
            Argument('int', 'a'),
        ],
        'float function (int a) { return a / 2; }'
    )


@pytest.fixture
def bool_arg_function():
    return Function(
        'function',
        'float',
        [
            Argument('bool', 'a'),
        ],
        'float function (bool a) { return (a) ? 1.0 : 0.0; }'
    )


@pytest.fixture
def bool_return_function():
    return Function(
        'function',
        'bool',
        [],
        'bool function () { return true; }'
    )


@pytest.fixture
def int_return_function():
    return Function(
        'function',
        'int',
        [],
        'int function () { return 1; }'
    )
