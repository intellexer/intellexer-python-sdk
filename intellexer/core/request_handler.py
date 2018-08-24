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
		defaults = {
			'api_key': self._api_key,
		}
		defaults.update(params)
		print(defaults)
		return defaults

	def _get(self, path, params):
		response = requests.get(
			url=self.__url(path),
			params=self.__params(params),
		)

		print(response.status_code)

		if response.status_code == 400:
			raise errors.BadRequest400

		return response.json()

	def _post(self, path, params, **kwargs):
		response = requests.post(
			url=self.__url(path),
			params=self.__params(params),
			**kwargs
		)

		print(response.status_code)

		if response.status_code == 400:
			raise errors.BadRequest400

		return response.json()
