---
source_image: page_508.png
page_number: 508
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.94
tokens: 11554
characters: 1206
timestamp: 2025-12-24T03:37:50.743286
finish_reason: stop
---

---
primary_language: ru
is_rotation_valid: True
rotation_correction: 0
is_table: True
is_diagram: False
---
—license
Отобразить информацию о лицензировании dpkg и завершить работу. Написание —licence также считается верным и приводит к тому же результату.

—version
Отобразить информацию о версии dpkg и завершить работу.

Действия dpkg-deb
Следующие действия могут быть указаны dpkg и будут переданы на выполнение dpkg-deb. См. также описание dpkg-deb.

—b dir [archive ], —build dir [archive ]
Создать пакет.

—c archive, —contents archive
Отобразить содержимое пакета.

—e, —control archive dir
Извлечь из пакета информацию об управлении.

—f archive [control-fields ], —field archive [control-fields ]
Отобразить управляющее поле или поля пакета.

—I archive [control-files ], —info archive [control-files ]
Отобразить информацию о пакете.

—fsys-tarfile archive
Отобразить файловую систему tar-файла, содержащегося в архиве.

—x archive dir, —extract archive dir
Извлечь файлы из пакета.

—X archive dir, —vextract archive dir
Извлечь файлы из пакета, отображая их имена.

Параметры

—abort-after=num
Произвести аварийное завершение после указанного количества ошибок. Значение по умолчанию равно 50.