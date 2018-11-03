import OpenGL.GL as gl
import pytest

from shadertest.shader_function import ShaderFunction
from shadertest.graphics_context import GraphicsContext

@pytest.fixture(scope='module')
def graphics_context():
    with GraphicsContext() as context:
        yield context

def test_no_args(graphics_context, no_arg_function):
    shader_function = ShaderFunction(no_arg_function)
    assert shader_function.gl_program != 0
    assert shader_function.gl_return_buffer != 0
    assert shader_function.gl_return_texture != 0
    assert shader_function.gl_vao != 0
    assert shader_function() == 1.0
