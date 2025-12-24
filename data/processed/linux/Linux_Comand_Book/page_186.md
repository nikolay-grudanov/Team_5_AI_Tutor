---
source_image: page_186.png
page_number: 186
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.22
tokens: 5993
characters: 1348
timestamp: 2025-12-24T04:08:35.595054
finish_reason: stop
---

в консольном окне, например, в xterm. Она делит окно по горизонтали так, чтобы вы могли видеть то, что пишете сами, и то, что пишет ваш партнер.

$ talk friend@example.com Если ваш партнер работает в нескольких терминалах, вы можете указать один из этих терминалов для соединения.
write пользователь [tty\ Util-linux
/usr/bin stdin stdout -file --opt --help --version
Программа write более примитивна, чем talk: она отправляет строки текста от одного пользователя другому в той же Linux-системе.
$ write smith Hi, how are you? See you later.
Нажатие комбинации ЛБ завершит связь. Также программа write полезна в конвейерах для коротких одноразовых сообщений.
$ echo 'Howdy!' | write smith

mesg [y I n] SysVinit
/usr/bin stdin stdout - file - - opt - -help - -version
Программа mesg управляет тем, смогут ли talk-или write-соединения достигнуть вашего терминала. Команда mesg у разрешает их, mesg n - запрещает, а mesg - выводит текущий статус ("у" -да, или "п" - нет)*, mesg не влияет на современные программы для обмена мгновенными сообщениями, например, gaim.
$ mesg
is n
$ mesg y
tty coreutils
/usr/bin stdin stdout - file - opt --help -version
Программа tty выводит название терминального устройства (терминала), связанного с текущим командным процессором.
$ tty /dev/pts/4

Вывод на экран
echo Вывести простой текст в стандартный поток вывода