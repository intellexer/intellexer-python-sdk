import re
from . import interface

positive_words_re = re.compile('<pos[^<>]*?>\s*(.*?)<\/pos>')
negative_words_re = re.compile('<neg[^<>]*?>\s*(.*?)<\/neg>')
sentiment_object_re = re.compile('<obj>(.*?)<\/obj>')


def Sentiment(data):
	if not data:
		return None

	return interface.Sentiment(
		author=data['author'],
		dt=data['dt'],
		id=data['id'],
		title=data['title'],
		weight=data['w'],
	)


def Sentence(data):
	if not data:
		return None

	return interface.Sentence(
		positive_words=tuple(positive_words_re.findall(data['text'])),
		negative_words=tuple(negative_words_re.findall(data['text'])),
		sentiment_object=tuple(sentiment_object_re.findall(data['text'])),
		sid=data['sid'],
		text=data['text'],
		weight=data['w'],
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
