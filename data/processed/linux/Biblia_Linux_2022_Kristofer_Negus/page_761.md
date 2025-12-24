---
source_image: page_761.png
page_number: 761
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.08
tokens: 7561
characters: 1894
timestamp: 2025-12-24T05:06:45.136286
finish_reason: stop
---

Теперь можно применять команды podman или docker для работы с контейнерами и образами контейнеров для проработки примеров этой главы.

Загрузка и запуск контейнеров

Установив и подготовив к использованию пакеты docker или podman, вы можете попробовать запустить контейнер. Для начала перетащите контейнер в свою локальную систему и запустите его. При желании можете пропустить команду pull, так как запуск контейнера приведет к ошибке, если запрошенного образа еще нет в вашей системе.

Загрузка контейнера

Выберите надежный образ контейнера для тестирования из официального источника, актуального и желательно проверенного на наличие уязвимостей. Вот пример загрузки базового образа RHEL 8 UBI с помощью команды podman (в этих примерах можно заменить команду podman на docker):

# podman pull registry.access.redhat.com/ubi8/ubi
Trying to pull .../ubi8/ubi...Getting image source signatures
Copying blob fd8daf2668d1 done
Copying blob cb3c77f9bdd8 done
Copying config 096cae65a2 done
Writing manifest to image destination
Storing signatures
096cae65a2078ff26b3a2f82b28685b6091e4e2823809d45aef68aa2316300c7

Чтобы убедиться, что образ находится в вашей системе, выполните следующие действия:

# podman images
REPOSITORY    TAG    IMAGE ID    CREATED    SIZE
/ubi8/ubi    latest    096cae65a207    2 weeks ago    239 M

Запуск командной оболочки из контейнера

Используйте команды podman или docker для запуска оболочки внутри контейнера. Можно идентифицировать образ либо по его идентификатору (096cae65a207), либо по имени (registry.access.redhat.com/ubi8/ubi). Задействуйте параметры -i (interactive) и -t (terminal), чтобы подключить интерактивный сеанс внутри контейнера из оболочки bash:

# podman run -it 096cae65a207 bash
[root@e9086da6ed70 /]#

При запущенной оболочке команды, которые вы вводите, будут работать в контейнере. Например, вы перечисляете файловую систему контейнера или