import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

'''
#문제
    n(2 ≤ n ≤ 100)개의 도시가 있다. 
    m(1 ≤ m ≤ 100,000)개의 버스가 있다. 
    각 버스는 한 번 사용할 때 필요한 비용이 있다.

    모든 도시의 쌍 (A, B)에 대해서 필요한 비용의 최솟값
    
#입력
    첫 줄 : N
    둘째 줄 : M
    그 다음 (M줄): 간선 정보 Ai, Bi, costi

#풀이
    플로이드와샬로 각 정점 사이 거리를 구한다.
'''


def solution(n: int, m: int, dis: list):
    # 모든 정점간 최단거리를 미리 구한다.
    floyd_warshall(n, dis)
    for line in dis:
        for item in line:
            if item == sys.maxsize:
                print(0, end=' ')
            else:
                print(item, end=' ')
        print()


def floyd_warshall(n: int, dis: list):
    for temp in range(n):
        dis[temp][temp] = 0
        for start in range(n):
            for end in range(n):
                if start != end:
                    dis[start][end] = min(dis[start][temp] + dis[temp][end], dis[start][end])


def main():
    n = get_input()
    m = get_input()
    distance = []

    # max 값으로 초기화된 2차원 배열 생성
    for _ in range(n):
        distance.append([sys.maxsize] * n)

    for _ in range(m):
        a, b, cost = get_line()
        distance[a - 1][b - 1] = min(distance[a - 1][b - 1], cost)

    solution(n, m, distance)


if __name__ == '__main__':
    main()
