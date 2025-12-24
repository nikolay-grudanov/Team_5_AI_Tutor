---
source_image: page_473.png
page_number: 473
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.58
tokens: 7595
characters: 1983
timestamp: 2025-12-24T08:43:34.307184
finish_reason: stop
---

★ узнать адрес для отправки;
★ определить сумму для отправки: 0,001 BTC;
★ как быстро должна быть подтверждена транзакция: транзакция не срочная (нас вполне устроит, если она подтвердится в течение 20 блоков).

Я отправлю биткоины на адрес bc1qu456...5t7uulqm, но вы должны использовать другой адрес для отправки. Если у вас нет другого кошелька, создайте новый адрес в Bitcoin Core для экспериментов. Я искажил свой адрес в команде ниже, чтобы вы по ошибке не отправили на него свои деньги.

$ ./bitcoin-cli -named sendtoaddress \
    address="bc1qu456w7a5mawlgXXXXXXu03wp8wc7d65t7uulqm" \
    amount=0.001 conf_target=20 estimate_mode=ECONOMICAL
error code: -13
error message:
Error: Please enter the wallet passphrase with walletpassphrase first.¹

Вот те на! Ошибка. Как нетрудно догадаться по тексту сообщения об ошибке, закрытые ключи в файле wallet.dat оказались зашифрованы. Закрытые ключи нужны Bitcoin Core для подписания транзакции. Чтобы открыть доступ к закрытым ключам, их нужно расшифровать. Это делается с помощью команды walletpassphrase с параметром -stdin, чтобы предотвратить сохранение пароля интерпретатором командной строки, таким как bash:

$ ./bitcoin-cli -stdin walletpassphrase
secretpassword<ENTER>
300<ENTER>
<CTRL-D>

Последний аргумент, 300, это время в секундах, в течение которого кошелек должен оставаться открытым. Спустя 300 секунд кошелек автоматически закроется, если вы забудете сделать это вручную. Теперь повторим команду endtoaddress:

$ ./bitcoin-cli -named sendtoaddress \
    address="bc1qu456w7a5mawlgXXXXXXu03wp8wc7d65t7uulqm" \
    amount=0.001 conf_target=20 estimate_mode=ECONOMICAL
a13bcb16d8f41851cab8e939c017f1e05cc3e2a3c7735bf72f3dc5ef4a5893a2

На этот раз команда вывела идентификатор вновь созданной транзакции. Это означает, что деньги благополучно отправлены. Теперь можно закрыть кошелек командой walletlock:

$ ./bitcoin-cli walletlock

¹ Ошибка: сначала введите пароль к кошельку с помощью walletpassphrase. — Примеч. пер.