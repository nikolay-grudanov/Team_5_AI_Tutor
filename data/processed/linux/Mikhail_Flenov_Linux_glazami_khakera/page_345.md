---
source_image: page_345.png
page_number: 345
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 59.54
tokens: 8660
characters: 3475
timestamp: 2025-12-24T04:29:05.741353
finish_reason: stop
---

локально, а через сеть, то будет отображена информация о хосте, с которого входили в систему.

Если выполнить эту команду для себя, то может вывалиться такой список, что читать его будет невозможно, потому что вы достаточно часто работаете в системе. Чтобы ограничить выводимые данные, можно указать ключ -n и количество отображаемых строк. Например, следующая команда выдаст информацию о последних пяти входах:

last -n 5 robert

lastlog

Если выполнить команду lastlog, то она выведет на экран перечень всех пользователей с датами их последнего подключения к системе. Пример результата ее выполнения можно увидеть в листинге 12.1.

Листинг 12.1. Результат выполнения команды lastlog

<table>
  <tr>
    <th>Username</th>
    <th>Port</th>
    <th>From</th>
    <th>Latest</th>
  </tr>
  <tr>
    <td>root</td>
    <td>ftpd2022</td>
    <td>192.168.77.10</td>
    <td>Mon Feb 21 12:05:06 +0300 2005</td>
  </tr>
  <tr>
    <td>bin</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>daemon</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>adm</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>lp</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>sync</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>shutdown</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>halt</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>mail</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>news</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>uucp</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>operator</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>games</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>gopher</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>ftp</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>nobody</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>vcsa</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>mailnull</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>rpm</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>xfs</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>apache</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>ntp</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>rpc</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>gdm</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>rpcuser</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>nscd</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>ident</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
  <tr>
    <td>radvd</td>
    <td></td>
    <td></td>
    <td>**Never logged in**</td>
  </tr>
</table>