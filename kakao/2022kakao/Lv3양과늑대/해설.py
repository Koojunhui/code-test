from collections import defaultdict

def solution(info, edges):
    # 트리 구성
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)

    return dfs(0, 0, 0, [0], info, graph)

def dfs(node, sheep, wolf, available, info, graph):
    # 현재 노드 방문
    if info[node] == 0:
        sheep += 1
    else:
        wolf += 1

    # 늑대 수가 양 이상이면 중단
    if wolf >= sheep:
        return sheep - 1  # 현재는 실패한 상태이므로 마지막 유효 상태로

    # 다음 방문할 수 있는 노드 갱신
    next_nodes = available.copy()
    next_nodes.remove(node)
    next_nodes.extend(graph[node])

    max_sheep = sheep
    for next_node in next_nodes:
        max_sheep = max(max_sheep, dfs(next_node, sheep, wolf, next_nodes, info, graph))
    return max_sheep

