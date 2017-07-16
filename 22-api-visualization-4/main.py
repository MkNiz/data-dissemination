import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call for python projects ordered by stars; store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)

print("Status Code: ", response.status_code)

# Store API response in a variable
response_d = response.json()
repo_dics = response_d['items']

# Retrieve information from the repositories
names, plot_dics = [], []
for repo_dic in repo_dics:
    names.append(repo_dic['name'])
    plot_dic = {
        'value': repo_dic['stargazers_count'],
        'label': str(repo_dic['description']),
        'xlink': repo_dic['html_url']
    }
    plot_dics.append(plot_dic)

# Create visualization
style = LS('#333366', base_style=LCS)

cfg = pygal.Config()
cfg.x_label_rotation = 45
cfg.show_legend = False
cfg.title_font_size = 42
cfg.label_font_size = 14
cfg.major_label_font_size = 18
cfg.truncate_label = 15
cfg.show_y_guides = False
cfg.width = 1000

chart = pygal.Bar(cfg, style=style)
chart.title = 'Python Projects with Most Stars on GitHub'
chart.x_labels = names

chart.add('', plot_dics)
chart.render_to_file('python_stars.svg')
