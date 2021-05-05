# BOJ_Algorithm_python
파이썬을 이용한 알고리즘 문제풀이

```python
# 기본 틀
import math
import sys

# from collections import deque

# a, b, c = get_line(), 입력값 2개 이상
# array:list = list(get_line()), 리스트로 입력 받고 싶을 때
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())

# a = get_input(), 입력값 1개
get_input: int = lambda: int(sys.stdin.readline())

# print_list(array), 리스트를 한번에 출력해줌.
print_list = lambda lst: print('\n'.join(map(str, lst)))

# for index in find_indexes(value, array), 배열안에 해당 값(x)의 모든 인덱스를 찾아줌.
# find_indexes = lambda x, lst: [idx for idx, value in enumerate(lst) if value == x]


def solution():
    pass


def main():
    #  입력값을 받아 solution 의 인자로 넘깁니다.
    solution()


if __name__ == '__main__':
    main()
```