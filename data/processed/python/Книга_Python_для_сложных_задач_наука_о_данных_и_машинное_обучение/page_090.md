---
source_image: page_090.png
page_number: 90
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.48
tokens: 7608
characters: 1860
timestamp: 2025-12-24T00:53:54.842135
finish_reason: stop
---

Пример: чему равен средний рост президентов США

Имеющиеся в библиотеке NumPy функции агрегирования могут очень пригодиться для обобщения набора значений. В качестве простого примера рассмотрим рост всех президентов США. Эти данные доступны в файле president_heights.csv, представляющем собой простой разделенный запятыми список меток и значений:

In[13]: !head -4 data/president_heights.csv

order,name,height(cm)
1,George Washington,189
2,John Adams,170
3,Thomas Jefferson,189

Мы воспользуемся пакетом Pandas, который изучим более детально в главе 3, для чтения файла и извлечения данной информации (обратите внимание, что рост указан в сантиметрах):

In[14]: import pandas as pd
    data = pd.read_csv('data/president_heights.csv')
    heights = np.array(data['height(cm)'])
    print(heights)

[189 170 189 163 183 171 185 168 173 183 173 173 175 178 183 193 178 173
 174 183 183 168 170 178 182 180 183 178 182 188 175 179 183 193 182 183
 177 185 188 188 182 185]

Теперь, получив такой массив данных, мы можем вычислить множество сводных статистических показателей:

In[15]: print("Mean height:      ", heights.mean())
    print("Standard deviation:", heights.std())
    print("Minimum height:     ", heights.min())
    print("Maximum height:     ", heights.max())

Mean height:      179.738095238
Standard deviation:   6.93184344275
Minimum height:     163
Maximum height:     193

Обратите внимание, что в каждом случае операция агрегирования редуцирует весь массив к одному итоговому значению, дающему нам информацию о распределении значений. Возможно, нам захочется также вычислить квантили:

In[16]: print("25th percentile:   ", np.percentile(heights, 25))
    print("Median:            ", np.median(heights))
    print("75th percentile:   ", np.percentile(heights, 75))

25th percentile:   174.25
Median:            182.0
75th percentile:   183.0