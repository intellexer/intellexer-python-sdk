#!/usr/bin/env python3

# mock data
import data
import intellexer

clusterizer = intellexer.Clusterizer(data.INTELLEXER_API_KEY)

print('Trying to use URL:')

response = clusterizer.url(
	url=data.URL,
)

print(response.data)

print()

print('Trying to use TEXT:')

response = clusterizer.text(
	text=data.TEXT,
)

print(response.data)

print()

print('Trying to use FILE:')
response = clusterizer.file(
	file=data.FILE1(),
)

print(response.data)

print()

