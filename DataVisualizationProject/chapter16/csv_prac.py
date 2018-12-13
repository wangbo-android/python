import csv
import matplotlib.pyplot as pl
from datetime import datetime


filename = 'death_valley_2014.csv'
# with open(filename) as csv_file:
#     contents = csv_file.readlines()
#     print(contents)
#
#     for line in contents:
#         print(line)

with open(filename) as csv_files:
    reader = csv.reader(csv_files)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
fig = pl.figure(dpi=128, figsize=(10, 6))
pl.plot(dates, highs, c='red')
pl.plot(dates, lows, c='blue')
pl.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
fig.autofmt_xdate()
pl.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
pl.xlabel('', fontsize=16)
pl.ylabel('Temperature(F)', fontsize=16)
pl.tick_params(axis='both', which='major', labelsize=16)
pl.savefig('temperature.png', bbox='tight')
pl.show()
# first_date = dt.datetime('2014-1-1', '%Y-%m-%d')
# print(first_date)
