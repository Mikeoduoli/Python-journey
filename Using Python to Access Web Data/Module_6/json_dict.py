import json

data = '''{
"name" : "Obed",
"phone" : {
"type" : "intl",
"number" : "+254724 681 254"},
"email" : {
    "hide" : "yes"}
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
