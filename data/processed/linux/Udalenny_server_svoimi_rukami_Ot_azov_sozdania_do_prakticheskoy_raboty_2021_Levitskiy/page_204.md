---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.98
tokens: 6306
characters: 1110
timestamp: 2025-12-24T04:00:37.064629
finish_reason: stop
---

plain = {
    something = something-else
}
fcc-mit-ticketflags = true

[realms]
LAB.LOCAL = {
    kdc = dc
    admin_server = dc
    default_domain = MY.COMPANY
}

[domain_realm]
.lab.local = MY.COMPANY
lab.local = MY.COMPANY
[login]
krb4_convert = false
krb4_get_tickets = false

Теперь проверим, работает ли Kerberos и можем ли мы аутентифицироваться в домене:

kinit пользователь@MY.COMPANY

Здесь нужно указать имя пользователя, зарегистрированного в домене MY.COMPANY. Имя домена нужно писать заглавными буквами.

Если аутентификация прошла успешно, и вы не получили сообщения об ошибке, значит вы все сделали правильно. В результате вам будет назначен тикет Kerberos. Просмотреть все тикеты можно командой klist, а уничтожить все тикеты - командой kdestroy.

12.5. Настройка Samba

Следующий шаг - это настройка Samba. Вам нужно отредактировать файл /etc/samba/smb.conf, в котором прописываются параметры входа в домен, а также предоставляемые нашим сервером ресурсы.

Самое главное в файле /etc/samba/smb.conf - это секция global, где описываются основные параметры Samba. Остальные секции, как правило,