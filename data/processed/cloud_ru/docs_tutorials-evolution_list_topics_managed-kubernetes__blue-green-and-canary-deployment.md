---
source_image: docs_tutorials-evolution_list_topics_managed-kubernetes__blue-green-and-canary-deployment.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 179.55
tokens: 21694
characters: 18340
timestamp: 2025-12-24T05:54:38.650059
finish_reason: stop
---

### Продвинутые методики развертывания приложений Blue-Green и Canary в управляемом кластере Managed Kubernetes

#### Перед началом работы

1. Сгенерируйте ключевую пару и загрузите публичный ключ SSH в облако Cloud.ru Evolution.
2. Создайте виртуальную машину и установите Docker.
3. Соберите образ простого веб-приложения.
4. Создайте приватный реестр в Artifact Registry и загрузите образ приложения.
5. Создайте кластер Managed Kubernetes и подключите плагин Ingress Nginx.
6. Разверните Blue-приложение.
7. Реализуйте стратегию Blue-Green.
8. Реализуйте стратегию Canary

#### Продвинутые методики развертывания приложений Blue-Green и Canary в управляемом кластере Managed Kubernetes

С помощью этого руководства вы научитесь работать с продвинутыми стратегиями развертывания контейнерных приложений Blue-Green Deployment и Canary Deployment в управляемом кластере Managed Kubernetes на платформе Cloud.ru Evolution.

Blue-Green Deployment — это метод развертывания, использующий две идентичные среды: синюю — текущую и зеленую — новую. После пользователи работают с синей средой, а зеленой разворачивается и тестируется обновление. После проверки весь трафик мгновенно переключается на зеленую среду. Это позволяет обновлять приложение без простоев и быстро откатываться в случае проблем.

Canary Deployment — это стратегия постепенного развертывания, при которой новая версия приложения сначала выпускается для группы пользователей. Это позволяет протестировать работу обновления в реальных условиях с минимальным риском. Если канареечная, то новая версия показывает стабильность, развертывание постепенно расширяется на всех пользователей. Такой подход обеспечивает контроль над рисками и позволяет быстро откатить изменения при обнаружении проблем.

Вы будете использовать следующие сервисы:
• Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
• Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
• Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
• Docker — система контейнеризации.

Шаги:
1. Сгенерируйте ключевую пару и загрузите публичный ключ SSH в облако Cloud.ru Evolution.
2. Создайте виртуальную машину и установите Docker.
3. Соберите образ простого веб-приложения.
4. Создайте приватный реестр в Artifact Registry и загрузите в него образ приложения.
5. Создайте кластер Managed Kubernetes и подключите плагин Ingress Nginx.
6. Разверните Blue-приложение.
7. Реализуйте стратегию Blue-Green.
8. Реализуйте стратегию Canary.

#### Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Убедитесь, что у вас достаточно прав для создания реестра и загрузки артефактов в сервисе Artifact Registry.
3. Создайте группу безопасности с правами, разрешающими доступ по портам 8080 и 8081 для внешнего IP-адреса локальной машины. Узнайте адрес локальной машины через сервис https://www.myip.ru/.

1. Сгенерируйте ключевую пару и загрузите публичный ключ SSH в облако Cloud.ru Evolution
   1. Сгенерируйте ключевую пару SSH.
   2. Загрузите публичный ключ в облако Cloud.ru Evolution.

2. Создайте виртуальную машину и установите Docker
   1. Создайте виртуальную машину с параметрами:
      • Гарантированная доля vCPU — 10%.
      • vCPU, шт. — 2 .
      • RAM, ГБ — 4 .
      • Загрузочный диск → Размер, ГБ — 30 .
      • Сетевой интерфейс №1— Подсеть с публичным IP .
      • Группы безопасности — группа, созданная перед началом работы.
      • Авторизация пользователя — Метод аутентификации — Публичный ключ и Пароль .
   В списке виртуальных машин появится новая ВМ. Примерно через минуту ее статус должен измениться на «Запущена».
   2. Подключитесь к виртуальной машине через сертифицированную консоль.
   3. Установите Docker на ВМ. Для этого в серийной консоли выполните команды:

   ```
   sudo apt update -y
   sudo apt upgrade -y
   curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
   sudo usermod -aG docker $USER
   newgrp docker
   ```

   4. Чтобы проверить, что Docker установлен и работает корректно, выполните команду:

   ```
   docker version
   ```

