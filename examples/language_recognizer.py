#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

language_recognizer = intellexer.LanguageRecognizer(data.INTELLEXER_API_KEY)

print('Trying to use TEXT:')

response = language_recognizer.text(
	text=data.TEXT,
)

print(response.data)
