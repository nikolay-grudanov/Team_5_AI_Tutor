---
source_image: page_048.png
page_number: 48
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.12
tokens: 11318
characters: 512
timestamp: 2025-12-24T03:16:55.026252
finish_reason: stop
---

нию карт. При установке NIS существующие учетные записи автоматически становятся локальными.

RPC и XDR

Удаленный вызов процедур (Remote Procedure Call, RPC) является протоколом работы, используемым как NFS, так и NIS. Он позволяет узлу делать запросы, которые с виду являются локальными, но выполняются на удаленном узле в сети. RPC реализован как библиотека функций плюс сетевой стандарт порядка следования байтов и структур данных, называемый XDR (eXternal Data Representation, представление внешних данных).