import matplotlib.pyplot as plt
import scipy as sc
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""


signal = np.loadtxt(signal_filepath, skiprows = 2, delimiter = ',')
elapsed_time = signal[: , 0]
MLII = signal[: , 1]
V1 = signal[: , 2]

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""
"""
N = 6
fc = 15
fs = 250
a, b  = sc.signal.butter(N, fc, btype='low', fs=fs )

filtered_data = sc.signal.filtfilt(a, b, V1)

"""

"""
Step 3: Pass data through weighted differentiator
"""

difference = np.diff(V1)


"""
Step 4: Square the results of the previous step
"""
square = np.square(difference)

"""
Step 5: Pass a moving filter over your data
"""

weight = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
moving_average = np.convolve(square, weight)


# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.plot(moving_average)
plt.show()