import json as _json
from ..core.util import ChainStream
from ..core.request_handler import BaseRequest

from .interface import CompareResult, Documents


class Comparator(BaseRequest):
	__slots__ = BaseRequest.__slots__
	json = True

	@staticmethod
	def builder(response):
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

		fields={}

		data = {
			'text1': text1,
			'text2': text2,
		}

		headers = {
			'Content-Type': 'application/json',
		}

		body = _json.dumps(data)

		return self._post(
			path=path,
			fields=fields,
			body=body,
			headers=headers,
		)

	def urls(self, url1, url2):
		path = 'compareUrls'

		fields = {
			'url1': url1,
			'url2': url2,
		}

		return self._get(
			path=path,
			fields=fields,
		)

	def url_and_file(self, url, file):
		path = 'compareUrlwithFile'

		fields = {
			'url': url,
			'fileName': file.name,
		}

		return self._post(
			path=path,
			fields=fields,
			body=file,
		)

	def files(self, file1, file2):
		path = 'compareFiles'

		sizes = (
			file1.seek(0, 2),
			file2.seek(0, 2)
		)

		file1.seek(0, 0)
		file2.seek(0, 0)


		fields = {
			'fileName1': file1.name,
			'fileName2': file2.name,
			'firstFileSize': sizes[0],
		}

		body = ChainStream(
			file1,
			file2,
		)

		headers = {
			'Content-Length': sum(sizes),
		}

		return self._post(
			path=path,
			fields=fields,
			body=body,
			headers=headers,
		)
