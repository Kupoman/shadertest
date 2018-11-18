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
def vec2_arg_function():
    return Function(
        'function',
        'float',
        [
            Argument('vec2', 'a'),
        ],
        'float function (vec2 a) { return a.x + a.y; }'
    )


@pytest.fixture
def vec3_arg_function():
    return Function(
        'function',
        'float',
        [
            Argument('vec3', 'a'),
        ],
        'float function (vec3 a) { return a.x + a.y + a.z; }'
    )


@pytest.fixture
def vec4_arg_function():
    return Function(
        'function',
        'float',
        [
            Argument('vec4', 'a'),
        ],
        'float function (vec4 a) { return a.x + a.y + a.z + a.w; }'
    )


@pytest.fixture
def ivec2_arg_function():
    return Function(
        'function',
        'int',
        [
            Argument('ivec2', 'a'),
        ],
        'int function (ivec2 a) { return a.x + a.y; }'
    )


@pytest.fixture
def ivec3_arg_function():
    return Function(
        'function',
        'int',
        [
            Argument('ivec3', 'a'),
        ],
        'int function (ivec3 a) { return a.x + a.y + a.z; }'
    )


@pytest.fixture
def ivec4_arg_function():
    return Function(
        'function',
        'int',
        [
            Argument('ivec4', 'a'),
        ],
        'int function (ivec4 a) { return a.x + a.y + a.z + a.w; }'
    )


@pytest.fixture
def bvec2_arg_function():
    return Function(
        'function',
        'bool',
        [
            Argument('bvec2', 'a'),
        ],
        'bool function (bvec2 a) { return any(a); }'
    )


@pytest.fixture
def bvec3_arg_function():
    return Function(
        'function',
        'bool',
        [
            Argument('bvec3', 'a'),
        ],
        'bool function (bvec3 a) { return any(a); }'
    )


@pytest.fixture
def bvec4_arg_function():
    return Function(
        'function',
        'bool',
        [
            Argument('bvec4', 'a'),
        ],
        'bool function (bvec4 a) { return any(a); }'
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
