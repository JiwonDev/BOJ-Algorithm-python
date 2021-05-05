import math
import sys


def delete_leaf(target: int, parent: list):
    """
    그래프에서 target을 삭제했을 때 없어지는 parent[node]를 None 으로 바꿔줌.

    :param target: 삭제할 노드 parent[target]
    :param parent: 부모를 나타낸 트리정보
    :return: None
    """

    find_indexes = lambda x, lst: [idx for idx, value in enumerate(lst) if value == x]
    parent[target] = None

    # target 이랑 같은 값인 요소들의 인덱스
    # == target 을 부모로 가지는 노드들을 기준으로 재귀적으로 node를 삭제함.
    for node in find_indexes(target, parent):
        delete_leaf(node, parent)


def main():
    get_line: list = lambda: map(int, sys.stdin.readline().rstrip().split())
    get_input: int = lambda: int(input())
    print_list = lambda lst: print('\n'.join(map(str, lst)))
    # a, b, c = get_line()
    # a = get_input()
    # print_list(array)

    n: int = get_input()
    parent: list = list(get_line())
    target: int = get_input()

    delete_leaf(target, parent)

    # value 가 None 이 아니고 , index 가 parent 리스트 안에 없는 경우
    leaves = [value for idx, value in enumerate(parent) if (value is not None) and (idx not in parent)]
    print(len(leaves))


if __name__ == "__main__":
    main()
