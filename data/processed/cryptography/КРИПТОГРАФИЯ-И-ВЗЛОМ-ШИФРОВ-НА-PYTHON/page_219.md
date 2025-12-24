---
source_image: page_219.png
page_number: 219
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.99
tokens: 7558
characters: 1933
timestamp: 2025-12-24T08:51:35.976062
finish_reason: stop
---

Исходный код программы Transposition Hacker

Откройте в редакторе файлов новое окно, выбрав пункты меню File⇒New File. Введите в этом окне приведенный ниже код и сохраните его в файле transpositionHacker.py. Как всегда, убедитесь в том, что модули pyperclip.py и transpositionDecrypt.py (см. главу 8), а также модуль detectEnglish.py и файл dictionary.txt (см. главу 11) находятся в том же каталоге, что и файл transpositionHacker.py. Запустите программу, нажав клавишу <F5>.

transpositionHacker.py

1. # Программа взлома перестановочного шифра
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import pyperclip, detectEnglish, transpositionDecrypt
5.
6. def main():
7.     # Приведенный ниже текст можно скопировать
8.     # из файла примера (см. введение)
9.     myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e enlh na indeit n uhoretrm au ieu v er Ne2 gmanw, forwnlbsya apor tE.no euarisfatt e mealefedhsppmgAnlnoe(c-or)alat r lw o eb ngIom,Ain one dtes ilhetcdba. t tg eturmudg,tfllel v nitiaicynhrCsaemie-sp ncgHt nie cetrqmnoa yc r,ieaa toesa- e a0m82e1w shcnth ekh gaecnpeutaaietgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss d iorr."""

11. hackedMessage = hackTransposition(myMessage)
12.
13. if hackedMessage == None:
14.     print('Failed to hack encryption.')
15. else:
16.     print('Copying hacked message to clipboard:')
17.     print(hackedMessage)
18.     pyperclip.copy(hackedMessage)
19.
20.
21. def hackTransposition(message):
22.     print('Hacking...')
23.
24.     # Выполнение программы на Python можно в любой момент прервать,
25.     # нажав <Ctrl+C> (Windows) или <Ctrl+D> (macOS и Linux)
26.     print('(Press Ctrl-C (on Windows) or Ctrl-D (on macOS and Linux) to quit at any time.)')
27.
28.     # Перебор всех возможных ключей методом грубой силы
29.     for key in range(1, len(message)):
30.         print('Trying key #%s...' % (key))