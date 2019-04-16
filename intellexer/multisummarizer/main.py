import json as _json
from ..core.request_handler import BaseRequest
from .constructors import MultiSummarizeResult


class MultiSummarizer(BaseRequest):
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
		return MultiSummarizeResult(data)

	def __fields(self, **kwargs):
		fields = {}

		for fieldname in self.bool_optional_fields:
			if fieldname in kwargs:
				fields[fieldname] = str(kwargs[fieldname]).lower()

		for fieldname in self.optional_fields:
			if fieldname in kwargs:
				fields[fieldname] = kwargs[fieldname]

		return fields


	def url(self, urls, **kwargs):
		path = 'multiUrlSummary'

		fields = self.__fields(**kwargs)

		body = _json.dumps(urls)

		headers = {
			'Content-Type': 'application/json',
		}

		return self._post(
			path=path,
			fields=fields,
			body=body,
			headers=headers,
		)
