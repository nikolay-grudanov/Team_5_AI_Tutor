---
source_image: page_224.png
page_number: 224
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.18
tokens: 5562
characters: 1321
timestamp: 2025-12-24T04:14:14.090001
finish_reason: stop
---

Параметр hidden подробно рассматривался в разделе «Включите параметр настройки hidden перед вызовом команды :argdo или :bufdo» в главе 6.
Если вы собираетесь следовать за примерами в этом рецепте, прочитайте раздел «Загружаемые примеры» во вступлении. Комплект файлов, с которыми мы будем здесь работать, находится в каталоге code/macros/ruby_module.

Создание списка целевых файлов

Давайте обозначим границы наших владений, создав список целевых файлов. Мы будем перемещаться по ним с применением списка аргументов (рецепт 37 в главе 6):

⇒ :cd code/macros/ruby_module
⇒ :args *.rb

Если вызвать команду :args без аргументов, она выведет содержимое списка:

⇒ :args
[animal.rb] banker.rb frog.rb person.rb

Перемещаться по списку файлов можно с помощью команд :first, :last, :prev и :next.

Запись единицы правки

Перед началом убедимся, что находимся в начале списка аргументов:

⇒ :first

Теперь запишем в макрос необходимые операции:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>qa</td>
    <td># ...[end of copyright notice]<br>class Animal<br>    # implementation...<br>end</td>
  </tr>
  <tr>
    <td>gg/class<CR></td>
    <td># ...[end of copyright notice]<br><span style="color:red">c</span>lass Animal<br>    # implementation...<br>end</td>
  </tr>
</table>