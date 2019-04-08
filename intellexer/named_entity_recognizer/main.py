from ..core.request_handler import BaseRequest
from .constructors import NamedEntityRecognizerResult


class NamedEntityRecognizer(BaseRequest):
	def __fields(self, **kwargs):
		return {
			i: str(kwargs.get(i, False)).lower()
			for i in (
				'loadNamedEntities',
				'loadRelationsTree',
				'loadSentences',
			)
		}

	def url(self, url, **kwargs):
		path = 'recognizeNe'
		fields = {
			'url': url,
		}
		fields.update(self.__fields(**kwargs))
		response = self._get(path=path, fields=fields)
		return NamedEntityRecognizerResult(response)

	# FIXME: *[file_path]
	# FIXME: possible vulnerability in file_size
	def file(self, file, **kwargs):
		path = 'recognizeNeFileContent'
		fields = {
			'fileName': file.name,
			'fileSize': file.seek(0, 2),
		}
		file.seek(0, 0)
		fields.update(self.__fields(**kwargs))
		response = self._post(path=path, fields=fields, body=file)
		return NamedEntityRecognizerResult(response)

	def text(self, text, **kwargs):
		path = 'recognizeNeText'
		fields = self.__fields(**kwargs)
		response = self._post(path=path, fields=fields, body=text)
		print(response)
		return NamedEntityRecognizerResult(response)
