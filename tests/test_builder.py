import subprocess

import pytest

from shadertest.builder import build
from shadertest.shader_parser import (
    Argument,
    Function,
)


@pytest.fixture
def no_arg_shader(no_arg_function):
    return build(no_arg_function)


def assert_shader(shader, function):
    echo_proc = subprocess.Popen(('echo', shader), stdout=subprocess.PIPE)
    results = subprocess.run(
        ('glslangValidator', '--stdin', '-S', 'frag'),
        stdin=echo_proc.stdout,
        stdout=subprocess.PIPE
    ).stdout
    echo_proc.wait()
    print(shader)
    print(results)
    assert results == b''

    assert '#version' in shader
    assert function.text in shader
    assert 'void main' in shader


def test_no_arg(no_arg_shader, no_arg_function):
    assert_shader(no_arg_shader, no_arg_function)
    assert f'{no_arg_function.name}()' in no_arg_shader
    assert 'uniform imageBuffer result' in  no_arg_shader
