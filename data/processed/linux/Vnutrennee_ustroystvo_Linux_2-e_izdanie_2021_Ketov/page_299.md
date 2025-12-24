---
source_image: page_299.png
page_number: 299
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.29
tokens: 7228
characters: 1037
timestamp: 2025-12-24T04:40:32.872118
finish_reason: stop
---

W:[SunOS]. Начиная с Ubuntu Linux 18.04 olwm(1) (что ожидаемо), больше не доступен (листинг 7.10), но можно взглянуть на его W:EN:[look and feel] на рис. 7.3.

Листинг 7.10. Оконный менеджер olwm

homer@ubuntu:~$ olwm
Команда "olvvm" не найдена. Возможно, вы имели в виду:

command 'olam' from snap olam (0+git.c66238a)
command 'lvm' from deb lvm2 (2.03.02-2ubuntu6)
command 'rlvm' from deb rlvm (0.14-3build1)

See 'snap info <snapname>' for additional versions.

homer@ubuntu:~$ apt search olwm
Сортировка... Готово
Полнотекстовый поиск... Готово
homer@ubuntu:~$ apt-file search bin/olwm

![Оконный менеджер olwm](../images/ch7_3.png)

Рис. 7.3. Оконный менеджер olwm (OpenLook Window Manager)

Еще один оконный менеджер «из прошлого», W:[Motif Window Manager], mwm(1), являющийся частью настольного окружения W:[CDE], проиллюстрирован в листинге 7.11 и на рис. 7.4. Как и twm(1) и olwm(1), окна приложений под управлением mwm(1) при минимизации сворачиваются в значки на «рабочем столе», а главное меню вызывается правой кнопкой мыши.