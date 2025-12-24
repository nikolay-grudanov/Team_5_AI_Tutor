---
source_image: page_432.png
page_number: 432
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.52
tokens: 7556
characters: 2091
timestamp: 2025-12-24T04:57:36.246089
finish_reason: stop
---

Понимание концепции целевых юнитов systemd упрощает понимание процесса загрузки Linux-сервера, использующего службу systemd. При загрузке службы systemd активизирует юнит default.target. Он является псевдонимом либо multi-user.target, либо graphical.target. Таким образом, в зависимости от установленных псевдонимов alias запускаются службы, на которые ориентирован целевой юнит.

Чтобы получить дополнительную информацию о демоне systemd, введите команду man -k systemd в командной строке.

Обратная совместимость служб systemd с SysVinit

Демон systemd поддерживает обратную совместимость с демоном SysVinit. Это позволяет дистрибутивам Linux постепенно переходить на использование демона systemd.

Хотя уровни выполнения не являются частью systemd, инфраструктура systemd создавалась для того, чтобы обеспечить совместимость с концепцией уровней выполнения. Существует семь файлов конфигурации целевого юнита, специально созданных для обратной совместимости с SysVinit:

● runlevel0.target;
● runlevel1.target;
● runlevel2.target;
● runlevel3.target;
● runlevel4.target;
● runlevel5.target;
● runlevel6.target.

Как вы, вероятно, уже поняли, для каждого из семи классических уровней запуска SysVinit существует файл конфигурации целевого юнита. Эти файлы символически связаны с файлами конфигурации целевого юнита, наиболее точно соответствующими исходному уровню выполнения. В следующем примере отображены символические ссылки для целевых юнитов уровня выполнения. Обратите внимание на то, что целевые юниты уровней выполнения 2, 3 и 4 символически связаны с юнитом multi-user.target, который наследует расширенный многопользовательский режим:

# ls -l /lib/systemd/system/runlevel*.target
lrwxrwxrwx. 1 root root 15 Apr 9 04:25 /lib/systemd/system/runlevel0.target
    -> poweroff.target
lrwxrwxrwx. 1 root root 13 Apr 9 04:25 /lib/systemd/system/runlevel1.target
    -> rescue.target
lrwxrwxrwx. 1 root root 17 Apr 9 04:25 /lib/systemd/system/runlevel2.target
    -> multi-user.target
lrwxrwxrwx. 1 root root 17 Apr 9 04:25 /lib/systemd/system/runlevel3.target
    -> multi-user.target