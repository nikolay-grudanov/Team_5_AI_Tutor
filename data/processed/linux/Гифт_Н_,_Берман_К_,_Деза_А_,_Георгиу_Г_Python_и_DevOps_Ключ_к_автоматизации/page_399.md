---
source_image: page_399.png
page_number: 399
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.62
tokens: 7297
characters: 1598
timestamp: 2025-12-24T03:11:19.233854
finish_reason: stop
---

$ serverless deploy

Serverless Error ------------------------------------------------------

Serverless plugin "serverless-google-cloudfunctions"
initialization errored: Cannot find module 'serverless-google-cloudfunctions'
Require stack:
- /usr/local/lib/node_modules/serverless/lib/classes/PluginManager.js
- /usr/local/lib/node_modules/serverless/lib/Serverless.js
- /usr/local/lib/node_modules/serverless/lib/utils/autocomplete.js
- /usr/local/lib/node_modules/serverless/bin/serverless.js

Get Support ------------------------------------------------------
    Docs:        docs.serverless.com
    Bugs:        github.com/serverless/serverless/issues
    Issues:      forum.serverless.com

Your Environment Information -----------------------------
    Operating System:      darwin
    Node Version:          12.9.0
    Framework Version:     1.50.0
    Plugin Version:        1.3.8
    SDK Version:           2.1.0

Ошибка, которую мы наблюдаем, связана с тем, что еще не установлены указанные в package.json зависимости:

$ cat package.json
{
  "name": "google-python-simple-http-endpoint",
  "version": "0.0.1",
  "description":
  "Example demonstrates how to setup a simple HTTP GET endpoint with python",
  "author": "Sebastian Borza <sebito91@gmail.com>",
  "license": "MIT",
  "main": "handler.py",
  "scripts": {
    "test": "echo \\\"Error: no test specified\\\" && exit 1"
  },
  "dependencies": {
    "serverless-google-cloudfunctions": "^2.1.0"
  }
}

Платформа Serverless написана на node.js, так что ее пакеты необходимо установить с помощью команды npm install:

$ npm install