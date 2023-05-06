"""
Verify my understanding of basic decorator functionality.
"""

from typing import Callable

def decorator_pre_post_print(fnc: Callable, pre_print: str = "pre-wrap message", post_print: str = "post-wrap message") -> Callable:
    def closure(printable: str = "Hello, World.") -> None:
        print(f"{pre_print}")
        fnc()
        print(f"{post_print}")

    return closure

def printable(to_print: str = "Hello, World."):
    print(f"{to_print}")

def main():
    decorated_func_with_default = decorator_pre_post_print(printable)
    # decorated_func_with_specified = decorator_pre_post_print(f"specified string")
    decorated_func_with_default()
    # decorated_func_with_specified()

if __name__ == "__main__":
    main()
