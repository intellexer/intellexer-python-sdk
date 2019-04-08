#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

sentiment_analyzer = intellexer.SentimentAnalyzer(data.INTELLEXER_API_KEY)


print('ontologies')
print(sentiment_analyzer.ontologies())


print('Trying to use TEXTS:')
print(sentiment_analyzer.texts(
	texts=[
		data.TEXT,
		data.OTHER_TEXT,
	],
	loadSentences=True,
))
