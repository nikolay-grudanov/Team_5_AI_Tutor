---
source_image: page_322.png
page_number: 322
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.79
tokens: 5651
characters: 1712
timestamp: 2025-12-24T04:16:20.911901
finish_reason: stop
---

попробуем заставить Vim распознавать их, чтобы мы могли быстро исправить их в Vim.

**Компиляция проекта в Vim**

Вместо того чтобы вызывать команду make в командной оболочке, попробуем выполнить компиляцию проекта непосредственно из редактора Vim. Убедитесь, что находитесь в каталоге *code/quickfix/wakeup* и в нем присутствует файл *Makefile*, а затем запустите редактор:

⇒ $ pwd; ls
~/code/quickfix/wakeup
Makefile wakeup.c wakeup.h
⇒ $ vim -u NONE -N wakeup.c

Теперь в редакторе Vim можно вызвать команду :make:

⇒ :make
gcc   -c -o wakeup.o wakeup.c
wakeup.c:68: error: conflicting types for 'generatePacket'
wakeup.h:3: error: previous declaration of 'generatePacket' was here
make: *** [wakeup.o] Error 1
Press ENTER or type command to continue

Мы получили тот же результат, что и выше, за исключением того, что Vim автоматически проанализировал полученный вывод. Редактор не просто вывел результаты работы команды make на экран, он проанализировал каждую строку, извлек имена файлов, номера строк и тексты сообщений об ошибках, и для каждой ошибки или предупреждения создал запись в списке результатов. Мы можем перемещаться по этим записям взад и вперед, а Vim будет переходить к строкам в исходном коде, соответствующим этим записям. Согласно документации Vim (:h quickfix http://vimdoc.sourceforge.net/htmldoc/quickfix.html#quickfix), это дает возможность «ускорить цикл правка — компиляция — правка».

После выполнения команды :make Vim переходит к первой записи в списке результатов. В данном случае вы заметите, что он установит курсор в файле *wakeup.c* в начало следующей функции:

void generatePacket(uint8_t *mac, uint8_t *packet)
{
    int i, j, k;
    k = 6;
    for (i = 0; i <= 15; i++)