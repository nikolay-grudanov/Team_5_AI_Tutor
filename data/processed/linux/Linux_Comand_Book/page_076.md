---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.16
tokens: 6023
characters: 1544
timestamp: 2025-12-24T04:06:23.177021
finish_reason: stop
---

drwx   2 smith smith 4096 Nov 11 12:27 dir

soffice [файлы]    openoffice.org
/usr/lib/openoffice/programs stdin stdout -file -opt --help -version
OpenOffice.org* - это комплексный интегрированный офисный программный пакет, в котором можно редактировать файлы Microsoft Word, Excel и PowerPoint. Просто выполните следующую команду:

$ soffice

и можно приступать к работе. В одной и той же программе можно редактировать все три типа файлов t. Это большая программа, которая требует много памяти и дискового пространства.
Также пакет OpenOffice.org умеет работать с изображениями (команда sdraw), факсами (sfax), почтовыми марками (slabel), и т. д. На сайте http://www.openoffice.org/ можно найти много информации, либо вы можете использовать меню Help программы soffice.

abiword [опции][файлы\ abiword
/usr/bin stdin stdout -file --opt --help --version
abiword - это еще одна программа для редактирования документов Microsoft Word. Она меньше и быстрее пакета soffice, хотя и не такая мощная, и идеально подходит для многих задач редактирования. Если вы задаете файлы в командной строке, то они должны существовать: программа abiword не создаст файлы автоматически.
* "org" - это часть названия программного пакета.
t Пакет soffice включает в себя отдельные программы Writer (команда swriter) для работы с текстом, Calc (scale) для работы с электронными таблицами и impress (simpress) для создания презентаций, которые при желании вы можете запускать отдельно.

gnumeric [опции][файлъ\ gnumeric
/usr/bin stdin stdout -file --opt —help —version