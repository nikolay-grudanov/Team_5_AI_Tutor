---
source_image: page_294.png
page_number: 294
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.11
tokens: 7731
characters: 1151
timestamp: 2025-12-24T04:26:57.921446
finish_reason: stop
---

```perl
{
    select LOG;
    $| = 1;
    select STDOUT;
}
}

@b468_60 = qw (
    www\.$sitename\.com/cgi/
    # Добавьте сюда описания URL-адресов с баннерами
    # размером 468x60
);

@b100_100= qw (
    www\.$sitename\.com/cgi/
    # Добавьте сюда описания URL-адресов с баннерами
    # размером 100x100
);

@various = qw (
    www\.$sitename\.com/cgi/
    # Добавьте сюда описания URL-адресов с нестандартными
    # размерами баннера
);

@popup_window = qw (
    ^http://members\.tripod\.com/adm/popup/.+html
    ^http://www\.geocities\.com/ad_container/pop\.html
    ^http://www\.geocities\.com/toto\?
    # Добавьте сюда описания URL-адресов, с которых
    # высаживают всплывающие окна
);

# Описание расположения картинок
$b468_60    = "$YOURSITE/468_60.gif";
$b100_100   = "$YOURSITE/100_100.gif";
$various    = "$YOURSITE/empty.gif";
$closewindow = "$YOURSITE/close.htm";

while (<>)
{
    ($url, $who, $ident, $method) = /^(\S+) (\S+) (\S+) (\S+)$/;
    $prev = $url;

    # Проверка баннера 468x60
    $url = $b468_60 if grep $url =~ m%$_%, @b468_60;

    # Проверка баннера 100x100
    $url = $b100_100 if grep $url =~ m%$_%, @b100_100;
}