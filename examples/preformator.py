#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

preformator = intellexer.Preformator(data.INTELLEXER_API_KEY)


print('supported_document_structures')

response = preformator.info_supported_document_structures()

print(response.json)

print()

print('supported_document_topics')

response = preformator.info_supported_document_topics()

print(response.json)

print()

print('Trying to use URL:')

response = preformator.url(
	url=data.URL,
)

print(response.data)

print()

print('Trying to use FILE:')

response = preformator.file(
	file=data.FILE1(),
)

print(response.data)

print()
