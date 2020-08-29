import sys
import unittest
try:
	from yandexfreetranslate import YandexFreeTranslate
except ImportError:
	sys.path.insert(0, "..")
	from yandexfreetranslate import YandexFreeTranslate
	del sys.path[0]

class yt_test_sid_to_key(unittest.TestCase):
	def test__sid_to_key(self):
		yt = YandexFreeTranslate()
		self.assertEqual(yt._sid_to_key("qw.er.ty"), "wq.re.yt-0-0")

if __name__ == "__main__":
	unittest.main()
