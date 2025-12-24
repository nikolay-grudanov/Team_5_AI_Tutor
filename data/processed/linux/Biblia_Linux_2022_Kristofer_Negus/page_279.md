---
source_image: page_279.png
page_number: 279
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.03
tokens: 7596
characters: 1914
timestamp: 2025-12-24T04:52:59.970153
finish_reason: stop
---

В результате поиска появляется длинный список пакетов, содержащих слово editor в названии или описании. Допустим, нам нужен редактор emacs. Чтобы получить информацию об этом пакете, можно использовать подкоманду info:

# yum info emacs
Name        : emacs
Epoch       : 1
Version     : 26.2
Release     : 1.fc30
Architecture: x86_64
Size        : 3.2 M
Source      : emacs-26.2-1.fc30.src.rpm
Repository  : updates
Summary     : GNU Emacs text editor
URL         : http://www.gnu.org/software/emacs/
License     : GPLv3+ and CC0-1.0
Description : Emacs is a powerful, customizable, self-documenting, modeless text editor. Emacs contains special code editing features, a scripting language (elisp), and the capability to read mail, news, and more without leaving the editor.

Если вы знаете имена нужных команды, файла конфигурации или библиотеки, но не знаете, в каком пакете они находятся, используйте подкоманду provides для поиска пакета. В примере видно, что команда dvdrecord является частью пакета wodim:

# yum provides dvdrecord
wodim-1.1.11-41.fc30.x86_64 : A command line CD/DVD recording program
Repo        : fedora
Matched from:
Filename    : /usr/bin/dvdrecord

Подкоманда list применяется для перечисления имен пакетов различными способами. Используйте ее с базовым именем пакета, чтобы найти версию и репозиторий. Вы можете перечислить только пакеты, которые доступны (available), или установлены (installed), или все (all):

# yum list emacs
emacs.i686   1:26.2-1.fc30   updates
# yum list available
CUnit.i686   2.1.3-17.el8   rhel-8-for-x86_64-appstream-rpms
CUnit.x86_64 2.1.3-17.el8   rhel-8-for-x86_64-appstream-rpms
GConf2.i686   3.2.6-22.el8   rhel-8-for-x86_64-appstream-rpms
LibRaw.i686   0.19.1-1.el8   rhel-8-for-x86_64-appstream-rpm
...
# yum list installed
Installed Packages
GConf2.x86_64   3.2.6-22.el8   @AppStream
ModemManager.x86_64 1.8.0-1.el8   @anaconda
...
# yum list all
...