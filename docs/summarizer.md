# Summarizer
```python
from intellexer_python_api.summarizer import Summarizer
key = "your key"
url = "https://www.intellexer.com/about_us.html"
file = open("obama.txt", "r")

result = Summarizer().summarize_file_content(key, file, load_concepts_tree=True, load_named_entity_tree=True)
print(result.get_topics())
print(result.get_structure())
summarizerDoc = result.get_summarizer_doc()
print(summarizerDoc.get_id())
print(summarizerDoc.get_url())
print(summarizerDoc.get_title())

for item in result.get_items():
    print(item.get_text())
    print(item.get_weight())
    print(item.get_rank())

namedEntityTree = result.get_named_entity_tree()
print(namedEntityTree.get_text())
print(namedEntityTree.get_main_phrase())
print(namedEntityTree.get_status())
children = namedEntityTree.get_children()
for child in children:
    print(child.get_text())
    print(child.get_weight())


result = Summarizer().summarize_url(key, url, load_named_entity_tree=True)
#...


urls = ["https://www.intellexer.com/about_us.html", "https://www.intellexer.com/"]
result = Summarizer().summarizeMultipleURLs(key, urls, load_concepts_tree=True)
for summarizer_doc in result.get_summarizer_doc():
    print(summarizer_doc.get_id())
    print(summarizer_doc.get_url())
    print(summarizer_doc.get_title())

print(result.get_topics())
print(result.get_structure())

for item in result.get_items():
    print(item.get_text())
    print(item.get_weight())
    print(item.get_rank())
#...
```