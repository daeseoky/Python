from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동을 위한 네방향 정의?????
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
