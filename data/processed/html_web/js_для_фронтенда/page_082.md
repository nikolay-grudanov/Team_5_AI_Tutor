---
source_image: page_082.png
page_number: 82
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.45
tokens: 6160
characters: 1227
timestamp: 2025-12-24T10:04:07.728559
finish_reason: stop
---

Здесь yuidoc — имя выходного каталога, в который будут помещены все сгенерированные HTML-файлы, а src — корневой каталог ваших JavaScript-файлов, по которому рекурсивно пройдется yuidoc для создания документации. Параметр -c задает файл конфигурации yuidoc.doc в формате JSON. В нашем случае этот файл может быть пустым JSON-объектом:

% cat src/yuidoc.json
{ }

Рассмотрим JavaScript-файл с комментариями, оформленными в соответствии с правилами (нотацией) YUIDoc:

/**
 * Предоставляет некоторые математические функции
 *
 * @class Math
 */
/**
 * Эта функция принимает два операнда, 'a' и 'b', и возвращает их сумму (или конкатенацию, если они являются строками)
 *
 * @method sum
 * @param {Number or String} a первый operand
 * @param {Number or String} b второй operand
 * @return {Number or String} Сумма
 */
exports.sum = function(a, b) { return a + b };

/**
 * Эта функция принимает два операнда, 'a' и 'b', и возвращает их произведение
 *
 * @method product
 * @param {Number} a первый operand
 * @param {Number} b второй operand
 * @return {Number} Произведение
 */
exports.mult = function(a, b) { return a * b };

На основании данного JavaScript-кода YUIDoc сгенерирует страницу, подобную изображенной на рис. 2.2.