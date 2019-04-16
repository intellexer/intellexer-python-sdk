#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

print('Running: linguistic_processor')

linguistic_processor = intellexer.LinguisticProcessor(data.INTELLEXER_API_KEY)

print('Trying to use TEXT:')

response = linguistic_processor.text(
	text=data.TEXT,
	loadSentences=True,
	loadTokens=True,
	loadRelations=True,
)

print(response.data)

print()
