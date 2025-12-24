---
source_image: page_222.png
page_number: 222
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.90
tokens: 7526
characters: 1914
timestamp: 2025-12-24T08:51:40.309260
finish_reason: stop
---

Создание многострочного текста с помощью тройных кавычек

Переменная myMessage содержит шифротекст, который мы пытаемся взломать. В строке 9 хранится строка, которая начинается и заканчивается тройными кавычками. Заметьте, насколько это длинная строка.

6. def main():
7.     # Приведенный ниже текст можно скопировать
8.     # из файла примера (см. введение)
9.     myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e enlh na indeit n uhoretrm au ieu v er Ne2 gmanw, forwnlbsya apor tE.no euarisfatt e mealefedhsppmgAnlnoe(c -or)alat r lw o eb ngom,Ain one dtes ilhetcdba. t tg eturmudg,tflle1 v nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa toesa- e a0m82elw shcnth ekh gaecnpeutaaiieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaiss d iorr."""

Текст, заключенный в тройные кавычки, называется многострочным, поскольку он охватывает несколько строк и может содержать символы разрыва строки. Многострочные тексты удобны по той причине, что их можно использовать для включения длинных строк в исходный код программы, а также тем, что они не требуют экранирования встречающихся в них одинарных и двойных кавычек. В качестве примера многострочного текста введите в интерактивной оболочке следующие инструкции.

>>> spam = """Dear Alice,
Why did you dress up my hamster in doll clothing?
I look at Mr. Fuzz and think, "I know this was Alice's doing."
Sincerely,
Brienne"""
>>> print(spam)
Dear Alice,
Why did you dress up my hamster in doll clothing?
I look at Mr. Fuzz and think, "I know this was Alice's doing."
Sincerely,
Brienne

Обратите внимание на то, что этот текст занимает несколько строк. Все, что следует за открывающими тройными кавычками, будет интерпретироваться как часть строки до тех пор, пока программа снова не встретит тройные кавычки. При создании многострочного текста допускается использование либо трех двойных, либо трех одинарных кавычек.