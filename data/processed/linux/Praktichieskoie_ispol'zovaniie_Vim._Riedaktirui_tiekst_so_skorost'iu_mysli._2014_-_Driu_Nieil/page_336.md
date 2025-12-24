---
source_image: page_336.png
page_number: 336
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.34
tokens: 5609
characters: 1701
timestamp: 2025-12-24T04:16:33.249812
finish_reason: stop
---

Рецепт 109. Настройка программы grep

В OS X программу ack можно установить с помощью Homebrew:

⇒ $ brew install ack

Давайте посмотрим, как настроить параметры grepprg и grepformat, чтобы команда :grep вызывала ack вместо grep. По умолчанию программа ack выводит имя файла в отдельной строке, за которой следует строка с номером и содержимым строки в файле, содержащей искомое совпадение:

⇒ $ ack Waldo *
department-store.txt
1:Waldo is beside the boot counter.

goldrush.txt
6:Waldo is studying his clipboard.
9:The penny farthing is 10 paces ahead of Waldo.

Мы легко можем организовать вывод результатов в формате, напоминающем формат вывода команды grep -n, вызвав команду ack с ключом --nogroup:

⇒ $ ack --nogroup Waldo *
department-store.txt:1:Waldo is beside the boot counter.
goldrush.txt:6:Waldo is studying his clipboard.
goldrush.txt:9:The penny farthing is 10 paces ahead of Waldo.

Этот формат вывода в точности соответствует формату вывода команды grep -n, а так как значение по умолчанию параметра grepformat уже прекрасно справляется с анализом этого формата, нам не требуется изменять его. То есть нам остается всего лишь подменить вызов команды grep командой ack, установив новое значение в параметре grepprg:

⇒ :set grepprg=ack\ --nogroup\ $*

Альтернативные расширения для поиска в файлах

Редактор Vim упрощает поиск совпадений во множестве файлов с применением внешней программы. Нам нужно только изменить параметры grepprg и grepformat, и можно начинать пользоваться командой :grep, которая точно так же будет сохранять вывод программы в списке результатов. Не важно, какая программа будет вызываться в действительности, интерфейс доступа к результатам остается неизменным.