---
source_image: page_605.png
page_number: 605
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 66.06
tokens: 12210
characters: 2400
timestamp: 2025-12-24T03:42:59.683400
finish_reason: stop
---

Усечение

<table>
  <tr>
    <th>Модификатор</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>:r</td>
    <td>Извлечение первого доступного корня путевого имени (до последнего символа точки)</td>
  </tr>
  <tr>
    <td>:gr</td>
    <td>Извлечение всех корней</td>
  </tr>
  <tr>
    <td>:e</td>
    <td>Извлечение первого доступного расширения имени файла (символы за последней точкой)</td>
  </tr>
  <tr>
    <td>:ge</td>
    <td>Извлечение всех расширений</td>
  </tr>
  <tr>
    <td>:h</td>
    <td>Извлечение первого доступного заголовка (до последнего символа /)</td>
  </tr>
  <tr>
    <td>:gh</td>
    <td>Извлечение всех заголовков из имен файлов</td>
  </tr>
  <tr>
    <td>:t</td>
    <td>Извлечение первого доступного хвоста путевого имени (символы за последним слэшем)</td>
  </tr>
  <tr>
    <td>:gt</td>
    <td>Извлечение всех хвостов</td>
  </tr>
  <tr>
    <td>:u</td>
    <td>Перевод в верхний регистр первой строчной буквы (только в tcsh)</td>
  </tr>
  <tr>
    <td>:l</td>
    <td>Перевод в нижний регистр первой прописной буквы (только в tcsh)</td>
  </tr>
  <tr>
    <td>:a</td>
    <td>Применить к слову модификаторы, следующие за а, столько раз, сколько возможно. Если а используется совместно с модификатором g, то применяется ко всем словам (только в tcsh)</td>
  </tr>
</table>

Примеры использования модификаторов команд журнала

В продолжение вышеприведенных примеров команда номер 17 выглядит так:

%17 cat ch01 ch02 ch03

<table>
  <tr>
    <th>Номер события</th>
    <th>Введенная команда</th>
    <th>Выполняемая команда</th>
  </tr>
  <tr>
    <td>19</td>
    <td>!17:s/ch/CH</td>
    <td>cat CH01 ch02 ch03</td>
  </tr>
  <tr>
    <td>20</td>
    <td>!17g&</td>
    <td>cat CH01 CH02 CH03</td>
  </tr>
  <tr>
    <td>21</td>
    <td>!more:p</td>
    <td>more cprogs/01.c (<i>только отобразить</i>)</td>
  </tr>
  <tr>
    <td>22</td>
    <td>cd !$:h</td>
    <td>cd cprogs</td>
  </tr>
  <tr>
    <td>23</td>
    <td>vi !mo:$:t</td>
    <td>vi 01.c</td>
  </tr>
  <tr>
    <td>24</td>
    <td>grep stdio !$</td>
    <td>grep stdio 01.c</td>
  </tr>
  <tr>
    <td>25</td>
    <td>^stdio^include stdio^:q</td>
    <td>grep "include stdio" 01.c</td>
  </tr>
  <tr>
    <td>26</td>
    <td>nroff !21:t:p</td>
    <td>nroff 01.c (<i>это ли нам нужно?</i>)</td>
  </tr>
  <tr>
    <td>27</td>
    <td>!!</td>
    <td>nroff 01.c (<i>выполнить</i>)</td>
  </tr>
</table>