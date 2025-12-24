---
source_image: page_311.png
page_number: 311
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.99
tokens: 7889
characters: 2414
timestamp: 2025-12-24T01:16:56.751552
finish_reason: stop
---

Таблица 9.2. Распространенные файловые операции

<table>
  <tr>
    <th>Операция</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>output = open(r'C:\spam', 'w')</td>
    <td>Создает выходной файл<br>('w' означает write — запись)</td>
  </tr>
  <tr>
    <td>input = open('data', 'r')</td>
    <td>Создает входной файл<br>('r' означает read — чтение)</td>
  </tr>
  <tr>
    <td>input = open('data')</td>
    <td>То же, что и в предыдущей строке<br>('r' выбирается по умолчанию)</td>
  </tr>
  <tr>
    <td>aString = input.read()</td>
    <td>Читает целый файл в одиночную строку</td>
  </tr>
  <tr>
    <td>aString = input.read(N)</td>
    <td>Читает до N следующих символов (или байтов) в строку</td>
  </tr>
  <tr>
    <td>aString = input.readline()</td>
    <td>Читает следующую строку файла (включая символ новой строки \n) в строку</td>
  </tr>
  <tr>
    <td>aList = input.readlines()</td>
    <td>Читает целый файл в список строк (с символами \n)</td>
  </tr>
  <tr>
    <td>output.write(aString)</td>
    <td>Записывает строку символов (или байтов) в файл</td>
  </tr>
  <tr>
    <td>output.writelines(aList)</td>
    <td>Записывает все строки из списка в файл</td>
  </tr>
  <tr>
    <td>output.close()</td>
    <td>Вручную закрывает файл (это делается автоматически, когда файловый объект подвергается сборке мусора)</td>
  </tr>
  <tr>
    <td>output.flush()</td>
    <td>Сбрасывает буфер вывода на диск, не закрывая файл</td>
  </tr>
  <tr>
    <td>anyFile.seek(N)</td>
    <td>Изменяет позицию на N для следующей операции</td>
  </tr>
  <tr>
    <td>for line in open('data'):<br>    использовать строку</td>
    <td>Файловые итераторы, читающие строку за строкой</td>
  </tr>
  <tr>
    <td>open('f.txt', encoding='latin-1')</td>
    <td>Текстовые файлы Unicode в Python 3.x (строки str)</td>
  </tr>
  <tr>
    <td>open('f.bin', 'rb')</td>
    <td>Байтовые файлы в Python 3.x (строки bytes)</td>
  </tr>
  <tr>
    <td>codecs.open('f.txt', encoding='utf8')</td>
    <td>Текстовые файлы Unicode в Python 2.x (строки unicode)</td>
  </tr>
  <tr>
    <td>open('f.bin', 'rb')</td>
    <td>Байтовые файлы в Python 2.x (строки str)</td>
  </tr>
</table>

Открытие файлов

Для открытия файла в программе вызывается встроенная функция open с указанием имени внешнего файла и режима обработки. Вызов возвращает файловый объект, имеющий методы для передачи данных:

afile = open(имя_файла, режим)
afile.метод()