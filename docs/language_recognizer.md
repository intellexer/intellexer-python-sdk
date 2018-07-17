# Language Recognizer
```python
from intellexer_python_api.language_recognizer import RecognizeLanguage
text = "Тут будет мое послание".encode('utf-8')
key = "your key"

res = RecognizeLanguage().recognize_language(key, text)

array_of_languages = res.get_languages()
for language in array_of_languages:
    print(language.get_language())
    print(language.get_encoding())
    print(language.get_weight())
    print("---")
```