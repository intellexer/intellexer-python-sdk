#!/usr/bin/env python3

# mock data
import data
import intellexer

print('Running: topic_modelling')

topic_modelling = intellexer.TopicModelling(data.INTELLEXER_API_KEY)

print('Trying to use URL:')

response = topic_modelling.url(
	url=data.URL,
)

print(response.data)

print()

print('Trying to use TEXT:')

response = topic_modelling.text(
	text=data.TEXT,
)

print(response.data)

print()

print('Trying to use FILE:')

response = topic_modelling.file(
	file=data.FILE1(),
)

print(response.data)

print()
