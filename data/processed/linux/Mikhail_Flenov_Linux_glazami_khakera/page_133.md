---
source_image: page_133.png
page_number: 133
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.03
tokens: 7606
characters: 1309
timestamp: 2025-12-24T04:22:18.340421
finish_reason: stop
---

# QMAIL_DIR is for Qmail
#
#QMAIL_DIR      Maildir
MAIL_DIR        /var/spool/mail
#MAIL_FILE      .mail

# Password aging controls:
#
#PASS_MAX_DAYS  Maximum number of days a password may be used.
#PASS_MIN_DAYS  Minimum number of days allowed between password changes.
#PASS_MIN_LEN   Minimum acceptable password length.
#PASS_WARN_AGE  Number of days warning given before a password expires.
#
PASS_MAX_DAYS   99999
PASS_MIN_DAYS   0
PASS_MIN_LEN    5
PASS_WARN_AGE   7

#
# Min/max values for automatic uid selection in useradd
#
UID_MIN         500
UID_MAX         60000

#
# Min/max values for automatic gid selection in groupadd
#
GID_MIN         500
GID_MAX         60000

#
# If defined, this command is run when removing a user.
# It should remove any at/cron/print jobs etc. owned by
# the user to be removed (passed as the first argument).
#
#USERDEL_CMD     /usr/sbin/userdel_local

#
# If useradd should create home directories for users by default
# On RH systems, we do. This option is ORed with the -m flag on
# useradd command line.
#
CREATE_HOME     yes

Ряд содержащихся здесь настроек можно использовать для повышения безопасности. Рассмотрим основные параметры файла:

☐ MAIL_DIR — каталог, в котором будет храниться почта пользователей;
☐ PASS_MAX_DAYS — максимальный срок жизни пароля;