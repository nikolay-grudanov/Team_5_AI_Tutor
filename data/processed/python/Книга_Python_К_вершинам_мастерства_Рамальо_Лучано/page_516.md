---
source_image: page_516.png
page_number: 516
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 66.52
tokens: 12279
characters: 3229
timestamp: 2025-12-24T01:59:12.765238
finish_reason: stop
---

нет понимание того, как библиотеки типа asyncio, Twisted и Tornado ухитряются управлять многочисленными параллельными операциями в одном потоке выполнения.

Моделирование работы таксопарка

В нашей программе моделирования taxi_sim.py создается несколько экземпляров такси. Каждое такси совершает фиксированное количество поездок и возвращается в гараж. Такси выезжает из гаража и начинает «рыскать» — искать пассажира. Это продолжается, пока пассажир не сядет в такси, в этот момент начинается поездка. Когда пассажир выходит, такси возвращается в режим поиска.

Время поиска и поездок имеет экспоненциальное распределение. Для простоты отображения время измеряется в минутах, но для моделирования можно применять и интервалы типа float12. Всякое изменение состояния любого такси выводится как событие. На рис. 16.3 показан пример прогона программы.

$ python3 taxi_sim.py -s 3
taxi: 0 Event(time=0, proc=0, action='leave garage')
taxi: 0 Event(time=2, proc=0, action='pick up passenger')
taxi: 1 Event(time=5, proc=1, action='leave garage')
taxi: 1 Event(time=8, proc=1, action='pick up passenger')
taxi: 2 Event(time=10, proc=2, action='leave garage')
taxi: 2 Event(time=15, proc=2, action='pick up passenger')
taxi: 2 Event(time=17, proc=2, action='drop off passenger')
taxi: 0 Event(time=18, proc=0, action='drop off passenger')
taxi: 2 Event(time=18, proc=2, action='pick up passenger')
taxi: 2 Event(time=25, proc=2, action='drop off passenger')
taxi: 1 Event(time=27, proc=1, action='drop off passenger')
taxi: 2 Event(time=27, proc=2, action='pick up passenger')
taxi: 0 Event(time=28, proc=0, action='pick up passenger')
taxi: 2 Event(time=40, proc=2, action='drop off passenger')
taxi: 2 Event(time=44, proc=2, action='pick up passenger')
taxi: 1 Event(time=55, proc=1, action='pick up passenger')
taxi: 1 Event(time=59, proc=1, action='drop off passenger')
taxi: 0 Event(time=65, proc=0, action='drop off passenger')
taxi: 1 Event(time=65, proc=1, action='pick up passenger')
taxi: 2 Event(time=65, proc=2, action='drop off passenger')
taxi: 2 Event(time=72, proc=2, action='pick up passenger')
taxi: 0 Event(time=76, proc=0, action='going home')
taxi: 1 Event(time=80, proc=1, action='drop off passenger')
taxi: 1 Event(time=88, proc=1, action='pick up passenger')
taxi: 2 Event(time=95, proc=2, action='drop off passenger')
taxi: 2 Event(time=97, proc=2, action='pick up passenger')
taxi: 2 Event(time=98, proc=2, action='drop off passenger')
taxi: 1 Event(time=106, proc=1, action='drop off passenger')
taxi: 2 Event(time=109, proc=2, action='going home')
taxi: 1 Event(time=110, proc=1, action='going home')
*** end of events ***

Рис. 16.3. Пример прогона скрипта taxi_sim.py при трех такси. Аргумент -s 3 инициализирует генератор случайных чисел, так что поведение программы можно воспроизвести для отладки и демонстрации. Стрелками показаны поездки

12 Я не специалист по работе таксопарка, поэтому не принимайте приведенные ниже числа всерьез. Экспоненциальное распределение часто применяется в DES. Некоторые поездки оказались очень короткими. Представьте, что выдался дождливый денек, и некоторые пассажиры берут такси, чтобы проехать всего один квартал — в идеальном городе, где в дождь можно поймать такси.