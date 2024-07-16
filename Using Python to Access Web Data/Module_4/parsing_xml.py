import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
        <phone type="intl">
            +254 724 681 254
        </phone>
    <email hide="Yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
