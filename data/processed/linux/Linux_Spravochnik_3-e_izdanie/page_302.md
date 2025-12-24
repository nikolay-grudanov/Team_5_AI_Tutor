---
source_image: page_302.png
page_number: 302
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.01
tokens: 11901
characters: 1960
timestamp: 2025-12-24T03:29:04.761755
finish_reason: stop
---

<table>
  <tr>
    <th>–p, --parents</th>
    <td>Создать недостающие в пути родительские каталоги.</td>
    <th>mkdir</th>
  </tr>
  <tr>
    <th>--verbose</th>
    <td>Уведомить пользователя о каждом создании каталога.</td>
    <td></td>
  </tr>
  <tr>
    <th>--help</th>
    <td>Вывести справку и завершить работу.</td>
    <td></td>
  </tr>
  <tr>
    <th>--version</th>
    <td>Отобразить номер версии и завершить работу.</td>
    <td></td>
  </tr>
  <tr>
    <th colspan="3">Примеры</th>
  </tr>
  <tr>
    <th colspan="3">Создать каталог personal, доступный только для чтения:</th>
  </tr>
  <tr>
    <td colspan="3">mkdir -m 444 personal</td>
  </tr>
  <tr>
    <th colspan="3">Последовательность команд:</th>
  </tr>
  <tr>
    <td colspan="3">mkdir work; cd work<br>mkdir junk; cd junk<br>mkdir questions; cd ../..</td>
  </tr>
  <tr>
    <th colspan="3">может быть заменена одной командой:</th>
  </tr>
  <tr>
    <td colspan="3">mkdir -p work/junk/questions</td>
  </tr>
  <tr>
    <th>mke2fs [options] device [blocks]</th>
    <th>mkfs.ext2 [options] device [blocks]</th>
    <th>mke2fs</th>
  </tr>
  <tr>
    <td colspan="3">Команда системного администрирования. Форматирование устройства под файловую систему ext2fs. Можно указать количество блоков на устройстве либо позволить mke2fs определить его автоматически.</td>
  </tr>
  <tr>
    <th colspan="3">Параметры</th>
  </tr>
  <tr>
    <th>-b block-size</th>
    <td>Указать размер блока в байтах.</td>
    <td></td>
  </tr>
  <tr>
    <th>-c</th>
    <td>Перед форматированием проверить устройство на наличие сбойных блоков.</td>
    <td></td>
  </tr>
  <tr>
    <th>-f fragment-size</th>
    <td>Указать размер фрагмента в байтах.</td>
    <td></td>
  </tr>
  <tr>
    <th>-i bytes-per-inode</th>
    <td>Создавать inode-блок для каждого bytes-per-inode байт дискового пространства. Значение должно быть больше либо равно 1024. По умолчанию равно 4096.</td>
    <td></td>
  </tr>
</table>