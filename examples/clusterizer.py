#!/usr/bin/env python3

# mock data
import data

#import intellexer
import intellexer_wrapper as intellexer

clusterizer = intellexer.Clusterizer(data.INTELLEXER_API_KEY)

print('Trying to use URL:')
print(clusterizer.url(data.URL))

print()

print('Trying to use TEXT:')
print(clusterizer.text(data.TEXT))

print()

print('Trying to use FILE:')
print(clusterizer.file(data.FILE1()))

