'''*docstring*
'''

import json
from ..core.request_handler import BaseRequest
from .constructors import SentimentAnalyzerResult


class SentimentAnalyzer(BaseRequest):
	'''*docstring*
	'''

	def ontologies(self):
		'''*docstring*
		'''
		path = 'sentimentAnalyzerOntologies'
		response = self._get(path=path, fields={})
		return response

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

		body = json.dumps(data)

		response = self._post(path=path, fields=fields, body=body, headers=headers)
		return SentimentAnalyzerResult(response)
