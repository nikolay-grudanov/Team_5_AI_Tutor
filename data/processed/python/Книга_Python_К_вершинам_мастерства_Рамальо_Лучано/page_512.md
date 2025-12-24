---
source_image: page_512.png
page_number: 512
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.90
tokens: 11588
characters: 1479
timestamp: 2025-12-24T01:58:16.844279
finish_reason: stop
---

Как и раньше, пример 16.19 — это расширение одного предложения в теле delegирующего генератора:

RESULT = yield from EXPR

Пример 16.19. Псевдокод, эквивалентный предложению RESULT = yield from EXPR в delegирующем генераторе

_i = iter(EXPR) ①
try:
    _y = next(_i) ②
except StopIteration as _e:
    _r = _e.value ③
else:
    while 1: ④
        try:
            _s = yield _y ⑤
        except GeneratorExit as _e: ⑥
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
                raise _e
        except BaseException as _e: ⑦
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else: ⑧
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
            else: ⑨
                try: ⑩
                    if _s is None: ⑪
                        _y = next(_i)
                    else:
                        _y = _i.send(_s)
                except StopIteration as _e: ⑫
                    _r = _e.value
                    break
RESULT = _r ⑬

① EXPR может быть произвольным итерируемым объектом, поскольку для получения итератора _i (субгенератора) применяется метод iter().

② Субгенератор инициализирован, результат сохраняется, чтобы потом стать первым отданым значением _y.