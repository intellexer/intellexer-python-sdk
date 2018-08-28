from ..core.request_handler import BaseRequest
from .interface import SummarizeResult, MultiSummarizeResult


class Summarizer(BaseRequest):
	def __params(self, **kwargs):
		params = {
			i: str(kwargs.get(i, False)).lower()
			for i in (
				'fullTextTrees',
				'loadConceptsTree',
				'loadNamedEntityTree',
				'useCache',
				'usePercentRestriction',
				'wrapConcepts',
			)
		}

		params.update({
			'conceptsRestriction': kwargs.get('conceptsRestriction', 7),
			'returnedTopicsCount': kwargs.get('returnedTopicsCount', 2),
			'summaryRestriction': kwargs.get('summaryRestriction', 7),
			'textStreamLength': kwargs.get('textStreamLength', 1000),
		})

		if 'structure' in kwargs:
			params['structure'] = kwargs['structure']

		return params

	def url(self, url, **kwargs):
		path = 'summarize'

		params = {
			'url': url,
		}

		params.update(self.__params(**kwargs))
		response = self._get(path=path, params=params)
		return SummarizeResult(response)

	def text(self, text, **kwargs):
		path = 'summarizeText'
		params = self.__params(**kwargs)
		response = self._post(path=path, params=params, data=text)
		return SummarizeResult(response)

	def file(self, file, **kwargs):
		path = 'summarizeFileContent'
		params = {
			'filename': file.name,
		}

		params.update(self.__params(**kwargs))

		files = {
			file.name: file,
		}

		response = self._post(path=path, params=params, files=files)
		return SummarizeResult(response)

	def multiple_urls(self, urls, **kwargs):
		path = 'multiUrlSummary'
		params = self.__params(**kwargs)
		response = self._post(path=path, params=params, data=urls)
		return MultiSummarizeResult(response)
