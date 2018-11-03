def build_version(function):
    return '#version 420'


def build_output_uniform(function):
    return 'layout(r32f) uniform imageBuffer result;'


def build_call(function):
    return f'imageStore(result, 0, vec4({function.name}(), vec3(0.0)));'


def build_main(function):
    return '\n'.join([
        'void main () {'
        f'\t{build_call(function)}'
        '}'
    ])


def build(function):
    shader = '\n'.join([
        build_version(function),
        build_output_uniform(function),
        function.text,
        build_main(function),
    ])
    return shader
