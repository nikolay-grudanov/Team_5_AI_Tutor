---
source_image: page_437.png
page_number: 437
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.36
tokens: 7441
characters: 1804
timestamp: 2025-12-24T04:57:36.650348
finish_reason: stop
---

Запуск и остановка служб

Запуск, остановка и перезапуск служб обычно относятся к необходимым задачам, другими словами, задачам управления службами без перезагрузки сервера. Например, если вы хотите временно остановить службу, подойдет этот раздел книги. Но если хотите остановить службу и не позволять ей перезапускаться при перезагрузке сервера, то действительно нужно отключить ее, как описано в разделе «Подключение постоянных служб» далее в этой главе.

Остановка и запуск служб SysVinit

Основная команда для остановки и запуска служб SysVinit — это команда service. С ее помощью имя нужной службы ставится на второе место в командной строке. В конце указывается подходящее действие для службы: stop, start, restart и т. д. В следующем примере показано, как остановить службу cups. Обратите внимание на значение ОК — оно дает понять, что служба cupsd была успешно остановлена:

# service cups status
cupsd (pid 5857) is running...
# service cups stop
Stopping cups:      [ ОК ]
# service cups status
cupsd is stopped

Чтобы запустить службу, используйте параметр start вместо параметра stop в конце команды service, как показано далее:

# service cups start
Starting cups:      [ ОК ]
# service cups status
cupsd (pid 6860) is running...

Для перезапуска службы SysVinit используется параметр restart. Он останавливает службу и затем сразу же запускает ее снова:

# service cups restart
Stopping cups:      [ ОК ]
Starting cups:      [ ОК ]
# service cups status
cupsd (pid 7955) is running...

Когда служба уже остановлена, параметр restart генерирует состояние FAILED при попытке остановить ее еще раз. Однако, как показано в следующем примере, служба успешно запускается при попытке перезапуска:

# service cups stop
Stopping cups:      [ ОК ]
# service cups restart
Stopping cups:      [FAILED]