---
source_image: page_169.png
page_number: 169
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.48
tokens: 7365
characters: 1553
timestamp: 2025-12-24T03:05:16.428650
finish_reason: stop
---

Файл control. В этом файле задаются название пакета, его описание и все необходимые для сборки и работы пакета зависимости. Он также отличается жестко заданным форматом, но его редко приходится менять (в отличие от файла changelog). Этот файл требует использовать Python 3, а также следовать рекомендациям по наименованиям Python для Debian.

При переходе от Python 2 к Python 3 большинство дистрибутивов остановились на применении для пакетов Python 3 схемы наименования python3-{название пакета}.

После добавления зависимостей, соглашений о наименованиях и короткого описания файл должен выглядеть вот так:

Source: hello-world
Maintainer: Alfredo Deza <alfredo@example.com>
Section: python
Priority: optional
Build-Depends:
debhelper (>= 11~),
dh-python,
python3-all
python3-setuptools
Standards-Version: 4.3.0

Package: python3-hello-world
Architecture: all
Depends: ${misc:Depends}, ${python3:Depends}
Description: An example hello-world package built with Python 3

Прочие необходимые файлы. Для генерации пакета Debian необходимо еще несколько файлов. Большинство из них состоят всего из нескольких строк и меняются нечасто.

Файл rules представляет собой исполняемый файл, указывающий Debian, что нужно запустить для генерации пакета, в данном случае он должен выглядеть так:

#!/usr/bin/make -f

export DH_VERBOSE=1

export PYBUILD_NAME=remoto

%:
    dh $@ --with python3 --buildsystem=pybuild

Файл compat задает уровень совместимости с debhelper (еще одна утилита для создания пакетов), рекомендуемое значение 10. Если вы получите связанное