import numpy as np
from Algorithms.BruteForce import BruteForce
from Algorithms.Greedy import Greedy
from Datasets.ulysses16 import ulysses16


class TSPSolver:
    def __init__(self):
        self.N = None
        self.path = []
        self.distance = 0
        self.MAP = None
        self.COORDS = None

    def getCoordsFromFile(self, problem):
        '''
        Read TSP problem from file.
        '''
        probs = {
            'ulysses16': ulysses16('Datasets/ulysses16.tsp')
        }
        dataset = probs[problem]
        self.COORDS = dataset.coords
        self.N = dataset.N
        self.MAP = self.setMapFromCoord(self.COORDS)

    def setMapFromDist(self, roads):
        m = np.zeros((self.N, self.N))
        for start, end, distance in roads:
            m[start, end] = distance
            m[end, start] = distance
        self.MAP = m

    def setMapFromCoord(self, coords):
        m = np.zeros((self.N, self.N))
        for i in range(self.N):
            for j in range(self.N):
                m[i, j] = np.linalg.norm(coords[i] - coords[j])
        self.MAP = m
        

    def solve(self, algorithm, start=0):
        algors = {
            'brute': BruteForce,
            'greedy': Greedy,
            # 'genetic': self.genetic
        }
        self.path, self.distance = algors[algorithm](self.MAP, start)
        return self.path, self.distance

    # def Visualize(self):
    #     v = createVisualizer()
    #     v.create()
    #     v.createNodes(self.N)
    #     v.animate(self.path)
    #     v.end()

    
if __name__ == '__main__':
    # MAP = np.array([
    #     [0, 1, 2, 3],
    #     [1, 0, 4, 5],
    #     [2, 4, 0, 6],
    #     [3, 5, 6, 0]
    # ])
    # solver = TSPSolver(4)
    # solver.MAP = MAP
    # solver.solve(algorithm='brute')
    # print(solver.path, solver.distance)

    solver = TSPSolver()
    solver.getCoordsFromFile(problem='ulysses16')
    print(solver.COORDS)