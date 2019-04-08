from ..core.request_handler import BaseRequest

from .constructors import Sentence


class LinguisticProcessor(BaseRequest):
	__slots__ = BaseRequest.__slots__

	def text(self, text, **kwargs):
		path = 'analyzeText'
		fields = {
			'loadSentences': str(kwargs.get('loadSentences', False)),
			'loadTokens': str(kwargs.get('loadTokens', False)),
			'loadRelations': str(kwargs.get('loadRelations', False)),
		}

		response = self._post(path, fields=fields, body=text)
		return tuple(Sentence(i) for i in response['sentences'])
