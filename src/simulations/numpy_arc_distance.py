'''
Created on Mar 19, 2012

@author: federicov
'''
from math import sin, cos, atan2, sqrt, pi
try:
    import numpy as np
    import numexpr as ne
    from numpy import arctan2 as arctan2
except ImportError:
    pass

def arc_distance_numpy(a, b):
    """
    Calculates the pairwise arc distance between all points in vector a and b.
    """
   
    if (len(a.shape) != 2) or (a.shape[1] != 2):
        raise ValueError('a should be Nx2')
    if (len(b.shape) != 2) or (b.shape[1] != 2):
        raise ValueError('b should be Nx2')
    #  Check for two dimensional arrays
       
    theta_1 = np.tile(a[:,0],(b.shape[0],1)).T
    phi_1 = np.tile(a[:,1],(b.shape[0],1)).T
   
    theta_2 = np.tile(b[:,0],(a.shape[0],1))
    phi_2 = np.tile(b[:,1],(a.shape[0],1))
   
    temp = np.sin((theta_2-theta_1)/2)**2+np.cos(theta_1)*np.cos(theta_2)*np.sin((phi_2-phi_1)/2)**2
    distance_matrix = 2 * (np.arctan2(np.sqrt(temp),np.sqrt(1-temp)))
   
    return distance_matrix

def arc_distance_broadcast_numpy(a,b):
    try:
        import numpypy as np
    except ImportError:
        import numpy as np
    theta_1 = a[:,0]
    phi_1 = a[:,1]
    
    theta_2 = b[:,0]
    phi_2 = b[:,1]
    temp = np.sin((theta_2-theta_1[:,np.newaxis])/2)**2
    temp = temp+np.cos(theta_1)[:,np.newaxis]*np.cos(theta_2).T*np.sin((phi_2-phi_1[:,np.newaxis])/2)**2
    distance_matrix = 2 * (np.arctan2(np.sqrt(temp),np.sqrt(1-temp)))
    
    return distance_matrix
def arc_distance_list(a, b):
    distance_matrix = []
    for theta_1, phi_1 in a:
        temp_matrix = []
        for theta_2, phi_2 in b:
            temp = sin((theta_2-theta_1)/2)**2+cos(theta_1)*cos(theta_2)*sin((phi_2-phi_1)/2)**2
            temp_matrix.append(2 * (atan2(sqrt(temp),sqrt(1-temp))))
        distance_matrix.append(temp_matrix)
        
    return distance_matrix

def arc_distance_numexpr(a, b):
    """
    Calculates the pairwise arc distance between all points in vector a and b.
    """
   
    if (len(a.shape) != 2) or (a.shape[1] != 2):
        raise ValueError('a should be Nx2')
    if (len(b.shape) != 2) or (b.shape[1] != 2):
        raise ValueError('b should be Nx2')
    #  Check for two dimensional arrays
       
    theta_1 = np.tile(a[:,0],(b.shape[0],1)).T
    phi_1 = np.tile(a[:,1],(b.shape[0],1)).T
   
    theta_2 = np.tile(b[:,0],(a.shape[0],1))
    phi_2 = np.tile(b[:,1],(a.shape[0],1))
   
    temp = ne.evaluate("sin((theta_2-theta_1)/2)**2+cos(theta_1)*cos(theta_2)*sin((phi_2-phi_1)/2)**2")
    distance_matrix = ne.evaluate("2 * (arctan2(sqrt(temp),sqrt(1-temp)))")
   
    return distance_matrix


def arc_distance_numba(theta_1, phi_1,
                       theta_2, phi_2):
    """
    Calculates the pairwise arc distance between all points in vector a and b.
    """
    temp = np.sin((theta_2-theta_1)/2)**2+np.cos(theta_1)*np.cos(theta_2)*np.sin((phi_2-phi_1)/2)**2
    distance_matrix = 2 * (arctan2(np.sqrt(temp),np.sqrt(1-temp)))
   
    return distance_matrix

def arc_distance_numpypy(a,b):
    """
    Not vectorized version using numpy pypy
    """
    try:
        import numpypy as np
        from numpypy import sin, cos, sqrt, arctan2
    except ImportError:
        import numpy as np
        from numpy import sin, cos, sqrt, arctan2
    distance_matrix = np.zeros((a.shape[0],
                                    b.shape[0]))
    for i in range(a.shape[0]):
        theta_1 = a[i][0]
        phi_1 = a[i][1]
        for j in range(b.shape[0]):
            theta_2 = b[j][0]
            phi_2 = b[j][1]
            temp = sin((theta_2-theta_1)/2)**2+cos(theta_1)*cos(theta_2)*sin((phi_2-phi_1)/2)**2
            distance_matrix[i,j] = (2 * (arctan2(sqrt(temp),sqrt(1-temp))))
        
    return distance_matrix