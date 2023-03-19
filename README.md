# Asaas API Python Client

This Python package provides a simple client for interacting with the Asaas API using custom adapter classes based on the `requests` library.

## Installation

1. Install the `requests` library if you haven't already:

```bash
pip install -r requirements.txt
````

## Usage

First, import the necessary classes:

```python
from python_asaas import AsaasAPI, Clients, Payments
```

Next, create instances of the Clients and Payments classes, passing your Asaas API base URL and API key:
```python
#...
BASE_URL = "https://sandbox.asaas.com/api/v3/" # or https://www.asaas.com/api/v3/
API_KEY = "your_api_key_here"

clients_api = Clients(BASE_URL, API_KEY)
payments_api = Payments(BASE_URL, API_KEY)

```

Now you can use the clients_api and payments_api instances to interact with the Asaas API:

## Clients

List clients
To list clients with optional filters, use the list_clients method:

```python
#...
clients = clients_api.list_clients(name="John Doe", email="john.doe@example.com")
print(clients)

```

## Customization
If you need to add additional endpoints or functionality, you can extend the AsaasAPI class and implement the necessary methods.

## License
This project is released under the MIT License.