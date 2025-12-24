---
source_image: page_504.png
page_number: 504
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.12
tokens: 11982
characters: 2682
timestamp: 2025-12-24T01:58:27.328592
finish_reason: stop
---

**дегерирующий генератор**
Генераторная функция, содержащая выражение yield from <iterable>.

**субгенератор**
Генератор, полученный от итерируемого объекта <iterable> в выражении yield from. Это именно тот «субгенератор», который упомянут в заглавии документа PEP 380: «Syntax for Delegating to a Subgenerator».

**вызывающая сторона**
В PEP 380 термином «вызывающая сторона» обозначается клиентский код, который вызывает делегирующий генератор. В зависимости от контекста я иногда использую слово «клиент» вместо «вызывающая сторона», чтобы не путать с делегирующим генератором, который тоже является «вызывающей стороной» (он вызывает субгенератор).

В документе PEP 380 часто для обозначения субгенератора используется слово «итератор». Это только запутывает ситуацию, потому что делегирующий генератор также является итератором. Поэтому я предпочитаю термин «субгенератор», согласующийся с названием PEP – «Syntax for Delegating to a Subgenerator». Однако субгенератор может быть простым итератором, реализующим только метод __next__, а yield from может работать и в этом случае, хотя задумывалась для поддержки генераторов, реализующих методы __next__, send, close и throw.

В примере 16.17 показан более полный контекст для применения yield from, а на рис 16.2 — важные части этого примера7.

<table>
  <tr>
    <th>вызывающая сторона</th>
    <th>делегирующий генератор</th>
    <th>субгенератор</th>
  </tr>
  <tr>
    <td>main</td>
    <td>grouper</td>
    <td>averager</td>
  </tr>
  <tr>
    <td>
      def main(data):
        results = {}
        for key, values in data.items():
          group = grouper(results, key)
          next(group)
          for value in values:
            group.send(value)
            group.close()
        report(results)
    </td>
    <td>
      def grouper(results, key):
        while True:
          results[key] = yield from averager()
    </td>
    <td>
      def averager():
        total = 0.0
        count = 0
        average = None
        while True:
          term = yield
          if term is None:
            break
          total += term
          count += 1
          average = total / count
          yield Result(count, average)
    </td>
  </tr>
</table>

Рис. 16.2. Пока делегирующий генератор приостановлен в yield from, вызывающая сторона отправляет данные напрямую субгенератору, который отдает данные вызывающей стороне. Выполнение делегирующего генератора возобновляется, когда субгенератор возвращает управление и интерпретатор возбуждает исключение StopIteration с присоединенным к нему возвращенным значением

7 Рисунок 16.2 основан на диаграмме Пола Соколовского (http://flupy.org/resources/yield-from.pdf).