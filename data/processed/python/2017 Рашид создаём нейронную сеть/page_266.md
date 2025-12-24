---
source_image: page_266.png
page_number: 266
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.46
tokens: 6415
characters: 963
timestamp: 2025-12-24T02:15:22.907116
finish_reason: stop
---

Если GitHub не воспримет Epiphany, введите в адресной строке браузера следующую ссылку для загрузки файлов:

https://github.com/makeyourownneuralnetwork/makeyourownneuralnetwork/archive/master.zip

Браузер сообщит вам об окончании загрузки. Откройте новое окно терминала и введите следующие команды, чтобы распаковать файлы, а затем освободить место, удалив zip-файл.

unzip Downloads/makeyourownneuralnetwork-master.zip
rm -f Downloads/makeyourownneuralnetwork-master.zip

Файлы будут распакованы в каталог makeyourownneuralnetwork-master. При желании можете присвоить ему более короткое имя, но делать это вовсе необязательно.

На сайте GitHub содержатся лишь сокращенные версии наборов данных MNIST, поскольку сайт не позволил бы мне разместить файлы большего размера. Чтобы получить полный набор данных, введите в том же окне терминала следующие команды для перехода в каталог mnist_dataset и получения тренировочного и тестового наборов данных в CSV-формате.