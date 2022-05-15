import os
import numpy as np
from statistics import mode


def main():
    # ------------------- DATA PARSING -------------------
    path = '/home/mandy/Desktop/347_4_DATA/'
    files = os.listdir(path)
    # Formatting of name: mesh factor, Re, wall thickness, window width
    for file in files:
        dir_U = path + file + '/postProcessing/singleGraph/6/E_U.xy'
        dir_P = path + file + '/postProcessing/singleGraph/6/E_p.xy'

        X = []
        Y = []
        Ux = []
        Uy = []
        P = []
        recirc = []

        with open(dir_U, 'r') as u_f:
            lines = u_f.read().split("\n")
            for line in lines:

                line = line.split('\t')

                if line != ['']:

                    X.append(float(line[0]))
                    Y.append(float(line[1]))
                    Ux.append(float(line[3]))
                    Uy.append(float(line[4]))

            u_f.close()

        with open(dir_P, 'r') as u_p:
            lines = u_p.read().split("\n")
            for line in lines:

                line = line.split('\t')

                if line != ['']:
                    P.append(float(line[3]))
            u_p.close()

        # ------------------- Find Number of Vortices and Location of Vortex Center -------------------
        num_vort_x = 0
        prev_x = np.sign(Ux[0])
        loc_x_vort = []

        for x in range(len(Ux)):
            sign = np.sign(Ux[x])

            if sign == -prev_x:
                num_vort_x = num_vort_x + 1
                prev_x = sign
                loc_x_vort.append(Y[x])

        # ------------------- Find Length of Pressure Disturbance Zone -------------------

        P0 = P[-1]  # General pressure
        for p in range(len(P)):
            diff_p = 1 / P0 * P[p]
            if abs(diff_p - 1) > 0.00001:
                recirc.append(Y[p])

        if recirc:
            recirc_range = max(recirc) - min(recirc)
        else:
            recirc_range = 0

        print(file)
        print('Location of Vortices: ', loc_x_vort)
        print('Pressure Disturbance Range: ', recirc_range, '\n')

    return


main()
