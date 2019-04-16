#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

print('Running: language_recognizer')

language_recognizer = intellexer.LanguageRecognizer(data.INTELLEXER_API_KEY)

print('Trying to use TEXT:')

response = language_recognizer.text(
	text=data.TEXT,
)

print(response.data)

print()
