import re
from typing import List
from dataclasses import dataclass


FUNCTION_REGEX = re.compile(
    r'^(?P<returnType>[^#\s]+)\s+(?P<functionName>[^\s(]+)\s*\((?P<args>[^)]*).*?\n}\n',
    re.MULTILINE | re.DOTALL
)

ARGS_REGEX = re.compile(
    r'(?P<type>[^\s]+)\s+(?P<name>[^,)]+),*\s*'
)

@dataclass
class Argument:
    type: str
    name: str


@dataclass
class Function:
    name: str
    return_type: str
    args: List[Argument]
    text: str


def parse_arguments(args: str):
    return [Argument(m['type'], m['name']) for m in ARGS_REGEX.finditer(args)]


def parse_functions(shader: str):
    return {
        match['functionName']:
        Function(
            match['functionName'],
            match['returnType'],
            parse_arguments(match['args']),
            match[0]
        )
        for match in FUNCTION_REGEX.finditer(shader)
        if match['functionName'] != 'main'
    }
