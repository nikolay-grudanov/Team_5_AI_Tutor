---
source_image: page_310.png
page_number: 310
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.08
tokens: 11927
characters: 1959
timestamp: 2025-12-24T03:29:28.987294
finish_reason: stop
---

<table>
  <tr>
    <th>–t type</th>
    <td>Указать тип файловой системы. Возможные значения: minix, ext, ext2, xiafs, hpfs, msdos, umsdos, vfat, proc, nfs, iso9660, smbfs, ncpfs, affs, ufs, romfs, sysv, xenix и coherent. Обратите внимание, что ext и xiafs доступны только для ядер версий меньше 2.1.21 и что вместо xenix и coherent следует использовать sysv.</td>
    <td>mount</td>
  </tr>
  <tr>
    <th>–v</th>
    <td>Диагностика монтирования.</td>
    <td></td>
  </tr>
  <tr>
    <th>–w</th>
    <td>Монтировать в режиме чтения/записи. Режим по умолчанию.</td>
    <td></td>
  </tr>
  <tr>
    <th>Файлы</th>
    <td colspan="2"></td>
  </tr>
  <tr>
    <th>/etc/fstab</th>
    <td>Список монтируемых файловых систем и параметров монтирования.</td>
    <td></td>
  </tr>
  <tr>
    <th>/etc/mtab</th>
    <td>Список подмонтированных в настоящий момент систем и параметров монтирования.</td>
    <td></td>
  </tr>
  <tr>
    <th>rpc.mountd [options]</th>
    <td colspan="2"></td>
  </tr>
  <tr>
    <th>Команда NFS/NIS. Сервер запросов на монтирование NFS. mountd читает файл /etc/exports и определяет, какие файловые системы доступны для монтирования и какими узлами сети. Также mountd отображает информацию о файловых системах, подмонтированных клиентами. См. также nfsd.</th>
    <td colspan="2"></td>
  </tr>
  <tr>
    <th>Параметры</th>
    <td colspan="2"></td>
  </tr>
  <tr>
    <th>–d, --debug</th>
    <td>Режим отладки. Вывод всей отладочной информации через syslogd.</td>
    <td></td>
  </tr>
  <tr>
    <th>–f file, --exports-file file</th>
    <td>Читать права экспорта для файловых систем из указанного файла, а не из /etc/exports.</td>
    <td></td>
  </tr>
  <tr>
    <th>–n, --allow-non-root</th>
    <td>Разрешить даже запросы на монтирование, приходящие не через зарезервированные порты.</td>
    <td></td>
  </tr>
  <tr>
    <th>–p, --promiscuous</th>
    <td>Принимать запросы от любого узла.</td>
    <td></td>
  </tr>
</table>