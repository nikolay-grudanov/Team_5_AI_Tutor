---
source_image: page_363.png
page_number: 363
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.50
tokens: 7642
characters: 2145
timestamp: 2025-12-24T04:55:28.438215
finish_reason: stop
---

Большинство систем Linux обеспечивают безопасность оболочки клиента, а многие из них — и безопасность оболочки сервера. Например, если вы используете дистрибутив Fedora или RHEL, клиентские и серверные программные пакеты, содержащие инструменты ssh, — это пакеты openssh, openssh-clients и openssh-server. Выглядит это следующим образом:

# yum list installed | grep openssh
...
openssh.x86_64 7.9p1-5.fc30 @anaconda
openssh-clients.x86_64 7.9p1-5.fc30 @anaconda
openssh-server.x86_64 7.9p1-5.fc30 @anaconda

В дистрибутиве Ubuntu установлен только пакет openssh-clients. Он включает в себя все функции пакета openssh. Если нужно установить сервер, используйте команду sudo apt-get install openssh-server:

$ sudo dpkg --list | grep openssh
openssh-client/bionic-updates,bionic-security,now 1:7.6p1-4ubuntu0.3 amd64 [installed]
    secure shell (SSH) client, for secure access to remote machines
openssh-client-ssh1/bionic 1:7.5p1-10 amd64
    secure shell (SSH) client for legacy SSH1 protocol

openssh-sftp-server/bionic-updates,bionic-security,now 1:7.6p1-4ubuntu0.3 amd64 [installed]
    secure shell (SSH) sftp server module, for SFTP access from remote machines
$ sudo apt-get install openssh-server

Запуск службы openssh-server

Системы Linux, которые поставляются с уже установленным пакетом openssh-server, не всегда настроены на его автоматический запуск. Управление службами Linux (см. главу 15 «Запуск и остановка служб») может различаться в зависимости от различных дистрибутивов. В табл. 13.1 показаны команды, определяющие, что ssh-демон сервера — sshd — запущен и работает.

Таблица 13.1. Команды, определяющие состояние демона sshd

<table>
  <tr>
    <th>Дистрибутив</th>
    <th>Команда</th>
  </tr>
  <tr>
    <td>RHEL 6</td>
    <td>chkconfig --list sshd</td>
  </tr>
  <tr>
    <td>Fedora и RHEL версии 7 и позже</td>
    <td>systemctl status sshd.service</td>
  </tr>
  <tr>
    <td>Ubuntu</td>
    <td>systemctl status ssh.service</td>
  </tr>
</table>

Если демон sshd в данный момент не запущен, его можно запустить, выполнив одну из команд, перечисленных в табл. 13.2. Для их работы требуются права суперпользователя.