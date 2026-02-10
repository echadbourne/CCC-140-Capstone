#!/usr/bin/env python3
import os #used to check file extensions
import pandas as pd # used for reading data files

"""
phish_philter.py

# Required Libraries: pandas, openpyxl, os
"""

__version__ = "0.1.0"
file_path = 'PhishPhilterTest.csv'

test_bank = ['Apple', 'Fig', 'Guava']
test_bank2 = ['Cherry', 'Date']
test_bank3 = ['Pear', 'Orange']
# Dictionary of different wordbanks to check against
wordbanks = { 
    'test_bank': {"name": "test_bank", "counter": 0, "words": test_bank},
    'test_bank2': {"name": "test_bank2", "counter": 0, "words": test_bank2},
    'test_bank3': {"name": "test_bank3", "counter": 0, "words": test_bank3}

}


# Checks all the chunks of the Data file for any words in a given word bank and returns the entry
def check_chunk(data, bank):
    #for chunk in data:
    #   in_chunk = chunk[chunk['Fruit'].isin(bank)]
    in_chunk = pd.concat([chunk[chunk['Fruit'].isin(bank)] for chunk in data])
    return in_chunk
# Export filtered entries to new csv
def export_phish(df):
    filename = input("Please enter the name for the new file: ")
    df.to_csv(filename+'.csv')
# Print summary statistics
def print_summary():
    pass
# Uses Pandas to read and objectify given datafile - COMPLETE (MIGHT EXPAND FILE TYPES LATER)
def get_file(file_path):
    if check_extention('.csv'):
        phishData = pd.read_csv(file_path, iterator=True, chunksize=10000)
    else:
        print(f"Invalid file extension.")
    return phishData
# Check file extension of input file
def check_extention(expected_extension):
    file_extension = os.path.splitext(file_path)
    return file_extension[1] == expected_extension

def check_html():
    pass
# Checks all the different Phishing Wordbanks and creates entries for the 
def is_phish(file_path):
    # Reset counts
    # Run the csv file through each wordbank, count the number of hits per bank
    # Export the results of each databank into separate files
    # Print Summary of the results
    counter = 0
    for bank in wordbanks.values():
        table = get_file(file_path)
        bank["counter"] = 0
        print ("Checking the " + bank["name"] + " wordbank...")
        filtered = check_chunk(table, bank["words"])
        bank["counter"] = len(filtered)
        print(bank["counter"])
        export_phish(filtered)
        counter += 1
    
def main():
    is_phish("PhishPhilterTest.csv")
    #print(check_chunk(get_file("PhishPhilterTest.csv"), test_bank))
if __name__ == "__main__":
    main()
