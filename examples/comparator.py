#!/usr/bin/env python3

# mock data
import data
import intellexer

print('Running: comparator')

comparator = intellexer.Comparator(data.INTELLEXER_API_KEY)

print('Trying to use URLs:')

response = comparator.urls(
	url1=data.URL,
	url2=data.OTHER_URL,
)

print(response.data)

print()

print('Trying to use TEXTs:')

response = comparator.text(
	text1=data.TEXT,
	text2=data.OTHER_TEXT,
)

print(response.data)

print()

print('Trying to use URL and FILE:')

response = comparator.url_and_file(
	url=data.URL,
	file=data.FILE1(),
)

print(response.data)

print()

print('Trying to use FILEs:')

response = comparator.files(
	file1=data.FILE1(),
	file2=data.FILE2(),
)

print(response.data)

print()

