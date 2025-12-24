---
source_image: page_751.png
page_number: 751
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.87
tokens: 11836
characters: 1997
timestamp: 2025-12-24T03:49:19.062987
finish_reason: stop
---

user@localhost$ cd ..

Затем запишем изменения между версиями 1.1 и 2.0 в рабочий каталог, поместим изменения в репозиторий, а также создадим метку:

user@localhost$ diff -Naur foo-1.1 foo-2.0 | (cd foo; patch -Np1)
user@localhost$ cd foo
user@localhost$ cvs commit -m 'Imported version 2.0'
user@localhost$ cvs tag foo-2_0

Теперь можно воспользоваться командой log для просмотра истории файлов, более старых версий файлов, и продолжить разработку с контролем версий.

Импортирование из RCS

Если вы переносите проект из RCS в CVS, следование приведенным ниже инструкциям поможет вам создать рабочий репозиторий CVS. Описанные операции включают внесение изменений непосредственно в репозиторий, поэтому должны выполняться с должной осторожностью.

Прежде чем начать, убедитесь, что никакие импортируемые в CVS файлы не заблокированы RCS. Создайте новый репозиторий CVS и модуль (либо новый модуль в существующем репозитории). Затем создайте в репозитории CVS набор каталогов, который отражает структуру каталогов импортируемого проекта. И, наконец, скопируйте все файлы версий (они имеют расширение ,v) проекта (которые могут быть в подкаталогах RCS) в соответствующие каталоги в репозитории (без подкаталогов RCS).

Например, сначала скопируем каталог, который управляет RCS, создадим пустой каталог для новой структуры CVS, импортируем каталог, а затем извлечем файлы в рабочий каталог:

user@localhost$ mv foo foo-rcs
user@localhost$ mkdir foo
user@localhost$ cd foo
user@localhost$ cvs import -m 'New empty project' foo vendor start
user@localhost$ cd ..
user@localhost$ mv foo foo.bak
user@localhost$ cvs checkout foo

Затем создадим каталоги и добавим их в репозиторий, чтобы воспроизвести структуру проекта RCS:

user@localhost$ cd foo
user@localhost$ mkdir dir
user@localhost$ cvs add dir
user@localhost$ cd ..

Теперь скопируем файлы версий (,v) проекта RCS в репозиторий проекта CVS:

user@localhost$ cp -p foo-rcs/*,v $CVSROOT/foo
user@localhost$ cp -p foo-rcs/dir/*,v $CVSROOT/foo/dir