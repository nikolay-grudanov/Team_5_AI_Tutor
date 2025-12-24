---
source_image: page_376.png
page_number: 376
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.18
tokens: 7481
characters: 1789
timestamp: 2025-12-24T08:55:32.391714
finish_reason: stop
---

Импорт модулей и функция main()

Рассмотрим исходный код программы для взлома шифра Виженера. Данная программа импортирует различные модули, в том числе и новый модуль itertools, о котором вскоре будет рассказано более подробно.

1. # Программа взлома шифра Виженера
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import itertools, re
5. import vigenereCipher, pyperclip, freqAnalysis, detectEnglish

В строках 7–11 задается несколько констант, о назначении которых мы поговорим, когда будем обсуждать код, в котором они используются.

Функция main() напоминает аналогичные функции предыдущих программ взлома.

14. def main():
15.     # Этот шифротекст можно скопировать из
16.     # файла исходного кода (см. введение)
17.     ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi,
lgouqdaf, kdmktsvmztstl, izr xoexghrz kkusitaaf. Vz wsa twbhdg
ubalmmzhdad qz
--опущено--
azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo
Tmzubb a kbmhptgzk dvrvwz wa efiohzd.""""
18.     hackedMessage = hackVigenere(ciphertext)
19.
20.     if hackedMessage != None:
21.         print('Copying hacked message to clipboard:')
22.         print(hackedMessage)
23.         pyperclip.copy(hackedMessage)
24.     else:
25.         print('Failed to hack encryption.')

Шифротекст передается функции hackVigenere(), которая возвращает либо дешифрованную строку, если попытка взлома оказалась успешной, либо значение None в случае неудачи. В случае успеха программа выводит взломанное сообщение на экран и копирует его в буфер обмена.

Нахождение повторяющихся последовательностей

Функция findRepeatSequencesSpacings() реализует первый этап метода Касиски, обнаруживая все повторяющиеся последовательности букв в строке сообщения и вычисляя длину интервалов между ними.