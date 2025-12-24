---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.95
tokens: 7536
characters: 2000
timestamp: 2025-12-24T03:05:37.444948
finish_reason: stop
---

Утилита командной строки называется rpmbuild, а пакет — rpm-build, так что убедитесь, что rpmbuild (утилита командной строки) доступна для использования в терминале.

Для создания бинарного файла утилите rpmbuild необходима определенная структура каталогов. После их создания в каталоге SOURCES должен присутствовать файл source (сгенерированный setuptools файл tar.gz). Далее показано, как следует создавать эту структуру и как она будет выглядеть в итоге:

$ mkdir -p /opt/repo/centos/{SOURCES,SRPMS,SPECS,RPMS,BUILD}
$ cp dist/hello-world-0.0.1.tar.gz /opt/repo/centos/SOURCES/
$ tree /opt/repo/centos
/opt/repo/centos
│   └── BUILD
├── BUILDROOT
├── RPMS
├── SOURCES
│   └── hello-world-0.0.1.tar.gz
├── SPECS
└── SRPMS

6 directories, 1 file

Эта структура каталогов необходима всегда, причем по умолчанию утилита rpmbuild ожидает ее наличия в домашнем каталоге. Чтобы не сваливать все в одну кучу, воспользуемся другим местом в файловой системе (/opt/repo/centos). Это значит, что нам нужно попросить утилиту rpmbuild задействовать этот каталог. В результате благодаря флагу -ba будут сгенерированы бинарный файл и пакет source (мы немного сократили выводимое командой):

$ rpmbuild -ba --define "_topdir /opt/repo/centos" dist/hello-world.spec
...
Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.CmGOdp
running build
running build_py
creating build
creating build/lib
creating build/lib/hello_world
copying hello_world/main.py -> build/lib/hello_world
copying hello_world/__init__.py -> build/lib/hello_world
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.CQgOKD
+ python3 setup.py install --single-version-externally-managed \
-01 --root=/opt/repo/centos/BUILDROOT/hello-world-0.0.1-1.x86_64
running install
writing hello_world.egg-info/PKG-INFO
writing dependency_links to hello_world.egg-info/dependency_links.txt
writing top-level names to hello_world.egg-info/top_level.txt
reading manifest file 'hello_world.egg-info/SOURCES.txt'
writing manifest file 'hello_world.egg-info/SOURCES.txt'