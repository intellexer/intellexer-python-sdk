#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

sentiment_analyzer = intellexer.SentimentAnalyzer(data.INTELLEXER_API_KEY)


print('ontologies')

response = sentiment_analyzer.ontologies()

print(response.json)


print('Trying to use TEXTS:')

response = sentiment_analyzer.texts(
	texts=[
		data.TEXT,
		data.OTHER_TEXT,
	],
	loadSentences=True,
)

print(response.data)
