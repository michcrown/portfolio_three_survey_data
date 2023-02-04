import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pip install pandas
pip install numpy
pip install matplotlib

# function to read the data from the file
def import_survey_results(file_path):

    data = pd.read_csv(file_path)
    return data

# function to analyse survey data in a basic way
def analyze_survey_data(data):
   
    mean = np.mean(data)
    median = np.median(data)
    mode = stats.mode(data)
    std_dev = np.std(data)
   
    print("Mean: ", mean)
    print("Median: ", median)
    print("Mode: ", mode)
    print("Standard Deviation: ", std_dev)
    
   
    plt.hist(data)
    plt.show()
    
    key_findings = "The survey results show a mean of {} with a median of {} and a mode of {}. The standard deviation is {}.".format(mean, median, mode, std_dev)
    print(key_findings)
    return key_findings


