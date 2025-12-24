---
source_image: page_692.png
page_number: 692
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.57
tokens: 11874
characters: 1965
timestamp: 2025-12-24T03:46:48.271692
finish_reason: stop
---

<table>
  <tr>
    <th>se parameter1 parameter2 ...</th>
    <th>set</th>
  </tr>
  <tr>
    <td>Установить значения parameter1 и parameter2. Команда без параметров выводит те из них, значения которых отличаются от принятых по умолчанию. Для булевых переменных, имеющих состояния включено/выключено, значения могут устанавливаться как parameter или noparameter (как в первом примере). Другим параметрам можно присваивать значения, используя синтаксис parameter=value. Ключевое слово all перечисляет параметры и их текущие значения.</td>
    <td></td>
  </tr>
  <tr>
    <th>Примеры</th>
    <th></th>
  </tr>
  <tr>
    <td>:set nows wm=10<br>:set all</td>
    <td></td>
  </tr>
  <tr>
    <th>sh</th>
    <th>shell</th>
  </tr>
  <tr>
    <td>Создать экземпляр интерпретатора. Продолжить редактирование по завершении работы с ним.</td>
    <td></td>
  </tr>
  <tr>
    <th>so file</th>
    <th>source</th>
  </tr>
  <tr>
    <td>Прочитать и выполнить команды ex из файла file.</td>
    <td></td>
  </tr>
  <tr>
    <th>Пример</th>
    <th></th>
  </tr>
  <tr>
    <td>:so $HOME/.exrc</td>
    <td></td>
  </tr>
  <tr>
    <th>st</th>
    <th>stop</th>
  </tr>
  <tr>
    <td>Приостановить сеанс редактирования. Идентично Ctrl-Z.<br>Команда fg позволяет продолжить работу с редактором.</td>
    <td></td>
  </tr>
  <tr>
    <th>[address] s [/pattern/replacement/][options][count]</th>
    <th>substitute</th>
  </tr>
  <tr>
    <td>Заменить в указанных строках (address) каждое соответствие шаблону pattern на replacement. Если опущены шаблон и подстановка, повторить последнюю замену. Параметр count определяет количество строк, в которых должна производиться замена, начиная со строки address. Если команде замены предшествует команда global (g) или v, шаблон может быть опущен; в таком случае используемый шаблон определяется этими командами. Большее количество примеров приводится в разделе «Примеры поиска и замены» главы 9.</td>
    <td></td>
  </tr>
</table>