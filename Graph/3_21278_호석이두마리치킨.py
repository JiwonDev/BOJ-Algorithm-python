import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

'''
#문제
    N개의 정점과 M개의 간선이 주어집니다.
    모든 간선은 가중치 1(시간)을 가집니다.
    모든 정점에서 선택한 2개의 정점 중 가까운 정점과의 거리가 최소가 되게끔 만드시오.
    (= 모든 정점 왕복시간의 합이 최소)

#제약조건
    2 ≤ N ≤ 100
    N-1 ≤ M ≤ N×(N - 1)/2

#입력
    첫 줄 : N, M
    그 다음 (M줄): 간선 정보 Ai, Bi

#출력
    거리가 최소인 정점 2개와 그 거리값 ( Ai, Bi, 거리값 )

#생각
    개수가 작아서 bfs 노가다로 풀어도 될거같긴하다.
    근데 그래프니까 플로이드와샬로 두 정점간의 최단거리를 구해 풀어보자

#풀이
    플로이드와샬로 각 정점 사이 거리를 구한다.
    모든 경우의 수를 돌려보며 최솟값을 찾는다.
'''


def solution(n: int, m: int, dis: list):
    # 모든 정점간 최단거리를 미리 구한다.
    floyd_warshall(n, dis)

    # 응~ 모든 경우의 수 노가다~
    answer = [0, 0, sys.maxsize]
    for store1 in range(n):
        for store2 in range(n):
            if store1 == store2:
                continue
            total = 0
            # 접근성은 X 에서 가장 가까운 호석이 두마리 치킨집까지 왕복하는 최단 시간
            for customer in range(n):
                total += min(dis[customer][store1], dis[customer][store2])

            if answer[2] > total:
                answer[0] = store1 + 1
                answer[1] = store2 + 1
                answer[2] = total

    answer[2] = answer[2] * 2  # 왕복거리를 물어봤으므로 * 2
    print(*answer)


def floyd_warshall(n: int, dis: list):
    '''
    1. 모든 정점간 최단 경로를 모두 구해야하는 경우
    - 플로이드와샬

    2. 시작점으로 부터 최단거리만 구하는 경우
    - 다익스트라 (단, 음의 가중치가 없을 때)
    '''

    for temp in range(n):
        dis[temp][temp] = 0
        for start in range(n):
            for end in range(n):
                dis[start][end] = min(dis[start][temp] + dis[temp][end], dis[start][end])


def main():
    n, m = get_line()
    distance = []

    # max 값으로 초기화된 2차원 배열 생성
    for _ in range(n):
        distance.append([sys.maxsize] * n)

    for _ in range(m):
        a, b = get_line()
        distance[a - 1][b - 1] = 1
        distance[b - 1][a - 1] = 1

    solution(n, m, distance)


if __name__ == '__main__':
    main()
