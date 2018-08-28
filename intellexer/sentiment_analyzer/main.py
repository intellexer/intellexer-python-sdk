from ..core.request_handler import BaseRequest
from .constructors import SentimentAnalyzerResult


class SentimentAnalyzer(BaseRequest):
	def ontologies(self):		# FIXME: no args? RLY?
		path = 'sentimentAnalyzerOntologies'
		response = self._get(path=path, params={})
		return response

	def sentiments(self, data, **kwargs):
		path = 'analyzeSentiments'
		params = {
			'loadSentences': str(kwargs.get('loadSentences', False)).lower(),
		}

		if 'ontology' in kwargs:
			params['ontology'] = kwargs['ontology']

		response = self._post(path=path, params=params)
		return SentimentAnalyzerResult(response)
