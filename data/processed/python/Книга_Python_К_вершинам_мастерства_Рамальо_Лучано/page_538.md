---
source_image: page_538.png
page_number: 538
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.45
tokens: 11901
characters: 2230
timestamp: 2025-12-24T01:59:54.723797
finish_reason: stop
---

print(msg.format(future, res)) ⑨
results.append(res)
return len(results)

1 Для этой демонстрации мы ограничимся только пятью странами с самым большим населением.
2 Устанавливаем значение max_workers равным 3, чтобы можно было следить за ожидающими будущими объектами в распечатке.
3 Обходим коды стран в алфавитном порядке, чтобы было понятно, что результаты поступают не по порядку.
4 Метод executor.submit планирует выполнение вызываемого объекта и возвращает объект future, представляющий ожидаемую операцию.
5 Сохраняем каждый будущий объект, чтобы впоследствии его можно было извлечь с помощью функции as_completed.
6 Выводим сообщение, содержащее код страны и соответствующий ему будущий объект future.
7 as_completed отдает будущие объекты по мере их завершения.
8 Получаем результат этого объекта future.
9 Отображаем объект future и результат его выполнения.

Отметим, что вызов future.result() в этом примере никогда не приводит к блокировке, потому что будущий объект получен как результат as_completed. В примере 17.5 показан результат одного прохождения программы из примера 17.4.

Пример 17.5. Результат работы скрипта flags_threadpool_ac.py

$ python3 flags_threadpool_ac.py
Scheduled for BR: <Future at 0x100791518 state=running> ①
Scheduled for CN: <Future at 0x100791710 state=running>
Scheduled for ID: <Future at 0x100791a90 state=running>
Scheduled for IN: <Future at 0x101807080 state=pending> ②
Scheduled for US: <Future at 0x101807128 state=pending>
CN <Future at 0x100791710 state=finished returned str> result: 'CN' ③
BR ID <Future at 0x100791518 state=finished returned str> result: 'BR' ④
<Future at 0x100791a90 state=finished returned str> result: 'ID'
IN <Future at 0x101807080 state=finished returned str> result: 'IN'
US <Future at 0x101807128 state=finished returned str> result: 'US'

5 flags downloaded in 0.70s

1 Будущие объекты планируются в алфавитном порядке; метод repr() будущего объекта показывает его состояние: первые три объекта выполняются, поскольку есть всего три рабочих потока.
2 Последние два будущих объекта ожидают освобождения рабочего потока.
3 Первое слово CN напечатано функцией download_one, исполняемой в рабочем потоке, остаток строки напечатан функцией download_many.