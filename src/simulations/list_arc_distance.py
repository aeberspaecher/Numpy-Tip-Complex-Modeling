'''
Created on Mar 25, 2012

@author: federicov
'''
from math import sin, cos, atan2, sqrt, pi
from random import random

def arc_distance_list(a, b):
    distance_matrix = []
    for theta_1, phi_1 in a:
        temp_matrix = []
        for theta_2, phi_2 in b:
            temp = sin((theta_2 - theta_1) / 2) ** 2 + cos(theta_1) * cos(theta_2) * sin((phi_2 - phi_1) / 2) ** 2
            temp_matrix.append(2 * (atan2(sqrt(temp), sqrt(1 - temp))))
        distance_matrix.append(temp_matrix)
        
    return distance_matrix

if __name__ == '__main__':
    a = []
    for I in range(5):
        theta = random() * 2 * pi
        phi = random() * pi
        a.append((theta, phi))
    
    b = []
    for I in range(3):
        theta = random() * 2 * pi
        phi = random() * pi
        b.append((theta, phi))
    
    c = arc_distance_list(a, b)
