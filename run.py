import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pip install pandas
pip install numpy
pip install matplotlib

# function to read the data from the file - 1
def import_survey_results(file_path):

    data = pd.read_csv(file_path)
    return data

# function to analyse survey data in a basic way - 2
# will need more detail - maybe on what information this parses? 
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

# write the data to a CSV file using pandas - 3
# maybe will need to be able "appropriate file" - maybe need PDF's too?
def export_results(data, file_path):
    data.to_csv(file_path, index=False)
    print("Results exported successfully to", file_path)




###The application should provide actionable insights from an inputted dataset. - actionable?

###Import survey results from the terminal, structured data file or similar. - function 1
###Parse and analyse the data - function 2
###Export the results to an appropriate file - function 3
