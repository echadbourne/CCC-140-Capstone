#!/usr/bin/env python3
import openpyxl #necessary for Excel file handling
import os #used to check file extensions
import pandas as pd # used for reading data files

"""
phish_philter.py

# Required Libraries: pandas, openpyxl, os
"""

__version__ = "0.1.0"
file_path = 'PhishPhilterTest.csv'
test_word = 'Fig'
# Filter Email Entries (csv) for Phishing Indicators
def is_phish(data, word):
    #filtered_data = data[data['Fruit'] == word]
    in_chunk = pd.concat([chunk[chunk['Fruit'] == word] for chunk in data])
    return in_chunk
# Export filtered entries to new csv
def export_phish():
    pass
# Print summary statistics
def print_summary():
    pass
# Uses Pandas to read and objectify given datafile - COMPLETE (MIGHT EXPAND FILE TYPES LATER)
def get_file(file_path):
    if check_extention('.csv'):
        phishData = pd.read_csv(file_path, iterator=True, chunksize=1000)
    elif check_extention('.xlsx'):
        phishData = pd.read_excel(file_path)
    else:
        print(f"Invalid file extension.")
    return phishData
# Check file extension of input file
def check_extention(expected_extension):
    file_extension = os.path.splitext(file_path)
    return file_extension[1] == expected_extension
def main():
    entry = get_file("PhishPhilterTest.csv")
    print(is_phish(entry,test_word))

if __name__ == "__main__":
    main()