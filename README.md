# Custom Hamcrest Matchers

Highly reusable custom hamcrest matchers

## Installation

	python setup.py install

## Dependences

- lxml
- pyHamcrest

## Available matchers

-	empty
-	date_iso (ISO 8601 formatted date string)
-	has_properties
-	has_keys
-	matches_re
-	callable_
-	json_
-	xml_document
-	xml_root
-	xml_element
-	xml_contains_element
-	xml_namespaced
-	soap_document
-	soap_message

### empty

	```python
	from hamcrest import *
	from matchers import empty

	assert_that(str(), is_(empty()))
	assert_that(set(), is_(empty()))
	assert_that(dict(), is_(empty()))
	assert_that(list(), is_(empty()))
	assert_that(tuple(), is_(empty()))
	assert_that(unicode(), is_(empty()))
	```

It's smart enough to deal with iterators and generators

	```python
	assert_that(iter([]), is_(empty()))
	assert_that((i for i in []), is_(empty()))
	```

### date_iso (ISO 8601 formatted date string)

	```python
	from hamcrest import *
	from matchers import date_iso

	assert_that('1988-10-04T06:15:00.230943Z', is_(date_iso()))
	```

### has_properties

	```python
	from hamcrest import *
	from matchers import has_properties

	class Object(object):
		first = 'foo'
		second = 'bar'

	assert_that(Object(), has_properties(dict(
			first='foo',
			second='bar'
	})

	assert_that(Object(), has_properties([
			('first', 'foo'), 
			('second', 'bar')
	])
	```

### has_keys

	```python
	from hamcrest import *
	from matchers import has_keys

	dictionary = {
		'first': 'foo',
		'second': 'bar'
	}

	assert_that(dictionary, has_keys(['first', 'second']))
	```

### matches_re

	```python
	from hamcrest import *
	from matchers import matches_re

	assert_that('pattern', matches_re(r'pattern'))
	```

### callable_

	```python
	from hamcrest import *
	from matchers import callable_

	assert_that(lambda : 'foo', is_(callable_()))
	```

### json_

	```python
	from hamcrest import *
	from matchers import json_

	assert_that("{'foo': ['bar']}, is_(json_()))
	assert_that("{'foo': ['bar']}, is_(json_(has_key('foo'))))
	```

### xml_document

	```python
	from hamcrest import *
	from matchers import xml_document
	from lxml.etree import _Element

	assert_that('<element/>', is_(xml_document()))
	assert_that('<element/>', is_(xml_document(instance_of(_Element))))
	```

### xml_root

	```python
	from hamcrest import *
	from matchers import xml_root
	from lxml.etree import _Element

	assert_that('<element/>', xml_root(tag='element'))
	```

### xml_element

	```python
	from hamcrest import *
	from matchers import xml_document, xml_element

	assert_that('<element/>', is_(xml_element('element')))
	assert_that('<element/>', is_(xml_element('element', another_matcher)))
	assert_that('<foo:element/>', is_(xml_element(tag='element', ns='foo')))
	```

### xml_contains_element

	```python
	from hamcrest import *
	from matchers import xml_root, xml_element, xml_contains_element

	assert_that('<parent><child/></parent>', 
		is_(xml_element('parent', xml_contains_element('child'))))

	assert_that('<parent><child/></parent>', 
		xml_root(is_(xml_element('parent', xml_contains_element('child')))))
	```

### xml_namespaced

	```python
	from hamcrest import *
	from matchers import xml_namespaced

    assert_that('<element xmlns="http://foo.com"/>',
    	is_(xml_namespaced('http://foo.com')))
	```

### soap_document

	```python
	from hamcrest import *
	from matchers import xml_document, soap_document

    ns_url = "http://schemas.xmlsoap.org/soap/envelope/"
    string = "<Envelope xmlns='" + ns_url + "' />"

    assert_that(string, is_(xml_document(is_(soap_document()))))
	```

### soap_message

	```python
	from hamcrest import *
	from matchers import xml_document, soap_document, soap_message

    ns_url = "http://schemas.xmlsoap.org/soap/envelope/"
    string = """
    	<Envelope xmlns='""" + ns_url + """' >"
    		<Body/>
		</Envelope>
	"""

    assert_that(string, 
			is_(xml_document(is_(soap_document(is_(soap_message()))))))
	```
 
