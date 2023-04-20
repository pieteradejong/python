import argparse
from sys import argv

def area_rectangle(width: int, length: int) -> int:
    return width * length

def parse_args(_args: list):
    parser = argparse.ArgumentParser(description='Calculate area of rectangle.')
    parser.add_argument('-w', '--width', type=int, required=True, help='Width of rectangle.')
    parser.add_argument('-l', '--length', type=int, required=True, help='Length of rectangle.')
    return parser.parse_args(_args)

def main() -> None:
    args = parse_args(argv[1:])
    area = area_rectangle(args.width, args.length)
    print(f"Reactangle area is {args.width} * {args.length} = {area}")

main()

