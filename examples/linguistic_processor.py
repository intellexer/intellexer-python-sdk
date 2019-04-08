#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

linguistic_processor = intellexer.LinguisticProcessor(data.INTELLEXER_API_KEY)

print('Trying to use TEXT:')
print(linguistic_processor.text(
	text=data.TEXT,
	loadSentences=True,
	loadTokens=True,
	loadRelations=True,
))
