---
source_image: page_311.png
page_number: 311
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.61
tokens: 7384
characters: 1240
timestamp: 2025-12-24T02:48:30.181258
finish_reason: stop
---

Для построения таких графиков необходима библиотека SciPy. Если вы не установили ее раньше, сделайте это сейчас командой

conda install scipy

Seaborn еще упрощает построение гистограмм и графиков плотности благодаря методу histplot, который может строить одновременно гистограмму и непрерывную оценку плотности. В качестве примера рассмотрим бимодальное распределение, содержащее выборки из двух разных стандартных нормальных распределений (рис. 9.23):

In [100]: comp1 = np.random.standard_normal(200)

In [101]: comp2 = 10 + 2 * np.random.standard_normal(200)

In [102]: values = pd.Series(np.concatenate([comp1, comp2]))

In [103]: sns.histplot(values, bins=100, color="black")

![Нормированная гистограмма смеси нормальных распределений](../images/fig_9_23.png)

Рис. 9.23. Нормированная гистограмма смеси нормальных распределений

Диаграммы рассеяния
Диаграмма рассеяния, или точечная диаграмма, — полезный способ исследования соотношения между двумя одномерными рядами данных. Для демонстрации я загрузил набор данных macrodata из проекта statsmodels, выбрал несколько переменных и вычислил логарифмические разности:

In [104]: macro = pd.read_csv("examples/macrodata.csv")

In [105]: data = macro[["cpi", "m1", "tbilrate", "unemp"]]