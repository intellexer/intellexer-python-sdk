from . import interface


def Document(data):
	return interface.Document(
		id=data['id'],
		size=data['size'],
		title=data['title'],
		url=data['url'],
		error=data['error'],
		size_format=data['sizeFormat'],
	)


def Item(data):
	return interface.Item(
		text=data['text'],
		rank=data['rank'],
		weight=data['weight'],
	)


def ConceptTree(data):
	children = None

	if 'children' in data:
		children=tuple(ConceptTree(child) for child in data["children"])

	return interface.ConceptTree(
		children=children,
		main_pharse=data['mp'],
		sentence_ids=data['sentenceIds'],
		status=data['st'],
		text=data['text'],
		weight=data['w'],
	)


def MultiSummarizeResult(data):
	concept_tree = None
	named_entity_tree = None
	related_facts_tree = None

	if 'conceptTree' in data and data['conceptTree']:
		concept_tree = ConceptTree(data['conceptTree'])

	if 'namedEntityTree' in data and data['namedEntityTree']:
		concept_tree = ConceptTree(data['namedEntityTree'])

	if 'relatedFactsTree' in data and data['relatedFactsTree']:
		related_facts_tree = ConceptTree(data['relatedFactsTree'])

	return interface.MultiSummarizeResult(
		documents=tuple(Document(i) for i in data['documents']),
		structure=data['structure'],
		topics=data['topics'],
		items=tuple(data['items']),
		concept_tree=concept_tree,
		named_entity_tree=named_entity_tree,
		related_facts_query=data['relatedFactsQuery'],
		related_facts_tree=related_facts_tree,
	)
