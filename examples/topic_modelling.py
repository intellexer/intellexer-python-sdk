#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

topic_modelling = intellexer.TopicModelling(data.INTELLEXER_API_KEY)

print('Trying to use URL:')
print(topic_modelling.url(
	url=data.URL,
))

print()

print('Trying to use TEXT:')
print(topic_modelling.text(
	text=data.TEXT,
))

print()

print('Trying to use FILE:')
print(topic_modelling.file(
	file=data.FILE1(),
))
