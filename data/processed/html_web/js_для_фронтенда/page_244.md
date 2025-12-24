---
source_image: page_244.png
page_number: 244
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.41
tokens: 6163
characters: 1199
timestamp: 2025-12-24T10:07:37.200318
finish_reason: stop
---

current += countBy;
return (current > upTill) ? NaN : current;
}
ret.displayName = "Iterator от " + startAt + " до "
    + upTill + " by " + countBy;
return ret;
}

Здесь я добавил свойство displayName к анонимной функции, благодаря чему информация на панели Стек вызовов стала понятнее, см. рис. 7.5. Вместо (?) мы получили описывающее имя, да еще и с параметрами функции. Теперь мы знаем, что есть что.

![Анонимная функция со свойством displayName в Firebug](https://i.imgur.com/3Q5z5QG.png)

Рис. 7.5. Анонимная функция со свойством displayName в Firebug

Отладчик Chrome

У Chrome есть аналогичный набор инструментов разработчика (https://developers.google.com/chrome-developer-tools/?hl=ru), получить доступ к которому можно, выбрав в окне браузера Chrome Инструменты > Инструменты разработчика или нажав сочетание клавиш Ctrl + Shift + I. Инструменты разработчика могут отображаться в одном окне с отлаживаемой веб-страницей, а могут быть выделены в отдельное окно.

На рис. 7.6 показано, как все это будет выглядеть при изначально открытой в браузере странице Yahoo.com.

Инструменты разработчика Google Chrome содержат ряд вкладок, подобных тем, которые вы видели в Firebug. При этом вклад-