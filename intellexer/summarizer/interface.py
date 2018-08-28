from collections import namedtuple


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

Item = namedtuple(
	'Item',
	(
		'text',
		'rank',
		'weight',
	)
)

ConceptTree = namedtuple(		# FIXME: clusterizer.interface.ConceptTree
	'ConceptTree',
	(
		'children',
		'main_pharse',
		'sentence_ids',
		'status',
		'text',
		'weight',
	)
)

SummarizeResult = namedtuple(
	'SummarizeResult',
	(
		'document',
		'structure',
		'topics',
		'items',
		'total_items_count',
		'concept_tree',
		'named_entity_tree',
	)
)

MultiSummarizeResult = namedtuple(
	'MultiSummarizeResult',
	(
		'documents',
		'structure',
		'topics',
		'items',
		'concept_tree',
		'named_entity_tree',
		'related_facts_query',
		'related_facts_tree',
	)
)
