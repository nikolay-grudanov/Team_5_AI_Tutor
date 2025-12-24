---
source_image: page_398.png
page_number: 398
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.57
tokens: 7320
characters: 1559
timestamp: 2025-12-24T03:11:14.481582
finish_reason: stop
---

Инициализируем локальную среду gcloud:

$ gcloud init
Welcome! This command will take you through the configuration of gcloud.

Settings from your current configuration [pythonfordevops-gke-pulumi] are:
compute:
  region: us-west1
  zone: us-west1-c
core:
  account: grig.gheorghiu@gmail.com
  disable_usage_reporting: 'True'
  project: pythonfordevops-gke-pulumi

Pick configuration to use:
[1] Re-initialize this configuration with new settings
[2] Create a new configuration
[3] Switch to and re-initialize existing configuration: [default]
Please enter your numeric choice: 2

Enter configuration name. Names start with a lower case letter and contain only lower case letters a-z, digits 0-9, and hyphens '-':
pythonfordevops-cloudfunction
Your current configuration has been set to: [pythonfordevops-cloudfunction]

Choose the account you would like to use to perform operations for this configuration:
[1] grig.gheorghiu@gmail.com
[2] Log in with a new account
Please enter your numeric choice: 1

You are logged in as: [grig.gheorghiu@gmail.com].
Pick cloud project to use:
[1] pulumi-gke-testing
[2] pythonfordevops-cloudfunction
[3] pythonfordevops-gke-pulumi
[4] Create a new project
Please enter numeric choice or text value (must exactly match list item): 2
Your current project has been set to: [pythonfordevops-cloudfunction].

Авторизация локальной командной оболочки в GCP:

$ gcloud auth login

Развертываем с помощью фреймворка Serverless ту же конечную точку HTTP Python, что и примере с AWS Lambda, но на этот раз как функцию Google Cloud: