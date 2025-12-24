---
source_image: page_095.png
page_number: 95
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.16
tokens: 5920
characters: 1215
timestamp: 2025-12-24T04:06:42.876531
finish_reason: stop
---

Если несколько программ в пути поиска имеют одинаковые названия (скажем, /usr/bin/who и /usr/local/bin/who), то команда which выщаст первую из них.

type [опции] команды        bash
встроенная команда   stdin stdout -file —opt --help -version

Команда type, как и which, осуществляет поиск исполняемых файлов в пути поиска вашего командного процессора.

$ type grep who
grep is /bin/grep
who is /usr/bin/who

Однако команда type является встроенной в командный процессор, тогда как which - это программа на диске.

$ type which type rm if
which is /usr/bin/which
type is a shell builtin
rm is aliased to /bin/rm'
if is a shell keyword

Так как type встроена в командный процессор, она работает быстрее which; однако она доступна только тогда, когда вы работаете в bash.

whereis [опции] файлы        util-linux
/usr/bin   stdin stdout -file --opt --help --version

Команда whereis осуществляет попытку найти заданные файлы в жестко запрограммированном списке директорий. Она может искать исполняемые файлы, документацию и файлы с исходным кодом. Команда whereis несколько неудобная, поскольку ее список директорий может не включать нужную вам директорию.

Полезные опции
-b        Выводить список только исполняемых