---
source_image: page_522.png
page_number: 522
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.60
tokens: 11787
characters: 2231
timestamp: 2025-12-24T01:59:01.253323
finish_reason: stop
---

```python
while sim_time < end_time:
    if self.events.empty():
        print('*** end of events ***')
        break

    current_event = self.events.get()
    sim_time, proc_id, previous_action = current_event
    print('taxi:', proc_id, proc_id * ' ', current_event)
    active_proc = self.procs[proc_id]
    next_time = sim_time + compute_duration(previous_action)
    try:
        next_event = active_proc.send(next_time)
    except StopIteration:
        del self.procs[proc_id]
    else:
        self.events.put(next_event)
else:
    msg = '*** end of simulation time: {} events pending ***'
    print(msg.format(self.events.qsize()))
```

1 Окончание модельного времени end_time — единственный обязательный аргумент run.
2 Используем функцию sorted для выборки элементов self.procs, упорядоченных по ключу; сам ключ нам не важен, поэтому присваиваем его переменной _.
3 Вызов next(proc) инициализирует каждую сопрограмму, заставляя ее дойти до первого предложения yield, после чего ей можно посылать данные. Отдается объект Event.
4 Помещаем каждое событие в очередь с приоритетами self.events. Первым событием для каждого такси является 'leave garage', как видно из распечатки демонстрационного прогона (пример 16.20).
5 Обнуляем часы модельного времени sim_time.
6 Главный цикл моделирования: выполнять, пока sim_time меньше end_time.
7 Выход из главного цикла производится и тогда, когда в очереди не осталось событий.
8 Получаем из очереди объект Event с наименьшим значением time; присваиваем его переменной current_event.
9 Распаковываем кортеж Event. В этой строке часы модельного времени sim_time приводятся в соответствии с временем события15.
10 Распечатываем объект Event: выводим идентификатор такси и соответствующий ему отступ.
11 Извлекаем сопрограмму для активного такси из словаря self.procs.
12 Вычисляем время следующего возобновления, складывая sim_time и результат вызова функции compute_duration(...) для предыдущего действия (т.е. 'pick up passenger', 'drop off passenger' и т.д.)

15 Это типично для моделирования дискретных событий: часы модельного времени не увеличиваются на фиксированную величину на каждой итерации цикла, а сдвигаются в соответствии с продолжительностью закончившегося события.