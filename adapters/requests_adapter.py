import requests
from requests.adapters import HTTPAdapter


class CustomHTTPAdapter(HTTPAdapter):
    def __init__(self, base_url, timeout=None, max_retries=3, *args, **kwargs):
        self.base_url = base_url
        self.timeout = timeout
        super().__init__(max_retries=max_retries, *args, **kwargs)
        self.session = requests.Session()
        self.session.mount("http://", self)
        self.session.mount("https://", self)

    def send(self, request, **kwargs):
        # Apply default timeout if not specified
        if self.timeout is not None and kwargs.get("timeout") is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)

    def _make_url(self, path):
        return f"{self.base_url}{path}"

    def get(self, path, params=None, **kwargs):
        url = self._make_url(path)
        return self.session.get(url, params=params, **kwargs)

    def post(self, path, data=None, json=None, **kwargs):
        url = self._make_url(path)
        return self.session.post(url, data=data, json=json, **kwargs)

    def update(self, path, data=None, json=None, **kwargs):
        url = self._make_url(path)
        return self.session.put(url, data=data, json=json, **kwargs)

    def delete(self, path, **kwargs):
        url = self._make_url(path)
        return self.session.delete(url, **kwargs)
