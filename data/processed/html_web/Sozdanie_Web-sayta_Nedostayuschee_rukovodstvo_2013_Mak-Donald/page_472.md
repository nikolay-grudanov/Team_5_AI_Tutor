---
source_image: page_472.png
page_number: 472
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.59
tokens: 11874
characters: 2259
timestamp: 2025-12-24T09:47:22.110482
finish_reason: stop
---

можно указать URL изображения. (Если позже захотите применить другую кнопку, вы всегда можете изменить HTML-код, сгенерированный PayPal.)

7. Прокрутите страницу и при желании введите дополнительные параметры.

Например, нужен ли вам адрес покупателя (PayPal полагает, что нужен), хотите ли вы, чтобы покупатели добавили свои комментарии к платежу (обычно они не могут), и должен ли PayPal направлять посетителей в определенное место после завершения или отмены платежа (вы можете отправить покупателей на определенный URL на вашем сайте вместо стандартных страниц PayPal).

8. Щелкните мышью кнопку Create Button (Создать кнопку).

PayPal отображает текстовое поле с разметкой для вашей настроенной кнопки Buy Now (Купить сейчас). Скопируйте и вставьте разметку на вашу Web-страницу.

Когда создается кнопка Buy Now (Купить сейчас), PayPal помещает все внутрь элемента <form> (см. разд. "Элементы формы" главы 15). Далее приведен пример кнопки для пары самодельных носков оригами, основанной на последних нескольких пунктах, приведенных ранее.

<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_s-xclick" />
<input type="hidden" name="hosted_button_id" value="633788" />
<table>
<tr><td>
<input type="hidden" name="on0" value="Choose a Color" />
Choose a Color</td></tr><tr><td>
<select name="os0">
<option value="Yellow">Yellow</option>
<option value="Green">Green</option>
<option value="Tomato">Tomato</option>
<option value="Chartreuse">Chartreuse</option>
</select>
</td></tr>
</table>
<input type="image" border="0" name="submit" alt="" src="https://www.paypal.com/en_US/i/btn/btn_buynowCC_LG.gif" />
<img src="https://www.paypal.com/en_US/i/scr/pixel.gif" alt="" width="1" height="1" />
</form>

Если вы добавили варианты, то увидите в HTML-коде элементы <select> и <option>, описывающие соответствующие поля списка (см. табл. 15.3). Вы можете изменить у кнопки атрибут src (выделенный жирным шрифтом в только что приведенном листинге) и указать на другой файл изображения. PayPal вставляет после кода для кнопки Buy Now (Купить сейчас) невидимое изображение (pixel.gif в приведенном примере), которое отслеживает просмотры страницы. (Это тот же метод отслеживания, который использует Amazon.)