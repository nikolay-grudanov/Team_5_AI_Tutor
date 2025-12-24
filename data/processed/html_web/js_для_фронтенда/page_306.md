---
source_image: page_306.png
page_number: 306
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.82
tokens: 6153
characters: 1248
timestamp: 2025-12-24T10:08:45.437179
finish_reason: stop
---

find $(OUTPUT_DIR) -name lcov.info -exec echo '-a {}' \;
l xargs lcov > /tmp/lcov.info
cp /tmp/lcov.info ${TOTAL_LCOV_FILE}

Этот код собирает все сгенерированные файлы lcov.info в каталог output и запускает команду lcov -a ... для агрегации всех этих файлов в один файл lcov.info, который создается в корне каталога output.

Теперь, когда у нас есть один большой файл lcov.info, нам нужно конвертировать его в формат Cobertura XML. Мы можем сделать это с помощью сценария, предоставленного специальным проектом на GitHub: https://github.com/eriwen/lcov-to-cobertura-xml. Цель make-файла будет выглядеть так:

cobertura_convert:
lcov-to-cobertura-xml.py $(TOTAL_LCOV_FILE) -b src
-o $(OUTPUT)/cob.xml

Добавление этих двух целей в исходную цель unit_tests сгенерирует всю необходимую Jenkins информацию для отображения покрытия кода.

Следующий шаг — установка Jenkins-плагина Cobertura, в результате которой должна стать доступной опция Publish Cobertura Coverage Report в списке действий после сборки. Поэтому установите плагин и укажите ему, где будут находиться файлы Cobertura XML (каталоге output), как показано на рис. 8.13.

![Настройка вывода Cobertura в Jenkins](../images/chapter8_13.png)

Рис. 8.13. Настройка вывода Cobertura в Jenkins