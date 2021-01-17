import requests


class DataManager:
    def __init__(self):
        self.i = 2
        self.city_list = ["ory", "txl", "hnd", "syd", "ist", "kul", "jfk", "sfo", "cpt"]
        self.sheety_url = "SHEETY URL"
        self.headers = {
                        "Authorization": "Bearer TOKEN",
                        "Content-Type": "application/json"
                        }

    def requesting(self):
        for iata in self.city_list:
            data = {
                "sheet1": {
                    "iata": str(iata.upper())
                }
            }
            response = requests.put(url=f"{self.sheety_url}/{self.i}", json=data, headers=self.headers)
            self.i += 1

    def getting_data(self):
        response = requests.get(url=self.sheety_url, headers=self.headers)
        return response.json()




