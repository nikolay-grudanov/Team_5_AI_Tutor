---
source_image: page_508.png
page_number: 508
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.88
tokens: 11672
characters: 1788
timestamp: 2025-12-24T09:48:43.147404
finish_reason: stop
---

вызове функции вы указываете, какое изображение хотите заменить (задавая соответствующий ID) и какой файл с новым изображением хотите использовать. Поскольку функция использует параметры, ее можно вызывать для замены любого изображения в ролловере для мыши в любом месте вашей страницы.

<script>
    function ChangeImage(imageName, newImageFile) {
        // Находит объект, представляющий элемент img
        var image = document.getElementById(imageName)

        // Изменяет изображение
        image.src = newImageFile
    }
</script>

При создании графического ролловера вам понадобятся два события. Событие onmouseover переходит к изображению ролловера, а событие onmouseout (запускающееся, когда посетитель отводит указатель мыши в сторону от HTML-элемента) возвращает назад исходное изображение. На рис. 15.8 показан результат.

<img id="SwappableImage" src="pic1.gif" alt="" onmouseover="ChangeImage('SwappableImage', 'LostInterestMessage.gif')" onmouseout="ChangeImage('SwappableImage', 'ClickMe.gif')" />

![Графический ролловер в действии](image_rollover.png)

Рис. 15.8. Графический ролловер в действии

Если хотите вставить дополнительные изображения в ролловер, просто добавьте новый элемент <img> с другим именем. Следующий элемент использует то же самое исходное изображение, но отображает другое изображение при каждом наведении посетителем указателя мыши на картинку и отведении указателя мыши в сторону.

<img id="SwappableImage2" src="pic1.gif" alt="" onmouseover="ChangeImage('SwappableImage2', 'MouseOverPicture.gif')" onmouseout="ChangeImage('SwappableImage2', 'InitialPicture.gif')" />

Если хотите создать причудливый эффект, можно использовать даже событие onclick (которое запускается при щелчке элемента кнопкой мыши) и добавить еще одно изображение в набор.