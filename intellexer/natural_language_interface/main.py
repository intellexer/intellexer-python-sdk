from ..core.request_handler import BaseRequest


class NaturalLanguageInterface(BaseRequest):
	__slots__ = BaseRequest.__slots__
	json = False

	@staticmethod
	def builder(response):
		# FIXME: response must be structurized
		# FIXME: Quotes are syntax garbage
		return response[1:-1]

	def convert_query_to_bool(self, text):
		path = 'convertQueryToBool'

		return self._post(
			path=path,
			fields={},
			body=text,
		)
