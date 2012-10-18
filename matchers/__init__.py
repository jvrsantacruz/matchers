# -*- coding: utf-8 -*-

import re
import json
from lxml import etree

from hamcrest import *
from hamcrest.core.base_matcher import BaseMatcher


class matches_re(BaseMatcher):
    """Custom hamcrest matcher for regular expressions"""

    def __init__(self, regex):
        self.regex_text = regex
        self.regex = re.compile(regex)

    def _matches(self, item):
        return any(self.regex.finditer(item))

    def describe_to(self, description):
        description.append_text(u"string that does match regex: {0}".format(self.regex_text))

    def describe_mismatch(self, description):
        description.append_text(u"string does not match regex: {0}".format(self.regex_text))


class edi_document(matches_re):
    """Custom hamcrest matcher to pseudo-validate EDI"""
    def __init__(self):
        super(edi_document, self).\
                __init__(u'UNB\+UNOA:1\+[^:]+:ZZ\+AEATADUE:ZZ\+\d{8}:\d{4}\+\d+\+\+&EE')


class date_iso(matches_re):
    def __init__(self):
        super(date_iso, self).\
                __init__(u'^(\d{4})-(\d{2})-(\d{2})[T ](\d+):(\d+):(\d+).(\d+)$')

    def describe_to(self, description):
        description.append_text(u'an ISO formatted date string')

    def describe_mismatch(self, actual, description):
        description.append_text(u'"{}" does not match "{}"'.format(actual, self.regex_text))


class xml_document(BaseMatcher):
    """Custom hamcrest matcher for XML documents"""
    def __init__(self, matcher=None):
        self.matcher = matcher

    def _matches(self, item):
        try:
            doc = etree.fromstring(item)
        except ValueError, err:
            # try again at ValueError: Unicode strings with encoding declaration are not supported.
            item = item.encode('utf-8')
            doc = etree.fromstring(item)

        except etree.Error, err:
            self.error = err
            return False

        if self.matcher:
            return self.matcher.matches(doc)

        return True

    def describe_to(self, description):
        description.append_text(u"string conforming a valid XML document")

    def describe_mismatch(self, description):
        description.append_text(u"failed to load xml document: '{0}'".format(self.error))


class xml_element(BaseMatcher):
    """Checks for a xml element with a certain name"""
    def __init__(self, tag, matcher=None, ns=None):
        self.tag = tag
        if ns:
            self.tag = "{{{ns}}}{tag}".format(ns=ns, tag=tag)
        self.matcher = matcher

    def _matches(self, item):
        if not item.tag == self.tag:
            return False

        if self.matcher:
            return self.matcher.matches(item)

        return True

    def describe_to(self, description):
        description.append_text(u" xml element with tag named '{0}'".format(self.tag))


# A etree xml document is the root element also.
# This may change in other implementation.
xml_root = xml_element


class xml_contains_element(xml_element):
    def _matches(self, item):
        try:
            item = item.find(".//" + self.tag)
        except:
            return False

        if item is None:
            return False

        return super(xml_contains_element, self)._matches(item)

    def describe_to(self, description):
        description.append_text(u" xml element has a children: '{0}'".format(self.tag))
        if self.matcher:
            description.append_text(u" matching {}".format(self.matcher))


class xml_namespaced(BaseMatcher):
    def __init__(self, ns_url):
        self.url = ns_url

    def _matches(self, item):
        return self.url in item.nsmap.values()

    def describe_to(self, description):
        description.append_text(u"xml document wich is namespaced with the url '{0}'".format(self.url))

    def describe_mismatch(self, description):
        description.append_text(u"url '{0}' is not within the namespaces of the xml element".format(self.url))


class soap_document(xml_document):
    """Checks for a well constructed soap document. xml_document with extra checking"""

    ns_url = "http://schemas.xmlsoap.org/soap/envelope/"

    def __init__(self, matcher=None):
        default_matcher = all_of(xml_root('Envelope', ns=self.ns_url))
        if matcher:
            default_matcher = all_of(default_matcher, matcher)

        super(soap_document, self).__init__(default_matcher)

    def describe_to(self, description):
        description.append_text(u"SOA xml document envelope")

    def describe_mismatch(self, description):
        description.append_text(u"is not a valid xml document or does not have namespace '{0}'"
                                .format(self.ns_url))


class soap_message(soap_document):
    def __init__(self, matcher=None):
        super(soap_message, self).__init__(xml_contains_element('Body', ns=self.ns_url, matcher=matcher))

    def describe_to(self, description):
        description.append_text(u"xml document within a SOA envelope")

    def describe_mismatch(self, description):
        description.append_text(u" should containg a 'Body' element ")


class json_(BaseMatcher):
    def __init__(self, matcher=None):
        self.matcher = matcher
        self.response = None

    def _matches(self, response):
        self.response = response
        try:
            self.response = json.loads(response)
        except:
            return False

        if self.matcher:
            return self.matcher.matches(self.response)

        return True

    def describe_to(self, description):
        description.append_text(u'a JSON object that ').append_description_of(self.matcher)

    def describe_mismatch(self, response, description):
        description.append_text(u'was ').append_value(self.response)
        if self.matcher:
            self.matcher.describe_mismatch(self.response, description)


class callable_(BaseMatcher):
    def _matches(self, item):
        return callable(item)

    def describe_to(self, description):
        description.append_text('callable object')

    def describe_mismatch(self, description):
        description.append_text('was not a callable object')


class has_properties(BaseMatcher):
    def __init__(self, entries):
        self.entries = dict(entries)

    def _matches(self, obj):
        return has_entries(self.entries).matches(self._properties(obj))

    def _properties(self, obj):
        return {k: getattr(obj, k, None) for k in self.entries.iterkeys()}

    def describe_to(self, description):
        description.append_text('an object with all this properties: {}'
                                .format(self.entries))

    def describe_mismatch(self, actual, description):
        description.append_text('but found instead a {} object with this properties: {}'
                                .format(actual, self._properties(actual)))


class has_properties(BaseMatcher):
    def __init__(self, entries):
        self.entries = dict(entries)

    def _matches(self, obj):
        return has_entries(self.entries).matches(self._properties(obj))

    def _properties(self, obj):
        return {k: getattr(obj, k, None) for k in self.entries.iterkeys()}

    def describe_to(self, description):
        description.append_text('an object with all this properties: {}'.format(self.entries))

    def describe_mismatch(self, actual, description):
        properties = self._properties(actual)
        description.append_text(' but found instead a {} object with this properties: {}'
                                .format(actual, properties))
        difference = set(properties.items()) - set(self.entries.items())
        description.append_text(' which differs in {}'.format(difference))
