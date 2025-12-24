---
source_image: page_360.png
page_number: 360
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.69
tokens: 7478
characters: 1917
timestamp: 2025-12-24T03:10:22.018713
finish_reason: stop
---

Основная команда для взаимодействия с Kubernetes — kubectl.

Установите kubectl на машине под управлением macOS, скачав его со страницы загрузок (https://oreil.ly/f9Wv0), а затем переместите в /usr/local/bin/minikube и сделайте исполняемым.

Одно из главных понятий при работе с kubectl — контекст, то есть кластер Kubernetes, с которым вы хотите работать. В процессе установки minikube уже был создан контекст minikube. Указать kubectl, какой контекст использовать, можно с помощью следующей команды:

$ kubectl config use-context minikube
Switched to context "minikube".

Другой, более удобный способ — установить утилиту kubectx из репозитория Git (https://oreil.ly/SIf1U), а затем выполнить:

$ kubectx minikube
Switched to context "minikube".

Еще одна удобная клиентская утилита для работы с Kubernetes — kube-ps1 (https://oreil.ly/AcE32). Если вы работаете под macOS, используя Zsh, добавьте в файл ~/.zshrc следующий фрагмент кода:

source "/usr/local/opt/kube-ps1/share/kube-ps1.sh"
PS1='$(kube_ps1)'$PS1

Эти команды меняют приглашение командной строки так, чтобы отображать текущий контекст и пространство имен Kubernetes. В ходе работы с несколькими кластерами Kubernetes это настоящая палочка-выручалочка, позволяющая легко различать кластеры предэксплуатационного тестирования и промышленной эксплуатации.

Теперь можно выполнять команды kubectl для локального кластера minikube. Например, команда kubectl get nodes выводит список узлов, входящий в этот кластер. В данном случае узел только один, с ролью master:

$ kubectl get nodes
NAME      STATUS   ROLES    AGE     VERSION
minikube  Ready    master   2m14s   v1.15.0

Начнем с формирования объекта PVC (Persistent Volume Claim — заявка на том постоянного хранения) из созданного Kompose файла dbdata-persistentvolumeclaim.yaml, соответствующего при запуске с помощью docker-compose выделенному для контейнера базы данных PostgreSQL локальному тому: