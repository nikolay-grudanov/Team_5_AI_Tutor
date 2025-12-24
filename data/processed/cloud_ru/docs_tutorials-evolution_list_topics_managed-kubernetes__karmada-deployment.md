---
source_image: docs_tutorials-evolution_list_topics_managed-kubernetes__karmada-deployment.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 155.77
tokens: 17697
characters: 13267
timestamp: 2025-12-24T05:56:16.975534
finish_reason: stop
---

<h2>Развертывание мультикластера Managed Kubernetes с помощью Karmada</h2>
<p>С помощью этого руководства вы развернете мультикластерное окружение на базе Managed Kubernetes при помощи платформы Karmada. Вы научитесь создавать и конфигурировать кластеры Kubernetes, управлять доступом и интегрировать несколько кластеров через централизованную платформу. В результате вы получите рабочую мультикластерную инфраструктуру для одновременного и унифицированного управления приложениями в разных кластерах Kubernetes.</p>
<p>Вы будете использовать следующие сервисы:</p>
<ul>
<li><b>Managed Kubernetes</b> — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.</li>
<li><b>Виртуальные машины</b> — сервис, в рамках которого предоставляется виртуальная машина для подключения и администрирования кластеров Kubernetes.</li>
<li><b>Karmada</b> — Kubernetes-совместимая платформа для централизованного управления и оркестрации приложений в мультикластерной инфраструктуре.</li>
</ul>
<p>Шаги:</p>
<ol>
<li>Сгенерируйте ключи доступа для интеграции</li>
<li>Создайте необходимые сети, NAT и виртуальную машину</li>
<li>Подготовьте окружение виртуальной машины</li>
<li>Создайте и настройте кластеры Evolution Managed Kubernetes</li>
<li>Настройте подключение к кластерам Kubernetes</li>
<li>Настройте внешний балансировщик нагрузки для Karmada</li>
<li>Установите Karmada и интегрируйте кластеры-участники</li>
</ol>
<h3>Перед началом работы</h3>
<p>Зарегистрируйтесь в личном кабинете Cloud.ru.</p>
<p>Если вы уже зарегистрированы, войдите под своей учетной записью.</p>
<h4>1. Сгенерируйте ключи доступа для интеграции</h4>
<p>Получите ключи для программного доступа к ресурсам облака Cloud.ru, которые понадобятся для интеграции с Managed Kubernetes.</p>
<ol>
<li>Сгенерируйте ключи доступа (Key ID и Key Secret) для вашего аккаунта по инструкции.</li>
<li>Сохраните значения Key ID и Key Secret в безопасном месте.</li>
</ol>
<h4>2. Разверните ресурсы в облаке</h4>
<p>На этом шаге вы подготовите подсети, NAT-шлюз и виртуальную машину, которая будет использоваться для управления кластерами.</p>
<ol>
<li>Создайте три отдельные подсети в одной зоне доступности (например, AZ2) для размещения кластеров Managed Kubernetes.</li>
<li>Создайте NAT-шлюз (SNAT) в этой же зоне.</li>
<li>Создайте виртуальную машину с подсетью и публичным IP.</li>
</ol>
<h4>3. Подготовьте окружение виртуальной машины</h4>
<p>На этом шаге вы настроите окружение для последующей работы с кластерами Kubernetes.</p>
<ol>
<li>Подключитесь к виртуальной машине по SSH, используя соответствующий клиент.</li>
<li>Установите на виртуальной машине необходимые инструменты для работы с Managed Kubernetes:
<ul>
<li>Установите kubectl.</li>
<li>Установите cloudlogin.</li>
</ul>
</li>
<li>Установите Git и клонируйте репозиторий Karmada:
<ul>
<li>Установите Git (команда приведена для ОС на базе Ubuntu/Debian):</li>
</ul>
<pre>sudo apt update &amp;&amp; sudo apt install -y git</pre>
<ul>
<li>Клонируйте официальный репозиторий Karmada:</li>
</ul>
<pre>git clone https://github.com/karmada-io/karmada.git</pre>
</li>
<li>Установите Go версии 1.24.6:</li>
</ol>
<div class="note">
<b>Примечание</b>
<p>Проверьте версию Go в файле go.mod репозитория karmada.</p>
</div>
<ol start="4">
<li>Загрузите и установите Go:</li>
</ol>
<pre>curl -fsSL go1.24.6.linux-amd64.tar.gz https://go.dev/dl/go1.24.6.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.24.6.linux-amd64.tar.gz
echo 'export GOPATH=$HOME/go' &gt;&gt; ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' &gt;&gt; ~/.bashrc
source ~/.bashrc</pre>
<ol start="5">
<li>Проверьте корректность установки:</li>
</ol>
<pre>go version</pre>
<ol start="6">
<li>Установите Docker:</li>
</ol>
<pre>curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker</pre>
<h4>4. Создайте и настройте кластеры Managed Kubernetes</h4>
<p>На этом шаге вы создадите основной кластер для control plane Karmada и два кластера-участника.</p>
<ol>
<li>Создайте три кластера в сервисе Managed Kubernetes: основной (control plane) и два кластера-участника. Для каждого выберите ранее созданные подсети и разместите их в одной VPC.
<ul>
<li>Основной кластер:
<ul>
<li>Имя: mk8s-karmada-control-plane</li>
<li>Число мастер-узлов: 1</li>
<li>Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM</li>
<li>Публичный IP: включен</li>
<li>Под сеть сервисов: 10.101.0.0/16</li>
<li>Под сеть подов: 10.102.0.0/16</li>
<li>Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM</li>
<li>Количество узлов: 3</li>
</ul>
</li>
<li>Кластер-участник 1:
<ul>
<li>Имя: mk8s-evo1</li>
<li>Число мастер-узлов: 1</li>
<li>Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM</li>
<li>Публичный IP: включен</li>
<li>Под сеть сервисов: 10.111.0.0/16</li>
<li>Под сеть подов: 10.112.0.0/16</li>
<li>Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM</li>
<li>Количество узлов: 3</li>
</ul>
</li>
<li>Кластер-участник 2:
<ul>
<li>Имя: mk8s-evo2</li>
<li>Число мастер-узлов: 1</li>
<li>Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM</li>
<li>Публичный IP: включен</li>
<li>Под сеть сервисов: 10.121.0.0/16</li>
<li>Под сеть подов: 10.122.0.0/16</li>
<li>Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM</li>
<li>Количество узлов: 3</li>
</ul>
</li>
</ul>
</li>
<li>Дождитесь окончания создания кластеров. Убедитесь, что в личном кабинете статус всех кластеров — «Запущено».</li>
</ol>
<h4>5. Настройте подключение к кластерам Kubernetes</h4>
<p>На этом шаге вы обеспечите конфигурирование доступа к каждому кластеру с управляющей виртуальной машины.</p>
<ol>
<li>Скачайте файлы kubeconfig для всех кластеров в личном кабинете.</li>
<li>Создайте директорию .kube, которая будет использоваться по умолчанию для основного кластера:</li>
</ol>
<pre>mkdir -p $HOME/.kube</pre>
<ol start="3">
<li>Создайте директорию для конфигураций кластеров-участников:</li>
</ol>
<pre>mkdir -p $HOME/join-clusters</pre>
<ol start="4">
<li>Сохраните файлы kubeconfig по следующим путям:
<ul>
<li>mk8s-karmada-control-plane: $HOME/.kube/config (по умолчанию)</li>
<li>mk8s-evo1: $HOME/join-clusters/evo1</li>
<li>mk8s-evo2: $HOME/join-clusters/evo2</li>
</ul>
</li>
<li>Задайте значения <KEY_ID> и <KEY_SECRET> для параметров CLOUDRU_KEY_ID и CLOUDRU_SECRET_ID с помощью команды:</li>
</ol>
<pre>sed -i \
-e '/name: CLOUDRU_KEY_ID/ in; s/value: ""/value: "<KEY_ID>"/i' \
-e '/name: CLOUDRU_SECRET_ID/ in; s/value: ""/value: "<KEY_SECRET>"/i' \
$HOME/.kube/config \
$HOME/join-clusters/evo1 \
$HOME/join-clusters/evo2</pre>
<p>Где:</p>
<ul>
<li>&lt;KEY_ID&gt; — сгенерированный ранее Key ID.</li>
<li>&lt;KEY_SECRET&gt; — сгенерированный ранее Key Secret.</li>
</ul>
<ol start="6">
<li>Проверьте доступ к кластерам Kubernetes:</li>
</ol>
<pre>kubectl cluster-info
kubectl --kubeconfig=$HOME/join-clusters/evo1 cluster-info
kubectl --kubeconfig=$HOME/join-clusters/evo2 cluster-info</pre>
<p>Убедитесь, что каждая команда возвращает информацию о кластере без ошибок аутентификации.</p>
<h4>6. Настройте внешний балансировщик нагрузки для Karmada</h4>
<p>На этом шаге вы создадите внешний балансировщик, чтобы организовать доступ к API-серверу Karmada через сервис Load Balancer.</p>
<p>Мы будем устанавливать Karmada на кластер mk8s-karmada-control-plane с помощью скрипта установки из репозитория Karmada. При установке необходимо указать каким образом мы будем обращаться к API-серверу Karmada:</p>
<ul>
<li>через HostNetwork — отправка обращений на порт tcp/5443 непосредственно узла, на котором будет запущен под karmada-apiserver;</li>
<li>через LoadBalancer — отправка обращений к API-серверу через балансировщик нагрузки. Балансировщик нагрузки слушает порт tcp/5443 и переадресует наши запросы поду karmada-apiserver.</li>
</ul>
<p>В этом сценарии мы будем обращаться к API-серверу через LoadBalancer.</p>
<p>Важно учесть, что скрипт установки сначала генерирует все необходимые сертификаты, а затем создает все необходимые ресурсы, в том числе сервис LoadBalancer. Скрипт создает сертификаты для серверных компонентов с опцией SAN. Поскольку скрипт в начале не может знать IP-адрес балансировщика нагрузки, т.к. он еще не создан, то он не добавляет этот IP-адрес как альтернативное имя субъекта. Из-за этого вы не сможете подключиться к API-серверу через балансировщик нагрузки. Чтобы выйти из ситуации, вы можете перезапустить сертификаты после установки, но этот путь довольно ресурсозатратный.</p>
<p>Также вы можете, узнав IP-адрес балансировщика, переустановить Karmada. В этом случае вы не застрахованы, что IP-адрес балансировщика будет другим. Мы предлагаем создать заранее namespace karmada-system и сервис типа LoadBalancer. Когда вы создадите балансировщик нагрузки в кластере Kubernetes, платформа автоматически создаст балансировщик нагрузки в сервисе Evolution Load Balancer с параметрами сервиса Kubernetes.</p>
<ol>
<li>Создайте папку karmada-manifests :</li>
</ol>
<pre>mkdir $HOME/karmada-manifests</pre>
<ol start="2">
<li>Создайте там файл karmada.yaml и скопируйте следующий манифест:</li>
</ol>
<pre>apiVersion: v1
kind: Namespace
metadata:
  labels:
    kubernetes.io/metadata.name: karmada-system
