# 0x10. Python - Network #0
## URL (Uniform Resource Locator)
A URL, or Uniform Resource Locator, is a reference or address used to access resources on the internet. It consists of several components:

## Reading a URL:
A URL typically follows the format:

```
scheme://domain:port/path?query#fragment
```
- **Scheme**: Specifies the protocol used (e.g., HTTP, HTTPS).
- **Domain**: Identifies the server hosting the resource.
- **Port**: Specifies the network port on the server.
- **Path**: Specifies the location of the resource on the server.
- **Query**: Contains parameters for the resource.
- **Fragment**: Points to a specific section within the resource.

## HTTP (Hypertext Transfer Protocol)
HTTP is a protocol used for communication between web browsers and servers. It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.

## HTTP URL Scheme:
The scheme for an HTTP URL is usually **\`http\`** or **\`https\`** for secure connections.

## Domain and Sub-Domain
- **Domain Name**: A human-readable label assigned to an IP address, identifying a server on the internet.
- **Sub-Domain**: A subdivision of a domain, allowing for additional categorization or organization of resources.

## Port Number in a URL
Port numbers are optional in a URL and are specified after the domain, separated by a colon. The default HTTP port is 80, and HTTPS is 443.

## Query String
A query string appears after the path in a URL, separated by a question mark (**\`?\`**). It contains key-value pairs used to pass data to the server.

## HTTP Request and Response
- **HTTP Request**: An action performed by a client to retrieve or send data from/to a server.
- **HTTP Response**: The server's reply to an HTTP request, containing the requested data or an error message.

## HTTP Headers
Headers provide additional information about the request or response, including content type, caching directives, authentication, etc.

## HTTP Message Body
The message body carries data in an HTTP request or response. In POST requests, it often contains form data or JSON payloads.

## HTTP Request Method
Request methods define the action the client wants to perform. Common methods include GET, POST, PUT, DELETE, etc.

## HTTP Response Status Code
Status codes indicate the result of an HTTP request. Examples include 200 OK, 404 Not Found, and 500 Internal Server Error.

## HTTP Cookie
A small piece of data stored on the client-side, sent by the server, and included in subsequent requests. Cookies are used for session management, tracking, and personalization.

## Making a Request with cURL
cURL is a command-line tool for making HTTP requests. Example:
```
curl -X GET https://example.com/resource
```

## Browser Behavior
When you type "google.com" in your browser:

1. The browser sends an HTTP request to the DNS server to resolve the domain.
2. The DNS server returns the IP address of the server hosting Google.
3. The browser sends an HTTP request to that IP, asking for the Google homepage.
4. The server responds with the HTML content of the Google homepage.
5. The browser renders and displays the page.

Understanding these fundamentals is crucial for anyone working with web technologies and helps in developing a deeper understanding of how data is transferred and resources are accessed on the internet.