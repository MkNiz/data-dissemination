import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Retrieve dates/highs/lows from file
filename = "../sitka_weather_2014.csv"
dates, highs, lows = [], [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        highs.append(int(row[1]))
        lows.append(int(row[3]))

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily High and Low Temps, 2014", fontsize=22)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temp(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
