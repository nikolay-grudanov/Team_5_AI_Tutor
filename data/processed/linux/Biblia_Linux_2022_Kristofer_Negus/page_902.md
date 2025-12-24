---
source_image: page_902.png
page_number: 902
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.39
tokens: 7587
characters: 2181
timestamp: 2025-12-24T05:10:33.833850
finish_reason: stop
---

6. Для установки логических типов SELinux, необходимых для того, чтобы пользователь phil мог получить доступ к своему домашнему каталогу через клиент Samba, как суперпользователь из оболочки введите следующее:

# setsebool -P samba_enable_home_dirs on
# systemctl restart smb
# systemctl restart nmb

и перезапустите службы smb и nmb.

7. В локальной системе используйте команду smbclient, чтобы указать, что общий ресурс [homes] доступен:

# smbclient -L localhost
Enter TESTGROUP\root's password: <ENTER>
Anonymous login successful

<table>
  <tr>
    <th>Sharename</th>
    <th>Type</th>
    <th>Comment</th>
  </tr>
  <tr>
    <td>--------</td>
    <td>----</td>
    <td>-------</td>
  </tr>
  <tr>
    <td>homes</td>
    <td>Disk</td>
    <td>Home Directories</td>
  </tr>
  <tr>
    <td colspan="3">...</td>
  </tr>
</table>

8. Чтобы подключиться к разделу [homes] из окна Nautilus (Файлы) в локальной системе сервера Samba для пользователя phil1 таким образом, чтобы можно было перетаскивать файлы в эту папку, выполните следующие действия:
а) откройте Nautilus (Файлы), нажав на соответствующий значок;
б) на панели слева выберите Other Locations (Другие места) и нажмите кнопку Connect to Server (Подключиться к серверу);
в) введите адрес сервера, например smb://localhost/phil/;
г) при появлении запроса выберите пункт Registered User (Зарегистрированный пользователь), введите имя пользователя phil, домен (TESTGROUP) и пароль этого пользователя;
д) откройте еще одно окно Nautilus (Файлы) и перенесите файл в домашнюю папку пользователя phil.

9. Чтобы открыть брандмауэр так, чтобы любой, кто имеет доступ к серверу, мог получить доступ к службе Samba (демоны smbd и nmbd), откройте окно Firewall (Межсетевой экран) и установите флажки Samba и samba-client (как для Runtime, так и для Permanent). Если в вашей системе работает служба iptables (не служба firewalld), измените файл /etc/sysconfig/iptables так, чтобы брандмауэр выглядел следующим образом (правила, которые нужно добавить, выделены жирным шрифтом):

*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
-A INPUT -p icmp -j ACCEPT