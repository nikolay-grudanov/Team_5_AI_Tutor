---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.22
tokens: 6150
characters: 571
timestamp: 2025-12-24T03:57:53.339442
finish_reason: stop
---

Откройте Gnome Tweaks и перейдите в раздел Автозапуск. Нажмите кнопку + и добавьте в автозапуск приложение Plank. Так мы обеспечим автоматический запуск нашей панели при входе в систему пользователя (рис. 3.25).

![Автоматический запуск панели задач Plank](../images/ch3_25.png)

Рис. 3.25. Автоматический запуск панели задач Plank

Осталось удалить стандартную панель задач. Для этого введите команду:

$ sudo apt remove gnome-shell-extension-ubuntu-dock

После этой команды нужно выйти из системы и снова в нее войти. В результате у вас должна получиться «почти» macOS.