---
source_image: page_014.png
page_number: 14
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.13
tokens: 7221
characters: 1402
timestamp: 2025-12-24T04:32:08.706992
finish_reason: stop
---

/bin/chmod
/bin/chown
/bin/cp
/bin/date
/bin/dd
/bin/df

bart@ubuntu:~$ dpkg -s coreutils
Package: coreutils
Essential: yes
Status: install ok installed
Priority: required
Section: utils
Installed-Size: 7196
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Multi-Arch: foreign
Version: 8.30-3ubuntu2
Pre-Depends: libacl1 (>= 2.2.23), libattr1 (>= 1:2.4.44), libc6 (>= 2.28), libselinux1 (>= 2.1.13)
Description: GNU core utilities
This package contains the basic file, shell and text manipulation utilities which are expected to exist on every operating system.

Specifically, this package includes:
arch base64 basename cat chcon chgrp chmod chown chroot cksum comm cp csplit cut date dd df dir dircolors dirname du echo env expand expr ...

Homepage: http://gnu.org/software/coreutils
Original-Maintainer: Michael Stone <mstone@debian.org>

Если при попытке выполнить ту или иную команду операционной системы Ubuntu Linux (это одна из причин, по которой иллюстрация в книге ведется именно с ее помощью) обнаружится, что нужный пакет с программным обеспечением не установлен, то при наличии доступа в Интернет можно тривиальным способом доустановить недостающие компоненты (листинг В2).

Листинг В2. Установка недостающего программного обеспечения

bart@ubuntu:~$ finger
Команда «finger» не найдена, но может быть установлена с помощью:
sudo apt install finger