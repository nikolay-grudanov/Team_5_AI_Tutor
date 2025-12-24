---
source_image: page_567.png
page_number: 567
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.84
tokens: 7414
characters: 1472
timestamp: 2025-12-24T05:01:06.556157
finish_reason: stop
---

чтобы открыть брандмауэр для службы NFS. Введите firewall-config, затем убедитесь, что в окне установлены флажки mountd, nfs и rpcbind, которые открывают соответствующие порты службе NFS. На рис. 20.3 показан пример этого окна.

![Окно Firewall Configuration с открытыми портами nfs и rpc-bind](../images/ch20_03.png)

Рис. 20.3. Используйте окно Firewall, чтобы открыть брандмаузру доступ к службе

Для RHEL 6 и других систем, задействующих службу iptables напрямую (до появления firewalld), чтобы открыть порты на брандмауэре сервера NFS, убедитесь, что iptables включен и запущен с правилами брандмауэра, аналогичными следующим, добавленным в файл /etc/sysconfig/iptables:

-A INPUT -m state --state NEW -m tcp -p tcp --dport 111 -j ACCEPT
-A INPUT -m state --state NEW -m udp -p udp --dport 111 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 2049 -j ACCEPT
-A INPUT -m state --state NEW -m udp -p udp --dport 2049 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 20048 -j ACCEPT
-A INPUT -m state --state NEW -m udp -p udp --dport 20048 -j ACCEPT

В Red Hat Enterprise Linux 6.x и более ранних версиях настройка брандмауэра немного сложнее. Проблема с брандмауэрами заключается в том, что существует несколько связанных с NFS служб, которые прослушивают разные порты, назначаемые случайным образом. Чтобы обойти эту проблему, нужно заблокировать номера портов, использующих эти службы, и открыть брандмауэр, чтобы эти порты были доступными.