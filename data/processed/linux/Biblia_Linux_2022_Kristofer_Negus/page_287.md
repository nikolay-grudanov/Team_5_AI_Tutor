---
source_image: page_287.png
page_number: 287
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.79
tokens: 7386
characters: 1301
timestamp: 2025-12-24T04:53:18.433456
finish_reason: stop
---

# rpm -qi zsh
Name      : zsh
Version   : 5.5.1
Release   : 6.el8
...
# rpm -ql zsh
/etc/skel/.zshrc
/etc/zlogin
/etc/zlogout
...
# rpm -qd zsh
/usr/share/doc/zsh/BUGS
/usr/share/doc/zsh/CONTRIBUTORS
/usr/share/doc/zsh/FAQ
...
# rpm -qc zsh
/etc/skel/.zshrc
/etc/zlogin
/etc/zlogout
...

Используйте параметры для запроса любой части информации, содержащейся в RPM. Вы можете узнать, что требуется RPM для установки (--requirements), какую версию программного обеспечения пакет предоставляет (--provides), какие сценарии запускаются до и после установки или удаления RPM (--scripts) и какие изменения были внесены в RPM (--changelog):

# rpm -q --requires emacs-common
/bin/sh
/usr/bin/pkg-config
/usr/sbin/alternatives
...
# rpm -q --provides emacs-common
config(emacs-common) = 1:26.2-1.fc30
emacs-common = 1:26.2-1.fc30
emacs-common(x86-64) = 1:26.2-1.fc30
emacs-el = 1:26.2-1.fc30
pkgconfig(emacs) = 1:26.2
# rpm -q --scripts httpd
postinstall scriptlet (using /bin/sh):
if [ $1 -eq 1 ] ; then
    # Initial installation
    systemctl --no-reload preset httpd.service...
...
# rpm -q --changelog httpd | less
* Thu May 02 2019 Lubos Uhliarik <luhliari@redhat.com> - 2.4.39-4
- httpd dependency on initscripts is unspecified (#1705188)
* Tue Apr 09 2019 Joe Orton <jorton@redhat.com> - 2.4.39-3
...