import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Obed</name>
    <phone type= "intl">
        +254724681254
    </phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
