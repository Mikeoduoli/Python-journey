import urllib.request
import urllib.parse
import json
import ssl

# API EndPoint
url_service = 'http://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificates warnings
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    loc_adr = input('Enter Address Location: ')
    if len(loc_adr) < 1:
        break

    loc_adr = loc_adr.strip()
    dict_adr = dict()
    dict_adr['q'] = loc_adr

    url = url_service + urllib.parse.urlencode(dict_adr)

    print('Retrieving', url)
    url_data = urllib.request.urlopen(url, context=ctx)
    data = url_data.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js_data = json.loads(data)
    except:
        js_data = None

    if not js_data or 'features' not in js_data:
        print('----Download Error---')
        print(data)
        break

    if len(js_data['features']) == 0:
        print('----Features Not Found---')
        print(data)
        break

    plus_code = js_data['features'][0]['properties']['plus_code']
    print('Plus code: ', plus_code)
    break
