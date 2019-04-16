#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

print('Running: natural_language_interface')

natural_language_interface = intellexer.NaturalLanguageInterface(data.INTELLEXER_API_KEY)

print('Trying to use TEXT:')

response = natural_language_interface.convert_query_to_bool(
	text=data.TEXT,
)

print(response.data)

print()
