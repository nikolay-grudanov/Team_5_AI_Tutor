---
source_image: page_546.png
page_number: 546
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.78
tokens: 11725
characters: 1674
timestamp: 2025-12-24T09:50:25.378201
finish_reason: stop
---

margin-top: 30px;
margin-right: 20px;
}

В этих стилях нет ничего нового. Вы видели их в предыдущих примерах.

Пришло время создавать меню. Его структура очень похожа на предыдущие примеры в этой главе. По сути, каждый сворачиваемый раздел меню состоит из контейнера <div>, заполненного элементами-якорями. Единственное дополнительное свойство — текст заголовка, содержащийся в элементе <span>, который вставлен в начало элемента <div>.

<div>
  <span>About Me</span>
  <a href="...">My Traumatic Childhood</a>
  <a href="...">My Education</a>
  <a href="...">Painful Episodes</a>
</div>

Типичное меню Slashdot содержит несколько сворачиваемых разделов. Вы заключаете их все в еще один элемент <div> и присваиваете ему имя, совпадающее с именем меню в сценарии.

<div class="sdmenu" id="my_menu">
  ...
</div>

Этого достаточно для создания меню Slashdot со всем его форматированием и функциональностью в полном составе. Но возможно вам захочется заключить <div> для Slashdot в еще один <div>, представляющий боковую панель меню. В этом случае вы сможете поместить боковую панель точно туда, куда захотите, не беспокоясь о конфликтах в таблице стилей или модификации файла sdmenu.css.

<div class="MenuBar">
  <div class="sdmenu" id="my_menu">
    ...
  </div>
</div>

Далее приведена разметка целиком для меню, показанного на рис. 16.8.

<div class="MenuBar">
  <div class="sdmenu" id="my_menu">
    <div>
      <span>About Me</span>
      <a href="...">My Traumatic Childhood</a>
      <a href="...">My Education</a>
      <a href="...">Painful Episodes</a>
    </div>
    <div>
      <span>My Store</span>
      <a href="...">Buy Something</a>
    </div>
  </div>
</div>