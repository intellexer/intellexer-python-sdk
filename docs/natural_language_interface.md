# Natural Language Interface
```python
from intellexer_python_api.natural_language_interface import NaturalLanguageInterface
key = "your key"
text = "How to increase an integration density in semiconductor memory device?"
res = NaturalLanguageInterface().convert_query_to_bool(key, text)
print(res)
```