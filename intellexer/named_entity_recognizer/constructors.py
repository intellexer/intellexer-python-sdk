from . import interface

EntryTypeNames = (
	"Unknown",
	"Person",
	"Organization",
	"Location",
	"Title",
	"Position",
	"Age",
	"Date",
	"Duration",
	"Nationality",
	"Event",
	"Url",
	"MiscellaneousLocation",
)


def EntryType(entry_id):
	if entry_id not in range(0, len(EntryTypeNames)):
		entry_id = 0		# FIXME: raise?

	return interface.EntryType(
		id=entry_id,
		name=EntryTypeNames[entry_id]

	)


def RelationTree(data):
	if data:
		return interface.RelationTree(
			children=tuple(RelationTree(i) for i in data['children']),
			count=data['count'],
			dependency=data['dependency'],
			sentence_ids=data['sentenceIds'],
			text=data['text'],		# FIXME: linguistic_processor.interface.Text
			type=data['type'],		# FIXME: EntryType?
		)


def Entity(data):
	return interface.Entity(
		sentence_ids=data['sentenceIds'],
		type=EntryType(data['type']),
		wc=data['wc'],		# FIXME: wtf?!
		text=data['text'],
	)


def Entityes(data):
	if data is not None:
		for entity in data:
			yield Entity(entity)


def Document(data):
	if data:
		return interface.Document(
			id=data['id'],
			size=data['size'],
			title=data['title'],
			url=data['url'],
			error=data['error'],
			size_format=data['sizeFormat'],
		)


def NamedEntityRecognizerResult(data):
	return interface.NamedEntityRecognizerResult(
		document=Document(data.get("document")),
		entities=tuple(Entityes(data.get("entities"))),
		# FIXME: linguistic_processor.interface.Sentence
		sentences=data["sentences"],
		relations_tree=RelationTree(data.get("relationsTree")),
	)
