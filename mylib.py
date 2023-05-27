from functools import wraps
from time import time
import csv
from typing import List, Tuple, Dict

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


def write_to_csv(filehandle: str = None, data: List[List] = None, headers: List = None):
    """Data must be list (length zero or more) of lists."""
    if not filehandle:
        raise ValueError('Must provide file handle')
    if not data and not headers:
        raise ValueError('Must provide either column headers or at least one data row')
    
    

    messages = []
    with open('1-1000.txt', 'r') as fh:
        words = fh.readlines()
        words = [w.rstrip().lower() for w in words]
        words = [w for w in words if w.isalpha()]
        for _ in range(number_of_messages):
            sample_size = randint(MIN_TEXT_WORDS, MAX_TEXT_WORDS)
            words_sampled: list = sample(words, sample_size)
            messages.append(' '.join(words_sampled))
    return messages

def write_to_csv(TARGET_FILE_CSV, data):
    with open(TARGET_FILE_CSV, 'w', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.write(CSV_COLUMN_NAMES)



def main():
    # test_timer(1_000_000)
    pass

if __name__ == "__main__":
    main()

