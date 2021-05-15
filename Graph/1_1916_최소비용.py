# 기본 틀
import heapq
import sys

# a, b, c = get_line(), 입력값 2개 이상
# array:list = list(get_line()), 리스트로 입력 받고 싶을 때
get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())

# a = get_input(), 입력값 1개
get_input: int = lambda: int(sys.stdin.readline())

# print_list(array), 리스트를 한번에 출력해줌.
print_list = lambda lst: print('\n'.join(map(str, lst)))


# for index in find_indexes(value, array), 배열안에 해당 값(x)의 모든 인덱스를 찾아줌.
# find_indexes = lambda x, lst: [idx for idx, value in enumerate(lst) if value == x]


def solution(start: int, arrival: int, n: int, edges: list):
    # 최솟값 우선순위 트리, heapq 라이브러리로 배열을 이용하여 구현.
    heap_que = []
    distance = [sys.maxsize for _ in range(n)]

    for to, cost in edges[start]:
        # 해당 힙(리스트) , 값
        # 값이 튜플인 경우 첫번째 값을 기준으로 최소 힙정렬
        heapq.heappush(heap_que, (cost, to))

    while heap_que:
        cost, node = heapq.heappop(heap_que)

        # (start -> node)의 최단거리 갱신, 다익스트라
        # 우선순위 큐를 이용하여 visited 없이 빠른속도로 갱신.
        if distance[node] > cost:
            distance[node] = cost
            for node, c in edges[node]:  # 각각의 노드에 대한 최솟값 업데이트
                heapq.heappush(heap_que, (cost + c, node))

    print(distance[arrival])


def main():
    #  입력값을 받아 solution 의 인자로 넘깁니다.
    n = get_input()
    m = get_input()
    edges = [[] for _ in range(n)]

    # 배열 사용의 편의를 위해 위치값에 -1 (0부터 시작)
    for i in range(m):
        start, end, cost = get_line()
        edges[start - 1].append([end - 1, cost])

    start, end = get_line()  # 출발지, 도착지
    solution(start - 1, end - 1, n, edges)


if __name__ == '__main__':
    main()
