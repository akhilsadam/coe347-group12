''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: strain_rate_main.py                                      
 Description: This python module serves as the main program for
 post-processing the velocity data from each of the simulations
 unsteady flows for the purpose of generating Mean rate of strain tensor vs. time
 plots, and location of Mean rate of strain tensor vs. time plots for 
 the high Re flow along the left and right wall surfaces'''            

# Import modules                                                 

from matplotlib import pyplot as plt
import strain_rate as sr
import os
import numpy as np


''' Part 1: Read in xy files of velocity field, and
 associated line distances for each time step into 2D numpy arrays for unsteady flow with Re = 1000 number sims '''

''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.50, and wall thickness of 0.1
into a 2D numpy array '''

os.chdir('/Users/jcam98/Desktop/EducationInstitutions/UniversityofTexas/Courses/SPRING_2022/COE_347/Assignments/OpenFOAM/Projects/Final_Project/Team_12/Sim_Data/High_Re/run_3_1000_050_01/postProcessing/singleGraph')

v_all_time_left_1 = []
v_all_time_left_2 = []
v_all_time_right_1 = []
v_all_time_right_2 = []
time_1000_1 = np.array(np.zeros(601))


''' Iterate through each timestep folder and extract velocity distributions
across left and right wall surfaces for two sample lines across each surface'''

count = 0
for d in os.listdir("./"):
    
   try: 
    
        float(d)
        q = d
        B_U_1 = np.genfromtxt(f'{q}/B_U.xy')
        B_U_2 = np.genfromtxt(f'{q}/B2_U.xy')
        C_U_1 = np.genfromtxt(f'{q}/C_U.xy')
        C_U_2 = np.genfromtxt(f'{q}/C2_U.xy')
        v_all_time_left_1.append(B_U_1[:,4])
        v_all_time_left_2.append(B_U_2[:,4])
        v_all_time_right_1.append(C_U_1[:,4])
        v_all_time_right_2.append(C_U_2[:,4])
        y = B_U_1[:,1]
        x_left_1 = B_U_1[:,0]
        x_left_2 = B_U_2[:,0]
        x_right_1 = C_U_1[:,0]
        x_right_2 = C_U_2[:,0]
        time_1000_1[count] = float(f'{q}')
        count = count + 1
        
   except: 
        
        pass

time_1000_1 = np.sort(time_1000_1)
v_all_time_left_1 = np.array(v_all_time_left_1)
v_all_time_right_1 = np.array(v_all_time_right_1)
v_all_time_left_2 = np.array(v_all_time_left_2)
v_all_time_right_2 = np.array(v_all_time_right_2)

e_y_Mean_left_val_1000_1, e_y_Mean_right_val_1000_1 = sr.get_strain_tensor(v_all_time_left_1, v_all_time_left_2, v_all_time_right_1, v_all_time_right_2, y, x_left_1, x_left_2, x_right_1, x_right_2)    


