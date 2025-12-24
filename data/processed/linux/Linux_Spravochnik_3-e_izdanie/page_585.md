---
source_image: page_585.png
page_number: 585
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.23
tokens: 11852
characters: 1951
timestamp: 2025-12-24T03:41:44.641207
finish_reason: stop
---

<table>
  <tr>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td><i>cmd | tee files</i></td>
    <td>Перенаправить результат работы команды на стандартный вывод (обычно терминал) и в файлы <i>files</i> (см. примеры в описании команды <b>tee</b> в главе 3)</td>
  </tr>
</table>

Примеры

% cat part1 > book
% cat part2 part3 >> book

% mail tim < report
% cc calc.c >& error_out

% cc newcalc.c >! error_out
% grep Unix ch* |& pr

% (find / -print > filelist) >& no_access

% sed 's/^\XX/' << "END_ARCHIVE"
This is often how a shell archive is "wrapped",
bundling text for distribution. You would normally
run sed from a shell program, not from the command line.
"END_ARCHIVE"

Скопировать part1 в book
Добавить part2 и part3 в тот же файл, что и part1
Получить текст сообщения из report
Сохранить все сообщения, включая сообщения об ошибках
Перезаписать старый файл
Передать все сообщения (включая сообщения об ошибках) через конвейер
Отделить сообщения об ошибках от списка файлов
Вести текст до слова END_ARCHIVE

Переменные

В этом разделе представлены следующие темы:

• Подстановка значений переменных
• Модификаторы переменных
• Предопределенные переменные интерпретатора
• Форматирование переменной приглашения
• Пример файла .cshrc
• Переменные окружения

Подстановка значений переменных

В приводимых ниже вариантах подстановок фигурные скобки необязательны, за исключением тех случаев, когда имя переменной необходимо отделить от следующего символа, который иначе считался бы частью имени.

<table>
  <tr>
    <th>Переменная</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>${var}</td>
    <td>Значение переменной <i>var</i></td>
  </tr>
  <tr>
    <td>${var[i]}</td>
    <td>Выбрать слово (или слова) в <i>i</i>-й позиции строки <i>var</i>. <i>i</i> может быть обычным числом, диапазоном в виде <i>m-n</i>, диапазоном в виде <i>-n</i> (отсутствующее <i>m</i> принимает значение 1), диапазоном в виде <i>m-</i> (отсутствую-