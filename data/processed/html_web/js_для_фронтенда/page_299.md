---
source_image: page_299.png
page_number: 299
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.09
tokens: 6096
characters: 940
timestamp: 2025-12-24T10:08:38.861126
finish_reason: stop
---

В разделе Build Triggers вы можете включить триггер Poll SCM, позволяющий неоднократно проверять любые изменения. На рис. 8.9 показано, что я опрашиваю Subversion каждые 20 минут. Если что-то изменилось, будет начата сборка (вот она наша непрерывная интеграция!)

Наконец, вы должны указать Jenkins, что нужно сделать для сборки репозитория (например, указать команду сборки) и что сделать после сборки.

Рассмотрим Makefile, который произведет модульное тестирование всего кода и сожмет код, разместив его в каталоге release, который может быть впоследствии размещен на веб-сервере, если все нормально:

DO_COVERAGE=1
RELEASE=release
UGLIFY=uglifyjs
SRC := $(shell find src -name '*.js')
OBJS := $(patsubst %.js,%_jc,$(SRC))
%.jc : %.js
    -mkdir -p $(RELEASE)/$(@D)
    $(UGLIFY) -o $(RELEASE)/$(*D)/$(*F).js $<
prod: unit_tests $(OBJS)
setupJUTE:
ifdef WORKSPACE
    npm config set jute:docRoot '$(WORKSPACE)'
    npm restart jute
endif