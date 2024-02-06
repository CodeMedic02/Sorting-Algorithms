# Name: Trent Adams
# Date: 2024-01-28

import time
from datetime import date
import csv
from Client import Client

# Import your sorting modules
from BubbleSort import BubbleSort
from InsertionSort import InsertionSort
from MergeSort import MergeSort
from Quicksort import Quicksort
from SelectionSort import SelectionSort
from ShellSort import ShellSort


print("Name: ", "Trent Adams")
print("Date: ", date.today())
print()

input_file_name = 'ClientData100.csv'
# input_file_name = 'ClientData1000.csv'
# input_file_name = 'ClientData10000.csv'
# input_file_name = 'ClientData100000.csv'


clients = []  # Ensure this is defined before the loop


# Function to read data from CSV file.
def read_csv(csv_file):

   with open(csv_file) as infile:
    for line in infile:
        fileData = line.split(',')
        client_id = int(fileData[0])  # Convert to integer.
        f_name = fileData[1]
        l_name = fileData[2]
        phone = fileData[3]
        email = fileData[4]

        # Create client objects using the data from the file.
        clientObject = Client(client_id, f_name, l_name, phone, email)

        # Add client objects to list
        clients.append(clientObject)


def test_sort_performance(sort_function, data):
    # Function to test and time the sorting performance
    start_time = time.time()
    sorted_data = sort_function(data)
    end_time = time.time()
    return end_time - start_time


def main():
    read_csv(input_file_name)


    # Testing BubbleSort
    print("Testing BubbleSort...")
    time_taken = test_sort_performance(BubbleSort.sort, clients)
    print(f"BubbleSort took {time_taken} seconds to sort {len(clients)} records")

    # Display sorted list
    for clt in clients:
        print(clt)

    # Testing SelectionSort
    # print("Testing SelectionSort...")
    # time_taken = test_sort_performance(SelectionSort.sort, clients)
    # print(f"SelectionSort took {time_taken} seconds")
    #
    # for clt in clients:
    #     print(clt)
    
    # # Testing ShellSort
    # print("Testing ShellSort...")
    # time_taken = test_sort_performance(ShellSort.sort, clients)
    # print(f"ShellSort took {time_taken} seconds")

    # for clt in clients:
    #    print(clt)

    # Testing InsertionSort
    # print("Testing InsertionSort...")
    # time_taken = test_sort_performance(InsertionSort.sort, clients)
    # print(f"InsertionSort took {time_taken} seconds to insert {len(clients)} records")
    # Display sorted list
    # for clt in clients:
        # print(clt)

    # Testing QuickSort
    # print("Testing Quicksort...")
    # time_taken = test_sort_performance(Quicksort.sort, clients)
    # print(f"Quicksort took {time_taken} seconds")
    #
    # for clt in clients:
    #     print(clt)

    # Testing MergeSort
    # print("Testing MergeSort...")
    # time_taken = test_sort_performance(MergeSort.sort, clients)
    # print(f"MergeSort took {time_taken} seconds")
    #
    # for clt in clients:
    #     print(clt)


if __name__ == "__main__":
    main()
    