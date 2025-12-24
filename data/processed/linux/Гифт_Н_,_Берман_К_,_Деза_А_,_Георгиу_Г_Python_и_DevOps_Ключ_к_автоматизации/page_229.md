---
source_image: page_229.png
page_number: 229
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.94
tokens: 7386
characters: 1755
timestamp: 2025-12-24T03:06:51.119517
finish_reason: stop
---

},
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'BASE_FORMAT'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'FILE_FORMAT'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file']
    }
})

dictConfig тут помогает нагляднее отобразить, куда что попадает и как все связано друг с другом, по сравнению с приведенным ранее примером. Для сложных архитектур, где нужны несколько механизмов журналирования, предпочтительнее вариант с dictConfig. В большинстве веб-фреймворков используется исключительно конфигурация на основе ассоциативных массивов.

Иногда формат журналирования игнорируется. Его часто рассматривают как некую обертку, предназначенную для удобства читающих журнал. Хотя в этом есть доля истины, но квадратные скобки с обозначением уровня журналирования (например, [CRITICAL]) очень удобны, особенно когда нужно отделять среды друг от друга в соответствии с другими параметрами, например среды промышленной эксплуатации, предэксплуатационного тестирования и разработки. Разработчику может быть и так сразу ясно, что эти журналы — из версии для разработки, но чрезвычайно важно понимать, были ли они переданы откуда-то или собирались централизованно. Вот как эти возможности применяются динамически в dictConfig с помощью переменных среды и logging.Filter:

import os
from logging.config import dictConfig

import logging

class EnvironFilter(logging.Filter):
    def filter(self, record):
        record.app_environment = os.environ.get('APP_ENVIRON', 'DEVEL')
        return True

dictConfig({
    'version': 1,
    'filters' : {