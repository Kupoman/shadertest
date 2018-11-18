import OpenGL.GL as gl
import pytest

from shadertest.shader_function import ShaderFunction
from shadertest.graphics_context import GraphicsContext
from shadertest.shader_parser import (
    Argument,
    Function,
)

@pytest.fixture(scope='module')
def graphics_context():
    with GraphicsContext() as context:
        yield context


def assert_gl_state(shader_function):
    assert shader_function.gl_program != 0
    assert shader_function.gl_return_buffer != 0
    assert shader_function.gl_return_texture != 0
    assert shader_function.gl_vao != 0


def test_no_args(graphics_context, no_arg_function):
    shader_function = ShaderFunction(no_arg_function)
    assert_gl_state(shader_function)
    assert shader_function() == 1.0


def test_one_arg(graphics_context, one_arg_function):
    shader_function = ShaderFunction(one_arg_function)
    assert_gl_state(shader_function)
    with pytest.raises(TypeError):
        shader_function()
    with pytest.raises(TypeError):
        shader_function(1, 2)
    return_value = shader_function(5)
    assert return_value == 10
    assert type(return_value) == float


def test_int_return(graphics_context, int_return_function):
    shader_function = ShaderFunction(int_return_function)
    assert_gl_state(shader_function)
    return_value = shader_function()
    assert return_value == 1
    assert type(return_value) == int


def test_bool_return(graphics_context, bool_return_function):
    shader_function = ShaderFunction(bool_return_function)
    assert_gl_state(shader_function)
    return_value = shader_function()
    assert return_value == True
    assert type(return_value) == bool


def test_two_arg(graphics_context, two_arg_function):
    shader_function = ShaderFunction(two_arg_function)
    assert_gl_state(shader_function)
    assert shader_function(4, 2) == 6


def test_int_arg(graphics_context, int_arg_function):
    shader_function = ShaderFunction(int_arg_function)
    assert_gl_state(shader_function)
    assert shader_function(3) == 1


def test_bool_arg(graphics_context, bool_arg_function):
    shader_function = ShaderFunction(bool_arg_function)
    assert_gl_state(shader_function)
    assert shader_function(True) == 1.0
    assert shader_function(False) == 0.0


def build_vec_type(base_type, size):
    vec_map = {
        'float': 'vec',
        'double': 'dvec',
        'int': 'ivec',
        'uint': 'uvec',
        'bool': 'bvec',
    }
    return f'{vec_map[base_type]}{size}'

def build_sum_function(base_type, size):
    vec_type = build_vec_type(base_type, size)
    if base_type == 'bool':
        sum_expr = 'any(a)'
    else:
        sum_expr = ' + '.join([f'a[{i}]' for i in range(size)])
    function_data = Function(
        'sum',
        base_type,
        [Argument(vec_type, 'a')],
        f'{base_type} sum ({vec_type} a) {{ return {sum_expr}; }}'
    )
    return ShaderFunction(function_data)


@pytest.mark.parametrize('size', [2, 3, 4])
@pytest.mark.parametrize('base_type', ['float', 'int', 'bool'])
def test_gvec_arg(graphics_context, base_type, size):
    shader_function = build_sum_function(base_type, size)
    assert_gl_state(shader_function)
    if base_type == 'bool':
        arg = (True,) * size
        expect = True
    else:
        arg = range(size)
        expect = sum(arg)
    assert shader_function(arg) == expect


def build_spread_function(base_type, size):
    vec_type = build_vec_type(base_type, size)
    function_data = Function(
        'spread',
        vec_type,
        [Argument(base_type, 'a')],
        f'{vec_type} spread ({base_type} a) {{ return {vec_type}(a); }}'
    )
    return ShaderFunction(function_data)


@pytest.mark.parametrize('size', [2, 3, 4])
@pytest.mark.parametrize('base_type', ['float', 'int', 'bool'])
def test_gvec_return(graphics_context, base_type, size):
    shader_function = build_spread_function(base_type, size)
    assert_gl_state(shader_function)
    arg = {
        'float': 42.0,
        'int': 42,
        'bool': True,
    }[base_type]
    assert shader_function(arg) == (arg,) * size
