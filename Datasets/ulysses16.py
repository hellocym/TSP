import numpy as np


class ulysses16:
    def __init__(self, filepath):
        self.loadTSP(filepath)


    def loadTSP(self, filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('DIMENSION'):
                    self.N = int(line.split()[-1])
                    self.coords = np.zeros((self.N, 2))
                if line.startswith('EDGE_WEIGHT_SECTION'):
                    self.MAP = np.zeros((self.N, self.N))
                    for i in range(self.N):
                        for j in range(self.N):
                            self.MAP[i, j] = int(lines[i + 7].split()[j])
                    break
                if line.startswith('NODE_COORD_SECTION'):
                    self.MAP = np.zeros((self.N, self.N))
                    for i in range(self.N):
                        _, x, y = map(float, lines[i + 7].split())
                        self.coords[i] = np.array([x, y])


if __name__ == '__main__':
    dataset = ulysses16('Datasets/ulysses16.tsp')
    print(dataset.coords)