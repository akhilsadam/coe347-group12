import os
import pandas as pd
from scipy import signal as sig
import matplotlib.pyplot as plt
import numpy as np


def main():
    # ------------------- DATA PARSING -------------------
    path = '/home/mandy/Desktop/High Re/'
    files = os.listdir(path)
    # Formatting of name: mesh factor, Re, wall thickness, window width
    for file in files:
        print(file)
        data = path + file + '/postProcessing/probes/0/U'

        df = pd.read_csv(data, sep='             ', header=None, names=['Time', 'Probe 0', 'Probe 1'], engine='python')

        uy0 = []
        uy1 = []
        time = []

        for val in df['Probe 0']:
            val = val.split()
            uy0.append(float(val[1]))

        for val in df['Probe 1']:
            val = val.split()
            uy1.append(float(val[1]))

        for val in df['Time']:
            time.append(float(val))

        # ------------------- Fourier Transform -------------------
        # Using fourier transform of data to calculate frequency
        t0 = 0  # Multiply by sampling rate

        t = time

        X = np.fft.fft(uy0)  # Fourier transform
        N = len(X)
        n = np.arange(N)
        T = N / 10
        freq = n / T
        freq = [x for x in freq if x < 1]
        X = X[0:len(freq)]
        # ------------------- Filter -------------------
        p = 100
        peak_location = [[]]
        while not peak_location[0]:
            p -= 1
            peak_location = sig.find_peaks(X, prominence=p)  # find locations of peaks so we may find
        # frequency! (FREQUENCY IS X DOMAIN)

        # Frequency will be LOW frequency
        Yu_filtered = abs(np.abs(freq[min(peak_location[0]) + 1]))  # For some reason indices seem to be 1 lower?
        # ------------------- Get variables ! -------------------
        fs = 10  # [Hz] Samples collected per second
        ts = 1.0 / fs  # [s] Time step
        N = len(X)  # Number of samples
        f0 = Yu_filtered  # [Hz] Frequency obtained from fourier transform
        D = 1  # [m OR dimensionless] Diameter of Cylinder
        U = 1  # [m/s OR dimensionless] Velocity of Freestream

        # ------------------- Strouhal number Calculation -------------------
        St = f0 * D / U  # [dimensionless] Strouhal Number
        print('Strouhal Number at Probe 0:', St)

        # ------------------- PLOTS -------------------
        plt.figure(figsize=(8, 6))
        plt.plot(t, uy0, 'r')
        plt.ylabel('Velocity (Uy)')
        plt.xlabel('Time')
        plt.title('Uy vs Time Probe 0 ' + file)
        plt.show()

        plt.figure(figsize=(8, 6))
        plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="b")
        plt.xlabel('Freq (Hz)')
        plt.ylabel('FFT Amplitude |X(freq)|')
        plt.title('FFT Plot of Von Karman Vortex Shedding Frequency Probe 0 ' + file)
        plt.xlim(0, max(freq))
        plt.show()

        # ------------------- Wildly inefficient but doing again for probe 1 :') sorry -------------------
        # ------------------- Fourier Transform -------------------
        # Using fourier transform of data to calculate frequency

        t = time

        X = np.fft.fft(uy1)  # Fourier transform
        N = len(X)
        n = np.arange(N)
        T = N / 10
        freq = n / T

        freq = [x for x in freq if x < 1]
        X = X[0:len(freq)]
        # ------------------- Filter -------------------
        p = 100
        peak_location = [[]]
        while not peak_location[0]:
            p -= 1
            peak_location = sig.find_peaks(X, prominence=p)  # find locations of peaks so we may find

        # frequency! (FREQUENCY IS X DOMAIN)

        # Frequency will be LOW frequency
        Yu_filtered = abs(np.abs(freq[min(peak_location[0]) + 1]))  # For some reason indices seem to be 1 lower?
        # ------------------- Get variables ! -------------------
        fs = 10  # [Hz] Samples collected per second
        ts = 1.0 / fs  # [s] Time step
        N = len(X)  # Number of samples
        f0 = Yu_filtered  # [Hz] Frequency obtained from fourier transform
        D = 1  # [m OR dimensionless] Diameter of Cylinder
        U = 1  # [m/s OR dimensionless] Velocity of Freestream

        # ------------------- Strouhal number Calculation -------------------
        St = f0 * D / U  # [dimensionless] Strouhal Number
        print('Strouhal Number at Probe 1:', St)

        # ------------------- PLOTS -------------------
        plt.figure(figsize=(8, 6))
        plt.plot(t, uy1, 'r')
        plt.ylabel('Velocity (Uy)')
        plt.xlabel('Time')
        plt.title('Uy vs Time Probe 1 ' + file)
        plt.show()

        plt.figure(figsize=(8, 6))
        plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="b")
        plt.xlabel('Freq (Hz)')
        plt.ylabel('FFT Amplitude |X(freq)|')
        plt.title('FFT Plot of Von Karman Vortex Shedding Frequency Probe 1 ' + file)
        plt.xlim(0, max(freq))
        plt.show()

    return


main()
