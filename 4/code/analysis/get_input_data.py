''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: get_input_data.py                                      
 Description: This python module is used to read in velocity field, solutions 
 and associated computational domain coordinate positions for both high and low 
 Re number simulations for the final project. These properties will be read in 
 as ".xy" files and converted to 2D numpy arrays for further manipulation '''

# Import modules                                                 

import numpy as np


def get_input_data(filename_1, filename_2, filename_3, filename_4, filename_5, filename_6):
    
    ''' Read in ".xy" files of velocity field solutions
    for a particular mesh configuration with fixed window size, wall thickness, 
    and Re number'''
    
    xy_object_1 = open(filename_1) 
    xy_object_2 = open(filename_2) 
    xy_object_3 = open(filename_3)
    xy_object_4 = open(filename_4) 
    xy_object_5 = open(filename_5) 
    xy_object_6 = open(filename_6)
    
    ''' Read object file of solutions for mesh configuration 
    into a 2D numpy array '''

    array_input_1 = np.loadtxt(xy_object_1)
    array_input_2 = np.loadtxt(xy_object_2)
    array_input_3 = np.loadtxt(xy_object_3)
    array_input_4 = np.loadtxt(xy_object_4)
    array_input_5 = np.loadtxt(xy_object_5)
    array_input_6 = np.loadtxt(xy_object_6)
  
    
    return array_input_1, array_input_2, array_input_3, array_input_4, array_input_5, array_input_6
