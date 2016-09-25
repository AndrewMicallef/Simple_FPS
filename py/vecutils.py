import numpy as np
import math

def length(vector):
	'''returns the length of a 3D vector'''
    return np.linalg.norm(vector)
	
def normalise(vector):
	'''returns the direction of a 3D vector'''
    if length(vector) != 0:
        return np.array(vector) / length(vector)
    else:
        return np.array((0,0,0))