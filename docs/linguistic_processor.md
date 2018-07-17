# Linguistic Processor
```python
from intellexer_python_api.linguistic_processor import LinguisticProcessor


api_key = "your key"
text = "I stayed here on a 2 night business trip. Excellent location to the airport \
        and the hotel runs a free shuttle bus to the airport."

result = LinguisticProcessor().analyze_text(api_key, text, load_sentences=True, load_tokens=True, load_relations=True)
sentences = result.gets()
for sentence in sentences:
    print(sentence.get_text().get_content())
    tokens = sentence.get_tokens()
    for token in tokens:
        print("Token - " + token.get_text().get_content() + " lemma - " + token.get_lemma())


sentence = result.get(0)
print(sentence.get_text().get_content())

relations = sentence.get_relations()
for relation in relations:
    print(relation.get_subject())
    print(relation.get_adverbial_phrase())
    print(relation.get_verb())
    print(relation.get_object())
```