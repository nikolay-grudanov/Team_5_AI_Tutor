---
source_image: page_341.png
page_number: 341
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.94
tokens: 7875
characters: 2841
timestamp: 2025-12-24T04:55:06.402671
finish_reason: stop
---

<table>
  <tr>
    <th>Mem:</th>
    <td>1955</td>
    <td>1720</td>
    <td>235</td>
    <td>0</td>
    <td>42</td>
    <td>1310</td>
  </tr>
  <tr>
    <th>-/+ buffers/cache:</th>
    <td>367</td>
    <td></td>
    <td>1588</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>Swap:</th>
    <td>819</td>
    <td>0</td>
    <td>819</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

Обратите внимание: объем доступного места для подкачки был уменьшен после выполнения команды swapoff.

Определение монтируемых файловых систем с помощью файла fstab

Разделы жесткого диска на компьютере и удаленные файловые системы, которые используются ежедневно, скорее всего, настроены на автоматическое монтирование при загрузке Linux. Файл /etc/fstab содержит определения для каждого раздела, а также параметры, описывающие способ монтирования раздела. Пример применения файла /etc/fstab:

# /etc/fstab
/dev/mapper/vg_abc-lv_root   /   ext4   defaults   1 1
UUID=78bdae46-9389-438d-bfee-06dd934fae28 /boot ext4 defaults 1 2
/dev/mapper/vg_abc-lv_home   /home ext4 defaults 1 2
/dev/mapper/vg_abc-lv_swap   swap swap defaults 0 0
# Mount entries added later
/dev/sdb1                    /win vfat ro 1 2
192.168.0.27:/nfsstuff       /remote nfs users,_netdev 0 0
//192.168.0.28/myshare       /share cifs guest,_netdev 0 0
# special Linux filesystems
tmpfs                        /dev/shm tmpfs defaults 0 0
devpts                       /dev/pts devpts gid=5,mode=620 0 0
sysfs                        /sys sysfs defaults 0 0
proc                         /proc proc defaults 0 0

Здесь файл /etc/fstab взят из стандартной установки сервера Red Hat Enterprise Linux 6 с добавлением нескольких строк.

В данный момент вы можете игнорировать записи tmpfs, devpts, sysfs и proc. Это специальные устройства, связанные с общей памятью, терминальными окнами, информацией об устройстве и параметрами ядра соответственно.

В первом столбце файла /etc/fstab показано устройство или общий ресурс (что монтируется), а во втором — точка монтирования (где монтируется). За ними следуют тип файловой системы, любые параметры монтирования (или значения по умолчанию) и два числа, указывающие командам, таким как dump и fsck, что делать с файловой системой.

Первые три записи представляют разделы диска, назначенные корневому каталогу файловой системы (/), каталогу /boot и каталогу /home. Все они являются файловыми системами ext4. Четвертая строка — это устройство подкачки (применяется для хранения данных при переполнении оперативной памяти). Обратите внимание на то, что имена устройств для каталогов /, /home и swap начинаются с /dev/mapper. Это связано с тем, что они являются логическими томами LVM, которым назначается пространство из группы томов LVM (подробнее о LVM — в разделе «Использование разделов LVM» ранее в этой главе).