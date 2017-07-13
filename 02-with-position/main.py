import csv

filename = "../sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for idx, column_header in enumerate(header_row):
        print(idx, column_header)
