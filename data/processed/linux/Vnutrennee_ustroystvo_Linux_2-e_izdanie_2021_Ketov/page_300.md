---
source_image: page_300.png
page_number: 300
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.45
tokens: 7151
characters: 766
timestamp: 2025-12-24T04:40:28.518306
finish_reason: stop
---

**Листинг 7.11. Оконный менеджер mwm**

homer@ubuntu:~$ kill %twm
[5]+ Завершён тwm
homer@ubuntu:~$ mwm &
[5] 14090

![Оконный менеджер mwm (Motif Window Manager)](https://i.imgur.com/3Q5z5QG.png)

Рис. 7.4. Оконный менеджер mwm (Motif Window Manager)

Более поздние оконные менеджеры, как, например, W:[IceWM], представленный в листинге 7.12 и на рис. 7.5, зачастую имеют «панель задач» снизу, кнопку «Пуск» с главным меню слева панели задач, область уведомлений («трей») справа панели задач и прочие «современные» элементы пользовательского интерфейса.

**Листинг 7.12. Оконный менеджер icewm**

homer@ubuntu:~$ kill -9 %mwm
[5]+ Убито mwm
homer@ubuntu:~$ icewm-session &
[5] 15315
homer@ubuntu:~$ pstree 15315
★ icewm-session─┬─icewm
                │   └─icewmbg