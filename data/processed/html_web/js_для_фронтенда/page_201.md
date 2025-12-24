---
source_image: page_201.png
page_number: 201
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.92
tokens: 6287
characters: 1609
timestamp: 2025-12-24T10:06:44.855026
finish_reason: stop
---

package com.example.tests;

Измените это объявление так, чтобы оно соответствовало вашему окружению (вместо example укажите имя вашего класса) или просто удалите эту строку.

Для дальнейших опытов нам понадобятся установленные сервер Selenium Server и клиентские Java-драйверы. Загрузите текущую версию сервера Selenium Server (3.141.59 на момент написания этих строк) и Java Selenium client driver (3.141.59 на момент написания этих строк) — WebDriver под Java — с сайта http://www.seleniumhq.org/download/. Вам нужно распаковать клиент Java Selenium.

Теперь откомпилируем экспортированный нами ранее Selenium-сценарий с помощью selenium-server.jar:

% java -cp path/to/selenium-server-standalone-3.141.59.jar test.java

Данная команда откомпилирует экспортируемый вами тестовый случай Selenium. Чтобы выполнить ваш тест, вам сначала нужно запустить сервер Selenium:

% java -jar path/to/selenium-server-standalone-3.141.59.jar

Ну а затем «скормить» ваш тестовый JUnit-сценарий (введите все в одной строке):

% java -cp path/to/selenium-server-standalone-3.141.59.jar:Downloads/selenium-2.20.0/libs/junit-dep-5.1.jar:. org.junit.runner.JUnitCore test

Понятно, что вы должны указать свои пути к файлу сервера Selenium (selenium-server-standalone-3.141.59.jar) и к JAR-файлу JUnit (junit-dep-5.1.jar).

Приведенная ранее команда подразумевает, что вы удалили объявление package. Если нет, вам нужно использовать немного другую команду (опять все в одной строке):

% java -cp selenium-server-standalone-3.141.59.jar:selenium-3.141.59/libs/junit-dep-5.1.jar:. org.junit.runner.JUnitCore com.example.tests.test