# 0x11. Python - Network #1

## Fetching Internet Resources with urllib

Example:
```
import urllib.request

url = 'https://www.example.com'
response = urllib.request.urlopen(url)

# Read the content of the response
html_content = response.read()

# Decode the content if necessary
decoded_content = html_content.decode('utf-8')

print(decoded_content)
```

## Decoding urllib Body Response

After fetching a resource with \`**urllib**\`, you can decode the response content into a string using the \`**decode()**\` method.

Example:
```
import urllib.request

url = 'https://www.example.com'
response = urllib.request.urlopen(url)

# Read the content of the response as bytes
content_bytes = response.read()

# Decode the bytes into a string using the appropriate character encoding
content_string = content_bytes.decode('utf-8')

print(content_string)
```

## Using the requests Package

The \`**requests**\` library simplifies HTTP requests and provides a more user-friendly interface compared to \`**urllib**\`.

Example:
```
import requests

url = 'https://www.example.com'
response = requests.get(url)

# Print or do something with the content
print(response.text)
```

## Making HTTP GET Request

Fetching a resource using a GET request with the \`**requests**\` library.

Example:
```
import requests

url = 'https://www.example.com'
response = requests.get(url)

if response.status_code == 200:
    print('Request was successful')
    print(response.text)
else:
    print(f'Request failed with status code: {response.status_code}')
```

## Making HTTP POST/PUT/etc. Request

Sending data in POST and PUT requests with the \`**requests**\` library.

Example:
```
import requests

url = 'https://www.example.com/post'
data = {'key1': 'value1', 'key2': 'value2'}

response = requests.post(url, data=data)

if response.status_code == 200:
    print('POST request was successful')
    print(response.text)
else:
    print(f'POST request failed with status code: {response.status_code}')
```

## Fetching JSON Resources

Fetching and decoding JSON resources with the \`**requests**\` library.

Example:
```
import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    print('JSON data:', json_data)
else:
    print(f'Request failed with status code: {response.status_code}')
```

## Manipulating Data from an External Service

Fetching data from an external service, manipulating it, and potentially sending modified data back.

Example:
```
import requests

# Fetch data from an external service
url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Manipulate the data (e.g., filtering, processing)
    modified_data = [item['value'] * 2 for item in data]

    # Send modified data back to the service (if needed)
    update_url = 'https://api.example.com/update'
    update_response = requests.put(update_url, json={'modified_data': modified_data})

    if update_response.status_code == 200:
        print('Data updated successfully')
    else:
        print(f'Update request failed with status code: {update_response.status_code}')
else:
    print(f'Request failed with status code: {response.status_code}')
```
