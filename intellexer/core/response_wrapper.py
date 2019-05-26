import json
from . import errors


class Response:
	__slots__ = (
		'__request_functin',
		'__response_builder',
		'__response',
	)

	def __init__(self, response_builder, request_functin=None, response=None):
		self.__request_functin = request_functin
		self.__response_builder = response_builder
		self.__response = response

	def __response_handler(self):
		try:
			response = self.__request_functin()

			decoded_response = response.read().decode()

			if response.status == 200:
				return decoded_response

			if response.status in range(400, 500):
				raise errors.BadRequest400(decoded_response)

			if response.status in range(500, 600):
				raise errors.BadRequest500(decoded_response)

		finally:
			response.release_conn()

	@property
	def raw(self):
		if not self.__response:
			self.__response = self.__response_handler()

		return self.__response

	@property
	def data(self):
		return self.__response_builder(self.raw)

	@property
	def json(self):
		return json.loads(self.raw)
