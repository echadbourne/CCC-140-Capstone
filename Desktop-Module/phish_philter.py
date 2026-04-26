#!/usr/bin/env python3
import os #used to check file extensions
import pandas as pd # used for reading data files
import sys
import requests
import json

"""
phish_philter.py

# Required Libraries: pandas, openpyxl, os
"""

__version__ = "0.1.0"

#test_bank = ['Apple', 'Fig', 'Guava']
#test_bank2 = ['Cherry', 'Date']
#test_bank3 = ['Pear', 'Orange']

# Dictionary of different wordbanks to check against
wordbanks = { 
 #   'test_bank': {"name": "test_bank", "counter": 0, "words": test_bank},
 #   'test_bank2': {"name": "test_bank2", "counter": 0, "words": test_bank2},
 #   'test_bank3': {"name": "test_bank3", "counter": 0, "words": test_bank3},
}
labels = []

# Checks all the chunks of the Data file for any words in a given word bank and returns the entry
def check_chunk(data, bank, label):
    if label in data.get_chunk(0).columns.tolist():
        in_chunk = pd.concat([chunk[chunk[label].str.contains('|'.join(bank))] for chunk in data])
        return in_chunk
    else:
        print(f"Label '{label}' not found in the data. Skipping this label...")
    
# Export filtered entries to new csv
def export_phish_csv(df):
    filename = input("Please enter the name for the new file: ")
    df.to_csv(filename+'.csv')
# Export filtered entries to local CouchDB database
def export_phish_db(df):
    df = df.drop_duplicates()
    result = df.reset_index().to_json(force_ascii=False)
    print(result)
    response = requests.post("http://phish:philter@localhost:5984/phishphilter", data=result.encode('utf-8'), headers={'Content-Type': 'application/json'})
    print(response.json())
# Print summary statistics
def print_summary():
    total = 0
    for bank in wordbanks.values():
        print("Number of hits in " + bank["name"] + ": " + str(bank["counter"]))
        total += bank["counter"]
    print("Total hits across all wordbanks: " + str(total))
    for bank in wordbanks.values():
        percentage = (bank["counter"] / total) * 100 if total > 0 else 0
        print(f"Percentage of hits in {bank['name']}: {percentage:.2f}%")
# Prints PhishPhilter Version
def print_version():
    print(f"Phish Philter Version: {__version__}")
# Imports a wordbank from a .txt file and adds it to the wordbanks dictionary
def import_wordbank(file_path):
    global wordbanks
    if check_extention(file_path, '.txt'):
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split(',')
        for word in words:
            wordbanks[file_path] = {"name": file_path, "counter": 0, "words": words}
        export_wordbank_json()
# Imports wordbanks from a .json file and adds them to the wordbanks dictionary
def import_wordbank_json():
    global wordbanks
    with open('Desktop-Module\\wordbanks.json', 'r') as file:
        wordbanks = json.load(file)
# Exports wordbanks to a .json file
def export_wordbank_json():
    global wordbanks
    with open('Desktop-Module\\wordbanks.json', 'w') as file:
        json.dump(wordbanks, file)
# Imports labels from a .json file
def import_labels_json():
    global labels
    with open('Desktop-Module\\labels.json', 'r') as file:
        labels = json.load(file)
# Exports labels to a .json file
def export_labels_json():
    global labels
    with open('Desktop-Module\\labels.json', 'w') as file:
        json.dump(labels, file)
# Uses Pandas to read and objectify given datafile - COMPLETE (MIGHT EXPAND FILE TYPES LATER)
def get_file(file_path):
    if check_extention(file_path,'.csv'):
        phishData = pd.read_csv(file_path, iterator=True, chunksize=10000)
    else:
        print("Unsupported file type. Please provide a .csv file.")
        exit()
    return phishData
# Check file extension of input file
def check_extention(file_path, expected_extension):
    file_extension = os.path.splitext(file_path)
    return file_extension[1] == expected_extension


# Checks all the different Phishing Wordbanks and creates entries for the 
def is_phish(file_path):
    # Reset counts
    # Run the csv file through each wordbank, count the number of hits per bank
    # Export the results of each databank into separate files
    # Print Summary of the results
    counter = 0
    global labels
    global wordbanks
    for bank in wordbanks.values():
        temp = []
        hold = None
        bank["counter"] = 0
        print ("Checking the " + bank["name"] + " wordbank...")
        for label in labels:
            table = get_file(file_path)
            hold = check_chunk(table, bank["words"], label)
            if hold is not None:
                temp.append(hold)
        filtered = pd.concat(temp)
        print(filtered)
        bank["counter"] = len(filtered)
        print("Number of hits in " + bank["name"] + ": " + str(bank["counter"]))
        export_phish_db(filtered)
        counter += 1
    #print_summary()


if __name__ == "__main__":
    #is_phish("Desktop-Module\\emails.csv") # Run check against the test file
    #is_phish("Desktop-Module\\PhishPhilterTest.csv")
    import_wordbank_json() # Import wordbanks from json file
    import_labels_json() # Import labels from json file
    is_phish(sys.argv[1]) # Run check against whatever is after it
