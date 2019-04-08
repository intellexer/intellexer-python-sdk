from collections import namedtuple


CompareResult = namedtuple(
	'CompareResult',
	(
		'proximity',
		'documents',
	)
)

Documents = namedtuple(
	'Documents',
	(
		'id',
		'size',
		'title',
		'url',
		'error',
		'size_format',
	)
)
