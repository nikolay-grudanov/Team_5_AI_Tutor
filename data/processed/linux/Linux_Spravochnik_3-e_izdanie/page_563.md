---
source_image: page_563.png
page_number: 563
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.09
tokens: 11741
characters: 1781
timestamp: 2025-12-24T03:40:51.408769
finish_reason: stop
---

<table>
  <tr>
    <th>read</th>
    <td>
      <ul>
        <li><b>-r</b> Режим без преобразования; символ продолжения строки (\) игнорируется.</li>
        <li><b>-s</b> Не отображать символы, вводимые пользователем (возможность полезна при запросе паролей).</li>
        <li><b>-t seconds</b><br>Для диалогового ввода установить интервал ожидания в указанное количество секунд, по истечении которых возвращать соответствующие переменные неинициализированными.</li>
      </ul>
      <h3>Примеры</h3>
      <pre>
$ read first last address
Sarah Caldwell 123 Main Street
$ echo "$last, $first\n$address"
Caldwell, Sarah
123 Main Street
      </pre>
      В следующих командах производится чтение пароля в переменную $user_pw и отображение значения этой переменной, при этом используются относительно новые параметры, которые поддерживаются не всеми версиями bash.
      <pre>
$ read -sp "Введите пароль (буквы не отображаются при вводе)" user_pw
Введите пароль (буквы не отображаются при вводе)
$ echo $user_pw
Вам это знать не положено!
      </pre>
      Следующий сценарий читает данные из файла паролей, в котором поля разделяются двоеточием (что и делает этот файл популярным объектом для примеров разбора ввода):
      <pre>
IFS=:
cat /etc/passwd |
while
read account pw user group gecos home shell
do
echo "Account name $account has user info $gecos"
done
      </pre>
    </td>
  </tr>
  <tr>
    <th>readonly</th>
    <td>
      <b>readonly [options] [variable1 variable2 ...]</b>
      <p>Запретить присваивание новых значений перечисленным переменным интерпретатора. Можно читать значения переменных, но изменять их нельзя. В интерпретаторе bash для присваивания неизменяемого значения допускается следующая запись: <i>variable=value</i>.</p>
    </td>
  </tr>
</table>