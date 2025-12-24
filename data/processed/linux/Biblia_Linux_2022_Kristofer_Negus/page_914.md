---
source_image: page_914.png
page_number: 914
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.94
tokens: 7475
characters: 1735
timestamp: 2025-12-24T05:10:46.663505
finish_reason: stop
---

вы используете на своем сервере Linux, будут иными. Они могут выглядеть примерно так:

# nmap -sT 127.0.0.1
    ...
    PORT   STATE SERVICE
    25/tcp open  smtp
    631/tcp open  ipp

3. Чтобы запустить сканирование UDP Connect в своей системе Linux из удаленной системы, выполните следующие действия:
а) определите IP-адрес Linux-сервера, введя команду ifconfigat. Выходные данные будут выглядеть как в примере далее, и IP-адрес системы следует за inet addr: в выходных данных команды ifconfig:

# ifconfig
    ...
    p2p1  Link encap:Ethernet  HWaddr 08:00:27:E5:89:5A
        inet addr: 10.140.67.23

б) из удаленной системы Linux введите команду nmap-sU IP address, используя полученный ранее IP-адрес, например:

# nmap -sU 10.140.67.23

4. Чтобы проверить, работает ли в вашей системе служба firewalld, а затем установить и запустить ее, выполните следующие действия:
а) введите команду systemctl status firewalld.service;
б) если служба firewalld не запущена в системе Fedora или RHEL, введите следующее:

# yum install firewalld firewall-config -y
# systemctl start firewalld
# systemctl enable firewalld

5. Чтобы открыть порты в брандмауэре и разрешить удаленный доступ к локальной веб-службе, выполните следующие действия:
а) откройте окно Firewall (Межсетевой экран) с помощью команды firewalld-config;
б) выберите настройку Runtime (Рабочая среда);
в) выберите текущую зону (например, FedoraWorkstation);
г) в разделе Services (Службы) выберите варианты http и https;
д) выберите настройку Permanent (Постоянная);
е) в разделе Services (Службы) выберите варианты http и https.

6. Чтобы определить текущие политики и правила брандмауэра netfilter/iptables в своей системе Linux, введите iptables-vnL в командной строке.