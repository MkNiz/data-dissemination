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

# Group countries into 3 population levels
pops_sm, pops_md, pops_lg = {}, {}, {}
for cc, pop in cc_pops.items():
    if pop < 10000000:
        pops_sm[cc] = pop
    elif pop < 1000000000:
        pops_md[cc] = pop
    else:
        pops_lg[cc] = pop


# Build and save the world map
wm = World()
wm.title = '2010 World Population (By Country)'
wm.add('0-10m', pops_sm)
wm.add('10m-1b', pops_md)
wm.add('>1bn', pops_lg)

wm.render_to_file('world_pop_2010.svg')
