import requests

from operator import itemgetter

# Make a call to the API; store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Status Code: ", r.status_code)

# Process submission information
sub_ids = r.json()
sub_dics = []
for sub_id in sub_ids[:30]:
    # Make individual calls for details
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(sub_id) + '.json')
    sub_r = requests.get(url)
    print("Sub ID#" + str(sub_id) + ": " + str(sub_r.status_code))
    resp_dic = sub_r.json()

    sub_dic = {
        'title': resp_dic['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(sub_id),
        'comments': resp_dic.get('descendants', 0)
    }
    sub_dics.append(sub_dic)

sub_dics = sorted(sub_dics, key=itemgetter('comments'), reverse=True)

for sub_dic in sub_dics:
    print('\nTitle: ', sub_dic['title'])
    print('Discussion Link: ', sub_dic['link'])
    print('Comments: ', sub_dic['comments'])
