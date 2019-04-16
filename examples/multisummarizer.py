#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

multisummarizer = intellexer.MultiSummarizer(data.INTELLEXER_API_KEY)

print('Trying to use URL:')

response = multisummarizer.url(
	urls=(
		data.URL,
		data.OTHER_URL,
	)
)

print(response.data)

