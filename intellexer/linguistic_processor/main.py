from ..core.request_handler import BaseRequest

from .constructors import Sentence


class LinguisticProcessor(BaseRequest):
	__slots__ = BaseRequest.__slots__
	json = True

	@staticmethod
	def builder(response):
		return tuple(Sentence(i) for i in response['sentences'])

	def text(self, text, **kwargs):
		path = 'analyzeText'
		fields = {
			'loadSentences': str(kwargs.get('loadSentences', False)),
			'loadTokens': str(kwargs.get('loadTokens', False)),
			'loadRelations': str(kwargs.get('loadRelations', False)),
		}

		return self._post(path, fields=fields, body=text)
