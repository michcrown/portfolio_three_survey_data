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
    file = open('altcrime.csv', "r")

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


def get_records_related_to_npu(records):
    """
        Get all the records related to a user inputted NPU.
    """

    npu = input("Enter NPU (Neighboured Police Unit) : ")

    matched_list = []

    # check with every record
    for record in records:
        if record["npu"] == npu:
            matched_list.append(record)

    # if no matched record found
    if len(matched_list) == 0:
        print("There are no any matching! Please check the npu again!")

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


def get_number_of_records_related_to_crime_type(records):
    """
        Get number of related cases for a type of crime
    """

    my_dict = {}

    # save the number of crimes for each type
    for record in records:
        if record["crime"] not in my_dict:
            my_dict[record["crime"]] = 1

        else:
            my_dict[record["crime"]] += 1

    for key in my_dict:
        print(key, ":", my_dict[key])


def get_records_in_a_location(records):
    """
        Get all the records related to a location.
    """

    location = input("Enter the location : ")

    matched_list = []

    for record in records:
        if location.upper() in record["location"]:
            matched_list.append(record)

    if len(matched_list) == 0:
        print("There are no any matching! Please check the location again!")

    else:
        print("There are ", len(matched_list), "number of potential records")
        confirm = input("Do you want to view all of them? (Y/N) : ")

        if confirm.upper() == "Y":
            for record in matched_list:
                print_record(record)

        elif confirm.upper() == "N":
            return

        else:
            print("Invalid input!")


def get_bar_plot(records):
    """
        Generate bar plot for each crime type
    """

    my_dict = {}

    for record in records:
        if record["crime"] not in my_dict:
            my_dict[record["crime"]] = 1

        else:
            my_dict[record["crime"]] += 1

    for key in my_dict:
        print(key, ":", my_dict[key])

    crime_types = list(my_dict.keys())
    crime_values = list(my_dict.values())

    # plot the bar plot
    plt.bar(crime_types, crime_values, color="r")
    plt.xticks(rotation=45, ha='right')

    plt.show()


def get_records_by_latitude(records):
    """
        Get the records with  in a latitude
    """
    latitude = input("Enter the latitude : ")

    matched_list = []

    for record in records:
        if float(latitude)+0.000001 >= float(record["lat"]) and float(latitude)-0.000001 <= float(record["lat"]):
            matched_list.append(record)

    if len(matched_list) == 0:
        print("There are no any matching! Please check the latitude again!")

    else:
        print("There are ", len(matched_list), "number of potential records")
        confirm = input("Do you want to view all of them? (Y/N) : ")

        if confirm.upper() == "Y":
            for record in matched_list:
                print_record(record)

        elif confirm.upper() == "N":
            return

        else:
            print("Invalid input!")


def get_records_by_longitude(records):
    """
        Get the records with  in a longitude
    """
    longitude = input("Enter the latitude : ")

    matched_list = []

    for record in records:
        if float(longitude)+0.000001 >= float(record["long"]) and float(longitude)-0.000001 <= float(record["long"]):
            matched_list.append(record)

    if len(matched_list) == 0:
        print("There are no any matching! Please check the longitude again!")

    else:
        print("There are ", len(matched_list), "number of potential records")
        confirm = input("Do you want to view all of them? (Y/N) : ")

        if confirm.upper() == "Y":
            for record in matched_list:
                print_record(record)

        elif confirm.upper() == "N":
            return

        else:
            print("Invalid input!")


def exit():
    """
        Message to be printed when exiting
    """
    print("Exiting...")


def invalid_input():
    """
        Message to be printed when the user enters invalid input
    """
    print("Invalid user input! Please try again!")


def run_program():

    # read the filename
    filename = input("Enter the filename :\n ")

    # read all the records
    records = get_records(filename)

    # run the menu until user exits
    while True:
        # print the menu
        user_input = menu()

        # deal with each case
        if (user_input == "1"):
            get_total_records(records)

        elif (user_input == "2"):
            print_all_records(records)

        elif (user_input == "3"):
            get_record_by_number(records)

        elif (user_input == "4"):
            get_records_by_date(records)

        elif (user_input == "5"):
            get_records_related_to_npu(records)

        elif (user_input == "6"):
            get_number_of_records_related_to_crime_type(records)

        elif (user_input == "7"):
            get_records_in_a_location(records)

        elif (user_input == "8"):
            get_bar_plot(records)

        elif (user_input == "9"):
            get_records_by_latitude(records)

        elif (user_input == "10"):
            get_records_by_longitude(records)

        elif (user_input == "11"):
            exit()
            break

        else:
            invalid_input()


if __name__ == "__main__":
    # run the program
    run_program()