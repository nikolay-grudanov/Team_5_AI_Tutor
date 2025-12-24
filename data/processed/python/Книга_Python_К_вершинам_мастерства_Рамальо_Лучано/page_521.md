---
source_image: page_521.png
page_number: 521
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.77
tokens: 11832
characters: 2144
timestamp: 2025-12-24T01:59:01.962631
finish_reason: stop
---

Пример: применение сопрограмм для моделирования...

Это означает, что такси 0 потребуется 14 минут для поиска первого пассажира, а такси 1, которое выехало из гаража в момент time=10, — всего 1 минуту, первый пассажир сядет в момент time=11. Если эти два события находятся в очереди, то первым главный цикл извлечет событие Event (time=11, proc=1, action='pick up passenger').

Теперь рассмотрим основной алгоритм моделирования, метод Simulator.run. Он вызывается из функции main сразу после создания объекта Simulator:

sim = Simulator(taxis)
sim.run(end_time)

В примере 16.23 приведен полный текст класса Simulator с аннотациями, а пока дадим общий обзор алгоритма:

1. Цикл по процессам, представляющим такси.
   a. Инициализировать сопрограмму для каждого такси, вызвав для нее функцию next(). В ответ будет отдано первое событие для такси.
   b. Поместить каждое событие в очередь self.events объекта Simulator.

2. Выполнять главный цикл моделирования, пока sim_time < end_time.
   a. Проверить, пуста ли очередь self.events; если да, выйти из цикла.
   b. Получить из self.events текущее событие current_event. Это будет объект Event с наименьшим временем.
   c. Вывести Event.
   d. Обновить модельное время, присвоив ему значение атрибута time объекта current_event.
   e. Отправить время сопрограмме, определяемой атрибутом proc объекта current_event. Сопрограмма отдаст следующее событие next_event.
   f. Запланировать next_event, поместив его в очередь self.events.

Полный текст класса Simulator приведен в примере 16.23.

Пример 16.23. taxi_sim.py: Simulator, простейший класс моделирования дискретных событий, наиболее интересен метод run

class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time): ①
        """Планировать и отображать события, пока не истечет время"""
        # Запланировать первое событие для каждого такси
        for _, proc in sorted(self.procs.items()): ②
            first_event = next(proc) ③
            self.events.put(first_event) ④

        # главный цикл моделирования
        sim_time = 0 ⑤