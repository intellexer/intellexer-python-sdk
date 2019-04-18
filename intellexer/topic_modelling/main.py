from ..core.request_handler import BaseRequest


class TopicModelling(BaseRequest):
	__slots__ = BaseRequest.__slots__
	json = True

	@staticmethod
	def builder(response):
		return response

	def url(self, url):
		path = 'getTopicsFromUrl'

		fields = {
			'url': url,
		}

		response = self._get(path=path, fields=fields)
		return response

	def text(self, text):
		path = 'getTopicsFromText'

		fields = {}

		response = self._post(path=path, fields=fields, body=text)
		return response

	def file(self, file):
		path = 'getTopicsFromFile'

		fields = {
			'filename': file.name,
		}

		response = self._post(path=path, fields=fields, body=file)
		return response
