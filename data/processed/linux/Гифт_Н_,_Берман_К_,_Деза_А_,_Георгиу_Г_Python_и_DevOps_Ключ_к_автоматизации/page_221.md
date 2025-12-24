---
source_image: page_221.png
page_number: 221
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.29
tokens: 7348
characters: 1576
timestamp: 2025-12-24T03:06:24.244405
finish_reason: stop
---

Создать экземпляр Counter для небольшого Python-приложения, вызывающего API Amazon S3 с путем web/api/aws.py, можно вот так (см. пример из раздела «Соглашения о наименованиях» далее):

from metrics import Counter

counter = Counter(__name__)

counter += 1

Благодаря использованию __name__ объект Counter создается с полным пространством имен модуля Python в названии, что на стороне получателя вызова будет выглядеть как web.api.aws.Counter. Эта схема работает хорошо, но оказывается недостаточно гибкой в случае, если нам понадобится несколько счетчиков в циклах, протекающих в различных местах. Необходимо модифицировать адаптер, чтобы можно было применить суффикс:

import statsd
import get_prefix

def Counter(name, suffix=None):
    if suffix:
        name_parts = name.split('.')
        name_parts.append(suffix)
        name = '.'.join(name_parts)
    return statsd.Counter("%s.%s" % (get_prefix(), name))

Если счетчик в файле aws.py требуется в двух местах, скажем в функциях чтения и записи для S3, то можно с легкостью добавить в их названия префиксы:

from metrics import Counter
import boto

def s3_write(bucket, filename):
    counter = Counter(__name__, 's3.write')
    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket)
    key = boto.s3.key.Key(bucket, filename)
    with open(filename) as f:
        key.send_file(f)
    counter += 1

def s3_read(bucket, filename):
    counter = Counter(__name__, 's3.read')
    conn = boto.connect_s3()
    bucket = conn.get_bucket(bucket)
    k = Key(bucket)
    k.key = filename
    counter += 1
    return k