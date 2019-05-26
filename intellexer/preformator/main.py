from ..core.request_handler import BaseRequest
from .interface import ParseResult


class Preformator(BaseRequest):
	__slots__ = BaseRequest.__slots__
	json = True

	def info_supported_document_structures(self):
		path = 'supportedDocumentStructures'

		return self._get(
			path=path,
			fields={},
		)

	def info_supported_document_topics(self):
		path = 'supportedDocumentTopics'

		return self._get(
			path=path,
			fields={},
		)

	@staticmethod
	def builder(response):
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

		return self._post(
			path=path,
			fields=fields,
			body=file,
		)

	def url(self, url):
		path = 'parse'

		fields = {
			'url': url,
		}

		return self._get(
			path=path,
			fields=fields,
		)
