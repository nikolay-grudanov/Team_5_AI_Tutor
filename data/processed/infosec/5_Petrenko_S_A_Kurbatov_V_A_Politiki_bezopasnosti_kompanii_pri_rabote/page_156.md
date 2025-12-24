---
source_image: page_156.png
page_number: 156
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.69
tokens: 11285
characters: 242
timestamp: 2025-12-23T23:41:11.233773
finish_reason: stop
---

Блокирование опасного трафика:

deny udp any any range 161 162
deny udp any any eq 69
deny tcp any any range 135 139
deny udp any any range 135 139
deny tcp any any eq 445
deny udp any any eq 514
permit tcp host 70.70.1.2 host 70.70.1.1 eq 79