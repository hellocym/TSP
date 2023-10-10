import numpy as np


def BruteForce(MAP: np.ndarray, start: int = 0):
    '''
    Solve TSP using Brute Force algorithm (DFS).
    Time complexity: O(N!).
    '''
    N = MAP.shape[0]
    vis = np.zeros(N, dtype=bool)
    vis[start] = True
    path = [start]
    distance = 0
    min_distance = np.inf
    min_path = []

    def dfs():
        nonlocal distance, min_distance, min_path
        if len(path) == N:
            if distance + MAP[path[-1], start] < min_distance:
                min_distance = distance + MAP[path[-1], start]
                min_path = path.copy()
            return
        for i in range(N):
            if not vis[i]:
                vis[i] = True
                path.append(i)
                distance += MAP[path[-2], i]
                dfs()
                distance -= MAP[path[-2], i]
                path.pop()
                vis[i] = False

    dfs()
    return min_path, min_distance


if __name__ == '__main__':
    MAP = np.array([
        [0, 1, 2, 3],
        [1, 0, 4, 5],
        [2, 4, 0, 6],
        [3, 5, 6, 0]
    ])
    print(BruteForce(MAP))