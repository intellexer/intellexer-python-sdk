import requests


"""
    Class ClusterizeResult stores the result 
"""


class ClusterizeResult:
    def __init__(self, obj):
        self.__concept_tree = ConceptTree(obj["conceptTree"])
        self.__sentences = []
        for i in obj["sentences"]:
            self.__sentences.append(i)

    def get_concept_tree(self):
        return self.__concept_tree

    def get_sentences(self):
        return self.__sentences


"""
    Clusterizer
    has 3 method
    - clusterize_url
    - clusterize_text
    - clusterize_file
"""


class Clusterizer:
    def clusterize_url(self, apikey, url, load_sentences, fullTextTrees):
        self.__url = "http://api.intellexer.com/clusterize?apikey={0}"\
                     "&fullTextTrees={1}&loadSentences={2}" \
                     "&url={3}"\
                     "&useCache=false&wrapConcepts=false".format(apikey, fullTextTrees, load_sentences, url)
        try:
            response = requests.get(self.__url)
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])
        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)
        return ClusterizeResult(response.json())

    def clusterize_text(self, apikey, text, load_sentences, fullTextTrees):
        self.__url = "http://api.intellexer.com/clusterizeText?apikey={0}"\
                     "&fullTextTrees={1}&loadSentences={2}" \
                     "&useCache=false&wrapConcepts=false".format(apikey, fullTextTrees, load_sentences)
        try:
            response = requests.post(self.__url, data=text)
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])
        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)
        return ClusterizeResult(response.json())

    def clusterize_file(self, apikey, file, load_sentences, fullTextTrees):
        self.__url = "http://api.intellexer.com/clusterizeFileContent?"\
                     "apikey={0}"\
                     "&fileName=2.txt&fullTextTrees={1}&loadSentences={2}".format(apikey, fullTextTrees, load_sentences)
        file = {"file1": file}
        try:
            response = requests.post(self.__url, files=file)
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])
        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)
        return ClusterizeResult(response.json())


"""
    Object model ConceptTree
    And methods of access to its properties
"""


class ConceptTree:
    def __init__(self, obj):
        self.__children = []
        self.__main_phrase = obj["mp"]
        self.__sentence_ids = []
        self.__status = obj["st"]
        self.__text = obj["text"]
        self.__weight = obj["w"]
        for i in obj["sentenceIds"]:
            self.__sentence_ids.append(i)
        for i in obj["children"]:
            self.__children.append(ConceptTree(i))

    def get_children(self):
        return self.__children

    def get_main_pharse(self):
        return self.__main_phrase

    def get_sentence_ids(self):
        return self.__sentence_ids

    def get_status(self):
        return self.__status

    def get_text(self):
        return self.__text

    def get_weight(self):
        return self.__weight
