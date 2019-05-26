from ..core.request_handler import BaseRequest

from .interface import Language


class LanguageRecognizer(BaseRequest):
	__slots__ = BaseRequest.__slots__
	json = True

	@staticmethod
	def builder(response):
		return tuple(
			Language(
				language=lang['language'],
				encoding=lang['encoding'],
				weight=lang['weight'],
			) for lang in response["languages"]
		)

	def text(self, text):
		path = 'recognizeLanguage'

		return self._post(
			path=path,
			fields={},
			body=text,
		)
