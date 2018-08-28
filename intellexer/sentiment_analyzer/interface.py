from collections import namedtuple


Sentiment = namedtuple(
	'Sentiment',
	(
		'author',
		'dt',		# FIXME: wtf?!
		'id',
		'title',
		'weight',
	)
)

Sentence = namedtuple(
	'Sentence',
	(
		'positive_words',
		'negative_words',
		'sentiment_object',
		'sid',
		'text',
		'weight',
	)
)

Opinions = namedtuple(
	'Opinions',
	(
		'children',
		'f',		# FIXME: wtf?!
		'rs',		# FIXME: wtf?!
		't',		# FIXME: wtf?!
		'weight',
	)
)

SentimentAnalyzerResult = namedtuple(
	'SentimentAnalyzerResult',
	(
		'sentiment_count',
		'ontology',
		'sentences',
		'opinions',
		'sentiments',
	)
)
