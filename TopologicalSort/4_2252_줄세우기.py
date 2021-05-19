import sys
from collections import defaultdict
from collections import deque

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())


def solution(n: int, student_next: dict, depths: list):
    que = deque([item for item, depth in enumerate(depths) if depth == 0])

    answer = []
    while que:
        student = que.pop()
        answer.append(student + 1)

        for next_student in student_next[student]:
            depths[next_student] -= 1
            if depths[next_student] == 0:
                que.append(next_student)
    print(*answer)


def main():
    n, m = get_line()

    depths = [0 for _ in range(n)]
    student_next = defaultdict(list)

    for _ in range(m):
        first, second = get_line()
        student_next[first - 1].append(second - 1)
        depths[second - 1] += 1

    solution(n, student_next, depths)


if __name__ == '__main__':
    main()
