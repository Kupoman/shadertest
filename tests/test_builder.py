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

@pytest.fixture
def one_arg_shader(one_arg_function):
    return build(one_arg_function)

@pytest.fixture
def two_arg_shader(two_arg_function):
    return build(two_arg_function)

@pytest.fixture
def int_arg_shader(int_arg_function):
    return build(int_arg_function)

@pytest.fixture
def bool_arg_shader(bool_arg_function):
    return build(bool_arg_function)


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


def test_one_arg(one_arg_shader, one_arg_function):
    assert_shader(one_arg_shader, one_arg_function)
    assert 'uniform float a' in one_arg_shader


def test_two_arg(two_arg_shader, two_arg_function):
    assert_shader(two_arg_shader, two_arg_function)
    assert 'uniform float a' in two_arg_shader
    assert 'uniform float b' in two_arg_shader


def test_int_arg(int_arg_shader, int_arg_function):
    assert_shader(int_arg_shader, int_arg_function)
    assert 'uniform int a' in int_arg_shader


def test_bool_arg(bool_arg_shader, bool_arg_function):
    assert_shader(bool_arg_shader, bool_arg_function)
    assert 'uniform bool a' in bool_arg_shader
