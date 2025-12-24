---
source_image: page_370.png
page_number: 370
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.62
tokens: 7662
characters: 1963
timestamp: 2025-12-24T01:01:05.007921
finish_reason: stop
---

По умолчанию библиотека Pandas загружает столбцы с временем как строки Python (тип object), убедиться в этом можно, посмотрев значение атрибута dtypes объекта DataFrame:

In[24]: data.dtypes

Out[24]: age      int64
          gender   object
          split    object
          final    object
          dtype: object

Исправим это, создав функцию для преобразования значений времени:

In[25]: def convert_time(s):
        h, m, s = map(int, s.split(':'))
        return pd.datetools.timedelta(hours=h, minutes=m, seconds=s)
data = pd.read_csv('marathon-data.csv',
                   converters={'split':convert_time,
                               'final':convert_time})
data.head()

Out[25]:    age  gender  split         final
           0   33      M 01:05:3802:08:51
           1   32      M 01:06:2602:09:28
           2   31      M 01:06:4902:10:42
           3   38      M 01:06:1602:13:45
           4   31      M 01:06:3202:13:59

In[26]: data.dtypes

Out[26]: age      int64
          gender   object
          split    timedelta64[ns]
          final    timedelta64[ns]
          dtype: object

Выглядит намного лучше. Добавим для использования при построении графиков столбцы с временем в секундах¹:

In[27]: data['split_sec'] = data['split'].astype(int) / 1E9
        data['final_sec'] = data['final'].astype(int) / 1E9
        data.head()

Out[27]:    age  gender  split         final  split_sec  final_sec
           0   33      M 01:05:3802:08:51     3938.0     7731.0
           1   32      M 01:06:2602:09:28     3986.0     7768.0
           2   31      M 01:06:4902:10:42     4009.0     7842.0
           3   38      M 01:06:1602:13:45     3976.0     8025.0
           4   31      M 01:06:3202:13:59     3992.0     8039.0

¹ При работе в командной оболочке IPython в 64-битной операционной системе Windows может возникнуть ошибка преобразования типа. Один из путей решения этой проблемы — использовать в следующем коде тип np.int64 вместо int.