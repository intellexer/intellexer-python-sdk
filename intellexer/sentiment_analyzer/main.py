'''*docstring*
'''

import json as _json
from ..core.request_handler import BaseRequest
from .constructors import SentimentAnalyzerResult


class SentimentAnalyzer(BaseRequest):
	'''*docstring*
	'''
	json = True

	@staticmethod
	def builder(response):
		return SentimentAnalyzerResult(response)

	def ontologies(self):
		'''*docstring*
		'''
		path = 'sentimentAnalyzerOntologies'
		return self._get(
			path=path,
			fields={},
		)

	def texts(self, texts, **kwargs):
		'''*docstring*
		'''
		path = 'analyzeSentiments'

		fields = {
			'loadSentences': str(kwargs.get('loadSentences', False)).lower(),
		}

		if 'ontology' in kwargs:
			fields['ontology'] = kwargs['ontology']

		headers = {
			'Content-Type': 'application/json',
		}

		data = [
			{
				'id': number,
				'text': text,
			} for number, text in enumerate(texts)
		]

		body = _json.dumps(data)

		return self._post(path=path, fields=fields, body=body, headers=headers)
