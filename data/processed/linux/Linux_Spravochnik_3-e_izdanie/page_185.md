---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.15
tokens: 11647
characters: 1345
timestamp: 2025-12-24T03:23:30.542458
finish_reason: stop
---

<table>
  <tr>
    <th>gdc</th>
    <td>
      <b>KILL</b><br>
      Немедленное (и неэлегантное) принудительное завершение.<br>
      <b>modeconf</b><br>
      Установить права доступа для всех файлов настройки в режим 664 с владельцем root и группой gdmaint.<br>
      <b>newconf</b><br>
      Убедиться, что /etc/gated.conf+ существует, и перенести его содержимое в /etc/gated.conf. Старый файл /etc/gated.conf сохраняется под именем /etc/gated.conf-.<br>
      <b>reconfig</b><br>
      Перезагрузить файл настройки.<br>
      <b>restart</b><br>
      Завершить и перезапустить gated.<br>
      <b>rmcore</b><br>
      Удалить все найденные файлы образов.<br>
      <b>rmdmp</b><br>
      Удалить все найденные файлы образов состояния.<br>
      <b>rmparse</b><br>
      Удалить все файлы gated, в которых найдены ошибки разбора. Они генерируются командами checkconf и checknew.<br>
      <b>running</b><br>
      Завершение с кодом 0, если gated запущен, и с ненулевым кодом — в противном случае.<br>
      <b>start</b><br>
      Выполнить gated, если он еще не запущен. В последнем случае вернуть ошибку.<br>
      <b>stop</b><br>
      Завершить выполнение gated как можно мягче.<br>
      <b>term</b><br>
      Принудительное мягкое завершение.<br>
      <b>togglettrace</b><br>
      Переключение трассировки.
    </td>
  </tr>
</table>