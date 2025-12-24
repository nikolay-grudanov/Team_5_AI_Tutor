---
source_image: page_084.png
page_number: 84
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.84
tokens: 6234
characters: 1452
timestamp: 2025-12-24T10:04:16.921215
finish_reason: stop
---

дополнительных файлов шаблонов. После загрузки и распаковки пакета нужно установить две переменные окружения — JSDOCDIR и JSDOCTEMPLATEDIR. Переменная JSDOCDIR задает каталог, в котором находится файл jsrun.jar. JSDOCTEMPLATEDIR содержит имя каталога шаблонов и всегда должен указывать на каталог $JSDOCDIR/templates/jsdoc, если вы, конечно, не собираетесь создавать собственные шаблоны для JSDoc.

Как только вы установили эти две переменных окружения, вы можете использовать сценарий оболочки jsrun.sh (находится в каталоге $JSOCDIR) так:

% /bin/sh $JSDOCDIR/jsrun.sh -d=<output dir> <JavaScript file>

Эта команда создаст набор HTML-файлов и поместит их в результирующий каталог <output dir>. Теперь рассмотрим JavaScript-файл с комментариями, подготовленными в стиле JSDoc (обратите внимание на разницу между JSDoc-тегами и YUIDoc-тегами):

/**
 * Эта функция принимает два операнда, 'a' и 'b', и возвращает их сумму (или конкатенацию, если они являются строками)
 *
 * @name sum
 * @function
 * @param {Number or String} a первый operand
 * @param {Number or String} b второй operand
 * @returns {Number or String} Сумма
 */
exports.sum = function(a, b) { return a + b };

/**
 * Эта функция принимает два операнда, 'a' и 'b', и возвращает их произведение
 *
 * @name product
 * @function
 * @param {Number} a первый operand
 * @param {Number} b второй operand
 * @returns {Number} Произведение
 */
exports.mult = function(a, b) { return a * b };