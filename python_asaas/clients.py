from python_asaas import AsaasAPI


class Clients(AsaasAPI):
    def list_clients(self, *args, **kwargs):
        return self._make_request("GET", "/customers", params=kwargs)
