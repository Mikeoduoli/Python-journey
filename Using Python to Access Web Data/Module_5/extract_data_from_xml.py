import xml.etree.ElementTree as ET
import urllib.request as ur

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1991507.xml'

print('Retrieving', url)
read_url = ur.urlopen(url)
data = read_url.read()

print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')

nums = [int(count.text) for count in counts]

print('Count: ', len(nums))
print('Sum: ', sum(nums))
