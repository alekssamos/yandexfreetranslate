from setuptools import setup, find_packages
from os.path import join, dirname
import sys
if sys.version_info[0] != 3:
	print("This script requires Python >= 3")
	exit(1)

setup(
    name="yandexfreetranslate",
    version="1.3",
    author="alekssamos",
    author_email="aleks-samos@yandex.ru",
    url="https://github.com/alekssamos/yandexfreetranslate/",
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=open(join(dirname(__file__), "README.md"), encoding="UTF8").read(),
)
