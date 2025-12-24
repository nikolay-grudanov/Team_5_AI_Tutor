---
source_image: page_137.png
page_number: 137
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.62
tokens: 7193
characters: 994
timestamp: 2025-12-24T09:23:42.047796
finish_reason: stop
---

19.11. Свойство flex-shrink

Свойство flex-shrink является противоположностью flex-grow. В данном примере значение 7 использовалось, чтобы «сжать» выбранный элемент на промежуток времени, равный 1/7 размера окружающих его элементов, что также будет изменено автоматически:

flex-shrink: 7 (сжатие в семь раз больше, чем у остальных элементов)

Работая с отдельными элементами, можно применить свойство flex в качестве сокращения для свойств flex-grow, flex-shrink и flex-based, используя только одно имя свойства:

.item { flex-none | [flex-grow | flex-shrink | flex-basis] }

19.12. Свойство justify-items

Свойство justify-items аналогично justify-content во flex-верстке, только применяется в grid-верстке:

normal | auto (по умолчанию), так же как start или flex-start или self-start или left

stretch (автоматическая ширина, если не определена явно)
center (или safe center или unsafe center)    center (расширяется в зависимости от контента)
end (так же как flex-end и self-end или right)