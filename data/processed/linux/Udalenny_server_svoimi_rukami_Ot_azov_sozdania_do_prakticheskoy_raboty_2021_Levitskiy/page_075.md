---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.50
tokens: 6548
characters: 1730
timestamp: 2025-12-24T03:58:02.569341
finish_reason: stop
---

Удаленный сервер своими руками

Установить новую тему достаточно просто. Скачайте архив с темой. Много тем оформления доступно на сайте https://www.gnome-look.org/, например, по адресу https://www.gnome-look.org/p/1275087/ доступна тема в стиле macOS. Перед установкой этой темы нужно установить два пакета:

$ sudo apt install gtk2-engines-murrine gtk2-engines-pixbuf

Далее нужно скачать архив с темой и распаковать его в каталог .themes:

$ tar xf Mojave-dark.tar.xz
$ mkdir ~/.themes
$ mv Mojave-dark ~/.themes/

Затем откройте Gnome Tweaks и в качестве темы приложений выберите Mojave-dark. Закройте Gnome Tweaks.

Следующий шаг — скачать значки в стиле macOS. Они доступны по адресу https://www.gnome-look.org/p/1210856/. Аналогично, значки нужно распаковать:

$ tar xf Mojave-CT-Night-Mode.tar.xz
$ mkdir ~/.icons
$ mv Mojave-CT-Night-Mode ~/.icons/

После этого опять запустите Gnome Tweaks и в качестве темы значков выберите Mojave-CT-Night-Mode. Наконец, нужно установить тему для курсоров мыши. Скачайте архив по адресу https://www.gnome-look.org/p/1148748/ и распакуйте архив в соответствующий каталог:

$ unzip -qq macOS\ Cursor\ Set.zip
$ mv macOS\ Cursor\ Set ~/.icons/

Опять запустите Gnome Tweaks и выберите MacOS Cursor Set в качестве темы курсоров.

На рис. 3.21 показан процесс распаковки необходимых архивов, а на рис. 3.22 — настройки, сделанные в Gnome Tweaks. У вас должно получиться так, как показано на рис. 3.22. Обратите внимание, как изменились значки в заголовках окон и значки приложений на панели задач.

Следующий шаг (по желанию) — скачать и установить в качестве фонаового следующее изображение: https://www.reddit.com/r/wallpapers/comments/e4fz6s/a_more_purpleish_version_of_the_mac_os_mojave/