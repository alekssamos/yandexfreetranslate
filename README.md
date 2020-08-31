Yandex Free Translate! More than six million requests! No limits or restrictions! Tested within a year!

Яндекс Переводчик бесплатно (Более шести миллионов запросов! Никаких ограничений и лимитов! Проверено в течение года!)
## Installing (Установка)
`python3 -m pip install git+https://github.com/alekssamos/yandexfreetranslate.git`

or (или)

`python3 -m pip install yandexfreetranslate`
### Using (Использование)
```python3
from yandexfreetranslate import YandexFreeTranslate
yt = YandexFreeTranslate()
# yt.set_proxy("socks5", "localhost", 9050, "username", "password")

print(yt.translate("en", "ru", "Hello, world!"))
```
Or from command line (Или из командной строки):
```bash
# for use socks4, socks5 or https proxy (Для использования socks4, socks5 или https proxy):
export https_proxy=127.0.0.1:9050
# or (или)
export https_proxy=username:password@127.0.0.1:9050

python3 yandexfreetranslate/__init__.py en ru "Hello, world!"
# or (или)
python3 yandexfreetranslate/__init__.py en ru in.txt
# or (или)
python3 yandexfreetranslate/__init__.py en ru in.txt out.txt
```
## Runing tests (Запуск тестов)
```bash
git clone https://github.com/alekssamos/yandexfreetranslate.git
cd yandexfreetranslate
python3 -m unittest

# or
python3 -m pip install tox
python3 -m tox
```
