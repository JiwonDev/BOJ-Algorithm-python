# 기본 틀
import sys

# from collections import deque

# a, b, c = get_line(), 입력값 2개 이상
# array:list = list(get_line()), 리스트로 입력 받고 싶을 때
get_line: iter = lambda:map(int, sys.stdin.readline().rstrip().split())

# a = get_input(), 입력값 1개
get_input = lambda:int(sys.stdin.readline())

# print_list(array), 리스트를 한번에 출력해줌.
print_list = lambda lst:print('\n'.join(map(str, lst)))


# for index in find_indexes(value, array), 배열안에 해당 값(x)의 모든 인덱스를 찾아줌.
# find_indexes = lambda x, lst: [idx for idx, value in enumerate(lst) if value == x]

def solution(n: int, order: list):
    tabs = [0 for _ in range(n)]
    answer = 0

    for i, new in enumerate(order, start=0):
        if new in tabs:
            pass

        elif not all(tabs):  # 사용중이 아닌데 반칸이 있다면
            tabs[tabs.index(0)] = new

        else:  # 사용중이 아닌데 빈칸이 없다면
            change = 0  # 교체될 대상
            max_waiting = 0  # remains 안에서 가장 나중에 사용되는 아이템의 인덱스
            remains = order[i:]

            for item in tabs:
                if item not in remains:
                    change = item
                    break
                elif remains.index(item) > max_waiting:
                    max_waiting = remains.index(item)
                    change = item

            tabs[tabs.index(change)] = new
            answer += 1

    print(answer)


def main():
    #  입력값을 받아 solution 의 인자로 넘깁니다.
    n, k = get_line()  # 사실 k는 필요없음.
    lst = list(get_line())
    solution(n, lst)


if __name__ == '__main__':
    main()
