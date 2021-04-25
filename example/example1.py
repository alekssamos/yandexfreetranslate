from yandexfreetranslate import YandexFreeTranslate
yt = YandexFreeTranslate("ios")
print(yt.translate("auto", "ru", "Hello, my friend!"))

yt.set_proxy("socks5", "socks.zaborona.help", 1488)

with open("in.txt", "r", encoding="utf8") as f:
	text = yt.translate("en", "ru", f.read())

with open("out.txt", "w", encoding="utf8") as f:
	f.write(text)
