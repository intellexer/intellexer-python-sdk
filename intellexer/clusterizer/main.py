from ..core.request_handler import BaseRequest

from .interface import ClusterizeResult
from .constructors import ConceptTree


class Clusterizer(BaseRequest):
	__slots__ = BaseRequest.__slots__

	def __build_response(self, response):
		concept_tree = ConceptTree(response)

		return ClusterizeResult(
			sentences=tuple(response['sentences']),
			concept_tree=concept_tree,
		)

	def url(self, url, **kwargs):
		path = 'clusterize'
		params = {
			'url': url,
			'fullTextTrees': str(kwargs.get('fullTextTrees', False)).lower(),
			'loadSentences': str(kwargs.get('loadSentences', False)).lower(),
			'useCache': str(kwargs.get('useCache', False)).lower(),
			'wrapConcepts': str(kwargs.get('wrapConcepts', False)).lower(),
		}

		response = self._get(path, params)

		return self.__build_response(response)

	def text(self, text, **kwargs):
		path = 'clusterizeText'
		params = {
			'fullTextTrees': str(kwargs.get('fullTextTrees', False)).lower(),
			'loadSentences': str(kwargs.get('loadSentences', False)).lower(),
			'useCache': str(kwargs.get('useCache', False)).lower(),
			'wrapConcepts': str(kwargs.get('wrapConcepts', False)).lower(),
		}

		response = self._post(path, params, data=text)

		return self.__build_response(response)

	def file(self, file, **kwargs):
		path = 'clusterizeFileContent'
		params = {
			'fullTextTrees': str(kwargs.get('fullTextTrees', False)).lower(),
			'loadSentences': str(kwargs.get('loadSentences', False)).lower(),
			# 'useCache': str(kwargs.get('useCache', False)).lower(),
			# 'wrapConcepts': str(kwargs.get('wrapConcepts', False)).lower(),
			'fileName': '2.txt',		# FIXME: looks like error
		}

		response = self._post(path, params, files=file)

		return self.__build_response(response)
