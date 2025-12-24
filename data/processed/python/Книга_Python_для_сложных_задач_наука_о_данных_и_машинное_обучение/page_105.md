---
source_image: page_105.png
page_number: 105
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.93
tokens: 7580
characters: 1880
timestamp: 2025-12-24T00:54:19.241732
finish_reason: stop
---

In[26]: x

Out[26]: array([[5, 0, 3, 3],
                [7, 9, 3, 5],
                [2, 4, 7, 6]])

Как мы уже видели, можно легко получить булев массив для этого условия:

In[27]: x < 5

Out[27]: array([[False,  True,  True,  True],
                [False, False,  True, False],
                [ True,  True, False, False]], dtype=bool)

Чтобы выбрать нужные значения из массива, достаточно просто проиндексировать исходный массив x по этому булеву массиву. Такое действие носит название операции наложения маски или маскирования:

In[28]: x[x < 5]

Out[28]: array([0, 3, 3, 3, 2, 4])

При этом был возвращен одномерный массив, заполненный всеми значениями, удовлетворяющими нашему условию. Другими словами, все значения, находящиеся в массиве x на позициях, на которых в массиве-маске находятся значения True.

После этого можно поступать с этими значениями так, как нам будет нужно. Например, можно вычислить какой-нибудь соответствующий статистический показатель на наших данных о дождях в Сиэтле:

In[29]:
# создаем маску для всех дождливых дней
rainy = (inches > 0)
# создаем маску для всех летних дней (21 июня¹ – 172-й день)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)

print("Median precip on rainy days in 2014 (inches): ", np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches): ", np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ", np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):", np.median(inches[rainy & ~summer]))

Median precip on rainy days in 2014 (inches): 0.194881889764
Median precip on summer days in 2014 (inches): 0.0
Maximum precip on summer days in 2014 (inches): 0.850393700787
Median precip on non-summer rainy days (inches): 0.200787401575

¹ Астрономическое лето в Северном полушарии начинается 21 июня, в день летнего солнцестояния.