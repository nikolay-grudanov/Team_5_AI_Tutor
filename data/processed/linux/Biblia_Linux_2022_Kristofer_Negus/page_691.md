---
source_image: page_691.png
page_number: 691
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.75
tokens: 7565
characters: 2368
timestamp: 2025-12-24T05:04:47.741613
finish_reason: stop
---

Настройки предела устанавливаются для каждого входа в систему и действуют лишь в течение всего сеанса входа. Злоумышленник может войти в систему несколько раз, чтобы создать fork-бомбу. Таким образом, стоит также установить максимальное количество входов для учетных записей пользователей.

Максимальное количество входов можно задать для каждого пользователя по отдельности. Например, пользователю johndoe можно войти в систему Linux только один раз. Чтобы другие не могли задействовать учетную запись johndoe, установите maxlogins его учетной записи в значение 1:

johndoe    hard    maxlogins    1

Чтобы переопределить любые настройки в файле limits.conf, добавьте файлы с именем .conf в каталог /etc/security/limits.d.

Это удобный способ управлять файлом RPM или другим для добавления и удаления ограничений, не редактируя сам файл limits.conf.

Последним шагом в установке ограничений для этого ресурса является обеспечение того, чтобы модуль, использующий файл limits.conf, был включен в один из файлов конфигурации системных событий PAM. Модуль PAM, задействующий limits.conf, называется pam_limits. В приведенном далее примере команда grep проверяет, применяется ли PAM в файлах конфигурации системных событий:

# grep "pam_limits" /etc/pam.d/*
/etc/pam.d/fingerprint-auth:session required    pam_limits.so
/etc/pam.d/password-auth:session    required    pam_limits.so
/etc/pam.d/runuser:session    required    pam_limits.so
/etc/pam.d/system-auth:session    required    pam_limits.so

Ограничения по времени доступа к службам и учетным записям не обрабатываются файлом конфигурации PAM /etc/security/limits.conf. Вместо этого они обрабатываются файлом time.conf.

Временные ограничения с помощью модулей PAM

Модули PAM могут заставить всю вашу систему Linux работать в режиме PAM. Временные ограничения, такие как доступ к определенным приложениям в определенное время дня или разрешение входить в систему только в определенные дни недели, обрабатываются с помощью модулей.

Файл конфигурации PAM, который обрабатывает эти ограничения, находится в каталоге /etc/security. В следующем примере показан хорошо закомментированный файл конфигурации PAM /etc/security/time.conf:

$ cat /etc/security/time.conf
# this is an example configuration file for the pam_time module. Its
# syntax was initially based heavily on that of the shadow package (shadow-960129).