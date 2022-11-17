from collection_json import *

#
# Link object tests
#
def test_link_obj():
	link = CollectionJSONLink()
	link.href = "http://link.example.com"
	link.rel = "foo"

	l = link.to_dict()

	assert l.get('rel') == 'foo'
	assert l.get('href') == 'http://link.example.com'

#
# Data object tests
#
def test_data_obj():
	data = CollectionJSONData()
	data.name = "foo"
	data.value = "bar"
	data.type = "str"
	data.prompt = "some message about 'foo' property"
	
	d = data.to_dict()

	assert d.get("name") == "foo"
	assert d.get("value") == "bar"
	assert d.get("type") == "str"
	assert d.get("prompt") == "some message about 'foo' property"

#
# Item object tests
#
def test_item_obj():
	item = CollectionJSONItem()
	item.href = "http://item.example.com"
	item.add_data(CollectionJSONData(name="foo", value="bar"))
	item.add_data(CollectionJSONData(name="foo2", value="bar2"))
	item.add_link(CollectionJSONLink(href="http://link.example.com", rel="descrição link"))
	item.add_link(CollectionJSONLink(href="http://link2.example.com", rel="descrição link 2"))

	i = item.to_dict()

	assert i.get("href") == "http://item.example.com"
	assert len(i.get("data")) == 2
	for d in i.get("data"): assert d.get("name") == "foo" or "foo2"
	for d in i.get("data"): assert d.get("value") == "bar" or "bar2"
	assert len(i.get("links")) == 2
	for l in i.get("links"): assert l.get("href") == "http://link.example.com" or "http://link2.example.com"
	for l in i.get("links"): assert l.get("rel") == "descrição link" or "descrição link 2"

#
# Query object tests
#
def test_query_obj():
	query = CollectionJSONQuery()
	query.href = "http://query.example.com"
	query.rel = "foo"
	query.add_data()
