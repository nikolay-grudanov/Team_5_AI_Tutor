---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 106.23
tokens: 9667
characters: 4933
timestamp: 2025-12-24T04:22:49.081903
finish_reason: stop
---

Добро пожаловать в Linux

11:44am up 1:22, 2 users, load average: 0,00, 0,00, 0,00
58 processes: 46 sleeping, 1 running, 0 zombie, 11 stopped
CPU states: 0,0% user, 0,5% system, 0,0% nice, 99,4% idle
Mem: 255884K av, 248416K used, 7468K free, 0K shrd, 60188K buff
Swap: 514040K av, 0K used, 514040K free 61472K cached

<table>
  <tr>
    <th>PID</th>
    <th>USER</th>
    <th>PRI</th>
    <th>Ni</th>
    <th>SIZE</th>
    <th>RSS</th>
    <th>SHARE</th>
    <th>STAT</th>
    <th>%CPU</th>
    <th>%MEM</th>
    <th>TIME</th>
    <th>COMMAND</th>
  </tr>
  <tr><td>1847</td><td>root</td><td>16</td><td>0</td><td>1036</td><td>1036</td><td>824</td><td>R</td><td>0,3</td><td>0,4</td><td>0:00</td><td>top</td></tr>
  <tr><td>859</td><td>mysql</td><td>15</td><td>0</td><td>4300</td><td>4300</td><td>1644</td><td>S</td><td>0,1</td><td>1,6</td><td>0:00</td><td>mysqld</td></tr>
  <tr><td>1</td><td>root</td><td>15</td><td>0</td><td>452</td><td>452</td><td>400</td><td>S</td><td>0,0</td><td>0,1</td><td>0:04</td><td>init</td></tr>
  <tr><td>2</td><td>root</td><td>15</td><td>0</td><td>0</td><td>0</td><td>0</td><td>SW</td><td>0,0</td><td>0,0</td><td>0:00</td><td>keventd</td></tr>
  <tr><td>3</td><td>root</td><td>15</td><td>0</td><td>0</td><td>0</td><td>0</td><td>SW</td><td>0,0</td><td>0,0</td><td>0:00</td><td>kapmd</td></tr>
  <tr><td>4</td><td>root</td><td>34</td><td>19</td><td>0</td><td>0</td><td>0</td><td>SWN</td><td>0,0</td><td>0,0</td><td>0:00</td><td>ksoftirqd_CPU0</td></tr>
  <tr><td>5</td><td>root</td><td>15</td><td>0</td><td>0</td><td>0</td><td>0</td><td>SW</td><td>0,0</td><td>0,0</td><td>0:00</td><td>kswapd</td></tr>
  <tr><td>6</td><td>root</td><td>25</td><td>0</td><td>0</td><td>0</td><td>0</td><td>SW</td><td>0,0</td><td>0,0</td><td>0:00</td><td>bdfflush</td></tr>
  <tr><td>7</td><td>root</td><td>15</td><td>0</td><td>0</td><td>0</td><td>0</td><td>SW</td><td>0,0</td><td>0,0</td><td>0:00</td><td>kupdated</td></tr>
  <tr><td>8</td><td>root</td><td>25</td><td>0</td><td>0</td><td>0</td><td>0</td><td>SW</td><td>0,0</td><td>0,0</td><td>0:00</td><td>mdrecoveryd</td></tr>
  <tr><td>17</td><td>root</td><td>15</td><td>0</td><td>0</td><td>0</td><td>0</td><td>SW</td><td>0,0</td><td>0,0</td><td>0:00</td><td>kjournald</td></tr>
  <tr><td>525</td><td>root</td><td>15</td><td>0</td><td>540</td><td>540</td><td>448</td><td>S</td><td>0,0</td><td>0,2</td><td>0:00</td><td>syslogd</td></tr>
  <tr><td>530</td><td>root</td><td>15</td><td>0</td><td>436</td><td>436</td><td>376</td><td>S</td><td>0,0</td><td>0,1</td><td>0:00</td><td>klogd</td></tr>
  <tr><td>551</td><td>rpc</td><td>15</td><td>0</td><td>540</td><td>540</td><td>456</td><td>S</td><td>0,0</td><td>0,2</td><td>0:00</td><td>portmap</td></tr>
  <tr><td>579</td><td>rpcuser</td><td>15</td><td>0</td><td>740</td><td>740</td><td>636</td><td>S</td><td>0,0</td><td>0,2</td><td>0:00</td><td>rpc.statd</td></tr>
  <tr><td>683</td><td>root</td><td>15</td><td>0</td><td>468</td><td>468</td><td>412</td><td>S</td><td>0,0</td><td>0,1</td><td>0:00</td><td>apmd</td></tr>
  <tr><td>737</td><td>ident</td><td>17</td><td>0</td><td>896</td><td>896</td><td>716</td><td>S</td><td>0,0</td><td>0,3</td><td>0:00</td><td>identd</td></tr>
  <tr><td>750</td><td>ident</td><td>15</td><td>0</td><td>896</td><td>896</td><td>716</td><td>S</td><td>0,0</td><td>0,3</td><td>0:00</td><td>identd</td></tr>
</table>

Рис. 3.4. Результат работы команды top

Если мой компьютер начинает "тормозить", или работа замедляется через определенные промежутки времени, то я запускаю top в отдельном терминале и, по мере необходимости, переключаюсь на него, чтобы увидеть нагрузку процессов.

В верхней строке окна (см. рис. 3.4) выводится количество пользователей, общая загрузка системы и статистика процессов: общее количество, спящие, выполняемые, зависшие и остановленные.

Помимо этого, там можно увидеть краткий отчет по использованию памяти: количество занятой и свободной оперативной памяти и размер раздела подкачки. В моем случае в компьютере установлено 256 Мбайт памяти, и из них свободно только 7 Мбайт, а раздел подкачки пока не используется. Такое малое количество свободной памяти говорит о том, что не помешало бы ее нарастить. Чем меньше компьютер использует swap-раздел, тем быстрее он работает. Конечно, пока что этот раздел практически не используется, но если перейти в графический режим и запустить пару мощных приложений, то и swap-раздела не хватит.

Программа top будет обновлять информацию о загрузке процессора с определенным интервалом времени. Для выхода из программы нажмите комбинацию клавиш <Ctrl>+<C>.

3.4.4. Зомби против растений

В системе иногда появляются процессы зомби, которые умирают. Я часто применяю Linux для запуска различных задач, по расписанию использую команду cron или просто скрипты, которые бесконечно работают в цикле и выполняют задачи в определенное время. ОС Linux в этом отношении удобна и достаточно надежна, но далеко не всегда надежны ее приложения.