---
source_image: page_128.png
page_number: 128
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.36
tokens: 7966
characters: 2580
timestamp: 2025-12-24T04:22:30.152137
finish_reason: stop
---

учетных записях. Заключительная строка в нем будет выглядеть следующим образом:

robert:x:501:501::/home/robert:/bin/bash

Вспомните формат этого файла, который мы рассматривали в разд. 3.3.1. Первый параметр — это имя. Затем стоит пароль, который спрятан в теневом файле, поэтому здесь указано x. Далее следуют идентификаторы пользователя и группы. Так получилось, что в обоих случаях свободными оказались номера, равные 501, поэтому идентификаторы одинаковы, но это далеко не всегда так. Потом идет домашний каталог пользователя. По умолчанию все каталоги создаются в папке /home и соответствуют имени пользователя.

Давайте посмотрим файл /etc/shadow. Обратите внимание, что в строке пользователя robert стоят два восклицательных знака, — мы не указывали пароль и войти в систему не можем. Я и не советую задавать пароль при создании пользователя. Это лишние мучения, потому что нужно шифровать его функцией crypt, при этом нет гарантии сложности пароля. Лучше изменить его после создания пользователя с помощью команды passwd:

passwd robert

В ответ на это вы увидите приглашение ввести пароль и пояснения о необходимости делать его сложным. Сообщение, которое выдает программа, выглядит следующим образом:

Changing password for user robert.
You can now choose the new password or passphrase.
A valid password should be a mix of upper and lower case letters, digits and other characters. You can use an 8 character long password with characters from at least 3 of these 4 classes, or a 7 character long password containing characters from all the classes. Characters that form a common pattern are discarded by the check.
A passphrase should be of at least 3 words, 12 to 40 characters long and contain enough different characters.
Alternatively, if noone else can see your terminal now, you can pick this as your password: "trial&bullet_scare".

Что по-русски звучит примерно следующим образом:

Изменяется пароль для пользователя robert.
Сейчас вы можете выбрать новый пароль или идентификационную фразу.
Хороший пароль должен состоять из заглавных и строчных букв, цифр и других знаков. Вы можете ввести пароль длиной в 8 символов с использованием значений как минимум 3 из 4 указанных классов или пароль из 7 символов, сочетающий знаки из всех классов. Пароли, содержащие часто используемые шаблоны, будут отвергнуты.
Идентификационная фраза должна состоять из 3 слов общей длиной от 12 до 40 символов и содержать разнообразные знаки.
В качестве альтернативы, если в данный момент никто кроме вас не смотрит на ваш терминал, можно использовать пароль trial&bullet_scare.