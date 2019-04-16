from ..core.request_handler import BaseRequest

from .interface import ClusterizeResult
from .constructors import ConceptTree


class Clusterizer(BaseRequest):
	__slots__ = BaseRequest.__slots__

	def __fields(self, **kwargs):
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

	json = True

	@staticmethod
	def builder(response):
		concept_tree = ConceptTree(response['conceptTree'])

		return ClusterizeResult(
			sentences=tuple(response['sentences']),
			concept_tree=concept_tree,
		)

	def url(self, url, **kwargs):
		path = 'clusterize'
		fields = self.__fields(**kwargs)

		fields.update({
			'url': url,
		})

		return self._get(
			path=path,
			fields=fields,
		)

	def text(self, text, **kwargs):
		path = 'clusterizeText'
		fields = self.__fields(**kwargs)

		return self._post(path, fields, body=text)

	def file(self, file, **kwargs):
		path = 'clusterizeFileContent'
		fields = self.__fields(**kwargs)

		fields.update({
			'fileName': file.name,
		})

		return self._post(
			path=path,
			fields=fields,
			body=file,
		)
