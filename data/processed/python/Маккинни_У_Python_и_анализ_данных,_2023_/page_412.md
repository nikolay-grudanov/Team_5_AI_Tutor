---
source_image: page_412.png
page_number: 412
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.14
tokens: 7593
characters: 1566
timestamp: 2025-12-24T02:51:36.411391
finish_reason: stop
---

В качестве примера я возьму ставший уже классическим набор данных с конкурса Kaggle (https://www.kaggle.com/c/titanic), содержащий сведения о пассажирах «Титаника», затонувшего в 1912 году. Загрузим обучающий и тестовый наборы с помощью pandas:

In [87]: train = pd.read_csv('datasets/titanic/train.csv')

In [88]: test = pd.read_csv('datasets/titanic/test.csv')

In [89]: train[:4]
Out[89]:
   PassengerId  Survived  Pclass
0            1         0        3
1            2         1        1
2            3         1        3
3            4         1        1

Name                Sex  Age  SibSp
0    Braund, Mr. Owen Harris    male  22.0  1
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0  1
2      Heikkinen, Miss. Laina  female  26.0  0
3  Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0  1

Parch  Ticket  Fare  Cabin  Embarked
0      A/5 21171  7.2500  NaN  S
1      PC 17599  71.2833  C85  C
2     STON/O2. 3101282  7.9250  NaN  S
3     113803  53.1000  C123  S

Библиотеки типа statsmodels и scikit-learn, вообще говоря, не допускают подачи на вход неполных данных, поэтому посмотрим, в каких столбцах есть отсутствующие данные:

In [90]: train.isna().sum()
Out[90]:
PassengerId    0
Survived       0
Pclass         0
Name           0
Sex            0
Age            177
SibSp          0
Parch          0
Ticket         0
Fare           0
Cabin          687
Embarked       2
dtype: int64

In [91]: test.isna().sum()
Out[91]:
PassengerId    0
Pclass         0
Name           0
Sex            0
Age            86
SibSp          0