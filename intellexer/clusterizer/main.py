from ..core.request_handler import BaseRequest

from .interface import ClusterizeResult
from .constructors import ConceptTree


class Clusterizer(BaseRequest):
	__slots__ = BaseRequest.__slots__

	def __params(self, **kwargs):
		return {
			'fullTextTrees': str(kwargs.get('fullTextTrees', False)).lower(),
			'loadSentences': str(kwargs.get('loadSentences', False)).lower(),
			'useCache': str(kwargs.get('useCache', False)).lower(),
			'wrapConcepts': str(kwargs.get('wrapConcepts', False)).lower(),
			'conceptsRestriction': kwargs.get('conceptsRestriction', 7),
			# 'options': str(kwargs.get('options', self.options())),
		}

# 	def options(self):
# 		return {
# 			"topics": [],
# 			"reorderConcepts": [
# 				{
# 					"term": "fish",
# 					"selection": [
# 						"farmed fish",
# 						"commercial fish",
# 					]
# 				}, {
# 					"term": "fishing",
# 					"selection": [
# 						"sport fishing",
# 					]
# 				}
# 			]
# 		}

	def __build_response(self, response):
		concept_tree = ConceptTree(response['conceptTree'])

		return ClusterizeResult(
			sentences=tuple(response['sentences']),
			concept_tree=concept_tree,
		)

	def url(self, url, **kwargs):
		path = 'clusterize'
		params = self.__params(**kwargs)

		params.update({
			'url': url,
		})

		response = self._get(path, params)

		return self.__build_response(response)

	def text(self, text, **kwargs):
		path = 'clusterizeText'
		params = self.__params(**kwargs)

		response = self._post(path, params, data=text)

		return self.__build_response(response)

	def file(self, file, **kwargs):
		path = 'clusterizeFileContent'
		params = self.__params(**kwargs)

		params.update({
			'fileName': '2.txt',
		})

		response = self._post(path, params, files=file)

		return self.__build_response(response)
