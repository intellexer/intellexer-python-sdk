import json
from ..core.request_handler import BaseRequest
from .constructors import SummarizeResult, MultiSummarizeResult


class Summarizer(BaseRequest):
	optional_fields = (
		'structure',
		'wrapConcepts',
		'summaryRestriction',
		'textStreamLength',
		'conceptsRestriction',
		'returnedTopicsCount',
	)

	bool_fields = (
		'useCache',
		'fullTextTrees',
		'loadConceptsTree',
		'loadNamedEntityTree',
		'usePercentRestriction',
	)

	def __fields(self, **kwargs):
		fields = {}

		for fieldname in self.bool_fields:
			if fieldname in kwargs:
				fields[fieldname] = str(kwargs[fieldname]).lower()

		for fieldname in self.optional_fields:
			if fieldname in kwargs:
				fields[fieldname] = kwargs[fieldname]

		return fields

	def url(self, url, **kwargs):
		def json(url, **kwargs):
			path = 'summarize'

			fields = {
				'url': url,
			}

			fields.update(self.__fields(**kwargs))
			return self._get(path=path, fields=fields)

		response = json(url, **kwargs)
		return SummarizeResult(response)

	def url_post(self, url, **kwargs):
		def as_json(url, **kwargs):
			path = 'summarize'

			fields = {
				'url': url,
			}

			headers = {
				'Content-Type': 'application/json',
			}

			if 'options' in kwargs:
				data = kwargs.pop('options')
				body = json.dumps(data)
			else:
				body = None

			fields.update(self.__fields(**kwargs))
			return self._post(path=path, body=body, fields=fields, headers=headers)

		response = as_json(url, **kwargs)
		return SummarizeResult(response)

	def text(self, text, **kwargs):
		path = 'summarizeText'

		fields = self.__fields(**kwargs)
		response = self._post(path=path, fields=fields, body=text)
		return SummarizeResult(response)

	def file(self, file, **kwargs):
		path = 'summarizeFileContent'

		fields = {
			'fileName': file.name,
			'fileSize': file.seek(0, 2),
		}

		file.seek(0, 0)

		fields.update(self.__fields(**kwargs))
		response = self._post(path=path, fields=fields, body=file)
		return SummarizeResult(response)

	def urls(self, urls, **kwargs):
		path = 'multiUrlSummary'
		fields = self.__fields(**kwargs)
		body = json.dumps(urls)

		headers = {
			'Content-Type': 'application/json',
		}


		response = self._post(path=path, fields=fields, body=body, headers=headers)
		return MultiSummarizeResult(response)
