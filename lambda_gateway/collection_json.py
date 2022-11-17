
from array import array

class CollectionJSONLink(object):

	def __init__(self, href:str="", rel:str="") -> None:
		
		self.__href = href
		self.__rel = rel

	@property
	def href(self) -> str:
		return self.__href

	@href.setter
	def href(self, href: str) -> None:
		self.__href = href

	@property
	def rel(self) -> str:
		return self.__rel
	
	@rel.setter
	def rel(self, rel: str) -> None:
		self.__rel = rel

	def to_dict(self) -> dict:
		return {
			"href": self.__href,
			"rel": self.__rel
		}

class CollectionJSONData(object):

	def __init__(self, name:str, value:str="") -> None:
		self.__name = name
		self.__value = value
		self.__type = ""
		self.__prompt = ""

	@property
	def name(self) -> str:
		return self.__name
	
	@name.setter
	def name(self, name: str) -> None:
		self.__name = name

	@property
	def value(self) -> str:
		return self.__value

	@value.setter
	def value(self, value: str) -> None:
		self.__value = value

	@property
	def type(self) -> str:
		return self.__type
	
	@type.setter
	def type(self, type:str) -> None:
		self.__type = type

	@property
	def prompt(self) -> str:
		return self.__prompt
	
	@prompt.setter
	def prompt(self, prompt) -> None:
		self.__prompt = prompt

	def to_dict(self) -> dict:
		return {
			"name": self.__name,
			"type": self.__type,
			"value": self.__value,
			"prompt": self.__prompt
		}

class CollectionJSONItem(object):

	def __init__(self) -> None:

		self.__href = ""
		self.__data = []
		self.__links = []

	@property
	def href(self) -> str:
		return self.__href

	@href.setter
	def href(self, href: str) -> None:
		self.__href = href

	@property
	def data(self) -> array:
		return self.__data
	
	def add_data(self, data:CollectionJSONData) -> None:
		self.__data.append(data)

	def add_link(self, link:CollectionJSONLink) -> None:
		self.__links.append(link)

	def to_dict(self) -> dict:
		d = []
		for data in self.__data: d.append(data.to_dict())

		l = []
		for link in self.__links: l.append(link.to_dict())

		return {
			"href": self.__href,
			"data": d,
			"links": l
		}

class CollectionJSONQuery(object):

	def __init__(self) -> None:
		self.__href = ""
		self.__rel = ""
		self.__data = []

	@property
	def href(self) -> str:
		return self.__href

	@href.setter
	def href(self, href: str) -> None:
		self.__href = href

	@property
	def rel(self) -> str:
		return self.__rel
	
	@rel.setter
	def rel(self, rel:str) -> None:
		self.__rel = rel

	@property
	def data(self) -> array:
		return self.__data

	def add_data(self, name:str, value:str="") -> None:

		if name is None or name == "":
			raise AttributeError("The 'name' attribute is mandatory")

		data = CollectionJSONData()
		data.name = name
		data.value(value)

		self.__data.append(data)


	def to_dict(self) -> dict:

		d = []
		for data in self.__data: d.append(data.to_dict())

		return {
			"rel": self.__rel,
			"href": self.__href,
			"data": d
		}

class CollectionJSON(object):
	"""
	Representa um objeto de retorno segundo a especificação Collection+JSON

	link: http://amundsen.com/media-types/collection/
	"""

	def __init__(self, version="1.0") -> None:

		self.__version = version
		self.__href = ""
		self.__links = []
		self.__items = []
		self.__queries = []
		self.__template_data = []
		self.__error = {}
	
	@property
	def version(self):
		return self.__version

	@version.setter
	def version(self, version="1.0"):
		self.__version = version

	@property
	def href(self):
		return self.__href
	
	@href.setter
	def href(self, href):
		self.__href = href

	@property
	def links(self):
		return self.__links

	def add_link(self, url: str, rel: str):
		link = CollectionJSONLink()
		link.href = url
		link.rel = rel

		self.__links.append(link)

	@property
	def items(self):
		return self.__items

	def add_item(self, item: CollectionJSONItem) -> None:
		self.__items.append(item)

	def add_query(self, query: CollectionJSONQuery) -> None:
		self.__queries.append(query)

	def add_data_to_template(self, name: str) -> None:
		data = CollectionJSONData()
		data.name(name)
		data.value("")

		self.__template_data.append(data)
		
	def error(self) -> dict:
		return self.__error

	def error(self, message: str, why=None, trace=None) -> None:
		self.__error["message"] = message
		self.__error["why"] = why 
		self.__error["trace"] = trace

	def to_dict(self) -> dict:

		links = []
		for link in self.__links: links.append(link.to_dict())

		items = []
		for item in self.__items: items.append(item.to_dict())

		queries = []
		for query in self.__queries: queries.append(query.to_dict())

		template_data = []
		for td in self.__template_data: template_data.append(td.to_dict())

		return {

			"collection": {
				"version": self.__version,
				"href": self.__href,
				"links": links,
				"items": items,
				"queries": queries,
				"template": {
					"data": template_data
				},
				"error": self.__error 
			}

		}

	

	
	
		