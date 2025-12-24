---
source_image: page_837.png
page_number: 837
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.93
tokens: 7558
characters: 2145
timestamp: 2025-12-24T05:08:49.931156
finish_reason: stop
---

● Необходимо установить команду kubectl (используется для доступа к кластеру и работы с ним) и саму виртуальную машину Minikube.

Чтобы получить инструкцию по установке для систем Linux, macOS и Windows, перейдите на страницу kubernetes.io/docs/tasks/tools/install-minikube.

Вы можете установить Minikube от имени суперпользователя, но позже его нужно будет запустить из обычной учетной записи пользователя. Установка Minikube в Fedora, RHEL, Ubuntu или другую систему Linux (обратитесь к справочной странице install-minikube, если что-либо в установке изменилось) выполняется так.

1. Установите пакет команды kubectl. Установите ту версию команды kubectl, которая соотносится с версией Kubernetes в вашей системе Minikube. Последние версии команд kubectl и minikube отслеживают обновления. Введите следующее (все в одной строке):

# curl -LO \
https://storage.googleapis.com/kubernetes-release/release/ `curl \ -s https://storage.googleapis.com/kubernetes-release/release/ stable.txt \ `/bin/linux/amd64/kubectl

2. Скопируйте kubectl в каталог bin. Скопируйте команду kubectl в доступный каталог bin и сделайте ее исполняемой, например:

# mkdir /usr/local/bin
# cp kubectl /usr/local/bin
# chmod 755 /usr/local/bin/kubectl

3. Настройте гипервизор. Настройте свою систему Linux как гипервизор. Для KVM выполните действия, описанные в подразделе «Настройка гипервизоров» в главе 27.

4. Загрузите команду minikube. Загрузите исполняемый файл minikube и введите следующее (в одной строке):

# curl -Lo minikube \
https://storage.googleapis.com/minikube/releases/latest/minikubelinux-amd64 \
&& chmod +x minikube

5. Установите Minikube. Введите следующее:

# install minikube /usr/local/bin/

6. Запустите Minikube. От имени обычного пользователя введите следующие команды для идентификации драйвера, если задействуете гипервизор KVM (если у вас другой гипервизор, см. страницу minikube.sigs.k8s.io/docs/reference/drivers):

$ minikube config set vm-driver kvm2
$ minikube start --vm-driver=kvm2

7. Начните использовать Minikube. Теперь можно начать применять Minikube, выполнив команды minikube и kubectl. Далее рассмотрим, как это сделать.