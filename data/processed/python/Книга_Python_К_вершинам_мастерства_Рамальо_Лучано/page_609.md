---
source_image: page_609.png
page_number: 609
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.09
tokens: 11902
characters: 2740
timestamp: 2025-12-24T02:03:11.228927
finish_reason: stop
---

Применение динамических атрибутов для обработки данных

Применение динамических атрибутов для обработки данных

В примерах ниже мы воспользуемся динамическими атрибутами для обработки данных в формате JSON, опубликованных издательством O'Reilly для конференции OSCON 2014. В примере 19.1 показаны четыре записи из этого набора3.

Пример 19.1. Примеры записей из файла osconfeed.json; значения некоторых полей сокращены

{
    "Schedule": {
        "conferences": [
            {
                "serial": 115,
                "events": [
                    {
                        "serial": 34505,
                        "name": "Why Schools Don't Use Open Source to Teach Programming",
                        "event_type": "40-minute conference session",
                        "time_start": "2014-07-23 11:30:00",
                        "time_stop": "2014-07-23 12:10:00",
                        "venue_serial": 1462,
                        "description": "Aside from the fact that high school programming...",
                        "website_url": "http://oscon.com/oscon2014/public/schedule/detail/34505",
                        "speakers": [157509],
                        "categories": ["Education"]
                    }
                ],
                "speakers": [
                    {
                        "serial": 157509,
                        "name": "Robert Lefkowitz",
                        "photo": null,
                        "url": "http://sharewave.com/",
                        "position": "CTO",
                        "affiliation": "Sharewave",
                        "twitter": "sharewaveteam",
                        "bio": "Robert /r0ml/ Lefkowitz is the CTO at Sharewave, a startup..."
                    }
                ],
                "venues": [
                    {
                        "serial": 1462,
                        "name": "F151",
                        "category": "Conference Venues"
                    }
                ]
            }
        ]
    }
}

В примере 19.1 показаны 4 из 895 записей JSON-файла. Как видим, весь набор данных — это единственный JSON-объект с ключом "Schedule", значением которого является отображение с четырьмя ключами: "conferences" (конференции), "events" (мероприятия), "speakers" (докладчики) и "venues" (места проведения).

3 Об этом наборе и правилах его использования можно прочитать на странице «DIY: OSCON schedule» (http://bit.ly/1TxUXBP). Оригинальный JSON-файл размером 744 КБ еще был доступен в сети на момент написания этой книги (http://www.oreilly.com/pub/sc/osconfeed). Его копию под названием osconfeed.json можно найти в каталоге oscon-schedule/data/ репозитория кода к этой книге (http://bit.ly/1TxUXBP).