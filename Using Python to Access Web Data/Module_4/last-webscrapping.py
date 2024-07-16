import urllib.request
from bs4 import BeautifulSoup

def retrieve_last_name(url, position, repeat):
    for _ in range(repeat):
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        url = links[position - 1].get('href')

    return url.split('_')[-1].split('.')[0]

# URL and parameters for the actual problem
start_url = "http://py4e-data.dr-chuck.net/known_by_Izabel.html"
position = 18
repeat = 7

# Retrieve and report the last name
last_name = retrieve_last_name(start_url, position, repeat)
print("Last name:", last_name)