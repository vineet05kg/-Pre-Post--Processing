##############################################################################################################
#                                     GAUSSIAN DISTRIBUTION PROGRAM                                          #
##############################################################################################################

##############################################################################################################
#          To plot the Gaussian curve of different sampling rate CSV file based on the outcome of            #
#          statistical parameters of same...                                                                 #
##############################################################################################################

# To call the different related libraries required for the program//
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##############################################################################################################
# To locate and read the files//

csvfile_location_1 = (r'D:/Python/VacuumData_Analysis/ForAcquired_Date[18.Dec.2019]viaAPD/1MSas/NoiseFree '
                      r'RawData(1MSas)Set1.csv')
csvfile_location_2 = (r'D:/Python/VacuumData_Analysis/ForAcquired_Date[18.Dec.2019]viaAPD/2.5MSas/NoiseFree'
                      r' RawData(2.5MSas)Set1.csv')
csvfile_location_3 = (r'D:/Python/VacuumData_Analysis/ForAcquired_Date[18.Dec.2019]viaAPD/3.15MSas/NoiseFree'
                      r' RawData(3.15MSas)Set1.csv')
csvfile_location_4 = (r'D:/Python/VacuumData_Analysis/ForAcquired_Date[18.Dec.2019]viaAPD/6.25MSas/NoiseFree'
                      r' RawData(6.25MSas)Set1.csv')
csvfile_location_5 = (r'D:/Python/VacuumData_Analysis/ForAcquired_Date[18.Dec.2019]viaAPD/10MSas/NoiseFree'
                      r' RawData(10MSas)Set1.csv')

csvfile_read_1 = pd.read_csv(csvfile_location_1)
csvfile_read_2 = pd.read_csv(csvfile_location_2)
csvfile_read_3 = pd.read_csv(csvfile_location_3)
csvfile_read_4 = pd.read_csv(csvfile_location_4)
csvfile_read_5 = pd.read_csv(csvfile_location_5)

# To print the first ten elements of all the columns of CSV files//
print("First 10 elements of all the columns of data file =", csvfile_read_1.head(10))
print("First 10 elements of all the columns of data file =", csvfile_read_2.head(10))
print("First 10 elements of all the columns of data file =", csvfile_read_3.head(10))
print("First 10 elements of all the columns of data file =", csvfile_read_4.head(10))
print("First 10 elements of all the columns of data file =", csvfile_read_5.head(10))

#############################################################################################################
print ('########################################################################################')
print ('#########   To determine the statistical Values of the Different Sampled File  #########')
print ('########################################################################################')

# To determine the minimum values of the CSV data files//
csvfile_min_1 = csvfile_read_1.min()
print ('Min. value of the CSV data file1: '+ str(csvfile_min_1[0]))
csvfile_min_2 = csvfile_read_2.min()
print ('Min. value of the CSV data file2: '+ str(csvfile_min_2[0]))
csvfile_min_3 = csvfile_read_3.min()
print ('Min. value of the CSV data file3: '+ str(csvfile_min_3[0]))
csvfile_min_4 = csvfile_read_4.min()
print ('Min. value of the CSV data file4: '+ str(csvfile_min_4[0]))
csvfile_min_5 = csvfile_read_5.min()
print ('Min. value of the CSV data file5: '+ str(csvfile_min_5[0]))

# To determine the maximum values of the CSV data files//
csvfile_max_1 = csvfile_read_1.max()
print ('Max value of the CSV data file1: '+ str(csvfile_max_1[0]))
csvfile_max_2 = csvfile_read_2.max()
print ('Max value of the CSV data file2: '+ str(csvfile_max_2[0]))
csvfile_max_3 = csvfile_read_3.max()
print ('Max value of the CSV data file3: '+ str(csvfile_max_3[0]))
csvfile_max_4 = csvfile_read_4.max()
print ('Max value of the CSV data file4: '+ str(csvfile_max_4[0]))
csvfile_max_5 = csvfile_read_5.max()
print ('Max value of the CSV data file5: '+ str(csvfile_max_5[0]))

