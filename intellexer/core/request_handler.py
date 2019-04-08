'''
*docstring*
'''

import os
import urllib
import urllib3
import json
import io
from . import errors


class BaseRequest:
	'''
	*docstring*
	'''
	__slots__ = (
		'_api_key',
		'_server',
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

	def __response_handler(self, response, as_json):
		decoded_response = io.TextIOWrapper(
			response,
			encoding='utf-8',
		)

		if response.status == 200:
			if as_json:
				ret = json.load(decoded_response)
			else:
				ret = decoded_response.read()
			response.release_conn()
			return ret

		#ret = json.load(decoded_response)
		#response.release_conn()
		raise errors.BadRequest400(decoded_response.read())

	def _get(self, path, fields, as_json=True, headers=None):
		response = self.http.request(
			method='GET',
			url=self.__url(path),
			fields=self.__fields(fields),
			preload_content=False,
			headers=headers,
		)
		return self.__response_handler(response, as_json)

	def _post(self, path, fields, body, as_json=True, headers=None):
		url=self.__url(path)
		fields=self.__fields(fields)

		if fields:
			url += '?' + urllib.parse.urlencode(fields)

		response = self.http.request(
			method='POST',
			url=url,
			body=body,
			preload_content=False,
			headers=headers,
		)
		return self.__response_handler(response, as_json)
