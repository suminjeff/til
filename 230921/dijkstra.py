import sys

sys.stdin = open("dijkstra.txt", "r")
input = sys.stdin.readline
inf = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]

# 방문 표시 리스트
visited = [False] * (n + 1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [inf] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())

    # a에서 b노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def get_smallest_node():
    min_value = inf
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx


def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# print(distance)
dijkstra(start)
print(distance)
for i in range(1, n + 1):
    if distance[i] == inf:
        print('INFINITE')
    else:
        print(distance[i])