---
source_image: page_194.png
page_number: 194
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.55
tokens: 7292
characters: 1382
timestamp: 2025-12-24T03:05:57.522409
finish_reason: stop
---

filename = "../content/blog/%s.md" % title
if os.path.exists(filename):
    print("Removing: %s" % filename)
    os.unlink(filename)

with open(filename, 'a') as the_file:
    the_file.write(out)

if __name__ == '__main__':
    from new_pic_category import PRODUCT
    for product in PRODUCT:
        write_post(product)

Создание поискового индекса Algolia и его обновление

После преобразования товаров из базы данных в посты в формате Markdown необходимо написать код на языке Python для создания поискового индекса Algolia и его синхронизации. Algolia (https://www.algolia.com/) — замечательный инструмент, позволяющий быстро решить проблему поискового механизма, с прекрасной поддержкой Python.

Следующий сценарий сканирует все файлы в формате Markdown и генерирует поисковый индекс, который можно загрузить в Algolia:

"""
Создает очень простой и очень легко расширяемый JSON-индекс для Hugo для импорта в Algolia
# Возможно, имеет смысл запустить следующую команду для каталога content,
# чтобы удалить пробелы
for f in *\ *; do mv "$f" "${f// /_}"; done

import os
import json

CONTENT_ROOT = "../content/products"
CONFIG = "../config.toml"
INDEX_PATH = "../index.json"

def get_base_url():
    for line in open(CONFIG):
        if line.startswith("baseurl"):
            url = line.split("=")[-1].strip().strip('""')
            return url

def build_url(base_url, title):