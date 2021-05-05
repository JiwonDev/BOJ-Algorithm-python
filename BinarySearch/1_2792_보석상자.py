import math
import sys

# a, b, c = get_line(), 입력값 2개 이상
# array:list = list(get_line()), 리스트로 입력 받고 싶을 때
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())

# a = get_input(), 입력값 1개
get_input: int = lambda: int(sys.stdin.readline())

# print_list(array), 리스트를 한번에 출력해줌.
print_list = lambda lst: print('\n'.join(map(str, lst)))

# for index in find_indexes(value, array), 배열안에 해당 값(x)의 모든 인덱스를 찾아줌.
find_indexes = lambda x, lst: [idx for idx, value in enumerate(lst) if value == x]


def solution(n: int, m: int, box: list):
    start = 1  # 최솟값
    end = max(box)  # 최대값

    answer = end
    while start <= end:
        count = 0
        current = math.floor((start + end) / 2)

        # current 로 잘랐을 때(나눴을 때) 받을 수 있는 학생의 수
        # ex) color(14), current(5) 일 때 >> count = 3
        for color in box:
            count += math.ceil(color / current)

        if count > n:
            start = current + 1
        elif count <= n:
            if current < answer:
                answer = current
            end = current - 1

    return answer


def main():
    n, m = get_line()
    box = []
    for _ in range(m):
        box.append(int(sys.stdin.readline()))
    answer = solution(n, m, box)
    print(answer)


if __name__ == "__main__":
    main()
