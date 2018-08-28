from ..core.request_handler import BaseRequest
from .interface import ParseResult


class Preformator(BaseRequest):
	def supported_document_structures(self):
		path = 'supportedDocumentStructures'
		return self._get(path=path, params={})

	def supported_document_topics(self):
		path = 'supportedDocumentTopics'
		return self._get(path=path, params={})

	def __build_response(self, response):
		return ParseResult(
			structure=response['structure'],
			topics=response['topics'] or [],
			language=response['lang'],
			language_id=response['langId'],
			input_size=response['inputSize'],
			size=response['size'],
			text=response['text'],
		)

	def file(self, file):
		path = 'parseFileContent'
		params = {
			'filename': file.name,
		}
		files = {
			file.name: file,
		}
		response = self._post(path=path, params=params, files=files)
		return self.__build_response(response)

	def url(self, url):
		path = 'parse'
		params = {
			'url': url,
		}
		response = self._get(path=path, params=params)
		return self.__build_response(response)
