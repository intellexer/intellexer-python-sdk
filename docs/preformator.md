# Preformator
```python
from intellexer_python_api.preformator import Preformator


key = "your key"
url = "https://www.intellexer.com/about_us.html"
file = open("About me.docx", "rb")


res = Preformator().parse_file_content(key, file, filename="About me.docx")
print(res.get_structure())
print(res.get_input_size())
print(res.get_size())
print(res.get_topics())
print(res.get_text())
print(res.get_language())


res = Preformator().parse(key, url)
print(res.get_structure())
print(res.get_input_size())
print(res.get_size())
print(res.get_topics())
print(res.get_text())
print(res.get_language())

res = Preformator().supported_document_topics(key)
print(res)
```