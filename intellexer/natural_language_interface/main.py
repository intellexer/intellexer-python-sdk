from ..core.request_handler import BaseRequest


class NaturalLanguageInterface(BaseRequest):
	def convert_query_to_bool(self, text):
		path = 'convertQueryToBool'
		response = self._post(path=path, fields={}, body=text, as_json=False)
		# FIXME: Quotes are syntax garbage
		# FIXME: response must be structurized
		return response[1:-1]
