---
source_image: page_168.png
page_number: 168
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.58
tokens: 7486
characters: 1831
timestamp: 2025-12-24T03:05:18.961482
finish_reason: stop
---

не слишком информативны, а заметить возможные проблемы очень непросто. Далее приведен пример записи из файла changelog, вызвавшего проблемы:

--Alfredo Deza <alfredo@example.com> Sat, 11 May 2013 2:12:00 -0800

Эта запись вызвала следующее сообщение об ошибке:

parsechangelog/debian: warning: debian/changelog(17): found start of entry where expected more change data or trailer

Можете сразу заметить, что было исправлено?

-- Alfredo Deza <alfredo@example.com> Sat, 11 May 2013 2:12:00 -0800

Причиной проблемы было отсутствие пробела между тире и моим именем. Избавьте себя от мучений и воспользуйтесь dch. Эта утилита входит в состав пакета devscripts:

$ sudo apt-get install devscripts

Число опций утилиты командной строки dch очень велико, так что рекомендуем просмотреть ее документацию (основной страницы вполне достаточно). Мы воспользуемся ею для первоначального создания журнала изменений (для этого нам потребуется однократно указать флаг --create). Прежде чем запустить ее, экспортируйте свои полное имя и адрес электронной почты, чтобы включить их в генерируемый файл:

$ export DEBEMAIL="alfredo@example.com"
$ export DEBFULLNAME="Alfredo Deza"

Теперь запустите dch, чтобы сгенерировать журнал изменений:

$ dch --package "hello-world" --create -v "0.0.1" \
    -D stable "New upstream release"

Только что созданный вами файл должен выглядеть примерно так:

hello-world (0.0.1) stable; urgency=medium

    * New upstream release

-- Alfredo Deza <alfredo@example.com> Thu, 11 Apr 2019 20:28:08 -0400

Журналы изменений Debian учитывают специфику пакетов Debian. Если формат не соответствует или какая-то другая информация требует обновления, вполне можно вести отдельный журнал изменений для проекта. Во многих проектах файл changelog Debian хранится в виде отдельного файла, предназначенного только для Debian.