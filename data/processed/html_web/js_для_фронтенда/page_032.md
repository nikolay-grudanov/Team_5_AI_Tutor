---
source_image: page_032.png
page_number: 32
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.68
tokens: 6208
characters: 1584
timestamp: 2025-12-24T10:03:10.423529
finish_reason: stop
---

В качестве примера рассмотрим разделение команд и запросов в контексте применения Node.js²:

function configure(values) {
    var fs = require('fs')
        , config = { docRoot: '/somewhere' }
        , key
        , stat
    ;
    for (key in values) {
        config[key] = values[key];
    }
    try {
        stat = fs.statSync(config.docRoot);
        if (!stat.isDirectory()) {
            throw new Error('Не допустимо');
        }
    } catch(e) {
        console.log("** " + config.docRoot +c
            " не существует или это не каталог!!! **");
        return;
    }
    // ... проверяем другие значения ...
    return config;
}

Давайте рассмотрим тестовый сценарий для этой функции. В главе 4 мы обсудим синтаксис этих тестов более подробно, а сейчас мы просто посмотрим на него:

describe("настраиваем тесты", function() {
    it("не определено, если docRoot не существует", function() {
        expect(configure({ docRoot: '/xxx' })).toBeUndefined();
    });
    it("определен, если docRoot существует", function() {
        expect(configure({ docRoot: '/tmp' })).not.toBeUndelined();
    });
    it("добавляем значения в хэш config", function() {
        var config = configure({ docRoot: '/tmp', zany: 'crazy' });
        expect(config).not.toBeUndefined();
    });
}

² Node.js — это сервверная платформа (каркас, фреймворк) на базе JavaScript, предназначенная для создания масштабируемых распределённых сетевых приложений, таких как веб-сервер. В отличие от большинства JavaScript-программ, этот фреймворк исполняется не в браузере клиента, а на стороне сервера.