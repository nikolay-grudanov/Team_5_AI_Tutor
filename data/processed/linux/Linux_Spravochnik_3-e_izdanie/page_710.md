---
source_image: page_710.png
page_number: 710
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.74
tokens: 11482
characters: 1019
timestamp: 2025-12-24T03:47:17.082216
finish_reason: stop
---

[address1[,address2]]h

Скопировать содержимое пространства копий в специальный временный буфер. Предыдущее содержимое специального буфера уничтожается. Команду h можно использовать для сохранения строки перед редактированием.

Пример

# Редактировать строку; отобразить изменения;
# отобразить исходный вариант
/Linux/{
h
s/.*Linux \(.\\) .*/\1:/
p
x
}

Пример ввода:

This describes the Linux ls command.
This describes the Linux cp command.

Пример вывода:

ls:
This describes the Linux ls command.
cp:
This describes the Linux cp command.

[address1[,address2]]H

Добавить содержимое пространства шаблонов (предваряемое символом новой строки) к содержимому специального буфера. Символ новой строки добавляется, даже если буфер пуст. Команда H обеспечивает пошаговое копирование. См. примеры для команд g и G.

[address1]i\
text

Вставить текст text перед каждой строкой, соответствующей указанному адресу. (См. описание параметра text в информации по команде a).

Пример

/Item 1/i\
The five items are listed below: