import requests

# Make an API call for python projects ordered by stars; store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)

print("Status Code: ", response.status_code)

# Store API response in a variable
response_d = response.json()
print("Total Repositories: ", response_d['total_count'])

# Print information from the response
repo_dics = response_d['items']
print("Repositories Returned: ", len(repo_dics))

# Print information from the first repository
repo_dic = repo_dics[0]
print('\nKeys: ', len(repo_dic))
for key in sorted(repo_dic.keys()):
    print(key)

print(response_d.keys())
