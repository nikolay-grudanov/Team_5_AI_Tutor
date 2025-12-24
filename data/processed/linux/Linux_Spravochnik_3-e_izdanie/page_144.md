---
source_image: page_144.png
page_number: 144
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 57.40
tokens: 11932
characters: 1950
timestamp: 2025-12-24T03:21:57.750708
finish_reason: stop
---

<table>
  <tr>
    <th>—n, —-norewrite</th>
    <td>Не расширять локальные почтовые идентификаторы до полных адресов. Этот параметр отключает обычную адресацию и должен использоваться только для отладки.</td>
  </tr>
  <tr>
    <th>—P n, —-port n</th>
    <td>Указать порт для соединения с почтовым сервером. Обычно бывает достаточно значений по умолчанию для портов поддерживаемых протоколов.</td>
  </tr>
  <tr>
    <th>—p proto, —-protocol proto</th>
    <td>Указать протокол, используемый для опроса сервера. Возможные значения proto:</td>
  </tr>
  <tr>
    <td>POP2</td>
    <td>Post Office Protocol 2.</td>
  </tr>
  <tr>
    <td>POP3</td>
    <td>Post Office Protocol 3.</td>
  </tr>
  <tr>
    <td>APOP</td>
    <td>POP3 с авторизацией по MD5.</td>
  </tr>
  <tr>
    <td>RPOP</td>
    <td>POP3 с авторизацией по RPOP.</td>
  </tr>
  <tr>
    <td>KPOP</td>
    <td>POP3 с авторизацией Kerberos v4 через порт 1109.</td>
  </tr>
  <tr>
    <td>IMAP</td>
    <td>IMAP2bis, IMAP4 или IMAP4rev1. fetchmail автоматически определяет их характеристики.</td>
  </tr>
  <tr>
    <th>IMAP-K4</th>
    <td>IMAP4 или IMAP4rev1 с авторизацией по Kerberos v4.</td>
  </tr>
  <tr>
    <th>IMAP-GSS</th>
    <td>IMAP4 или IMAP4rev1 с авторизацией по GSSAPI.</td>
  </tr>
  <tr>
    <th>ETRN</th>
    <td>ESMTP.</td>
  </tr>
  <tr>
    <th>—Q string, —-qvirtual string</th>
    <td>Удалить префикс string, являющийся локальным идентификатором узла пользователя, из адреса в заголовке сообщения (например, «Delivered-To:»).</td>
  </tr>
  <tr>
    <th>—r folder, —-folder folder</th>
    <td>Получить указанную почтовую папку folder с почтового сервера.</td>
  </tr>
  <tr>
    <th>—s, —-silent</th>
    <td>Не выводить сообщения о состоянии в процессе получения почты.</td>
  </tr>
  <tr>
    <th>—U, —-uidl</th>
    <td>Для протокола POP3 отслеживать возраст сохраненных на сервере сообщений с помощью списка уникальных идентификаторов.</td>
  </tr>
</table>