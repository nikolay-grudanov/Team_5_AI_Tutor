---
source_image: page_366.png
page_number: 366
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.89
tokens: 7728
characters: 2028
timestamp: 2025-12-24T04:55:36.340482
finish_reason: stop
---

системе. (Если локальная оболочка не возвращается после выхода из удаленной оболочки, введите любой текст, это поможет прервать соединение.)

$ exit
logout
Connection to 10.140.67.23 closed

После прерывания удаленного подключения к системе в вашем локальном системном подкаталоге появится файл ~.ssh/known_hosts. Он содержит открытый ключ удаленного хоста вместе с его IP-адресом. Открытый и закрытый ключи вашего сервера хранятся в каталоге /etc/ssh:

$ ls .ssh
known_hosts
$ cat .ssh/known_hosts
10.140.67.23 ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEAoyfJK1YwZhNmpHE4yLPZAZ9ZNEdRE7I159f3IyGiH21Ijfqs
NYFR10Z1BL1YyTQi06r/9019GwCaJ753InQ8FWHW+O0YOG5pQmghhn
/x0LD2uUb6egOu6zim1NEC
JwZf5DWkKdy4euCUEMsqADh/WYeuOSoZ0pp2IAVCdh6
w/PIHMF1HVR069cvdv+OTL4vD0X8llSpw
0ozqRptz2UQgQBBbBjK1RakD7fY1TrWv
NQhYG/ugt gPaY4JDYeY60BzcadpxZmf7EYUw0ucXGVQ1a
NP/erIDOQ9rA0YNzCRv
y2LYCm2/9adpAxc+UYi5UsxTw4ewSBjmsXYq//Ahaw4mjw==

СОВЕТ
При следующих подключениях этого пользователя к серверу по адресу 10.140.67.23 он будет аутентифицироваться с помощью сохраненного ключа. Если сервер изменяет свой ключ (это происходит, если операционная система переустановлена или изменены ключи), попытки подключиться к системе приведут к отказу в соединении и выводу предупреждения о том, что вы можете подвергнуться атаке. Если ключ действительно изменился, то чтобы снова получить доступ по ssh к этому адресу, просто удалите ключ хоста (всю строку) из файла known_hosts и скопируйте новый ключ.

Удаленное выполнение команд с помощью команды ssh
Помимо входа в удаленную оболочку, команда ssh может использоваться для удаленного выполнения команды и возврата выходных данных в локальную систему, например:

$ ssh johndoe@10.140.67.23 hostname
johndoe@10.140.67.23's password: ***********
host01.example.com

В примере команда hostname выполняется от имени пользователя johndoe в системе Linux, расположенной по IP-адресу 10.140.67.23. Выходные данные команды — это имя удаленного хоста (в данном случае host01.example.com), который появляется на локальном экране.