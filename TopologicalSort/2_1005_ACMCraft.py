import heapq
import sys
from collections import defaultdict

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())


def solution(depths: list, build_next: dict, build_time: list, target: int):
    # 바로 지을 수 있는 것들, depth == 0
    que = [(build_time[i], i) for i, depth in enumerate(depths) if depth == 0]

    # 리스트 -> 최소 힙 변환
    heapq.heapify(que)

    while que:
        # heapq.pop == 건물 건설완료
        time, building = heapq.heappop(que)

        # target 건설
        if building == target:
            print(time)
            break

        for next_building in build_next[building]:
            # depths 값 갱신, -= 1
            depths[next_building] -= 1

            # 현재 깊이가 0이라면 (건설 가능하다면)
            if depths[next_building] == 0:
                _time = time + build_time[next_building]
                _building = next_building
                heapq.heappush(que, (_time, _building))


def main():
    testcase = get_input()

    for _ in range(testcase):
        n, k = get_line()

        depths = [0 for _ in range(n)]  # 그래프에서 해당 노드의 깊이

        build_time = list(get_line())  # 건물당 건설에 필요한 시간
        build_next = defaultdict(list)  # 다음에 지을 수 있는 건물들

        for _ in range(k):
            first, second = get_line()
            depths[second - 1] += 1
            build_next[first - 1].append(second - 1)

        target = get_input()  # 지어야하는 건물들.
        target -= 1  # 인덱스 0 부터 시작을 위해 -1

        solution(depths, build_next, build_time, target)


if __name__ == '__main__':
    main()
