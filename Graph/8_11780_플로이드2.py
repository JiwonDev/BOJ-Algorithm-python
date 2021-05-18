import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

'''
n(1 ≤ n ≤ 100)개의 도시가 있다
m(1 ≤ m ≤ 100,000)개의 버스가 있다.
각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 필요한 비용의 최솟값을 구하는 프로그램

단 갈수없는경우 0
'''


def floyd_warshall(n: int, dis: list, mid_node: list):
    for temp in range(n):
        dis[temp][temp] = 0
        for start in range(n):
            for end in range(n):
                new_route = dis[start][temp] + dis[temp][end]
                if start != end and dis[start][end] > new_route:
                    dis[start][end] = new_route
                    mid_node[start][end] = temp

def get_path(start, end, mid_node, path):
    if mid_node[start][end] == (-1):
        # start -> end 까지 중간 노드가 없다면 (연결 되어있다면)
        path.append(start + 1)
        if start != end:
            path.append(end + 1)
    else:
        # start -> ??? -> end 라면
        # s -> m1- > m1 -> m2 -> m3 ->end
        get_path(start, mid_node[start][end], mid_node, path)
        path.pop()  # mid(???)가 중복으로 들어가는걸 방지
        get_path(mid_node[start][end], end, mid_node, path)


def main():
    n = get_input()
    m = get_input()
    graph = [[sys.maxsize] * n for _ in range(n)]
    mid_node = [[-1] * n for i in range(n)]

    for _ in range(m):
        start, end, cost = get_line()
        graph[start - 1][end - 1] = min(graph[start - 1][end - 1], cost)

    # 모든 정점간의 최단거리를 구한다.
    floyd_warshall(n, graph, mid_node)

    for line in graph:
        print(*map(lambda x: 0 if x == sys.maxsize else x, line))

    for start in range(n):
        for end in range(n):
            if start == end:
                print("0")
            else:
                path = []
                get_path(start, end, mid_node, path)
                print(len(path), *path)


if __name__ == '__main__':
    main()
