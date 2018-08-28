from collections import namedtuple


V = namedtuple(
	'V',
	(
		'correction_text',
		'weight',
	)
)

Correction = namedtuple(
	'Correction',
	(
		'length',
		'index',
		'offset',
		'candidates',
	)
)

SpellCheckerResult = namedtuple(
	'SpellCheckerResult',
	(
		'input_size',
		'sentences_count',
		'processed_sentences',
		'source_sentences',
		'corrections',
	)
)
