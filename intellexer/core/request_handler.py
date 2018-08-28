import requests
from . import urls
from . import errors


class BaseRequest:
	__slots__ = (
		'_api_key',
	)

	def __init__(self, api_key):
		self._api_key = api_key

	def __url(self, path):
		return urls.base.format(
			path=path,
		)

	def __params(self, params):
		params.update({
			'apikey': self._api_key,
		})
		return params

	def __response_handler(self, response, as_json):
		# print(response.__dict__)
		response_status = response.status_code

		if response_status in range(400, 405):
			raise errors.BadRequest400

		if as_json:
			return response.json()

		return response

	def _get(self, path, params, **kwargs):
		as_json = kwargs.pop('as_json', True)
		response = requests.get(
			url=self.__url(path),
			params=self.__params(params),
			**kwargs
		)
		return self.__response_handler(response, as_json)

	def _post(self, path, params, **kwargs):
		as_json = kwargs.pop('as_json', True)
		response = requests.post(
			url=self.__url(path),
			params=self.__params(params),
			**kwargs
		)
		return self.__response_handler(response, as_json)
