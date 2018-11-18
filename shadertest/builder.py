from .type_map import TYPE_MAP


def build_version():
    return '#version 420'


def build_output_uniforms(function):
    layout = TYPE_MAP[function.return_type]['shader_layout']
    buffer_type = TYPE_MAP[function.return_type]['shader_buffer']
    out_uniform = f'layout({layout}) uniform {buffer_type} result;'
    arg_uniforms = [f'uniform {arg.type} {arg.name};' for arg in function.args]

    return '\n'.join((out_uniform, *arg_uniforms))


def build_args(function):
    return ', '.join([arg.name for arg in function.args])


def build_call(function):
    args = build_args(function)
    return TYPE_MAP[function.return_type]['shader_store'](function.name, args)


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
