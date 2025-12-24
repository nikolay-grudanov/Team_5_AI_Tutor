---
source_image: page_188.png
page_number: 188
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.35
tokens: 7182
characters: 837
timestamp: 2025-12-24T03:05:37.443988
finish_reason: stop
---

В нашем маленьком примере команда journalctl не может найти ничего за последние 15 минут. В начале выводимой ею информации указывается промежуток времени, а далее отображаются записи, если они найдены:

$ journalctl -u hello-world --since "-15min"
-- Logs begin at Mon 2019-04-15 09:05:11 EDT, end at Tue 2019-04-23
-- No entries --

Вопросы и упражнения

• Получите записи журналов от systemd с помощью journalctl, воспользовавшись тремя различными командами.
• Поясните, для чего служит опция WorkinDirectory у юнитов systemd.
• Почему журналы изменений так важны?
• Для чего предназначен файл setup.py?
• Назовите три различия пакетов Debian и RPM.

Задача на ситуационный анализ

Создайте локальный экземпляр PyPI с помощью devpi, загрузите в него пакет Python, а затем попробуйте установить его из этого локального экземпляра devpi.