from . import interface


def ConceptTree(data):
	return interface.ConceptTree(
		children=tuple(
			ConceptTree(child) for child in data["children"]
			if 'children' in data
		),
		main_pharse=data["mp"],
		sentence_ids=data["sentenceIds"],
		status=data["st"],
		text=data["text"],
		weight=data["w"],
	)
