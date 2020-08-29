import sys
import os
import os.path
import re
import unittest
try:
	import yandexfreetranslate
except ImportError:
	sys.path.insert(0, "..")
	import yandexfreetranslate
	del sys.path[0]

class dummy_urlopen(object):
	def __init__(self, url, *a, **kw):
		if type(url) == yandexfreetranslate.urllibrequest.Request:
			url = url.full_url
		self.url = url
	def read(self):
		if "https://translate.yandex.ru/" in self.url:
			with open(os.path.join(os.path.dirname(__file__), "page.html"), "rb") as f:
				body = f.read()
				return body
		if "https://translate.yandex.net/api/v1/tr.json/translate?" in self.url+"?":
			body='{"text": ["Привет"]}'.encode("UTF8")
			return body
		raise ValueError("URL!")

yandexfreetranslate.urllibrequest.urlopen = dummy_urlopen

class yt_test_translate(unittest.TestCase):
	def test_translate(self):
		yt = yandexfreetranslate.YandexFreeTranslate()
		self.assertTrue(len(yt.translate("en", "ru", "hello")) > 1)

if __name__ == "__main__":
	unittest.main()
