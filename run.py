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
        Printing the information of a given record
    """
    print("ID:", record["id"], "Crime:", record["crime"],
          "Number:", record["number"], "Date:", record["date"])
    print("Location:", record["location"])


def get_total_records(records):
    """
        Printing the total number of records in the file
    """
    print("Total number of records in the file:", len(records))


def print_all_records(records):
    """
        Printing all the records in the file
    """
    for record in records:
        print_record(record)


def get_record_by_number(records):
    """
        Print the record related to a user-inputted number
    """
    # Get the number from the user
    number = input("Enter the number: ")

    # Check with every record
    for record in records:
        # If the number is equal, print information
        if record["number"] == number:
            print_record(record)
            return

    print("No matched numbers! Please check again!!")


def get_records_by_date(records):
    """
        Get all the records that have happened on a user-inputted date.
    """
    # Get the date from the user
    date = input("Enter the date (MM/DD/YYYY): ")

    matched_list = []

    # Check with every record
    for record in records:
        if record["date"] == date:
            matched_list.append(record)

    # If no matched record is found
    if len(matched_list) == 0:
        print("There are no matches. Please check the date again!")

    # Print it
    else:
        print("There are", len(matched_list), "number of records")
        confirm = input("Do you want to view all of them? (Y/N): ")

        if confirm.upper() == "Y":
            for record in matched_list:
                print_record(record)

        elif confirm.upper() == "N":
            return

        else:
            print("Invalid input!")



def print_record(record):
    """
    Print the information of a given record.

    Parameters:
        record (dict): a dictionary containing the information of a record.

    Returns:
        None
    """
    print(f"ID: {record['id']}\nCrime: {record['crime']}\nNumber: {record['number']}\nDate: {record['date']}\nLocation: {record['location']}")


def get_total_records(records):
    """
    Print the total number of records in the file.

    Parameters:
        records (list of dict): a list of dictionaries, where each dictionary represents a record.

    Returns:
        None
    """
    print(f"Total number of records in the file: {len(records)}")


def print_all_records(records):
    """
    Print all the records in the file.

    Parameters:
        records (list of dict): a list of dictionaries, where each dictionary represents a record.

    Returns:
        None
    """
    for record in records:
        print_record(record)


def get_record_by_number(records):
    """
    Print the record related to a user inputted number.

    Parameters:
        records (list of dict): a list of dictionaries, where each dictionary represents a record.

    Returns:
        None
    """
    try:
        number = int(input("Enter the number: "))
    except ValueError:
        print("Invalid input! The number must be an integer.")
        return

    for record in records:
        if record["number"] == number:
            print_record(record)
            return

    print("No matched numbers! Please check again!!")


def get_records_by_date(records):
    """
    Get all the records that have happened on a user inputted date.

    Parameters:
        records (list of dict): a list of dictionaries, where each dictionary represents a record.

    Returns:
        None
    """
    date = input("Enter the date (MM/DD/YYYY): ")

    matched_list = []

    for record in records:
        if record["date"] == date:
            matched_list.append(record)

    if len(matched_list) == 0:
        print("There are no matching records! Please check the date again!")
    else:
        print(f"There are {len(matched_list)} number of records")
        confirm = input("Do you want to view all of them? (Y/N))

def print_record(record):
    """
        Print a single record
    """
    print("latitude: ", record["lat"])
    print("longitude: ", record["long"])
    print("crime: ", record["crime"])
    print("date: ", record["date"])
    print("\n")

def get_bar_plot(records):
    """
        Generate bar plot for each crime type
    """

    crime_types = {}

    for record in records:
        crime = record["crime"]
        if crime not in crime_types:
            crime_types[crime] = 1
        else:
            crime_types[crime] += 1

    # plot the bar plot
    plt.bar(crime_types.keys(), crime_types.values(), color="r")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Crime Types")
    plt.ylabel("Number of Crimes")
    plt.title("Number of Crimes by Type")
    plt.show()

def get_records_by_location(records, latitude, longitude):
    """
        Get the records with in a certain latitude and longitude
    """
    latitude = float(latitude)
    longitude = float(longitude)

    matched_records = [record for record in records if (float(record["lat"]) <= latitude + 0.000001 and float(record["lat"]) >= latitude - 0.000001) and (float(record["long"]) <= longitude + 0.000001 and float(record["long"]) >= longitude - 0.000001)]

    if not matched_records:
        print("No matching records found. Please check the latitude and longitude values.")
        return

    print(f"{len(matched_records)} potential records found.")
    confirm = input("Do you want to view all of them? (Y/N) : ")

    if confirm.upper() == "Y":
        for record in matched_records:
            print_record(record)
    elif confirm.upper() != "N":
        print("Invalid input.")

def get_records_by_latitude(records):
    """
        Get the records with in a certain latitude
    """
    latitude = input("Enter the latitude: ")
    longitude = None
    get_records_by_location(records, latitude, longitude)

def get_records_by_longitude(records):
    """
        Get the records with in a certain longitude
    """
    longitude = float(input("Enter the longitude: "))
    latitude = None
    get_records_by_location(records, latitude, longitude)

def run_program():
    # read the filename
    filename = input("Enter the filename: ")

    # read all the records
    records = get_records(filename)

    # run the menu until user exits
    while True:
        # print the menu
        user_input = menu()

        # deal with each case
        if user_input == "1":
            get_total_records(records)

        elif user_input == "2":
            print_all_records(records)

        elif user_input == "3":
            get_record_by_number(records)

        elif user_input == "4":
            get_records_by_date(records)

        elif user_input == "5":
            get_records_related_to_npu(records)

        elif user_input == "6":
            get_number_of_records_related_to_crime_type(records)

        elif user_input == "7":
            get_records_in_a_location(records)

        elif user_input == "8":
            get_bar_plot(records)

        elif user_input == "9":
            get_records_by_latitude(records)

        elif user_input == "10":
            get_records_by_longitude(records)

        elif user_input == "11":
            exit()
            break

        else:
            invalid_input()


if __name__ == "__main__":
    run_program()
