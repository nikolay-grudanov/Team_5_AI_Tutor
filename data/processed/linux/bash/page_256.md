---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.60
tokens: 7290
characters: 1257
timestamp: 2025-12-23T23:11:27.832205
finish_reason: stop
---

logger

Команда logger используется во многих дистрибутивах Linux для записи событий в системный журнал.

Общие параметры команды

- -s — одновременно записать событие в stderr.
- -t — пометить событие указанным значением.

Запись событий в журнал Windows

Команда eventcreate предназначена для создания записей в журнале событий Windows. Чтобы ее можно было использовать, необходимо предоставить ей некоторые данные.

- Идентификатор события (/id) — номер для идентификации события. Допустимо любое число от 1 до 1000.
- Тип события (/t) — категория, которая наилучшим образом описывает событие. Допускаются следующие параметры:
  • ERROR;
  • WARNING;
  • INFORMATION
  • SUCCESSAUDIT;
  • FAILUREAUDIT.
- Имя журнала событий (/l) — имя журнала, в который необходимо внести запись. Допустимы следующие параметры:
  • APPLICATION;
  • SYSTEM.
- Источник события (/so) — имя приложения, генерирующего событие. Допустима любая строка.
- Описание (/d) — характеристика события. Допустима любая строка.

Вот, например, запуск из Git Bash:

$ eventcreate //ID 200 //L APPLICATION //T INFORMATION //SO "Cybersecurity Ops" //D "This is an event"

SUCCESS: An event of type 'INFORMATION' was created in the 'APPLICATION' log with 'Cybersecurity Ops' as the source.