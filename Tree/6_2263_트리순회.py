import math
import sys


class MyLib:
    get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
    get_input: int = lambda: int(input())
    print_list = lambda lst: print('\n'.join(map(str, lst)))
    find_indexes = lambda x, lst: [idx for idx, value in enumerate(lst) if value == x]
    # a, b, c = get_line()
    # array:list = list(get_line())
    # a = get_input()
    # print_list(array)
    # for index in find_indexes(value, array)


def main():
    n = MyLib.get_input()

if __name__ == "__main__":
    main()
