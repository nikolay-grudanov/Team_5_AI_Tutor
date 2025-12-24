---
source_image: page_188.png
page_number: 188
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.54
tokens: 7515
characters: 1781
timestamp: 2025-12-24T00:56:07.842519
finish_reason: stop
---

Ключевое слово on

Проще всего указать название ключевого столбца с помощью ключевого слова on, в котором указывается название или список названий столбцов:

In[6]: print(df1); print(df2); print(pd.merge(df1, df2, on='employee'))

df1
   employee    group
0     Bob  Accounting
1    Jake  Engineering
2    Lisa  Engineering
3     Sue        HR

df2
   employee  hire_date
0      Lisa       2004
1      Bob       2008
2     Jake       2012
3     Sue       2014

pd.merge(df1, df2, on='employee')
   employee    group  hire_date
0     Bob  Accounting      2008
1    Jake  Engineering     2012
2    Lisa  Engineering     2004
3     Sue        HR        2014

Этот параметр работает только в том случае, когда в левом и правом объектах DataFrame имеется указанное название столбца.

Ключевые слова left_on и right_on

Иногда приходится выполнять слияние двух наборов данных с различными именами столбцов. Например, у нас может быть набор данных, в котором столбец для имени служащего называется Name, а не Employee. В этом случае можно воспользоваться ключевыми словами left_on и right_on для указания названий двух нужных столбцов:

In[7]:
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                   'salary': [70000, 80000, 120000, 90000]})
print(df1); print(df3);
print(pd.merge(df1, df3, left_on="employee", right_on="name"))

df1
   employee    group
0     Bob  Accounting
1    Jake  Engineering
2    Lisa  Engineering
3     Sue        HR

df3
   name  salary
0   Bob   70000
1  Jake   80000
2  Lisa  120000
3  Sue   90000

pd.merge(df1, df3, left_on="employee", right_on="name")
   employee    group   name  salary
0     Bob  Accounting   Bob   70000
1    Jake  Engineering  Jake   80000
2    Lisa  Engineering  Lisa  120000
3     Sue        HR     Sue   90000