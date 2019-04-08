from ..core.request_handler import BaseRequest
from .interface import ParseResult


class Preformator(BaseRequest):
	def supported_document_structures(self):
		path = 'supportedDocumentStructures'
		return self._get(path=path, fields={})

	def supported_document_topics(self):
		path = 'supportedDocumentTopics'
		return self._get(path=path, fields={})

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
		fields = {
			'filename': file.name,
		}
		response = self._post(path=path, fields=fields, body=file)
		return self.__build_response(response)

	def url(self, url):
		path = 'parse'
		fields = {
			'url': url,
		}
		response = self._get(path=path, fields=fields)
		return self.__build_response(response)
