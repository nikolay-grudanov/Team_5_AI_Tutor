---
source_image: page_342.png
page_number: 342
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.35
tokens: 7366
characters: 1423
timestamp: 2025-12-24T08:39:39.696408
finish_reason: stop
---

"pruned": false,
"softforks": [
    {
        "id": "bip34",
        "version": 2,
        "reject": {
            "status": false
        }
    },
    {
        "id": "bip66",
        "version": 3,
        "reject": {
            "status": false
        }
    },
    {
        "id": "bip65",
        "version": 4,
        "reject": {
            "status": false
        }
    }
],
"bip9_softforks": {
    "csv": {
        "status": "defined",
        "startTime": 1462060800,
        "timeout": 1493596800,
        "since": 0
    },
    "segwit": {
        "status": "defined",
        "startTime": 1479168000,
        "timeout": 1510704000,
        "since": 0
    }
},
"warnings": ""
}

Эта команда выводит большой объем информации о блокчейне. Обратите внимание, что в данном случае будут загружаться и проверяться блоки до высоты 207546. Bitcoin Core сначала загрузит заголовки блоков, чтобы проверить доказательство работы, и только потом начнет загружать полные блоки. В этом примере узел загрузил заголовки до высоты 54398, то есть все заголовки, существующие на этот момент. Также обратите внимание на интересное поле initialblockdownload, которое будет содержать значение true, пока начальная загрузка блоков не будет завершена.

Пусть этот демон продолжает работу. Мы еще вернемся к нему в приложении А, где я расскажу, как с помощью bitcoin-cli можно исследовать блокчейн и как пользоваться встроенным кошельком.