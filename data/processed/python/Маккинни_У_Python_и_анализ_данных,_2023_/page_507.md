---
source_image: page_507.png
page_number: 507
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.85
tokens: 7710
characters: 1878
timestamp: 2025-12-24T02:54:22.871680
finish_reason: stop
---

ipdb> s
--Call--
> /home/wesm/code/pydata-book/examples/ipython_bug.py(6) throws_an_exception()
    5
----> 6 def throws_an_exception():
     7     a = 5

ipdb> n
> /home/wesm/code/pydata-book/examples/ipython_bug.py(7) throws_an_exception()
    6 def throws_an_exception():
----> 7     a = 5
     8     b = 6

ipdb> n
> /home/wesm/code/pydata-book/examples/ipython_bug.py(8) throws_an_exception()
    7     a = 5
----> 8     b = 6
     9     assert(a + b == 10)

ipdb> n
> /home/wesm/code/pydata-book/examples/ipython_bug.py(9) throws_an_exception()
    8     b = 6
----> 9     assert(a + b == 10)
     10

ipdb> !a
5
ipdb> !b
6

Мой собственный опыт показывает, что для уверенного овладения интерактивным отладчиком нужно время и практика. В табл. В.4 приведен полный перечень команд отладчика. Если вы привыкли к IDE, то консольный отладчик на первых порах может показаться неуклюжим, но со временем это впечатление рассеется. В некоторых IDE для Python имеются отличные графические отладчики, так что всякий пользователь найдет что-то себе по вкусу.

Таблица В.4. Команды отладчика Python

<table>
  <tr>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>h(elp)</td>
    <td>Вывести список команд</td>
  </tr>
  <tr>
    <td>help <i>команда</i></td>
    <td>Показать документацию по <i>команде</i></td>
  </tr>
  <tr>
    <td>c(ontinue)</td>
    <td>Продолжить выполнение программы</td>
  </tr>
  <tr>
    <td>q(uit)</td>
    <td>Выйти из отладчика, прекратив выполнение кода</td>
  </tr>
  <tr>
    <td>b(reak) <i>номер</i></td>
    <td>Поставить точку останова на строке с указанным <i>номером</i> в текущем файле</td>
  </tr>
  <tr>
    <td>b <i>путь/к/файлу.ру:номер</i></td>
    <td>Поставить точку останова на строке с указанным <i>номером</i> в указанном файле</td>
  </tr>
  <tr>
    <td>s(tep)</td>
    <td>Войти внутрь функции</td>
  </tr>
</table>