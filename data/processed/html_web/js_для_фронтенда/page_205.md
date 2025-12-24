---
source_image: page_205.png
page_number: 205
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.79
tokens: 6249
characters: 1741
timestamp: 2025-12-24T10:06:45.301595
finish_reason: stop
---

дине страницы, а внизу идет продолжение страницы, которое, так сказать, "не видно". При реальном просмотре страницы в браузере баннер прилеплен к низу видимой области и остается там при прокрутке содержимого страницы.

Это мы работали под Firefox, который используется по умолчанию. Чтобы запустить этот же пример в Chrome, вам нужно загрузить драйвер Chrome для вашей операционной системы (https://code.google.com/p/selenium/wiki/ChromeDriver) и установить его в любой из каталогов, определенный в переменной окружения PATH. Затем просто измените эту строчку:

, desiredCapabilities: { browserName: 'firefox' }

исправив на:

, desiredCapabilities: { browserName: 'chrome' }

Так, а что насчет Internet Explorer'a? Для него тоже есть свой драйвер. Последний для вашей платформы драйвер IE можно загрузить с сайта https://code.google.com/p/selenium/downloads/list. Затем поместите исполняемый файл в один из каталогов, указанных в переменной PATH, и запустите его. По умолчанию драйвер использует порт 5555:

, port: 5555
, desiredCapabilities: { browserName: 'internetExplorer' }

Selenium Remote Control

Программное решение Selenium Remote Control является «замороженной» веткой развития Selenium, место которой занял поддерживаемый и развивающийся WebDriver. Однако могут быть ситуации, когда вам может пригодиться Selenium RT.

Дело в том, что WebDriver не является результатом эволюционного развития Selenium RT и оба этих продукта построены на очень разных принципах, и у них практически нет общего кода. Так вот, Selenium RT при создании тестовых сценариев использует свой скриптовый язык, условно называемый Selenium 1, который по своей сути является JavaScript. Тогда как WebDriver использует уже свой индивидуальный язык Selenium.