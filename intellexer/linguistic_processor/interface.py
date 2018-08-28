from collections import namedtuple


Text = namedtuple(
	'Text',
	(
		'content',
		'begin_offset',
		'end_offset',
	)
)

Token = namedtuple(
	'Token',
	(
		'text',
		'part_of_speech_tag',
		'lemma',
	)
)

Relation = namedtuple(
	'Relation',
	(
		'subject',
		'verb',
		'object',
		'adverbial_phrase',
	)
)

Sentence = namedtuple(
	'Sentence',
	(
		'tokens',
		'text',
		'relations',
	)
)
