---
source_image: page_315.png
page_number: 315
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.11
tokens: 7568
characters: 1924
timestamp: 2025-12-24T03:09:17.875147
finish_reason: stop
---

Your new project is ready to go!
To perform an initial deployment, run the following commands:

1. virtualenv -p python3 venv
2. source venv/bin/activate
3. pip3 install -r requirements.txt

Then, run 'pulumi up'

Важно осознавать различия между проектом Pulumi и стеком Pulumi. Проект — это код, с помощью которого задается желаемое состояние системы, то есть ресурсы, которые Pulumi должен выделить. А стек — это конкретное развертывание проекта. Стек может соответствовать конкретной среде — разработки, предэксплуатационного тестирования или промышленной эксплуатации. В следующих примерах мы создадим два стека Pulumi: staging для среды предэксплуатационного тестирования и prod для промышленной эксплуатации.

Вот файлы, входящие в шаблон aws-python, которые сгенерировала команда pulumi new:

$ ls -la
total 40
drwxr-xr-x   7 ggheo  staff  224 Jun 13 21:43 .
drwxr-xr-x  11 ggheo  staff  352 Jun 13 21:42 ..
-rw-------   1 ggheo  staff   12 Jun 13 21:43 .gitignore
-rw-r--r--   1 ggheo  staff   32 Jun 13 21:43 Pulumi.staging.yaml
-rw-------   1 ggheo  staff   77 Jun 13 21:43 Pulumi.yaml
-rw-------   1 ggheo  staff  184 Jun 13 21:43 __main__.py
-rw-------   1 ggheo  staff   34 Jun 13 21:43 requirements.txt

Следуем инструкциям, выведенным командой pulumi new, и устанавливаем virtualenv, после чего создаем новую среду virtualenv и устанавливаем указанные в файле requirements.txt библиотеки:

$ pip3 install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv) pip3 install -r requirements.txt

Прежде чем выделять с помощью команды pulumi up какие-либо ресурсы AWS, необходимо убедиться, что используется нужная учетная запись AWS. Один из вариантов указания нужной учетной записи AWS — задание переменной среды AWS_PROFILE в текущей командной оболочке. В нашем случае в локальном файле ~/.aws/credentials уже был настроен профиль AWS gheorghiu-net.

(venv) export AWS_PROFILE=gheorghiu-net