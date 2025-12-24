---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 6.32
tokens: 7231
characters: 1093
timestamp: 2025-12-23T23:04:12.833733
finish_reason: stop
---

Пример команды

Чтобы перечислить все корневые ключи в ветке HKEY_LOCAL_MACHINE, введите в Git Bash команду:

$ reg query HKEY_LOCAL_MACHINE

HKEY_LOCAL_MACHINE\BCD00000000
HKEY_LOCAL_MACHINE\HARDWARE
HKEY_LOCAL_MACHINE\SAM
HKEY_LOCAL_MACHINE\SECURITY
HKEY_LOCAL_MACHINE\SOFTWARE
HKEY_LOCAL_MACHINE\SYSTEM

wevtutil

wevtutil — это утилита командной строки, используемая для просмотра системных журналов в среде Windows и управления ими. Она доступна в большинстве современных версий Windows и вызывается из Git Bash.

Общие параметры команды

□ el — перечислить доступные журналы.
□ qe — запросить события журнала.

Общие опции команды

□ /c — максимальное количество событий для чтения.
□ /f — форматировать вывод в виде текста или XML.
□ /rd — если установлено значение true, то сначала прочитать самые последние журналы.

В командной строке Windows перед параметрами команды требуется только один символ /. В терминале Git Bash из-за способа обработки команд необходимы два символа // (например, //c).

Пример команды

Чтобы перечислить все доступные журналы, введите команду:

wevtutil el