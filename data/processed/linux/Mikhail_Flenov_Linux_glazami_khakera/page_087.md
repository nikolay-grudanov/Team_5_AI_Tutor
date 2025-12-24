---
source_image: page_087.png
page_number: 87
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.00
tokens: 7932
characters: 2284
timestamp: 2025-12-24T04:21:14.105559
finish_reason: stop
---

network-interface-security (network-interface/lo) start/running
network-interface-security (networking) start/running
networking start/running
procps stop/waiting
tty6 start/running, process 1058
console-font stop/waiting
network-interface-container stop/waiting
ureadahead stop/waiting
mflenov@ubuntuseru:~$ sudo /etc/init.d/apache2 status
[sudo] password for mflenov:
* apache2 is running
mflenov@ubuntuseru:~$ sudo /etc/init.d/apache2 stop
* Stopping web server apache2
*
mflenov@ubuntuseru:~$ sudo /etc/init.d/apache2 status
* apache2 is not running
mflenov@ubuntuseru:~$ sudo /etc/init.d/apache2 start
* Starting web server apache2
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message
*
mflenov@ubuntuseru:~$ sudo /etc/init.d/apache2 status
* apache2 is running
mflenov@ubuntuseru:~$

Рис. 3.3. Управление службами в консоли

Если вы запускаете или останавливаете сервис с помощью подобных команд, то это носит только временный характер. Если вы хотите, чтобы изменение носило постоянный характер и состояние службы сохранялось после перезапуска, то можно создать файл /etc/init/имя_сервиса.override, в котором будет содержаться только слово manual. Из командной строки такое можно выполнить с помощью команды echo и перенаправить результат команды в файл:

echo 'manual' > /etc/init/mysql.override

Команда echo 'manual' говорит о том, что нужно напечатать слово manual. Оно будет напечатано на стандартном выводе, которым по умолчанию является окно терминала. Символ > говорит, что вывод команды слева нужно перенаправить в поток справа. А справа идет файл. Значит, теперь слово будет напечатано не на экране, а записано в файл.

Но папка /etc требует прав администратора для работы, а это значит, что команда завершится ошибкой, если ее выполнять с правами простого пользователя.

Проблема решается использованием команды sudo:

sudo bash -c "echo 'manual' > /etc/init/mysql.override"

Команда bash -c говорит о том, что нужно просто выполнить команду, которая идет дальше в кавычках. Использование команды bash -c вызвано тем, что команда sudo не сможет работать с командой echo и перенаправить наш вывод в файл, потому что echo — это команда не ОС, а bash.