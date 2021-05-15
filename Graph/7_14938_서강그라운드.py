import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())


def solution():
    pass


def floyd_warshall(n: int, dis: list):
    for temp in range(n):
        dis[temp][temp] = 0
        for start in range(n):
            for end in range(n):
                if start != end:
                    dis[start][end] = min(dis[start][temp] + dis[temp][end], dis[start][end])


def main():
    #  입력값을 받아 solution 의 인자로 넘깁니다.
    n, search_range, road_count = get_line()
    item_values: list = list(get_line())
    graph = [[sys.maxsize] * n for _ in range(n)]

    for _ in range(road_count):
        start, end, cost = get_line()
        min_cost = min(graph[start - 1][end - 1], cost)
        graph[start - 1][end - 1] = min_cost
        graph[end - 1][start - 1] = min_cost

    floyd_warshall(n, graph)

    answer = 0
    for i in range(n):
        total = 0
        for j in range(n):
            if graph[i][j] <= search_range:
                total += item_values[j]
        answer = max(total, answer)
    print(answer)


if __name__ == '__main__':
    main()
