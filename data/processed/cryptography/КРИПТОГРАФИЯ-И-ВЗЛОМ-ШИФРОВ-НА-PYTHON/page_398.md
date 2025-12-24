---
source_image: page_398.png
page_number: 398
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.48
tokens: 7459
characters: 1926
timestamp: 2025-12-24T08:56:07.910057
finish_reason: stop
---

мы определяем возможные варианты длины ключа с помощью функции kasiskiExamination().

223. def hackVigenere(ciphertext):
224.     # Прежде всего, необходимо применить метод Касиски
225.     # для выяснения возможной длины ключа
226.     allLikelyKeyLengths = kasiskiExamination(ciphertext)

Список возможных вариантов выводится на экран, если для константы SILENT_MODE было установлено значение False.

227.     if not SILENT_MODE:
228.         keyLengthStr = ''
229.         for keyLength in allLikelyKeyLengths:
230.             keyLengthStr += '%s ' % (keyLength)
231.         print('Kasiski examination results say the most likely key lengths are: ' + keyLengthStr + '\n')

Далее необходимо найти наиболее вероятные буквы подключей для каждой длины ключа. Это делается с помощью еще одного цикла, в котором функция пытается взломать шифр, используя каждую найденную длину ключа.

Выход из цикла, если найден потенциальный ключ

Мы хотим, чтобы цикл тестирования длины ключа продолжался до тех пор, пока не будет найдена корректная длина ключа. Если функция attemptHackWithKeyLength() сумела подобрать ключ, то цикл принудительно завершается с помощью инструкции break.

По аналогии с тем, как инструкция continue применяется в теле цикла для возврата в его начало, инструкция break предназначена для немедленного выхода из цикла. Встретив данную инструкцию, программа немедленно переходит к выполнению строки, стоящей сразу за телом цикла. Мы прервем цикл, когда программа найдет корректный ключ, подтвержденный пользователем.

232.     hackedMessage = None
233.     for keyLength in allLikelyKeyLengths:
234.         if not SILENT_MODE:
235.             print('Attempting hack with key length %s (%s possible keys) ...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
236.             hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
237.             if hackedMessage != None:
238.                 break