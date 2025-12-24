---
source_image: page_210.png
page_number: 210
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.38
tokens: 7713
characters: 1644
timestamp: 2025-12-24T02:45:46.817391
finish_reason: stop
---

2 48060
3 48059
4 48058
...
25 48032
26 48030
27 48028
28 48027
29 48026

0
1
2 DOC: "Creating a Python environment" in "Creating a development environ...
3 REGR: Avoid overflow with groupby sum
4 REGR: fix reset_index (Index.insert) regression with custom Index subcl...
...
25 BUG: Union of multi index with EA types can lose EA dtype
26 ENH: Add rolling.prod()
27 CLN: Refactor groupby's _make_wrapper
28 ENH: Support masks in groupby prod
29 DEP: Add pip to environment.yml labels \ []
0
1 [{'id': 106935113, 'node_id': 'MDU6TGFiZWwxMDY5MzUxMTM=', 'url': 'https...
2 [{'id': 134699, 'node_id': 'MDU6TGFiZWwxMzQ2OTk=', 'url': 'https://api....
3 [{'id': 233160, 'node_id': 'MDU6TGFiZWwyMzMxNjA=', 'url': 'https://api....
4 [{'id': 32815646, 'node_id': 'MDU6TGFiZWWzMjgxNTY0Ng==', 'url': 'https:...
...
25 [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ==', 'url': 'https://api.g...
26 [{'id': 76812, 'node_id': 'MDU6TGFiZWw3NjgxMg==', 'url': 'https://api.g...
27 [{'id': 233160, 'node_id': 'MDU6TGFiZWwyMzMxNjA=', 'url': 'https://api....
28 [{'id': 233160, 'node_id': 'MDU6TGFiZWwyMzMxNjA=', 'url': 'https://api....
29 [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ==', 'url': 'https://api.g...
state
0 open
1 open
2 open
3 open
4 open
...
25 open
26 open
27 open
28 open
29 open
[30 rows x 4 columns]

Немного попотев, вы сможете создать высокоуровневые интерфейсы к распространенным API работы с вебом, которые возвращают объекты DataFrame для дальнейшего анализа.

6.4. ВЗАИМОДЕЙСТВИЕ С БАЗАМИ ДАННЫХ

В корпоративных системах большая часть данных хранится не в текстовых или Excel-файлах. Широко используются реляционные базы данных на осно-