from ..core.request_handler import BaseRequest
from .constructors import NamedEntityRecognizerResult


class NamedEntityRecognizer(BaseRequest):
	def __params(self, **kwargs):
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
		params = {
			'url': url,
		}
		params.update(self.__params(**kwargs))
		response = self._get(path=path, params=params)
		return NamedEntityRecognizerResult(response)

	# FIXME: *[file_path]
	# FIXME: possible vulnerability in file_size
	def file(self, file, **kwargs):
		path = 'recognizeNeFileContent'
		files = {
			file.name: file,
		}
		params = {
			'file_name': file.name,
			'file_size': file.seek(0, 2),
		}
		file.seek(0, 0)
		params.update(self.__params(**kwargs))
		response = self._post(path=path, params=params, files=files)
		return NamedEntityRecognizerResult(response)

	def text(self, text, **kwargs):
		path = 'recognizeNeText'
		params = self.__params(**kwargs)
		response = self._post(path=path, params=params, data=text)
		return NamedEntityRecognizerResult(response)