---
apiVersion: v1
kind: Service
metadata:
  name: karmada-apiserver
  labels:
    app: karmada-apiserver
  annotations:
    loadbalancer.mk8s.cloud.ru/type: "external"
    loadbalancer.mk8s.cloud.ru/health-check-interval-seconds: "3"
    loadbalancer.mk8s.cloud.ru/health-check-unhealthy-threshold-count: "4"
    loadbalancer.mk8s.cloud.ru/health-check-healthy-threshold-count: "4"
  namespace: karmada-system
spec:
  type: LoadBalancer
  selector:
    app: karmada-apiserver
  ports:
  - name: karmada-apiserver-kubelet
    port: 5443
    protocol: tcp
    targetPort: 5443</pre>
<ol start="3">
<li>Примените манифест к основному кластеру Kubernetes:</li>
</ol>
<pre>kubectl apply -f $HOME/karmada-manifests/karmada.yaml</pre>
<ol start="4">
<li>Убедитесь, что сервис создан:</li>
</ol>
<pre>kubectl -n karmada-system get svc karmada-apiserver</pre>
<p>Проверьте, что сервис отображается, статус внешнего IP — <pending>. Это означает, что Evolution Load Balancer создает ресурс и назначает публичный IP. Подождите около 8-10 минут, пока балансировщик нагрузки получит внешний IP-адрес и закончит настройку.</p>
<h4>7. Установите Karmada и интегрируйте кластеры-участники</h4>
<p>На этом шаге вы установите Karmada на основной кластер, учитывая внешний IP-адрес балансировщика, и подключите оба кластера-участника.</p>
<ol>
<li>После назначения публичного IP для балансировщика получите этот IP-адрес:</li>
</ol>
<pre>kubectl -n karmada-system get svc karmada-apiserver -o jsonpath="{range .status.loadBalancer.ingress[0].ip} {end}"</pre>
<ol start="2">
<li>Скопируйте полученный IP и вставьте его в установочный скрипт deploy-karmada.sh для корректной генерации сертификатов:</li>
</ol>
<pre>sed -i "s/KARMADA_APISERVER_IP=\"<IP_BALANCER>\" \"$HOME/karmada/hack/deploy-karmada.sh
sed -i "karmada_apiserver_alt_names=("$karmada-apiserver,karmada-system,svc.cluster.local" "$karmada-ap
sed -i "HOST_CLUSTER_NAME=$HOST_CLUSTER_NAME-$karmada-host"/HOST_CLUSTER_NAME=$HOST_CLUSTER_NAME</pre>
<p>Где:</p>
<ul>
<li>&lt;IP_BALANCER&gt; — публичный IP-адрес балансировщика нагрузки.</li>
</ul>
<ol start="3">
<li>Установите переменную окружения, чтобы скрипт использовал сервис Load Balancer:</li>
</ol>
<pre>export LOAD_BALANCER=true</pre>
<ol start="4">
<li>Запустите установку Karmada на кластер mk8s-karmada-control-plane:</li>
</ol>
<pre>$HOME/karmada/hack/remote-up-karmada.sh $HOME/.kube/config <K8S_KARMADA_CONTEXT_NAME></pre>
<p>Где:</p>
<ul>
<li>&lt;K8S_KARMADA_CONTEXT_NAME&gt; — имя контекста кластера из файла конфигурации.</li>
</ul>
<ol start="5">
<li>Проверьте, что все компоненты Karmada развернуты корректно:</li>
</ol>
<pre>kubectl get pods -n karmada-system
kubectl get services -n karmada-system</pre>
<ol start="6">
<li>Установите инструмент CLI karmadactl:</li>
</ol>
<ul>
<li>Скачайте и установите утилиту:</li>
</ul>
<pre>curl -s https://raw.githubusercontent.com/karmada-io/karmada/master/hack/install-cli.sh | sudo bash</pre>
<ul>
<li>Проверьте, что karmadactl успешно установлено:</li>
</ul>
<pre>karmadactl version</pre>
<ol start="7">
<li>Подключите оба кластера-участника к Karmada:
<ul>
<li>Для кластера mk8s-evo1 выполните команду:</li>
</ul>
<pre>karmadactl join evo1 --karmada-context karmada-apiserver --cluster-kubeconfig $HOME/join-clusters/evo1</pre>
<ul>
<li>Для кластера mk8s-evo2 выполните команду:</li>
</ul>
<pre>karmadactl join evo2 --karmada-context karmada-apiserver --cluster-kubeconfig $HOME/join-clusters/evo2</pre>
</li>
<li>Проверьте, что оба кластера успешно добавлены и отображаются со статусом «Ready»:</li>
</ol>
<pre>karmadactl --karmada-context karmada-apiserver get clusters</pre>
<p>В консоли должны отобразиться оба кластера: evo1 и evo2, статус — «Ready».</p>
<h3>Результат</h3>
<p>Вы развернули мультикластерную инфраструктуру Evolution Managed Kubernetes, подготовили внешний балансировщик нагрузки и добавили кластеры-участники control plane Karmada. Теперь вы можете централизованно управлять приложениями в распределенной среде Kubernetes, расширять масштабируемость и надежность ваших сервисов.</p>