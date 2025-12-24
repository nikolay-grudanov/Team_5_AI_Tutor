---
source_image: page_194.png
page_number: 194
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.20
tokens: 7714
characters: 2479
timestamp: 2025-12-24T00:56:24.036305
finish_reason: stop
---

194 Глава 3 • Манипуляции над данными с помощью пакета Pandas

<table>
  <tr>
    <th>1</th>
    <td>Alaska</td>
    <td>AK</td>
  </tr>
  <tr>
    <th>2</th>
    <td>Arizona</td>
    <td>AZ</td>
  </tr>
  <tr>
    <th>3</th>
    <td>Arkansas</td>
    <td>AR</td>
  </tr>
  <tr>
    <th>4</th>
    <td>California</td>
    <td>CA<sup>1</sup></td>
  </tr>
</table>

Допустим, нам нужно на основе этой информации отсортировать штаты и территорию США по плотности населения в 2010 году. Информации для этого у нас достаточно, но для достижения цели придется объединить наборы данных.

Начнем со слияния «многие-ко-многим», которое позволит получить полное имя штата в объекте DataFrame для населения. Выполнить слияние нужно на основе столбца state/region объекта pop и столбца abbreviation объекта abbrevs. Мы воспользуемся опцией how='outer', чтобы гарантировать, что не упустим никаких данных из-за несовпадения меток.

In[21]: merged = pd.merge(pop, abbrevs, how='outer',
                        left_on='state/region', right_on='abbreviation')
        merged = merged.drop('abbreviation', 1) # Удаляем дублирующуюся
                                                    # информацию
        merged.head()
Out[21]:   state/region   ages   year   population   state
           AL             under18  2012   1117489.0   Alabama
           AL             total    2012   4817528.0   Alabama
           AL             under18  2010   1130966.0   Alabama
           AL             total    2010   4785570.0   Alabama
           AL             under18  2011   1125763.0   Alabama

Следует проверить, не было ли каких-то несовпадений. Сделать это можно путем поиска строк с пустыми значениями:

In[22]: merged.isnull().any()

Out[22]: state/region    False
          ages           False
          year            False
          population      True
          state           True
          dtype: bool

Часть информации о населении отсутствует, выясним, какая именно:

In[23]: merged[merged['population'].isnull()].head()

Out[23]:   state/region   ages   year   population   state
           2448           PR     under18  1990         NaN   NaN
           2449           PR     total    1990         NaN   NaN
           2450           PR     total    1991         NaN   NaN
           2451           PR     under18  1991         NaN   NaN
           2452           PR     total    1993         NaN   NaN

1 Функция head() возвращает первые n строк набора данных. По умолчанию n = 5.