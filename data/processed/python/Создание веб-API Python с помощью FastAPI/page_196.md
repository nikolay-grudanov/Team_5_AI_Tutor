---
source_image: page_196.png
page_number: 196
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.88
tokens: 8271
characters: 1006
timestamp: 2025-12-24T02:20:46.962207
finish_reason: stop
---

Результат выглядит следующим образом:

![Остановка экземпляров приложения](./images/9.5.png)

Рисунок 9.5 – Остановка экземпляров приложения

Развертывание Docker образов

В последнем разделе мы узнали, как создавать и развертывать образы Docker локально. Эти образы можно развернуть на любой виртуальной машине и на бессерверных платформах, таких как Google Cloud и AWS.

Обычный режим работы включает в себя отправку ваших образов Docker в частный реестр на бессерверной платформе. Процесс, связанный с развертыванием образов Docker на бессерверных платформах, варьируется от поставщика к поставщику, поэтому здесь приведены ссылки на избранных поставщиков бессерверных услуг:

• Google Cloud Run: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python
• Amazon EC2: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-ecs-ec2.html
• Развертывание в Microsoft Azure: https://docs.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-deploy-app