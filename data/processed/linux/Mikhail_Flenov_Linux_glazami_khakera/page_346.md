---
source_image: page_346.png
page_number: 346
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.92
tokens: 8506
characters: 3067
timestamp: 2025-12-24T04:29:02.640270
finish_reason: stop
---

**Never logged in**
**Never logged in**
Mon Feb 21 12:05:06 +0300 2005
**Never logged in**
Mon Feb 21 12:10:47 +0300 2005

Список состоит из четырех колонок:

- имя пользователя из файла /etc/passwd;
- порт или терминал, на который происходило подключение;
- адрес компьютера, если вход был по сети;
- время входа.

С помощью lastlog удобно контролировать системные записи. У них дата последнего входа должна быть **Never logged in**, потому что под ними нельзя войти в систему (в качестве командной оболочки установлены /bin/false, /dev/null, /sbin/nologin и др.). Если вы заметили, что кто-либо проник в систему через одну из этих учетных записей, то это значит, что хакер использует ее, изменяя настройки.

Простая замена командной оболочки в файле /etc/passwd может открыть хакеру потайную дверь, и администратор не заметит этой трансформации. Но после выполнения команды lastlog все неявное становится явным.

Обращайте внимание на тип подключения и адрес. Если что-то вызывает подозрение, то можно выявить атаку на этапе ее созревания.

lsof

С помощью этой команды можно определить, какие файлы и какими пользователями открыты в данный момент. Результат ее выполнения приведен в листинге 12.2.

Листинг 12.2. Результат выполнения команды lsof

<table>
  <tr>
    <th>COMMAND</th>
    <th>PID</th>
    <th>USER</th>
    <th>FD</th>
    <th>TYPE</th>
    <th>DEVICE</th>
    <th>SIZE</th>
    <th>NODE</th>
    <th>NAME</th>
  </tr>
  <tr>
    <td>init</td>
    <td>1</td>
    <td>root</td>
    <td>cwd</td>
    <td>DIR</td>
    <td>3,2</td>
    <td>4096</td>
    <td>2</td>
    <td>/</td>
  </tr>
  <tr>
    <td>init</td>
    <td>1</td>
    <td>root</td>
    <td>rtd</td>
    <td>DIR</td>
    <td>3,2</td>
    <td>4096</td>
    <td>2</td>
    <td>/</td>
  </tr>
  <tr>
    <td>init</td>
    <td>1</td>
    <td>root</td>
    <td>txt</td>
    <td>REG</td>
    <td>3,2</td>
    <td>26920</td>
    <td>635284</td>
    <td>/sbin/init</td>
  </tr>
  <tr>
    <td>init</td>
    <td>1</td>
    <td>root</td>
    <td>mem</td>
    <td>REG</td>
    <td>3,2</td>
    <td>89547</td>
    <td>553856</td>
    <td>/lib/ld-2.2.5.so</td>
  </tr>
  <tr>
    <td>init</td>
    <td>1</td>
    <td>root</td>
    <td>10u</td>
    <td>FIFO</td>
    <td>3,2</td>
    <td></td>
    <td>195499</td>
    <td>/dev/initctl</td>
  </tr>
  <tr>
    <td>keventd</td>
    <td>2</td>
    <td>root</td>
    <td>cwd</td>
    <td>DIR</td>
    <td>3,2</td>
    <td>4096</td>
    <td>2</td>
    <td>/</td>
  </tr>
  <tr>
    <td>keventd</td>
    <td>2</td>
    <td>root</td>
    <td>rtd</td>
    <td>DIR</td>
    <td>3,2</td>
    <td>4096</td>
    <td>2</td>
    <td>/</td>
  </tr>
  <tr>
    <td>kapmd</td>
    <td>3</td>
    <td>root</td>
    <td>10u</td>
    <td>FIFO</td>
    <td>3,2</td>
    <td></td>
    <td>195499</td>
    <td>/dev/initctl</td>
  </tr>
</table>

Это далеко не полный результат. Даже если в данный момент вы один работаете с системой, количество открытых файлов может исчисляться парой десятков, и число их заметно растет, если в системе несколько пользователей, ведь один файл