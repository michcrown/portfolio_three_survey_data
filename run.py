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



