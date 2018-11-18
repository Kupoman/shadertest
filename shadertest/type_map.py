import ctypes

import OpenGL.GL as gl


TYPE_MAP = {
    'float': {
        'uniform': gl.glUniform1f,
        'ctype': ctypes.c_float,
        'buffer_type': gl.GL_R32F,
        'shader_layout': 'r32f',
        'shader_buffer': 'imageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, vec4({name}({args}), vec3(0.0)));'
    },
    'vec2': {
        'uniform': gl.glUniform2f,
        'ctype': (ctypes.c_float * 2),
        'buffer_type': gl.GL_RG32F,
        'shader_layout': 'rg32f',
        'shader_buffer': 'imageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, vec4({name}({args}), vec2(0.0)));'
    },
    'vec3': {
        'uniform': gl.glUniform3f,
        'ctype': (ctypes.c_float * 4),
        'buffer_type': gl.GL_RGBA32F,
        'shader_layout': 'rgba32f',
        'shader_buffer': 'imageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, vec4({name}({args}), 0.0));'
    },
    'vec4': {
        'uniform': gl.glUniform4f,
        'ctype': (ctypes.c_float * 4),
        'buffer_type': gl.GL_RGBA32F,
        'shader_layout': 'rgba32f',
        'shader_buffer': 'imageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0,{name}({args}));'
    },
    'int': {
        'uniform': gl.glUniform1i,
        'ctype': ctypes.c_int,
        'buffer_type': gl.GL_R32I,
        'shader_layout': 'r32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args}), ivec3(0)));'
    },
    'ivec2': {
        'uniform': gl.glUniform2i,
        'ctype': (ctypes.c_int * 2),
        'buffer_type': gl.GL_RG32I,
        'shader_layout': 'rg32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args}), ivec2(0)));'
    },
    'ivec3': {
        'uniform': gl.glUniform3i,
        'ctype': (ctypes.c_int * 4),
        'buffer_type': gl.GL_RGBA32I,
        'shader_layout': 'rgba32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args}), 0));'
    },
    'ivec4': {
        'uniform': gl.glUniform4i,
        'ctype': (ctypes.c_int * 4),
        'buffer_type': gl.GL_RGBA32I,
        'shader_layout': 'rgba32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, {name}({args}));'
    },
    'uint': {
        'uniform': gl.glUniform1ui,
        'ctype': ctypes.c_uint,
        'buffer_type': gl.GL_R32UI,
        'shader_layout': 'r32ui',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args}), ivec3(0)));'
    },
    'ivec2': {
        'uniform': gl.glUniform2i,
        'ctype': (ctypes.c_int * 2),
        'buffer_type': gl.GL_RG32I,
        'shader_layout': 'rg32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args}), ivec2(0)));'
    },
    'ivec3': {
        'uniform': gl.glUniform3i,
        'ctype': (ctypes.c_int * 4),
        'buffer_type': gl.GL_RGBA32I,
        'shader_layout': 'rgba32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args}), 0));'
    },
    'ivec4': {
        'uniform': gl.glUniform4i,
        'ctype': (ctypes.c_int * 4),
        'buffer_type': gl.GL_RGBA32I,
        'shader_layout': 'rgba32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, {name}({args}));'
    },
    'bool': {
        'uniform': gl.glUniform1i,
        'ctype': ctypes.c_int,
        'buffer_type': gl.GL_R32I,
        'shader_layout': 'r32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args}), ivec3(0)));'
    },
    'bvec2': {
        'uniform': gl.glUniform2i,
        'ctype': (ctypes.c_int * 2),
        'buffer_type': gl.GL_RG32I,
        'shader_layout': 'rg32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args}), ivec2(0)));'
    },
    'bvec3': {
        'uniform': gl.glUniform3i,
        'ctype': (ctypes.c_int * 4),
        'buffer_type': gl.GL_RGBA32I,
        'shader_layout': 'rgba32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args}), 0));'
    },
    'bvec4': {
        'uniform': gl.glUniform4i,
        'ctype': (ctypes.c_int * 4),
        'buffer_type': gl.GL_RGBA32I,
        'shader_layout': 'rgba32i',
        'shader_buffer': 'iimageBuffer',
        'shader_store':
            lambda name, args: f'imageStore(result, 0, ivec4({name}({args})));'
    },
}
