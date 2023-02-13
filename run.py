# importing
import numpy as np
import matplotlib.pyplot as plt

def get_records(filename):
    """
        read the file and save all the records in a list.
        the list is a list of dictionaries.
    """

    # list
    records = []

    # open the file
    file = open(filename, "r")
     # read lines
    lines = file.readlines()

    # get all the lines to the list
    for line in lines:
        line = line.strip()
        fields = line.split(",")
        records.append(fields)

    records = records[1:]
  temp = []
    # make all the lines according to the below dictionary
    for record in records:
        my_dict = {
            "id": record[0],
            "crime": record[1],
            "number": record[2],
            "date": record[3],
            "location": record[4],
            "beat": record[5],
            "neighborhood": record[6],
            "npu": record[7],
            "lat": record[8],
            "long": record[9]
        }

        temp.append(my_dict)

    records = temp
    
