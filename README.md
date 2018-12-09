# shadertest
A pyhton library for unit testing GLSL functions

## Example
Below we have a very simple fragment shader called `add.frag`.
```glsl
#version 330

out vec4 outColor;

float add(float a, float b) {
    return a + b;
}
void main() {
	outColor = vec4(add(0.5, 0.5));
}
```

To test using shadertest, we just need to create a `ShaderContext`, and start calling functions from the shader.
```python
import pytest

import shadertest


@pytest.fixture(scope='module')
def basic_shader():
    with shadertest.ShaderContext.from_file('add.frag') as funcs:
        yield funcs


def test_add(basic_shader):
    assert basic_shader.add(4, 2) == 6
```
