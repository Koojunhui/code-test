from collections import deque

# 너비 우선 탐색 (start - 시작 노드 번호, n - 노드 개수)
def bfs(start, graph, n):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

# 깊이 우선 탐색 (node - 현재 탐색중인 노드, visited - 방문 체크 배열)
def dfs(node, graph, visited):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, graph, visited)
