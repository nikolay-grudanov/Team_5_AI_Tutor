---
source_image: page_917.png
page_number: 917
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.96
tokens: 7440
characters: 1687
timestamp: 2025-12-24T05:10:47.249579
finish_reason: stop
---

7. Используйте команду docker или podman, чтобы построить образ containerworks из только что созданного файла Dockerfile:

# podman build -t myproject .

или

# docker build -t myproject .

8. Получить доступ к реестру контейнеров можно, либо установив пакет docker для дистрибутива:

# yum install docker-distribution -y
# systemctl start docker-distribution
# systemctl enable docker-distribution

либо получив учетную запись в реестре Quay.IO (quay.io/plans/) или хабе Docker (Docker Hub):

# podman login quay.io
Username: <username>
Password: **********

9. Чтобы пометить новое изображение и поместить его в выбранный реестр контейнеров, выполните следующие команды:

# podman tag aa0274872f23 \
quay.io/<user>/<imagename>:v1.0
# podman push \
quay.io/<user>/<imagename>:v1.0

Глава 27. Облачные вычисления в системе Linux

1. Чтобы проверить, поддерживает ли ваш компьютер виртуализацию KVM, введите следующую команду:

# cat /proc/cpuinfo | grep --color -E "vmx|svm|lm"
flags : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good xtopology nonstop_tsc aperfmprefr pni pclmulqdq dtes64 monitor ds_cpl vmx smx es...

Процессор должен поддерживать VMX или SVM. Lm указывает на то, что это 64-разрядный компьютер.

2. Чтобы установить систему Linux вместе с пакетами, необходимыми для использования ее в качестве хоста KVM, и запустить приложение Virtual Machine Manager, выполните следующие действия:
а) загрузите «живой» или установочный образ с сайта Linux (например, getfedora.org) и запишите его на DVD (или иным образом установите его);