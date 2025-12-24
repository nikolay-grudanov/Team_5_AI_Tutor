---
source_image: page_322.png
page_number: 322
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.48
tokens: 11505
characters: 1091
timestamp: 2025-12-24T03:29:30.309852
finish_reason: stop
---

Параметры

+ [options] [original2]
Повторное наложение исправлений (заплат) с другими параметрами или другим исходным файлом.

-b, --backup
Создать резервные копии изменяемых файлов.

-z suffix, --suffix=suffix
Сохранить исходный файл под именем original.suffix.

-B prefix, --prefix=prefix
Добавить prefix к имени резервной копии исходного файла.

-c, --context
Интерпретировать patchfile как контекстный diff-файл (context diff).

-d dir, --directory=dir
Перейти в указанный каталог, прежде чем применять исправления.

-D string, --ifdef=string
Отметить все изменения следующим образом:
ifdef
string
endif

-e, --ed
Считать, что patchfile содержит команды редактора ed.

-E, --remove-empty-files
Если в результате работы patch появились пустые файлы, удалить их.

-f, --force
Принудительно наложить все изменения (заплаты), даже некорректные. Если исходный файл не существует, изменения не накладываются. Изменять файлы с неправильно указанной версией, считать наложенные изменения необратимыми.

-i file, --input=file
Читать файл изменений из указанного файла, а не со стандартного ввода.