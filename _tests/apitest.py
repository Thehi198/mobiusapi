import requests

url = "http://127.0.0.1:8000/api/server/query"  # Replace with your server URL

# Define the JSON request body
request_body = {
    "name": "your_index_name"
}

response = requests.post(url, json=request_body)

# Print the response from the server
print(response.status_code)
print(response.json())