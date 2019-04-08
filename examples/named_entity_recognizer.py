#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

named_entity_recognizer = intellexer.NamedEntityRecognizer(data.INTELLEXER_API_KEY)

print('Trying to use URL:')
print(named_entity_recognizer.url(
	url=data.URL,
	loadSentences=True,
	loadTokens=True,
	loadRelations=True,
))

print()

print('Trying to use TEXT:')
print(named_entity_recognizer.text(
	text=data.TEXT,
	loadSentences=True,
	loadTokens=True,
	loadRelations=True,
))

print()

print('Trying to use FILE:')
print(named_entity_recognizer.file(
	file=data.FILE1(),
	loadSentences=True,
	loadTokens=True,
	loadRelations=True,
))
