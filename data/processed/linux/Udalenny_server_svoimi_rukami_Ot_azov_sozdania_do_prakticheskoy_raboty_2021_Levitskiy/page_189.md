---
source_image: page_189.png
page_number: 189
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 5.54
tokens: 6064
characters: 301
timestamp: 2025-12-24T04:00:03.627599
finish_reason: stop
---

zone "example.com" {
    type slave;
    file "example.com";
    masters { 192.168.1.1; };
};

На первичном сервере в блоке options нужно добавить блок allow-transfer, в котором указывают IP-адрес вторичного DNS-сервера:

options {
...
allow-transfer { 192.168.1.2; };
}

Вот теперь действительно все.