---
source_image: page_102.png
page_number: 102
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.17
tokens: 7767
characters: 1684
timestamp: 2025-12-23T23:05:34.927322
finish_reason: stop
---

Опция -n +2 указывает команде tail выводить содержимое файла, начиная со строки 2, удаляя таким образом заголовок поля.

Вы также можете предоставить команде cut список полей, которые необходимо извлечь. Например, -f1-3 извлечет поля с 1 по 3, а -f1, 4 — поля 1 и 4.

Итерация данных с разделителями

Хотя для извлечения целых столбцов данных можно использовать команду cut, иногда при обработке файла требуется извлекать поля построчно. В этом случае вам лучше всего воспользоваться командой awk.

Предположим, вы хотите проверить хеш пароля каждого пользователя, который хранится в файле csvex.txt, на соответствие файлу со словарем известных паролей passwords.txt (примеры 6.6 и 6.7).

Пример 6.6. csvex.txt

"name","username","phone","password hash"
"John Smith","jsmith","555-555-1212",5f4dcc3b5aa765d61d8327deb882cf99
"Jane Smith","jnsmith","555-555-1234",e10adc3949ba59abbe56e057f20f883e
"Bill Jones","bjones","555-555-6789",d8578edf8458ce06fbc5bb76a58c5ca4

Пример 6.7. passwords.txt

password,md5hash
123456,e10adc3949ba59abbe56e057f20f883e
password,5f4dcc3b5aa765d61d8327deb882cf99
welcome,40be4e59b9a2a2b5dfffb918c0e86b3d7
ninja,3899dcbab79f92af727c2190bbd8abc5
abc123,e99a18c428cb38d5f260853678922e03
123456789,25f9e794323b453885f5181f1b624d0b
12345678,25d55ad283aa400af464c76d713c07ad
sunshine,0571749e2ac330a7455809c6b0e7af90
princess,8afa847f50a716e64932d995c8e7435a
qwerty,d8578edf8458ce06fbc5bb76a58c5c

Вы можете извлечь хеш пароля каждого пользователя из файла csvex.txt, следующим образом используя команду awk:

$ awk -F "," '{print $4}' csvex.txt

"password hash"
5f4dcc3b5aa765d61d8327deb882cf99
e10adc3949ba59abbe56e057f20f883e
d8578edf8458ce06fbc5bb76a58c5ca4