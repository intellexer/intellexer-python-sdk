from ..core.request_handler import BaseRequest
from .interface import SpellCheckerResult


class SpellChecker(BaseRequest):
	def text(self, text, **kwargs):
		path = 'checkTextSpelling'
		params = {
			'errorBound': kwargs.get('error_bound', 3),
			'errorTune': kwargs.get('error_tune', 1),
			'language': kwargs.get('language', 'english').upper(),
			'minProbabilityTune': kwargs.get('min_probability_tune', 3),
			'minProbabilityWeight': kwargs.get('min_probability_weight', 30),
			'separateLines': str(kwargs.get('wrapConcepts', False)).lower(),
		}

		response = self._post(path, params, data=text)
		return SpellCheckerResult(response)

	__call__ = text
