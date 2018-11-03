import OpenGL.GL as gl

from shadertest.graphics_context import GraphicsContext


def test_gl():
    with GraphicsContext() as ctx:
        assert gl.glGetString(gl.GL_VENDOR) is not None
    assert gl.glGetString(gl.GL_VENDOR) is None
