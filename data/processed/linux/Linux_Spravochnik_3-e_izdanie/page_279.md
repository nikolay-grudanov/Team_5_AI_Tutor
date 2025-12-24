---
source_image: page_279.png
page_number: 279
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.36
tokens: 11730
characters: 1470
timestamp: 2025-12-24T03:27:53.888868
finish_reason: stop
---

<table>
  <tr>
    <th>ls</th>
    <td>
      <b>-T, --tabsize n_cols</b><br>
      Установить размер табуляции в <i>n_cols</i> колонок. По умолчанию — 8.<br>
      <b>-U, --sort=none</b><br>
      Не сортировать список файлов. Аналогично <b>-f</b>, но отображение в длинном формате.<br>
      <b>-X, --sort=extension</b><br>
      Сортировка файлов по расширениям.<br>
      <b>Примеры</b><br>
      Перечислить все файлы в текущем каталоге и отобразить их размеры; использовать многоколоночный вывод и отмечать специальные файлы:<br>
      <code>ls -asCF</code><br>
      Отобразить состояние каталогов <i>/bin</i> и <i>/etc</i>:
      <code>ls -ld /bin /etc</code><br>
      Перечислить файлы исходных текстов на языке C в текущем каталоге, начиная с самого старого:
      <code>ls -rt *.c</code><br>
      Сосчитать файлы в текущем каталоге:
      <code>ls | wc -l</code>
    </td>
  </tr>
  <tr>
    <th>lsattr</th>
    <td>
      <b>lsattr [options] [files]</b><br>
      Отобразить атрибуты файлов файловой системы Linux Second Extended Filesystem (ext2). См. также <b>chattr</b>.<br>
      <b>Параметры</b><br>
      <b>-a</b> Перечислить все файлы в указанных каталогах.<br>
      <b>-d</b> Перечислить атрибуты самих каталогов, а не их содержимого.<br>
      <b>-R</b> Рекурсивно обрабатывать каталоги и их содержимое.<br>
      <b>-v</b> Перечислить версии файлов.<br>
      <b>-V</b> Вывести информацию о версии и завершить работу.
    </td>
  </tr>
</table>