import OpenGL.GL as gl
import pytest

from shadertest.shader_function import ShaderFunction
from shadertest.graphics_context import GraphicsContext

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
