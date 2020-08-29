#!/usr/bin/env python3
try: from utils import smartsplit
except: from .utils import smartsplit
import json
import os
import os.path
import re
import sys
import time
try:
	import urllib.parse as urllibparse
	import urllib.request as urllibrequest
except ImportError:
	import urllib as urllibrequest
	import urllib as urllibparse


class YandexFreeTranslateError(Exception): pass

class YandexFreeTranslate():
	siteurl = "https://translate.yandex.ru/"
	apibaseurl = "https://translate.yandex.net/api/v1/tr.json/"
	ua = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
	key = ""
	keysuffix = "-0-0"
	keyfilename = os.path.join(os.path.expanduser("~"), ".YandexFreeTranslate.key")
	expiretime = 60*60*24*4
	def _sid_to_key(self, sid):
		splitter = "."
		l = []
		for item in sid.split(splitter): l.append(item[::-1])
		return splitter.join(l)+self.keysuffix
	def _parse_sid(self):
		req = urllibrequest.Request(self.siteurl)
		req.add_header("User-Agent", self.ua)
		req.add_header("Accept", r"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8 ")
		req.add_header("Accept-Language", r"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3")
		req.add_header("DNT", "1")
		req.add_header("Accept-Encoding", "gzip, deflate, br")
		page = urllibrequest.urlopen(req).read().decode("UTF8")
		#open("page.html", "w", encoding="utf8").write(page)
		try:
			return re.search(r'''SID[\s]?[:][\s]?['"]([^'"]+)['"]''', page).group(1)
		except AttributeError:
			raise YandexFreeTranslateError("blocked or not found")
	def _save_key(self, key):
		with open(self.keyfilename, "w", encoding="utf8") as f:
			f.write(key)
	def _get_key(self):
		if os.path.isfile(self.keyfilename) and (time.time() - os.path.getmtime(self.keyfilename)) < self.expiretime:
			# print("from file")
			with open(self.keyfilename, "r", encoding="utf8") as f:
				return f.read()
		else:
			# print("from internet")
			sid = self._parse_sid()
			key = self._sid_to_key(sid)
			self._save_key(key)
			return key
	def get_key(self): return self._get_key()
	def regenerate_key(self):
		if os.path.isfile(self.keyfilename): os.rename(self.keyfilename, self.keyfilename+".back")
		return self._get_key()
	def __init__(self):
		if not os.path.isfile(self.keyfilename) and os.path.isfile(self.keyfilename+".back"):
			os.rename(self.keyfilename+".back", self.keyfilename)
	def translate(self, source = "auto", target="", text=""):
		if self.key == "": self.key = self._get_key()
		if source == "auto": source = ""
		if len(source) != 0 and len(source) != 2: raise ValueError("source")
		if len(target) == 0 or len(target) > 2: raise ValueError("target")
		if text == "": raise ValueError("text")
		if source==target: return text
		if source == "": lang = target
		else: lang = source+"-"+target
		p=[]
		for part in smartsplit(text, 500, 550):
			req = urllibrequest.Request(self.apibaseurl+"translate?"+urllibparse.urlencode({
				"id":self.key, "srv":"tr-text", "lang":lang, "reason":"paste"
			}))
			req.add_header("User-Agent", self.ua)
			req.add_header("Accept", r"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8 ")
			req.add_header("Accept-Language", r"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3")
			req.add_header("DNT", "1")
			req.add_header("Accept-Encoding", "gzip, deflate, br")
			try:
				content = urllibrequest.urlopen(req, data = urllibparse.urlencode({
					"options": 4, "text":part
				}).encode("UTF8")).read().decode("UTF8")
				resp = json.loads(content)
			except json.JSONDecodeError:
				raise YandexFreeTranslateError(content)
			if "text" not in resp:
				raise YandexFreeTranslateError(content)
			p.append(resp["text"][0])
		return "\n".join(p)


if __name__ == "__main__":
	if len(sys.argv) < 4:
		print("usage: "+sys.argv[0]+" \t sourcelang \t  targetlang \t  text or file.txt \t [output_file_name.txt]")
		print('example: {0} "{1}" "{2}" "{3}"'.format(sys.argv[0], "en", "ru", "hello, world!"))
		print('example: {0} "{1}" "{2}" "{3}"'.format(sys.argv[0], "en", "ru", "in.txt"))
		sys.exit(0)
	yt = YandexFreeTranslate()
	text = sys.argv[3]
	if len(text) < 150 and os.path.isfile(text): text = open(text, "r", encoding="utf8").read()
	tr_text = yt.translate(sys.argv[1], sys.argv[2], text)
	if len(sys.argv) == 5:
		with open(sys.argv[4], "w") as f: f.write(tr_text)
		print("text saved in file: "+sys.argv[4])
	else:
		print(tr_text)
