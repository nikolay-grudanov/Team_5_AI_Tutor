---
source_image: page_174.png
page_number: 174
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.72
tokens: 6410
characters: 1381
timestamp: 2025-12-24T04:00:05.920067
finish_reason: stop
---

• 3306 - порт сервера;
• ftp - имя MySQL-пользователя (его еще нужно создать!);
• password - пароль MySQL-пользователя.

Директива SQLUserInfo задает имя и структуру таблицы с информацией о пользователях. Здесь 'users' - имя таблицы, остальные поля задают, соответственно, имя пользователя, пароль, UID, GID, домашний каталог и оболочку.

Далее с помощью phpMyAdmin или клиента mysql создайте в базе данных ftpusers следующую таблицу:

CREATE TABLE `users` (
  `uuid` int(11) NOT NULL auto_increment,
  `username` varchar(32) NOT NULL,
  `password` varchar(128) NOT NULL,
  `uid` int(11) NOT NULL,
  `gid` int(11) NOT NULL,
  `homedir` varchar(50) NOT NULL,
  `shell` varchar(20) NOT NULL,
  `last_login` int(15) NOT NULL,
  `login_count` int(15) NOT NULL,
  `last_err_login` int(15) NOT NULL,
  `err_login_count` int(15) NOT NULL,
  PRIMARY KEY  (`uuid`)
) ENGINE=MyISAM;

Собственно, вот и все. Можно приступить к заполнению этой таблицы. Если вы желаете хранить пароли в зашифрованном виде, используйте тип аутентификации Backend и пароли в БД вносите через MySQL-функцию PASSWORD()¹.

9.3. Очень безопасный vsftpd

Сервер vsftpd не только очень безопасный, но и очень компактный. Функционала меньше, настраивать его придется меньше времени, меньше вероятность допустить ошибку при настройке.

¹ http://dev.mysql.com/doc/refman/5.0/en/encryption-functions.html#function_password