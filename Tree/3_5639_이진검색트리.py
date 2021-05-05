import math
import sys
sys.setrecursionlimit(10 ** 9)


class MyLib:
    get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
    get_input: int = lambda: int(input())
    print_list = lambda lst: print('\n'.join(map(str, lst)))
    find_indexes = lambda x, lst: [idx for idx, value in enumerate(lst) if value == x]
    # a, b, c = get_line()
    # array:list = list(get_line())
    # a = get_input()
    # print_list(array)
    # for index in find_indexes(value, array)


def print_postorder(start, end, inputs: list):
    if start > end:
        return
    else:
        current = inputs[start]
        mid = end + 1

        # mid 찾기
        # 현재 노드 ~ end
        for index in range(start + 1, end + 1):
            if current < inputs[index]:
                mid = index
                break

        # start+1 부터 mid-1 은 왼쪽 트리
        # mid 부터 end는 오른쪽 트리
        print_postorder(start + 1, mid - 1, inputs)
        print_postorder(mid, end, inputs)
        print(current)


def main():
    # 이진검색트리를 전위순회(root->left->right)한 결과를 보고 후위순회(left->right->root)로 바꾸기.
    inputs = []

    for line in sys.stdin:
        for var in line.split():
            inputs.append(int(var))
    print_postorder(0, len(inputs) - 1, inputs)


if __name__ == "__main__":
    main()
