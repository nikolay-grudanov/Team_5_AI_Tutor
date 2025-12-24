---
source_image: page_316.png
page_number: 316
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.63
tokens: 5736
characters: 1871
timestamp: 2025-12-24T04:16:15.876635
finish_reason: stop
---

Рецепт 103. Навигация по определениям ключевых слов

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>&lt;C-]&gt;</td>
    <td>
      require './speaker.rb'<br>
      class Anglophone &lt; Speaker<br>
      def speak<br>
        puts "Hello, my name is #{@name}"<br>
      end<br>
      Anglophone.new('Jack').speak
    </td>
  </tr>
</table>

В данном случае определение класса Anglophone оказалось в том же буфере, но если установить курсор на ключевое слово Speaker и вызвать ту же команду еще раз, будет открыт буфер с определением этого класса:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>fS</td>
    <td>
      require './speaker.rb'<br>
      class Anglophone &lt; Speaker<br>
      def speak<br>
        puts "Hello, my name is #{@name}"<br>
      end<br>
      Anglophone.new('Jack').speak
    </td>
  </tr>
  <tr>
    <td>&lt;C-]&gt;</td>
    <td>
      class Speaker<br>
      def initialize(name)<br>
        @name = name<br>
      end<br>
      def speak<br>
        puts "#{name}"<br>
      end<br>
      end
    </td>
  </tr>
</table>

При навигации по исходным кодам таким способом Vim запоминает историю посещавшихся индексов. Команда &lt;C-t&gt; действует подобно кнопке Back (Назад) браузера, возвращая нас назад на один шаг. Если нажать ее прямо сейчас, редактор вернется к определению Anglophone, а если нажать ее еще раз, он вернется в то место, откуда мы начали. За дополнительной информацией по приемам работы со списком переходов по индексам обращайтесь к разделу справки :h tag-stack http://vimdoc.sourceforge.net/htmldoc/tagsrch.html#tag-stack.

Определение точки перехода при наличии нескольких совпадений с ключевым словом

В предыдущем примере мы не испытывали никаких сложностей, потому что исходный код демонстрационного проекта содержал