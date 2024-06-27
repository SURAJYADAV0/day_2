import requests

# API endpoint URL
url = "http://api.open-notify.org/iss-now.json"

# Send GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the JSON response
    print("JSON Response:")
    print(response.json())
else:
    print(f"Error: Unable to fetch data, status code {response.status_code}")