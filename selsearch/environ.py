import os

PREFIX = "SELSEARCH"


def get_environment_variable(name, prefix=PREFIX):
    if prefix:
        name = f"{prefix}_{name}"

    return os.environ.get(name, None)
