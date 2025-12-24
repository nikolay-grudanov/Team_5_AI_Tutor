---
source_image: page_697.png
page_number: 697
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.32
tokens: 7471
characters: 2021
timestamp: 2025-12-24T05:04:55.377516
finish_reason: stop
---

ПРИМЕЧАНИЕ
Ограничения pam_cracklib не применяются к суперпользователю, если вы не задействуете параметр enforce_for_root.

Использование команды sudo вместе с модулями PAM

Чтобы разрешить отслеживание применения учетной записи суперпользователя отдельными лицами (см. главу 22 «Базовые методы обеспечения безопасности»), вы должны ограничить использование команды su и поощрять использование команды sudo. Если в вашей организации такая политика, можете сделать это с помощью PAM всего за несколько шагов.

Команда su может использовать модули PAM, что значительно упрощает процесс. Она задействует модуль PAM pam_wheel для проверки пользователей в группе wheel. Здесь показан файл конфигурации /etc/pam.d/su:

# cat /etc/pam.d/su
#%PAM-1.0
auth      required     pam_rootok.so
auth      sufficient   pam_rootok.so
# Uncomment the following line to implicitly trust users
# in the "wheel" group.
#auth      sufficient   pam_wheel.so trust use_uid
# Uncomment the following line to require a user to be
# in the "wheel" group.
auth      required     pam_wheel.so use_uid
auth      substack     system-auth
auth      include      postlogin
account   sufficient   pam_succeed_if.so uid = 0 use_uid quiet
account   include      system-auth
password  include      system-auth
session   include      system-auth
session   include      postlogin
session   optional     pam_xauth.so

Поначалу, чтобы ограничить использование команды su, если вы задействуете группу wheel в качестве административной, необходимо переназначить свою группу (см. главу 11 «Управление учетными записями»). Если вы не используете группу wheel, просто не назначайте никого в нее в будущем.

Далее нужно отредактировать файл конфигурации /etc/pam.d/su. Удалите знак комментария # из следующей строки:

#auth      required     pam_wheel.so use_uid

После таких изменений модуль PAM отключает использование команды. Администраторы теперь должны применять команду sudo, которую система отслеживает и для которой обеспечивает желаемую среду (см. главу 22).