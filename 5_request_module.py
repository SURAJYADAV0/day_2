import requests

# API endpoint URL
url = "http://api.open-notify.org/iss-now.json"

# Send GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Extract latitude, longitude, and timestamp
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']

    # Print the extracted data
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Timestamp:", timestamp)
else:
    print(f"Error: Unable to fetch data, status code {response.status_code}")