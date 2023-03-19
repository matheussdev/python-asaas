from adapters.requests_adapter import CustomHTTPAdapter


class AsaasAPI(CustomHTTPAdapter):
    def __init__(self, base_url, api_key, *args, **kwargs):
        super().__init__(base_url, *args, **kwargs)
        self.api_key = api_key

    def _build_headers(self):
        return {
            "access_token": f"{self.api_key}",
            "Content-Type": "application/json",
        }

    def _make_request(self, method, endpoint, params=None, **kwargs):
        if params is None:
            params = {}

        headers = self._build_headers()

        if method == "GET":
            response = self.get(endpoint, params=params, headers=headers,
                                **kwargs)
        elif method == "POST":
            response = self.post(endpoint, json=params, headers=headers,
                                 **kwargs)
        elif method == "PUT":
            response = self.update(endpoint, json=params, headers=headers,
                                   **kwargs)
        elif method == "DELETE":
            response = self.delete(endpoint, headers=headers, **kwargs)
        else:
            raise ValueError(f"Invalid method: {method}")

        response.raise_for_status()
        return response.json()
