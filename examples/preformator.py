#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

preformator = intellexer.Preformator(data.INTELLEXER_API_KEY)


print('supported_document_structures')
print(preformator.supported_document_structures())


print('supported_document_topics')
print(preformator.supported_document_topics())


print('Trying to use URL:')
print(preformator.url(
	url=data.URL,
))


print('Trying to use FILE:')
print(preformator.file(
	file=data.FILE1(),
))
