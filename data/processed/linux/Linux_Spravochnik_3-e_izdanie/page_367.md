---
source_image: page_367.png
page_number: 367
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.28
tokens: 11678
characters: 1477
timestamp: 2025-12-24T03:31:47.309510
finish_reason: stop
---

<table>
  <tr>
    <th>sendmail</th>
    <td>
      <i>yfactor</i><br>
      Установить штрафной коэффициент <i>factor</i> за длинные списки получателей сообщений.<br>
      <b>Y</b> Выполнить каждое задание из очереди как отдельный процесс. Это позволяет ограничить размер процессов для систем с небольшим объемом памяти.<br>
      <i>zfactor</i><br>
      Множитель увеличения приоритетов. Это значение определяет вес приоритета сообщения. Значение по умолчанию для sendmail составляет 1800.<br>
      <i>Zinc</i><br>
      Увеличивать приоритет сообщений в очереди на <i>inc</i> после завершения каждого задания. Значение по умолчанию равно 90 000.<br>
      <b>Файлы поддержки sendmail</b><br>
      /usr/lib/sendmail<br>
      Исполняемый файл sendmail.<br>
      /usr/bin/newaliases<br>
      Ссылка на /usr/lib/sendmail. Выполняется пересборка базы данных псевдонимов.<br>
      /usr/bin/mailq<br>
      Вывод содержимого очереди сообщений.<br>
      /etc/sendmail.cf<br>
      Файл настройки в текстовом виде.<br>
      /etc/sendmail.hf<br>
      Файл справки SMTP.<br>
      /usr/lib/sendmail.st<br>
      Файл статистики. Может не существовать.<br>
      /etc/aliases<br>
      Файл псевдонимов в текстовом виде.<br>
      /etc/aliases.{pag,dir}<br>
      Файл псевдонимов в формате dbm.<br>
      /var/spool/mqueue<br>
      Каталог почтовой очереди и временных файлов.<br>
      /var/spool/mqueue/qf<br>
      Контрольные файлы сообщений.
    </td>
  </tr>
</table>