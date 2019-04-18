'''
*docstring*
'''

import os
import urllib
import urllib3
from . import response_builders
from . import response_wrapper




class BaseRequest:
	'''
	*docstring*
	'''
	__slots__ = (
		'_api_key',
		'_server',
		'_builder',
	)

	http = urllib3.PoolManager()

	def __init__(self, api_key=None, server=None):
		api_key = api_key or os.environ['INTELLEXER_API_KEY']
		server = server or os.getenv(
			'INTELLEXER_SERVER',
			'http://api.intellexer.com',
		)
		self._api_key = api_key
		self._server = server.rstrip('/')

		builder_function = response_builders.builders[self.json]
		self._builder = builder_function(self.builder)

	def __url(self, path):
		return '/'.join((
			self._server,
			path,
		))

	def __fields(self, fields):
		fields.update({
			'apikey': self._api_key,
		})
		return fields

	@classmethod
	def from_raw(cls, raw_data):
		builder_function = response_builders.builders[cls.json]
		response_builder = builder_function(cls.builder)

		return response_wrapper.Response(
			response_builder=response_builder,
			response=raw_data,
		)

	def __response_handler(self, response):
		return response_wrapper.Response(
			response_builder=self._builder,
			request_functin=response,
		)

	def _get(self, path, fields, headers=None):
		response = lambda: self.http.request(
			method='GET',
			url=self.__url(path),
			fields=self.__fields(fields),
			preload_content=False,
			headers=headers,
		)
		return self.__response_handler(response)

	def _post(self, path, fields, body, headers=None):
		url=self.__url(path)
		fields=self.__fields(fields)

		if fields:
			url += '?' + urllib.parse.urlencode(fields)

		response = lambda: self.http.request(
			method='POST',
			url=url,
			body=body,
			preload_content=False,
			headers=headers,
		)
		return self.__response_handler(response)
