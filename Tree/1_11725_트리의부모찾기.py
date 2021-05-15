import sys

def find_parents(graph: list[list], root: int = 1) -> list:
    """
    root 를 받아 그래프를 순회하며 각각의 부모 노드를 parent[node] 에 저장함.

    :param graph: 순회 할 그래프
    :param root: root
    :return: parent: list
    """

    stack = [root]
    parent = [[] for _ in range(len(graph))]

    while stack:
        current = stack.pop()

        for child in graph[current]:
            parent[child] = current
            stack.append(child)

            # 부모가 결정되었다면 중복 제거
            # 제거하지 않으면 사이클이 생겨 무한루프를 돌게 됨.
            graph[child].remove(current)

    return parent


def main():
    get_line: list = lambda: map(int, sys.stdin.readline().rstrip().split())
    get_input: int = lambda: int(input())
    print_list = lambda lst: print('\n'.join(map(str, lst)))
    # a, b, c = get_line()
    # a = get_input()
    # print_list(array)

    n = get_input()
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        first, second = get_line()
        graph[first].append(second)
        graph[second].append(first)

    # [0] : None , [1] : root
    answer = find_parents(graph)[2:]
    print_list(answer)


if __name__ == "__main__":
    main()
