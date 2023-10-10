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
    min_distance = np.inf
    min_path = []

    for i in range(N):
        for j in range(N):
            if not vis[]