---
source_image: page_068.png
page_number: 68
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.62
tokens: 7596
characters: 2077
timestamp: 2025-12-24T04:33:55.389498
finish_reason: stop
---

Нужно заметить, что удаление файла — двухшаговая операция, состоящая из удаления имени файла, а затем — удаления метаданных (и высвобождения блоков, занимавшихся этим файлом). Удаление метаданных файла не выполняется вообще, если у файла еще остались имена (жесткие ссылки), и не происходит сразу, если файл открыт (см. разд. 3.3) каким-либо процессом. Метаданные и блоки, занимаемые файлом, высвобождаются только при закрытии этого файла всеми открывшими его процессами, что проиллюстрировано в примере из листинга 3.7.

Команда df(1) измеряет доступное (свободное, disk free) место на файловой системе указанного файла, тогда как команда du(1), наоборот, измеряет занимаемое (disk usage) указанным файлом место на его файловой системе.

Листинг 3.7. Удаление открытого файла

finn@ubuntu:~$ df -h .
Файл.система    Размер Использовано Дост Использовано% Смонтировано в
/dev/mapper/ubuntu-root 455G , 400G 32G 93% /
finn@ubuntu:~$ du -sh astra-linux-1.3-special-edition-smolensk-disk3-devel.iso
2,8G astra-linux-1.3-special-edition-smolensk-disk3-devel.iso
\ finn@ubuntu:~$ rm astra-linux-1.3-special-edition-smolensk-disk3-devel.iso
finn@ubuntu:~$ df -h .
Файл.система    Размер Использовано Дост Использовано% Смонтировано в
? /dev/mapper/ubuntu-root 455G 400G 32G 93% /
finn@ubuntu:~$ lsof astra-linux-1.3-special-edition-smolensk-disk3-devel.iso
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
fuseiso 16925 finn 3r REG 252,0 2947385344 20316584 astra-linux-1.3-special-edition-smolensk-disk3-devel.iso
\ finn@ubuntu:~$ kill 16925
finn@ubuntu:~$ df -h .
Файл.система    Размер Использовано Дост Использовано% Смонтировано в
! /dev/mapper/ubuntu-root 455G 397G 35G 92% /

Специальные имена текущего ... и родительского ... каталогов на поверку тоже оказываются жесткими ссылками, поэтому у любого каталога по крайней мере два имени — свое «собственное» в родительском и специальное ... в самом себе, а у каталогов с подкаталогами еще и имена ... в каждом из дочерних (листинг 3.8).

Листинг 3.8. Имена каталогов

finn@ubuntu:~$ mkdir folder
finn@ubuntu:~$ ls -ldt folder