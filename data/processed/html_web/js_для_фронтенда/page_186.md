---
source_image: page_186.png
page_number: 186
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.05
tokens: 6207
characters: 1681
timestamp: 2025-12-24T10:06:14.829466
finish_reason: stop
---

В случае интеграционного тестирования

Процесс сохранения информации о покрытии интеграционного тестирования с использованием Selenium аналогичен. После выполнения тестов Selenium, но перед тем, как уйти с текущей страницы, нужно получить информацию о покрытии и передать ее обратно на сервер. Selenium предоставляет функции tearDown и after, в которые и нужно добавить код для обеспечения захвата результатов покрытия.

Лучше всего в Selenium это делать с использованием глобальной переменной _yuitest_coverage, в которую помещается вся информация о покрытии. В Selenium1 код получения информации о покрытии будет выглядеть так:

String coverage = selenium.getEval(
    "JSON.stringify(window._yuitest_coverage)");;

При использовании Selenium2/WebDriver код будет следующим:

String coverage = (String)((JavaScriptExecutor) driver)
    .executeScript("return JSON.stringify(window._yuitest_coverage);");

Затем просто выведите переменную coverage в файл. В идеале, этот файл должен называться так же, как и ваш тест, например testClick.coverage.json.

Имейте в виду, что, если ваше приложение использует фреймы (iframes), информация о покрытии кода из iframe не будет получена посредством высокоуровневой переменной yuitest_coverage. После захвата покрытия кода из высокоуровневого главного окна вам нужно указать Selenium1, какой фрейм использовать:

selenium.SelectFrame("src=foo.html");

В Selenium2-3/WebDriver нужно использовать следующий код:

driver.SwitchTo().Frame(driver.FindElement(By.CssSelector(
    "iframe[src=\"foo.html\"]")));;

Кроме того, можно просто использовать селектор Selenium для выбора нужного фрейма, для которого нужно получить информацию о покрытии.