3. Соберите образ простого веб-приложения
   1. На ВМ создайте каталог с рабочим проектом deploy-lab :

   ```
   mkdir ~/deploy-lab
   ```

   2. В этом каталоге создайте еще два: blue-app и green-app :

   ```
   mkdir ~/deploy-lab/blue-app
   mkdir ~/deploy-lab/green-app
   ```

   3. В каталоге blue-app создайте файл index.html :

   ```
   nano ~/deploy-lab/blue-app/index.html
   ```

   4. В index.html добавьте код:

   ```html
   <!DOCTYPE html>
   <html lang="ru">
   <head>
     <meta http-equiv="cache-control" content="no-cache">
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <style>
       body {
         margin: 0;
         display: flex;
         justify-content: center;
         align-items: center;
         height: 100vh;
         background-color: #e0f2f9;
         font-family: Arial, sans-serif;
       }
       .blue-square {
         width: 250px;
         height: 250px;
         background-color: #00bfff;
         border-radius: 10px;
         box-shadow: 20px rgba(0, 102, 255, 0.5);
         display: flex;
         justify-content: center;
         align-items: center;
         color: white;
         font-size: 18px;
         font-weight: bold;
         text-align: center;
       }
     </style>
   </head>
   <body>
     <div class="blue-square">
       Синяя версия 1.0<br>
       This is the stable version of the application.
     </div>
   </body>
   </html>
   ```

   5. Создайте dockerfile :

   ```
   nano ~/deploy-lab/blue-app/dockerfile
   ```

   6. В dockerfile добавьте код:

   ```
   FROM nginx:alpine
   COPY index.html /usr/share/nginx/html/index.html
   EXPOSE 80
   ```

   7. В каталоге green-app создайте файл index.html :

   ```
   nano ~/deploy-lab/green-app/index.html
   ```

   8. В index.html добавьте код:

   ```html
   <!DOCTYPE html>
   <html lang="ru">
   <head>
     <meta http-equiv="cache-control" content="no-cache">
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <style>
       body {
         margin: 0;
         padding: 0;
         display: flex;
         justify-content: center;
         align-items: center;
         height: 100vh;
         background-color: #e0f2f9;
         font-family: Arial, sans-serif;
       }
       .green-square {
         width: 250px;
         height: 250px;
         background-color: #00c6dc;
         border-radius: 10px;
         box-shadow: 20px rgba(0, 102, 255, 0.5);
         display: flex;
         justify-content: center;
         align-items: center;
         color: white;
         font-size: 18px;
         font-weight: bold;
         text-align: center;
       }
     </style>
   </head>
   <body>
     <div class="green-square">
       Новая версия 2.0<br>
       This is the new, updated version of the application!
     </div>
   </body>
   </html>
   ```

   9. Создайте dockerfile :

   ```
   nano ~/deploy-lab/green-app/dockerfile
   ```

   10. В dockerfile добавьте код:

   ```
   FROM nginx:alpine
   COPY index.html /usr/share/nginx/html/index.html
   EXPOSE 80
   ```

   11. Соберите образы приложения:

   ```
   docker build -t blue-app:1.0 -f /home/cuser/deploy-lab/blue-app/dockerfile ~/deploy-lab/blue-app/
   docker build -t green-app:2.0 -f /home/cuser/deploy-lab/green-app/dockerfile ~/deploy-lab/green-app/
   ```

   Где «cuser» — имя пользователя, которое указали при создании ВМ.

   12. Запустите контейнеры:

   ```
   docker run -d -p 8080:80 --name blue-container blue-app:1.0
   docker run -d -p 8081:80 --name green-container green-app:2.0
   ```

   В адресную строку браузера введите по очереди адреса:
   • http://<public-ip>:8080 — приложение «Синий квадрат»;
   • http://<public-ip>:8081 — приложение «Зеленый квадрат».

   Где «public-ip» — публичный IP-адрес, присвоенный ВМ при ее создании на шаге 2.

