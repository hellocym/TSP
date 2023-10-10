import numpy as np

def Greedy(MAP: np.ndarray, start: int = 0):
    '''
    Solve TSP using Greedy algorithm.
    Time complexity: O(n^2).
    '''
    N = MAP.shape[0]
    vis = np.zeros(N, dtype=bool)
    vis[start] = True
    path = [start]
    distance = 0
    local_min_distance = np.inf
    min_path = []

    while len(path) < N:
        local_min_distance = np.inf
        for i in range(N):
            if not vis[i] and MAP[path[-1], i] < local_min_distance:
                local_min_distance = MAP[path[-1], i]
                min_path = i
        path.append(min_path)
        distance += local_min_distance
        vis[min_path] = True

    return path, distance



if __name__ == '__main__':
    MAP = np.array([
        [0, 1, 2, 3],
        [1, 0, 4, 5],
        [2, 4, 0, 6],
        [3, 5, 6, 0]
    ])
    print(Greedy(MAP))