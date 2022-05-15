''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: strain_rate.py                                      
 Description: This python module evaluates the rate of strain tensor along the 
 left and right wall surfaces for Re = 1000 and Re = 10000 unsteady flows. In particular, 
 the rate of strain tensor values are evaluated at each grid location along the respective
 surfaces for each timestep from the simulation. The maximum value and location 
 from each timestep are stored and will be used to generate a max strain rate vs.
 time plot and a location of max strain rate vs. time plot for each surface.''' 

# Import modules                                                 

import numpy as np

def get_strain_tensor(v_all_time_left_1, v_all_time_left_2, v_all_time_right_1, v_all_time_right_2,y, x_left_1, x_left_2,  x_right_1, x_right_2):
    
    ''' For each velocity distribution across left wall surface corresponding
    to individual array element in "v_all_time", evaluate rate of strain tensor
    of y component of velocity in y direction, and shear stress on the wall
    and store value and location of maximum rate of strain tensor and maximum
    shear stress properties for each time step'''
    
    # Initialize arrays to store value and location of each maximum strain rate tensor value
    
    e_y_mean_right_wall = np.transpose(np.array(np.zeros(len(v_all_time_right_1))))
    e_y_mean_left_wall = np.transpose(np.array(np.zeros(len(v_all_time_left_1))))
    
    h_left = np.abs(x_left_1[0] - x_left_2[0]) # Define uniform horizontal grid spacing for left surface
    h_right = np.abs(x_right_1[0] - x_right_2[0]) # Define uniform horizontal grid spacing for right surface
     
    for i in range(0, len(v_all_time_left_1)):
        
        e_y_left = np.transpose(np.array(np.zeros(len(v_all_time_left_1[i]))))
        e_y_right = np.transpose(np.array(np.zeros(len(v_all_time_right_1[i]))))
        
        for j in range(0, len(v_all_time_left_1[i])):
                
            ''' Using first-order backward difference method for rate of strain tensor
            on left wall '''
            
            e_y_left[j] = (v_all_time_left_2[i][j] - v_all_time_left_1[i][j]) / h_left
              
            
            ''' Using first-order forward difference method for rate of strain tensor 
            for right wall'''
        
        
            e_y_right[j] = (v_all_time_right_2[i][j] - v_all_time_right_1[i][j]) / h_right
            
            
            ''' When strain rate at last grid location is evaluated store location
            and value of maximum strain rate tensor for "ith" timestep '''
                
        
            if (j == len(v_all_time_left_1[i]) - 1):
                
                e_y_mean_left_wall[i] = np.mean(e_y_left)
                e_y_mean_right_wall[i] = np.mean(e_y_right)
                
                
                
    return e_y_mean_left_wall, e_y_mean_right_wall