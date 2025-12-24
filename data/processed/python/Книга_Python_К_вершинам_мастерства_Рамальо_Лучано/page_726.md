---
source_image: page_726.png
page_number: 726
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.03
tokens: 11576
characters: 1457
timestamp: 2025-12-24T02:08:06.486051
finish_reason: stop
---

try:
    cc_list = expand_cc_args(args.every, args.all, args.cc, args.limit)
except ValueError as exc:
    print(exc.args[0])
    parser.print_usage()
    sys.exit(1)

if not cc_list:
    cc_list = sorted(POP20_CC)
return args, cc_list

def main(download_many, default_concur_req, max_concur_req):
    args, cc_list = process_args(default_concur_req)
    actual_req = min(args.max_req, max_concur_req, len(cc_list))
    initial_report(cc_list, actual_req, args.server)
    base_url = SERVERS[args.server]
    t0 = time.time()
    counter = download_many(cc_list, base_url, args.verbose, actual_req)
    assert sum(counter.values()) == len(cc_list), \
        'some downloads are unaccounted for'
    final_report(cc_list, counter, t0)

Скрипт flags2_sequential.py (пример А.11) является эталоном для сравнения с параллельными реализациями. В скрипте flags2_threadpool.py (пример 17.14) также используются функции get_flag и download_one из flags2_sequential.py.

Пример А.11. flags2_sequential.py

"""Загружает флаги стран (с обработкой ошибок).

Sequential version

Sample run::

$ python3 flags2_sequential.py -s DELAY b
DELAY site: http://localhost:8002/flags
Searching for 26 flags: from BA to BZ
1 concurrent connection will be used.
----------------------
17 flags downloaded.
9 not found.
Elapsed time: 13.36s

"""

import collections

import requests
import tqdm

from flags2_common import main, save_flag, HTTPStatus, Result

DEFAULT_CONCUR_REQ = 1