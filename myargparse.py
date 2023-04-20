import math
import argparse

parser = argparse.ArgumentParser(description='Calculate area of rectangle.')
parser.add_argument('-w', '--width', type=int, required=True, help='Width of rectangle.')
parser.add_argument('-l', '--length', type=int, required=True, help='Length of rectangle.')
args = parser.parse_args()

def area_rectangle(width: int, length: int) -> int:
    return width * length

def main() -> None:
    width, length = args.width, args.length
    area = area_rectangle(width, length)
    print(f"Reactangle area is {width} * {length} = {area}")

main()

