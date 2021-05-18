import heapq
import sys
from collections import defaultdict

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())


def solution(n: int, build_time: list, build_next: dict, depths: list):
    que = [(build_time[i], i) for i, depth in enumerate(depths) if depth == 0]

    heapq.heapify(que)
    answer = [0 for _ in range(n)]

    while que:
        time, buliding = heapq.heappop(que)
        answer[buliding] = time

        for next_building in build_next[buliding]:
            depths[next_building] -= 1
            if depths[next_building] == 0:
                _time = time + build_time[next_building]
                _building = next_building
                heapq.heappush(que, (_time, _building))
    print(*answer)


def main():
    n = get_input()
    depths = [0 for _ in range(n)]
    build_time = [0 for _ in range(n)]
    build_next = defaultdict(list)

    for current in range(n):
        inputs = list(get_line())
        build_time[current] = inputs[0]

        # 선행으로 지어야 되는 건물
        for preceding in inputs[1:-1]:
            preceding -= 1  # 인덱스 0
            build_next[preceding].append(current)
            depths[current] += 1

    # print("Depths")
    # pprint(depths)
    # print("\nBuild Time")
    # pprint(build_time)
    # print("\nBuild Next")
    # pprint(list(build_next.items()))

    solution(n, build_time, build_next, depths)


if __name__ == '__main__':
    main()
