def build_version():
    return '#version 420'


def build_output_uniforms(function):
    out_uniform = 'layout(r32f) uniform imageBuffer result;'
    arg_uniforms = [f'uniform {arg.type} {arg.name};' for arg in function.args]

    return '\n'.join((out_uniform, *arg_uniforms))


def build_args(function):
    return ', '.join([arg.name for arg in function.args])


def build_call(function):
    args = build_args(function)
    return f'imageStore(result, 0, vec4({function.name}({args}), vec3(0.0)));'


def build_main(function):
    return '\n'.join([
        'void main () {'
        f'\t{build_call(function)}'
        '}'
    ])


def build(function):
    shader = '\n'.join([
        build_version(),
        build_output_uniforms(function),
        function.text,
        build_main(function),
    ])
    return shader
