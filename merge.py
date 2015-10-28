#!/usr/bin/python

import os
import sys
import csv
import sqlite3
#import pandas
#import pylab

# object for each behavioural episode
# each behavioural episode will have associated average acceleration data
class episode:
    def __init__():
        self.start  = 0
        self.end    = 0

def read_files(cam_csv, acc_csv):
    episodes = {}
    with open(cam_csv, 'rb') as cam_data:
        cam_reader = csv.DictReader(cam_data, delimiter=',', quotechar='"') # unicode_csv_reader()?
        print("importing camera data")
        for row in cam_reader: 
            sys.stdout.write('.')
            #print(row['participant'], row['startTime'])

    with open(acc_csv, 'rb') as acc_data:
        acc_reader = csv.DictReader(acc_data, delimiter=',', quotechar='"') # unicode_csv_reader()?
        print("importing accelerometer data")
        for row in acc_reader: 
            sys.stdout.write('.')
            #print(row['timestamp'], row['acceleration'])

def save_data():
    # merged information should then be stored in a database of your choosing
    sqlite_file = './wearables.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    print("TODO")
    exit()

def query():
    # script should support subsequent querying of the database to describe the average acceleration associated with each behaviour type
    print("TODO")
    exit()

if __name__ == '__main__': # running standalone
    ins = True
    clear = lambda : os.system('clear')
    while ins:
        clear()
        print("""
        1. Merge raw data
        2. Query merged data
            """)
        ins = raw_input("Enter a number or q to quit: ") # http://stackoverflow.com/questions/4915361/whats-the-difference-between-raw-input-and-input-in-python3-x
        if ins == "1":
            print("Merge raw data")
            cam_csv = 'p325Camera.csv'
            acc_csv = 'p325Accelerometer.csv'
            read_files(cam_csv, acc_csv)
        elif ins == "2":
            print("Query merged data")
            query()
        elif ins == "q":
            exit()
        else:
            print("Try again")







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