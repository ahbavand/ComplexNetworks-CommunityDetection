from numpy import linalg as LA
import numpy as np

a = np.array([[3, -1, -1, 0, -1, 0], [-1, 2, -1, 0, 0, 0] , [-1, -1, 3, -1, 0, 0],[0, 0, -1, 3, -1, -1] , [-1, 0, 0, -1, 3, -1] , [0, 0, 0, -1, -1, 2]])


w, v = LA.eigh(a)

ind = w.real.argsort()[:3]
print(v)
