---
source_image: page_519.png
page_number: 519
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.25
tokens: 11917
characters: 2159
timestamp: 2025-12-24T01:59:09.173056
finish_reason: stop
---

Пример: применение сопрограмм для моделирования...

>>> next(taxi) ②
Event(time=0, proc=13, action='leave garage')
>>> taxi.send(_.time + 7) ③
Event(time=7, proc=13, action='pick up passenger') ④
>>> taxi.send(_.time + 23) ⑤
Event(time=30, proc=13, action='drop off passenger')
>>> taxi.send(_.time + 5) ⑥
Event(time=35, proc=13, action='pick up passenger')
>>> taxi.send(_.time + 48) ⑦
Event(time=83, proc=13, action='drop off passenger')
>>> taxi.send(_.time + 1)
Event(time=84, proc=13, action='going home') ⑧
>>> taxi.send(_.time + 10) ⑨
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration

① Создаем объект-генератор, представляющий такси с ident=13, которое сделает две поездки и начнет работать в момент t=0.
② Инициализируем сопрограмму, она отдает начальное событие.
③ Теперь можно отправить ей текущее время. В оболочке переменная _ связана с последним результатом; здесь я прибавляю 7 к текущему времени, т. е. такси потратит на поиск первого пассажира 7 минут.
④ Это событие отдается циклом for в начале первой поездки.
⑤ Отправка _.time + 23 означает, что поездка с первым пассажиром займет 23 минуты.
⑥ Затем такси будет 5 минут искать пассажира.
⑦ Последняя поездка займет 48 минут.
⑧ После завершения двух поездок цикл заканчивается и отдается событие 'going home'.
⑨ Следующая попытка послать что-то сопрограмме приводит к естественному возврату из нее. В этот момент интерпретатор возбуждает исключение StopIteration.

В примере 16.21 я использую оболочку для имитации главного цикла моделирования. Я получаю атрибут .time объекта Event, отданного сопрограммой taxi, прибавляю к нему произвольное число, и отправляю сумму методом taxi.send для возобновления сопрограммы. При моделировании все сопрограммы, представляющие такси, управляются главным циклом в методе Simulator.run. Часы модельного времени хранятся в переменной sim_time и обновляются временем каждого отданного события.

Чтобы создать экземпляр класса Simulator, функция main из скрипта taxi_sim.py строит словарь taxis:

taxis = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL)
    for i in range(num_taxis)}
    sim = Simulator(taxis)