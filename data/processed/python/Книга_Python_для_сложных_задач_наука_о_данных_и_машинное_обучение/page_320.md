---
source_image: page_320.png
page_number: 320
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.67
tokens: 7651
characters: 2145
timestamp: 2025-12-24T00:59:52.714160
finish_reason: stop
---

Matplotlib, поэтому вместо перечисления их я просто покажу несколько возможностей. Продемонстрируем часть имеющихся параметров на уже знакомом вам графике рождаемости (рис. 4.72):

In[8]:
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)

# Добавляем на график метки
ax.annotate("New Year's Day", xy=('2012-1-1', 4100), xycoords='data',
    xytext=(50, -30), textcoords='offset points',
    arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3,rad=-0.2"))

ax.annotate("Independence Day", xy=('2012-7-4', 4250), xycoords='data',
    bbox=dict(boxstyle="round", fc="none", ec="gray"),
    xytext=(10, -40), textcoords='offset points', ha='center',
    arrowprops=dict(arrowstyle="->"))

ax.annotate('Labor Day', xy=('2012-9-4', 4850), xycoords='data', ha='center',
    xytext=(0, -20), textcoords='offset points')
ax.annotate('', xy=('2012-9-1', 4850), xytext=('2012-9-7', 4850),
    xycoords='data', textcoords='data',
    arrowprops={'arrowstyle': '|-|,widthA=0.2,widthB=0.2', })

ax.annotate('Halloween', xy=('2012-10-31', 4600), xycoords='data',
    xytext=(-80, -40), textcoords='offset points',
    arrowprops=dict(arrowstyle="fancy",
        fc="0.6", ec="none",
        connectionstyle="angle3,angleA=0,angleB=-90"))

ax.annotate('Thanksgiving', xy=('2012-11-25', 4500), xycoords='data',
    xytext=(-120, -60), textcoords='offset points',
    bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
    arrowprops=dict(arrowstyle="->",
        connectionstyle="angle,angleA=0,angleB=80,rad=20"))

ax.annotate('Christmas', xy=('2012-12-25', 3850), xycoords='data',
    xytext=(-30, 0), textcoords='offset points',
    size=13, ha='right', va="center",
    bbox=dict(boxstyle="round", alpha=0.1),
    arrowprops=dict(arrowstyle="wedge, tail_width=0.5",
        alpha=0.1));

# Задаем метки для осей координат
ax.set(title='USA births by day of year (1969-1988)',
    ylabel='average daily births')

# Размещаем ось X центрированными метками для месяцев
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())