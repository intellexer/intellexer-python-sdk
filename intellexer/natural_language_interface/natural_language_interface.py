import requests


class NaturalLanguageInterface:
    def convert_query_to_bool(self, apikey, text):
        url = "http://api.intellexer.com/convertQueryToBool?"\
              "apikey={0}".format(apikey)
        try:
            response = requests.post(url, data=text)
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])
        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)
        return response.text
