# BOJ_Algorithm_python

파이썬을 이용한 알고리즘 문제풀이

```python
    PI = 3.14  # 상수명은 대문자로
    my_value = 5  # 변수명은 소문자로

    my_int = value()  # 여러 단어는 언더바(_)로
    _private_value = 3  # 내부에서만 사용되는 함수는 언더바로 시작
    do_func()  # 메서드는 동사로 시작
    class MyClass():# 클래스는 대문자로
    myObject = MyClass()   # 클래스 변수(타입변수)는 CamelCase
```

```python
'''
# 기본 틀
# from collections import deque

# a, b, c = get_line(), 입력값 2개 이상
# array:list = list(get_line()), 리스트로 입력 받고 싶을 때
# a = get_input(), 입력값 1개
# print_list(array), 리스트를 한번에 출력해줌.

# for index in find_indexes(value, array), 배열안에 해당 값(x)의 모든 인덱스를 찾아줌.
# find_indexes = lambda x, lst: [idx for idx, value in enumerate(lst) if value == x]
'''
import math
import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

def solution():
    pass

def main():
    #  입력값을 받아 solution 의 인자로 넘깁니다.
    solution()


if __name__ == '__main__':
    main()
```