---
source_image: page_669.png
page_number: 669
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.68
tokens: 11832
characters: 2062
timestamp: 2025-12-24T02:05:45.266469
finish_reason: stop
---

Методы являются дескрипторами

Text('forward')
>>> word.reverse() ②
Text('drawrof')
>>> Text.reverse(Text('backward')) ③
Text('drawkcab')
>>> type(Text.reverse), type(word.reverse) ④
(<class 'function'>, <class 'method'>)
>>> list(map(Text.reverse, ['repaid', (10, 20, 30), Text('stressed')])) ⑤
['diaper', (30, 20, 10), Text('desserts')]
>>> Text.reverse.__get__(word) ⑥
<bound method Text.reverse of Text('forward')>
>>> Text.reverse.__get__(None, Text) ⑦
<function Text.reverse at 0x101244e18>
>>> word.reverse ⑧
<bound method Text.reverse of Text('forward')>
>>> word.reverse.__self__ ⑨
Text('forward')
>>> word.reverse.__func__ is Text.reverse ⑩
True

① Представление repr экземпляра Text выглядит как вызов конструктора Text, создающего точно такой же экземпляр.
② Метод reverse возвращает инвертированный текст.
③ Метод, вызванный от имени класса, работает как функция.
④ Обратите внимание на различие типов: function и method.
⑤ Метод Text.reverse работает как функция и применим даже к объектам, не являющимся экземплярами Text.
⑥ Любая функция является непереопределяющим дескриптором. Если вызвать ее метод __get__ от имени экземпляра, то будет возвращен метод, связанный с этим экземпляром.
⑦ Если вызвать метод __get__, указав в качестве аргумента instance объект None, то будет возвращена сама функция.
⑧ Выражение word.reverse приводит к вызову Text.reverse.__get__(word) и возврату связанного метода.
⑨ У объекта связанного метода имеется атрибут __self__, в котором хранится ссылка на экземпляр, от имени которого вызывался метод.
⑩ В атрибуте __func__ связанного метода хранится ссылка на исходную функцию, присоединенную к управляемому классу.

У объекта связанного метода имеется метод __call__, который и отвечает за активацию. Этот метод вызывает исходную функцию, на которую ссылается атрибут __func__, передавая ей атрибут метода __self__ в первом аргументе. Именно так работает неявное связывание с традиционным аргументом self.

Превращение функций в связанные методы — основной пример использования дескрипторов в инфраструктуре языка.