from ..core.request_handler import BaseRequest

from .constructors import Sentence


class LinguisticProcessor(BaseRequest):
	__slots__ = BaseRequest.__slots__

	def analyze_text(self, text, **kwargs):
		path = 'analyzeText'
		params = {
			'loadSentences': str(kwargs.get('loadSentences', False)),
			'loadTokens': str(kwargs.get('loadTokens', False)),
			'loadRelations': str(kwargs.get('loadRelations', False)),
		}

		response = self._post(path, params=params, data=text)
		return tuple(Sentence(i) for i in response['sentences'])
