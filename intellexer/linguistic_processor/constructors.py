from . import interface


def Text(data):
	if data is None:
		return None

	return interface.Text(
		content=data['content'],
		begin_offset=data['beginOffset'],
		end_offset=data['endOffset'],
	)


def Token(data):
	if data is None:
		return None

	return interface.Token(
		text=Text(data['text']),
		part_of_speech_tag=data['partOfSpeechTag'],
		lemma=data['lemma'],
	)


def Relation(data):
	if data is None:
		return None

	return interface.Relation(
		subject=data['subject'],
		verb=data['verb'],
		object=data['object'],
		adverbial_phrase=data['adverbialPhrase'],
	)


def Sentence(data):
	if data is None:
		return None

	if data.get('tokens') is None:
		tokens = None
	else:
		tokens = tuple(Token(i) for i in data['tokens'])

	if data.get('relations') is None:
		relations = None
	else:
		relations = tuple(Relation(i) for i in data['relations'])

	if data.get('text') is None:
		text = None
	else:
		text = Text(data['text'])

	return interface.Sentence(
		tokens=tokens,
		text=text,
		relations=relations,
	)
