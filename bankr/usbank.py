import requests, json, uuid
from loguru import logger as log
from bankr.config import API_TOKEN, API_SECRET, API_AUTH_URL, API_BASE_URL


class USBank:
    def __init__(self):
        pass

    def _generate_oauth_token(self) -> str:
        """Generate a new OAuth token for the API."""
        return json.loads(
            requests.post(
                API_AUTH_URL,
                data={"grant_type": "client_credentials"},
                allow_redirects=False,
                auth=(API_TOKEN, API_SECRET),
            ).text
        ).get("accessToken")

    def _get_credit_transfer_template(self) -> dict:
        return {
            "creditTransfer": {
                "clientDetails": {"clientRequestID": "TRX-000000377"},
                "payerDetails": { # TODO for these 2 sections payer and payee, can i just pass a template of my details to each and move on
                    "name": "Bryan Jenks",
                    "accountNumber": "12344232122",
                    "routingNumber": "122105155",
                    "address": {
                        "addressLine1": "100 Main St",
                        "addressLine2": "Apt 116",
                        "city": "Chicago",
                        "state": "IL",
                        "zipCode": "60606",
                        "country": "US",
                    },
                },
                "payeeDetails": {
                    "name": "ABC Corp",
                    "accountNumber": "asd-344232122",
                    "routingNumber": "091000019",
                    "address": {
                        "addressLine1": "100 Main St",
                        "addressLine2": "Apt 116",
                        "city": "Chicago",
                        "state": "IL",
                        "zipCode": "60606",
                        "country": "US",
                    },
                },
                "transactionDetails": {"amount": 100.12, "paymentType": "STANDARD"},
            }
        }

    def _get_credit_transfer_headers(self) -> dict:
        return {
                "Authorization": "Bearer " + self._generate_oauth_token(),
                "Content-Type": "application/json",
                "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                "Accept": "application/json",
                "Accept-Encoding": "*",
                "Correlation-ID": f"{uuid.uuid4()}",
            }

    def credit_transfer(self):
        endpoint = API_BASE_URL + "/credit-transfers"
        headers = self._get_credit_transfer_headers()
        payload = json.dumps(self._get_credit_transfer_template())

        response = requests.post(endpoint, headers=headers, data=payload)
        print(response.text)



# TODO make the below read from template json files into dicts and then fill in necessary data after

    def read_transaction_data_from_json(transaction: json) -> None:
        pass

