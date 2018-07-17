# Sentiment Analyzer
```python
from intellexer_python_api.sentiment_analyzer import SentimentAnalyzer
key = "your key"
data = [{"id": "1", "text": "Hello, world! It's been a great day"},
        {"id": "2", "text": "Intellexer Summarizer has an unique feature."}]

result = SentimentAnalyzer().analyze_sentiments(key, data, load_sentences=True, ontology="Hotels")
print(result.get_sentiment_count())
print(result.get_sentiments()[0].get_weight())
print(result.get_sentiments()[0].get_title())
array_sentences = result.get_sentences()
for sentence in array_sentences:
    print(sentence.get_text() + " weight = " + str(sentence.get_weight()))
    print(sentence.get_positive_words())
    print(sentence.get_negative_words())

opinions = result.get_opinions()
print(opinions.get_weight())
print(opinions.get_t())
```