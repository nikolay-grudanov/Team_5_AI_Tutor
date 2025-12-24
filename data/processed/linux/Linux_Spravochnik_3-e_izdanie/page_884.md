---
source_image: page_884.png
page_number: 884
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.37
tokens: 11597
characters: 1258
timestamp: 2025-12-24T03:54:55.708259
finish_reason: stop
---

*FvwmWinListFont -adobe-helvetica-bold-r-*--10-*-*-*-*-*-*-
*FvwmWinListAction Click1 Iconify -1, Focus
*FvwmWinListAction Click2 Iconify
*FvwmWinListAction Click3 Module "FvwmIdent" FvwmIdent
*FvwmWinListUseSkipList
*FvwmWinListGeometry +0-1

Первые три строки определяют цвет фона, цвет текста и используемый в приложении шрифт. Следующие три привязывают нажатия на различные кнопки мыши к определенным действиям внутри WinList. UseSkipList является предписанием для WinList не отображать строки для окон, которым присвоена стилевая классификация WindowListSkip. Как правило, таким образом скрываются все модули, в результате чего они не отображаются в списке FvwmWinList. Последняя строка определяет точку экрана, в которой должно появляться окно (левый нижний угол).

WinList является липким окном, т. е. оно доступно на каждом рабочем столе. Файл настройки может вводить в заблуждение. Данное свойство определяется в другом месте файла посредством переменной Style:

    Style "*Fvwm*"    NoTitle, Sticky, WindowListSkip

Эта строка определяет свойства липкости, отсутствия заголовка и отсутствия всех модулей (включая WinList) в списке окон FvwmWinList. В случае же с модулем FvwmWinList, появись он в собственном списке, это было бы более чем странно.