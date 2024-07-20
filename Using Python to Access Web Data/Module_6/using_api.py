import ssl
import json
import http
import urllib.parse
import urllib.request
{
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature",
         "properties":
            {"datasource":
                {"sourcename": "openstreetmap",
                 "attribution": "© OpenStreetMap contributors",
                 "license": "Open Database License",
                 "url": "https://www.openstreetmap.org/copyright"},
             "country": "United States",
             "country_code": "us",
             "state": "Michigan",
             "county": "Washtenaw County",
             "city": "Ann Arbor",
             "lon": -83.7484616,
             "lat": 42.2813722,
             "state_code": "MI",
             "result_type": "city",
             "formatted": "Ann Arbor, MI, United States of America",
             "address_line1": "Ann Arbor, MI",
             "address_line2": "United States of America",
             "category": "administrative",
             "timezone":
             {"display_name": "America/Detroit",
                    "offset_STD": "-05:00",
                    "offset_STD_seconds": -18000,
                    "offset_DST": "-04:00",
                    "offset_DST_seconds": -14400,
                     "abbreviation_STD": "EST",
                     "abbreviation_DST": "EDT"},
             "plus_code": "86JR77J2+GJ",
             "plus_code_short": "J2+GJ Ann Arbor, Washtenaw County, United States",
             "rank": {"importance": 0.837069344370284,
                      "popularity": 4.698969047117768,
                      "confidence": 1,
                      "confidence_city_level": 1,
                      "match_type": "full_match"},
             "place_id": "51f5937bcbe6ef54c0597580160104244540f00101f901da0f020000000000c00208"},
         "geometry":
            {"type": "Point",
             "coordinates": [-83.7484616, 42.2813722]},
             "bbox": [-83.799572, 42.222668, -83.675807, 42.3238941]}],
    "query": {"text": "Ann Arbor, MI",
              "parsed":
              {"city": "ann arbor", "state": "mi",
               "expected_type": "city"
               }
              }
}


# serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'


# Ignore SS Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'character', data[:20].replace('\n', ' '))

    try:
        js = json.load(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('===Download Error===')
        print(data)
        break

    # print(json.dumps(js, indent=4))

    

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formated']
