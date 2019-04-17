from ..core.request_handler import BaseRequest
from .constructors import SpellCheckerResult


class SpellChecker(BaseRequest):
	__slots__ = BaseRequest.__slots__
	json = True

	@staticmethod
	def builder(response):
		return SpellCheckerResult(response)

	def text(self, text, **kwargs):
		path = 'checkTextSpelling'

		fields = {
			'errorBound': kwargs.get('error_bound', 3),
			'errorTune': kwargs.get('error_tune', 1),
			'language': kwargs.get('language', 'english').upper(),
			'minProbabilityTune': kwargs.get('min_probability_tune', 3),
			'minProbabilityWeight': kwargs.get('min_probability_weight', 30),
			'separateLines': str(kwargs.get('wrapConcepts', False)).lower(),
		}

		return self._post(
			path=path,
			fields=fields,
			body=text,
		)
