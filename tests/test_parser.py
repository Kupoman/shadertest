import pytest

import shadertest.shader_parser as parser


@pytest.fixture
def basic_functions():
    with open('./tests/basic.frag') as fin:
        return parser.parse_functions(fin.read())


def test_finding_functions(basic_functions):
    parsed_functions = set(basic_functions.keys())
    for function in basic_functions.values():
        print(function)

    expected_functions = {
        'mad',
        'add',
        'no_op',
        'increment',
        'nested_blocks',
    }

    assert parsed_functions == expected_functions


def test_no_args(basic_functions):
    no_op = basic_functions['no_op']
    assert len(no_op.args) == 0


def assert_simple_args(args):
    for arg in args:
        assert arg.name in ('a', 'b', 'c')
        assert arg.type == 'float'


def test_single_args(basic_functions):
    incr = basic_functions['increment']
    assert len(incr.args) == 1
    assert_simple_args(incr.args)


def test_multi_args(basic_functions):
    mad = basic_functions['mad']
    assert len(mad.args) == 3
    assert_simple_args(mad.args)


def test_return_type(basic_functions):
    mad = basic_functions['mad']
    assert mad.return_type == 'float'


def test_parse_text(basic_functions):
    expected_text = 'float add(float a, float b) {\n    return a + b;\n}\n'
    assert basic_functions['add'].text == expected_text


def test_nested_blocks(basic_functions):
    function = basic_functions['nested_blocks']
    assert function.text.count('}') == 3
