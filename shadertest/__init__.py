from . import shader_parser


class ShaderFunctions:
    def parse(self, shader_text):
        function_data = shader_parser.parse_functions(shader_text)
        for functionName in function_data.keys():
            self.__dict__[functionName] = lambda *x: 0


def parse(shader_text):
    functions = ShaderFunctions()
    functions.parse(shader_text)
    return functions
