---
source_image: page_817.png
page_number: 817
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.42
tokens: 7581
characters: 2034
timestamp: 2025-12-24T01:32:34.625817
finish_reason: stop
---

его свойства. Обратите внимание, что ваш сценарий может сообщать о меньшем количестве символов, чем среда Windows — в целях переносимости Python преобразует маркеры \r\n конца строки Windows в \n, отбрасывая тем самым 1 байт (символ) на строку. Для точного соответствия счетчиков байтов с Windows вы должны открыть файл в двоичном режиме ('rb') или добавить количество байтов, равное количеству строк. Дополнительные сведения о трансляции символов конца строки ищите в главах 9 и 37.

"Амбициозная" часть этого упражнения (передача файлового объекта, чтобы открывать файл только один раз) потребует применения метода seek встроенного файлового объекта. Он работает подобно функции fseek в языке C (и может внутренне вызывать ее): seek переустанавливает текущую позицию в файле согласно переданному смещению. После вызова seek будущие операции ввода-вывода станут выполняться относительно новой позиции. Для перехода в начало файла без его закрытия и повторного открытия вызовите file.seek(0); все файловые методы read производят чтение с текущей позиции файла, так что для повторного чтения вам придется переходить в начало файла. Вот как может выглядеть описанная настройка:

def countLines(file):
    file.seek(0)
    return len(file.readlines())
def countChars(file):
    file.seek(0)
    return len(file.read())
def test(name):
    file = open(name)
    return countLines(file), countChars(file)

>>> import mymod2
>>> mymod2.test("mymod2.py")
(11, 392)

2. from/from *. Ниже показана часть from *; чтобы сделать остальное, поменяйте
* на countChars:
% python
>>> from mymod import *
>>> countChars("mymod.py")

3. __main__. При надлежащем написании кода этот файл работает в любом из двух режимов — запуск как программы или импортирование как модуля:

def countLines(name):
    file = open(name)
    return len(file.readlines())
def countChars(name):
    return len(open(name).read())
def test(name):
    return countLines(name), countChars(name)
if __name__ == '__main__':
    print(test('mymod.py'))
% python mymod.py
(13, 346)