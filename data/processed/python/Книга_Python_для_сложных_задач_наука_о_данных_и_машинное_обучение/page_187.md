---
source_image: page_187.png
page_number: 187
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.71
tokens: 7454
characters: 2067
timestamp: 2025-12-24T00:56:05.738193
finish_reason: stop
---

содержит повторяющиеся значения, результат окажется слиянием типа «многие-ко-многим». Рассмотрим следующий пример, в котором объект DataFrame отражает один или несколько навыков, соответствующих конкретной группе.

Выполнив соединение «многие-ко-многим», можно выяснить навыки каждого конкретного человека:

In[5]: df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                                    'Engineering', 'Engineering',
                                    'HR', 'HR'],
                        'skills': ['math', 'spreadsheets', 'coding',
                                   'linux',
                                   'spreadsheets', 'organization']})
print(df1); print(df5); print(pd.merge(df1, df5))

df1
   employee    group
0      Bob  Accounting
1     Jake  Engineering
2     Lisa  Engineering
3      Sue         HR

df5
   group    skills
0  Accounting    math
1  Accounting  spreadsheets
2 Engineering    coding
3 Engineering    linux
4           HR  spreadsheets
5           HR organization

pd.merge(df1, df5)
   employee    group    skills
0      Bob  Accounting    math
1      Bob  Accounting  spreadsheets
2     Jake  Engineering    coding
3     Jake  Engineering    linux
4     Lisa  Engineering    coding
5     Lisa  Engineering    linux
6      Sue         HR  spreadsheets
7      Sue         HR organization

Эти три типа соединений можно использовать и в других инструментах библиотеки Pandas, что дает возможность реализовать широкий диапазон функциональности. Однако на практике наборы данных редко оказываются такими же «чистыми», как те, с которыми мы имели дело. В следующем разделе мы рассмотрим параметры метода pd.merge(), позволяющие более тонко описывать желаемое поведение операций соединения.

Задание ключа слияния

Мы рассмотрели поведение метода pd.merge() по умолчанию: он выполняет поиск в двух входных объектах соответствующих названий столбцов и использует найденное в качестве ключа. Однако зачастую имена столбцов не совпадают добуквенно точно, и в методе pd.merge() имеется немало параметров для такой ситуации.