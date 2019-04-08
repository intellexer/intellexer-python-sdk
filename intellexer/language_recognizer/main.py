from ..core.request_handler import BaseRequest

from .interface import Language


class LanguageRecognizer(BaseRequest):
	__slots__ = BaseRequest.__slots__

	def __build_response(self, response):
		return tuple(
			Language(
				language=lang['language'],
				encoding=lang['encoding'],
				weight=lang['weight'],
			) for lang in response["languages"]
		)

	def text(self, text):
		path = 'recognizeLanguage'
		response = self._post(path, fields={}, body=text)
		return self.__build_response(response)
