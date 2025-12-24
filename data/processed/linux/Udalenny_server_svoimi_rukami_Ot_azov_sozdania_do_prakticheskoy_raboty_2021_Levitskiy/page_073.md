---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.02
tokens: 6260
characters: 952
timestamp: 2025-12-24T03:57:52.927660
finish_reason: stop
---

sudo apt install mc
sudo apt install synaptic

3.13. Тонкая настройка GNOME. Установка темы оформления в стиле macOS

Множество настроек графической среды GNOME скрыто от глаз пользователя. Для более тонкой настройки GNOME вы можете использовать утилиту Gnome Tweaks, позволяющую легко кастомизировать ваш рабочий стол. Для ее установки введите команды:

$ sudo add-apt-repository universe
$ sudo apt install gnome-tweak-tool

Первая команда включает репозитарий universe, в котором находится нужный нам пакет. Вполне возможно, что он уже включен у вас, но лучше убедиться в этом явно. Вторая — устанавливает сам пакет.

Далее запустите средство командой или выберите из меню команду Дополнительные настройки GNOME:

$ gnome-tweaks

Данная утилита — настоящая находка для любителей кастомизации (рис. 3.18). Кстати, только с ее помощью можно изменить тему оформления в

![Приложение Gnome Tweaks](../images/3.18.png)

Рис. 3.18. Приложение Gnome Tweaks