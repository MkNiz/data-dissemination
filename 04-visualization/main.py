import csv
from matplotlib import pyplot as plt

# Retrieve highs from file
filename = "../sitka_weather_07-2014.csv"
highs = []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        highs.append(int(row[1]))

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# Format plot
plt.title("Daily High Temps, July 2014", fontsize=22)
plt.xlabel('', fontsize=16)
plt.ylabel("Temp(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
