---
source_image: page_380.png
page_number: 380
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.93
tokens: 11920
characters: 2001
timestamp: 2025-12-24T01:52:26.358947
finish_reason: stop
---

Глава 12. Наследование: хорошо или плохо

Однако безопаснее и в большей степени совместимо с будущими версиями пользоваться функцией super(), особенно при вызове методов каркаса или любой не контролируемой вами иерархии классов. В примере 12.6 показано, что функция super() следует порядку MRO при вызове метода.

Пример 12.6. Использование super() для вызова ping (для примера 12.4)

```python
>>> from diamond import D
>>> d = D()
>>> d.ping() # ①
ping: <diamond.D object at 0x10cc40630> # ②
post-ping: <diamond.D object at 0x10cc40630> # ③
```

① Метод ping из D делает два вызова
② Первый вызов — super().ping(); super делегирует вызов ping классу A; A.ping выводит эту строку.
③ Второй вызов — print('post-ping:', self), он выводит эту строку.

Теперь посмотрим, что происходит, когда pingpong вызывается от имени экземпляра класса D.

Пример 12.7. Пять вызовов, выполненных методом pingpong (для примера 12.4)

```python
>>> from diamond import D
>>> d = D()
>>> d.pingpong()
>>> d.pingpong()
ping: <diamond.D object at 0x10bf235c0> # ①
post-ping: <diamond.D object at 0x10bf235c0>
ping: <diamond.D object at 0x10bf235c0> # ②
pong: <diamond.D object at 0x10bf235c0> # ③
pong: <diamond.D object at 0x10bf235c0> # ④
PONG: <diamond.D object at 0x10bf235c0> # ⑤
```

① Вызов 1 — self.ping(), выполняется метод ping класса D, который выводит эту и следующую строку.
② Вызов 2 — super.ping(), пропускает ping из D и находит метод ping в A.
③ Вызов 3 — self.pong(), находит в B реализацию pong в соответствии с __mro__.
④ Вызов 4 — super.pong(), находит ту же самую реализацию в pong, также следуя __mro__.
⑤ Вызов 5 — C.pong(self), находит реализацию C.pong, игнорируя __mro__.

Порядок MRO принимает в расчет не только граф наследования, но также порядок, в котором перечислены суперклассы в объявлении подкласса. Иными словами, если бы в файле diamond.py (пример 12.4) класс D был объявлен как class D(C, B):, то __mro__ класса D был бы другим: поиск производился бы сначала в классе C, а потом в B.