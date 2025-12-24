---
source_image: page_313.png
page_number: 313
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.08
tokens: 6061
characters: 1050
timestamp: 2025-12-24T10:08:47.314702
finish_reason: stop
---

Затем добавьте цель dupfind в вашу цель target. Осталось только настроить сам dupfind. Для этого создайте файл dupfind.cfg в текущем каталоге:

{
    min: 30,
    max: 500,
    increment: 10,
    fuzzy: true,
    cpd: true,
    sources:
    [
        {
            name: "myProject",
            def: true,
            root: ".",
            directories:
            [
                "src"
            ],
            include:
            [
                "*.*js"
            ],
            exclude:
            [
                "*/.svn",
                "*-[^/]*.js",
            ]
        }
    ]
}

Это конфигурационный файл в формате JSON, говорящий dupfind, что нужно сделать. Самое интересное в нем — это свойство fuzzy, позволяющее dupfind делать нечеткие действия (например, игнорировать имена переменных), и массив sources, определяющий, какие каталоги и какие файлы нужно исследовать, а какие нужно проигнорировать.

Как только у вас есть такой файл конфигурации, ваша панель инструментов отобразит график дублирующегося кода, как показа-