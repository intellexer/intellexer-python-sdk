from ..core.request_handler import BaseRequest

from .interface import CompareResult, Documents


class Comparator(BaseRequest):
	__slots__ = BaseRequest.__slots__

	def __build_response(self, response):
		return CompareResult(
			proximity=response['proximity'],
			documents=tuple(
				Documents(
					id=response[i]["id"],
					size=response[i]["size"],
					title=response[i]["title"],
					url=response[i]["url"],
					error=response[i]["error"],
					size_format=response[i]["sizeFormat"],
				) for i in ('document1', 'document2')
			),
		)

	def text(self, text1, text2):
		path = 'compareText'

		data = {
			'text1': text1,
			'text2': text2,
		}

		response = self._post(path, params={}, json=data)

		return self.__build_response(response)

	def urls(self, url1, url2):
		path = 'compareUrls'

		params = {
			'url1': url1,
			'url2': url2,
		}

		response = self._get(path, params)

		return self.__build_response(response)

	def url_and_text(self, url, text):
		path = 'compareUrlwithFile'

		params = {
			'url': url,
		}

		data = {
			'file1': text,
		}

		response = self._post(path, params, json=data)

		return self.__build_response(response)
