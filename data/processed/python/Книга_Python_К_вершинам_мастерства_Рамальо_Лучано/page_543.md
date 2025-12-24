---
source_image: page_543.png
page_number: 543
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.10
tokens: 11879
characters: 2228
timestamp: 2025-12-24T02:00:11.740171
finish_reason: stop
---

Эксперименты с Executor.map

```python
msg = '{}loiter({}): doing nothing for {}s...'
display(msg.format('\t'*n, n, n))
sleep(n)
msg = '{}loiter({}): done.'
display(msg.format('\t'*n, n))
return n * 10  # 3

def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)  # 4
    results = executor.map(loiter, range(5))  # 5
    display('results:', results) # 6
    display('Waiting for individual results:')
    for i, result in enumerate(results):  # 7
        display('result {}: {}'.format(i, result))

main()
```

1 Эта функция печатает переданные ей аргументы, добавляя временнную метку в формате [HH:MM:SS].
2 Функция loiter печатает время начала работы, затем спит n секунд и печатает время окончания; знаки табуляции формируют отступ сообщения в соответствии с величиной n.
3 loiter возвращает n * 10, чтобы нагляднее представить результаты.
4 Создаем объект ThreadPoolExecutor с тремя потоками.
5 Передаем исполнителю executor пять задач (поскольку есть только три потока, сразу начнут выполнение лишь три из них: вызывающие loiter(0), loiter(1) и loiter(2)); это неблокирующий вызов.
6 Немедленно распечатываем объект results, полученный от executor.map: это генератор, как видно из результатов, показанных в примере 17.7.
7 Обращение к enumerate в цикле for неявно вызывает функцию next(results), которая, в свою очередь вызывает метод _f.result() (внутреннего) будущего объекта _f, представляющего первый вызов, loiter(0). Метод result блокирует программу до завершения будущего объекта, поэтому каждая итерация этого цикла будет ждать готовности следующего результата.

Призываю вас прогнать пример 17.6 и полюбоваться на то, как постепенно печатаются сообщения. А заодно уж поэкспериментируйте с аргументом max_workers объекта ThreadPoolExecutor и с функцией range, которая порождает аргументы для обращения к executor.map, — или замените ее списками подобраных вручную значений, если хотите задать другие задержки.

В примере 17.7 показаны результаты прогона программы из примера 17.6.

Пример 17.7. Результаты прогона скрипта demo_executor_map.py из примера 17.6

$ python3 demo_executor_map.py
[15:56:50] Script starting. ①
[15:56:50] loiter(0): doing nothing for 0s... ②