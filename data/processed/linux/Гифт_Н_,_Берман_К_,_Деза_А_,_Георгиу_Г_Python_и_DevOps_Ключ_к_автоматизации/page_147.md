---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.43
tokens: 7491
characters: 1617
timestamp: 2025-12-24T03:04:45.523085
finish_reason: stop
---

else
    echo "Module ${1} not found or is not importable: $MODULE_DIRECTORY"
fi
}

Немного повысим ее устойчивость к ошибкам на случай, если в названии пакета присутствует тире, а в модуле — подчеркивание, добавив:

module=$(sed 's/-/_/g' <<< $1)

Если во введенном названии есть тире, наша маленькая функция сразу решит проблему и перенесет нас в нужный каталог:

$ cdp pkg-resources
$ pwd
/usr/lib/python2.7/dist-packages/pkg_resources

Преобразование CSV-файла в JSON

В Python есть несколько встроенных утилит, которые могут вас приятно удивить, если вы раньше с ними не сталкивались, в частности, для нативной обработки JSON и CSV-файлов. Для загрузки CSV-файла и дальнейшего сброса его содержимого в JSON достаточно всего нескольких строк кода. Возьмем следующий CSV-файл (addresses.csv) и посмотрим на содержимое после сброса JSON в командную оболочку Python:

John,Doe,120 Main St.,Riverside, NJ, 08075
Jack,Jhonson,220 St. Vernardeen Av.,Phila, PA,09119
John,Howards,120 Monroe St.,Riverside, NJ,08075
Alfred, Reynolds, 271 Terrell Trace Dr., Marietta, GA, 30068
Jim, Harrison, 100 Sandy Plains Plc., Houston, TX, 77005

>>> import csv
>>> import json
>>> contents = open("addresses.csv").readlines()
>>> json.dumps(list(csv.reader(contents)))
'[["John", "Doe", "120 Main St.", "Riverside", " NJ", " 08075"],
["Jack", "Jhonson", "220 St. Vernardeen Av.", "Phila", " PA", "09119"],
["John", "Howards", "120 Monroe St.", "Riverside", " NJ", "08075"],
["Alfred", " Reynolds", " 271 Terrell Trace Dr.", " Marietta", " GA", " 30068"],
["Jim", " Harrison", " 100 Sandy Plains Plc.", " Houston", " TX", " 77005"]]'