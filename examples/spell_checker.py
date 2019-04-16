#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

print('Running: spell_checker')

spell_checker = intellexer.SpellChecker(data.INTELLEXER_API_KEY)

print('Trying to use TEXT:')

response = spell_checker.text(
	text=data.TEXT,
)

print(response.data)

print()
