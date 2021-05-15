import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())


def bellman_ford(n: int, dis: list, graph: list):
    for i in range(n):
        # 전체 간선 확인, n번
        for cur, end, cost in graph:
            if dis[end] > dis[cur] + cost:
                if i == n - 1:
                    return False
                dis[end] = dis[cur] + cost
    return True


def solution(n: int, edge: list):
    dis = [sys.maxsize] * n
    if not bellman_ford(n, dis, edge):
        print("YES")
    else:
        print("NO")


def main():
    testcase = get_input()
    for _ in range(testcase):
        edge = []

        n, plus_count, minus_count = get_line()
        for _ in range(plus_count):
            start, end, cost = get_line()
            edge.append([start - 1, end - 1, cost])
            edge.append([end - 1, start - 1, cost])
        for _ in range(minus_count):
            start, end, cost = get_line()
            edge.append([start - 1, end - 1, -cost])
        solution(n, edge)


if __name__ == '__main__':
    main()
