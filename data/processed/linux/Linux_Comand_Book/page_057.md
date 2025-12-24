---
source_image: page_057.png
page_number: 57
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.02
tokens: 5859
characters: 998
timestamp: 2025-12-24T04:05:57.420867
finish_reason: stop
---

$ pwd
/users/smith/mydir

basename путь
/bin stdin stdout -file -opt —help —version

Команда basename выводит последний компонент пути к файлу; поэтому, например, для примера, показанного выше, результат будет следующим.
$ basename /users/smith/mydir
mydir

dirname путь
/usr/bin stdin stdout -file --opt —help —version

Команда dirname отбрасывает последний компонент пути к файлу.

$ dirname /users/smith/mydir /users/smith

Команда dirname просто обрабатывает строку, которая является именем директории. Она не изменяет вашу текущую рабочую директорию.

mkdir [опции] директории
/bin stdin stdout -file —opt —help —version
Команда mkdir создает одну или несколько директорий.

$ mkdir dl d2 d3

Полезные опции
-p Если вы указываете путь к директории (а не просто имя директории), то команда создаст все необходимые родительские директории автоматически. Например, командатксИг -р /one/two/three создаст директории /one и /one/two, если они не существуют, а затем и саму директорию /one/two/three