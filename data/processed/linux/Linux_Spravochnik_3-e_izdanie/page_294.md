---
source_image: page_294.png
page_number: 294
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.19
tokens: 11901
characters: 2096
timestamp: 2025-12-24T03:28:39.661529
finish_reason: stop
---

<table>
  <tr>
    <th>$(join list1, list2)</th>
    <td>Вернуть список, полученный векторной конкатенацией аргументов. Например, $(join a b, .c .o) вернет a.c b.o.</td>
    <td>make</td>
  </tr>
  <tr>
    <th>$(word n, string)</th>
    <td>Вернуть n-ное слово строки string.</td>
    <td></td>
  </tr>
  <tr>
    <th>$(words string)</th>
    <td>Вернуть количество слов в строке.</td>
    <td></td>
  </tr>
  <tr>
    <th>$(firstword list)</th>
    <td>Вернуть первое слово из списка list.</td>
    <td></td>
  </tr>
  <tr>
    <th>$(wildcard pattern)</th>
    <td>Вернуть список файлов из текущего каталога, соответствующих маске pattern.</td>
    <td></td>
  </tr>
  <tr>
    <th>$(origin variable)</th>
    <td>Вернуть одну из следующих строк, описывающих, как была определена переменная variable: undefined, default, environment, environment override, file, command line, override или automatic.</td>
    <td></td>
  </tr>
  <tr>
    <th>$(shell command)</th>
    <td>Вернуть результат выполнения команды. Символы новой строки преобразуются в пробелы. Функция работает аналогично подстановке по обратным кавычкам в большинстве командных интерпретаторов.</td>
    <td></td>
  </tr>
  <tr>
    <th>Подстановка строк в макросах</th>
    <td colspan="2"></td>
  </tr>
  <tr>
    <th>$(macro:s1=s2)</th>
    <td>Вычислить подстановку по текущему определению макроса $(macro), предварительно заменив строкой s2 каждое вхождение строки s1, непосредственно следующее перед пробелом или символом табуляции либо находящееся в конце строки макроопределения.</td>
    <td></td>
  </tr>
  <tr>
    <th>Специальные имена целей</th>
    <td colspan="2"></td>
  </tr>
  <tr>
    <th>.DEFAULT:</th>
    <td>Команды, ассоциированные с этой целью, выполняются, если make не может найти строки описаний в соответствующем файле или правила суффиксов, с помощью которых может быть собрана запрошённая цель.</td>
    <td></td>
  </tr>
  <tr>
    <th>.EXPORT_ALL_VARIABLES:</th>
    <td>Если существует эта цель, экспорттировать все макроопределения во все порожденные процессы.</td>
    <td></td>
  </tr>
</table>