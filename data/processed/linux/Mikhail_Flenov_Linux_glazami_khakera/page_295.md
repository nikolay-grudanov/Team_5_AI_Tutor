---
source_image: page_295.png
page_number: 295
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.04
tokens: 7819
characters: 1660
timestamp: 2025-12-24T04:27:15.042900
finish_reason: stop
---

# Проверка баннера произвольного размера
$url = $various if grep $url =~ m%$_%, @various;

# Всплывающее окно
$url = $closewindow if grep $url =~ m%$_%, @popup_window;

# Отдельный сайт, не внесенный в список в начале файла
$url = "$YOURSITE/empty.gif" if $url =~ m%hitbox\.com/Hitbox\?%;

if ($LOG and $url ne $prev)
{
    my ($sec, $min, $hour, $mday, $mon, $year) = localtime;
    printf LOG "%2d.%02d.%2d %2d:%02d:%04d: %s\r\n",
        $mday, $mon + 1, $year + 1900, $hour, $min, $sec,
        "$who $prev > $url";
}

print "$url $who $ident $method\n";
}
close LOG if $LOG;

Я постарался снабдить код в листинге 9.2 комментариями. Если у вас есть опыт программирования на Perl, то дальнейшие действия вы выполните без проблем.

Сохраните эту программу в файле /usr/etc/redirector и установите для squid права на его исполнение. После этого добавьте в файл squid.conf следующую строку:

redirect_program /usr/local/etc/squid/redirector

Чтобы эта программа заработала, создайте на своем веб-сервере файлы со следующими именами:

□ 468_60.gif — картинка размером 468×60;
□ 100_100.gif — картинка размером 100×100;
□ empty.gif — картинка, которая будет заменять нестандартные баннеры. Лучше всего ее сделать размером 1×1 пиксел, чтобы она не испортила дизайн сайта;
□ close.htm — файл HTML, который будет закрывать всплывающие окна. В нем нужно поместить всего лишь функцию, которая будет закрывать окно. Для этого служит функция JavaScript window.close(). Пример содержимого файла показан в листинге 9.3.

Все эти файлы должны лежать на веб-сервере в одном каталоге. Не забудьте в сценарии (в переменной $YOURSITE) указать правильный путь к этому каталогу.