# To determine the mean values of the CSV data file//
csvfile_mean_1 = csvfile_read_1.mean()
print ('Mean value of the CSV data file1: '+ str(csvfile_mean_1[0]))
csvfile_mean_2 = csvfile_read_2.mean()
print ('Mean value of the CSV data file2: '+ str(csvfile_mean_2[0]))
csvfile_mean_3 = csvfile_read_3.mean()
print ('Mean value of the CSV data file3: '+ str(csvfile_mean_3[0]))
csvfile_mean_4 = csvfile_read_4.mean()
print ('Mean value of the CSV data file4: '+ str(csvfile_mean_4[0]))
csvfile_mean_5 = csvfile_read_5.mean()
print ('Mean value of the CSV data file5: '+ str(csvfile_mean_5[0]))

# To determine the standard deviation values of the CSV data files//
csvfile_std_1 = csvfile_read_1.std()
print ('Standard deviation of the CSV data file1: '+ str(csvfile_std_1[0]))
csvfile_std_2 = csvfile_read_2.std()
print ('Standard deviation of the CSV data file2: '+ str(csvfile_std_2[0]))
csvfile_std_3 = csvfile_read_3.std()
print ('Standard deviation of the CSV data file3: '+ str(csvfile_std_3[0]))
csvfile_std_4 = csvfile_read_4.std()
print ('Standard deviation of the CSV data file4: '+ str(csvfile_std_4[0]))
csvfile_std_5 = csvfile_read_5.std()
print ('Standard deviation of the CSV data file5: '+ str(csvfile_std_5[0]))

'''
    For reference related to this program check the mentioned URL's attached herein below:
    https://www.science-emergence.com/Articles/How-to-plot-a-normal-distribution-with-matplotlib-in-python-/
    https://machinelearningmastery.com/quick-and-dirty-data-analysis-with-pandas/
    https://realpython.com/python-histograms/
    https://codefellows.github.io/sea-python-401d2/lectures/stats_day2.html

'''
#############################################################################################################
print ('########################################################################################')
print ('###########   To Plot the Gaussian Distribtuion on the CSV Data based Files   ##########')
print ('########################################################################################')

# To define the function over different variables//
def gaussian(x, mean, std):
    return (1/ np.sqrt(2 * np.pi * std**2)* np.exp(-0.5 *((x - mean)/ std)**2)) # The same defined function
    # will work for each of the different CSV files//

# To define the range between which the gaussian curve will plot, i.e. from -0.25 to +0.25, with total count
# same as of the data file counts//
x1 = np.linspace(-0.25, 0.25, int(csvfile_read_1.count()))
x2 = np.linspace(-0.25, 0.25, int(csvfile_read_2.count()))
x3 = np.linspace(-0.25, 0.25, int(csvfile_read_3.count()))
x4 = np.linspace(-0.25, 0.25, int(csvfile_read_4.count()))
x5 = np.linspace(-0.25, 0.25, int(csvfile_read_5.count()))

w = 5.0 
h = 4.0
d = 70 
plt.figure(figsize=(w, h), dpi=d) # To plot the figure//
plt.subplots_adjust(left=0.155)
plt.subplots_adjust(bottom=0.15)
plt.plot(x1, gaussian(x1, csvfile_mean_1[0], csvfile_std_1[0]), color='blue', label="1MSa/s")
plt.plot(x2, gaussian(x2, csvfile_mean_2[0], csvfile_std_2[0]), color='coral', label="2.5MSa/s")
plt.plot(x3, gaussian(x3, csvfile_mean_3[0], csvfile_std_3[0]), color='red', label="3.15MSa/s")
plt.plot(x4, gaussian(x4, csvfile_mean_4[0], csvfile_std_4[0]), color='cyan', label="6.25MSa/s")
plt.plot(x5, gaussian(x5, csvfile_mean_5[0], csvfile_std_5[0]), color='magenta', label="10MSa/s")
plt.xlabel("$x$", fontsize=16)
plt.ylabel("$p(x)$", fontsize=16)
plt.legend()
plt.grid('on')
plt.show()
