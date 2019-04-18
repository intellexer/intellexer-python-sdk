from ..core.request_handler import BaseRequest
from .constructors import NamedEntityRecognizerResult


class NamedEntityRecognizer(BaseRequest):
	__slots__ = BaseRequest.__slots__
	json = True

	def __fields(self, **kwargs):
		return {
			i: str(kwargs.get(i, False)).lower()
			for i in (
				'loadNamedEntities',
				'loadRelationsTree',
				'loadSentences',
			)
		}

	@staticmethod
	def builder(response):
		return NamedEntityRecognizerResult(response)

	def url(self, url, **kwargs):
		path = 'recognizeNe'

		fields = {
			'url': url,
		}

		fields.update(self.__fields(**kwargs))

		return self._get(
			path=path,
			fields=fields,
		)

	def file(self, file, **kwargs):
		path = 'recognizeNeFileContent'

		fields = {
			'fileName': file.name,
			'fileSize': file.seek(0, 2),
		}

		file.seek(0, 0)
		fields.update(self.__fields(**kwargs))

		return self._post(
			path=path,
			fields=fields,
			body=file,
		)

	def text(self, text, **kwargs):
		path = 'recognizeNeText'

		fields = self.__fields(**kwargs)

		return self._post(
			path=path,
			fields=fields,
			body=text,
		)
