---
source_image: page_718.png
page_number: 718
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.36
tokens: 11601
characters: 1892
timestamp: 2025-12-24T02:07:48.668010
finish_reason: stop
---

```python
# конец процесса такси
# END TAXI_PROCESS

# BEGIN TAXI_SIMULATOR
class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """Планирует и отображает события, пока не истечет время"""
        # планируем первое событие для каждой машины
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        # главный цикл моделирования
        sim_time = 0
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
        # END TAXI_SIMULATOR

def compute_duration(previous_action):
    """Вычисляет длительность действия, пользуясь экспоненциальным распределением"""
    if previous_action in ['leave garage', 'drop off passenger']:
        # новое состояние - поиск пассажира
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # Новое состояние - поездка
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
```