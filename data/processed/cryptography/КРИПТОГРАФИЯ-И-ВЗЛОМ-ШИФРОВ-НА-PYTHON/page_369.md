---
source_image: page_369.png
page_number: 369
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.83
tokens: 7543
characters: 1941
timestamp: 2025-12-24T08:55:16.531163
finish_reason: stop
---

Исходный код программы Vigenere Hacker

Откройте в редакторе файлов новое окно, выбрав пункты меню File→New. Введите в этом окне приведенный ниже код и сохраните его в файле vigenereHacker.py. Убедитесь в том, что файлы detectEnglish.py, freqAnalysis.py, vigenereCipher.py и pyperclip.py находятся в той же самой папке. Запустите программу, нажав клавишу <F5>.

Шифротекст, заданный в строке 17 программы, неудобно вводить вручную. Чтобы избежать возможных опечаток, скопируйте его из файла исходного кода, доступного на сайте издательства (см. введение). Для выявления возможных различий между текстом вашей программы и текстом программы, приведенным в книге, воспользуйтесь онлайн-утилитой diff (http://inventwithpython.com/hacking/diff/).

vigenere.Hacker.py

1. # Программа взлома шифра Виженера
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import itertools, re
5. import vigenereCipher, pyperclip, freqAnalysis, detectEnglish
6.
7. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
8. MAX_KEY_LENGTH = 16      # ограничение длины проверяемых ключей
9. NUM_MOST_FREQ_LETTERS = 4 # ограничение количества букв на подключ
10. SILENT_MODE = False     # True - отключение вывода
11. NONLETTERS_PATTERN = re.compile('[^A-Z]')
12.
13.
14. def main():
15.     # Этот шифротекст можно скопировать из
16.     # файла исходного кода (см. введение)
17.     ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi,
        lgouqdaf, kdmktsvmztstl, izr xoexghzr kkusitaaf. Vz wsa twbhdg
        ubalmmzhdad qz
        --опущено--
        azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo
        Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""

18.     hackedMessage = hackVigenere(ciphertext)
19.
20.     if hackedMessage != None:
21.         print('Copying hacked message to clipboard:')
22.         print(hackedMessage)
23.         pyperclip.copy(hackedMessage)
24.     else:
25.         print('Failed to hack encryption.')