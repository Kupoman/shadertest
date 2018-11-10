import ctypes

import OpenGL.GL as gl
from OpenGL.GL import shaders

from . import builder


VERTEX_SOURCE = '''
#version 120
void main() {
    gl_Position = gl_Vertex;
}
'''

UNIFORM_MAP = {
    'float': gl.glUniform1f,
    'int': gl.glUniform1i,
    'bool': gl.glUniform1i,
}

class ShaderFunction:
    def __init__(self, function_data):
        self.function_data = function_data
        self.gl_vao = self.create_gl_vao()
        self.gl_program = self.create_gl_program()
        self.gl_return_buffer = self.create_gl_buffer()
        self.gl_return_texture = self.create_gl_buffer_texture(self.gl_return_buffer)

    def create_gl_vao(self):
        return gl.glGenVertexArrays(1)

    def create_gl_program(self):
        shader_source = builder.build(self.function_data)
        print(shader_source)
        shader = shaders.compileShader(shader_source, gl.GL_FRAGMENT_SHADER)
        vertex_shader = shaders.compileShader(VERTEX_SOURCE, gl.GL_VERTEX_SHADER)
        program = shaders.compileProgram(vertex_shader, shader)
        return program


    def create_gl_buffer(self):
        buffer = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_TEXTURE_BUFFER, buffer)
        host_buffer = ctypes.c_float(10)
        gl.glBufferData(gl.GL_TEXTURE_BUFFER, 4, ctypes.byref(host_buffer), gl.GL_STREAM_READ)
        gl.glBindBuffer(gl.GL_TEXTURE_BUFFER, 0)
        return buffer

    def create_gl_buffer_texture(self, buffer):
        texture = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_BUFFER, texture)
        gl.glTexBuffer(gl.GL_TEXTURE_BUFFER, gl.GL_R32F, buffer)
        gl.glBindTexture(gl.GL_TEXTURE_BUFFER, 0)
        return texture

    def __call__(self, *args):
        takes = len(self.function_data.args)
        given = len(args)
        if given != takes:
            name = self.function_data.name
            raise TypeError(f'{name} takes {takes} positional argument but {given} were given')

        self.bind(args)
        self.draw()
        rvalue = self.read_return_buffer()
        self.unbind()
        return rvalue

    def bind(self, args):
        gl.glBindVertexArray(self.gl_vao)
        gl.glUseProgram(self.gl_program)
        gl.glBindImageTexture(
            0,
            self.gl_return_texture,
            0,
            gl.GL_FALSE,
            0,
            gl.GL_WRITE_ONLY,
            gl.GL_R32F
        )
        gl.glUniform1i(0, 0)
        for i, (arg, value) in enumerate(zip(self.function_data.args, args)):
            UNIFORM_MAP[arg.type](i + 1, value)

    def draw(self):
        gl.glDrawArrays(gl.GL_POINTS, 0, 1)

    def read_return_buffer(self):
        host_buffer = ctypes.c_float(42)
        gl.glBindBuffer(gl.GL_TEXTURE_BUFFER, self.gl_return_buffer)
        gl.glGetBufferSubData(gl.GL_TEXTURE_BUFFER, 0, 4, ctypes.byref(host_buffer))
        gl.glBindBuffer(gl.GL_TEXTURE_BUFFER, 0)
        return host_buffer.value

    def unbind(self):
        gl.glBindTexture(gl.GL_TEXTURE_BUFFER, 0)
        gl.glUseProgram(0)
        gl.glBindVertexArray(0)
