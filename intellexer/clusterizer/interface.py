from collections import namedtuple


ClusterizeResult = namedtuple(
	'ClusterizeResult',
	(
		'concept_tree',
		'sentences',
	)
)

ConceptTree = namedtuple(
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
