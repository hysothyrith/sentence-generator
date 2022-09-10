import itertools
from typing import Iterable

from pipe import select


def materialize(*args):
    return list(itertools.chain(*(generate(*x) for x in args)))


def generate(*args):
    return generate_from_format(
        parse_format(*args), [arg for arg in args if not isinstance(arg, str)]
    )


def parse_format(*args):
    return "".join([arg if isinstance(arg, str) else "{}" for arg in args])


def generate_from_format(format: str, args: Iterable):
    return itertools.product(*args) | select(lambda x: [format.format(*x)])
