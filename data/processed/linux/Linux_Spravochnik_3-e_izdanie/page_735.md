---
source_image: page_735.png
page_number: 735
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.80
tokens: 11715
characters: 1851
timestamp: 2025-12-24T03:48:33.121564
finish_reason: stop
---

работа над следующей версией идет своим чередом. И в том и в другом случаях решением является создание ветви (развилки) в соответствующей точке развития проекта. Если в какой-то момент потребуется интегрировать некоторые или все изменения ветви в основную линию разработки, они могут быть слиты (объединены).

Ветвление выполняется командой tag -b, а объединение — командой update -j.

Инструмент CVS

В данном разделе представлены общие сведения о CVS.

Формат команд CVS

Команды CVS имеют следующий вид:

cvs global_options command command_options

Например, приведем простую последовательность команд, в которой отображены оба вида параметров в контексте создания репозитория, импортирования существующих файлов и выполнения нескольких распространенных операций над ними:

user@localhost$ cvs -d /usr/local/cvsrep init
user@localhost$ cd ~/work/hello
user@localhost$ cvs -d /usr/local/cvsrep import -m 'Import' hello vendor start
user@localhost$ cd ..
user@localhost$ mv hello hello.bak
user@localhost$ cvs -d /usr/local/cvsrep checkout hello
user@localhost$ cd hello
user@localhost$ vi hello
user@localhost$ cvs commit -m 'Fixed a typo'
user@localhost$ cvs tag hello-1_0
user@localhost$ cvs remove -f Makefile
user@localhost$ cvs commit -m 'Removed old Makefile'
user@localhost$ cvs upd -r hello-1_0
user@localhost$ cvs upd -A

Некоторые глобальные параметры являются общими для команд администратора и пользователей, а некоторые являются специфичными для каждой из этих категорий. Общие глобальные параметры описаны в следующем разделе, а специфичные для пользователей и администратора — в разделах «Справочник пользователя CVS» и «Справочник администратора CVS», соответственно.

Общие глобальные параметры

В табл. 14.1 приведены глобальные параметры, которые могут использоваться как в командах пользователей, так и в командах администратора.