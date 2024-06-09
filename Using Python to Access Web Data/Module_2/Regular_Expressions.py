# import re
# txt = open('http://py4e-data.dr-chuck.net/regex_sum_1991503.txt')
# txt_count = re.findall('[0-9]+', txt)
# print(txt_count)

import re
import requests

# Fetch the content from the URL
url = 'http://py4e-data.dr-chuck.net/regex_sum_1991503.txt'
response = requests.get(url)
txt = response.text

# Use regular expression to find all numbers in the content
numbers = re.findall('[0-9]+', txt)

# Convert the extracted numbers from strings to integers
numbers = [int(num) for num in numbers]

# Compute the sum of these numbers
total_sum = sum(numbers)

# Print the result
print("Sum:", total_sum)