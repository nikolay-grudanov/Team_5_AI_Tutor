---
source_image: page_328.png
page_number: 328
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.55
tokens: 7605
characters: 1655
timestamp: 2025-12-24T04:54:30.287169
finish_reason: stop
---

Select (default p): p
Partition number (2-4, default 2): 2
First sector (10487808-240254975, default 10487808):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (10487808-240254975, default 240254975): +5G

Created a new partition 2 of type 'Linux' and of size 5 GiB.

Command (m for help): n
Partition type
    p   primary (2 primary, 0 extended, 2 free)
    e   extended (container for logical partitions)
Select (default p): p
Partition number (3,4, default 3): 3
First sector (20973568-240254975, default 20973568):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (20973568-240254975, default 240254975): +3G

Created a new partition 3 of type 'Linux' and of size 3 GiB.

Command (m for help): n
Partition type
    p   primary (3 primary, 0 extended, 1 free)
    e   extended (container for logical partitions)
Select (default e): e
Selected partition 4
First sector (27265024-240254975, default 27265024):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (27265024-240254975, default 240254975): <ENTER>

Created a new partition 4 of type 'Extended' and of size 101.6 GiB.

Command (m for help): n
All primary partitions are in use.
Adding logical partition 5
First sector (27267072-240254975, default 27267072):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (27267072-240254975, default 240254975): +3G

Created a new partition 5 of type 'Linux' and of size 3 GiB.

Command (m for help): n
All primary partitions are in use.
Adding logical partition 6
First sector (33560576-240254975, default 33560576):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (33560576-240254975, default 240254975): +4G

Created a new partition 6 of type 'Linux' and of size 4 GiB.