'''
Created on Mar 19, 2012

@author: federicov
'''

import random
from math import pi
from numpy_arc_distance import arc_distance_list, arc_distance_numpypy, arc_distance_broadcast_numpy
import timeit
try:
    import numpypy as np
except ImportError:
    import numpy as np
    
def assertAlmostEqual(a,b):
    assert (round(a-b, 7) == 0)

if __name__ == '__main__':
    a = []
    for I in range(1000):
        theta = random.random() * 2 * pi
        phi = random.random() * pi
        a.append((theta, phi))
    
    b = []
    for I in range(1000):
        theta = random.random() * 2 * pi
        phi = random.random() * pi
        b.append((theta, phi))
    
    t = timeit.Timer(lambda : arc_distance_list(a,b))
    print "List Implementation: %.5f " % (t.timeit(5))
    c = arc_distance_list(a,b)
   
    np_a = np.array(a, dtype = 'float')
    np_b = np.array(b, dtype = 'float')
    
    t = timeit.Timer(lambda : arc_distance_numpypy(np_a,np_b))
    print "Numpy Implementation: %.5f " % (t.timeit(5))
    np_c = arc_distance_numpypy(np_a,np_b)
    
    for i in range(np_c.shape[0]):
        for j in range(np_c.shape[1]):
            assertAlmostEqual(c[i][j],np_c[i,j])
            
    t = timeit.Timer(lambda : arc_distance_broadcast_numpy(np_a,np_b)[0,0])
    print "Numpy Broadcast Implementation: %.5f " % (t.timeit(5))
    np_c = arc_distance_broadcast_numpy(np_a,np_b)
            
    for i in range(np_c.shape[0]):
        for j in range(np_c.shape[1]):
            assertAlmostEqual(c[i][j],np_c[i,j])