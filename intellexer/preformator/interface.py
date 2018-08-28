from collections import namedtuple


ParseResult = namedtuple(
	'ParseResult',
	(
		'structure',
		'topics',
		'language',
		'language_id',
		'input_size',
		'size',
		'text',
	)
)
