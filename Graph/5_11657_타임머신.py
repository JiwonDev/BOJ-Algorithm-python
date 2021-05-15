import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

'''
#문제
    n(1 ≤ n ≤ 500)개의 도시가 있다. 
    m(1 ≤ m ≤ 6000)개의 버스가 있다. 
    각 버스는 한 번 사용할 때 필요한 비용이 있다.
    근데 타임머신이 있어 비용이 음수일 수도 있다.

    1번도시에서 출발하여 해당 도시로 가는 최소비용
    (경로가 없거나 무한음수라면 -1)
    
#입력
    첫 줄 : N
    둘째 줄 : M
    그 다음 (M줄): 간선 정보 Ai, Bi, costi

#풀이
    벨만 포드로 음수 간선 순환이 있는 최단 경로를 구한다.
    * 음수 사이클이 없다면 다익스트라로 가능.
'''


def solution(n: int, m: int, graph: list):
    dis = [sys.maxsize] * (n + 1)

    if bellman_ford(1, n, dis, graph):
        for x in dis[2:]:  # 0번쨰는 없고 1번쨰는 start
            if x != sys.maxsize:
                print(x)
            else:
                print(-1)
    else:
        print(-1)


def bellman_ford(start: int, n: int, dis: list, graph: list):
    '''
    # 1. 출발노드 지정
    # 2. 최단 거리 테이블 초기화
    # 3. 다음 과정을 N-1반복
        3-1 전체 간선을 하나씩 확인
        3-2 각 간선을 거쳐 다른 노드로 가는 비용을 계산
    # 4. [3]에서 최단거리가 구해져야 정상임.
        여기에서 한번 더 최단거리를 구해 음수간선 여부 확인.

        만약 음수간선이 생긴다면 답은 없음.

    :param start: 출발노드
    :param n: 노드의 갯수
    :param dis: start에서 각 정점의 최단거리
    :param graph: 인접행렬 그래프
    :return:
    '''
    dis[start] = 0

    for i in range(n):
        # 전체 간선 확인, n번
        for start, end, cost in graph:
            if dis[start] != sys.maxsize and dis[end] > dis[start] + cost:
                if i == n - 1:
                    return False
                dis[end] = dis[start] + cost
    return True


def main():
    n, m = get_line()
    graph = []

    for _ in range(m):
        a, b, cost = get_line()
        graph.append([a, b, cost])

    solution(n, m, graph)


if __name__ == '__main__':
    main()
