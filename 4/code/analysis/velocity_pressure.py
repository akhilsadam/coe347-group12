''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: velocity_pressure.py                                      
 Description: This python module serves as the main program for
 post-processing the velocity field data from each of the simulations
 of the low and high Re flows. In particular, the magnitude of the velocity along
 three sample lines in each flow field (two vertical lines that are flushed with the
 wall surfaces just upwards from cavity entrance, and vertical line that extends
 from top to bottom of cavity through x component of cavity centroid. '''            

# Import modules                                                 

from matplotlib import pyplot as plt
import get_input_data as gid
import os
import numpy as np

os.chdir('/Users/jcam98/Desktop/EducationInstitutions/UniversityofTexas/Courses/SPRING_2022/COE_347/Assignments/OpenFOAM/Projects/Final_Project/Team_12/Sim_Data/Low_Re')

''' Part 1: Read in xy files of velocity field, pressure field and
 associated line distances into 2D numpy arrays for steady flow with Re = 10 number sims '''


''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.05, and wall thickness of 0.1
into a 2D numpy array '''

B_U_10_005_01_1, B_P_10_005_01_1, C_U_10_005_01_1, C_P_10_005_01_1, E_U_10_005_01_1, E_P_10_005_01_1 = \
    gid.get_input_data("run_5_10_005_01/postProcessing/singleGraph/6/B_U.xy", "run_5_10_005_01/postProcessing/singleGraph/6/B_p.xy", "run_5_10_005_01/postProcessing/singleGraph/6/C_U.xy", "run_5_10_005_01/postProcessing/singleGraph/6/C_p.xy", "run_5_10_005_01/postProcessing/singleGraph/6/E_U.xy", "run_5_10_005_01/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_10_005_01_1 = B_U_10_005_01_1[:,1]
B_u_10_005_01_1 = B_U_10_005_01_1[:,3]
B_v_10_005_01_1 = B_U_10_005_01_1[:,4]
B_P_y_10_005_01_1 = B_P_10_005_01_1[:,1]
B_P_10_005_01_1 = B_P_10_005_01_1[:,3]
C_U_y_10_005_01_1 = C_U_10_005_01_1[:,1]
C_u_10_005_01_1 = C_U_10_005_01_1[:,3]
C_v_10_005_01_1 = C_U_10_005_01_1[:,4]
C_P_y_10_005_01_1 = C_P_10_005_01_1[:,1]
C_P_10_005_01_1 = C_P_10_005_01_1[:,3]
E_U_y_10_005_01_1 = E_U_10_005_01_1[:,1]
E_u_10_005_01_1 = E_U_10_005_01_1[:,3]
E_v_10_005_01_1 = E_U_10_005_01_1[:,4]
E_P_y_10_005_01_1 = E_P_10_005_01_1[:,1]
E_P_10_005_01_1 = E_P_10_005_01_1[:,3]


''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.05, and wall thickness of 0.1
into a 2D numpy array '''

B_U_10_005_01_2, B_P_10_005_01_2, C_U_10_005_01_2, C_P_10_005_01_2, E_U_10_005_01_2, E_P_10_005_01_2 = \
    gid.get_input_data("run_10_10_005_01/postProcessing/singleGraph/6/B_U.xy", "run_10_10_005_01/postProcessing/singleGraph/6/B_p.xy", "run_10_10_005_01/postProcessing/singleGraph/6/C_U.xy", "run_10_10_005_01/postProcessing/singleGraph/6/C_p.xy", "run_10_10_005_01/postProcessing/singleGraph/6/E_U.xy", "run_10_10_005_01/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_10_005_01_2 = B_U_10_005_01_2[:,1]
B_u_10_005_01_2 = B_U_10_005_01_2[:,3]
B_v_10_005_01_2 = B_U_10_005_01_2[:,4]
B_P_y_10_005_01_2 = B_P_10_005_01_2[:,1]
B_P_10_005_01_2 = B_P_10_005_01_2[:,3]
C_U_y_10_005_01_2 = C_U_10_005_01_2[:,1]
C_u_10_005_01_2 = C_U_10_005_01_2[:,3]
C_v_10_005_01_2 = C_U_10_005_01_2[:,4]
C_P_y_10_005_01_2 = C_P_10_005_01_2[:,1]
C_P_10_005_01_2 = C_P_10_005_01_2[:,3]
E_U_y_10_005_01_2 = E_U_10_005_01_2[:,1]
E_u_10_005_01_2 = E_U_10_005_01_2[:,3]
E_v_10_005_01_2 = E_U_10_005_01_2[:,4]
E_P_y_10_005_01_2 = E_P_10_005_01_2[:,1]
E_P_10_005_01_2 = E_P_10_005_01_2[:,3]


''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.05, and wall thickness of 0.05
into a 2D numpy array '''

B_U_10_005_005_1, B_P_10_005_005_1, C_U_10_005_005_1, C_P_10_005_005_1, E_U_10_005_005_1, E_P_10_005_005_1 = \
    gid.get_input_data("run_5_10_005_005/postProcessing/singleGraph/6/B_U.xy", "run_5_10_005_005/postProcessing/singleGraph/6/B_p.xy", "run_5_10_005_005/postProcessing/singleGraph/6/C_U.xy", "run_5_10_005_005/postProcessing/singleGraph/6/C_p.xy", "run_5_10_005_005/postProcessing/singleGraph/6/E_U.xy", "run_5_10_005_005/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_10_005_005_1 = B_U_10_005_005_1[:,1]
B_u_10_005_005_1 = B_U_10_005_005_1[:,3]
B_v_10_005_005_1 = B_U_10_005_005_1[:,4]
B_P_y_10_005_005_1 = B_P_10_005_005_1[:,1]
B_P_10_005_005_1 = B_P_10_005_005_1[:,3]
C_U_y_10_005_005_1 = C_U_10_005_005_1[:,1]
C_u_10_005_005_1 = C_U_10_005_005_1[:,3]
C_v_10_005_005_1 = C_U_10_005_005_1[:,4]
C_P_y_10_005_005_1 = C_P_10_005_005_1[:,1]
C_P_10_005_005_1 = C_P_10_005_005_1[:,3]
E_U_y_10_005_005_1 = E_U_10_005_005_1[:,1]
E_u_10_005_005_1 = E_U_10_005_005_1[:,3]
E_v_10_005_005_1 = E_U_10_005_005_1[:,4]
E_P_y_10_005_005_1 = E_P_10_005_005_1[:,1]
E_P_10_005_005_1 = E_P_10_005_005_1[:,3]


''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.05, and wall thickness of 0.05
into a 2D numpy array '''

B_U_10_005_005_2, B_P_10_005_005_2, C_U_10_005_005_2, C_P_10_005_005_2, E_U_10_005_005_2, E_P_10_005_005_2 = \
    gid.get_input_data("run_10_10_005_005/postProcessing/singleGraph/6/B_U.xy", "run_10_10_005_005/postProcessing/singleGraph/6/B_p.xy", "run_10_10_005_005/postProcessing/singleGraph/6/C_U.xy", "run_10_10_005_005/postProcessing/singleGraph/6/C_p.xy", "run_10_10_005_005/postProcessing/singleGraph/6/E_U.xy", "run_10_10_005_005/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_10_005_005_2 = B_U_10_005_005_2[:,1]
B_u_10_005_005_2 = B_U_10_005_005_2[:,3]
B_v_10_005_005_2 = B_U_10_005_005_2[:,4]
B_P_y_10_005_005_2 = B_P_10_005_005_2[:,1]
B_P_10_005_005_2 = B_P_10_005_005_2[:,3]
C_U_y_10_005_005_2 = C_U_10_005_005_2[:,1]
C_u_10_005_005_2 = C_U_10_005_005_2[:,3]
C_v_10_005_005_2 = C_U_10_005_005_2[:,4]
C_P_y_10_005_005_2 = C_P_10_005_005_2[:,1]
C_P_10_005_005_2 = C_P_10_005_005_2[:,3]
E_U_y_10_005_005_2 = E_U_10_005_005_2[:,1]
E_u_10_005_005_2 = E_U_10_005_005_2[:,3]
E_v_10_005_005_2 = E_U_10_005_005_2[:,4]
E_P_y_10_005_005_2 = E_P_10_005_005_2[:,1]
E_P_10_005_005_2 = E_P_10_005_005_2[:,3]


''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.50, and wall thickness of 0.05
into a 2D numpy array '''

B_U_10_050_005_1, B_P_10_050_005_1, C_U_10_050_005_1, C_P_10_050_005_1, E_U_10_050_005_1, E_P_10_050_005_1 = \
    gid.get_input_data("run_5_10_050_005/postProcessing/singleGraph/6/B_U.xy", "run_5_10_050_005/postProcessing/singleGraph/6/B_p.xy", "run_5_10_050_005/postProcessing/singleGraph/6/C_U.xy", "run_5_10_050_005/postProcessing/singleGraph/6/C_p.xy", "run_5_10_050_005/postProcessing/singleGraph/6/E_U.xy", "run_5_10_050_005/postProcessing/singleGraph/6/E_p.xy" )


B_U_y_10_050_005_1 = B_U_10_050_005_1[:,1]
B_u_10_050_005_1 = B_U_10_050_005_1[:,3]
B_v_10_050_005_1 = B_U_10_050_005_1[:,4]
B_P_y_10_050_005_1 = B_P_10_050_005_1[:,1]
B_P_10_050_005_1 = B_P_10_050_005_1[:,3]
C_U_y_10_050_005_1 = C_U_10_050_005_1[:,1]
C_u_10_050_005_1 = C_U_10_050_005_1[:,3]
C_v_10_050_005_1 = C_U_10_050_005_1[:,4]
C_P_y_10_050_005_1 = C_P_10_050_005_1[:,1]
C_P_10_050_005_1 = C_P_10_050_005_1[:,3]
E_U_y_10_050_005_1 = E_U_10_050_005_1[:,1]
E_u_10_050_005_1 = E_U_10_050_005_1[:,3]
E_v_10_050_005_1 = E_U_10_050_005_1[:,4]
E_P_y_10_050_005_1 = E_P_10_050_005_1[:,1]
E_P_10_050_005_1 = E_P_10_050_005_1[:,3]


''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.50, and wall thickness of 0.05
into a 2D numpy array '''

B_U_10_050_005_2, B_P_10_050_005_2, C_U_10_050_005_2, C_P_10_050_005_2, E_U_10_050_005_2, E_P_10_050_005_2 = \
    gid.get_input_data("run_10_10_050_005/postProcessing/singleGraph/6/B_U.xy", "run_10_10_050_005/postProcessing/singleGraph/6/B_p.xy", "run_10_10_050_005/postProcessing/singleGraph/6/C_U.xy", "run_10_10_050_005/postProcessing/singleGraph/6/C_p.xy", "run_10_10_050_005/postProcessing/singleGraph/6/E_U.xy", "run_10_10_050_005/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_10_050_005_2 = B_U_10_050_005_2[:,1]
B_u_10_050_005_2 = B_U_10_050_005_2[:,3]
B_v_10_050_005_2 = B_U_10_050_005_2[:,4]
B_P_y_10_050_005_2 = B_P_10_050_005_2[:,1]
B_P_10_050_005_2 = B_P_10_050_005_2[:,3]
C_U_y_10_050_005_2 = C_U_10_050_005_2[:,1]
C_u_10_050_005_2 = C_U_10_050_005_2[:,3]
C_v_10_050_005_2 = C_U_10_050_005_2[:,4]
C_P_y_10_050_005_2 = C_P_10_050_005_2[:,1]
C_P_10_050_005_2 = C_P_10_050_005_2[:,3]
E_U_y_10_050_005_2 = E_U_10_050_005_2[:,1]
E_u_10_050_005_2 = E_U_10_050_005_2[:,3]
E_v_10_050_005_2 = E_U_10_050_005_2[:,4]
E_P_y_10_050_005_2 = E_P_10_050_005_2[:,1]
E_P_10_050_005_2 = E_P_10_050_005_2[:,3]


''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.50, and wall thickness of 0.1
into a 2D numpy array '''

B_U_10_050_01_1, B_P_10_050_01_1, C_U_10_050_01_1, C_P_10_050_01_1, E_U_10_050_01_1, E_P_10_050_01_1 = \
    gid.get_input_data("run_5_10_050_01/postProcessing/singleGraph/6/B_U.xy", "run_5_10_050_01/postProcessing/singleGraph/6/B_p.xy", "run_5_10_050_01/postProcessing/singleGraph/6/C_U.xy", "run_5_10_050_01/postProcessing/singleGraph/6/C_p.xy", "run_5_10_050_01/postProcessing/singleGraph/6/E_U.xy", "run_5_10_050_01/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_10_050_01_1 = B_U_10_050_01_1[:,1]
B_u_10_050_01_1 = B_U_10_050_01_1[:,3]
B_v_10_050_01_1 = B_U_10_050_01_1[:,4]
B_P_y_10_050_01_1 = B_P_10_050_01_1[:,1]
B_P_10_050_01_1 = B_P_10_050_01_1[:,3]
C_U_y_10_050_01_1 = C_U_10_050_01_1[:,1]
C_u_10_050_01_1 = C_U_10_050_01_1[:,3]
C_v_10_050_01_1 = C_U_10_050_01_1[:,4]
C_P_y_10_050_01_1 = C_P_10_050_01_1[:,1]
C_P_10_050_01_1 = C_P_10_050_01_1[:,3]
E_U_y_10_050_01_1 = E_U_10_050_01_1[:,1]
E_u_10_050_01_1 = E_U_10_050_01_1[:,3]
E_v_10_050_01_1 = E_U_10_050_01_1[:,4]
E_P_y_10_050_01_1 = E_P_10_050_01_1[:,1]
E_P_10_050_01_1 = E_P_10_050_01_1[:,3]


''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.50, and wall thickness of 0.1
into a 2D numpy array '''

B_U_10_050_01_2, B_P_10_050_01_2, C_U_10_050_01_2, C_P_10_050_01_2, E_U_10_050_01_2, E_P_10_050_01_2 = \
    gid.get_input_data("run_10_10_050_01/postProcessing/singleGraph/6/B_U.xy", "run_10_10_050_01/postProcessing/singleGraph/6/B_p.xy", "run_10_10_050_01/postProcessing/singleGraph/6/C_U.xy", "run_10_10_050_01/postProcessing/singleGraph/6/C_p.xy", "run_10_10_050_01/postProcessing/singleGraph/6/E_U.xy", "run_10_10_050_01/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_10_050_01_2 = B_U_10_050_01_2[:,1]
B_u_10_050_01_2 = B_U_10_050_01_2[:,3]
B_v_10_050_01_2 = B_U_10_050_01_2[:,4]
B_P_y_10_050_01_2 = B_P_10_050_01_2[:,1]
B_P_10_050_01_2 = B_P_10_050_01_2[:,3]
C_U_y_10_050_01_2 = C_U_10_050_01_2[:,1]
C_u_10_050_01_2 = C_U_10_050_01_2[:,3]
C_v_10_050_01_2 = C_U_10_050_01_2[:,4]
C_P_y_10_050_01_2 = C_P_10_050_01_2[:,1]
C_P_10_050_01_2 = C_P_10_050_01_2[:,3]
E_U_y_10_050_01_2 = E_U_10_050_01_2[:,1]
E_u_10_050_01_2 = E_U_10_050_01_2[:,3]
E_v_10_050_01_2 = E_U_10_050_01_2[:,4]
E_P_y_10_050_01_2 = E_P_10_050_01_2[:,1]
E_P_10_050_01_2 = E_P_10_050_01_2[:,3]



''' Part 2: Read in xy files of velocity field, pressure field and
 associated line distances into 2D numpy arrays for steady flow with Re = 200 number sims '''


''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.05, and wall thickness of 0.1
into a 2D numpy array '''

B_U_200_005_01_1, B_P_200_005_01_1, C_U_200_005_01_1, C_P_200_005_01_1, E_U_200_005_01_1, E_P_200_005_01_1 = \
    gid.get_input_data("run_5_200_005_01/postProcessing/singleGraph/6/B_U.xy", "run_5_200_005_01/postProcessing/singleGraph/6/B_p.xy", "run_5_200_005_01/postProcessing/singleGraph/6/C_U.xy", "run_5_200_005_01/postProcessing/singleGraph/6/C_p.xy", "run_5_200_005_01/postProcessing/singleGraph/6/E_U.xy", "run_5_200_005_01/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_200_005_01_1 = B_U_200_005_01_1[:,1]
B_u_200_005_01_1 = B_U_200_005_01_1[:,3]
B_v_200_005_01_1 = B_U_200_005_01_1[:,4]
B_P_y_200_005_01_1 = B_P_200_005_01_1[:,1]
B_P_200_005_01_1 = B_P_200_005_01_1[:,3]
C_U_y_200_005_01_1 = C_U_200_005_01_1[:,1]
C_u_200_005_01_1 = C_U_200_005_01_1[:,3]
C_v_200_005_01_1 = C_U_200_005_01_1[:,4]
C_P_y_200_005_01_1 = C_P_200_005_01_1[:,1]
C_P_200_005_01_1 = C_P_200_005_01_1[:,3]
E_U_y_200_005_01_1 = E_U_200_005_01_1[:,1]
E_u_200_005_01_1 = E_U_200_005_01_1[:,3]
E_v_200_005_01_1 = E_U_200_005_01_1[:,4]
E_P_y_200_005_01_1 = E_P_200_005_01_1[:,1]
E_P_200_005_01_1 = E_P_200_005_01_1[:,3]


''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.05, and wall thickness of 0.1
into a 2D numpy array '''

B_U_200_005_01_2, B_P_200_005_01_2, C_U_200_005_01_2, C_P_200_005_01_2, E_U_200_005_01_2, E_P_200_005_01_2 = \
    gid.get_input_data("run_10_200_005_01/postProcessing/singleGraph/6/B_U.xy", "run_10_200_005_01/postProcessing/singleGraph/6/B_p.xy", "run_10_200_005_01/postProcessing/singleGraph/6/C_U.xy", "run_10_200_005_01/postProcessing/singleGraph/6/C_p.xy", "run_10_200_005_01/postProcessing/singleGraph/6/E_U.xy", "run_10_200_005_01/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_200_005_01_2 = B_U_200_005_01_2[:,1]
B_u_200_005_01_2 = B_U_200_005_01_2[:,3]
B_v_200_005_01_2 = B_U_200_005_01_2[:,4]
B_P_y_200_005_01_2 = B_P_200_005_01_2[:,1]
B_P_200_005_01_2 = B_P_200_005_01_2[:,3]
C_U_y_200_005_01_2 = C_U_200_005_01_2[:,1]
C_u_200_005_01_2 = C_U_200_005_01_2[:,3]
C_v_200_005_01_2 = C_U_200_005_01_2[:,4]
C_P_y_200_005_01_2 = C_P_200_005_01_2[:,1]
C_P_200_005_01_2 = C_P_200_005_01_2[:,3]
E_U_y_200_005_01_2 = E_U_200_005_01_2[:,1]
E_u_200_005_01_2 = E_U_200_005_01_2[:,3]
E_v_200_005_01_2 = E_U_200_005_01_2[:,4]
E_P_y_200_005_01_2 = E_P_200_005_01_2[:,1]
E_P_200_005_01_2 = E_P_200_005_01_2[:,3]


''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.05, and wall thickness of 0.05
into a 2D numpy array '''

B_U_200_005_005_1, B_P_200_005_005_1, C_U_200_005_005_1, C_P_200_005_005_1, E_U_200_005_005_1, E_P_200_005_005_1 = \
    gid.get_input_data("run_5_200_005_005/postProcessing/singleGraph/6/B_U.xy", "run_5_200_005_005/postProcessing/singleGraph/6/B_p.xy", "run_5_200_005_005/postProcessing/singleGraph/6/C_U.xy", "run_5_200_005_005/postProcessing/singleGraph/6/C_p.xy", "run_5_200_005_005/postProcessing/singleGraph/6/E_U.xy", "run_5_200_005_005/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_200_005_005_1 = B_U_200_005_005_1[:,1]
B_u_200_005_005_1 = B_U_200_005_005_1[:,3]
B_v_200_005_005_1 = B_U_200_005_005_1[:,4]
B_P_y_200_005_005_1 = B_P_200_005_005_1[:,1]
B_P_200_005_005_1 = B_P_200_005_005_1[:,3]
C_U_y_200_005_005_1 = C_U_200_005_005_1[:,1]
C_u_200_005_005_1 = C_U_200_005_005_1[:,3]
C_v_200_005_005_1 = C_U_200_005_005_1[:,4]
C_P_y_200_005_005_1 = C_P_200_005_005_1[:,1]
C_P_200_005_005_1 = C_P_200_005_005_1[:,3]
E_U_y_200_005_005_1 = E_U_200_005_005_1[:,1]
E_u_200_005_005_1 = E_U_200_005_005_1[:,3]
E_v_200_005_005_1 = E_U_200_005_005_1[:,4]
E_P_y_200_005_005_1 = E_P_200_005_005_1[:,1]
E_P_200_005_005_1 = E_P_200_005_005_1[:,3]


''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.05, and wall thickness of 0.05
into a 2D numpy array '''

B_U_200_005_005_2, B_P_200_005_005_2, C_U_200_005_005_2, C_P_200_005_005_2, E_U_200_005_005_2, E_P_200_005_005_2 = \
    gid.get_input_data("run_10_200_005_005/postProcessing/singleGraph/6/B_U.xy", "run_10_200_005_005/postProcessing/singleGraph/6/B_p.xy", "run_10_200_005_005/postProcessing/singleGraph/6/C_U.xy", "run_10_200_005_005/postProcessing/singleGraph/6/C_p.xy", "run_10_200_005_005/postProcessing/singleGraph/6/E_U.xy", "run_10_200_005_005/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_200_005_005_2 = B_U_200_005_005_2[:,1]
B_u_200_005_005_2 = B_U_200_005_005_2[:,3]
B_v_200_005_005_2 = B_U_200_005_005_2[:,4]
B_P_y_200_005_005_2 = B_P_200_005_005_2[:,1]
B_P_200_005_005_2 = B_P_200_005_005_2[:,3]
C_U_y_200_005_005_2 = C_U_200_005_005_2[:,1]
C_u_200_005_005_2 = C_U_200_005_005_2[:,3]
C_v_200_005_005_2 = C_U_200_005_005_2[:,4]
C_P_y_200_005_005_2 = C_P_200_005_005_2[:,1]
C_P_200_005_005_2 = C_P_200_005_005_2[:,3]
E_U_y_200_005_005_2 = E_U_200_005_005_2[:,1]
E_u_200_005_005_2 = E_U_200_005_005_2[:,3]
E_v_200_005_005_2 = E_U_200_005_005_2[:,4]
E_P_y_200_005_005_2 = E_P_200_005_005_2[:,1]
E_P_200_005_005_2 = E_P_200_005_005_2[:,3]


''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.50, and wall thickness of 0.05
into a 2D numpy array '''

B_U_200_050_005_1, B_P_200_050_005_1, C_U_200_050_005_1, C_P_200_050_005_1, E_U_200_050_005_1, E_P_200_050_005_1 = \
    gid.get_input_data("run_5_200_050_005/postProcessing/singleGraph/6/B_U.xy", "run_5_200_050_005/postProcessing/singleGraph/6/B_p.xy", "run_5_200_050_005/postProcessing/singleGraph/6/C_U.xy", "run_5_200_050_005/postProcessing/singleGraph/6/C_p.xy", "run_5_200_050_005/postProcessing/singleGraph/6/E_U.xy", "run_5_200_050_005/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_200_050_005_1 = B_U_200_050_005_1[:,1]
B_u_200_050_005_1 = B_U_200_050_005_1[:,3]
B_v_200_050_005_1 = B_U_200_050_005_1[:,4]
B_P_y_200_050_005_1 = B_P_200_050_005_1[:,1]
B_P_200_050_005_1 = B_P_200_050_005_1[:,3]
C_U_y_200_050_005_1 = C_U_200_050_005_1[:,1]
C_u_200_050_005_1 = C_U_200_050_005_1[:,3]
C_v_200_050_005_1 = C_U_200_050_005_1[:,4]
C_P_y_200_050_005_1 = C_P_200_050_005_1[:,1]
C_P_200_050_005_1 = C_P_200_050_005_1[:,3]
E_U_y_200_050_005_1 = E_U_200_050_005_1[:,1]
E_u_200_050_005_1 = E_U_200_050_005_1[:,3]
E_v_200_050_005_1 = E_U_200_050_005_1[:,4]
E_P_y_200_050_005_1 = E_P_200_050_005_1[:,1]
E_P_200_050_005_1 = E_P_200_050_005_1[:,3]

''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.50, and wall thickness of 0.05
into a 2D numpy array '''

B_U_200_050_005_2, B_P_200_050_005_2, C_U_200_050_005_2, C_P_200_050_005_2, E_U_200_050_005_2, E_P_200_050_005_2 = \
    gid.get_input_data("run_10_200_050_005/postProcessing/singleGraph/6/B_U.xy", "run_10_200_050_005/postProcessing/singleGraph/6/B_p.xy", "run_10_200_050_005/postProcessing/singleGraph/6/C_U.xy", "run_10_200_050_005/postProcessing/singleGraph/6/C_p.xy", "run_10_200_050_005/postProcessing/singleGraph/6/E_U.xy", "run_10_200_050_005/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_200_050_005_2 = B_U_200_050_005_2[:,1]
B_u_200_050_005_2 = B_U_200_050_005_2[:,3]
B_v_200_050_005_2 = B_U_200_050_005_2[:,4]
B_P_y_200_050_005_2 = B_P_200_050_005_2[:,1]
B_P_200_050_005_2 = B_P_200_050_005_2[:,3]
C_U_y_200_050_005_2 = C_U_200_050_005_2[:,1]
C_u_200_050_005_2 = C_U_200_050_005_2[:,3]
C_v_200_050_005_2 = C_U_200_050_005_2[:,4]
C_P_y_200_050_005_2 = C_P_200_050_005_2[:,1]
C_P_200_050_005_2 = C_P_200_050_005_2[:,3]
E_U_y_200_050_005_2 = E_U_200_050_005_2[:,1]
E_u_200_050_005_2 = E_U_200_050_005_2[:,3]
E_v_200_050_005_2 = E_U_200_050_005_2[:,4]
E_P_y_200_050_005_2 = E_P_200_050_005_2[:,1]
E_P_200_050_005_2 = E_P_200_050_005_2[:,3]

''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.50, and wall thickness of 0.1
into a 2D numpy array '''

B_U_200_050_01_1, B_P_200_050_01_1, C_U_200_050_01_1, C_P_200_050_01_1, E_U_200_050_01_1, E_P_200_050_01_1 = \
    gid.get_input_data("run_5_200_050_01/postProcessing/singleGraph/6/B_U.xy", "run_5_200_050_01/postProcessing/singleGraph/6/B_p.xy", "run_5_200_050_01/postProcessing/singleGraph/6/C_U.xy", "run_5_200_050_01/postProcessing/singleGraph/6/C_p.xy", "run_5_200_050_01/postProcessing/singleGraph/6/E_U.xy", "run_5_200_050_01/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_200_050_01_1 = B_U_200_050_01_1[:,1]
B_u_200_050_01_1 = B_U_200_050_01_1[:,3]
B_v_200_050_01_1 = B_U_200_050_01_1[:,4]
B_P_y_200_050_01_1 = B_P_200_050_01_1[:,1]
B_P_200_050_01_1 = B_P_200_050_01_1[:,3]
C_U_y_200_050_01_1 = C_U_200_050_01_1[:,1]
C_u_200_050_01_1 = C_U_200_050_01_1[:,3]
C_v_200_050_01_1 = C_U_200_050_01_1[:,4]
C_P_y_200_050_01_1 = C_P_200_050_01_1[:,1]
C_P_200_050_01_1 = C_P_200_050_01_1[:,3]
E_U_y_200_050_01_1 = E_U_200_050_01_1[:,1]
E_u_200_050_01_1 = E_U_200_050_01_1[:,3]
E_v_200_050_01_1 = E_U_200_050_01_1[:,4]
E_P_y_200_050_01_1 = E_P_200_050_01_1[:,1]
E_P_200_050_01_1 = E_P_200_050_01_1[:,3]

''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.50, and wall thickness of 0.1
into a 2D numpy array '''

B_U_200_050_01_2, B_P_200_050_01_2, C_U_200_050_01_2, C_P_200_050_01_2, E_U_200_050_01_2, E_P_200_050_01_2 = \
    gid.get_input_data("run_10_200_050_01/postProcessing/singleGraph/6/B_U.xy", "run_10_200_050_01/postProcessing/singleGraph/6/B_p.xy", "run_10_200_050_01/postProcessing/singleGraph/6/C_U.xy", "run_10_200_050_01/postProcessing/singleGraph/6/C_p.xy", "run_10_200_050_01/postProcessing/singleGraph/6/E_U.xy", "run_10_200_050_01/postProcessing/singleGraph/6/E_p.xy" )

B_U_y_200_050_01_2 = B_U_200_050_01_2[:,1]
B_u_200_050_01_2 = B_U_200_050_01_2[:,3]
B_v_200_050_01_2 = B_U_200_050_01_2[:,4]
B_P_y_200_050_01_2 = B_P_200_050_01_2[:,1]
B_P_200_050_01_2 = B_P_200_050_01_2[:,3]
C_U_y_200_050_01_2 = C_U_200_050_01_2[:,1]
C_u_200_050_01_2 = C_U_200_050_01_2[:,3]
C_v_200_050_01_2 = C_U_200_050_01_2[:,4]
C_P_y_200_050_01_2 = C_P_200_050_01_2[:,1]
C_P_200_050_01_2 = C_P_200_050_01_2[:,3]
E_U_y_200_050_01_2 = E_U_200_050_01_2[:,1]
E_u_200_050_01_2 = E_U_200_050_01_2[:,3]
E_v_200_050_01_2 = E_U_200_050_01_2[:,4]
E_P_y_200_050_01_2 = E_P_200_050_01_2[:,1]
E_P_200_050_01_2 = E_P_200_050_01_2[:,3]

''' Part 3: Read in xy files of velocity field, pressure field and
 associated line distances into 2D numpy arrays for unsteady flow with Re = 1000 number sims '''

os.chdir('/Users/jcam98/Desktop/EducationInstitutions/UniversityofTexas/Courses/SPRING_2022/COE_347/Assignments/OpenFOAM/Projects/Final_Project/Team_12/Sim_Data/High_Re')

''' Read in "xy" files of properties for simulation with first mesh refinement, 
window size of 0.50, and wall thickness of 0.1 at time step "t ~= 1.3s" corresponding 
to timestep directly preceding the time with the highest vortex shedding frequency
and thus likely the most interesting velocity/pressure distributions into a 2D numpy array '''

B_U_1000_050_01_1, B_P_1000_050_01_1, C_U_1000_050_01_1, C_P_1000_050_01_1, E_U_1000_050_01_1, E_P_1000_050_01_1 = \
    gid.get_input_data("run_3_1000_050_01/postProcessing/singleGraph/1.3013333/B_U.xy", "run_3_1000_050_01/postProcessing/singleGraph/1.3013333/B_p.xy", "run_3_1000_050_01/postProcessing/singleGraph/1.3013333/C_U.xy", "run_3_1000_050_01/postProcessing/singleGraph/1.3013333/C_p.xy", "run_3_1000_050_01/postProcessing/singleGraph/1.3013333/E_U.xy", "run_3_1000_050_01/postProcessing/singleGraph/1.3013333/E_p.xy" )

B_U_y_1000_050_01_1 = B_U_1000_050_01_1[:,1]
B_u_1000_050_01_1 = B_U_1000_050_01_1[:,3]
B_v_1000_050_01_1 = B_U_1000_050_01_1[:,4]
B_P_y_1000_050_01_1 = B_P_1000_050_01_1[:,1]
B_P_1000_050_01_1 = B_P_1000_050_01_1[:,3]
C_U_y_1000_050_01_1 = C_U_1000_050_01_1[:,1]
C_u_1000_050_01_1 = C_U_1000_050_01_1[:,3]
C_v_1000_050_01_1 = C_U_1000_050_01_1[:,4]
C_P_y_1000_050_01_1 = C_P_1000_050_01_1[:,1]
C_P_1000_050_01_1 = C_P_1000_050_01_1[:,3]
E_U_y_1000_050_01_1 = E_U_1000_050_01_1[:,1]
E_u_1000_050_01_1 = E_U_1000_050_01_1[:,3]
E_v_1000_050_01_1 = E_U_1000_050_01_1[:,4]
E_P_y_1000_050_01_1 = E_P_1000_050_01_1[:,1]
E_P_1000_050_01_1 = E_P_1000_050_01_1[:,3]

''' Read in "xy" files of properties for simulation with second mesh refinement, 
window size of 0.50, and wall thickness of 0.1 at time step "t = 1.3s" corresponding 
to timestep directly preceding the time with the highest vortex shedding frequency
and thus likely the most interesting velocity/pressure distributions into a 2D numpy array '''

B_U_1000_050_01_2, B_P_1000_050_01_2, C_U_1000_050_01_2, C_P_1000_050_01_2, E_U_1000_050_01_2, E_P_1000_050_01_2 = \
    gid.get_input_data("run_5_1000_050_01/postProcessing/singleGraph/1.2992/B_U.xy", "run_5_1000_050_01/postProcessing/singleGraph/1.2992/B_p.xy", "run_5_1000_050_01/postProcessing/singleGraph/1.2992/C_U.xy", "run_5_1000_050_01/postProcessing/singleGraph/1.2992/C_p.xy", "run_5_1000_050_01/postProcessing/singleGraph/1.2992/E_U.xy", "run_5_1000_050_01/postProcessing/singleGraph/1.2992/E_p.xy" )

B_U_y_1000_050_01_2 = B_U_1000_050_01_2[:,1]
B_u_1000_050_01_2 = B_U_1000_050_01_2[:,3]
B_v_1000_050_01_2 = B_U_1000_050_01_2[:,4]
B_P_y_1000_050_01_2 = B_P_1000_050_01_2[:,1]
B_P_1000_050_01_2 = B_P_1000_050_01_2[:,3]
C_U_y_1000_050_01_2 = C_U_1000_050_01_2[:,1]
C_u_1000_050_01_2 = C_U_1000_050_01_2[:,3]
C_v_1000_050_01_2 = C_U_1000_050_01_2[:,4]
C_P_y_1000_050_01_2 = C_P_1000_050_01_2[:,1]
C_P_1000_050_01_2 = C_P_1000_050_01_2[:,3]
E_U_y_1000_050_01_2 = E_U_1000_050_01_2[:,1]
E_u_1000_050_01_2 = E_U_1000_050_01_2[:,3]
E_v_1000_050_01_2 = E_U_1000_050_01_2[:,4]
E_P_y_1000_050_01_2 = E_P_1000_050_01_2[:,1]
E_P_1000_050_01_2 = E_P_1000_050_01_2[:,3]

''' Part 4: Read in xy files of velocity field, pressure field and
 associated line distances into 2D numpy arrays for unsteady flow with Re = 10000 number sims '''

''' Read in "xy" files of properties for simulation with first mesh refinement, 
window size of 0.50, and wall thickness of 0.1 at time step "t = 1.3s" corresponding 
to timestep directly preceding the time with the highest vortex shedding frequency
and thus likely the most interesting velocity/pressure distributions into a 2D numpy array '''

B_U_10000_050_01_1, B_P_10000_050_01_1, C_U_10000_050_01_1, C_P_10000_050_01_1, E_U_10000_050_01_1, E_P_10000_050_01_1 = \
    gid.get_input_data("run_3_10000_050_01/postProcessing/singleGraph/1.3013333/B_U.xy", "run_3_10000_050_01/postProcessing/singleGraph/1.3013333/B_p.xy", "run_3_10000_050_01/postProcessing/singleGraph/1.3013333/C_U.xy", "run_3_10000_050_01/postProcessing/singleGraph/1.3013333/C_p.xy", "run_3_10000_050_01/postProcessing/singleGraph/1.3013333/E_U.xy", "run_3_10000_050_01/postProcessing/singleGraph/1.3013333/E_p.xy" )

B_U_y_10000_050_01_1 = B_U_10000_050_01_1[:,1]
B_u_10000_050_01_1 = B_U_10000_050_01_1[:,3]
B_v_10000_050_01_1 = B_U_10000_050_01_1[:,4]
B_P_y_10000_050_01_1 = B_P_10000_050_01_1[:,1]
B_P_10000_050_01_1 = B_P_10000_050_01_1[:,3]
C_U_y_10000_050_01_1 = C_U_10000_050_01_1[:,1]
C_u_10000_050_01_1 = C_U_10000_050_01_1[:,3]
C_v_10000_050_01_1 = C_U_10000_050_01_1[:,4]
C_P_y_10000_050_01_1 = C_P_10000_050_01_1[:,1]
C_P_10000_050_01_1 = C_P_10000_050_01_1[:,3]
E_U_y_10000_050_01_1 = E_U_10000_050_01_1[:,1]
E_u_10000_050_01_1 = E_U_10000_050_01_1[:,3]
E_v_10000_050_01_1 = E_U_10000_050_01_1[:,4]
E_P_y_10000_050_01_1 = E_P_10000_050_01_1[:,1]
E_P_10000_050_01_1 = E_P_10000_050_01_1[:,3]

''' Read in "xy" files of properties for simulation with second mesh refinement, 
window size of 0.50, and wall thickness of 0.1 at time step "t = 1.3s" corresponding 
to timestep directly preceding the time with the highest vortex shedding frequency
and thus likely the most interesting velocity/pressure distributions into a 2D numpy array '''

B_U_10000_050_01_2, B_P_10000_050_01_2, C_U_10000_050_01_2, C_P_10000_050_01_2, E_U_10000_050_01_2, E_P_10000_050_01_2 = \
    gid.get_input_data("run_5_10000_050_01/postProcessing/singleGraph/1.2992/B_U.xy", "run_5_10000_050_01/postProcessing/singleGraph/1.2992/B_p.xy", "run_5_10000_050_01/postProcessing/singleGraph/1.2992/C_U.xy", "run_5_10000_050_01/postProcessing/singleGraph/1.2992/C_p.xy", "run_5_10000_050_01/postProcessing/singleGraph/1.2992/E_U.xy", "run_5_10000_050_01/postProcessing/singleGraph/1.2992/E_p.xy" )

B_U_y_10000_050_01_2 = B_U_10000_050_01_2[:,1]
B_u_10000_050_01_2 = B_U_10000_050_01_2[:,3]
B_v_10000_050_01_2 = B_U_10000_050_01_2[:,4]
B_P_y_10000_050_01_2 = B_P_10000_050_01_2[:,1]
B_P_10000_050_01_2 = B_P_10000_050_01_2[:,3]
C_U_y_10000_050_01_2 = C_U_10000_050_01_2[:,1]
C_u_10000_050_01_2 = C_U_10000_050_01_2[:,3]
C_v_10000_050_01_2 = C_U_10000_050_01_2[:,4]
C_P_y_10000_050_01_2 = C_P_10000_050_01_2[:,1]
C_P_10000_050_01_2 = C_P_10000_050_01_2[:,3]
E_U_y_10000_050_01_2 = E_U_10000_050_01_2[:,1]
E_u_10000_050_01_2 = E_U_10000_050_01_2[:,3]
E_v_10000_050_01_2 = E_U_10000_050_01_2[:,4]
E_P_y_10000_050_01_2 = E_P_10000_050_01_2[:,1]
E_P_10000_050_01_2 = E_P_10000_050_01_2[:,3]

''' Part 5: Generation of Plots Depicting Pressure as Function of Position for Re = 10 Across Lines B,C,E  '''


os.chdir('/Users/jcam98/Desktop/EducationInstitutions/UniversityofTexas/Courses/SPRING_2022/COE_347/Assignments/OpenFOAM/Projects/Final_Project/Team_12/Sim_Data/Low_Re')

# Line B

plt.plot(B_P_y_10_005_005_1, B_P_10_005_005_1, linestyle = '-.')
plt.plot(B_P_y_10_005_005_2, B_P_10_005_005_2, linestyle = '-.')
plt.plot(B_P_y_10_005_01_1, B_P_10_005_01_1, linestyle = '-.')
plt.plot(B_P_y_10_005_01_2, B_P_10_005_01_2, linestyle = '-.')
plt.plot(B_P_y_10_050_005_1, B_P_10_050_005_1, linestyle = '-.')
plt.plot(B_P_y_10_050_005_2, B_P_10_050_005_2, linestyle = '-.')
plt.plot(B_P_y_10_050_01_1, B_P_10_050_01_1, linestyle = '-.')
plt.plot(B_P_y_10_050_01_2, B_P_10_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position Along Left Wall Surface for Re = 10")
plt.legend(['WS:0.05, WT:0.05, REF:5','WS:0.05, WT:0.05, REF:10','WS:0.05,WT:0.1,REF:5', 'WS:0.05,WT:0.1, REF:10','WS:0.50,WT:0.05,REF:5','WS:0.50,WT:0.05,REF:10','WS:0.50,WT:0.1,REF:5','WS:0.50,WT:0.1,REF:10'],bbox_to_anchor=(1, 1))
plt.savefig("B_p_10.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_P_y_10_005_005_1, C_P_10_005_005_1, linestyle = '-.')
plt.plot(C_P_y_10_005_005_2, C_P_10_005_005_2, linestyle = '-.')
plt.plot(C_P_y_10_005_01_1, C_P_10_005_01_1, linestyle = '-.')
plt.plot(C_P_y_10_005_01_2, C_P_10_005_01_2, linestyle = '-.')
plt.plot(C_P_y_10_050_005_1, C_P_10_050_005_1, linestyle = '-.')
plt.plot(C_P_y_10_050_005_2, C_P_10_050_005_2, linestyle = '-.')
plt.plot(C_P_y_10_050_01_1, C_P_10_050_01_1, linestyle = '-.')
plt.plot(C_P_y_10_050_01_2, C_P_10_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position Along Right Wall Surface for Re = 10")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("C_p_10.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()


# Line E

plt.plot(E_P_y_10_005_005_1, E_P_10_005_005_1, linestyle = '-.')
plt.plot(E_P_y_10_005_005_2, E_P_10_005_005_2, linestyle = '-.')
plt.plot(E_P_y_10_005_01_1, E_P_10_005_01_1, linestyle = '-.')
plt.plot(E_P_y_10_005_01_2, E_P_10_005_01_2, linestyle = '-.')
plt.plot(E_P_y_10_050_005_1, E_P_10_050_005_1, linestyle = '-.')
plt.plot(E_P_y_10_050_005_2, E_P_10_050_005_2, linestyle = '-.')
plt.plot(E_P_y_10_050_01_1, E_P_10_050_01_1, linestyle = '-.')
plt.plot(E_P_y_10_050_01_2, E_P_10_050_01_2, linestyle = '-.')


plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("Pressure")
plt.title("Pressure vs Vertical Position Along Cavity Midsection for Re = 10")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("E_p_10.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()


''' Part 6: Generation of Plots Depicting x-component of velocity as Function of Position for Re=10 Across Lines B,C,E '''

# Line B

plt.plot(B_U_y_10_005_005_1, B_u_10_005_005_1, linestyle = '-.')
plt.plot(B_U_y_10_005_005_2, B_u_10_005_005_2, linestyle = '-.')
plt.plot(B_U_y_10_005_01_1, B_u_10_005_01_1, linestyle = '-.')
plt.plot(B_U_y_10_005_01_2, B_u_10_005_01_2, linestyle = '-.')
plt.plot(B_U_y_10_050_005_1, B_u_10_050_005_1, linestyle = '-.')
plt.plot(B_U_y_10_050_005_2, B_u_10_050_005_2, linestyle = '-.')
plt.plot(B_U_y_10_050_01_1, B_u_10_050_01_1, linestyle = '-.')
plt.plot(B_U_y_10_050_01_2, B_u_10_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("x-component of velocity 'u'")
plt.title("x-component of velocity vs Position Along Left Wall Surface for Re = 10")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("B_u_10.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_U_y_10_005_005_1, C_u_10_005_005_1, linestyle = '-.')
plt.plot(C_U_y_10_005_005_2, C_u_10_005_005_2, linestyle = '-.')
plt.plot(C_U_y_10_005_01_1, C_u_10_005_01_1, linestyle = '-.')
plt.plot(C_U_y_10_005_01_2, C_u_10_005_01_2, linestyle = '-.')
plt.plot(C_U_y_10_050_005_1, C_u_10_050_005_1, linestyle = '-.')
plt.plot(C_U_y_10_050_005_2, C_u_10_050_005_2, linestyle = '-.')
plt.plot(C_U_y_10_050_01_1, C_u_10_050_01_1, linestyle = '-.')
plt.plot(C_U_y_10_050_01_2, C_u_10_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("x-component of velocity 'u'")
plt.title("x-component of velocity vs Position Along Right Wall Surface for Re = 10")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("C_u_10.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_U_y_10_005_005_1, E_u_10_005_005_1, linestyle = '-.')
plt.plot(E_U_y_10_005_005_2, E_u_10_005_005_2, linestyle = '-.')
plt.plot(E_U_y_10_005_01_1, E_u_10_005_01_1, linestyle = '-.')
plt.plot(E_U_y_10_005_01_2, E_u_10_005_01_2, linestyle = '-.')
plt.plot(E_U_y_10_050_005_1, E_u_10_050_005_1, linestyle = '-.')
plt.plot(E_U_y_10_050_005_2, E_u_10_050_005_2, linestyle = '-.')
plt.plot(E_U_y_10_050_01_1, E_u_10_050_01_1, linestyle = '-.')
plt.plot(E_U_y_10_050_01_2, E_u_10_050_01_2, linestyle = '-.')


plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("x-component of velocity 'u'")
plt.title("x-component of velocity vs Position Along Cavity Midsection for Re = 10")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("E_u_10.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()



''' Part 7: Generation of Plots Depicting y-component of Velocity as Function of Position for Re=10 Across Lines, B,C,E '''


# Line B

plt.plot(B_U_y_10_005_005_1, B_v_10_005_005_1, linestyle = '-.')
plt.plot(B_U_y_10_005_005_2, B_v_10_005_005_2, linestyle = '-.')
plt.plot(B_U_y_10_005_01_1, B_v_10_005_01_1, linestyle = '-.')
plt.plot(B_U_y_10_005_01_2, B_v_10_005_01_2, linestyle = '-.')
plt.plot(B_U_y_10_050_005_1, B_v_10_050_005_1, linestyle = '-.')
plt.plot(B_U_y_10_050_005_2, B_v_10_050_005_2, linestyle = '-.')
plt.plot(B_U_y_10_050_01_1, B_v_10_050_01_1, linestyle = '-.')
plt.plot(B_U_y_10_050_01_2, B_v_10_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("y-component of velocity 'v'")
plt.title("y-component of velocity vs Position Along Left Wall Surface for Re = 10")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("B_v_10.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_U_y_10_005_005_1, C_v_10_005_005_1, linestyle = '-.')
plt.plot(C_U_y_10_005_005_2, C_v_10_005_005_2, linestyle = '-.')
plt.plot(C_U_y_10_005_01_1, C_v_10_005_01_1, linestyle = '-.')
plt.plot(C_U_y_10_005_01_2, C_v_10_005_01_2, linestyle = '-.')
plt.plot(C_U_y_10_050_005_1, C_v_10_050_005_1, linestyle = '-.')
plt.plot(C_U_y_10_050_005_2, C_v_10_050_005_2, linestyle = '-.')
plt.plot(C_U_y_10_050_01_1, C_v_10_050_01_1, linestyle = '-.')
plt.plot(C_U_y_10_050_01_2, C_v_10_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("y-component of velocity 'v'")
plt.title("y-component of velocity vs Position Along Right Wall Surface for Re = 10")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("C_v_10.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_U_y_10_005_005_1, E_v_10_005_005_1, linestyle = '-.')
plt.plot(E_U_y_10_005_005_2, E_v_10_005_005_2, linestyle = '-.')
plt.plot(E_U_y_10_005_01_1, E_v_10_005_01_1, linestyle = '-.')
plt.plot(E_U_y_10_005_01_2, E_v_10_005_01_2, linestyle = '-.')
plt.plot(E_U_y_10_050_005_1, E_v_10_050_005_1, linestyle = '-.')
plt.plot(E_U_y_10_050_005_2, E_v_10_050_005_2, linestyle = '-.')
plt.plot(E_U_y_10_050_01_1, E_v_10_050_01_1, linestyle = '-.')
plt.plot(E_U_y_10_050_01_2, E_v_10_050_01_2, linestyle = '-.')


plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("y-component of velocity 'v'")
plt.title("y-component of velocity vs Position Along Cavity Midsection for Re = 10")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("E_v_10.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

''' Part 8: Generation of Plots Depicting Pressure as Function of Position for Re = 200 Across Lines B,C,E  '''


# Line B

plt.plot(B_P_y_200_005_005_1, B_P_200_005_005_1, linestyle = '-.')
plt.plot(B_P_y_200_005_005_2, B_P_200_005_005_2, linestyle = '-.')
plt.plot(B_P_y_200_005_01_1, B_P_200_005_01_1, linestyle = '-.')
plt.plot(B_P_y_200_005_01_2, B_P_200_005_01_2, linestyle = '-.')
plt.plot(B_P_y_200_050_005_1, B_P_200_050_005_1, linestyle = '-.')
plt.plot(B_P_y_200_050_005_2, B_P_200_050_005_2, linestyle = '-.')
plt.plot(B_P_y_200_050_01_1, B_P_200_050_01_1, linestyle = '-.')
plt.plot(B_P_y_200_050_01_2, B_P_200_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position Along Left Wall Surface for Re = 200")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'] ,bbox_to_anchor=(1, 1))
plt.savefig("B_p_200.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_P_y_200_005_005_1, C_P_200_005_005_1, linestyle = '-.')
plt.plot(C_P_y_200_005_005_2, C_P_200_005_005_2, linestyle = '-.')
plt.plot(C_P_y_200_005_01_1, C_P_200_005_01_1, linestyle = '-.')
plt.plot(C_P_y_200_005_01_2, C_P_200_005_01_2, linestyle = '-.')
plt.plot(C_P_y_200_050_005_1, C_P_200_050_005_1, linestyle = '-.')
plt.plot(C_P_y_200_050_005_2, C_P_200_050_005_2, linestyle = '-.')
plt.plot(C_P_y_200_050_01_1, C_P_200_050_01_1, linestyle = '-.')
plt.plot(C_P_y_200_050_01_2, C_P_200_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position Along Right Wall Surface for Re = 200")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("C_p_200.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()


# Line E

plt.plot(E_P_y_200_005_005_1, E_P_200_005_005_1, linestyle = '-.')
plt.plot(E_P_y_200_005_005_2, E_P_200_005_005_2, linestyle = '-.')
plt.plot(E_P_y_200_005_01_1, E_P_200_005_01_1, linestyle = '-.')
plt.plot(E_P_y_200_005_01_2, E_P_200_005_01_2, linestyle = '-.')
plt.plot(E_P_y_200_050_005_1, E_P_200_050_005_1, linestyle = '-.')
plt.plot(E_P_y_200_050_005_2, E_P_200_050_005_2, linestyle = '-.')
plt.plot(E_P_y_200_050_01_1, E_P_200_050_01_1, linestyle = '-.')
plt.plot(E_P_y_200_050_01_2, E_P_200_050_01_2, linestyle = '-.')


plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("Pressure")
plt.title("Pressure vs Vertical Position Along Cavity Midsection for Re = 200")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("E_p_200.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()


''' Part 9: Generation of Plots Depicting x-component of velocity as Function of Position for Re=200 Across Lines B,C,E '''

# Line B

plt.plot(B_U_y_200_005_005_1, B_u_200_005_005_1, linestyle = '-.')
plt.plot(B_U_y_200_005_005_2, B_u_200_005_005_2, linestyle = '-.')
plt.plot(B_U_y_200_005_01_1, B_u_200_005_01_1, linestyle = '-.')
plt.plot(B_U_y_200_005_01_2, B_u_200_005_01_2, linestyle = '-.')
plt.plot(B_U_y_200_050_005_1, B_u_200_050_005_1, linestyle = '-.')
plt.plot(B_U_y_200_050_005_2, B_u_200_050_005_2, linestyle = '-.')
plt.plot(B_U_y_200_050_01_1, B_u_200_050_01_1, linestyle = '-.')
plt.plot(B_U_y_200_050_01_2, B_u_200_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("x-component of velocity 'u'")
plt.title("x-component of velocity vs Position Along Left Wall Surface for Re = 200")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("B_u_200.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_U_y_200_005_005_1, C_u_200_005_005_1, linestyle = '-.')
plt.plot(C_U_y_200_005_005_2, C_u_200_005_005_2, linestyle = '-.')
plt.plot(C_U_y_200_005_01_1, C_u_200_005_01_1, linestyle = '-.')
plt.plot(C_U_y_200_005_01_2, C_u_200_005_01_2, linestyle = '-.')
plt.plot(C_U_y_200_050_005_1, C_u_200_050_005_1, linestyle = '-.')
plt.plot(C_U_y_200_050_005_2, C_u_200_050_005_2, linestyle = '-.')
plt.plot(C_U_y_200_050_01_1, C_u_200_050_01_1, linestyle = '-.')
plt.plot(C_U_y_200_050_01_2, C_u_200_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("x-component of velocity 'u'")
plt.title("x-component of velocity vs Position Along Right Wall Surface for Re = 200")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("C_u_200.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_U_y_200_005_005_1, E_u_200_005_005_1, linestyle = '-.')
plt.plot(E_U_y_200_005_005_2, E_u_200_005_005_2, linestyle = '-.')
plt.plot(E_U_y_200_005_01_1, E_u_200_005_01_1, linestyle = '-.')
plt.plot(E_U_y_200_005_01_2, E_u_200_005_01_2, linestyle = '-.')
plt.plot(E_U_y_200_050_005_1, E_u_200_050_005_1, linestyle = '-.')
plt.plot(E_U_y_200_050_005_2, E_u_200_050_005_2, linestyle = '-.')
plt.plot(E_U_y_200_050_01_1, E_u_200_050_01_1, linestyle = '-.')
plt.plot(E_U_y_200_050_01_2, E_u_200_050_01_2, linestyle = '-.')


plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("x-component of velocity 'u'")
plt.title("x-component of velocity vs Position Along Cavity Midsection for Re = 200")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("E_u_200.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()



''' Part 10: Generation of Plots Depicting y-component of Velocity as Function of Position for Re=200 Across Lines, B,C,E '''


# Line B

plt.plot(B_U_y_200_005_005_1, B_v_200_005_005_1, linestyle = '-.')
plt.plot(B_U_y_200_005_005_2, B_v_200_005_005_2, linestyle = '-.')
plt.plot(B_U_y_200_005_01_1, B_v_200_005_01_1, linestyle = '-.')
plt.plot(B_U_y_200_005_01_2, B_v_200_005_01_2, linestyle = '-.')
plt.plot(B_U_y_200_050_005_1, B_v_200_050_005_1, linestyle = '-.')
plt.plot(B_U_y_200_050_005_2, B_v_200_050_005_2, linestyle = '-.')
plt.plot(B_U_y_200_050_01_1, B_v_200_050_01_1, linestyle = '-.')
plt.plot(B_U_y_200_050_01_2, B_v_200_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("y-component of velocity 'v'")
plt.title("y-component of velocity vs Position Along Left Wall Surface for Re = 200")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("B_v_200.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_U_y_200_005_005_1, C_v_200_005_005_1, linestyle = '-.')
plt.plot(C_U_y_200_005_005_2, C_v_200_005_005_2, linestyle = '-.')
plt.plot(C_U_y_200_005_01_1, C_v_200_005_01_1, linestyle = '-.')
plt.plot(C_U_y_200_005_01_2, C_v_200_005_01_2, linestyle = '-.')
plt.plot(C_U_y_200_050_005_1, C_v_200_050_005_1, linestyle = '-.')
plt.plot(C_U_y_200_050_005_2, C_v_200_050_005_2, linestyle = '-.')
plt.plot(C_U_y_200_050_01_1, C_v_200_050_01_1, linestyle = '-.')
plt.plot(C_U_y_200_050_01_2, C_v_200_050_01_2, linestyle = '-.')


plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("y-component of velocity 'v'")
plt.title("y-component of velocity vs Position Along Right Wall Surface for Re = 200")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("C_v_200.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_U_y_200_005_005_1, E_v_200_005_005_1, linestyle = '-.')
plt.plot(E_U_y_200_005_005_2, E_v_200_005_005_2, linestyle = '-.')
plt.plot(E_U_y_200_005_01_1, E_v_200_005_01_1, linestyle = '-.')
plt.plot(E_U_y_200_005_01_2, E_v_200_005_01_2, linestyle = '-.')
plt.plot(E_U_y_200_050_005_1, E_v_200_050_005_1, linestyle = '-.')
plt.plot(E_U_y_200_050_005_2, E_v_200_050_005_2, linestyle = '-.')
plt.plot(E_U_y_200_050_01_1, E_v_200_050_01_1, linestyle = '-.')
plt.plot(E_U_y_200_050_01_2, E_v_200_050_01_2, linestyle = '-.')


plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("y-component of velocity 'v'")
plt.title("y-component of velocity vs Position Along Cavity Midsection for Re = 200")
plt.legend(['Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.05, Wall Thickness: 0.1, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.05, Refinement: 10', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 10'],bbox_to_anchor=(1, 1))
plt.savefig("E_v_200.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

''' Part 11: Generation of Plots Depicting Pressure as Function of Position for Re = 1000 Across Lines B,C,E  '''

os.chdir('/Users/jcam98/Desktop/EducationInstitutions/UniversityofTexas/Courses/SPRING_2022/COE_347/Assignments/OpenFOAM/Projects/Final_Project/Team_12/Sim_Data/High_Re')

# Line B

plt.plot(B_P_y_1000_050_01_1, B_P_1000_050_01_1, linestyle = '-.')
plt.plot(B_P_y_1000_050_01_2, B_P_1000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position at t = 1.3 seconds Along Left Wall Surface for Re = 1000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'],bbox_to_anchor=(1, 1))
plt.savefig("B_p_1000.jpg",bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_P_y_1000_050_01_1, C_P_1000_050_01_1, linestyle = '-.')
plt.plot(C_P_y_1000_050_01_2, C_P_1000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position at t = 1.3 seconds Along Right Wall Surface for Re = 1000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("C_p_1000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_P_y_1000_050_01_1, E_P_1000_050_01_1, linestyle = '-.')
plt.plot(E_P_y_1000_050_01_2, E_P_1000_050_01_2, linestyle = '-.')

plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position at t = 1.3 seconds Along Cavity Midsection for Re = 1000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'],bbox_to_anchor=(1, 1))
plt.savefig("E_p_1000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()


''' Part 12: Generation of Plots Depicting x-component of velocity as Function of Position for Re=1000 Across Lines B,C,E '''

# Line B

plt.plot(B_U_y_1000_050_01_1, B_u_1000_050_01_1, linestyle = '-.')
plt.plot(B_U_y_1000_050_01_2, B_u_1000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("x-component of velocity (u)")
plt.title("x-component of velocity vs Position at t = 1.3 seconds Along Left Wall Surface for Re = 1000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("B_u_1000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_U_y_1000_050_01_1, C_u_1000_050_01_1, linestyle = '-.')
plt.plot(C_U_y_1000_050_01_2, C_u_1000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("x-component of velocity (u)")
plt.title("x-component of velocity vs Position at t = 1.3 seconds Along Right Wall Surface for Re = 1000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("C_u_1000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_U_y_1000_050_01_1, E_u_1000_050_01_1, linestyle = '-.')
plt.plot(E_U_y_1000_050_01_2, E_u_1000_050_01_2, linestyle = '-.')

plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("x-component of velocity (u)")
plt.title("x-component of velocity vs Position at t = 1.3 seconds Along Cavity Midsection for Re = 1000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("E_u_1000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()


''' Part 13: Generation of Plots Depicting y-component of velocity as Function of Position for Re=1000 Across Lines B,C,E '''

# Line B

plt.plot(B_U_y_1000_050_01_1, B_v_1000_050_01_1, linestyle = '-.')
plt.plot(B_U_y_1000_050_01_2, B_v_1000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("y-component of velocity (v)")
plt.title("y-component of velocity vs Position at t = 1.3 seconds Along Left Wall Surface for Re = 1000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("B_v_1000.jpg", bbox_inches = 'tight',  dpi = 600)
plt.show()

# Line C

plt.plot(C_U_y_1000_050_01_1, C_v_1000_050_01_1, linestyle = '-.')
plt.plot(C_U_y_1000_050_01_2, C_v_1000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("y-component of velocity (u)")
plt.title("y-component of velocity vs Position at t = 1.3 seconds Along Right Wall Surface for Re = 1000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("C_v_1000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_U_y_1000_050_01_1, E_v_1000_050_01_1, linestyle = '-.')
plt.plot(E_U_y_1000_050_01_2, E_v_1000_050_01_2, linestyle = '-.')

plt.xlabel("Vertical Position Along Cavity Midsection 'E'")
plt.ylabel("y-component of velocity (v)")
plt.title("y-component of velocity vs Position at t = 1.3 seconds Along Cavity Midsection for Re = 1000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("E_v_1000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

''' Part 14: Generation of Plots Depicting Pressure as Function of Position for Re = 10000 Across Lines B,C,E  '''


# Line B

plt.plot(B_P_y_10000_050_01_1, B_P_10000_050_01_1, linestyle = '-.')
plt.plot(B_P_y_10000_050_01_2, B_P_10000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position at t = 1.3 seconds Along Left Wall Surface for Re = 10000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("B_p_10000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_P_y_10000_050_01_1, C_P_10000_050_01_1, linestyle = '-.')
plt.plot(C_P_y_10000_050_01_2, C_P_10000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position at t = 1.3 seconds Along Right Wall Surface for Re = 10000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("C_p_10000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_P_y_10000_050_01_1, E_P_10000_050_01_1, linestyle = '-.')
plt.plot(E_P_y_10000_050_01_2, E_P_10000_050_01_2, linestyle = '-.')

plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("Pressure")
plt.title("Pressure vs Position at t = 1.3 seconds Along Cavity Midsection for Re = 10000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("E_p_10000.jpg", bbox_inches = 'tight',  dpi = 600)
plt.show()


''' Part 15: Generation of Plots Depicting x-component of velocity as Function of Position for Re=10000 Across Lines B,C,E '''

# Line B

plt.plot(B_U_y_10000_050_01_1, B_u_10000_050_01_1, linestyle = '-.')
plt.plot(B_U_y_10000_050_01_2, B_u_10000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("x-component of velocity (u)")
plt.title("x-component of velocity vs Position at t = 1.3 seconds Along Left Wall Surface for Re = 10000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("B_u_10000.jpg", bbox_inches = 'tight',  dpi = 600)
plt.show()

# Line C

plt.plot(C_U_y_10000_050_01_1, C_u_10000_050_01_1, linestyle = '-.')
plt.plot(C_U_y_10000_050_01_2, C_u_10000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("x-component of velocity (u)")
plt.title("x-component of velocity vs Position at t = 1.3 seconds Along Right Wall Surface for Re = 10000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("C_u_10000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_U_y_10000_050_01_1, E_u_10000_050_01_1, linestyle = '-.')
plt.plot(E_U_y_10000_050_01_2, E_u_10000_050_01_2, linestyle = '-.')

plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("x-component of velocity (u)")
plt.title("x-component of velocity vs Position at t = 1.3 seconds Along Cavity Midsection for Re = 10000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("E_u_10000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()


''' Part 16: Generation of Plots Depicting y-component of velocity as Function of Position for Re=10000 Across Lines B,C,E '''

# Line B

plt.plot(B_U_y_10000_050_01_1, B_v_10000_050_01_1, linestyle = '-.')
plt.plot(B_U_y_10000_050_01_2, B_v_10000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Left Wall Surface 'B'")
plt.ylabel("y-component of velocity (v)")
plt.title("y-component of velocity vs Position at t = 1.3 seconds Along Left Wall Surface for Re = 10000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("B_v_10000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line C

plt.plot(C_U_y_10000_050_01_1, C_v_10000_050_01_1, linestyle = '-.')
plt.plot(C_U_y_10000_050_01_2, C_v_10000_050_01_2, linestyle = '-.')

plt.xlabel("Coordinate Position Along Right Wall Surface 'C'")
plt.ylabel("y-component of velocity (u)")
plt.title("y-component of velocity vs Position at t = 1.3 seconds Along Right Wall Surface for Re = 10000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("C_v_10000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Line E

plt.plot(E_U_y_10000_050_01_1, E_v_10000_050_01_1, linestyle = '-.')
plt.plot(E_U_y_10000_050_01_2, E_v_10000_050_01_2, linestyle = '-.')

plt.xlabel("Vertical Coordinate Position Along Cavity Midsection 'E'")
plt.ylabel("y-component of velocity (v)")
plt.title("y-component of velocity vs Position at t = 1.3 seconds Along Cavity Midsection for Re = 10000")
plt.legend(['Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 3', 'Win.Size: 0.50, Wall Thickness: 0.1, Refinement: 5'], bbox_to_anchor=(1, 1))
plt.savefig("E_v_10000.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

