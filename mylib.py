from functools import wraps
from time import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"START timing function: {func.__name__}()")
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"END timing function: {func.__name__}() - execution time {str(end-start)}")
    return wrapper

@time_function
def test_timer(num):
    return sum(list(range(num)))

def main():
    # test_timer(1_000_000)
    pass

if __name__ == "__main__":
    main()

