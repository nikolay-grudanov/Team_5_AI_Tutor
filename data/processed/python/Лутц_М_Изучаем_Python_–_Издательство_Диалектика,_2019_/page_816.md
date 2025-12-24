---
source_image: page_816.png
page_number: 816
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.82
tokens: 7601
characters: 1942
timestamp: 2025-12-24T01:32:34.970961
finish_reason: stop
---

else:
    return S[-1] + rev1(S[:-1])  # Рекурсивная реализация:
    # на порядок медленнее в CPython

def rev2(S):
    return ''.join(reversed(S))  # Нерекурсивная реализация
    # с итерацией: проще, быстрее

def rev3(S):
    return S[::-1]  # Даже лучше?: обращение последовательности
    # посредством нарезания

Часть V, "Модули и пакеты"

Упражнения приведены в главе 25.

1. Основы операций импортирования. После проработки упражнения итоговый файл (mymod.py) и взаимодействие должны выглядеть следующим образом; вспомните, что Python способен читать целый файл в список строк, а встроенная функция len возвращает длины строк и списков:

def countLines(name):
    file = open(name)
    return len(file.readlines())
def countChars(name):
    return len(open(name).read())
def test(name):  # Или передать файловый объект
    return countLines(name), countChars(name)  # Или возвратить словарь
% python
>>> import mymod
>>> mymod.test('mymod.py')
(10, 291)

Ваши функции подсчета могут варьироваться, как и мои могут включать или нет комментарии и дополнительную строку в конце. Обратите внимание, что эти функции загружают файл в память целиком, так что они не будут работать с крайне большими файлами, не умещающимися в память компьютера. Чтобы обеспечить более высокую надежность, взамен вы могли бы читать построчно с помощью итераторов и подсчитывать по мере продвижения:

def countLines(name):
    tot = 0
    for line in open(name): tot += 1
    return tot
def countChars(name):
    tot = 0
    for line in open(name): tot += len(line)
    return tot

Такой же эффект может дать генераторное выражение (хотя инструктор может снять баллы за чрезмерную магию!):

def countlines(name): return sum(+1 for line in open(name))
def countchars(name): return sum(len(line) for line in open(name))

В среде Unix вы можете проверить вывод посредством команды wc; в среде Windows щелкните правой кнопкой мыши на значке файла, чтобы просмотреть