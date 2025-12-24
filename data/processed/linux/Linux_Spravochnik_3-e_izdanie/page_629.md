---
source_image: page_629.png
page_number: 629
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.62
tokens: 11714
characters: 1441
timestamp: 2025-12-24T03:43:45.365759
finish_reason: stop
---

<table>
  <tr>
    <th>pushd</th>
    <td>производит прокрутку n-го каталога к вершине стека и делает его рабочим (нумерация начинается с 0). Команда без аргументов меняет местами два каталога на вершине стека и заменяет текущий рабочий каталог. Параметры +n, -l, -n и -v имеют такой же смысл, как и в popd. См. также dirs и popd.<br><b>Примеры</b><br>% dirs<br>/home/bob /usr<br>% pushd /etc<br>/etc /home/bob /usr<br>% pushd +2<br>/usr /etc /home/bob<br>% pushd<br>/etc /usr /home/bob<br>% popd<br>/usr /home/bob<br><i>Добавить /etc в стек каталогов</i><br><i>Переход к третьему каталогу</i><br><i>Обменять местами два первых каталога</i><br><i>Удалить текущую позицию; перейти к следующей</i></td>
  </tr>
  <tr>
    <th>rehash</th>
    <td><b>rehash</b><br>Создать заново хеш-таблицу для переменной PATH. Используется, когда в текущем сеансе добавлена новая команда. Это позволяет быстрее находить и выполнять команду. Путь к добавляемой команде (программе) следует добавить в переменную PATH, прежде чем выполнять rehash. См. также unhash.</td>
  </tr>
  <tr>
    <th>repeat</th>
    <td><b>repeat n command</b><br>Выполнить команду n раз.<br><b>Примеры</b><br>Распечатать три копии файла memo:<br>% repeat 3 pr memo | lp<br>Прочесть 10 строк с терминала и сохранить в файле item_list:<br>% repeat 10 line > item_list<br>Добавить 50 экземпляров файла шаблонов к отчету report:<br>% repeat 50 cat template >> report</td>
  </tr>
</table>