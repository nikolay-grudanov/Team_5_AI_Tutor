---
source_image: page_424.png
page_number: 424
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.89
tokens: 7777
characters: 2174
timestamp: 2025-12-24T04:57:28.449708
finish_reason: stop
---

примере равен N. Это значение (Nonexistent) говорит, что сервер был недавно загружен на текущий уровень выполнения:

$ runlevel
N 5

Как же сервер узнает, какие службы остановить и какие запустить, когда выбран определенный уровень выполнения? При выборе уровня выполнения запускаются скрипты, расположенные в каталоге /etc/rc.d/rc#.d, где # — выбранный уровень выполнения. Эти скрипты запускаются независимо от того, выбран ли уровень выполнения через загрузку сервера и используется ли параметр /etc/inittab initdefault или команда init либо telinit. Например, если выбран уровень выполнения 5, то все скрипты в каталоге /etc/rc.d/rc5.d будут запущены. Ваш список будет отличаться от приведенного далее в зависимости от того, какие службы вы установили и включили:

# ls /etc/rc.d/rc5.d
K01smolt
K02avahi-dnsconfd
K02NetworkManager
K02NetworkManagerDispatcher
K05saslauthd
K10dc_server
K10psacct
K12dc_client
K15gpm
K15httpd
K20nfs
K24irda
K25squid
K30spamassassin
K35vncserver
K50netconsole
K50tux
K69rpcsvcgcgssd
K73winbind
K73ypbind
K74nscd
K74ntpd
K84btseed
K84bttrack
K87multipathd
K88wpa_supplicant
K89dund
K89netplugd
K89pand
K89rdisc
K91capi
S00microcode_ctl
S04readahead_early
S05kudzu
S06cpuspeed
S08ip6tables
S08iptables
S09isdn
S10network
S11auditd
S12restorecond
S12syslog
S13irqbalance
S13mcstrans
S13rpctbind
S13setroubleshoot
S14nfslck
S15mdmonitor
S18rpcidmapd
S19rpcgssd
S22messagebus
S25bluetooth
S25fuse
S25netfs
S25pcscd
S26hidd
S26udev-post
S28autofs
S50hplip
S55cups
S55sshd
S80sendmail
S90ConsoleKit
S90crond
S90xfs
S95anacron
S95atd
S96readahead_later
S97dhcdbd
S97yum-updatesd
S98avahi-daemon
S98haldaemon
S99firstboot
S99local
S99smartd

Обратите внимание на то, что некоторые скрипты в каталоге /etc/rc.d/rc5.d начинаются с буквы K, а некоторые — с S. Значение K относится к скрипту, который немедленно останавливает процесс. Значение S относится к скрипту, который запускает процесс. Кроме того, каждый K- и S-скрипт имеет номер службы или демона, которыми они управляют. Это позволяет останавливать или запускать службы в определенном порядке. Например, благодаря этому сетевые службы Linux-сервера не будут запускаться до запуска самой сети.