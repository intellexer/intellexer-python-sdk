import json
import requests


class SummarizerDoc:
    def __init__(self, json):
        self.__id = json["id"]
        self.__size = json["size"]
        self.__title = json["title"]
        self.__url = json["url"]
        self.__error = json["error"]
        self.__size_format = json["sizeFormat"]

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
        return self.__size_format


class Item:
    def __init__(self, json):
        self.__text = json["text"]
        self.__rank = json["rank"]
        self.__weight = json["weight"]

    def get_text(self):
        return self.__text

    def get_rank(self):
        return self.__rank

    def get_weight(self):
        return self.__weight


class ConceptTree:
    def __init__(self, json):
        self.__children = []
        self.__main_phrase = json["mp"]
        self.__sentence_id = json["sentenceIds"]
        self.__status = json["st"]
        self.__text = json["text"]
        self.__weight = json["w"]
        for i in json["children"]:
            self.__children.append(ConceptTree(i))

    def get_children(self):
        return self.__children

    def get_main_phrase(self):
        return self.__main_phrase

    def get_sentence_id(self):
        return self.__sentence_id

    def get_status(self):
        return self.__status

    def get_text(self):
        return self.__text

    def get_weight(self):
        return self.__weight


"""
    Request result
    Fields:
    - summarizer_doc
    - structure
    - topics
    - items
    - total_items_count
    - concept_tree
    - named_entity_tree
"""


class SummarizeResult:
    def __init__(self, json):
        self.__summarizer_doc = SummarizerDoc(json["summarizerDoc"])
        self.__structure = json["structure"]
        self.__topics = json["topics"]
        self.__items = []
        self.__total_items_count = json["totalItemsCount"]
        self.__concept_tree = None
        if json["conceptTree"] is not None:
            self.__concept_tree = ConceptTree(json["conceptTree"])
        self.__named_entity_tree = None
        if json["namedEntityTree"] is not None:
            self.__named_entity_tree = ConceptTree(json["namedEntityTree"])
        for item in json["items"]:
            self.__items.append(Item(item))

    def get_summarizer_doc(self):
        return self.__summarizer_doc

    def get_structure(self):
        return self.__structure

    def get_topics(self):
        return self.__topics

    def get_items(self):
        return self.__items

    def get_total_items_count(self):
        return self.__total_items_count

    def get_concept_tree(self):
        return self.__concept_tree

    def get_named_entity_tree(self):
        return self.__named_entity_tree


"""
    Query result summarizeMultipleURLs
"""


class MultiSummarizeResult:
    def __init__(self, json):
        self.__summarizer_doc = []
        self.__structure = json["structure"]
        self.__topics = json["topics"]
        self.__items = []
        self.__related_facts_query = json["relatedFactsQuery"]
        self.__concept_tree = None
        if json["conceptTree"] is not None:
            self.__concept_tree = ConceptTree(json["conceptTree"])
        self.__named_entity_tree = None
        if json["namedEntityTree"] is not None:
            self.__named_entity_tree = ConceptTree(json["namedEntityTree"])
        self.__related_facts_tree = None
        if json["relatedFactsTree"] is not None:
            self.__related_facts_tree = ConceptTree(json["relatedFactsTree"])
        for item in json["items"]:
            self.__items.append(Item(item))
        for doc in json["documents"]:
            self.__summarizer_doc.append(SummarizerDoc(doc))

    def get_summarizer_doc(self):
        return self.__summarizer_doc

    def get_structure(self):
        return self.__structure

    def get_topics(self):
        return self.__topics

    def get_items(self):
        return self.__items

    def get_related_facts_query(self):
        return self.__related_facts_query

    def get_concept_tree(self):
        return self.__concept_tree

    def get_named_entity_tree(self):
        return self.__named_entity_tree

    def get_related_facts_tree(self):
        return self.__related_facts_tree


