---
source_image: page_716.png
page_number: 716
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.62
tokens: 11650
characters: 1497
timestamp: 2025-12-24T02:07:43.078409
finish_reason: stop
---

if args.couch:
    args.out.write('{}\n')
args.out.close()

if __name__ == '__main__':
    main()

1 Генераторная функция iter_iso_records читает iso-файл и отдает записи по одной.
2 Генераторная функция iter_mst_records читает mst-файл и отдает записи по одной.
3 Функция write_json обходит записи, отдаваемые генератором input_gen, и выводит json-файл.
4 Главная функция разбирает аргументы командной строки, затем...
5 ... выбирает функцию iter_iso_records или ...
6 ... функцию iter_mst_records в зависимости от расширения входного файла.
7 Выбранная генераторная функция строит объект-генератор.
8 Вызывается функция write_json, которой в первом аргументе передается генератор.

Глава 16: моделирование дискретных событий таксопарка

В примере А.6 приведен полный листинг из файла taxi_sim.py, обсуждавшегося в разделе «Моделирование работы таксопарка главы» 16.

Пример А.6. taxi_sim.py: моделирование таксопарка

"""
Моделирование такси
====================

Driving a taxi from the console::

>>> from taxi_sim import taxi_process
>>> taxi = taxi_process(ident=13, trips=2, start_time=0)
>>> next(taxi)
Event(time=0, proc=13, action='leave garage')
>>> taxi.send(_.time + 7)
Event(time=7, proc=13, action='pick up passenger')
>>> taxi.send(_.time + 23)
Event(time=30, proc=13, action='drop off passenger')
>>> taxi.send(_.time + 5)
Event(time=35, proc=13, action='pick up passenger')
>>> taxi.send(_.time + 48)
Event(time=83, proc=13, action='drop off passenger')
>>> taxi.send(_.time + 1)