from requests_adapter import CustomHTTPAdapter


class AsaasAPI(CustomHTTPAdapter):
    def __init__(self, base_url, api_key, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)
        self.api_key = api_key

    def _build_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _make_request(self, method, endpoint, **kwargs):
        url = self._make_url(endpoint)
        headers = self._build_headers()
        kwargs["headers"] = headers

        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()

        return response.json()


class Clients(AsaasAPI):
    def list_clients(self, **kwargs):
        return self._make_request("GET", "/clients", params=kwargs)


class Payments(AsaasAPI):
    def list_payments(self, **kwargs):
        return self._make_request("GET", "/payments", params=kwargs)