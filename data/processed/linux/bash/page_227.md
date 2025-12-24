---
source_image: page_227.png
page_number: 227
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.90
tokens: 7299
characters: 1306
timestamp: 2025-12-23T23:10:22.891833
finish_reason: stop
---

Как говорилось раньше, аргумент, который вы хотите изменить, обозначается знаком вопроса (?). Fuzzer.sh будет выполнять программу fuzzme.exe снова и снова, каждый раз добавляя ко второму аргументу еще один символ. Если это делать вручную, вы увидите следующее:

$ fuzzme.exe arg1 a
$ fuzzme.exe arg1 aa
$ fuzzme.exe arg1 aaa
$ fuzzme.exe arg1 aaaa
$ fuzzme.exe arg1 aaaaa

.

.

.

Реализация

В качестве целевого приложения используется программа fuzzme.exe. Мы возьмем два аргумента командной строки, объединим их и выведем объединенную строку на экран. Вот пример выполнения программы:

$ ./fuzzme.exe 'this is' 'a test'

The two arguments combined is: this is a test

Пример 15.1 предоставляет исходный код для fuzzme.exe, написанный на языке C.

Пример 15.1. fuzzme.c

#include <stdio.h>
#include <string.h>

// Внимание: эта программа не безопасна и предназначена только для демонстрации

int main(int argc, char *argv[])
{
    char combined[50] = "";
    strcat(combined, argv[1]);
    strcat(combined, " ");
    strcat(combined, argv[2]);
    printf("The two arguments combined is: %s\n", combined);

    return(0);
}

Программа использует функцию strcat(), которая, по своей сути, небезопасна и может привести к переполнению буфера. Кроме того, она не выполняет проверку ввода из командной строки.