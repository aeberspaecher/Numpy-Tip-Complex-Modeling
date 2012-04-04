'''
Created on Mar 19, 2012

@author: federicov
'''

import random
import list_arc_distance # Shedskin compiled
import cython_arc_distance # Cython compiled
import numpy as np
import time
import timeit
from numba.translate import Translate
from math import pi
from numpy_arc_distance import \
(arc_distance_list, arc_distance_numpy, arc_distance_numexpr, arc_distance_numba,
arc_distance_broadcast_numpy)

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
    
    t = timeit.Timer(lambda : list_arc_distance.arc_distance_list(a,b))
    print "C-List Implementation: %.5f " % (t.timeit(5))
    c_shedskin = list_arc_distance.arc_distance_list(a,b)
   
    np_a = np.array(a, dtype = 'float')
    np_b = np.array(b, dtype = 'float')
    
    t = timeit.Timer(lambda : arc_distance_numpy(np_a,np_b))
    print "Numpy Implementation: %.5f " % (t.timeit(5))
    np_c = arc_distance_numpy(np_a,np_b)
    
    for i in range(np_c.shape[0]):
        for j in range(np_c.shape[1]):
            assertAlmostEqual(c[i][j],np_c[i,j])
            
    t = timeit.Timer(lambda : arc_distance_broadcast_numpy(np_a,np_b))
    print "Numpy Broadcast Implementation: %.5f " % (t.timeit(5))
    np_c = arc_distance_broadcast_numpy(np_a,np_b)

    for i in range(np_c.shape[0]):
        for j in range(np_c.shape[1]):
            assertAlmostEqual(c[i][j],np_c[i,j])
    
    t = timeit.Timer(lambda : cython_arc_distance.arc_distance(np_a, np_b))
    print "Cython Implementation: %.5f " % (t.timeit(5))
    cy_c = cython_arc_distance.arc_distance(np_a, np_b)

    # Fortran:
    t = timeit.Timer(lambda : f2py_arc_distance.arc_distance(np_a, np_b))
    print "Cython Implementation: %.5f " % (t.timeit(5))
    cy_c = cython_arc_distance.arc_distance(np_a, np_b)

    t = timeit.Timer(lambda : arc_distance_numexpr(np_a, np_b))
    print "Numexpr Implementation: %.5f " % (t.timeit(5))
    ne_c = arc_distance_numexpr(np_a, np_b)

    for i in range(np_c.shape[0]):
        for j in range(np_c.shape[1]):
            assertAlmostEqual(cy_c[i,j],np_c[i,j])

##   Doesn't work yet.         
    t = Translate(arc_distance_numba)
    numba_arc_distance = t.make_ufunc()
    x = time.time()
    
    for I in range(3):
        if (len(a.shape) != 2) or (a.shape[1] != 2):
            raise ValueError('a should be Nx2')
        if (len(b.shape) != 2) or (b.shape[1] != 2):
            raise ValueError('b should be Nx2')
        #  Check for two dimensional arrays
           
        theta_1 = np.tile(a[:,0],(b.shape[0],1)).T
        phi_1 = np.tile(a[:,1],(b.shape[0],1)).T
        theta_2 = np.tile(b[:,0],(a.shape[0],1))
        phi_2 = np.tile(b[:,1],(a.shape[0],1))
        
        nb_c = numba_arc_distance(theta_1, phi_1,
                                  theta_2, phi_2)
    print "Numba Implementation: %.5f " % (time.time() - x)
