---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.53
tokens: 7085
characters: 759
timestamp: 2025-12-24T03:02:58.771212
finish_reason: stop
---

4 У объекта pathlib.Path есть метод exists.

5 Вызов as_postix возвращает путь в виде строки. В зависимости от ситуации можно вернуть и сам объект pathlib.Path.

6 Метод класса pathlib.Path.cmd возвращает объект pathlib.Path, соответствующий текущему рабочему каталогу. Здесь мы сразу же используем этот объект для создания config_path путем объединения его со строковым значением rc_name.

7 Метод класса pathlib.Path.home возвращает объект pathlib.Path, соответствующий домашнему каталогу активного пользователя.

8 Создаем объект pathlib.Path на основе содержащегося в file относительного пути, после чего вызываем его метод resolve для получения абсолютного пути.

9 Возвращает родительский объект pathlib.Path непосредственно из самого объекта file_path.