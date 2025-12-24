---
source_image: page_196.png
page_number: 196
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.26
tokens: 7334
characters: 1447
timestamp: 2025-12-24T03:06:04.360544
finish_reason: stop
---

Координация с помощью Makefile

Использование Makefile позволяет повторять шаги развертывания. Обычно я создаю Makefile для локальной координации этого процесса. Вот как выглядит весь ход сборки и развертывания:

build:
  rm -rf public
  hugo

watch: clean
  hugo server -w

create-index:
  cd algolia;python make_algolia_index.py;cd ..

update-index:
  cd algolia;python sync_algolia_index.py;cd ..

make-index: create-index update-index

clean:
  -rm -rf public

sync:
  aws s3 --profile <yourawsprofile> sync --acl \
    "public-read" public/ s3://example.com

build-deploy-local: build sync

all: build-deploy-local

Развертывание с помощью AWS CodePipeline

Веб-сервисы Amazon (Amazon Web Services, AWS) — часто используемая платформа развертывания статических веб-сайтов посредством Amazon S3, Amazon Route 53 и Amazon CloudFront. AWS CodePipeline, сервис сервера сборки, прекрасно подходит для этих сайтов в качестве механизма развертывания. Можно войти в систему AWS CodePipeline, создать новый проект сборки и задать для использования им файл настроек buildspec.yml. Код можно настроить под свои нужды, а шаблонизированные части заменить фактическими значениями.

Сразу после получения GitHub события фиксации изменения CodePipeline запускает установку в контейнере. Сначала он берет указанную конкретную версию Hugo, а затем выполняет сборку страниц Hugo. Благодаря мощи Go визуализация тысяч страниц Hugo занимает считаные доли секунды.