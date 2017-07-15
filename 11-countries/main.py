import json

from country_codes import get_country_code
# Load data into a list
filename = '../population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population of each country
for pop in pop_data:
    if pop['Year'] == '2010':
        country = pop['Country Name']
        population = int(float(pop['Value']))
        code = get_country_code(country)
        if code:
            print(code + ": " + str(population))
        else:
            print("ERROR - " + country)
