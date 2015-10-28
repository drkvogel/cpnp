#!/usr/bin/python

import csv
import sqlite3



# object for each behavioural episode
# class episode:
#   start, end

if __name__ == '__main__': # running standalone
    ins = True
    while ins:
        print("""
        1. something
        2. something
        3. something else
            """)
        ins = input("Enter a number or press Enter to quit")
        if ins == "1":
            print("Do something")
        if ins == "2":
            print("Do something")
        if ins == "3":
            print("Do something else")

def read_files():
    with open('p325Camera.csv', 'rb') as cam_csv:
        reader = csv.DictReader(cam_csv, delimiter=',', quotechar='"') # unicode_csv_reader()?
        for row in reader: 
            print(row['participant'], row['startTime'])

    with open('p325Accelerometer.csv', 'rb') as acc_csv:
        reader = csv.DictReader(acc_csv, delimiter=',', quotechar='"') # unicode_csv_reader()?
        for row in reader: 
            print(row['timestamp'], row['acceleration'])

# each behavioural episode will have associated average acceleration data

def save_data():
    # merged information should then be stored in a database of your choosing
    sqlite_file = '/home/kvogel/Projects/cpnp/wearables.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()


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