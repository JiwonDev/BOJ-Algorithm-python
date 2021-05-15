import heapq
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


def prim(start, edges, n):
    heap_que = []
    visited = [False for _ in range(n)]
    visited[start] = True

    for cost, end in edges[start]:
        heapq.heappush(heap_que, (cost, end))

    answer = 0
    count = 0
    while heap_que and count < n:
        cost, node = heapq.heappop(heap_que)

        if not visited[node]:
            visited[node] = True
            count += 1
            answer += cost
            for c, end in edges[node]:
                heapq.heappush(heap_que, (c, end))

    print(answer)


def main():
    n, e = get_line()  # 점의 갯수, 간선의 갯수

    edges = [[] for _ in range(n)]
    for _ in range(e):
        start, end, cost = get_line()
        edges[start - 1].append([cost, end - 1])
        edges[end - 1].append([cost, start - 1])

    prim(0, edges, n)


if __name__ == '__main__':
    main()
