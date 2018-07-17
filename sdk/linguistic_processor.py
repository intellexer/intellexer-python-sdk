import requests


"""
    Object Sentences keeps in itself all the sentence
    get(index) will return sentence(object Sentence) Under the number index
    gets will return a list of sentences(object Sentence)
"""


class Sentences:
    def __init__(self, res):
        self.__sentences = []
        for i in res["sentences"]:
            self.__sentences.append(Sentence(i))

    def get(self, index):
        return self.__sentences[index]

    def gets(self):
        return self.__sentences


"""
    Object Text stores the properties Content, beginOffset, endOffset
    and can give them the appropriate method
"""


class Text:
    def __init__(self, text):
        self.__content = text["content"]
        self.__beginOffset = text["beginOffset"]
        self.__endOffset = text["endOffset"]

    def get_content(self):
        return self.__content

    def get_begin_offset(self):
        return self.__beginOffset

    def get_end_offset(self):
        return self.__endOffset


"""
    Object Token stores the Text object in itself and can give it back,
    and properties partOfSpeechTag, lemma
"""


class Token:
    def __init__(self, token):
        self.__text = None
        if token["text"] is not None:
            self.__text = Text(token["text"])
        self.__partOfSpeechTag = token["partOfSpeechTag"]
        self.__lemma = token["lemma"]

    def get_text(self):
        return self.__text

    def get_part_of_speech_tag(self):
        return self.__partOfSpeechTag

    def get_lemma(self):
        if self.__lemma is None:
            return "null"
        else:
            return self.__lemma


"""
    The Relation class has the fields: subject, verb, object, adverbialPhrase
    and the corresponding methods for accessing these fields
"""


class Relation:
    def __init__(self, relation):
        self.__subject = relation["subject"]
        self.__verb = relation["verb"]
        self.__object = relation["object"]
        self.__adverbialPhrase = relation["adverbialPhrase"]

    def get_subject(self):
        return self.__subject

    def get_verb(self):
        return self.__verb

    def get_object(self):
        return self.__object

    def get_adverbial_phrase(self):
        return self.__adverbialPhrase


"""
    The sentence object stores a Text object and a list of Token objects
"""


class Sentence:
    def __init__(self, t):
        # или здесь сделать null
        self.__tokens = None
        self.__relations = []
        self.__text = None
        if t["text"] is not None:
            self.__text = Text(t["text"])
        if t["tokens"] is not None:
            self.__tokens = []
            for i in t["tokens"]:
                self.__tokens.append(Token(i))
        if t["relations"] is not None:
            for i in t["relations"]:
                self.__relations.append(Relation(i))

    def get_tokens(self):
        return self.__tokens

    def get_text(self):
        return self.__text

    def get_relations(self):
        return self.__relations


"""
    Main class
    Configures the request
    The analyzeText method starts the analysis and returns the object Sentences
"""


class LinguisticProcessor:
    def analyze_text(self, apikey, text, load_sentences=False, load_tokens=False, load_relations=False):
        url = "http://api.intellexer.com/analyzeText?"\
              "apikey={0}"\
              "&loadSentences={1}"\
              "&loadTokens={2}"\
              "&loadRelations={3}" \
            .format(apikey, load_sentences, load_tokens, load_relations)
        try:
            response = requests.post(url=url, data=text)
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])
        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)
        return Sentences(response.json())


