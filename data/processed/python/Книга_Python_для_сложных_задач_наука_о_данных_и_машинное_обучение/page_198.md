---
source_image: page_198.png
page_number: 198
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.36
tokens: 7817
characters: 2072
timestamp: 2025-12-24T00:56:43.101816
finish_reason: stop
---

Данные о планетах

Воспользуемся набором данных «Планеты» (Planets), доступным через пакет Seaborn (см. раздел «Визуализация с помощью библиотеки Seaborn» главы 4). Он включает информацию об открытых астрономами планетах, вращающихся вокруг других звезд, известных под названием внесолнечных планет или экзопланет (exoplanets). Скачать его можно с помощью команды пакета Seaborn:

In[2]: import seaborn as sns
    planets = sns.load_dataset('planets')
    planets.shape

Out[2]: (1035, 6)

In[3]: planets.head()

<table>
  <tr>
    <th>method</th>
    <th>number</th>
    <th>orbital_period</th>
    <th>mass</th>
    <th>distance</th>
    <th>year</th>
  </tr>
  <tr>
    <td>Radial Velocity</td>
    <td>1</td>
    <td>269.300</td>
    <td>7.10</td>
    <td>77.40</td>
    <td>2006</td>
  </tr>
  <tr>
    <td>Radial Velocity</td>
    <td>1</td>
    <td>874.774</td>
    <td>2.21</td>
    <td>56.95</td>
    <td>2008</td>
  </tr>
  <tr>
    <td>Radial Velocity</td>
    <td>1</td>
    <td>763.000</td>
    <td>2.60</td>
    <td>19.84</td>
    <td>2011</td>
  </tr>
  <tr>
    <td>Radial Velocity</td>
    <td>1</td>
    <td>326.030</td>
    <td>19.40</td>
    <td>110.62</td>
    <td>2007</td>
  </tr>
  <tr>
    <td>Radial Velocity</td>
    <td>1</td>
    <td>516.220</td>
    <td>10.50</td>
    <td>119.47</td>
    <td>2009</td>
  </tr>
</table>

Этот набор данных содержит определенную информацию о более чем 1000 экзопланет, открытых до 2014 года.

Простое агрегирование в библиотеке Pandas

Ранее мы рассмотрели некоторые доступные для массивов NumPy возможности по агрегированию данных (см. раздел «Агрегирование: минимум, максимум и все, что посередине» главы 2). Как и в случае одномерных массивов библиотеки NumPy, для объектов Series библиотеки Pandas агрегирующие функции возвращают скалярное значение:

In[4]: rng = np.random.RandomState(42)
    ser = pd.Series(rng.rand(5))
    ser

Out[4]: 0    0.374540
        1    0.950714
        2    0.731994
        3    0.598658
        4    0.156019
    dtype: float64

In[5]: ser.sum()

Out[5]: 2.8119254917081569