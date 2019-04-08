#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

spell_checker = intellexer.SpellChecker(data.INTELLEXER_API_KEY)

print('Trying to use TEXT:')
print(spell_checker.text(
	text=data.TEXT,
))
