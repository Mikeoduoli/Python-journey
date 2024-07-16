import json

input = '''[
{ "id" : "001",
  "x" : "2",
  "name" : "Obed"
},
{   "id" : "003",
    "x"  : "16",
    "name" : "Obed"}
]'''

info = json.loads(input)
print('USer count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])