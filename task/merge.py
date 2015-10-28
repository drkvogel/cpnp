#!/usr/bin/python

import csv
import sqlite3



# object for each behavioural episode
# class episode:
#   start, end

def read_files(cam_csv, acc_csv):
    with open(cam_csv, 'rb') as cam_data:
        reader = csv.DictReader(cam_data, delimiter=',', quotechar='"') # unicode_csv_reader()?
        for row in reader: 
            print(row['participant'], row['startTime'])

    with open(acc_csv, 'rb') as acc_data:
        reader = csv.DictReader(acc_data, delimiter=',', quotechar='"') # unicode_csv_reader()?
        for row in reader: 
            print(row['timestamp'], row['acceleration'])

# each behavioural episode will have associated average acceleration data

def save_data():
    # merged information should then be stored in a database of your choosing
    sqlite_file = '/home/kvogel/Projects/cpnp/wearables.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()


if __name__ == '__main__': # running standalone
    ins = True
    while ins:
        print("""
        1. Merge raw data
        2. Query merged data
        3. something else
            """)
        ins = raw_input("Enter a number or q to quit: ") # http://stackoverflow.com/questions/4915361/whats-the-difference-between-raw-input-and-input-in-python3-x
        if ins == "1":
            print("Merge raw data")
        elif ins == "2":
            print("Query merged data")
        elif ins == "3":
            print("Do something else")
        elif ins == "q":
            exit()
        else:
            print("Try again")

    cam_csv = 'p325Camera.csv'
    acc_csv = 'p325Accelerometer.csv'
    read_files(cam_csv, acc_csv)



# script should support subsequent querying of the database to describe the average acceleration associated with each behaviour type




"""
p325Accelerometer.csv
timestamp,          acceleration,   xRange,     yRange,     zRange,     xStd,       yStd,       zStd,       temp,   samples,    dataErrors, clipsBeforeCalibr,  clipsAfterCalibr
03/11/2014 15:26,   0.073449,       2.349882,   2.480954,   3.17729,    0.336255,   0.312917,   0.268746,   19.85,  490,        0,          0,                  0

p325Camera.csv
participant,    startTime,          endTime,            source,     annotations(comma-separated)
p325,           04/11/2014 07:15,   04/11/2014 07:15,   images,     home activity;miscellaneous;standing;9070 standing reading or without obvious activities
"""

# Faster code via static typing (Cython): http://docs.cython.org/src/quickstart/cythonize.html
# http://programmers.stackexchange.com/questions/59606/is-type-safety-worth-the-trade-offs









# cruft

"""
with open('p325Accelerometer.csv', 'rb') as csvfile:
    # reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    # for row in reader:
    #     print '\t '.join(row)
    try:
	    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"') # unicode_csv_reader()?
	    for row in reader:
	        #print '\t '.join(row)
	        print(row['timestamp'], row['acceleration'])
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
"""