from .__about__ import __version__


def custom_add(a: int, b: int):
    print("addition called...")
    return a + b


def custom_test():
    print("Worked...")


def print_version():
    print(f"Verison: {__version__}")