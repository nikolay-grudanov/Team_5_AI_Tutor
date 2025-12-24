---
source_image: page_418.png
page_number: 418
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.06
tokens: 11868
characters: 2003
timestamp: 2025-12-24T03:34:11.020143
finish_reason: stop
---

<table>
  <tr>
    <th>put filename</th>
    <td>tftp</td>
  </tr>
  <tr>
    <th>put localfile remotefile</th>
    <td></td>
  </tr>
  <tr>
    <th>put filename1 filename2 ... filenameN remote-directory</th>
    <td>Передать файл или набор файлов в указанный файл или каталог удаленного узла.</td>
  </tr>
  <tr>
    <th>quit</th>
    <td>Завершить работу с tftp.</td>
  </tr>
  <tr>
    <th>rexmt retransmission-timeout</th>
    <td>Установить интервал (в секундах), в течение которого предпринимаются попытки повторной передачи пакета.</td>
  </tr>
  <tr>
    <th>status</th>
    <td>Вывести информацию о состоянии: установлено ли tftp-соединение с удаленным узлом (т. е. задан ли узел для последующих операций), текущий режим передачи файлов, включены ли режимы диагностики и отслеживания маршрута, а также значения retransmission timeout и total transmission timeout.</td>
  </tr>
  <tr>
    <th>timeout total-transmission-timeout</th>
    <td>Установить интервал (в секундах), в течение которого предпринимаются попытки передачи файла.</td>
  </tr>
  <tr>
    <th>trace</th>
    <td>Управление отслеживанием маршрутов пакетов.</td>
  </tr>
  <tr>
    <th>verbose</th>
    <td>Управление режимом диагностики.</td>
  </tr>
  <tr>
    <th>tftpd [homedir]</th>
    <td>tftpd</td>
  </tr>
  <tr>
    <th colspan="2">Команда TCP/IP. Сервер протокола Trivial File Transfer Protocol. tftpd обычно запускается сервером inetd и работает с портом, указанным в описании интернет-сервиса tftp (в файле /etc/inetd.conf). По умолчанию запись для tftp в /etc/inetd.conf закомментирована, и символ комментария необходимо удалить, чтобы tftpd включился в работу. Перед тем как ответить на запрос, сервер пытается сменить текущий каталог на homedir; значение по умолчанию — tftpboot.</th>
  </tr>
  <tr>
    <th>tload [options] [tty]</th>
    <td>tload</td>
  </tr>
  <tr>
    <th colspan="2">Отображение средней загрузки системы в виде графика. Если задан терминал (tty), то отображать на нем.</th>
  </tr>
</table>