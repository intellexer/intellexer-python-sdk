from . import interface


def V(data):
	return interface.V(
		correction_text=data['t'],
		weight=data['w'],
	)


def Correction(data):
	if data['v']:
		candidates = tuple(V(i) for i in data['v'])
	else:
		candidates = None

	return interface.Correction(
		length=data['l'],
		index=data['ndx'],
		offset=data['s'],
		candidates=candidates,
	)


def SpellCheckerResult(data):
	processed_sentences = None
	source_sentences = None
	corrections = None

	if 'processedSentences' in data and data['processedSentences']:
		processed_sentences = tuple(data['processedSentences'])

	if 'sourceSentences' in data and data['sourceSentences']:
		source_sentences = tuple(data['sourceSentences'])

	if 'corrections' in data and data['corrections']:
		corrections = tuple(Correction(i) for i in data['corrections'])

	return interface.SpellCheckerResult(
		input_size=data['inputSize'],
		sentences_count=data['sentencesCount'],
		processed_sentences=processed_sentences,
		source_sentences=source_sentences,
		corrections=corrections,
	)
