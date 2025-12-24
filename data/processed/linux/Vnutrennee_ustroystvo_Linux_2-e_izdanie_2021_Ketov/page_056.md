---
source_image: page_056.png
page_number: 56
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.82
tokens: 7284
characters: 1115
timestamp: 2025-12-24T04:33:19.659183
finish_reason: stop
---

и командой tput(1), можно модифицировать приглашение по своему предпочтению (листинг 2.29).

Листинг 2.29. Переменная окружения PS1

finn@ubuntu:~$ man 5 terminfo

enter_reverse_mode ... rev ... mr ... turn on reverse video mode
enter_dim_mode ... dim ... mh ... turn on half-bright mode
exit_attribute_mode ... sgr0 ... me ... turn off all attributes

finn@ubuntu:~$ tput rev | od -a
0000000 esc [ 7 m
0000004

finn@ubuntu:~$ tput dim | od -a
0000000 esc [ 2 m
0000004

finn@ubuntu:~$ tput sgr0 | od -a
0000000 esc ( B esc [ m
0000006

finn@ubuntu:~$ PS1='\e[2m\t\n\e(B\e[m\u@h \e[7m\w\e(B\e[m \$ '
13:17:25
finn@ubuntu $ cd /etc
13:17:25
finn@ubuntu /etc $

Или даже можно воспользоваться поддержкой символов unicode(7) в UTF-8(7) представлении на терминале¹ (листинг 2.30).

Листинг 2.30. Переменная окружения PS1

finn@ubuntu:~$ stty
speed 38400 baud; line = 0;
eol = M-^?; eol2 = M-^?; swtch = M-^?;
ixany iutf8

¹ В этом примере эмулятор терминала в графическом интерфейсе по умолчанию имеет нужные шрифты, а на консоли необходимо загрузить подходящий Unicode-шрифт, например командой setfont Uni2-Terminus16.