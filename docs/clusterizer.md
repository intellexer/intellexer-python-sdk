# Clusterizer
```python
from intellexer_python_api.clusterizer import Clusterizer

key = "your key"
text = "Computer programming (often shortened to programming) is a process that leads from an"\
       "original formulation of a computing problem to executable computer programs."
url = "http://www.infoplease.com/biography/var/barackobama.html"

result = Clusterizer().clusterize_text(key, text, load_sentences=True, fullTextTrees=True)
print(result.get_concept_tree().get_children()[0].get_text())
print(result.get_concept_tree().get_children()[0].get_weight())
print(result.get_concept_tree().get_children()[0].get_main_pharse())
print(result.get_sentences())


result = Clusterizer().clusterize_url(key, url, True, True)
print(result.get_concept_tree().get_children()[0].get_text())
print(result.get_concept_tree().get_children()[0].get_weight())
print(result.get_concept_tree().get_children()[0].get_main_pharse())
for sentence in result.get_sentences():
    print(sentence)


file = open('About me.docx', 'rb')
res = Clusterizer().clusterize_file(key, file, True, True)
for sentence in res.get_sentences():
    print(sentence)
```