---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.43
tokens: 6186
characters: 1582
timestamp: 2025-12-24T10:07:47.100625
finish_reason: stop
---

, browser = webdriverjs.remote({
    host: 'localhost'
    , port: 4444
    , desiredCapabilities: {
        browserName: 'chrome'
        , seleniumProtocol: 'WebDriver'
        , 'chrome.switches': [
            '--remote-debugging-port=9222'
            , '--user-data-dir=remote-profile'
        ]
    }
})
);
browser.addCommand("startCapture", startCapture);
browser
    .init()
    .url('http://search.yahoo.com')
    .startCapture()
    .setValue("#yschsp", "JavaScript")
    .submitForm("#sf")
    .saveScreenshot('results.png')
    .end();

Все это — стандартный код webdriverjs, с которым мы знакомились чуть ранее. Однако, к нему есть два дополнения. Первое дополнение — желаемая возможность chrome.switches (предоставляет доступ к параметрам командной строки Chrome, по сути является массивом параметров). Драйвер Chrome позволяет нам указывать параметры командной строки для исполняемого файла Chrome. И мы при вызове браузера говорим Chrome, что нужно слушать удаленные соединения отладчика на порту 9222 и использовать профиль из определенного каталога. Для использования удаленной отладки нам не нужны ни какие-то определенные расширения или настройки Chrome. Поэтому мы просто используем пустой профиль.

Второе дополнение — это функция startCapture. Пакет webdriverjs позволяет нам определить свой пользовательский метод, который может быть объединен в цепочку вместе с другими стандартными методами webdriverjs. Любой пользовательский метод получает функцию обратного вызова, которая будет вызвана по завершении пользовательской функции. Здесь мы определили метод