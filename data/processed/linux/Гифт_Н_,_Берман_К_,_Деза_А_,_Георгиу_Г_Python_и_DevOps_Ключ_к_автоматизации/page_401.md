---
source_image: page_401.png
page_number: 401
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.77
tokens: 7336
characters: 1687
timestamp: 2025-12-24T03:11:25.124807
finish_reason: stop
---

Попробуем выполнить развертывание снова:

$ serverless deploy
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Compiling function "currentTime"...
Serverless: Uploading artifacts...

    Error -------------------------------------------------------------
    Error: Not Found
    at createError
    (/Users/ggheo/code/mycode/examples/google-python-simple-http-endpoint/node_modules/axios/lib/core/createError.js:16:15)
    at settle (/Users/ggheo/code/mycode/examples/google-python-simple-http-endpoint/node_modules/axios/lib/core/settle.js:18:12)
    at IncomingMessage.handleStreamEnd
    (/Users/ggheo/code/mycode/examples/google-python-simple-http-endpoint/node_modules/axios/lib/adapters/http.js:202:11)
    at IncomingMessage.emit (events.js:214:15)
    at IncomingMessage.EventEmitter.emit (domain.js:476:20)
    at endReadableNT (_stream_readable.js:1178:12)
    at processTicksAndRejections (internal/process/task_queues.js:77:11)

For debugging logs, run again after setting the "SLS_DEBUG=*" environment variable.

Заглянем в документацию платформы Serverless по учетным записям и ролям GCP (https://oreil.ly/scsRg).

Оказывается, что для использования учетной записи сервиса для развертывания необходимо назначить ей следующие роли:

• Deployment Manager Editor;
• Storage Admin;
• Logging Admin;
• Cloud Functions Developer.

Заглянем также в документацию платформы Serverless на предмет того, какие API GCP необходимо включить (https://oreil.ly/rKiHg).

Выясняется, что в консоли GCP необходимо включить следующие API:

• Google Cloud Functions;
• Google Cloud Deployment Manager;
• Google Cloud Storage;
• Stackdriver Logging.