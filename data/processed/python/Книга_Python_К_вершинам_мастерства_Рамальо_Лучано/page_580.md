---
source_image: page_580.png
page_number: 580
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.37
tokens: 11775
characters: 2106
timestamp: 2025-12-24T02:01:40.384357
finish_reason: stop
---

Глава 18. Применение пакета asyncio для организации...

ОДИН главный поток, и мы не можем допустить в нем блокирующих вызовов, так как в этом же потоке работает цикл обработки событий. Поэтому я был вынужден переписать get_flag, чтобы для всех операций доступа к сети использовалось yield from. Теперь get_flag стала сопрограммой, поэтому download_one должна управлять ей с помощью yield from, а, значит, и download_one становится сопрограммой. Ранее, в примере 18.5 функцией download_one управляла download_many: обращения к download_one были обернуты вызовом asyncio.wait и передавались методу loop.run_until_complete. Теперь для индикации хода выполнения и обработки ошибок нам необходимо более точное управление, поэтому я перенес большую часть логики download_many в новую сопрограмму downloader_coro, а download_many используется только для подготовки цикла обработки событий и планирования downloader_coro.

В примере 18.7 показана первая часть скрипта flags2_asyncio.py, где находятся определения сопрограмм get_flag и download_one, а в примере 18.8 — вторая часть, содержащая функции downloader_coro и download_many.

Пример 18.7. flags2_asyncio.py: первая часть скрипта, вторая — в примере 18.8

import asyncio
import collections
import aiohttp
from aiohttp import web
import tqdm

from flags2_common import main, HTTPStatus, Result, save_flag

# по умолчанию задаем небольшое значение, чтобы избежать ошибок на
# удаленном сервере, например 503 - служба временно недоступна
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000

class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code

@asyncio.coroutine
def get_flag(base_url, cc): ②
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    if resp.status == 200:
        image = yield from resp.read()
        return image
    elif resp.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.HttpProcessingError(
            code=resp.status, message=resp.reason,
            headers=resp.headers)

@asyncio.coroutine