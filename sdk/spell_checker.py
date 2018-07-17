import requests


"""
    Object for creating requests
"""


class SpellChecker:
    def check_text_spelling(self, apikey, text, error_bound=3, min_probability_weight=30,
                            min_probability_tune=3, error_tune=1, separate_lines=False):
        url = "http://api.intellexer.com/checkTextSpelling?" \
              "apikey={0}" \
              "&errorBound={1}" \
              "&errorTune={2}" \
              "&language=ENGLISH" \
              "&minProbabilityTune={3}" \
              "&minProbabilityWeight={4}" \
              "&separateLines={5}".format(apikey, error_bound, error_tune,
                                          min_probability_tune, min_probability_weight,
                                          separate_lines)
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
        return SpellCheckerResult(response.json())


class V:
    def __init__(self, json):
        self.__correction_text = json["t"]
        self.__weight = json["w"]

    def get_correction_text(self):
        return self.__correction_text

    def get_weight(self):
        return self.__weight


class Correction:
    def __init__(self, json):
        self.__length = json["l"]
        self.__index = json["ndx"]
        self.__offset = json["s"]
        self.__array_of_candidate = []
        if json["v"] is not None:
            for v in json["v"]:
                self.__array_of_candidate.append(V(v))

    def get_length(self):
        return self.__length

    def get_index(self):
        return self.__index

    def get_offset(self):
        return self.__offset

    def get_array_of_candidate(self):
        return self.__array_of_candidate


"""
    Request result
"""


class SpellCheckerResult:
    def __init__(self, json):
        self.__input_size = json["inputSize"]
        self.__sentences_count = json["sentencesCount"]
        self.__processed_sentences = []
        self.__sourceSentences = []
        self.__corrections = []
        if json["processedSentences"] is not None:
            for sentence in json["processedSentences"]:
                self.__processed_sentences.append(sentence)

        if json["sourceSentences"] is not None:
            for sentence in json["sourceSentences"]:
                self.__sourceSentences.append(sentence)

        for correction in json["corrections"]:
            self.__corrections.append(Correction(correction))

    def get_input_size(self):
        return self.__input_size

    def get_sentences_count(self):
        return self.__sentences_count

    def get_processed_sentences(self):
        return self.__processed_sentences

    def get_source_sentences(self):
        return self.__sourceSentences

    def get_corrections(self):
        return self.__corrections

