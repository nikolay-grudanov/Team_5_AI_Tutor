---
source_image: page_474.png
page_number: 474
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.19
tokens: 11864
characters: 1842
timestamp: 2025-12-24T03:36:39.386262
finish_reason: stop
---

number
Установить текстовый режим, соответствующий числу (number). Список чисел и соответствующих режимов можно получить, загрузившись с параметром vga=ask и нажав клавишу <Enter>.

Команда lilo

Для установки и обновления загрузчика (при изменении ядра или файла настройки /etc/lilo.conf) следует выполнить команду lilo.

Полный путь команды обычно /sbin/lilo. Синтаксис команды:

lilo [options]

Некоторые из параметров соответствуют ключевым словам файла /etc/lilo.conf.

<table>
  <tr>
    <th>Ключевое слово конфигурации</th>
    <th>Параметр</th>
  </tr>
  <tr>
    <td>boot=bootdev</td>
    <td>-b bootdev</td>
  </tr>
  <tr>
    <td>compact</td>
    <td>-c</td>
  </tr>
  <tr>
    <td>delay=tsecs</td>
    <td>-d tsecs</td>
  </tr>
  <tr>
    <td>default=label</td>
    <td>-D label</td>
  </tr>
  <tr>
    <td>disktab=file</td>
    <td>-f file</td>
  </tr>
  <tr>
    <td>install=bootsector</td>
    <td>-i bootsector</td>
  </tr>
  <tr>
    <td>lba32</td>
    <td>-L</td>
  </tr>
  <tr>
    <td>linear</td>
    <td>-l</td>
  </tr>
  <tr>
    <td>map=mapfile</td>
    <td>-m mapfile</td>
  </tr>
  <tr>
    <td>fix-table</td>
    <td>-P fix</td>
  </tr>
  <tr>
    <td>ignore-table</td>
    <td>-P ignore</td>
  </tr>
  <tr>
    <td>backup=file</td>
    <td>-s file</td>
  </tr>
  <tr>
    <td>force-backup=file</td>
    <td>-S file</td>
  </tr>
  <tr>
    <td>verbose=level</td>
    <td>-v</td>
  </tr>
</table>

По возможности эти параметры лучше описывать в файле настройки; использование их в командной строке lilo, а не в /etc/lilo.conf, уже устарело. В следующем разделе описаны параметры, которые можно задать только в командной строке lilo; все прочие параметры описаны в предыдущем разделе.

Параметры команды lilo

Далее перечислены командные параметры lilo. Если параметров несколько, они задаются раздельно:

% lilo -q -v