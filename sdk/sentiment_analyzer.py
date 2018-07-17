import json
import re
import requests

class Sentiment:
    def __init__(self, json):
        self.__authon = json["author"]
        self.__dt = json["dt"]
        self.__id = json["id"]
        self.__title = json["title"]
        self.__weight = json["w"]

    def get_author(self):
        return self.__authon

    def get_dt(self):
        return self.__dt

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_weight(self):
        return self.__weight
    

"""
    Object Sentence
    Contains regulars for extracting positive / negative words
    Fields:
    - sid
    - text
    - weight
    - positive_words
    - negative_words
    - sentiment_object
    
"""


class Sentence:
    def __init__(self, json):
        self.__patern_for_pos = "<pos[^<>]*?>\s*(.*?)<\/pos>"
        self.__patern_for_obj = "<obj>(.*?)<\/obj>"
        self.__patern_for_neg = "<neg[^<>]*?>\s*(.*?)<\/neg>"
        self.__sid = json["sid"]
        self.__text = json["text"]
        self.__weight = json["w"]
        self.__positive_words = re.findall(self.__patern_for_pos, self.__text)
        self.__negative_words = re.findall(self.__patern_for_neg, self.__text)
        self.__sentiment_object = re.findall(self.__patern_for_obj, self.__text)

    def get_positive_words(self):
        return self.__positive_words

    def get_negative_words(self):
        return self.__negative_words

    def get_sentiment_object(self):
        return self.__sentiment_object

    def get_sid(self):
        return self.__sid

    def get_text(self):
        return self.__text

    def get_weight(self):
        return self.__weight

    
"""
    Object Opinions
"""


class Opinions:
    def __init__(self, json):
        self.__children = []
        self.__f = json["f"]
        self.__rs = json["rs"]
        self.__t = json["t"]
        self.__w = json["w"]
        if json["children"] is not None:
            for i in json["children"]:
                self.__children.append(Opinions(i))

    def get_children(self):
        return self.__children

    def get_f(self):
        return self.__f

    def get_rs(self):
        return self.__rs

    def get_t(self):
        return self.__t

    def get_weight(self):
        return self.__w

    
"""
    Request result
    Fields:
    - sentiment_count
    - ontology
    - sentences
    - opinions
"""


class SentimentAnalyzerResult:
    def __init__(self, json):
        self.__sentiment_count = json["sentimentsCount"]
        self.__ontology = json["ontology"]
        self.__sentences = []
        if json["opinions"] is not None:
            self.__opinions = Opinions(json["opinions"])
        else:
            self.__opinions = None
        self.__sentiments = []
        if json["sentences"] is not None:
            for sentence in json["sentences"]:
                self.__sentences.append(Sentence(sentence))
        if json["sentiments"] is not None:
            for sentence in json["sentiments"]:
                self.__sentiments.append(Sentiment(sentence))

    def get_sentiment_count(self):
        return self.__sentiment_count

    def get_ontology(self):
        return self.__ontology

    def get_sentences(self):
        return self.__sentences

    def get_opinions(self):
        return self.__opinions

    def get_sentiments(self):
        return self.__sentiments


"""
    Using this class, make requests
"""


class SentimentAnalyzer:
    def sentiment_analyzer_ontologies(self, apikey):
        url = "http://api.intellexer.com/sentimentAnalyzerOntologies?apikey={0}".format(apikey)
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
        return response.json()

    def analyze_sentiments(self, apikey, data, load_sentences, ontology=None):
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        if ontology is not None:
            url = "http://api.intellexer.com/analyzeSentiments?apikey={0}&loadSentences={1}&ontology={2}"\
                .format(apikey, load_sentences, ontology)
        else:
            url = "http://api.intellexer.com/analyzeSentiments?apikey={0}&loadSentences={1}" \
                .format(apikey, load_sentences)
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
        return SentimentAnalyzerResult(response.json())





