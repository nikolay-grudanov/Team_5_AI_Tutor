---
source_image: page_175.png
page_number: 175
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.68
tokens: 7685
characters: 1700
timestamp: 2025-12-24T04:23:37.230198
finish_reason: stop
---

версию, вызвав команду sudo с ключом -v. Если вы являетесь администратором, то увидите на экране подробную информацию о программе, вроде приведенной в листинге 4.3.

Листинг 4.3. Информация о программе sudo

Sudo version 1.6.5p2

Authentication methods: 'pam'
Syslog facility if syslog is being used for logging: authpriv
Syslog priority to use when user authenticates successfully: notice
Syslog priority to use when user authenticates unsuccessfully: alert
Ignore '.' in $PATH
Send mail if the user is not in sudoers
Use a separate timestamp for each user/tty combo
Lecture user the first time they run sudo
Require users to authenticate by default
Root may run sudo
Allow some information gathering to give useful error messages
Visudo will honor the EDITOR environment variable
Set the LOGNAME and USER environment variables
Length at which to wrap log file lines (0 for no wrap): 80
Authentication timestamp timeout: 5 minutes
Password prompt timeout: 5 minutes
Number of tries to enter a password: 3
Umask to use or 0777 to use user's: 022
Path to mail program: /usr/sbin/sendmail
Flags for mail program: -t
Address to send mail to: root
Subject line for mail messages: *** SECURITY information for %h ***
Incorrect password message: Sorry, try again.
Path to authentication timestamp dir: /var/run/sudo
Default password prompt: Password:
Default user to run commands as: root
Path to the editor for use by visudo: /bin/vi
Environment variables to check for sanity:
    LANGUAGE
    LANG
    LC_*
Environment variables to remove:
    BASH_ENV
    ENV
    TERMCAP
    ...
    ...
When to require a password for 'list' pseudocommand: any
When to require a password for 'verify' pseudocommand: all