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

# Print information from the repositories
for idx, repo_dic in enumerate(repo_dics):
    print("\nSummary of Repository #", idx+1, ":")
    print("Name: ", repo_dic['name'])
    print("Owner: ", repo_dic['owner']['login'])
    print("Stars: ", repo_dic['stargazers_count'])
    print("Repository: ", repo_dic['html_url'])
    print("Created: ", repo_dic['created_at'])
    print("Updated: ", repo_dic['updated_at'])
    print("Description: ", repo_dic['description'])
