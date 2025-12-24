---
source_image: page_375.png
page_number: 375
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.54
tokens: 7331
characters: 1621
timestamp: 2025-12-24T03:10:40.367941
finish_reason: stop
---

Settings from your current configuration [default] are:
core:
    account: grig.gheorghiu@gmail.com
    disable_usage_reporting: 'True'
    project: pulumi-gke-testing

Pick configuration to use:
[1] Re-initialize this configuration [default] with new settings
[2] Create a new configuration
Please enter your numeric choice: 2

Enter configuration name. Names start with a lower case letter and contain only lower case letters a-z, digits 0-9, and hyphens '-':
pythonfordevops-gke-pulumi
Your current configuration has been set to: [pythonfordevops-gke-pulumi]

Pick cloud project to use:
[1] pulumi-gke-testing
[2] Create a new project
Please enter numeric choice or text value (must exactly match list item): 2

Enter a Project ID. pythonfordevops-gke-pulumi
Your current project has been set to: [pythonfordevops-gke-pulumi].

Войдите в учетную запись GCP:

$ gcloud auth login

Войдите в приложение по умолчанию — pythonfordevops-gke-pulumi:

$ gcloud auth application-default login

Создайте новый проект Pulumi с помощью команды pulumi new, указав в качестве шаблона gcp-python, а в качестве названия проекта — pythonfordevops-gke-pulumi:

$ pulumi new
Please choose a template: gcp-python
A minimal Google Cloud Python Pulumi program
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (pulumi_gke_py) pythonfordevops-gke-pulumi
project description: (A minimal Google Cloud Python Pulumi program)
Created project 'pythonfordevops-gke-pulumi'

stack name: (dev)
Created stack 'dev'