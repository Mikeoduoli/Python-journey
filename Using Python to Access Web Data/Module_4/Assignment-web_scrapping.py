import urllib.request
from bs4 import BeautifulSoup

# Function to parse HTML and extract numbers
def scrape_and_compute_sum(url):
    # Read HTML from URL
    html = urllib.request.urlopen(url).read()

    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <span> tags with class "comments"
    spans = soup.find_all('span', class_='comments')

    # Extract numbers and compute sum
    total_sum = 0
    for span in spans:
        total_sum += int(span.text)

    return total_sum

# URL for actual data
actual_data_url = "http://py4e-data.dr-chuck.net/comments_1991505.html"

# Compute sum of numbers
sum_of_numbers = scrape_and_compute_sum(actual_data_url)

# Print the sum
print("Sum of numbers:", sum_of_numbers)