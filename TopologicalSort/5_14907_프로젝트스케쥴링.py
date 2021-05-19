import sys
from collections import defaultdict
from collections import deque

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())


def solution(schedule_next: dict, days: dict, depths: dict):
    que = deque([i for i, depth in depths.items() if depth == 0])
    distance = defaultdict(int)

    #  우선순위가 0인 값들 초기화
    for current, day in [(i, days[i]) for i in que]:
        distance[current] = day

    while que:
        current = que.pop()
        for schedule in schedule_next[current]:
            distance[schedule] = max(distance[schedule], distance[current] + days[schedule])
            depths[schedule] -= 1

            if depths[schedule] == 0:
                que.append(schedule)

    print(max(distance.values()))


def main():
    depths = defaultdict(int)
    schedule_next = defaultdict(list)
    days = defaultdict(int)

    for line in sys.stdin:
        inputs = line.split()

        if len(inputs) == 2:
            first, day = inputs
            depths[first] = 0
        else:
            first, day, second_list = inputs
            for second in second_list:
                schedule_next[second].append(first)
                depths[first] += 1

        days[first] = int(day)

    # pprint(list(days.items()))
    # print()
    # pprint(list(schedule_next.items()))
    # print()
    # pprint(list(depths.items()))

    solution(schedule_next, days, depths)


if __name__ == '__main__':
    main()
