---
source_image: page_197.png
page_number: 197
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.09
tokens: 7383
characters: 1679
timestamp: 2025-12-24T03:06:09.613337
finish_reason: stop
---

Наконец, производится синхронизация HTML-страниц в Amazon S3. А поскольку она выполняется внутри AWS и синхронизируется, то тоже происходит чрезвычайно быстро. Последний шаг — удаление объектов из CloudFront:

version: 0.1

environment_variables:
    plaintext:
        HUGO_VERSION: "0.42"

phases:
    install:
        commands:
            - cd /tmp
            - wget https://github.com/gohugoio/hugo/releases/\
                download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
            - tar -xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
            - mv hugo /usr/bin/hugo
            - cd -
            - rm -rf /tmp/*
    build:
        commands:
            - rm -rf public
            - hugo
    post_build:
        commands:
            - aws s3 sync public/ s3://<yourwebsite>.com/ --region us-west-2 --delete
            - aws s3 cp s3://<yourwebsite>.com/\
                s3://<yourwebsite>.com/ --metadata-directive REPLACE \
                --cache-control 'max-age=604800' --recursive
            - aws cloudfront create-invalidation --distribution-id=<YOURID> --paths '/*'
            - echo Build completed on `date`

Ситуационный анализ примера из практики: развертывание приложения Python App Engine с помощью Google Cloud Build

В 2008 году я написал свою первую статью об использовании Google App Engine. Чтобы посмотреть ее в блоге O’Reilly, вам придется воспользоваться архивом Интернета (https://oreil.ly/8LoIf).

Этот пример — ее переосмысление применительно к современности. Это еще одна версия Google App Engine, но на этот раз задействующая Google Cloud Build (https://oreil.ly/MllhM). Далее приведен файл конфигурации, занесенный