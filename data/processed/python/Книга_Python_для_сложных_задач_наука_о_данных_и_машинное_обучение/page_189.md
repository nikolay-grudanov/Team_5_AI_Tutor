---
source_image: page_189.png
page_number: 189
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.45
tokens: 7408
characters: 1572
timestamp: 2025-12-24T00:56:00.749162
finish_reason: stop
---

Результат этой операции содержит избыточный столбец, который можно при желании удалить. Например, с помощью имеющегося в объектах DataFrame метода drop( ):

In[8]:
pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1)

Out[8]:    employee    group    salary
           0      Bob   Accounting   70000
           1     Jake   Engineering   80000
           2     Lisa   Engineering  120000
           3      Sue         HR      90000

Ключевые слова left_index и right_index

Иногда удобнее вместо слияния по столбцу выполнить слияние по индексу. Допустим, у нас имеются следующие данные:

In[9]: df1a = df1.set_index('employee')
       df2a = df2.set_index('employee')
       print(df1a); print(df2a)

df1a
employee    group
Bob        Accounting
Jake      Engineering
Lisa     Engineering
Sue            HR

df2a
employee    hire_date
Lisa          2004
Bob            2008
Jake          2012
Sue            2014

Можно использовать индекс в качестве ключа слияния путем указания в методе pd.merge() флагов left_index и/или right_index:

In[10]:
print(df1a); print(df2a);
print(pd.merge(df1a, df2a, left_index=True, right_index=True))

df1a
employee    group
Bob        Accounting
Jake      Engineering
Lisa     Engineering
Sue            HR

df2a
employee    hire_date
Lisa          2004
Bob            2008
Jake          2012
Sue            2014

pd.merge(df1a, df2a, left_index=True, right_index=True)
    group    hire_date
employee
Lisa    Engineering    2004
Bob     Accounting     2008
Jake    Engineering    2012
Sue     HR             2014