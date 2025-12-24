---
source_image: page_316.png
page_number: 316
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.67
tokens: 7469
characters: 1821
timestamp: 2025-12-24T08:53:57.235861
finish_reason: stop
---

функциями, которые необходимы для построения полного пересечения всех словарей шифробукв, взлома ключа и дешифрования сообщения. Рассмотрим пример того, как эти функции применяются в интерактивной оболочке.

Дешифрование сообщения в интерактивной оболочке

Вернемся к примеру из раздела "Как работают вспомогательные функции". Для дешифрования сообщения 'OLQIHXIRCKGNZ PLQRZKBZB MPBKSSIPLC' мы воспользуемся переменной intersectedMapping, которая ранее была создана в интерактивной оболочке.
Введите в интерактивной оболочке следующие инструкции.

>>> simpleSubHacker.decryptWithCipherletterMapping('OLQIHXIRCKGNZ PLQRZKBZB MPBKSSIPLC', intersectedMapping)
UNCOMFORTABLE INCREASES DISAPPOINT

Итак, шифротекст дешифруется в сообщение "Uncomfortable increases disappoint". Как видите, функция decryptWithCipherletterMapping() сработала идеально и вернула полностью дешифрованное сообщение. Однако этот пример не демонстрирует того, что происходит в тех случаях, когда не все символы, появляющиеся в шифротексте, удается расшифровать. Мы можем увидеть, что произойдет при отсутствии варианта дешифрования для какой-либо шифробуквы, удалив из объединенного пересечения intersectedMapping решения для шифробукв 'M' и 'S' с помощью следующих инструкций.

>>> intersectedMapping['M'] = []
>>> intersectedMapping['S'] = []

Попробуем снова дешифровать шифротекст с помощью словаря intersectedMapping.

>>> simpleSubHacker.decryptWithCipherletterMapping('OLQIHXIRCKGNZ PLQRZKBZB MPBKSSIPLC', intersectedMapping)
UNCOMFORTABLE INCREASES _ISA_OINT

На этот раз часть шифротекста осталась не дешифрованной. Шифробуквы, для которых не нашлось варианта дешифрования, были заменены символами подчеркивания.
В этом примере текст, используемый для демонстрации взлома, был очень коротким. Обычно длина дешифруемых текстов намного больше.