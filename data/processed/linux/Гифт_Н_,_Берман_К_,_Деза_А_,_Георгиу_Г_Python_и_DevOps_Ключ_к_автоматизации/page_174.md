---
source_image: page_174.png
page_number: 174
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.33
tokens: 7350
characters: 1607
timestamp: 2025-12-24T03:05:26.165567
finish_reason: stop
---

Создание пакетов RPM

Как и при создании пакетов Debian, в ходе работы с RPM уже должна быть подготовлена возможность генерации нативного пакета Python с помощью файла setup.py. Однако, в отличие от Debian, где требовалось много файлов, создание пакетов RPM требует всего одного файла — spec. Система управления пакетами RPM (известная ранее как система управления пакетами Red Hat) прекрасно подойдет для этой цели, если роль целевого дистрибутива Linux играет CentOS или Fedora.

Файл spec

В простейшем варианте файла spec (в этом примере он называется hello-world.spec) ничего сложного нет, большинство разделов его говорят сами за себя. Его можно даже сгенерировать с помощью setuptools:

$ python3 setup.py bdist_rpm --spec-only
running bdist_rpm
running egg_info
writing hello_world.egg-info/PKG-INFO
writing dependency_links to hello_world.egg-info/dependency_links.txt
writing top-level names to hello_world.egg-info/top_level.txt
reading manifest file 'hello_world.egg-info/SOURCES.txt'
writing manifest file 'hello_world.egg-info/SOURCES.txt'
writing 'dist/hello-world.spec'

Полученный в результате файл dist/hello-world.spec будет выглядеть примерно так:

%define name hello-world
%define version 0.0.1
%define unmangled_version 0.0.1
%define release 1

Summary: A hello-world example package
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Example Author <author@example.com>
Url: example.com