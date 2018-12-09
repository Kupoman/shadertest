import pytest

import shadertest


@pytest.fixture(scope='module')
def basic_shader():
    with shadertest.ShaderContext.from_file('tests/basic.frag') as funcs:
        yield funcs


def test_add(basic_shader):
    assert basic_shader.add(4, 2) == 6
