---
source_image: page_737.png
page_number: 737
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.14
tokens: 7668
characters: 2094
timestamp: 2025-12-24T05:06:05.384365
finish_reason: stop
---

Службы, работающие в настоящее время на Host-A, не так уж интересны. В следующем примере другая служба, sshd, запускается на Host-A с помощью команды systemctl (см. главу 15 «Запуск и остановка служб»). Эта служба интереснее для сканирования утилитой nmap:

# systemctl start sshd.service
# systemctl status sshd.service
• sshd.service – OpenSSH server daemon
    Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset: enabled)
    Active: active (running) since Fri 2020-1-30 15:08:29 EDT; 1 day 20h ago
    Docs: man:sshd(8)
          man:sshd_config(5)
    Main PID: 807 (sshd)
    Tasks: 1 (limit: 12244)
    Memory: 10.9M
    CGroup: /system.slice/sshd.service
        └─807 /usr/sbin/sshd -D -oCiphers=...

Кроме того, поскольку брандмауэр Host-A блокирует сканирование nmap от Host-B, было бы интересно посмотреть, что может сообщить nmap, когда брандмауэр не работает. В следующем примере показано, что брандмауэр отключен на Host-A для системы Fedora 21 или RHEL 7 (для других систем вам, вероятно, потребуется отключить службу iptables):

# systemctl stop firewalld.service
# systemctl status firewalld.service

При запущенной новой службе и отключенном брандмауэре Host-A сканирование nmap должно что-то найти. В следующем примере сканирование nmap выполняется снова с Host-B. На этот раз утилита nmap показывает службу ssh, работающую на открытом порте 22. Обратите внимание на то, что при отключенном брандмауэре на Host-A оба сканирования nmap собирают гораздо больше информации. Это действительно демонстрирует важность брандмауэра вашего Linux-сервера:

# nmap -sT 10.140.67.23
Starting Nmap 7.80 ( http://nmap.org ) at 2020-1-31 11:58 EDT
Nmap scan report for 10.140.67.23
Host is up (0.016s latency).
Not shown: 999 closed ports

PORT   STATE SERVICE
22/tcp open   ssh
Nmap done: 1 IP address (1 host up) scanned in 0.40 seconds

# nmap -sU 10.140.67.23
[sudo] password for johndoe: ***************
Starting Nmap 5.21 ( http://nmap.org ) at 2020-1-31 11:59 EDT
Nmap scan report for 10.140.67.23
Host is up (0.00072s latency).
Not shown: 997 closed ports