Yandex Free Translate! More than six million requests! No limits or restrictions! Tested within a year!

(Более шести миллионов запросов! Никаких ограничений и лимитов! Проверено в течение года!)
## Installing (Установка)
`python3 -m pip install git+https://github.com/alekssamos/yandexfreetranslate.git`

or (или)

`python3 -m pip install yandexfreetranslate`
### Using (Использование)
```python3
from yandexfreetranslate import YandexFreeTranslate
yt = YandexFreeTranslate()

print(yt.translate("en", "ru", "Hello, world!"))```
Or from command line (Или из командной строки):
```bash
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
# or (или)
python3 -m pip install tox
python3 -m tox
```