''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.50, and wall thickness of 0.1
into a 2D numpy array '''

os.chdir('/Users/jcam98/Desktop/EducationInstitutions/UniversityofTexas/Courses/SPRING_2022/COE_347/Assignments/OpenFOAM/Projects/Final_Project/Team_12/Sim_Data/High_Re/run_5_1000_050_01/postProcessing/singleGraph')

v_all_time_left_1 = []
v_all_time_left_2 = []
v_all_time_right_1 = []
v_all_time_right_2 = []
time_1000_2 = np.array(np.zeros(601))


''' Iterate through each timestep folder and extract velocity distributions
across left and right wall surfaces for two sample lines across each surface'''

count = 0
for d in os.listdir("./"):
    
   try: 
    
        float(d)
        q = d
        B_U_1 = np.genfromtxt(f'{q}/B_U.xy')
        B_U_2 = np.genfromtxt(f'{q}/B2_U.xy')
        C_U_1 = np.genfromtxt(f'{q}/C_U.xy')
        C_U_2 = np.genfromtxt(f'{q}/C2_U.xy')
        v_all_time_left_1.append(B_U_1[:,4])
        v_all_time_left_2.append(B_U_2[:,4])
        v_all_time_right_1.append(C_U_1[:,4])
        v_all_time_right_2.append(C_U_2[:,4])
        y = B_U_1[:,1]
        x_left_1 = B_U_1[:,0]
        x_left_2 = B_U_2[:,0]
        x_right_1 = C_U_1[:,0]
        x_right_2 = C_U_2[:,0]
        time_1000_2[count] = float(f'{q}')
        count = count + 1
        
   except: 
        
        pass

time_1000_2 = np.sort(time_1000_2)
v_all_time_left_1 = np.array(v_all_time_left_1)
v_all_time_right_1 = np.array(v_all_time_right_1)
v_all_time_left_2 = np.array(v_all_time_left_2)
v_all_time_right_2 = np.array(v_all_time_right_2)

e_y_Mean_left_val_1000_2, e_y_Mean_right_val_1000_2 = sr.get_strain_tensor(v_all_time_left_1, v_all_time_left_2, v_all_time_right_1, v_all_time_right_2, y, x_left_1, x_left_2, x_right_1, x_right_2)    


''' Part 2: Read in xy files of velocity field, and
  associated line distances for each time step into 2D numpy arrays for unsteady flow with Re = 10000 number sims '''

''' Read in "xy" files of properties for simulation 
with first mesh refinement, window size of 0.50, and wall thickness of 0.1
into a 2D numpy array '''

os.chdir('/Users/jcam98/Desktop/EducationInstitutions/UniversityofTexas/Courses/SPRING_2022/COE_347/Assignments/OpenFOAM/Projects/Final_Project/Team_12/Sim_Data/High_Re/run_3_10000_050_01/postProcessing/singleGraph')

v_all_time_left_1 = []
v_all_time_left_2 = []
v_all_time_right_1 = []
v_all_time_right_2 = []
time_10000_1 = np.array(np.zeros(601))


''' Iterate through each timestep folder and extract velocity distribution
across left and right wall surfaces '''

count = 0
for d in os.listdir("./"):
    
   try: 
    
        float(d)
        q = d
        B_U_1 = np.genfromtxt(f'{q}/B_U.xy')
        B_U_2 = np.genfromtxt(f'{q}/B2_U.xy')
        C_U_1 = np.genfromtxt(f'{q}/C_U.xy')
        C_U_2 = np.genfromtxt(f'{q}/C2_U.xy')
        v_all_time_left_1.append(B_U_1[:,4])
        v_all_time_left_2.append(B_U_2[:,4])
        v_all_time_right_1.append(C_U_1[:,4])
        v_all_time_right_2.append(C_U_2[:,4])
        y = B_U_1[:,1]
        x_left_1 = B_U_1[:,0]
        x_left_2 = B_U_2[:,0]
        x_right_1 = C_U_1[:,0]
        x_right_2 = C_U_2[:,0]
        time_10000_1[count] = float(f'{q}')
        count = count + 1
        
   except: 
        
        pass

time_10000_1 = np.sort(time_10000_1)
v_all_time_left_1 = np.array(v_all_time_left_1)
v_all_time_right_1 = np.array(v_all_time_right_1)
v_all_time_left_2 = np.array(v_all_time_left_2)
v_all_time_right_2 = np.array(v_all_time_right_2)

e_y_Mean_left_val_10000_1, e_y_Mean_right_val_10000_1 = sr.get_strain_tensor(v_all_time_left_1, v_all_time_left_2, v_all_time_right_1, v_all_time_right_2, y, x_left_1, x_left_2, x_right_1, x_right_2)    

''' Read in "xy" files of properties for simulation 
with second mesh refinement, window size of 0.50, and wall thickness of 0.1
into a 2D numpy array '''

os.chdir('/Users/jcam98/Desktop/EducationInstitutions/UniversityofTexas/Courses/SPRING_2022/COE_347/Assignments/OpenFOAM/Projects/Final_Project/Team_12/Sim_Data/High_Re/run_5_10000_050_01/postProcessing/singleGraph')

v_all_time_left_1 = []
v_all_time_left_2 = []
v_all_time_right_1 = []
v_all_time_right_2 = []
time_10000_2 = np.array(np.zeros(601))


''' Iterate through each timestep folder and extract velocity distributions
across left and right wall surfaces for two sample lines across each surface'''

count = 0
for d in os.listdir("./"):
    
   try: 
    
        float(d)
        q = d
        B_U_1 = np.genfromtxt(f'{q}/B_U.xy')
        B_U_2 = np.genfromtxt(f'{q}/B2_U.xy')
        C_U_1 = np.genfromtxt(f'{q}/C_U.xy')
        C_U_2 = np.genfromtxt(f'{q}/C2_U.xy')
        v_all_time_left_1.append(B_U_1[:,4])
        v_all_time_left_2.append(B_U_2[:,4])
        v_all_time_right_1.append(C_U_1[:,4])
        v_all_time_right_2.append(C_U_2[:,4])
        y = B_U_1[:,1]
        x_left_1 = B_U_1[:,0]
        x_left_2 = B_U_2[:,0]
        x_right_1 = C_U_1[:,0]
        x_right_2 = C_U_2[:,0]
        time_10000_2[count] = float(f'{q}')
        count = count + 1
        
   except: 
        
        pass

time_10000_2 = np.sort(time_10000_2)
v_all_time_left_1 = np.array(v_all_time_left_1)
v_all_time_right_1 = np.array(v_all_time_right_1)
v_all_time_left_2 = np.array(v_all_time_left_2)
v_all_time_right_2 = np.array(v_all_time_right_2)

e_y_Mean_left_val_10000_2, e_y_Mean_right_val_10000_2  = sr.get_strain_tensor(v_all_time_left_1, v_all_time_left_2, v_all_time_right_1, v_all_time_right_2, y, x_left_1, x_left_2, x_right_1, x_right_2)    

 
''' Part 3: Generation of Mean Strain Rate vs. Time Plots  '''  

# Simulation with Re = 1000, first mesh refinement for Left Wall Surface

plt.plot(time_1000_1, e_y_Mean_left_val_1000_1, linestyle = '-.')
plt.xlabel("Time")
plt.ylabel("Mean Strain Rate")
plt.title("Mean Strain Rate on Left Wall Surface for Re = 1000 with Refinement = 3")
plt.savefig("B_Mean_strain_rate_val_1000_1.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Simulation with Re = 1000, second mesh refinement for Left Wall Surface

plt.plot(time_1000_2, e_y_Mean_left_val_1000_2, linestyle = '-.')
plt.xlabel("Time")
plt.ylabel("Mean Strain Rate")
plt.title("Mean Strain Rate on Left Wall Surface for Re = 1000 with Refinement = 5")
plt.savefig("B_mean_strain_rate_val_1000_2.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Simulation with Re = 1000, first mesh refinement for Right Wall Surface

plt.plot(time_1000_1, e_y_Mean_right_val_1000_1, linestyle = '-.')
plt.xlabel("Time")
plt.ylabel("Mean Strain Rate")
plt.title("Mean Strain Rate on Right Wall Surface for Re = 1000 with Refinement = 3")
plt.savefig("C_Mean_strain_rate_val_1000_1.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Simulation with Re = 1000, second mesh refinement for Right Wall Surface

plt.plot(time_1000_2, e_y_Mean_right_val_1000_2, linestyle = '-.')
plt.xlabel("Time")
plt.ylabel("Mean Strain Rate")
plt.title("Mean Strain Rate on Right Wall Surface for Re = 1000 with Refinement = 5")
plt.savefig("C_mean_strain_rate_val_1000_2.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Simulation with Re = 10000, first mesh refinement for Left Wall Surface

plt.plot(time_10000_1, e_y_Mean_left_val_10000_1, linestyle = '-.')
plt.xlabel("Time")
plt.ylabel("Mean Strain Rate")
plt.title("Mean Strain Rate on Left Wall Surface for Re = 10000 with Refinement = 3")
plt.savefig("B_Mean_strain_rate_val_10000_1.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Simulation with Re = 10000, second mesh refinement for Left Wall Surface

plt.plot(time_10000_2, e_y_Mean_left_val_10000_2, linestyle = '-.')
plt.xlabel("Time")
plt.ylabel("Mean Strain Rate")
plt.title("Mean Strain Rate on Left Wall Surface for Re = 10000 with Refinement = 5")
plt.savefig("B_mean_strain_rate_val_10000_2.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Simulation with Re = 10000, first mesh refinement for Right Wall Surface

plt.plot(time_10000_1, e_y_Mean_right_val_10000_1, linestyle = '-.')
plt.xlabel("Time")
plt.ylabel("Mean Strain Rate")
plt.title("Mean Strain Rate on Right Wall Surface for Re = 10000 with Refinement = 3")
plt.savefig("C_Mean_strain_rate_val_10000_1.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()

# Simulation with Re = 10000, second mesh refinement for Right Wall Surface

plt.plot(time_10000_2, e_y_Mean_right_val_10000_2, linestyle = '-.')
plt.xlabel("Time")
plt.ylabel("Mean Strain Rate")
plt.title("Mean Strain Rate on Right Wall Surface for Re = 10000 with Refinement = 5")
plt.savefig("C_mean_strain_rate_val_10000_2.jpg", bbox_inches = 'tight', dpi = 600)
plt.show()
