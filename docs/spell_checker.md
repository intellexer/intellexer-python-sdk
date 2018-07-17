# SpellChecker
```python
from intellexer_python_api.spell_checker import SpellChecker
key = "your key"
text = "European Union leaders need to be bolder in how they tackle the eurozone crisis,"\
       " reduce budget deficets and encourage growt, Prime Minister David Cameron said today."


res = SpellChecker().check_text_spelling(key, text)
for sentence in res.get_processed_sentences():
    print(sentence)

corrections = res.get_corrections()

for correction in corrections:
    array_of_candidate = correction.get_array_of_candidate()
    for i in array_of_candidate:
        print(i.get_correction_text())
        print(i.get_weight())
    print("---")
```