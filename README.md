## Installing
`python3 -m pip install git+https://github.com/alekssamos/yandexfreetranslate.git`

or

`python3 -m pip install yandexfreetranslate`
### Using
```python3
from yandexfreetranslate import YandexFreeTranslate
yt = YandexFreeTranslate()

print(yt.translate("en", "ru", "Hello, world!"))```
Or from command line: ```bash
python3 yandexfreetranslate.py en ru "Hello, world!"
```
## Runing tests
```bash
git clone https://github.com/alekssamos/yandexfreetranslate.git
cd yandexfreetranslate
python3 -m pip install -r requirements-dev.txt

python3 -m unittest
# or
python3 -m tox
```
