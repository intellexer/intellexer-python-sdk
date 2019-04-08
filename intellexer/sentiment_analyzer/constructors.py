import re
from . import interface

positive_words_re = re.compile('<pos[^<>]*?>\s*(.*?)<\/pos>')
negative_words_re = re.compile('<neg[^<>]*?>\s*(.*?)<\/neg>')
sentiment_object_re = re.compile('<obj>(.*?)<\/obj>')


def Sentiment(data):
	if not data:
		return None

	return tuple(interface.Sentiment(
			author=sentiment['author'],
			dt=sentiment['dt'],
			id=sentiment['id'],
			title=sentiment['title'],
			weight=sentiment['w'],
		) for sentiment in data
	)


def Sentence(data):
	if not data:
		return None

	return tuple(interface.Sentence(
			positive_words=tuple(positive_words_re.findall(sentence['text'])),
			negative_words=tuple(negative_words_re.findall(sentence['text'])),
			sentiment_object=tuple(sentiment_object_re.findall(sentence['text'])),
			sid=sentence['sid'],
			text=sentence['text'],
			weight=sentence['w'],
		) for sentence in data
	)


def Opinions(data):
	if not data:
		return None

	return interface.Opinions(
		children=tuple(Opinions(i) for i in data['children']),
		f=data['f'],
		rs=data['rs'],
		t=data['t'],
		weight=data['w'],
	)


def SentimentAnalyzerResult(data):
	return interface.SentimentAnalyzerResult(
		sentiment_count=data['sentimentsCount'],
		ontology=data['ontology'],
		sentences=Sentence(data['sentences']),
		opinions=Opinions(data['opinions']),
		sentiments=Sentiment(data['sentiments']),
	)
