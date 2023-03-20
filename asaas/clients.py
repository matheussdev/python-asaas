from asaas import AsaasAPI


class Clients(AsaasAPI):
    def list_clients(self, *args, **kwargs):
        return self._make_request("GET", "/customers", params=kwargs)

    def get_client(self, client_id: str):
        return self._make_request("GET", f"/customers/{client_id}")

    def create_client(self, client_data: dict):
        return self._make_request("POST", "/customers", data=client_data)

    def update_client(self, client_id: str, client_data: dict):
        return self._make_request("PUT", f"/customers/{client_id}",
                                  data=client_data)

    def delete_client(self, client_id: str):
        return self._make_request("DELETE", f"/customers/{client_id}")

    def list_client_payments(self, client_id: str):
        return self._make_request("GET", f"/customers/{client_id}/payments")

    def list_client_subscriptions(self, client_id: str):
        return self._make_request("GET",
                                  f"/customers/{client_id}/subscriptions")
