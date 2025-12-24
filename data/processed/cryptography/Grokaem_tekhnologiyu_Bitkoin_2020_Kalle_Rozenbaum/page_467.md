---
source_image: page_467.png
page_number: 467
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.67
tokens: 7547
characters: 1981
timestamp: 2025-12-24T08:43:23.595036
finish_reason: stop
---

созданных биткоинов, которые нельзя потратить, пока не минует 100 блоков. Вызовите справку для getwalletinfo для получения более подробных сведений об информации, выводимой этой командой.

Чтобы получить зашифрованный кошелек, нужно создать новый кошелек командой encryptwallet:

$ ./bitcoin-cli -stdin encryptwallet secretpassword<ENTER>
<CTRL-D>
wallet encrypted; Bitcoin server stopping, restart to run with encrypted wallet.
↓The keypool has been flushed and a new HD seed was generated (if you are using HD).
↓You need to make a new backup.¹

Эта команда создаст новый зашифрованный кошелек. Ключ -stdin заставляет команду читать пароль из стандартного ввода, то есть команда предложит вам ввести пароль в окне терминала. Завершите ввод пароля, нажав Enter и Ctrl-D. Ключ -stdin используется, просто чтобы не указывать пароль в самой команде, потому что большинство командных оболочек, таких как bash, хранят историю команд в файле. Ключ -stdin гарантирует, что пароль не попадет в такой файл истории.

Важно создать новый зашифрованный кошелек, а не просто зашифровать существующий, потому что старый кошелек на вашем жестком диске мог быть скомпрометирован. Как отмечено в выводе команды, процесс bitcoind был остановлен. В настоящее время Bitcoin Core не может переключиться на новый файл кошелька во время работы.

Давайте запустим bitcoind и посмотрим на кошелек:

$ ./bitcoind -daemon
Bitcoin server starting
$ ./bitcoin-cli getwalletinfo
{
    "walletname": "",
    "walletversion": 169900,
    "balance": 0.00000000,
    "unconfirmed_balance": 0.00000000,
    "immature_balance": 0.00000000,
    "txcount": 0,
    "keypoololdest": 1541941063,
    "keypoolsize": 1000,
    "keypoolsize_hd_internal": 1000,

¹ Зашифрованный кошелек; сервер Bitcoin остановлен, запустите его снова, чтобы начать работу с новым зашифрованным кошельком. Пул ключей очищен и сгенерировано новое начальное число HD (если вы используете HD). Не забудьте создать резервную копию. — Примеч. пер.