#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

print('Running: summarizer')

summarizer = intellexer.Summarizer(data.INTELLEXER_API_KEY)

print('Trying to use URL:')

response = summarizer.url(
	url=data.URL,
)

print(response.data)

print()

print('Trying to use URL_POST:')

response = summarizer.url_post(
	url=data.URL,
	options={
		"topics": [],
		"reorderConcepts": [
			{
				"term":"fish",
				"selection": [
					"farmed fish",
					"commercial fish"
				]
			}, {
				"term":"fishing",
				"selection": [
					"sport fishing"
				]
			},
		]
	}
)

print(response.data)

print()

print('Trying to use TEXT:')

response = summarizer.text(
	text=data.TEXT,
)

print(response.data)

print()

print('Trying to use FILE:')

response = summarizer.file(
	file = data.FILE1()
)

print(response.data)

print()
