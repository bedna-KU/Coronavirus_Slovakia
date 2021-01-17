#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import sys
import argparse
from datetime import datetime

# Set input args
ap = argparse.ArgumentParser ()
ap.add_argument("-d", "--date", type = str, required = False,
	help = "select date in fomrat year-month-day ex.: 2020-10-01")
ap.add_argument("-c", "--column", type = int, required = True,
	help = "select column")
args = vars(ap.parse_args())

# Args parse
if args["date"]:
    date = args["date"]
column = args["column"]

def get_column(matrix, i):
	return [row[i] for row in matrix]

# Load csv
with open('OpenData_Slovakia_Covid_DailyStats.csv', newline = '') as f:
    reader = csv.reader(f)
    header = next(reader)
    data_list = list(reader)

# Extract date and column
dates = get_column(data_list, 0)
tests = get_column(data_list, column)

if 'date' in globals():
    for i in range(len(dates)):
        if dates[i] == date:
            position = i

# If a date has been entered extract date from this position
if not 'position' in globals():
    position = 0
dates = dates[position :]
tests = tests[position :]

tests_int = []
for i in tests:
    if i == "NA":
        tests_int.append(0)
    else:
        tests_int.append(int(i))

x_min = min(dates)
x_max = max(dates)
y_min = min(tests_int)
y_max = max(tests_int)

# Create datas array for X axis
jump_x = len(dates) // 20
dates_array = np.arange(x_min, x_max, np.timedelta64(jump_x,'D'), dtype='datetime64[D]')

# Numpy dates to list
dates_list = []
for date in dates_array:
    dates_list.append(str(date))

# Change X axis to date format
x = [datetime.strptime(d, '%Y-%m-%d') for d in dates_list]

# Change all values to date format
dates_plt = [datetime.strptime(d, '%Y-%m-%d') for d in dates]

# X axis
ax = plt.subplot()
xfmt = md.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(xfmt)
plt.subplots_adjust(bottom = 0.3)
plt.xticks(x, rotation = -90)

# Y axis
jump_y = y_max // 18
y_ticks = np.arange(0, y_max, jump_y)
plt.yticks(y_ticks)

# Grid
ax.grid(True, linestyle = '-.', color = 'orange')
ax.tick_params(labelcolor = 'black', labelsize = 'medium', width = 3)

# Plot graph
ax.plot(dates_plt, tests_int)
plt.show()