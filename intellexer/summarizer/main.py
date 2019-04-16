import json as _json
from ..core.request_handler import BaseRequest
from .constructors import SummarizeResult


class Summarizer(BaseRequest):
	optional_fields = (
		'options',
		'structure',
		'textStreamLength',
		'summaryRestriction',
		'conceptsRestriction',
		'returnedTopicsCount',
	)

	bool_optional_fields = (
		'useCache',
		'wrapConcepts',
		'fullTextTrees',
		'loadConceptsTree',
		'loadNamedEntityTree',
		'usePercentRestriction',
	)

	json = True

	@staticmethod
	def builder(data):
		return SummarizeResult(data)

	def __fields(self, **kwargs):
		fields = {}

		for fieldname in self.bool_optional_fields:
			if fieldname in kwargs:
				fields[fieldname] = str(kwargs[fieldname]).lower()

		for fieldname in self.optional_fields:
			if fieldname in kwargs:
				fields[fieldname] = kwargs[fieldname]

		return fields

	def url(self, url, **kwargs):
		path = 'summarize'

		fields = {
			'url': url,
		}

		fields.update(self.__fields(**kwargs))

		return self._get(
			path=path,
			fields=fields,
		)

	def url_post(self, url, options, **kwargs):
		path = 'summarize'

		fields = {
			'url': url,
		}

		headers = {
			'Content-Type': 'application/json',
		}

		body = _json.dumps(options)
		fields.update(self.__fields(**kwargs))

		return self._post(
			path=path,
			body=body,
			fields=fields,
			headers=headers,
		)

	def text(self, text, **kwargs):
		path = 'summarizeText'
		fields = self.__fields(**kwargs)

		return self._post(
			path=path,
			fields=fields,
			body=text,
		)

	def file(self, file, **kwargs):
		path = 'summarizeFileContent'

		fields = {
			'fileName': file.name,
			'fileSize': file.seek(0, 2),
		}

		file.seek(0, 0)
		fields.update(self.__fields(**kwargs))

		return self._post(
			path=path,
			fields=fields,
			body=file,
		)
