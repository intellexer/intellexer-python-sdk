# Comparator
```python
from intellexer_python_api.comparator import Comparator

apikey = "your key"
text = "The products, information,"\
       " and other content provided by this seller are provided for informational purposes only."

url = "https://www.infoplease.com/people"\
      "/who2-biography/barack-obama"

file = open("obama.txt", "rb")

comparator = Comparator().compare_url_with_file(apikey, url, file=file)
print(comparator.get_proximity())
doc = comparator.get_document1()
print(doc.get_url())
doc = comparator.get_doument2()
print(doc.get_title())

comparator = Comparator().compare_text(apikey, text1=text, text2=text)
print(comparator.get_proximity())

```