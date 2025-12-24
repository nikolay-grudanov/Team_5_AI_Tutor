---
source_image: page_157.png
page_number: 157
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.00
tokens: 6245
characters: 1704
timestamp: 2025-12-24T10:05:47.573922
finish_reason: stop
---

гому удаленному драйверу Selenium, поэтому симулятор, выполняющий приложение WebDriver, не должен быть на той же машине, на которой вы производите тестирование. Далее показано, как использовать webdriverjs:

    var browser = webdriverjs.remote({
        host: 'localhost'
        , port: 3001
        , desiredCapabilities: { browserName: 'iPhone' } // или 'iPad'
    });

И теперь ваши тесты Selenium смогут работать в iOS. Обратите внимание на то, что мы используем порт 3001 — это порт по умолчанию для iPhone WebDriver. Аналогично, вы можете использовать iPad вместо iPhone.

Android

Подробности запуска Selenium WebDriver на Android доступны на сайте проекта (https://code.google.com/p/selenium/wiki/AndroidDriver). После загрузки Android SDK и установки эмулятора у вас есть два пути: запустить "стоковый" драйвер Selenium Android или же запустить какой-либо Android-ориентированный фреймворк тестирования. При этом, если вы запускаете одни и те же тесты на разных операционных системах, лучше использовать стандартный драйвер Selenium Android Web-Driver. Но, если все ваши тесты проводятся только в Android, вам лучше остановиться на решении с Android-ориентированным фреймворком тестирования (платформой тестирования).

Давайте поподробнее рассмотрим этот драйвер. Первым делом вам нужно откомпилировать .apk-файл и установить его на ваше Android-устройство или в симулятор Android. Подключение достаточно простое:

    var browser = webdriverjs.remote({
        host: 'localhost'
        , port: 8080
        , desiredCapabilities: { browserName: 'android' }
    });

Данный код предполагает, что эмулятор работает на локальной машине. Если это не так или же вы соединяетесь с реальным устрой-