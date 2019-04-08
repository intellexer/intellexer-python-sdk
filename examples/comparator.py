#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer


comparator = intellexer.Comparator(data.INTELLEXER_API_KEY)

print('Trying to use URLs:')
print(comparator.urls(
	data.URL,
	data.OTHER_URL,
))

print()

print('Trying to use TEXTs:')
print(comparator.text(
	data.TEXT,
	data.OTHER_TEXT,
))

print()

print('Trying to use URL and FILE:')
print(comparator.url_and_file(
	data.URL,
	data.FILE1(),
))

print()

print('Trying to use FILEs:')
print(comparator.files(
	data.FILE1(),
	data.FILE2(),
))

