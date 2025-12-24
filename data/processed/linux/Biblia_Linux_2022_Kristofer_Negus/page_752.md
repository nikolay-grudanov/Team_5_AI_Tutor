---
source_image: page_752.png
page_number: 752
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.91
tokens: 7745
characters: 2202
timestamp: 2025-12-24T05:06:36.204148
finish_reason: stop
---

Матрица контроля доступа вашей организации (см. главу 22 «Базовые методы обеспечения безопасности») поможет создать необходимые правила для брандмауэра netfilter/iptables на сервере Linux. Затем нужно протестировать в тестовой или виртуальной среде каждую модификацию перед внедрением ее в брандмауэр рабочих систем Linux.

Сохранение настроек службы iptables. Поскольку firewalld — это рекомендуемая служба для создания брандмауэров в RHEL, Fedora и других системах Linux, ручная установка постоянных правил брандмауэра не очень популярна. Однако при желании вы можете вручную сохранять и восстанавливать правила брандмауэра, созданные непосредственно с помощью службы iptables.

В следующем примере внесенные ранее изменения зафиксированы в брандмауэре. Текущий набор правил фильтра брандмауэра можно сохранить с помощью команды iptables-save:

# iptables -vnL
Chain INPUT (policy ACCEPT 8 packets, 560 bytes)
 pkts bytes target prot opt in out source destination
   0    0 DROP   tcp -- *   * 10.140.67.22 0.0.0.0/0  tcp dpt:22
   0    0 DROP   tcp -- *   * 0.0.0.0/0    0.0.0.0/0  tcp dpt:33
   0    0 DROP   icmp -- *  * 0.0.0.0/0    0.0.0.0/0

...

# iptables-save > /tmp/myiptables

Чтобы восстановить эти правила позже, сначала сбросьте текущие правила (iptables-F), а затем восстановите их (iptables-restore):

# iptables -F
# iptables -vnL
Chain INPUT (policy ACCEPT 8 packets, 560 bytes)
 pkts bytes target prot opt in out source destination
   0    0 DROP   tcp -- *   * 0.0.0.0/0    0.0.0.0/0  tcp dpt:33
   0    0 DROP   icmp -- *  * 0.0.0.0/0    0.0.0.0/0

...

Сброс правил не влияет на файл конфигурации iptables. Чтобы восстановить исходное состояние брандмауэра, используйте команду iptables-restore. В следующем примере файл конфигурации iptables перенаправляется в команду restore и восстанавливается исходное правило DROP для 10.140.67.2:

# iptables-restore < /tmp/myiptables
# iptables -vnL
Chain INPUT (policy ACCEPT 16 packets, 1120 bytes)
 pkts bytes target prot opt in out source destination
   0    0 DROP   tcp -- *   * 10.140.67.22 0.0.0.0/0  tcp dpt:22
   0    0 DROP   tcp -- *   * 0.0.0.0/0    0.0.0.0/0  tcp dpt:33
   0    0 DROP   icmp -- *  * 0.0.0.0/0    0.0.0.0/0