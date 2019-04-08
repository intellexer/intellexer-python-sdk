from collections import namedtuple


EntryType = namedtuple(
	'EntryType',
	(
		'id',
		'name',
	)
)

RelationTree = namedtuple(
	'RelationTree',
	(
		'children',
		'count',
		'dependency',
		'sentence_ids',
		'text',
		'type',
	)
)

Entity = namedtuple(
	'Entity',
	(
		'sentence_ids',
		'type',
		'wc',		# FIXME: wtf?!
		'text',
	)
)

Document = namedtuple(		# FIXME: comparator.interface.Document
	'Document',
	(
		'id',
		'size',
		'title',
		'url',
		'error',
		'size_format',
	)
)

NamedEntityRecognizerResult = namedtuple(
	'NamedEntityRecognizerResult',
	(
		'document',
		'entities',
		'sentences',
		'relations_tree',
	)
)
