import requests
import json


"""
    Stores the result of a compare
"""


class CompareResult:
    def __init__(self, result):
        self.__proximity = result["proximity"]
        self.__document = []
        self.__document.append(Documents(result["document1"]))
        self.__document.append(Documents(result["document2"]))

    def get_proximity(self):
        return self.__proximity

    def get_document1(self):
        return self.__document[0]

    def get_doument2(self):
        return self.__document[1]


"""
    presents the object of the Document and the methods of access to its properties
"""


class Documents:
    def __init__(self, doc):
        self.__id = doc["id"]
        self.__size = doc["size"]
        self.__title = doc["title"]
        self.__url = doc["url"]
        self.__error = doc["error"]
        self.__sizeFormat = doc["sizeFormat"]

    def get_id(self):
        return self.__id

    def get_size(self):
        return self.__size

    def get_title(self):
        return self.__title

    def get_url(self):
        return self.__url

    def get_error(self):
        return self.__error

    def get_size_format(self):
        return self.__sizeFormat


"""
    Class Comparator
    Has three methods for comparison
    text - text
    url - url
    url - file
"""


class Comparator:

    def compare_text(self, apikey, text1, text2):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {'text1': text1, 'text2': text2}
        url = "http://api.intellexer.com/compareText?apikey={0}".format(apikey)
        try:
            response = requests.post(url=url, data=json.dumps(data), headers=headers)
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])
        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)
        return CompareResult(response.json())

    def compare_urls(self, apikey, url1, url2):
        url = "http://api.intellexer.com/compareUrls?apikey={0}&url1={1}&url2={2}".format(apikey, url1, url2)
        try:
            response = requests.get(url)
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])
        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)
        return CompareResult(response.json())

    def compare_url_with_file(self, apikey, url, file, filename="file.txt"):
        url = "http://api.intellexer.com/compareUrlwithFile?apikey={0}&fileName={1}&url={2}".format(apikey, filename, url)
        files = {"file1": file}
        try:
            response = requests.post(url, files=files)
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])
        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)
        return CompareResult(response.json())
