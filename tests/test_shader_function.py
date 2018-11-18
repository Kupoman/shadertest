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


def test_vec2_arg(graphics_context, vec2_arg_function):
    shader_function = ShaderFunction(vec2_arg_function)
    assert_gl_state(shader_function)
    assert shader_function((1, 2)) == 3


def test_vec3_arg(graphics_context, vec3_arg_function):
    shader_function = ShaderFunction(vec3_arg_function)
    assert_gl_state(shader_function)
    assert shader_function((1, 2, 3)) == 6


def test_vec4_arg(graphics_context, vec4_arg_function):
    shader_function = ShaderFunction(vec4_arg_function)
    assert_gl_state(shader_function)
    assert shader_function((1, 2, 3, 4)) == 10


def test_ivec2_arg(graphics_context, ivec2_arg_function):
    shader_function = ShaderFunction(ivec2_arg_function)
    assert_gl_state(shader_function)
    assert shader_function((1, 2)) == 3


def test_ivec3_arg(graphics_context, ivec3_arg_function):
    shader_function = ShaderFunction(ivec3_arg_function)
    assert_gl_state(shader_function)
    assert shader_function((1, 2, 3)) == 6


def test_ivec4_arg(graphics_context, ivec4_arg_function):
    shader_function = ShaderFunction(ivec4_arg_function)
    assert_gl_state(shader_function)
    assert shader_function((1, 2, 3, 4)) == 10


def test_bvec2_arg(graphics_context, bvec2_arg_function):
    shader_function = ShaderFunction(bvec2_arg_function)
    assert_gl_state(shader_function)
    assert shader_function((False, True)) == True


def test_bvec3_arg(graphics_context, bvec3_arg_function):
    shader_function = ShaderFunction(bvec3_arg_function)
    assert_gl_state(shader_function)
    assert shader_function((False, False, True)) == True


def test_bvec4_arg(graphics_context, bvec4_arg_function):
    shader_function = ShaderFunction(bvec4_arg_function)
    assert_gl_state(shader_function)
    assert shader_function((False, False, False, True)) == True
