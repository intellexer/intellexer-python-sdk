# Named Entity Recognizer
```python
from intellexer_python_api.named_entity_recognizer import NamedEntityRecognizer
# --- Example1


uri = "https://www.intellexer.com/about_us.html"
key = "your key"

result = NamedEntityRecognizer().recognize_from_url(key, uri, load_sentences=True, load_named_entities=True,
                                                    load_relations_tree=True)
entities = result.get_entities()
for entity in entities:
    print(entity.get_text())
    print(entity.get_type().get_name())
    print("----")


# --- Example 2
f = open("obama.txt", "rb")
res = NamedEntityRecognizer().recognize_from_file(key, f, load_sentences=True, load_named_entities=True,
                                                  load_relations_tree=True)
entities = res.get_entities()
for entity in entities:
    print(entity.get_text())
    print(entity.get_type().get_name())
    print(entity.get_wc())
    print("----")


# --- Example 3
text = "Eyal Shaked was appointed General Manager of the Optical Networks Division in October 2005."
result = NamedEntityRecognizer().recognize_from_text(key, text, load_sentences=True, load_named_entities=True,
                                                     load_relations_tree=True)

entities = result.get_entities()
for entity in entities:
    print(entity.get_text())
    print(entity.get_type().get_name())
    print("----")
```