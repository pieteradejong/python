from functools import wraps
from time import time
import csv
from typing import List, Tuple, Dict
from inspect import getmembers, isfunction

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


def write_to_csv(filehandle: str=None, data: list[list]=None, headers: list=None) -> tuple[str, int]:
    """Data must be list (length zero or more) of lists."""
    if not filehandle:
        raise ValueError('Must provide file handle')
    if not data and not headers:
        raise ValueError('Must provide either column headers or at least one data row')
    if not isinstance(data, list) or any(not isinstance(d, list) for d in data):
        raise ValueError('Input data must be a list of zero or more lists.')

    TARGET_FILE_NAME = 'output.csv' # TODO add path
    with open(TARGET_FILE_NAME, 'w', encoding='UTF-8') as fh:
        writer = csv.writer(fh)
        writer.writerow(headers)
        writer.writerows(data)

    return (filehandle, len(data))
        
def read_from_csv(filehandle: str=None) -> list:
    if not filehandle:
        raise ValueError('Must provide file handle')
    
    with open(filehandle, 'r', newline='') as fh:
        data = []
        reader = csv.reader(filehandle)
        for row in reader:
            data.append(row)
    return data

def main():
    print('Testing csv write:')
    headers = ['city', 'state', 'level']
    data = [ ['sf', 'CA', 45], ['nyc', 'NY', 12], ['miami', 'FL', 83] ]
    csv = write_to_csv('test.csv', data, headers)
    print(csv)

if __name__ == "__main__":
    main()

"""
TODO Context: added csv read/write defs, add tests by calling; then pytests
"""