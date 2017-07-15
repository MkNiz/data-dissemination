import json
import pygal
from pygal.maps.world import World

from country_codes import get_country_code
# Load data into a list
filename = '../population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Construct a dictionary holding population data
cc_pops = {}
for pop in pop_data:
    if pop['Year'] == '2010':
        country = pop['Country Name']
        population = int(float(pop['Value']))
        code = get_country_code(country)
        if code:
            cc_pops[code] = population

# Build and save the world map
wm = World()
wm.title = '2010 World Population (By Country)'
wm.add('2010', cc_pops)

wm.render_to_file('world_pop_2010.svg')
