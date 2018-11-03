#version 330

out vec4 outColor;

float mad(float a, float b, float c) {
    return a * b + c;
}

float add(float a, float b) {
    return a + b;
}

void no_op() {
}

float increment(float a) {
    return a += 1;
}

int nested_blocks (){
    if (1 == 1) {
        return 1;
    } else {
        return 0;
    }
}

void main() {
	outColor = vec4(vec3(mad(1.0, 0.5, 0.5)), 1.0);
}
