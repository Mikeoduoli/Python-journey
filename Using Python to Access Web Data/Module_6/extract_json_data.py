import json
import urllib.request as ur

url = input('Enter Location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1991508.json'

print('Retrieving', url)

read_json = ur.urlopen(url)
json_data = read_json.read().decode()

print('Retrieved', len(json_data), 'characters')


json_data = json.loads(json_data)

print(json.dumps(json_data, indent=2))

counts = json_data['comments']
nums = [int(comment['count']) for comment in counts]

print('Count: ', len(nums))
print('Sum: ', sum(nums))