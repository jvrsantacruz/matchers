# -*- coding: utf-8 -*-
"""
This file is part of matchers.

matchers is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

matchers is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with matchers.  If not, see <http://www.gnu.org/licenses/>.
"""

from hamcrest import *

from lxml import etree

from matchers import xml_document


class TestXMLDocument(object):
    document = """
    <element xmlns="http://espacio.com">
        <top_level>
            <first_inner_level>
                <second_inner_level>
                    <empty_element/>
                </second_inner_level>
            </first_inner_level>
        </top_level>
    </element>
    """

    document_consistent = "<?xml version='1.0' ?>" + document
    document_inconsistent = "<?xml version='1.0' encoding='utf-8'?>" + document


    def setup(self):
        self.dom = etree.fromstring(self.document)

    def test_xml_document(self):
        assert_that(self.document, is_(xml_document()))

    def test_xml_document_extra_matcher_works(self):
        assert_that(self.document, is_(xml_document(is_(instance_of(type(self.dom))))))

    def test_xml_document_encoding_inconsistence_does_not_trigger_exceptions(self):
        assert_that(self.document_inconsistent, is_(xml_document()))

    def test_xml_document_encoding_consistency_just_works(self):
        assert_that(self.document_consistent, is_(xml_document()))
