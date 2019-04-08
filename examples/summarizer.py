#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

summarizer = intellexer.Summarizer(data.INTELLEXER_API_KEY)

print('Trying to use URL:')
print(summarizer.url(data.URL))

print()

print('Trying to use URL_POST:')
print(summarizer.url_post(
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
))

print()

print('Trying to use TEXT:')
print(summarizer.text(data.TEXT))

print()

print('Trying to use FILE:')
print(summarizer.file(data.FILE1()))

print()

print('Trying to use URLs:')
print(summarizer.urls(
	urls=(
		data.URL,
		data.OTHER_URL,
	)
))
