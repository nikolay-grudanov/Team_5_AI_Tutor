---
source_image: page_408.png
page_number: 408
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.86
tokens: 7456
characters: 1742
timestamp: 2025-12-24T03:11:44.044616
finish_reason: stop
---

Развертывание функции на Python на самохостируемых FaaS-платформах

Как упоминалось ранее в этой главе, многие FaaS-платформы работают на кластерах Kubernetes. В числе преимуществ такого подхода следующее: развертываемые функции выполняются как обычные контейнеры Docker в Kubernetes, что позволяет применять обычный инструментарий Kubernetes, особенно для наблюдения (мониторинга, журналирования и трассировки). Еще одно потенциальное преимущество — экономия денег. Благодаря выполнению бессерверных функций в виде контейнеров в уже существующем кластере Kubernetes можно использовать имеющиеся ресурсы кластера, а не платить за каждый вызов функции, как было бы при развертывании функций на сторонней FaaS-платформе.

В этом разделе мы рассмотрим одну из таких платформ — OpenFaaS (https://www.openfaas.com). В число аналогичных FaaS-платформ, «под капотом» которых скрывается Kubernetes, входят, в частности:

• Kubeless (https://kubeless.io);
• Fn Project (https://fnproject.io) (технология, лежащая в основе FaaS-платформы от Oracle — Oracle Functions);
• Fission (https://fission.io);
• Apache OpenWhisk (https://openwhisk.apache.org).

Развертывание функции на Python в OpenFaaS

Для этого примера воспользуемся облегченным дистрибутивом Kubernetes от компании Rancher — k3s, чтобы продемонстрировать многообразие доступных в экосистеме Kubernetes средств.

Начнем с запуска утилиты k3sup (https://oreil.ly/qK0xJ) для выделения кластера Kubernetes k3s на EC2-инстансе под управлением Ubuntu.

Скачайте и установите k3sup:

$ curl -sLS https://get.k3sup.dev | sh
$ sudo cp k3sup-darwin /usr/local/bin/k3sup

Проверьте возможность подключения по SSH к удаленному EC2-инстансу:

$ ssh ubuntu@35.167.68.86 date
Sat Aug 24 21:38:57 UTC 2019