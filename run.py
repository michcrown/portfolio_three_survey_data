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

    # return the list of records
    return records


def menu():
    """
        print the menu to the user
    """
    print("\nPlease select option :")
    print(" 1 : Get total records")
    print(" 2 : Print all the records")
    print(" 3 : Get record by number")
    print(" 4 : Get record by date")
    print(" 5 : Get records related to the npu")
    print(" 6 : Get number of types of records")
    print(" 7 : Get records in a location")
    print(" 8 : Get Bar Plot for crime types")
    print(" 9 : Get Records by latitude")
    print(" 10 : Get Records by longitude")
    print(" 11 : Exit")

    # get the user input
    user_input = input("\nChoose your option : ")

    return user_input


def print_record(record):
    """
        printing the information of a give record
    """
    print("ID :", record["id"], "Crime :", record["crime"],
          "Number :", record["number"], "Date :", record["date"], end="")
    print("Location :", record["location"], "Beat :", record["beat"],
          "Neighborhood :", record["neighborhood"], "Npu :", record["npu"], "Latitude :", record["lat"], "Longitude :", record["long"])
  
def get_total_records(records):
    """
        printing the total number of records in the file
    """
    print("Total number of records in the file :", len(records))


def print_all_records(records):
    """
        printing all the records in the file
    """

    for record in records:
        print(record)
def get_record_by_number(records):
    """
        print the record related to a user inputted number
    """

    # get the number from the user
    number = input("Enter the number : ")

    # check with every record
    for record in records:

        # if the number is equal, print information
        if record["number"] == number:
            print_record(record)

            return

    print("No matched numbers! Please check again!!")

def get_records_by_date(records):
    """
        Get all the records that has happned in a user inputted date.
    """

    # get the date from the user
    date = input("Enter the date (MM/DD/YYYY) : ")

    matched_list = []

    # check with every record
    for record in records:
        if record["date"] == date:
            matched_list.append(record)

    # if no matched record found
    if len(matched_list) == 0:
        print("There are no any matching! Please check the date again!")

    # print it
    else:
        print("There are ", len(matched_list), "number of records")
        confirm = input("Do you want to view all of them? (Y/N) : ")

        if confirm.upper() == "Y":
            for record in matched_list:
                print_record(record)

        elif confirm.upper() == "N":
            return

        else:
            print("Invalid input!")
