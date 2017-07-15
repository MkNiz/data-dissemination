import json

# Load data into a list
filename = '../population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population of each country
for pop in pop_data:
    if pop['Year'] == '2010':
        print(pop['Country Name'] + ": " + pop['Value'])
