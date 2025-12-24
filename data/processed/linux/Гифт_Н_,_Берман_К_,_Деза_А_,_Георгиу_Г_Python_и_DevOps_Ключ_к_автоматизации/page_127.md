---
source_image: page_127.png
page_number: 127
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.21
tokens: 7907
characters: 2341
timestamp: 2025-12-24T03:04:26.756403
finish_reason: stop
---

с помощью dd — воспользоваться iostat. В следующем примере iostat выполняется только на устройстве, обрабатываемом dd, причем флаг -d означает лишь получение информации об устройстве с интервалом 1 секунда:

$ iostat -d /dev/sdc 1

<table>
  <tr>
    <th>Device</th>
    <th>tps</th>
    <th>kB_read/s</th>
    <th>kB_wrttn/s</th>
    <th>kB_read</th>
    <th>kB_wrttn</th>
  </tr>
  <tr>
    <td>sdc</td>
    <td>6813.00</td>
    <td>0.00</td>
    <td>1498640.00</td>
    <td>0</td>
    <td>1498640</td>
  </tr>
</table>

<table>
  <tr>
    <th>Device</th>
    <th>tps</th>
    <th>kB_read/s</th>
    <th>kB_wrttn/s</th>
    <th>kB_read</th>
    <th>kB_wrttn</th>
  </tr>
  <tr>
    <td>sdc</td>
    <td>6711.00</td>
    <td>0.00</td>
    <td>1476420.00</td>
    <td>0</td>
    <td>1476420</td>
  </tr>
</table>

Утилита iostat повторяет выводимую информацию ежесекундно, пока вы не прервете операцию, нажав Ctrl+C. Второй столбец в выводимой информации — tps (transactions per second — транзакций в секунду) — то же самое, что и IOPS. Можно более удобным способом визуализировать выводимую информацию, избавившись от всей этой мешанины повторов. Для этого достаточно очищать терминал при каждом вызове:

$ while true; do clear && iostat -d /dev/sdc && sleep 1; done

Повышаем точность измерения с помощью fio

Если dd и iostat недостаточно, чаще всего для измерения быстродействия используют fio. С ее помощью можно выяснить поведение в смысле быстродействия в среде с высокой нагрузкой по чтению и/или записи (и даже выбрать процентное соотношение операций чтения/записи).

fio выводит довольно много информации. В примере далее мы немного сократили ее, чтобы подчеркнуть полученные значения IOPS для операций чтения и записи:

$ fio --name=sdc-performance --filename=/dev/sdc --ioengine=libaio \
  --iodepth=1 --rw=randrw --bs=32k --direct=0 --size=64m
sdc-performance: (g=0): rw=randwrite, bs=(R) 32.0KiB-32.0KiB,
(W) 32.0KiB-32.0KiB, (T) 32.0KiB-32.0KiB, ioengine=libaio, iodepth=1
fio-3.1
Starting 1 process
sdc-performance: (groupid=0, jobs=1): err= 0: pid=2879:
  read: IOPS=1753, BW=54.8MiB/s (57.4MB/s)(31.1MiB/567msec)
...
  iops      : min= 1718, max= 1718, avg=1718.00, stdev= 0.00, samples=1
write: IOPS=1858, BW=58.1MiB/s (60.9MB/s)(32.9MiB/567msec)
...
  iops      : min= 1824, max= 1824, avg=1824.00, stdev= 0.00, samples=1