---
source_image: page_869.png
page_number: 869
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.48
tokens: 11886
characters: 2099
timestamp: 2025-12-24T03:54:35.636451
finish_reason: stop
---

Немногим пользователям требуется такой объем рабочего пространства. Но даже если вы добавите всего один рабочий стол, имейте в виду, что, возможно, придется изменить размеры пейджера и, соответственно, размеры панели кнопок, на которой он располагается, чтобы все ваши рабочие столы не занимали слишком много места. Также может потребоваться освободить место для размещения пейджера.

Существует несколько параметров, с которыми можно экспериментировать в целях освобождения места для пейджера, показывающего несколько рабочих столов:

• Размеры панели кнопок (модуль FvwmButtons)
• Количество колонок, на которое разделена панель кнопок
• Сколько из этих колонок занимает пейджер

Типичный модуль FvwmButtons занимает 520 точек в ширину и 100 точек в высоту:

*FvwmButtonsGeometry 520x100-1-1

Он также может быть настроен для отображения в две строки и пять колонок (размеры которых полностью зависят от геометрии FvwmButtons):

*FvwmButtons(Frame 2 Padding 2 2 Container(Rows 2 Columns 5 Frame 1 Padding 10 0))

В данной конкретной настройке пейджер занимает одну колонку в двух строках модуля FvwmButtons:

*FvwmButtons(1x2 Frame 2 Swallow(UseOld) "FvwmPager" "Module FvwmPager 0 1")

Менеджер пиктограмм занимает три колонки:

*FvwmButtons(3x2 Frame 2 Swallow "FvwmIconMan" "Module FvwmIconMan")

И оставшаяся колонка отводится под приложения рабочего стола (например, xbiff, xclock, xload), которые выполняются в контейнере (Container) в модуле FvwmButtons:

*FvwmButtons(1x2 Frame 0 Container(Rows 2 Columns 2 Frame 0))
*FvwmButtons(Frame 2 Swallow(UseOld,NoHints,Respawn) "xbiff" 'Exec exec xbiff -bg bisque3')
*FvwmButtons(Frame 3 Swallow(UseOld,NoHints,Respawn) "xclock" 'Exec exec xclock -bg bisque3 -fg black -hd black -hl black -padding 0 update 1')
*FvwmButtons(2x1 Frame 2 Swallow(UseOld,NoHints,Respawn) "xload" 'Exec exec xload -bg bisque3 -fg black -update 5 -nolabel')

Обратите внимание, что контейнер имеет дальнейшее разделение на две строки и две колонки, в которых могут располагаться приложения. Надеемся, это не запутает читателей (разбор файла настройки требует внимания).