class Summarizer:
    def summarize_url(self, apikey, user_url, concepts_restriction=7, full_text_trees=False, load_concepts_tree=False,
                      load_named_entity_tree=False, returned_topics_count=2, summary_restriction=7, text_stream_length=1000,
                      use_cache=False, use_percent_restriction=False, wrap_concepts=False, structure=None):
        str = "&structure={0}"
        url = "http://api.intellexer.com/summarize?" \
              "apikey={0}" \
              "&conceptsRestriction={1}" \
              "&fullTextTrees={2}" \
              "&loadConceptsTree={3}" \
              "&loadNamedEntityTree={4}" \
              "&returnedTopicsCount={5}" \
              "&summaryRestriction={6}" \
              "&textStreamLength={7}" \
              "&url={8}" \
              "&useCache={9}" \
              "&usePercentRestriction={10}" \
              "&wrapConcepts={11}".format(apikey, concepts_restriction, full_text_trees, load_concepts_tree, load_named_entity_tree,
                                          returned_topics_count, summary_restriction, text_stream_length, user_url,use_cache,
                                          use_percent_restriction, wrap_concepts)
        if structure is not None:
            url = url + str.format(structure)
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
        return SummarizeResult(response.json())

    def summarize_text(self, apikey, text, concepts_restriction=7, full_text_trees=False, load_concepts_tree=False,
                       load_named_entity_tree=False, returned_topics_count=2, summary_restriction=7, text_stream_length=1000,
                       use_cache=False, use_percent_restriction=False, wrap_concepts=False, structure=None):
        str = "&structure={0}"
        url = "http://api.intellexer.com/summarizeText?" \
              "apikey={0}" \
              "&conceptsRestriction={1}" \
              "&fullTextTrees={2}" \
              "&loadConceptsTree={3}" \
              "&loadNamedEntityTree={4}" \
              "&returnedTopicsCount={5}" \
              "&summaryRestriction={6}" \
              "&textStreamLength={7}" \
              "&useCache={8}" \
              "&usePercentRestriction={9}" \
              "&wrapConcepts={10}".format(apikey, concepts_restriction, full_text_trees, load_concepts_tree,
                                          load_named_entity_tree,
                                          returned_topics_count, summary_restriction, text_stream_length,
                                          use_cache,
                                          use_percent_restriction, wrap_concepts)
        if structure is not None:
            url = url + str.format(structure)
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
        return SummarizeResult(response.json())

    def summarize_file_content(self, apikey, file, file_size=499, file_name="1.txt", concepts_restriction=7, full_text_trees=False, load_concepts_tree=False,
                       load_named_entity_tree=False, returned_topics_count=2, summary_restriction=7, text_stream_length=1000,
                       use_cache=False, use_percent_restriction=False, wrap_concepts=False, structure=None):
        str = "&structure={0}"
        url = "http://api.intellexer.com/summarizeFileContent?" \
              "apikey={0}" \
              "&conceptsRestriction={1}" \
              "&fullTextTrees={2}" \
              "&loadConceptsTree={3}" \
              "&loadNamedEntityTree={4}" \
              "&returnedTopicsCount={5}" \
              "&summaryRestriction={6}" \
              "&textStreamLength={7}" \
              "&useCache={8}" \
              "&fileName={9}"\
              "&fileSize={10}"\
              "&usePercentRestriction={11}" \
              "&wrapConcepts={12}".format(apikey, concepts_restriction, full_text_trees, load_concepts_tree,
                                          load_named_entity_tree,
                                          returned_topics_count, summary_restriction, text_stream_length,
                                          use_cache, file_name, file_size, use_percent_restriction, wrap_concepts)
        if structure is not None:
            url = url + str.format(structure)

        f = {file_name: file}
        try:
            response = requests.post(url, files=f)
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])
        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)
        return SummarizeResult(response.json())

    def summarizeMultipleURLs(self, apikey, urls, concepts_restriction=7, full_text_trees=False, load_concepts_tree=False,
                              load_named_entity_tree=False, max_related_facts_concepts=20, max_related_facts_sentences=5,
                              related_facts_request=None, returned_topics_count=2, summary_restriction=7,
                              use_percent_restriction=False, structure=None):
        par_structure = "&structure={0}".format(structure)
        par_related_facts_request = "&relatedFactsRequest={0}".format(related_facts_request)
        url = "http://api.intellexer.com/multiUrlSummary"\
              "?apikey={0}"\
              "&conceptsRestriction={1}"\
              "&fullTextTrees={2}"\
              "&loadConceptsTree={3}"\
              "&loadNamedEntityTree={4}"\
              "&maxRelatedFactsConcepts={5}"\
              "&maxRelatedFactsSentences={6}"\
              "&returnedTopicsCount={7}"\
              "&summaryRestriction={8}"\
              "&usePercentRestriction={9}".format(apikey, concepts_restriction, full_text_trees, load_concepts_tree,
                                                 load_named_entity_tree, max_related_facts_concepts, max_related_facts_sentences,
                                                 returned_topics_count, summary_restriction, use_percent_restriction)
        if related_facts_request is not None:
            url = url + par_related_facts_request
        if structure is not None:
            url = url + par_structure
        try:
            response = requests.post(url, data=json.dumps(urls), headers={'Content-Type': 'application/json; charset=utf-8'})
            if response.status_code == 400:
                print("400 Bad Request")
                raise Exception("Error in request")
            if response.status_code != 200:
                print("error: " + str(response.json()["error"]) + "\nmessage: " + response.json()["message"])
                raise Exception(response.json()["message"])

        except Exception as ex:
            print("Exception: " + str(ex))
            exit(1)

        return MultiSummarizeResult(response.json())


