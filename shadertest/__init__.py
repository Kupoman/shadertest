import contextlib

from . import shader_parser
from .graphics_context import GraphicsContext
from .shader_function import ShaderFunction


class ShaderContext:
    def __init__(self, shader_text):
        self.function_data = {
            name: data
            for name, data in shader_parser.parse_functions(shader_text).items()
            if data.return_type != 'void'
        }
        self.graphics_context = GraphicsContext()

    @classmethod
    def from_file(cls, filepath):
        with open(filepath) as fin:
            return cls(fin.read())

    def __enter__(self):
        self.graphics_context.__enter__()
        for name, data in self.function_data.items():
            self.__dict__[name] = ShaderFunction(data)
        return self

    def __exit__(self, *args):
        self.graphics_context.__exit__(*args)
