---
source_image: page_174.png
page_number: 174
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.46
tokens: 11856
characters: 1998
timestamp: 2025-12-24T01:42:46.998390
finish_reason: stop
---

<table>
  <tr>
    <th>Имя</th>
    <th>Тип</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>__name__</td>
    <td>str</td>
    <td>Имя функции</td>
  </tr>
  <tr>
    <td>__qualname__</td>
    <td>str</td>
    <td>Полное имя функции, например, Random.choice (см. PEP-3155 (<a href="https://www.python.org/dev/peps/pep-3155/">https://www.python.org/dev/peps/pep-3155/</a>))</td>
  </tr>
</table>

Ниже мы обсудим атрибуты __defaults__, __code__ и __annotations__, которые используются интегрированными средами разработки и каркасами для получения информации о сигнатуре функции. Но чтобы полнее оценить их прелесть, сделаем небольшое отступление и рассмотрим богатый синтаксис, предлагаемый в Python для объявления параметров функции и передачи ей аргументов.

От позиционных к чисто именованным параметрам

Одна из самых замечательных особенностей функций в Python — чрезвычайно гибкий механизм обработки параметров, дополненный в Python 3 чисто именованными аргументами. С этой темой тесно связано использование * и ** для «развертывания» итерируемых объектов и отображений в отдельные аргументы при вызове функции. Чтобы понять, как это выглядит на практике, взгляните на код в примере 5.10 и результат его выполнения в примере 5.11.

Пример 5.10. Функция tag генерирует HTML; чисто именованный аргумент cls служит для передачи атрибута «class». Это обходное решение необходимо, потому что в Python class — зарезервированное слово

def tag(name, *content, cls=None, **attrs):
    """Генерирует один или несколько HTML-тегов"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
            for attr, value
            in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
            (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

Функцию tag можно вызывать различными способами, как показано в примере 5.11.