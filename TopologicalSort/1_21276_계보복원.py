import sys
from collections import defaultdict

get_line: iter = lambda: map(str, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())


def solution(n: int, names: list, memorys: list):
    '''
    출력
    가문의 수 K
    각 가문들의 root들의 이름
    (사전순)[이름, 자식의 수, 자식]

    :param n: int , 살고 있는 사람의 수
    :param names: list, [자식, 조상]
    - 모든 이름은 len(1이상~6이하), 알파벳  소문자, 중복없음

    :param memorys: list[list] 기억하고 있는 정보들
    :return:
    '''

    name_to_depth = dict.fromkeys(names, 0)
    depth_to_name = defaultdict(list)
    map = defaultdict(list)

    # dict{ key:부모, value:[ 자식1, 자식2, 자식3 ] }
    # dict{ key:이름, value:깊이 }
    for child, parent in memorys:
        map[parent].append(child)
        name_to_depth[child] += 1

    # dict{ key:깊이, value:[ 이름1, 이름2, 이름3 ] }
    for name, depth in name_to_depth.items():
        depth_to_name[depth].append(name)

    answer = defaultdict(list)
    for depth, nodes in sorted(depth_to_name.items()):
        for name in nodes:  # 자식들 중 [ 내 깊이 + 1 ] 인 자식만 저장
            answer[name] = [item for item in map[name] if name_to_depth[item] == (depth + 1)]

    print(len(depth_to_name[0]))
    print(*depth_to_name[0])

    # 저장된 정답을 이름순으로 정렬하여 출력
    for name, children in sorted(answer.items()):
        print(f'{name} {len(children)}', end=" ")
        print(*children)


def main():
    n: int = get_input()
    names: list = list(get_line())
    m: int = get_input()
    memorys: list = []

    for _ in range(m):
        memorys.append(list(get_line()))
    solution(n, names, memorys)


if __name__ == '__main__':
    main()