4. Создайте приватный реестр в Artifact Registry и загрузите образ приложения
   1. Создайте приватный реестр и авторизуйтесь в нем.
      Присвойте реестру название blue-green-canary-registry . Название реестра должно быть уникальным.
   2. Чтобы перегрузить ранее собранные образы и залить их в blue-green-canary-registry , выполните команды:

   ```
   docker tag blue-app:1.0 blue-green-canary-registry.cr.cloud.ru/blue-app:1.0
   docker tag green-app:2.0 blue-green-canary-registry.cr.cloud.ru/green-app:2.0
   docker push blue-green-canary-registry.cr.cloud.ru/blue-app:1.0
   docker push blue-green-canary-registry.cr.cloud.ru/green-app:2.0
   ```

   В результате этой операции образы blue-app и green-app появятся в Artifact Registry.

   ![Screenshot of Artifact Registry showing blue-app and green-app images](https://cloud.ru/screenshot/artifact-registry.png)

5. Создайте кластер Managed Kubernetes и подключите плагин Ingress Nginx
   1. Создайте кластер Managed Kubernetes.
      Кластер необходимо создавать в той же VPC, что и ВМ. Остальные параметры можно оставить по умолчанию.
      При создании группы узлов укажите следующие параметры:
      • Гарантированная доля vCPU, % — 30 .
      • CPU, шт. — 2 .
      • RAM, ГБ — 4 .
      • Объем хранилища — 30 .
      • Количество узлов — 2 .
      Создание кластера занимает примерно пять минут.
   2. В кластере установите Ingress Nginx.
   3. Подключитесь к кластеру с ВМ.

6. Разверните Blue-приложение
   1. В каталоге deploy-lab создайте YAML-манифест deploy-myapp-blue-v1.yaml :

   ```
   cd ~/deploy-lab
   nano deploy-myapp-blue-v1.yaml
   ```

   2. Скопируйте в deploy-myapp-blue-v1.yaml код манифеста:

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: blue-app
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: demo-app
     template:
       metadata:
         labels:
           app: demo-app
         spec:
           containers:
             - name: web
               image: blue-green-canary-registry.cr.cloud.ru/blue-app:1.0
               ports:
                 - containerPort: 80
   ```

   Где blue-green-canary-registry.cr.cloud.ru/blue-app:1.0 — путь до образа, который был загружен в Artifact Registry.

   3. В этом же каталоге создайте файл svc-myapp-blue.yaml :

   ```
   nano svc-myapp-blue.yaml
   ```

   4. Скопируйте в файл svc-myapp-blue.yaml код манифеста:

   ```yaml
   # service myapp-blue, которое будет перенаправлять трафик на синюю версию Blue (v1)
   apiVersion: networking.k8s.io/v1
   kind: Service
   metadata:
     name: blue-app-ingress
   annotations:
     nginx.ingress.kubernetes.io/rewrite-target: /
   spec:
     ingressClassName: nginx
     rules:
     - http:
         pathType: Prefix
         backend:
           service:
             name: blue-app-service
             port:
               number: 80
   ```

   5. В этом же каталоге создайте файл ingress-myapp.yaml с содержимым:

   ```yaml
   # ingress myapp-blue, которое будет перенаправлять трафик на синюю версию Blue (v1)
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: demo-app-ingress
   annotations:
     nginx.ingress.kubernetes.io/rewrite-target: /
   spec:
     ingressClassName: nginx
     rules:
     - http:
         pathType: Prefix
         backend:
           service:
             name: blue-app-service
             port:
               number: 80
   ```

   6. Чтобы создать ресурсы Kubernetes, выполните команды:

   ```
   kubectl apply -f deploy-myapp-blue-v1.yaml
   kubectl apply -f svc-myapp-blue.yaml
   kubectl apply -f ingress-myapp.yaml
   ```

   7. Проверьте создание ресурсов:

   ```
   kubectl get svc,pods,ingress
   ```

   На этом шаге мы организовали подачу трафика на стабильную версию приложения demo-app извне через Ingress-контроллер.

   Чтобы проверить работоспособность приложения, определите внешний IP Ingress-контроллера. Для этого используйте команду:

   ```
   kubectl get svc -n ingress
   ```

   В результате вы увидите информацию по External IP:

   NAME                TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)
   ingress-nginx-controller   LoadBalancer   10.104.209.33   xx.xxx.xxx.xx   80:30522/TCP,443:30796,

   Введите в браузере http://EXTERNAL-IP> и увидите отображаемую версию приложения.

   ![Screenshot of browser showing blue square](https://cloud.ru/screenshot/blue-square.png)

7. Реализуйте стратегию Blue-Green
   1. В каталоге deploy-lab создайте YAML-манифест Green-приложения:

   ```
   nano deploy-myapp-green-v2.yaml
   ```

   2. Скопируйте в deploy-myapp-green-v2.yaml код манифеста:

   ```yaml
   # сервис приложения на котором будет перенаправлен трафик синей версии Blue (v1) и зеленой версии Green (v2)
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: green-app
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: demo-app
     template:
       metadata:
         labels:
           app: demo-app
         spec:
           containers:
             - name: web
               image: blue-green-canary-registry.cr.cloud.ru/green-app:2.0
               ports:
                 - containerPort: 80
   ```

   3. В каталоге deploy-lab создайте файл svc-myapp-green.yaml :

   ```
   nano svc-myapp-green.yaml
   ```

   4. Скопируйте в файл svc-myapp-green.yaml код манифеста:

   ```yaml
   # сервис myapp-green, которое будет перенаправлять трафик на зеленую версию Green (v2)
   apiVersion: networking.k8s.io/v1
   kind: Service
   metadata:
     name: green-app-ingress
   annotations:
     nginx.ingress.kubernetes.io/rewrite-target: /
   spec:
     ingressClassName: nginx
     rules:
     - http:
         pathType: Prefix
         backend:
           service:
             name: green-app-service
             port:
               number: 80
   ```

   5. В этом же каталоге создайте файл ingress-myapp.yaml :

   ```
   nano ingress-myapp.yaml
   ```

   6. Скопируйте в ingress-myapp.yaml код манифеста:

   ```yaml
   # ingress myapp-green, которое будет перенаправлять трафик между основной и канарейской развертками
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: demo-app-ingress
   annotations:
     nginx.ingress.kubernetes.io/rewrite-target: /
   spec:
     ingressClassName: nginx
     rules:
     - http:
         pathType: Prefix
         backend:
           service:
             name: green-app-service
             port:
               number: 80
   ```

   7. Чтобы создать ресурсы Kubernetes, выполните команды:

   ```
   kubectl apply -f deploy-myapp-green-v2.yaml
   kubectl apply -f svc-myapp-green.yaml
   kubectl apply -f ingress-myapp.yaml
   ```

   8. Примените внесенные изменения в манифесте:

   ```
   kubectl apply -f ingress-myapp.yaml
   ```

   Теперь трафик идет на сборку приложения Green (v2).

   9. Чтобы проверить изменения, обновите окно браузера, где раньше отображалось приложение с синим квадратом. Теперь отображается зеленый квадрат.

   Таким образом, мы осуществили переключение с одной версии приложения Blue (v1) на другую Green (v2). В этом и заключается стратегия развертывания Blue-Green.

8. Реализуйте стратегию Canary
   1. На ВМ каталоге deploy-lab создайте файл deploy-canary.yaml с тем же образом, что и версия Green v2 — blue-green-canary-registry.cr.cloud.ru/green-app:2.0 :

   ```
   cd ~/deploy-lab
   nano deploy-canary.yaml
   ```

   2. Скопируйте в deploy-canary.yaml код манифеста:

   ```yaml
   # сервис приложения на котором будет перенаправлен трафик синей версии Blue (v1) и зеленой версии Green (v2)
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: canary-app
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: demo-app
     template:
       metadata:
         labels:
           app: demo-app
         spec:
           containers:
             - name: web
               image: blue-green-canary-registry.cr.cloud.ru/green-app:2.0
               ports:
                 - containerPort: 80
   ```

   3. В каталоге deploy-lab создайте файл svc-canary.yaml :

   ```
   nano svc-canary.yaml
   ```

   4. Скопируйте в файл svc-canary.yaml код манифеста:

   ```yaml
   # сервис myapp-canary, которое будет перенаправлять трафик между основной и канарейской развертками
   apiVersion: networking.k8s.io/v1
   kind: Service
   metadata:
     name: canary-app-ingress
   annotations:
     nginx.ingress.kubernetes.io/rewrite-target: /
   spec:
     ingressClassName: nginx
     rules:
     - http:
         pathType: Prefix
         backend:
           service:
             name: canary-app-service
             port:
               number: 80
   ```

   5. В каталоге deploy-lab создайте файл ingress-canary.yaml :

   ```
   nano ingress-canary.yaml
   ```

   6. Скопируйте в ingress-canary.yaml код манифеста:

   ```yaml
   # ingress myapp-canary, которое будет перенаправлять трафик между основной и канарейской развертками
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: demo-app-ingress
   annotations:
     nginx.ingress.kubernetes.io/rewrite-target: /
   spec:
     ingressClassName: nginx
     rules:
     - http:
         pathType: Prefix
         backend:
           service:
             name: canary-app-service
             port:
               number: 80
   ```

   7. Чтобы создать ресурсы Kubernetes, выполните команды:

   ```
   kubectl apply -f deploy-canary.yaml
   kubectl apply -f svc-canary.yaml
   kubectl apply -f ingress-canary.yaml
   ```

   8. Примените изменения:

   ```
   kubectl apply -f ingress-canary.yaml
   ```

   Теперь при обновлении браузера мы видим только Canary-версию приложения.

   Таким образом, мы обновили нашу приложение, подавая начальную трафик одновременно на текущую версию приложения Blue и новую версию Canary. В итоге мы перенесли 100% трафика на приложение Canary, тем самым реализовав стратегию развертывания Canary.

   Результат
   Вы научились работать с продвинутыми стратегиями развертывания контейнерных приложений Blue-Green и Canary. Эти методы позволяют обновлять приложения более управляемо и безопасно, сводя к минимуму простои и риски, связанные с внедрением новых версий.