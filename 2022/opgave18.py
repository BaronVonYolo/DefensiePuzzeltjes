import numpy as np
from matplotlib import pyplot as plt

base = [1, 2, 3, 4, 5, 6]
tolerance = 1

def fit(tuples):

    for i in range(0, 27):
        for j in range(0, 27):
            for k in range(0, 27):
                for l in range(0, 27):
                    # verify
                    count = 0
                    for x, y in tuples:
                        val = 0
                        val += l
                        val += i * np.cos(2*np.pi*x) 
                        val += j * np.cos(4*np.pi*x) 
                        val += k * np.cos(6*np.pi*x) 
                        if abs(val - y) > 1:
                            break
                        else:
                            count += 1
                    if count == len(tuples):
                        return (i, j, k, l)

i,j,k,l = fit([(0, 51), (0.5, -13), (3, -5)])
