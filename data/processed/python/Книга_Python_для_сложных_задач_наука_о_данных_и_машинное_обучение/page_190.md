---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.25
tokens: 7431
characters: 1554
timestamp: 2025-12-24T00:56:01.755299
finish_reason: stop
---

Для удобства в объектах DataFrame реализован метод join(), выполняющий по умолчанию слияние по индексам:

In[11]: print(df1a); print(df2a); print(df1a.join(df2a))

df1a
employee    group
Bob         Accounting
Jake        Engineering
Lisa        Engineering
Sue         HR

df2a
employee    hire_date
Lisa        2004
Bob         2008
Jake        2012
Sue         2014

df1a.join(df2a)
group    hire_date
employee
Bob      Accounting   2008
Jake     Engineering  2012
Lisa     Engineering  2004
Sue      HR           2014

Если требуется комбинация слияния по столбцам и индексам, можно для достижения нужного поведения воспользоваться сочетанием флага left_index с параметром right_on или параметра left_on с флагом right_index:

In[12]:
print(df1a); print(df3);
print(pd.merge(df1a, df3, left_index=True, right_on='name'))

df1a
employee    group
Bob         Accounting
Jake        Engineering
Lisa        Engineering
Sue         HR

df3
name    salary
Bob     70000
Jake    80000
Lisa    120000
Sue     90000

pd.merge(df1a, df3, left_index=True, right_on='name')
    group    name    salary
0    Accounting    Bob    70000
1    Engineering   Jake    80000
2    Engineering   Lisa   120000
3    HR            Sue    90000

Все эти параметры работают и в случае нескольких индексов и/или столбцов, синтаксис для этого интуитивно понятен. Более подробную информацию по этому вопросу см. в разделе Merge, Join and Concatenate («Слияние, соединение и конкатенация», http://pandas.pydata.org/pandas-docs/stable/merging.html) документации библиотеки Pandas.