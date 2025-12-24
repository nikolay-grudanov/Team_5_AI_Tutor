---
source_image: page_159.png
page_number: 159
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.39
tokens: 5850
characters: 987
timestamp: 2025-12-24T04:08:03.159842
finish_reason: stop
---

$ whoami
smith
$ groups
smith users
$ groups jones root
jones .- jones users
root : root bin daemon sys adm disk wheel src

* Разные системы могут хранить списки членов групп по-разному.

groupadd [опции] группа . shadow-utils
/usr/sbin stdin stdout -file —opt --help -version
Команда groupadd создает новую группу. В большинстве случаев следует использовать опцию -f для того, чтобы предотвратить дублирование групп.

#groupadd -f friends

Полезные опции
-g gid    Задать ваш собственный числовой идентификатор группы вместо того, чтобы команда groupadd выбирала его сама
-f        Если группа уже существует, сообщить об этом и завершить работу

groupdel группа shadow-utils
/usr/sbin stdin stdout -file --opt --help --version

Команда groupdel удаляет существующую группу.

#groupdel friends

Перед тем как сделать это, стоит определить все файлы, у которых идентификатор группы установлен на заданную группу, чтобы вы смогли обработать их в дальнейшем:

#find / -group friends -print