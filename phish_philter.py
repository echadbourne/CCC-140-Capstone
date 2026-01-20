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
test_word = 'fig'
# Filter Email Entries (csv) for Phishing Indicators
def is_phish():
    pass
# Export filtered entries to new csv
def export_phish():
    pass
# Print summary statistics
def print_summary():
    pass
# Check file extension of input file
def check_extention(expected_extension):
    file_extension = os.path.splitext(file_path)
    return file_extension[1] == expected_extension
def main():
    if check_extention('.csv'):
        test = pd.read_csv(file_path)
    elif check_extention('.xlsx'):
        test = pd.read_excel(file_path)
    else:
        print(f"Invalid file extension.")
        return
    print(test)


if __name__ == "__main__":
    main()