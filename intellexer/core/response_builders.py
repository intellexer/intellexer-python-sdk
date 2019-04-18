import json


def response_builder_json(builder):
	def target(raw):
		json_data = json.loads(raw)
		return builder(json_data)
	return target


def response_builder_void(builder):
	def target(raw):
		return builder(raw)
	return target


# builder = builders[self.json]
builders = (
	response_builder_void,
	response_builder_json,
)
